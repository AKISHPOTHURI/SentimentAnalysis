import { Component,OnInit,Input } from '@angular/core';
import { Color, LegendPosition, ScaleType } from '@swimlane/ngx-charts';

@Component({
  selector: 'app-single-response',
  templateUrl: './single-response.component.html',
  styleUrls: ['./single-response.component.scss']
})
export class SingleResponseComponent implements OnInit{

  @Input() inputPercentage: number = 0; 
  @Input() inputSentiment!:number
  resposneValue:any
  backgroundColor:any = []; 
  gaugeValue!: number;
  
  constructor() {
  } 

  // Color scheme for ngx-charts, initialized with the background color array.
  colorScheme: Color = {
    name: 'Custom',
    selectable: true,
    group: ScaleType.Ordinal,
    domain: this.backgroundColor
  };
  
  ngOnInit(): void { 

    // Define color codes for sentiment visualization.
    const red = '#A10A28';
    const green = '#5AA454';

    // Set the background color based on the input sentiment value.
    if (this.inputSentiment===0) {      
      this.backgroundColor.push(red);
    } else {
      this.backgroundColor.push(green);
    }
  }
  
  /**
   * onPercentageChange function updates the gaugeValue property when the percentage changes.
   * @param percentage - The new percentage value.
   * Output: Updates the gaugeValue property.
   */

  onPercentageChange(percentage: number) {
    this.gaugeValue = percentage;
    
  }

    /**
   * onSelect function logs the provided event to the console when a selection occurs.
   * @param event - The selection event.
   * Output: Logs the event object to the console.
   */
  
  onSelect(event:any) {
    console.log(event);
  }
}