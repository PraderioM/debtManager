import {Component, EventEmitter, Input, OnInit, Output} from '@angular/core';
import {Member} from '../../../services/models/member';
import {StateService} from '../../../services/state.services';
import {Group} from '../../../services/models/group';
import {PeriodicFlow, ReceiverBurden} from '../../../services/models/periodic.flow';

@Component({
  selector: 'app-periodic-flow-edition',
  templateUrl: './periodic-flow-edition.component.html',
  styleUrls: ['./periodic-flow-edition.component.css']
})
export class PeriodicFlowEditionComponent implements OnInit {
  @Input() group: Group;
  @Input() periodicFlow?: PeriodicFlow;
  @Input() periodicFlowIndex?: number;

  @Output() back = new EventEmitter<void>();

  memberList: Member[];
  issuer?: Member;
  payDay: number;
  period: number;
  amount?: number;
  receiverList: ReceiverBurden[];

  constructor(private stateService: StateService) { }

  ngOnInit(): void {
    this.updateMemberList();
    if (this.periodicFlow != null) {
      this.issuer = this.periodicFlow.issuer;
      this.payDay = this.periodicFlow.payDay;
      this.period = this.periodicFlow.period;
      this.amount = this.periodicFlow.amountPayed;
    } else {
      this.issuer = null;
      this.payDay = 1;
      this.period = 1;
      this.receiverList = [];
      this.amount = null;
    }
  }


  async updateMemberList(): Promise<void> {
    this.memberList = await this.stateService.getMemberList(this.group.name);
    if (this.memberList.length === 0) {
      this.back.emit();
    }
  }

  updateIssuer(issuer: Member): void {
    this.issuer = issuer;
  }

  updatePayDay(payDay: number): void {
    this.payDay = payDay;
  }

  updatePeriod(period: number): void {
    this.period = period;
  }

  addReceiver(): void {
    this.receiverList.push(new ReceiverBurden(this.memberList[0], 0));
  }

  updateReceiver(receiver: Member, i: number): void {
    this.receiverList[i].receiver = receiver;
  }

  getReceiverAmount(burden: number): number {
    if (this.amount == null) {
      return 0;
    } else {
      return this.amount * burden;
    }
  }

  updateFractionFromAmount(event: Event, i: number): void {
    // Todo understand event.
    console.log(event);
  }

  removeReceiver(i: number): void {
    this.receiverList.splice(i, 1);
  }

  updateFraction(event: Event, receiverBurden: ReceiverBurden): void {
    // Todo understand event.
    console.log(event);
  }

  updateAmount(event: Event): void {
    // Todo understand event.
    console.log(event);
  }

  getAmount(): number {
    if (this.amount == null) {
      return  0;
    } else {
      return this.amount;
    }
  }

  getButtonName(): string {
    if (this.periodicFlowIndex == null) {
      return 'Add';
    } else {
      return 'Modify';
    }
  }

  async removePeriodicFlow(): Promise<void> {
    await this.stateService.removePeriodicFlow(this.group.name, this.periodicFlowIndex);
    this.back.emit();
  }

  async editPeriodicFlow(checked: boolean): Promise<void> {
    if (this.receiverList.length === 0) {
      return ;
    }
    // Todo continue.
  }
}
