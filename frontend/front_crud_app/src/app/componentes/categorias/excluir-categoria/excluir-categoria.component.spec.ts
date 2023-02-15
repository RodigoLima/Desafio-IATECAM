import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ExcluirCategoriaComponent } from './excluir-categoria.component';

describe('ExcluirCategoriaComponent', () => {
  let component: ExcluirCategoriaComponent;
  let fixture: ComponentFixture<ExcluirCategoriaComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ExcluirCategoriaComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ExcluirCategoriaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
