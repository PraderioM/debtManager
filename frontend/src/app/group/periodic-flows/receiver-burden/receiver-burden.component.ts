import {Component, Input, OnInit} from '@angular/core';
import {ReceiverBurden} from '../../../services/models/periodic.flow';

@Component({
  selector: 'app-receiver-burden',
  templateUrl: './receiver-burden.component.html',
  styleUrls: ['./receiver-burden.component.css']
})
export class ReceiverBurdenComponent implements OnInit {
  @Input() receiverList: ReceiverBurden[];
  @Input() totalAmount?: number;

  constructor() { }

  ngOnInit(): void {
  }

  getBurdenString(fraction: number): string {
    if (this.totalAmount == null) {
      return (Math.round(fraction * 100)).toString() + '% of a variable amount';
    } else {
      return (Math.round(this.totalAmount * fraction * 100) / 100).toString();
    }
  }
}
