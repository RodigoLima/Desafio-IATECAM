import { Router, ActivatedRoute } from '@angular/router';
import { CategoriaService } from './../categoria.service';
import { Categoria } from './../categoria';
import { Component, Input, OnInit } from '@angular/core';
import { FormGroup, FormControl, FormBuilder, Validators } from '@angular/forms';
import { first } from 'rxjs/operators';

interface ICat {
  name: String;
}

@Component({
  selector: 'app-editar-categoria',
  templateUrl: './editar-categoria.component.html',
  styleUrls: ['./editar-categoria.component.scss']
})
export class EditarCategoriaComponent implements OnInit {

  formulario!: FormGroup;
  cat: ICat;
  id: Number;

  categoria = {
    name: ``

  }

  constructor(
    private service: CategoriaService,
    private router: Router,
    private route: ActivatedRoute
  ) {  this.cat = {} as ICat; this.id = 0}



  ngOnInit(): void {

    this.id = this.route.snapshot.params['id'];

    this.service.get_by_id(this.id).pipe(first()).subscribe(x => this.formulario.patchValue(x)
    ),
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



  editar_Categoria() {

    this.service.update(this.id,this.formulario.value).subscribe(() => {
      this.router.navigate(['/listarCategoria'])
    })

  }

  cancelar_edicao() {
    this.router.navigate(['/listarCategoria'])
  }

}
