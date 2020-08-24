import {Component, OnInit} from '@angular/core';
import {Group} from './services/models/group';
import {StateService} from './services/state.services';
import {HttpClient} from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers: [StateService, HttpClient]
})
export class AppComponent implements OnInit  {
  title = 'frontend';
  selectedItem = 'home';
  interval;
  token: string;
  groupList: Group[] = [new Group('group1', '', '')];

  constructor(private stateService: StateService) {}

  ngOnInit(): void {
    this.updateToken();
    this.updateGroupList();

    this.interval = setInterval(() => {
      this.verifyConnection();
    }, 1000);
  }

  async updateGroupList(): Promise<void> {
    this.groupList = await this.stateService.getGroupList();
  }

  async updateToken(): Promise<void> {
    this.token = await this.stateService.getToken();
  }

  async verifyConnection(): Promise<void> {
    await this.stateService.verifyConnection(this.token);
  }

  selectItem(name: string): void {
    this.selectedItem = name;
  }

  getNgClass(name: string): object {
    return {
      'header-btn': true,
      'selected-header': this.selectedItem === name
    };
  }

  getSelectedGroup(): Group {
    for (const group of this.groupList) {
      if (group.name === this.selectedItem) {
        return group;
      }
    }
  }
}
