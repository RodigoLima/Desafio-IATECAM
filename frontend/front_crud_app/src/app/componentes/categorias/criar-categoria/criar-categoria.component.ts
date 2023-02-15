import { CategoriaService } from './../categoria.service';
import { Component, Input, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { FormGroup, FormControl, FormBuilder, Validators } from '@angular/forms';

interface ICat {
  name: string;
}

@Component({
  selector: 'app-criar-categoria',
  templateUrl: './criar-categoria.component.html',
  styleUrls: ['./criar-categoria.component.scss']
})
export class CriarCategoriaComponent implements OnInit {


  formulario!: FormGroup;
  cat: ICat;

  categoria = {
    name: ``

  }
  constructor(private service: CategoriaService,
    private router: Router,

  ) { this.cat = {} as ICat; }

  ngOnInit(): void {

    this.formulario = new FormGroup({
      name: new FormControl(this.cat.name, [
        Validators.required,
        Validators.minLength(1),
        Validators.maxLength(128)
      ])
    });
  }

  get name() {
    return this.formulario.get('name')!;
  }

  public validate(): void {
    if (this.formulario.invalid) {
      for (const control of Object.keys(this.formulario.controls)) {
        this.formulario.controls[control].markAsTouched();
      }
      return;
    }

    this.cat = this.formulario.value;

  }
  criar_categoria() {

    this.service.create(this.formulario.value).subscribe(() => {
      this.router.navigate(['listarCategoria'])
    })
  }

  cancelar_criacao_categoria() {
    this.router.navigate(['listarCategoria'])
  }


}
