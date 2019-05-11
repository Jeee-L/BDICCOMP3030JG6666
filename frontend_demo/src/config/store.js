import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const actions = {}
const mutations = {
    handleCustomerInfo: (state, userInfo) => {

        state.username = userInfo.username
        localStorage.setItem('username', userInfo.username)

        state.first_name = userInfo.first_name
        localStorage.setItem('first_name', userInfo.first_name)

        state.last_name = userInfo.last_name
        localStorage.setItem('last_name', userInfo.last_name)

        state.avatar = userInfo.avatar
        localStorage.setItem('avatar', userInfo.avatar)

        state.password = userInfo.password
        localStorage.setItem('password', userInfo.password)

        state.phone_num = userInfo.phone_num
        localStorage.setItem('phone_num', userInfo.phone_num)

        state.passport_num = userInfo.passport_num
        localStorage.setItem('passport_num', userInfo.passport_num)

        state.email = userInfo.email
        localStorage.setItem('email', userInfo.email)

        state.birthday = userInfo.birthday
        localStorage.setItem('birthday', userInfo.birthday)

        state.address = userInfo.address
        localStorage.setItem('address', userInfo.address)

        state.insurance_list = userInfo.insurance_list
        localStorage.setItem('insurance_list', userInfo.insurance_list)

        state.insurance_order_list = userInfo.insurance_order_list
        localStorage.setItem('insurance_order_list', userInfo.insurance_order_list)

        state.claim_list = userInfo.claim_list
        localStorage.setItem('claim_list', userInfo.claim_list)
    },
    handleAvatar: (state, avatar) => {
        state.avatar = avatar;
        localStorage.setItem('avatar', avatar);
    },
    handleInsurance: (state, insurance_list) => {
        state.insurance_list = insurance_list;
        localStorage.setItem('insurance_list', insurance_list);
    },
    handleEmployee: (state, employee) => {
        state.employee_id = employee.employee_id;
        localStorage.setItem('employee_id', employee.employee_id);

        state.employee_password = employee.employee_password;
        localStorage.setItem('employee_password', employee.employee_password);

        state.username = employee.employee_id;
        localStorage.setItem('username', employee.employee_id);
    },
}
const state = {
    username: '' || localStorage.getItem('username'),
    first_name: '' || localStorage.getItem('first_name'),
    last_name: '' || localStorage.getItem('last_name'),
    avatar: '' || localStorage.getItem('avatar'),
    password: '' || localStorage.getItem('password'),
    phone_num: '' || localStorage.getItem('phone_num'),
    passport_num: '' || localStorage.getItem('passport_num'),
    email: '' || localStorage.getItem('email'),
    birthday: '' || localStorage.getItem('birthday'),
    address: '' || localStorage.getItem('address'),
    insurance_list: '' || localStorage.getItem('insurance_list'),
    insurance_order_list: '' || localStorage.getItem('insurance_order_list'),
    claim_list: '' || localStorage.getItem('claim_list'),

    employee_id: '' || localStorage.getItem('employee_id'),
    employee_password: '' || localStorage.getItem('employee_password'),
}
const getters = {
    username: (state) => state.username,
    first_name: (state) => state.first_name,
    last_name: (state) => state.last_name,
    avatar: (state) => state.avatar,
    password: (state) => state.password,
    phone_num: (state) => state.phone_num,
    passport_num: (state) => state.passport_num,
    email: (state) => state.email,
    birthday: (state) => state.birthday,
    address: (state) => state.address,
    insurance_list: (state) => state.insurance_list,
    insurance_order_list: (state) => state.insurance_order_list,
    claim_list: (state) => state.claim_list,

    employee_id: (state) => state.employee_id,
    employee_password: (state) => state.employee_password,
}

const store = new Vuex.Store({
    actions,
    mutations,
    state,
    getters
})
export default {
    install(Vue, options) {
        Vue.prototype.$store = store;
        Vue.prototype.showError = function (error_msg) {
            switch (error_msg) {
                case 'No such user':
                    return this.$t('m.e_user');
                case 'Password is not correct':
                    return this.$t('m.e_password');
                case 'Username already exist':
                    return this.$t('m.e_d_user');
                case 'The new password is same as the old one':
                    return this.$t('m.e_d_password');
                case 'The length of reason should less than 300 characters':
                    return this.$t('m.e_reason');
                case 'The length of remark should less than 300 characters':
                    return this.$t('m.e_remark');
                case 'The length of lost place should less than 100 characters':
                    return this.$t('m.e_place');
                case 'Cumulative compensation has reached the upper limit of compensation':
                    return this.$t('m.e_over_price');
                case 'This insurance is overdue':
                    return this.$t('m.e_overdue');
                case 'Unknown error':
                    return this.$t('m.e_unknown');
                default:
                    return;
            }
        }
    }
}