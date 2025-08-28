import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'pnx-calc-module',
  templateUrl: './module.component.html',
  styleUrls: ['./module.component.css'],
})
export class ModuleComponent implements OnInit {
  description: string;
  titleModule: string;
  indicators: Array<any> = [];

  constructor() {}

  ngOnInit() {
    this.titleModule = "Calculatrice";
    this.description = "C'est le module calculatrice";
    this.indicators = [
      {id: 1, name: "foo"},
      {id: 2, name: "bar"},
    ];
  }
}
