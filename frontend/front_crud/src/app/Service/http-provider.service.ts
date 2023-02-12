import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { WebApiService } from './web-api.service';

var apiUrl = "http://localhost:8100";

var httpLink = {
  getAllCategory: apiUrl + "/api/categories/getallcategory",
  deleteCategoryById: apiUrl + "/api/categories/deletecategorybyid",
  getCategoryDetailById: apiUrl + "/api/categories/getcategorybyid",
  saveCategory: apiUrl + "/api/categories/createcategory"
}
@Injectable({
  providedIn: 'root'
})
export class HttpProviderService {
  constructor(private webApiService: WebApiService) { }

  public getAllCategory(): Observable<any> {
    return this.webApiService.get(httpLink.getAllCategory);
  }
  public deleteCategoryById(model: any): Observable<any> {
    return this.webApiService.post(httpLink.deleteCategoryById + '/' + model, "");
  }
  public getCategoryDetailById(model: any): Observable<any> {
    return this.webApiService.get(httpLink.getCategoryDetailById + '/' + model);
  }
  public saveCategory(model: any): Observable<any> {
    return this.webApiService.post(httpLink.saveCategory, model);
  }
}
