import {Component, Input, OnInit} from '@angular/core';
import {StateService} from '../../services/state.services';
import {Group} from '../../services/models/group';
import {Member} from '../../services/models/member';
import {Flow} from '../../services/models/flow';

@Component({
  selector: 'app-flows',
  templateUrl: './flows.component.html',
  styleUrls: ['./flows.component.css']
})
export class FlowsComponent implements OnInit {
  @Input() group: Group;
  @Input() token: string;

  editionMode = false;
  selectedFlow?: Flow;
  selectedFlowIndex?: number;
  memberList: Member[];
  flowList: Flow[];

  constructor(private stateService: StateService) { }

  ngOnInit(): void {
    this.updateMemberList();
    this.updateFlowList();
  }

  async updateMemberList(): Promise<void> {
    this.memberList = await this.stateService.getMemberList(this.group.name);
  }

  async updateFlowList(): Promise<void> {
    this.flowList = await this.stateService.getFlowList(this.group.name);
  }

  async onBackFromEdition(): Promise<void> {
    this.editionMode = false;
    await this.updateFlowList();
  }

  enterCreationMode(): void {
    this.editionMode = true;
    this.selectedFlow = null;
    this.selectedFlowIndex = null;
  }

  enterModificationMode(flow: Flow, index: number): void {
    this.editionMode = true;
    this.selectedFlow = flow;
    this.selectedFlowIndex = index;
  }

  round(amount: number): number {
    return Math.round(amount * 100) / 100;
  }
}
