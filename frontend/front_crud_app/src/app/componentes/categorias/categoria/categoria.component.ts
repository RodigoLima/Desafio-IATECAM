import { CategoriaService } from './../categoria.service';
import { Categoria } from '../categoria';
import { Component, OnInit , Input} from '@angular/core';

@Component({
  selector: 'app-categoria',
  templateUrl: './categoria.component.html',
  styleUrls: ['./categoria.component.scss']
})
export class CategoriaComponent {

  @Input() categoria: Categoria = {
    id: 1,
    name: ''
  }

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
