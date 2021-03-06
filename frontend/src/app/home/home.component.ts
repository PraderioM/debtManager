import {Component, OnInit, Output, EventEmitter, Input} from '@angular/core';
import {Group} from '../services/models/group';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  @Output() updateGroups = new EventEmitter<void>();
  @Input() groupList: Group[];
  @Input() token: string;

  groupAdding = false;

  constructor() { }

  ngOnInit(): void {
  }

  toggleGroupAdding(): void {
    this.groupAdding = !this.groupAdding;
  }

  onGoBack(): void {
    this.groupAdding = false;
    this.updateGroups.emit();
}

}
