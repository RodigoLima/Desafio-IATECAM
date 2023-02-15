import { CategoriaService } from './../categoria.service';
import { Categoria } from './../categoria';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-listar-categorias',
  templateUrl: './listar-categorias.component.html',
  styleUrls: ['./listar-categorias.component.scss']
})
export class ListarCategoriasComponent implements OnInit {

  listaCategorias: Categoria[] = [];

  constructor( private service: CategoriaService) {}


  ngOnInit(): void {
    this.get_all();
  }

  get_all() {
    this.service.get_all().subscribe((data) => {
      this.listaCategorias = data;
    });
  }



}
