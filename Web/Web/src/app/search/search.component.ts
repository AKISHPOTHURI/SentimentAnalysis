import { Component, ElementRef, OnInit, ViewChild } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';
import * as XLSX from "xlsx";
import { AnalysisService } from '../services/analysis.service';
import {ExportAsConfig, ExportAsService } from 'ngx-export-as';


@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.scss']
})
export class SearchComponent implements OnInit {

  @ViewChild('content') content !:ElementRef;

  graphPercentage: number = 75;
  singleDataForm  !: FormGroup;
  showFileUpload: boolean = false;
  data: any
  showSingleResponse: boolean = true;
  showBulletComponent: boolean = false;
  isloading: boolean = false
  givenData: any;
  singleDataResult: any = {
    sentiment: 1, 
    prob: 0.75, 
  };  
  fileValue: any;
  multipleDataResult: any;
  constructor(private _service: AnalysisService,private exportAsService: ExportAsService) {
  }
  ngOnInit() {
    this.singleDataForm = new FormGroup({
      text: new FormControl('')
    });
  }
  
  exportAsConfig: ExportAsConfig = {
    type: 'pdf', 
    elementIdOrContent: 'htmlData',
  }
  


  SavePDF(){ {
      this.exportAsService.save(this.exportAsConfig, 'data').subscribe(() => {
      });
      this.exportAsService.get(this.exportAsConfig).subscribe(content => {
        console.log(content);
      });
    }
  }
  
  onLoading(form: FormGroup) {
    this.isloading = true;

    this._service.sendSingleResponse(form.value).subscribe((value: any) => {
      console.log(value);
      
      this.singleDataResult=value
      this.isloading = false
    this.showSingleResponse = true;
    this.showBulletComponent = false;
    this.graphPercentage = this.singleDataResult.prob * 100;
    console.log(value.sentiment);
    

    },
    (error) => {
      console.error('Error fetching data:', error);
      this.isloading = false;
    }
    );
  }
  toggleInputMode() {
    this.showFileUpload = !this.showFileUpload;
  }
  onFileSelected(evt: any) {
    const reader: FileReader = new FileReader();
    const target: DataTransfer = <DataTransfer>(evt.target);

    if (target.files.length > 1) {
      alert('Multiple files are not allowed');
      return;
    }
    else {
      this.fileValue=target.files[0]
      reader.readAsBinaryString(target.files[0]);

      reader.onload = (e: any) => {
        const bstr: string = e.target.result;
        const wb: XLSX.WorkBook = XLSX.read(bstr, { type: 'binary' });

        const wsname: string = wb.SheetNames[0];
        const ws: XLSX.WorkSheet = wb.Sheets[wsname];

        this.data = (XLSX.utils.sheet_to_json(ws));
      }
      reader.readAsBinaryString(target.files[0]);
    }
  }
  getSeverity(status: string) {
    switch (status) {
      case 'Positive':
        return 'success';
      case 'Negative':
        return 'danger';
    }
    return
  }
  multiple() {
    this.isloading = true

    this._service.sendMultipleResponse(this.fileValue).subscribe((value:any)=>{
      console.log(value);
      this.multipleDataResult=value.result      
      this.isloading=false;
      this.showBulletComponent = true;
    this.showSingleResponse = false;
    },
    (error) => {
      console.error('Error fetching data:', error);
      this.isloading = false;
    })
  
  }
  
  getObjectLength(obj: any): number {
    return Object.keys(obj).length;
  }

}
