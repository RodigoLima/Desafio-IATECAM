import { ActivatedRoute, Router } from '@angular/router';
import { ProdutoService } from './../produto.service';
import { Component } from '@angular/core';
import { Produto } from '../produto';

@Component({
  selector: 'app-excluir-produto',
  templateUrl: './excluir-produto.component.html',
  styleUrls: ['./excluir-produto.component.scss']
})
export class ExcluirProdutoComponent {
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

  excluirProduto() {
    if(this.produto.id) {
      this.service.delete(this.produto.id).subscribe(() => {
        this.router.navigate(['listarProduto'])
      },
      (err) =>{

        this.router.navigate(['listarProduto'])
      }

      )
    }
  }

  cancelarExclusao() {
    this.router.navigate(['listarProduto'])
  }

}
