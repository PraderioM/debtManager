import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ReceiverBurdenComponent } from './receiver-burden.component';

describe('ReceiverBurdenComponent', () => {
  let component: ReceiverBurdenComponent;
  let fixture: ComponentFixture<ReceiverBurdenComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ReceiverBurdenComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ReceiverBurdenComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
