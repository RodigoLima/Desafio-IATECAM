import { Router, ActivatedRoute } from '@angular/router';
import { CategoriaService } from './../categoria.service';
import { Categoria } from './../categoria';
import { Component } from '@angular/core';

@Component({
  selector: 'app-editar-categoria',
  templateUrl: './editar-categoria.component.html',
  styleUrls: ['./editar-categoria.component.scss']
})
export class EditarCategoriaComponent {
  categoria: Categoria = {
    id: 0,
    name: ''
  }

  constructor(
    private service: CategoriaService,
    private router: Router,
    private route: ActivatedRoute
  ) { }

  ngOnInit(): void {
    const id = this.route.snapshot.paramMap.get('id')
    this.service.get_by_id(parseInt(id!)).subscribe((categoria) => {
      this.categoria = categoria
    })
  }

  editar_Categoria() {
    this.service.update(this.categoria).subscribe(() => {
      this.router.navigate(['/listarCategoria'])
    })

  }

  cancelar_edicao() {
    this.router.navigate(['/listarCategoria'])
  }

}
