import { ProdutoService } from './../produto.service';
import { Produto } from './../produto';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-listar-produto',
  templateUrl: './listar-produto.component.html',
  styleUrls: ['./listar-produto.component.scss']
})
export class ListarProdutoComponent implements OnInit {

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
