import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { NgxSkeletonLoaderModule } from 'ngx-skeleton-loader';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import {     MultipleResponseComponent} from './multiple-response/multiple-response.component';
import {  ReactiveFormsModule } from '@angular/forms';
import { SearchComponent } from './search/search.component';
import {    NgxChartsModule} from '@swimlane/ngx-charts';
import { SingleResponseComponent } from './single-response/single-response.component';
import { ProgressBarModule } from 'primeng/progressbar';
import { TableModule } from 'primeng/table';
import { HttpClientModule } from '@angular/common/http';
import { ButtonModule } from "primeng/button";
import { BadgeModule } from "primeng/badge";
import { ExportAsModule } from 'ngx-export-as';


@NgModule({
  declarations: [
    AppComponent,
    MultipleResponseComponent,
    SearchComponent,
    SingleResponseComponent,
  ],
  imports: [
    ExportAsModule,
    ButtonModule,
    BadgeModule,
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    ReactiveFormsModule,
    NgxChartsModule,
    ProgressBarModule,
    TableModule,
    HttpClientModule,
    NgxSkeletonLoaderModule

  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
