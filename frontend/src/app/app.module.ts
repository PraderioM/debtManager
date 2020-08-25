import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';
import { GroupComponent } from './group/group.component';
import {HttpClientModule} from '@angular/common/http';
import { GroupAddingComponent } from './home/group-adding/group-adding.component';
import { SummaryComponent } from './group/summary/summary.component';
import { PeriodicFlowsComponent } from './group/periodic-flows/periodic-flows.component';
import { ReceiverBurdenComponent } from './group/periodic-flows/receiver-burden/receiver-burden.component';
import { PeriodicFlowEditionComponent } from './group/periodic-flows/periodic-flow-edition/periodic-flow-edition.component';
import { MembersComponent } from './group/members/members.component';
import { MemberEditionComponent } from './group/members/member-edition/member-edition.component';
import { FlowsComponent } from './group/flows/flows.component';
import { FlowEditionComponent } from './group/flows/flow-edition/flow-edition.component';
import { SettingsComponent } from './group/settings/settings.component';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    GroupComponent,
    GroupAddingComponent,
    SummaryComponent,
    PeriodicFlowsComponent,
    ReceiverBurdenComponent,
    PeriodicFlowEditionComponent,
    MembersComponent,
    MemberEditionComponent,
    FlowsComponent,
    FlowEditionComponent,
    SettingsComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule
  ],
  providers: [HttpClientModule],
  bootstrap: [AppComponent]
})
export class AppModule { }
