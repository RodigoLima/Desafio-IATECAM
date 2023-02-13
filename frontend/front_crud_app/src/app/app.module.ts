
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
import { ProdutoComponent } from './component/produtos/produto/produto.component';
import { CriarProdutoComponent } from './componentes/produtos/criar-produto/criar-produto.component';
import { EditarProdutoComponent } from './componentes/produtos/editar-produto/editar-produto.component';
import { ExcluirProdutoComponent } from './componentes/produtos/excluir-produto/excluir-produto.component';



@NgModule({
  declarations: [
    AppComponent,
    CriarCategoriaComponent,
    ListarCategoriasComponent,
    CategoriaComponent,
    ExcluirCategoriaComponent,
    EditarCategoriaComponent,
    ProdutoComponent,
    CriarProdutoComponent,
    EditarProdutoComponent,
    ExcluirProdutoComponent
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
