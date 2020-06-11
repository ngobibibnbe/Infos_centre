import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import {
   MatButtonModule
} from '@angular/material/button';
import { MatToolbarModule}from '@angular/material/Toolbar';
import { MatIconModule}from '@angular/material/Icon';
import { MatBadgeModule}from '@angular/material/Badge';
import { MatSidenavModule}from '@angular/material/Sidenav';
import { MatListModule}from '@angular/material/List';
import { MatGridListModule}from '@angular/material/Grid-list';
import { MatFormFieldModule}from '@angular/material/form-field';
import { MatInputModule}from '@angular/material/Input';
import { MatSelectModule}from '@angular/material/Select';
import { MatRadioModule}from '@angular/material/Radio';
import { MatDatepickerModule}from '@angular/material/datepicker';
import { MatChipsModule}from '@angular/material/Chips';
import { MatTableModule}from '@angular/material/Table';
import { MatTooltipModule}from '@angular/material/Tooltip';
import { MatPaginatorModule}from '@angular/material/Paginator';




@NgModule({
   imports: [
      CommonModule,
      MatButtonModule,
      MatToolbarModule,
      MatIconModule,
      MatSidenavModule,
      MatBadgeModule,
      MatListModule,
      MatGridListModule,
      MatFormFieldModule,
      MatInputModule,
      MatSelectModule,
      MatRadioModule,
      MatDatepickerModule,
      MatChipsModule,
      MatTooltipModule,
      MatTableModule,
      MatPaginatorModule
   ],
   exports: [
      MatButtonModule,
      MatToolbarModule,
      MatIconModule,
      MatSidenavModule,
      MatBadgeModule,
      MatListModule,
      MatGridListModule,
      MatInputModule,
      MatFormFieldModule,
      MatSelectModule,
      MatRadioModule,
      MatDatepickerModule,
      MatChipsModule,
      MatTooltipModule,
      MatTableModule,
      MatPaginatorModule
   ],
   providers: [
      MatDatepickerModule,
   ]
})

export class AngularMaterialModule { }