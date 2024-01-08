import { Component, OnInit,Input  } from '@angular/core';
import { Color, LegendPosition, ScaleType } from '@swimlane/ngx-charts';




@Component({
  selector: 'app-multiple-response',
  templateUrl: './multiple-response.component.html',
  styleUrls: ['./multiple-response.component.scss']
})
export class MultipleResponseComponent implements OnInit {
  @Input() data: any[] = [];
  sentimentCounts: any
  multiple!: any;
  view: any[] = [700, 400];
  positive: any
  negative: any

  // options
  gradient: boolean = true;
  showLegend: boolean = true;
  showLabels: boolean = true;
  isDoughnut: boolean = false;

  colorScheme: Color = {
    name: 'myScheme',
    selectable: true,
    group: ScaleType.Ordinal,

    domain: ['#A10A28', '#5AA454']
  };
  pieChartLabel: any;

  constructor() {
  }

  ngOnInit(): void {

    let totalItems = this.data.length;
    console.log("Data:",this.data);
    
    this.sentimentCounts = this.data.reduce((totals: { [key: number]: number }, item) => {
      if (item.sentiment === 1 || item.sentiment === 0) {
        totals[item.sentiment] = (totals[item.sentiment] || 0) + 1;
      }
      return totals;
    }, { 0: 0, 1: 0 });
    console.log("sentimentCounts",this.sentimentCounts);
    for (let sentiment in this.sentimentCounts) {
      this.sentimentCounts[sentiment] = (this.sentimentCounts[sentiment] / totalItems) * 100;
    }
    this.multiple = Object.keys(this.sentimentCounts).map(sentiment => ({
      name: sentiment === '1' ? 'Positive' : 'Negative',
      value: this.sentimentCounts[sentiment]
    }));
    console.log(this.multiple);
    
  }



  onSelect(data: any): void {

    console.log('Item clicked', JSON.parse(JSON.stringify(data)));
  }

  onActivate(data: any): void {
    console.log('Activate', JSON.parse(JSON.stringify(data)));
  }

  onDeactivate(data: any): void {
    console.log('Deactivate', JSON.parse(JSON.stringify(data)));
  }

}
