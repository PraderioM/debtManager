import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MemberEditionComponent } from './member-edition.component';

describe('MemberAdditionComponent', () => {
  let component: MemberEditionComponent;
  let fixture: ComponentFixture<MemberEditionComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MemberEditionComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MemberEditionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
