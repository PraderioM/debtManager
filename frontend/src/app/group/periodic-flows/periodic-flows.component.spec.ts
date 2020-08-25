import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { PeriodicFlowsComponent } from './periodic-flows.component';

describe('PeriodicFlowsComponent', () => {
  let component: PeriodicFlowsComponent;
  let fixture: ComponentFixture<PeriodicFlowsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PeriodicFlowsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(PeriodicFlowsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
