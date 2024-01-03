import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MultipleResponseComponent } from './multiple-response.component';

describe('MultipleResponseComponent', () => {
  let component: MultipleResponseComponent;
  let fixture: ComponentFixture<MultipleResponseComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [MultipleResponseComponent]
    });
    fixture = TestBed.createComponent(MultipleResponseComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
