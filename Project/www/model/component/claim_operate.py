

from www.model.component.database_basic.whats_your_name import Claim,db
from www.model.component.insurance_operate import __search_insurance








def add_claim(list):
    'insurance_id,id,employee_id,reason,status'

    if not __search_insurance(list[0]):
        return 'No such insurance_id'
    db.session.add(
        Claim(insurance_id=list[0], employee_id=list[1], reason=list[2], status='Creating'))
    db.session.commit()
    return 'Create Claim successfully'

def __search_claim(id):
    return Claim.query.filter_by(id=id).first()

def cancel_claim(id):
    if not __search_insurance(id):
        return 'No such Claim_id'
    claim = Claim.query.filter_by(id = id).first()
    claim.status = 'cancel'
