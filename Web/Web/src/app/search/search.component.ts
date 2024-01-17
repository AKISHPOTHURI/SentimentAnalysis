// Import necessary Angular modules and external libraries
import { Component, ElementRef, OnInit, ViewChild } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';
import * as XLSX from 'xlsx';
import { AnalysisService } from '../services/analysis.service';
import { ExportAsConfig, ExportAsService } from 'ngx-export-as';

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.scss']
})
export class SearchComponent implements OnInit {

  // ViewChild decorator to get a reference to the HTML element with the local variable 'content'
  @ViewChild('content') content!: ElementRef;

  // Initial graph percentage value
  graphPercentage: number = 75;
  singleDataForm: FormGroup = new FormGroup({
    text: new FormControl('')
  });
  data: any

  // Boolean flags for controlling UI elements
  showFileUpload: boolean = false;
  showSingleResponse: boolean = true;
  showBulletComponent: boolean = false;
  isloading: boolean = false;

  // Variable to store single data result
  singleDataResult: any = { sentiment: 1, prob: 0.75 };
  fileValue: any;
  multipleDataResult: any;
  count: any;

  // Configuration for exporting as PDF using ngx-export-as
  exportAsConfig: ExportAsConfig = {
    type: 'pdf',
    elementIdOrContent: 'htmlData',
  };

  constructor(private _service: AnalysisService, private exportAsService: ExportAsService) { }

  ngOnInit() { }

  /**
     * SavePDF function is responsible for saving the current content as a PDF.
     * It uses the ngx-export-as service for exporting and saving the content.
  */
  SavePDF() {
    this.exportAsService.save(this.exportAsConfig, 'data').subscribe(() => { });
    this.exportAsService.get(this.exportAsConfig).subscribe(() => { });
  }

  /**
   * onLoading function is triggered when submitting a single data form.
   * It sends a request to the AnalysisService to get a response for the provided text.
   * The result is then stored in the singleDataResult and displayed in the component, updating various properties accordingly.
   */

  onLoading(form: FormGroup) {
    this.isloading = true;
    setTimeout(() => {
      this._service.sendSingleResponse(form.value).subscribe(
        (value: any) => {
          this.singleDataResult = value;
          this.isloading = false;
          this.showSingleResponse = true;
          this.showBulletComponent = false;
          this.graphPercentage = this.singleDataResult.prob * 100;
        },
        (error) => {
          console.error('Error fetching data:', error);
          this.isloading = false;
        }
      );
    }, 3000);
  }

  /**
   * toggleInputMode function toggles the display of the file upload section.
   */
  toggleInputMode() {
    this.showFileUpload = !this.showFileUpload;
  }

  /**
   * onFileSelected function is triggered when a file is selected for upload.
   * It reads the content of the selected file, parses it using XLSX, and stores the data.
   */
  onFileSelected(evt: any) {
    const target: DataTransfer = <DataTransfer>(evt.target);

    if (target.files.length > 1) {
      alert('Multiple files are not allowed');
      return;
    }

    this.fileValue = target.files[0];

    const reader: FileReader = new FileReader();
    reader.onload = (e: any) => {
      const bstr: string = e.target.result;
      const wb: XLSX.WorkBook = XLSX.read(bstr, { type: 'binary' });

      const wsname: string = wb.SheetNames[0];
      const ws: XLSX.WorkSheet = wb.Sheets[wsname];

      this.data = XLSX.utils.sheet_to_json(ws);
    };

    reader.readAsBinaryString(target.files[0]);
  }

  /**
   * getSeverity function returns the Bootstrap class based on the sentiment status.
   */
  getSeverity(status: string) {
    return status === 'Positive' ? 'success' : status === 'Negative' ? 'danger' : '';
  }

  /**
   * multiple function is triggered when processing multiple data (file upload).
   * It sends a request to the AnalysisService to get a response for the provided file.
   * The result is then stored in the multipleDataResult and displayed in the component, updating various properties.
   * Set the loading flag to true, indicating that the operation is in progress.
   * Count the occurrences of sentiment values (0 and 1) in the result array.
   *Set the loading flag to false, indicating that the operation is complete.
   * Display the bullet component and hide the single response display.
  */
  multiple() {
    this.isloading = true;

    this._service.sendMultipleResponse(this.fileValue).subscribe(
      (value: any) => {
        this.multipleDataResult = value.result;
        this.count = this.multipleDataResult.reduce((totals: { [key: number]: number }, item: { sentiment: number }) => {
          if (item.sentiment === 1 || item.sentiment === 0) {
            totals[item.sentiment] = (totals[item.sentiment] || 0) + 1;
          }
          return totals;
        }, { 0: 0, 1: 0 });

        this.isloading = false;
        this.showBulletComponent = true;
        this.showSingleResponse = false;
      },
      (error) => {
        console.error('Error fetching data:', error);
        this.isloading = false;
      }
    );
  }

  /**
     * getObjectLength function returns the number of properties in an object.
  */
  getObjectLength(obj: any): number {
    return Object.keys(obj).length;
  }
}