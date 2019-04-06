from www.model.component.database_basic.whats_your_name import Claim,db
from www.model.component.insurance_operate import __search_insurance

def add_claim(dict):
    'insurance_id,id,employee_id,reason,status'
    assert (__search_insurance(id) is not None), 'No such insurance id'
    db.session.add(Claim(insurance_id=dict['insurance_id'], employee_id=dict['employee_id'], reason=dict['reason'], status=dict['status']))
    db.session.commit()
    return 'Create Claim successfully'

def __search_claim(id):
    return Claim.query.filter_by(id=id).first()

def cancel_claim(id):
    claim = __search_claim(id)
    assert(claim is not None), 'No such Claim'
    claim.status = 'cancel'
    return 'cancel Successfully'

def change_staue(id, state):
    claim = __search_claim(id)
    assert claim is not None,'No such Claim'
    claim.status = state
    return 'Change successfully'