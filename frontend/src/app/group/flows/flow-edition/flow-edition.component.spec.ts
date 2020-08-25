import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { FlowEditionComponent } from './flow-edition.component';

describe('FlowEditionComponent', () => {
  let component: FlowEditionComponent;
  let fixture: ComponentFixture<FlowEditionComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ FlowEditionComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(FlowEditionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
