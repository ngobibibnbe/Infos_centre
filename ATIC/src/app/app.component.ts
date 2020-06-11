import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Location } from '@angular/common';

@Component({
  selector: 'app-root',
  templateUrl: 'app.component.html',
  styleUrls: ['app.component.css']

})

export class AppComponent implements OnInit {
  values: string[] = ['Tag 1', 'Tag 2', 'Tag 4'];

  specialPage: boolean;

  private specialPages: any[] = [
    '/login',
    '/',

    '/pages/register',
    '/pages/lock',
    '/pages/pricing',
    '/pages/single-post',
    '/pages/post-listing'
  ];

  private currentUrl = '';

  constructor(
    private router: Router,
    private location: Location,

  ) {

    this.router.events.subscribe((route:any) => {
      this.currentUrl = this.router.url;

      this.specialPage = this.specialPages.indexOf(this.currentUrl) !== -1;
    console.log(this.currentUrl)
    
    
    });

  }

  ngOnInit(): void {
  }

  goBack(): void {
    this.location.back();
  }
}
