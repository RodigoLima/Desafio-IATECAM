import { Component, OnInit } from '@angular/core';
import { Categories } from '../categories';
import { CategoriesService } from '../categories.service';


@Component({
  selector: 'app-home-categories',
  templateUrl: './home-categories.component.html',
  styleUrls: ['./home-categories.component.scss']
})
export class HomeCategoriesComponent implements OnInit {

  allCategories: Categories[] = [];

  constructor(private categoriesService: CategoriesService) {}

  ngOnInit(): void {
    this.get_all();
  }

  get_all() {
    this.categoriesService.get_all().subscribe((data) => {
      this.allCategories = data;
    });
  }

}
