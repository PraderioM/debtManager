import {Component, Input, OnInit} from '@angular/core';
import {Group} from '../../services/models/group';
import {Member} from '../../services/models/member';
import {StateService} from '../../services/state.services';

@Component({
  selector: 'app-members',
  templateUrl: './members.component.html',
  styleUrls: ['./members.component.css']
})
export class MembersComponent implements OnInit {
  @Input() group: Group;
  @Input() token: string;

  editionMode = false;
  memberList: Member[];
  selectedMember?: Member;
  selectedMemberIndex?: number;

  constructor(private stateService: StateService) { }

  ngOnInit(): void {
    this.updateMembers();
  }

  async updateMembers(): Promise<void> {
    this.memberList = await this.stateService.getMemberList(this.group.name);
  }

  async onBackFromEdition(): Promise<void> {
    this.editionMode = false;
    await this.updateMembers();
  }

  enterCreationMode(): void {
    this.editionMode = true;
    this.selectedMember = null;
    this.selectedMemberIndex = null;
  }

  enterModificationMode(member: Member, index: number): void {
    this.editionMode = true;
    this.selectedMember = member;
    this.selectedMemberIndex = index;
  }
}
