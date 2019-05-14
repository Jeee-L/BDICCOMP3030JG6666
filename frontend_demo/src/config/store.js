import Vue from 'vue'
import Vuex from 'vuex'
import axios from "axios";
import { resolve } from 'path';

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

        if (userInfo.avatar != null) {
            state.avatar = userInfo.avatar
            localStorage.setItem('avatar', userInfo.avatar)
        } else {
            state.avatar = ''
            localStorage.setItem('avatar', '')
        }

        state.password = userInfo.password
        localStorage.setItem('password', userInfo.password)

        state.phone_num = userInfo.phone_num
        localStorage.setItem('phone_num', userInfo.phone_num)

        state.passport_num = userInfo.passport_num
        localStorage.setItem('passport_num', userInfo.passport_num)

        state.email = userInfo.email
        localStorage.setItem('email', userInfo.email)

        state.birthday = userInfo.birthday
        localStorage.setItem('email', userInfo.birthday)

        state.address = userInfo.address
        localStorage.setItem('address', userInfo.address)
    },
    handleCustomerInfoNoAv: (state, userInfo) => {

        state.username = userInfo.username
        localStorage.setItem('username', userInfo.username)

        state.first_name = userInfo.first_name
        localStorage.setItem('first_name', userInfo.first_name)

        state.last_name = userInfo.last_name
        localStorage.setItem('last_name', userInfo.last_name)

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

        // state.insurance_list = '';
        // localStorage.setItem('insurance_list', '');
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
    handleInsuranceInfo: (state, insurance_order_list) => {
        state.insurance_order_list = insurance_order_list;
        localStorage.setItem('insurance_order_list', insurance_order_list);

        var time = [];
        var amount = [];
        var label = [];
        var price = [];
        var date = [];

        if (insurance_order_list.amount_of_money) {
            amount.push(insurance_order_list.remaining_money);
            time.push(insurance_order_list.remaining_time);
        } else {
            for (var i = 0; i < insurance_order_list.length; i++) {
                if (insurance_order_list[i].state == '1') {
                    time.push(insurance_order_list[i].remaining_time);
                    amount.push(insurance_order_list[i].remaining_money);
                    label.push(insurance_order_list[i].insurance_order_id);
                    price.push(insurance_order_list[i].sumPrice);
                    date.push(insurance_order_list[i].date);
                }
            }
            if (label.length == 0) {
                amount.push(insurance_order_list[0].remaining_money);
                time.push(insurance_order_list[0].remaining_time);
            }
        }

        label.push('RM');
        price.push(amount[0]);

        state.insurance_time = time
        localStorage.setItem('insurance_time', time)

        state.insurance_amount = amount
        localStorage.setItem('insurance_amount', amount)

        state.insurance_order_labels = label
        localStorage.setItem('insurance_order_labels', label)

        state.insurance_order_prices = price
        localStorage.setItem('insurance_order_prices', price)

        state.insurance_order_dates = date
        localStorage.setItem('insurance_order_dates', date)
    },
    handleInsuranceInfoAll: (state, insurance_order_list) => {
        state.insurance_order_list = insurance_order_list;
        localStorage.setItem('insurance_order_list', insurance_order_list);
    },
    handleInsurance: (state, insurance) => {
        state.insurance_list = insurance
        localStorage.setItem('insurance_list', insurance)
    }
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
    insurance_time: '' || localStorage.getItem('insurance_time'),
    insurance_amount: '' || localStorage.getItem('insurance_amount'),

    insurance_order_list: null || localStorage.getItem('insurance_order_list'),
    insurance_order_labels: '' || localStorage.getItem('insurance_order_labels'),
    insurance_order_prices: '' || localStorage.getItem('insurance_order_prices'),
    insurance_order_dates: '' || localStorage.getItem('insurance_order_dates'),

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
    insurance_time: (state) => state.insurance_time,
    insurance_amount: (state) => state.insurance_amount,

    insurance_order_list: (state) => state.insurance_order_list,
    insurance_order_labels: (state) => state.insurance_order_labels,
    insurance_order_prices: (state) => state.insurance_order_prices,
    insurance_order_dates: (state) => state.insurance_order_dates,

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
                case 'No such order':
                    return this.$t('m.e_order');
                default:
                    return;
            }
        };
        Vue.prototype.requestData = function () {
            var requireInfo = {
                username: this.$store.getters.username
            };
            if (this.$store.state.insurance_list != '') {
                axios
                    .post("/list_user_all_insurance_order", requireInfo)
                    .then(res => {
                        var response = JSON.parse(JSON.stringify(res.data));
                        this.$store.commit("handleInsuranceInfo", response);
                        if (!response.remaining_time){
                            this.checkClaim();
                        }
                    })
                    .catch(function (error) {
                        console.log(error);
                    });
            }
        };
        Vue.prototype.requestInsurance = function () {
            var requireInfo = {
                username: this.$store.getters.username
            };
            axios
                .post("/list_all_user_insurances", requireInfo)
                .then(res => {
                    var response = JSON.parse(JSON.stringify(res.data));
                    this.$store.commit("handleInsurance", response);

                    if (this.$store.state.insurance_list != "" && this.$store.state.insurance_list != null) {
                        this.requestData();
                    }
                })
                .catch(function (error) {
                    console.log(error);
                });
        },
        Vue.prototype.checkClaim = function () {
            var requireInfo = {
                username: this.$store.getters.username
              };
              var obj = JSON.stringify(requireInfo);
              axios
                .post("/list_user_all_claim", obj)
                .then(res => {
                  var response = JSON.parse(JSON.stringify(res.data));
                  var claim_list = [];
                  for (var i = 0; i < response.length; i++) {
                    if (response[i].state != "-2") {
                      claim_list[claim_list.length] = response[i];
                    }
                  }
                  this.$store.state.claim_list = claim_list;
                })
                .catch(function(error) {
                  console.log(error);
                });
        }
    }
}