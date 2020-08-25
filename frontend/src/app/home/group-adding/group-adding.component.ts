import {Component, EventEmitter, Input, OnInit, Output} from '@angular/core';
import {StateService} from '../../services/state.services';
import {Group} from '../../services/models/group';

@Component({
  selector: 'app-group-adding',
  templateUrl: './group-adding.component.html',
  styleUrls: ['./group-adding.component.css']
})
export class GroupAddingComponent implements OnInit {
  @Output() back = new EventEmitter<void>();
  @Input() groupList: Group[];
  @Input() token: string;

  errorInName = false;

  constructor(private stateService: StateService) { }

  ngOnInit(): void {
  }

  getNameNgClass(): object {
    return {
      error: this.errorInName
    };
  }

  async tryCreateGame(name: string, mg1: string, mg2: string): Promise<void> {
    // Check for repeated names.
    for (const group of this.groupList) {
      if (group.name === name) {
        this.errorInName = true;
        return;
      }
    }

    // If name is not repeated then we can create a new group.
    await this.stateService.addGroup(this.token, name, mg1, mg2);

    // Once done we can go back and update groups.
    this.back.emit();
  }

}
