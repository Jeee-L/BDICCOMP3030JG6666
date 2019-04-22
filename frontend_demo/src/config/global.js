var user = {
    first_name: "",
    last_name: "",
    username: "Dear Customer",
    password: "",
    phone_num: "",
    passport_num: "",
    email: "",
    birthday: new Date(),
    address: "",
    order_list: ""
}

var employee = {
    username: "",
    password: ""
}

var administrator = {
    username: "",
    password: ""
}

export default {
    install(Vue, options){
        Vue.prototype.$user = user;
        Vue.prototype.$employee = employee;
        Vue.prototype.$administrator = administrator;
    }
}

