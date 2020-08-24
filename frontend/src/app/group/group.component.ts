import {Component, Input, OnInit} from '@angular/core';
import {Group} from '../services/models/group';

@Component({
  selector: 'app-group',
  templateUrl: './group.component.html',
  styleUrls: ['./group.component.css']
})
export class GroupComponent implements OnInit {
  @Input() group: Group;

  selectedItem = 'summary';

  constructor() { }

  ngOnInit(): void {
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

}
