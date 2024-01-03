import { Component,OnInit,Input } from '@angular/core';
import { Color, LegendPosition, ScaleType } from '@swimlane/ngx-charts';

@Component({
  selector: 'app-single-response',
  templateUrl: './single-response.component.html',
  styleUrls: ['./single-response.component.scss']
})
export class SingleResponseComponent implements OnInit{

  // progressValue = 90;

  // getProgressBarClass(): { [key: string]: boolean } {
  //   return {
  //     'red-bar': this.progressValue < 50,
  //     'green-bar': this.progressValue >= 50,
  //   };
  // }
  @Input() inputPercentage: number = 0; 

  resposneValue:any
  backgroundColor:any = []; 
  gaugeValue!: number;
  
  constructor() {
  } 
  colorScheme: Color = {
    name: 'Custom',
    selectable: true,
    group: ScaleType.Ordinal,
    domain: this.backgroundColor
  };
  
  ngOnInit(): void {  
    const red = '#A10A28';
    const green = '#5AA454';
  
    if (this.inputPercentage < 50) {
      this.backgroundColor.push(red);
    } else {
      this.backgroundColor.push(green);
    }
  }
  
  
  onPercentageChange(percentage: number) {
    // Update the gaugeValue when the percentage changes
    this.gaugeValue = percentage;
    console.log(this.gaugeValue);
    
  }
  onSelect(event:any) {
    console.log(event);
  }
}
