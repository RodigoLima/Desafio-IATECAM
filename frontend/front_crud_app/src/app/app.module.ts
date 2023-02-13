import { ProdutoComponent } from './componentes/produtos/produto/produto.component';

import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { CriarCategoriaComponent } from './componentes/categorias/criar-categoria/criar-categoria.component';
import { ListarCategoriasComponent } from './componentes/categorias/listar-categorias/listar-categorias.component';
import { CategoriaComponent } from './componentes/categorias/categoria/categoria.component';
import { ExcluirCategoriaComponent } from './componentes/categorias/excluir-categoria/excluir-categoria.component';
import { EditarCategoriaComponent } from './componentes/categorias/editar-categoria/editar-categoria.component';
import { CriarProdutoComponent } from './componentes/produtos/criar-produto/criar-produto.component';
import { EditarProdutoComponent } from './componentes/produtos/editar-produto/editar-produto.component';
import { ExcluirProdutoComponent } from './componentes/produtos/excluir-produto/excluir-produto.component';
import { ListarProdutoComponent } from './componentes/produtos/listar-produto/listar-produto.component';



@NgModule({
  declarations: [
    AppComponent,
    CriarCategoriaComponent,
    ListarCategoriasComponent,
    CategoriaComponent,
    ProdutoComponent,
    ExcluirCategoriaComponent,
    EditarCategoriaComponent,
    CriarProdutoComponent,
    EditarProdutoComponent,
    ExcluirProdutoComponent,
    ListarProdutoComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
