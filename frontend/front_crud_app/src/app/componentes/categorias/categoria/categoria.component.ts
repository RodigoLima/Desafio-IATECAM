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

}
