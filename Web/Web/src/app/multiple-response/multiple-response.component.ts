import { Component, OnInit, Input } from '@angular/core';
import { Color, ScaleType } from '@swimlane/ngx-charts';


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

  // Color scheme for ngx-charts, initialized with specific color codes.
  colorScheme: Color = {
    name: 'myScheme',
    selectable: true,
    group: ScaleType.Ordinal,
    domain: ['#A10A28', '#5AA454']
  };
  pieChartLabel: any;

  constructor() {
  }


  /**
 * The ngOnInit function is part of the Angular lifecycle hooks and is executed when the component is initialized.
 * It performs the following tasks:
 * - Calculates the total number of items in the provided data array.
 * - Initializes the sentimentCounts object to store the count of each sentiment (0 and 1).
 * - Uses the reduce function to iterate over the data array and update sentimentCounts with the count of each sentiment.
 * - Calculates the percentage of each sentiment based on the total number of items.
 * - Converts the sentimentCounts object into an array suitable for ngx-charts.
 * Output: Updates the sentimentCounts and multiple properties with the calculated values.
 */

  ngOnInit(): void {
    let totalItems = this.data.length;
    this.sentimentCounts = this.data.reduce((totals: { [key: number]: number }, item) => {
      if (item.sentiment === 1 || item.sentiment === 0) {
        totals[item.sentiment] = (totals[item.sentiment] || 0) + 1;
      }
      return totals;
    }, { 0: 0, 1: 0 });
    for (let sentiment in this.sentimentCounts) {
      this.sentimentCounts[sentiment] = (this.sentimentCounts[sentiment] / totalItems) * 100;
    }
    this.multiple = Object.keys(this.sentimentCounts).map(sentiment => ({
      name: sentiment === '1' ? 'Positive' : 'Negative',
      value: this.sentimentCounts[sentiment]
    }));
  }

  /**
     * onSelect function logs the clicked item's data to the console.
     * @param data - The data of the clicked item.
     * Output: Logs the clicked item's data to the console.
     */
  onSelect(data: any): void {
    console.log('Item clicked', JSON.parse(JSON.stringify(data)));
  }

  /**
     * onActivate function logs the activation event data to the console.
     * @param data - The activation event data.
     * Output: Logs the activation event data to the console.
     */
  onActivate(data: any): void {
    console.log('Activate', JSON.parse(JSON.stringify(data)));
  }

  /**
   * onDeactivate function logs the deactivation event data to the console.
   * @param data - The deactivation event data.
   * Output: Logs the deactivation event data to the console.
   */
  onDeactivate(data: any): void {
    console.log('Deactivate', JSON.parse(JSON.stringify(data)));
  }

}