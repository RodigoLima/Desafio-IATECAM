import { ActivatedRoute, Router } from '@angular/router';
import { CategoriaService } from './../categoria.service';
import { Categoria } from './../categoria';
import { Component } from '@angular/core';

@Component({
  selector: 'app-excluir-categoria',
  templateUrl: './excluir-categoria.component.html',
  styleUrls: ['./excluir-categoria.component.scss']
})
export class ExcluirCategoriaComponent {

  categoria: Categoria = {
    id: 1,
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

  excluirCategoria() {
    if(this.categoria.id) {
      this.service.delete(this.categoria.id).subscribe(() => {
        this.router.navigate(['listarCategoria'])
      })
    }
  }

  cancelarExclusao() {
    this.router.navigate(['listarCategoria'])
  }

}
