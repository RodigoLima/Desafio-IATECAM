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
    path: "criarCategoria",
    component: CriarCategoriaComponent
  },
  {
    path: "listarCategoria",
    component: ListarCategoriasComponent
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
