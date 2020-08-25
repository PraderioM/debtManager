import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { PeriodicFlowEditionComponent } from './periodic-flow-edition.component';

describe('PeriodicFlowEditionComponent', () => {
  let component: PeriodicFlowEditionComponent;
  let fixture: ComponentFixture<PeriodicFlowEditionComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PeriodicFlowEditionComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(PeriodicFlowEditionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
