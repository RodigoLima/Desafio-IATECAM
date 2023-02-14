import { EditarProdutoComponent } from './componentes/produtos/editar-produto/editar-produto.component';
import { ExcluirProdutoComponent } from './componentes/produtos/excluir-produto/excluir-produto.component';
import { CriarProdutoComponent } from './componentes/produtos/criar-produto/criar-produto.component';
import { ListarProdutoComponent } from './componentes/produtos/listar-produto/listar-produto.component';
import { EditarCategoriaComponent } from './componentes/categorias/editar-categoria/editar-categoria.component';
import { ExcluirCategoriaComponent } from './componentes/categorias/excluir-categoria/excluir-categoria.component';
import { ListarCategoriasComponent } from './componentes/categorias/listar-categorias/listar-categorias.component';
import { CriarCategoriaComponent } from './componentes/categorias/criar-categoria/criar-categoria.component';


import { NgModule, Component, createComponent } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';


const routes: Routes = [
  {
    path: '',
    redirectTo: `listarProduto`,
    pathMatch: 'full'
  },
  {
    path: "listarProduto",
    component: ListarProdutoComponent
  },
  {
    path: "criarProduto",
    component: CriarProdutoComponent
  },
  {
    path: "excluirProduto/:id",
    component: ExcluirProdutoComponent
  },
  {
    path: "editarProduto/:id",
    component: EditarProdutoComponent
  },

  {
    path: "listarCategoria",
    component: ListarCategoriasComponent
  },
  {
    path: "criarCategoria",
    component: CriarCategoriaComponent
  },
  {
    path: "excluirCategoria/:id",
    component: ExcluirCategoriaComponent
  },
  {
    path: "editarCategoria/:id",
    component: EditarCategoriaComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
