import {Component, EventEmitter, Output, Input, OnInit} from '@angular/core';
import {Group} from '../../services/models/group';
import {PeriodicFlow} from '../../services/models/periodic.flow';
import {StateService} from '../../services/state.services';

@Component({
  selector: 'app-periodic-flows',
  templateUrl: './periodic-flows.component.html',
  styleUrls: ['./periodic-flows.component.css']
})
export class PeriodicFlowsComponent implements OnInit {
  @Input() group: Group;
  @Input() token: string;

  periodicFlowList: PeriodicFlow[];
  selectedPeriodicFlow?: PeriodicFlow;
  selectedPeriodicFlowIndex?: number;
  editionMode = false;

  constructor(private stateService: StateService) { }

  ngOnInit(): void {
    this.updatePeriodicFlowList();
  }

  async updatePeriodicFlowList(): Promise<void> {
    this.periodicFlowList = await this.stateService.getPeriodicFlowList(this.group.name);
  }

  onBackFromEdition(): void {
    this.editionMode = false;
    this.updatePeriodicFlowList();
  }

  enterCreationMode(): void {
    this.editionMode = true;
    this.selectedPeriodicFlow = null;
    this.selectedPeriodicFlowIndex = null;
  }

  enterModificationMode(periodicFlow: PeriodicFlow, index: number): void {
    this.editionMode = true;
    this.selectedPeriodicFlow = periodicFlow;
    this.selectedPeriodicFlowIndex = index;
  }

  getPeriodString(period: number): string {
    if (period === 1) {
      return 'month';
    } else {
      return period.toString() + ' months';
    }
  }
}
