import {Component, Input, OnInit, Output, EventEmitter} from '@angular/core';
import {Group} from '../../services/models/group';
import {StateService} from '../../services/state.services';

@Component({
  selector: 'app-settings',
  templateUrl: './settings.component.html',
  styleUrls: ['./settings.component.css']
})
export class SettingsComponent implements OnInit {
  @Input() group: Group;
  @Input() groupIndex: number;
  @Input() token: string;

  @Output() remove = new EventEmitter<void>();
  @Output() back = new EventEmitter<void>();

  constructor(private stateService: StateService) { }

  ngOnInit(): void {
  }

  async modifyGroup(mailgun1: string, mailgun2: string): Promise<void> {
    await this.stateService.updateGroup(this.token, this.groupIndex, this.group.name, mailgun1, mailgun2);
    this.back.emit();
  }

  async removeGroup(): Promise<void> {
    await this.stateService.removeGroup(this.token, this.groupIndex);
    this.remove.emit();
  }
}
