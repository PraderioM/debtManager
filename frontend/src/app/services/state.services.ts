import {HttpClient, HttpParams} from '@angular/common/http';
import {Injectable} from '@angular/core';
import {Group} from './models/group';

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
      .get<Group[]>(this.backendURL + '/get-group-list')
      .toPromise();
  }

  async verifyConnection(userToken: string): Promise<void> {
    await this.http
      .post(this.backendURL + '/verify-connection',
        {token: userToken})
      .toPromise();
  }
}
