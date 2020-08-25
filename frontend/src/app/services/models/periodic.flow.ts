import {Member} from './member';

export class ReceiverBurden {
  constructor(public receiver: Member, public burden: number) { }
}

export class PeriodicFlow {
  constructor(public issuer: Member, public period: number, public payDay: number, public lastPayed: string,
              public receiverList: ReceiverBurden[],  public amountPayed?: number, public isUpdateAutomatic: boolean = true) { }
}
