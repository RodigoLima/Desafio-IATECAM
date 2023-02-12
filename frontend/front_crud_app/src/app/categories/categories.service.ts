import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpClientModule } from '@angular/common/http';
import { Categories } from './categories';

@Injectable({
  providedIn: 'root',
})



export class CategoriesService {
  constructor(private http: HttpClient) {}

  get_all() {
    return this.http.get<Categories[]>('http://127.0.0.1:8000/api/categories/getallcategory',);
  }

}


