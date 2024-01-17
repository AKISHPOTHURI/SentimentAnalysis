import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AnalysisService {

  private apiUrl = 'http://127.0.0.1:5000/api'; // Base API URL

  constructor(private http: HttpClient) {}

  /**
   * Sends a request to the server to perform sentiment analysis on a single data.
   * @param singleData$ - The data for single response analysis.
   * @returns An Observable with the analysis result.
   */
  sendSingleResponse(singleData$: any): Observable<any> {
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });
    const url = `${this.apiUrl}/Custompredict`;

    return this.http.post<any>(url, singleData$, { headers });
  }

  /**
   * Sends a request to the server to perform sentiment analysis on multiple data from an uploaded file.
   * @param file - The file containing multiple data for analysis.
   * @returns An Observable with the analysis result.
   */
  sendMultipleResponse(file: File): Observable<any> {
    const formData: FormData = new FormData();
    formData.append('file', file, file.name);
    const url = `${this.apiUrl}/customUploadExcel`;

    return this.http.post<any>(url, formData);
  }
}