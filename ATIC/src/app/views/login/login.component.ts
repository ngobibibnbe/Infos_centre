import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from 'src/app/auth.service';
@Component({
  selector: 'app-login',
  template: `
  <div style="text-align:center">
    <h1>
      Login
    </h1>
  </div>

  <input #username type='text' placeholder='username'>
  <input #password type='password' placeholder='password'>
  <button (click)="login(username.value, password.value)">login</button>
  <p>{{ error?.message }}</p>
  <p *ngIf="error">{{ error?.error | json }}</p>
  `

})

export class LoginComponent implements OnInit {

  error: any;
  private router: Router;
  private authService: AuthService;

  constructor(

  ) { }

  ngOnInit() {
  }

  login(username: string, password: string) {
    this.authService.logn(username, password).subscribe(
    () => this.router.navigate(['']),
      error => this.error = error
    );
  }
}