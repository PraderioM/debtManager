import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { GroupAddingComponent } from './group-adding.component';

describe('GroupAddingComponent', () => {
  let component: GroupAddingComponent;
  let fixture: ComponentFixture<GroupAddingComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ GroupAddingComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(GroupAddingComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
