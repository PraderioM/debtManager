import {Member} from './member';

export class Flow {
  constructor(public issuer: Member, public receiver: Member, public amount: number, public concept: string, public date: string) { }
}
