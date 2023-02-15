import { CategoriaService } from './../../categorias/categoria.service';
import { ActivatedRoute, Router } from '@angular/router';
import { ProdutoService } from './../produto.service';
import { Component } from '@angular/core';
import { Produto } from '../produto';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { Categoria } from '../../categorias/categoria';
import { first } from 'rxjs/operators';

interface IProd {
  name: string,
  category: number,
  price: number,
  serie: number
}


@Component({
  selector: 'app-editar-produto',
  templateUrl: './editar-produto.component.html',
  styleUrls: ['./editar-produto.component.scss']
})
export class EditarProdutoComponent {

  formulario!: FormGroup;
  prod: IProd;

  id: Number;

  categoria: Categoria = {
    id: 1,
    name: ''
  }

  produto = {
    name: "",
    category: 1,
    price: 1,
    serie: 1
  }

  listaCategorias: Categoria[] = [];

  constructor(
    private service: ProdutoService,
    private servicecat: CategoriaService,
    private router: Router,
    private route: ActivatedRoute
  ) {  this.prod = {} as IProd; this.id = 0 }

  ngOnInit(): void {
    this.id = this.route.snapshot.params['id'];

    this.service.get_by_id(this.id).pipe(first()).subscribe(x => this.formulario.patchValue(x)
    ),
    this.formulario = new FormGroup({
      name: new FormControl(this.prod.name, [
        Validators.required,
        Validators.minLength(1),
        Validators.maxLength(60)
      ]),
      category: new FormControl(this.prod.category, [
        Validators.required,
        Validators.minLength(1)
      ]),
      price: new FormControl(this.prod.price, [
        Validators.required,
        Validators.minLength(1)
      ]),
      serie: new FormControl(this.prod.serie, [
        Validators.required,
        Validators.min(1),
        Validators.pattern('^(0|[1-9][0-9]*)$')
      ])
    }),
      this.servicecat.get_all().subscribe((data) => {
        this.listaCategorias = data;
      });


  }
  get name() {
    return this.formulario.get('name')!;
  }
  get category() {
    return this.formulario.get('category')!;
  }
  get price() {
    return this.formulario.get('price')!;
  }
  get serie() {
    return this.formulario.get('serie')!;
  }

  public validate(): void {
    if (this.formulario.invalid) {
      for (const control of Object.keys(this.formulario.controls)) {
        this.formulario.controls[control].markAsTouched();
      }
      return;
    }

    this.prod = this.formulario.value;
  }


  editar_Produto() {
    this.service.update(this.id,this.formulario.value).subscribe(() => {
      this.router.navigate(['/listarProduto'])
    })

  }

  cancelar_edicao() {
    this.router.navigate(['/listarProduto'])
  }

}
