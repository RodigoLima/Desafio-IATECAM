import { Categoria } from './../categorias/categoria';
import { Produto } from './produto';
import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class ProdutoService {
  private readonly API = 'http://127.0.0.1:8000/api/products'

  constructor(private http: HttpClient) {}

  get_all():Observable<Produto[]> {
    return this.http.get<Produto[]>('http://127.0.0.1:8000/api/products/getallproduct',);
  }

  create(produto: Produto):Observable<Produto> {

    return this.http.post<Produto>('http://127.0.0.1:8000/api/products/createproduct', produto);
  }

  update(id: Number, params: any) {
    const url = `${this.API}/updateproductbyid`
    return this.http.put(`${url}/${id}`, params);
  }


  delete(id: Number): Observable<Produto>
  {
    const url = `${this.API}/deleteproductbyid/${id}`
    return this.http.delete<Produto>(url)
  }

  get_categorianame_by_id(id: Number): Observable<Categoria>
  {
    const url = `${this.API}/getcategorybyid/${id}`
    return this.http.get<Categoria>(url)
  }

  get_by_id(id: Number): Observable<Produto>
  {
    const url = `${this.API}/getproductbyid/${id}`
    return this.http.get<Produto>(url)
  }

}

