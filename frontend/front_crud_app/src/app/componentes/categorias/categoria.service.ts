import { Categoria } from './categoria';
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CategoriaService {

  private readonly API = 'http://127.0.0.1:8000/api/categories'

  constructor(private http: HttpClient) {}

  get_all():Observable<Categoria[]> {
    return this.http.get<Categoria[]>('http://127.0.0.1:8000/api/categories/getallcategory',);
  }

  create(categoria: Categoria):Observable<Categoria> {
    return this.http.post<Categoria>('http://127.0.0.1:8000/api/categories/createcategory', categoria);
  }

  update(id: Number, params: any) {
    const url = `${this.API}/updatecategorybyid`
    return this.http.put(`${url}/${id}`, params);
  }



  delete(id: Number): Observable<Categoria>
  {
    const url = `${this.API}/deletecategorybyid/${id}`
    return this.http.delete<Categoria>(url)
  }

  get_by_id(id: Number): Observable<Categoria>
  {
    const url = `${this.API}/getcategorybyid/${id}`
    return this.http.get<Categoria>(url)
  }

}
