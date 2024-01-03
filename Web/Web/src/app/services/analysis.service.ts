import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AnalysisService {


  

  constructor(private http:HttpClient) {
   }

  sendSingleResponse(singleData$:any):Observable<any>{
    const headers = { 'content-type': 'application/json'} 
    console.log(singleData$);
    return this.http.post<any>("http://127.0.0.1:5000/api/getSentiment",singleData$,{'headers':headers})
  }

  sendMultipleResponse(file: File):Observable<any>{
    const formData: FormData = new FormData();
    formData.append('file', file, file.name);
    console.log(formData);
    return this.http.post<any>("http://127.0.0.1:5000/api/UploadExcel",formData)
  }
}
