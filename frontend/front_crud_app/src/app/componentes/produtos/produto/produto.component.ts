import { Categoria } from './../../categorias/categoria';
import { ProdutoService } from './../produto.service';
import { Produto } from './../produto';
import { Component ,OnInit,Input} from '@angular/core';

@Component({
  selector: 'app-produto',
  templateUrl: './produto.component.html',
  styleUrls: ['./produto.component.scss']
})
export class ProdutoComponent {

  @Input() produto: Produto = {
    id: 1,
    name: '',
    category: 1,
    price: 1.2,
    serie: 23
  }

  categoria: Categoria = {
    id: 1,
    name: ''
  }

  listaCategorias: Categoria[] = [];

  listaProdutos: Produto[] = [];

  constructor( private service: ProdutoService) {}


  ngOnInit(): void {
    this.get_all();
  }


  get_all() {
    this.service.get_all().subscribe((data) => {
      this.listaProdutos = data;
    });
  }

}
