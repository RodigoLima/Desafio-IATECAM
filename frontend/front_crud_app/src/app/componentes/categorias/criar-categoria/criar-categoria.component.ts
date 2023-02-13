import { CategoriaService } from './../categoria.service';
import { Component, Input } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-criar-categoria',
  templateUrl: './criar-categoria.component.html',
  styleUrls: ['./criar-categoria.component.scss']
})
export class CriarCategoriaComponent {


  categoria = {
    name: ``

  }
  constructor(private service: CategoriaService,
    private router: Router
  ) { }

  criar_categoria() {
    this.service.create(this.categoria).subscribe(() => {
      this.router.navigate(['listarCategoria'])
    })
  }

  cancelar_criacao_categoria() {
    this.router.navigate(['listarCategoria'])
  }


}
