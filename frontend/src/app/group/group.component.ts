import {Component, Input, OnInit, Output, EventEmitter} from '@angular/core';
import {Group} from '../services/models/group';

@Component({
  selector: 'app-group',
  templateUrl: './group.component.html',
  styleUrls: ['./group.component.css']
})
export class GroupComponent implements OnInit {
  @Input() token: string;
  @Input() group: Group;
  @Input() groupIndex: number;

  @Output() back = new EventEmitter<void>();
  @Output() refresh = new EventEmitter<void>();

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
