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

  async addMember(token: string, groupName: string, name: string, eMail: string, creditorThr: number, debtorThr: number): Promise<void> {
    await this.http.post<void>(this.backendURL + '/add-member',
      '',
      {
        params: new HttpParams().set('token', token).set('group_name', groupName).set('name', name)
          .set('e_mail', eMail).set('creditor_thr', creditorThr.toString())
          .set('debtor_thr', debtorThr.toString())
      }).toPromise();
  }

  async updateMember(token: string, groupName: string, memberIndex: number,
                     name: string, eMail: string, creditorThr: number, debtorThr: number): Promise<void> {
    await this.http.post<void>(this.backendURL + '/update-member',
      '',
      {
        params: new HttpParams().set('token', token).set('group_name', groupName).set('id', memberIndex.toString())
                                .set('name', name).set('e_mail', eMail).set('creditor_thr', creditorThr.toString())
                                .set('debtor_thr', debtorThr.toString())
      }).toPromise();
  }

  async removeMember(token: string, groupName: string, memberIndex: number): Promise<void> {
    await this.http.post<void>(this.backendURL + '/remove-member',
      '',
      {
        params: new HttpParams().set('token', token).set('group_name', groupName).set('id', memberIndex.toString())
      }).toPromise();
  }

  async addFlow(token: string, groupName: string, issuerName: string, receiverName: string, amount: number): Promise<void> {
    await this.http.post<void>(this.backendURL + '/add-flow',
      '',
      {
        params: new HttpParams().set('token', token).set('group_name', groupName)
                                .set('issuer_name', issuerName).set('receiver_name', receiverName)
                                .set('amount', amount.toString())
      }).toPromise();
  }

  async getFlowList(groupName: string): Promise<Flow[]> {
    return await this.http
      .get<Flow[]>(this.backendURL + '/get-flows',
        {params: new HttpParams().set('group_name', groupName)})
      .toPromise();
  }

  async updateFlow(token: string, flowIndex: number, groupName: string,
                   issuerName: string, receiverName: string,
                   amount: number): Promise<void> {
    await this.http.post<void>(this.backendURL + '/modify-flow',
      '',
      {
        params: new HttpParams().set('token', token).set('group_name', groupName)
          .set('flow_index', flowIndex.toString())
          .set('issuer_name', issuerName).set('receiver_name', receiverName)
          .set('amount', amount.toString())
      }).toPromise();
  }

  async removeFlow(token: string, groupName: string, flowIndex: number): Promise<void> {
    await this.http.post<void>(this.backendURL + '/remove-flow',
      '',
      {
        params: new HttpParams().set('token', token).set('group_name', groupName).set('id', flowIndex.toString())
      }).toPromise();
  }
}
