import model.component.administrator_operate as adm_ope

class Administrator:

    employee_list = list()
    user_list = list()

    def __init__(self):
        pass
    def add_employee(self,employeename,password):
        adm_ope.create_employee(employeename, password)
    def update_employee(self,employeename):
        pass
    def delete_employee(self,employeename):
        adm_ope.delete_employee(employeename)
    def get_instance(self):
        administrator = Administrator()
        return administrator


