import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { GN2CommonModule } from '@geonature_common/GN2Common.module';
import { Routes, RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ReactiveFormsModule } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import { HttpClientXsrfModule } from '@angular/common/http';

import { MatSlideToggleModule } from '@angular/material/slide-toggle';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatAutocompleteModule } from '@angular/material/autocomplete';
import { MatSelectModule } from '@angular/material/select';
import { MatInputModule } from '@angular/material/input';
import { MatChipsModule } from '@angular/material/chips';

import {ModuleComponent} from "./components/module/module.component";


// my module routing
const routes: Routes = [
  /** modules  */
  { path: '', component: ModuleComponent },
];

@NgModule({
  declarations: [
      ModuleComponent,
  ],
  imports: [
    GN2CommonModule,
    RouterModule.forChild(routes),
    CommonModule,
    FormsModule,
    ReactiveFormsModule,
    MatSlideToggleModule,
    MatFormFieldModule,
    MatAutocompleteModule,
    MatSelectModule,
    MatInputModule,
    MatChipsModule,
    HttpClientXsrfModule.withOptions({
      headerName: 'token',
    }),
  ],
  providers: [
    HttpClient,
  ],
  bootstrap: [ModuleComponent],
  schemas: [
    // CUSTOM_ELEMENTS_SCHEMA
  ],
})
export class GeonatureModule {}
