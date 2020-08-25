import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';
import { GroupComponent } from './group/group.component';
import {HttpClientModule} from '@angular/common/http';
import { GroupAddingComponent } from './home/group-adding/group-adding.component';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    GroupComponent,
    GroupAddingComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule
  ],
  providers: [HttpClientModule],
  bootstrap: [AppComponent]
})
export class AppModule { }
