import {HttpClient, HttpParams} from '@angular/common/http';
import {Injectable} from '@angular/core';
import {Group} from './models/group';
import {Flow} from './models/flow';
import {PeriodicFlow} from './models/periodic.flow';
import {Member} from './models/member';

@Injectable()
export class StateService {
  backendURL = 'http://192.168.1.19:2121';

  constructor(private http: HttpClient) {
  }

  async getToken(): Promise<string> {
    return await this.http
      .get<string>(this.backendURL + '/get-token')
      .toPromise();
  }

  async getGroupList(): Promise<Group[]> {
    return await this.http
      .get<Group[]>(this.backendURL + '/get-group-list',
                {params: new HttpParams()})
      .toPromise();
  }

  async verifyConnection(userToken: string): Promise<void> {
    await this.http.post<void>(this.backendURL + '/verify-connection',
                               '',
                       {
                         params: new HttpParams().set('token', userToken)
                       }).toPromise();
  }

  async addGroup(token: string, name: string, mg1: string, mg2: string): Promise<void> {
    await this.http.post<void>(this.backendURL + '/add-group',
      '',
      {
        params: new HttpParams().set('token', token).set('name', name).set('mailgun_1', mg1).set('mailgun_2', mg2)
      }).toPromise();
  }

  async getSummary(groupName: string): Promise<Flow[]> {
    return await this.http
      .get<Flow[]>(this.backendURL + '/get-summary',
        {params: new HttpParams().set('group_name', groupName)})
      .toPromise();
  }

  async getPeriodicFlowList(groupName: string): Promise<PeriodicFlow[]> {
    return await this.http
      .get<PeriodicFlow[]>(this.backendURL + '/get-periodic-flows',
        {params: new HttpParams().set('group_name', groupName)})
      .toPromise();
  }

  async getMemberList(groupName: string): Promise<Member[]> {
    return await this.http
      .get<Member[]>(this.backendURL + '/get-members',
        {params: new HttpParams().set('group_name', groupName)})
      .toPromise();
  }

  async removePeriodicFlow(groupName: string, periodicFlowIndex: number): Promise<void> {
    await this.http
      .post<void>(this.backendURL + '/remove-periodic-flow',
        '',
        {params: new HttpParams().set('group_name', groupName).set('id', periodicFlowIndex.toString())})
      .toPromise();
  }
}
