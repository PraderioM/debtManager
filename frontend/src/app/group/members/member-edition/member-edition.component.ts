import {Component, Input, OnInit, Output, EventEmitter} from '@angular/core';
import {Group} from '../../../services/models/group';
import {Member} from '../../../services/models/member';
import {StateService} from '../../../services/state.services';

@Component({
  selector: 'app-member-addition',
  templateUrl: './member-edition.component.html',
  styleUrls: ['./member-edition.component.css']
})
export class MemberEditionComponent implements OnInit {
  @Input() group: Group;
  @Input() token: string;
  @Input() member?: Member;
  @Input() memberIndex?: number;
  @Input() memberList: Member[];

  @Output() back = new EventEmitter<void>();
  errorInName = false;

  creditorThr: number;
  debtorThr: number;

  constructor(private stateService: StateService) { }

  ngOnInit(): void {
    if (this.member == null) {
      this.creditorThr = 100;
    } else {
      this.debtorThr = 100;
    }
  }

  getNameNgClass(): object {
    return {
      error: this.errorInName
    };
  }

  getButtonName(): string {
    if (this.memberIndex == null) {
      return 'Add';
    } else {
      return 'Modify';
    }
  }

  async tryCreateMember(name: string, eMail: string, creditorThr: number, debtorThr: number): Promise<void> {
    // Check that there is no repeated name.
    for (const member of this.memberList) {
      if (name === member.name) {
        this.errorInName = true;
        return;
      }
    }

    // If name is not repeated then we can create a new member.
    await this.stateService.addMember(this.token, this.group.name, name, eMail, creditorThr, debtorThr);

    // Once done we can go back and update groups.
    this.back.emit();
  }

  async updateMember(memberIndex: number, name: string, eMail: string, creditorThr: number, debtorThr: number): Promise<void> {
    // If name is not repeated then we can create a new member.
    await this.stateService.updateMember(this.token, this.group.name, memberIndex, name, eMail, creditorThr, debtorThr);

    // Once done we can go back and update groups.
    this.back.emit();
  }

  async removeMember(): Promise<void> {
    // If name is not repeated then we can create a new member.
    await this.stateService.removeMember(this.token, this.group.name, this.memberIndex);

    // Once done we can go back and update groups.
    this.back.emit();
  }

  async editMember(name: string, eMail: string, creditorThr: number, debtorThr: number): Promise<void> {
    if (this.memberIndex == null) {
      await this.tryCreateMember(name, eMail, creditorThr, debtorThr);
    } else {
      await this.updateMember(this.memberIndex, name, eMail, creditorThr, debtorThr);
    }
  }
}
