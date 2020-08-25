import {Component, Input, OnInit} from '@angular/core';
import {Group} from '../../services/models/group';
import {StateService} from '../../services/state.services';
import {Flow} from '../../services/models/flow';

@Component({
  selector: 'app-summary',
  templateUrl: './summary.component.html',
  styleUrls: ['./summary.component.css']
})
export class SummaryComponent implements OnInit {
  @Input() group: Group;

  flowList: Flow[] = [];

  constructor(private stateService: StateService) { }

  ngOnInit(): void {
    this.updateFlowList();
  }

  round(x: number): number {
    return Math.round(x * 100) / 100;
  }

  async updateFlowList(): Promise<void> {
    this.flowList = await this.stateService.getSummary(this.group.name);
  }
}
