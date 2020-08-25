import {Component, Input, OnInit, Output, EventEmitter} from '@angular/core';
import {Flow} from '../../../services/models/flow';
import {Member} from '../../../services/models/member';
import {StateService} from '../../../services/state.services';
import {Group} from '../../../services/models/group';

@Component({
  selector: 'app-flow-edition',
  templateUrl: './flow-edition.component.html',
  styleUrls: ['./flow-edition.component.css']
})
export class FlowEditionComponent implements OnInit {
  @Input() group: Group;
  @Input() token: string;
  @Input() flow?: Flow;
  @Input() flowIndex?: number;
  @Input() memberList: Member[];

  @Output() back = new EventEmitter<void>();

  issuerName?: string;
  receiverName?: string;
  amount?: number;

  constructor(private stateService: StateService) { }

  ngOnInit(): void {
    if (this.flow == null) {
      this.issuerName = null;
      this.receiverName = null;
      this.amount = 0;
    } else {
      this.issuerName = this.flow.issuer.name;
      this.receiverName = this.flow.receiver.name;
      this.amount = this.flow.amount;
    }
  }

  getButtonName(): string {
    if (this.flowIndex == null) {
      return 'Add';
    } else {
      return 'Modify';
    }
  }

  async createFlow(amount: number, concept: string): Promise<void> {
    // If name is not repeated then we can create a new member.
    await this.stateService.addFlow(this.token, this.group.name, this.issuerName, this.receiverName, amount, concept);

    // Once done we can go back and update groups.
    this.back.emit();
  }

  async updateFlow(flowIndex: number, amount: number, concept: string): Promise<void> {
    // If name is not repeated then we can create a new member.
    await this.stateService.updateFlow(this.token, flowIndex, this.group.name, this.issuerName, this.receiverName, amount, concept);

    // Once done we can go back and update groups.
    this.back.emit();
  }

  updateIssuer(member: Member): void {
    this.issuerName = member.name;
  }

  updateReceiver(member: Member): void {
    this.receiverName = member.name;
  }

  async removeFlow(): Promise<void> {
    // If name is not repeated then we can create a new member.
    await this.stateService.removeFlow(this.token, this.group.name, this.flowIndex);

    // Once done we can go back and update groups.
    this.back.emit();
  }

  async editFlow(amount: number, concept: string): Promise<void> {
    if (this.flowIndex == null) {
      await this.createFlow(amount, concept);
    } else {
      await this.updateFlow(this.flowIndex, amount, concept);
    }
  }
}
