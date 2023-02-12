import { Categories } from './../categories/categories';
import { CategoriesService } from './../categories/categories.service';
import { Component, OnInit } from '@angular/core';


@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})

export class HomeComponent implements OnInit {
  allCategories: Categories[] = [];

  constructor(private CategoriesService: CategoriesService) {}

  ngOnInit(): void {
    this.get_all();
  }

  get_all() {
    this.CategoriesService.get_all().subscribe((data) => {
      this.allCategories = data;
    });
  }
}
