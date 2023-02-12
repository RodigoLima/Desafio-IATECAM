import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { CategoriesRoutingModule } from './categories-routing.module';

import { HomeCategoriesComponent } from './home-categories/home-categories.component';
import { CreateComponent } from './create/create.component';



@NgModule({
  declarations: [
    HomeCategoriesComponent,
    CreateComponent
  ],
  imports: [
    CommonModule,
    CategoriesRoutingModule
  ]
})
export class CategoriesModule { }
