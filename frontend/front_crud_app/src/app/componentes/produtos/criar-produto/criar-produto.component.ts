import { CategoriaService } from './../../categorias/categoria.service';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { ProdutoService } from '../produto.service';
import { Categoria } from '../../categorias/categoria';
import { HttpClientModule } from '@angular/common/http';

interface IProd {
  name: string,
  category: number,
  price: number,
  serie: number
}

@Component({
  selector: 'app-criar-produto',
  templateUrl: './criar-produto.component.html',
  styleUrls: ['./criar-produto.component.scss']
})
export class CriarProdutoComponent {

  formulario!: FormGroup;
  prod: IProd;

  categoria: Categoria = {
    id: 1,
    name: ''
  }

  produto = {
    name: ``,
    category: 1,
    price: 1,
    serie: 1
  }

  listaCategorias: Categoria[] = [];

  constructor(private serviceprod: ProdutoService,
    private servicecat: CategoriaService,
    private router: Router
  ) { this.prod = {} as IProd; }

  ngOnInit(): void {

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


  criar_produto() {

    this.serviceprod.create(this.formulario.value).subscribe(() => {
      this.router.navigate(['listarProduto'])
    })
  }

  cancelar_criacao_produto() {
    this.router.navigate(['listarProduto'])
  }


}
