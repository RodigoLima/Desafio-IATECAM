import { ActivatedRoute, Router } from '@angular/router';
import { ProdutoService } from './../produto.service';
import { Component } from '@angular/core';
import { Produto } from '../produto';

@Component({
  selector: 'app-editar-produto',
  templateUrl: './editar-produto.component.html',
  styleUrls: ['./editar-produto.component.scss']
})
export class EditarProdutoComponent {
  produto: Produto = {
    name: '',
    category: 1,
    price: 1,
    serie: 1
  }

  constructor(
    private service: ProdutoService,
    private router: Router,
    private route: ActivatedRoute
  ) { }

  ngOnInit(): void {
    const id = this.route.snapshot.paramMap.get('id')
    this.service.get_by_id(parseInt(id!)).subscribe((produto) => {
      this.produto = produto
    })
  }

  editar_Produto() {
    this.service.update(this.produto).subscribe(() => {
      this.router.navigate(['/listarProduto'])
    })

  }

  cancelar_edicao() {
    this.router.navigate(['/listarProduto'])
  }

}
