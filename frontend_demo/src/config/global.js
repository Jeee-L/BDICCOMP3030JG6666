var baggageDefault = [{
    id: "MNKD73DR",
    username: "Customer",
    flight_num: "ED234",
    luggage_width: 80,
    luggage_height: 80,
    luggage_image_outside: null,
    luggage_image_inside: "../components/img/baggage_interior.png",
    remark: "This baggage is really expensive.",
    select_img: [],
    sum_price: 1756
}]



var user = {
    first_name: "",
    last_name: "",
    username: "Customer",
    password: "",
    phone_num: "",
    passport_num: "",
    email: "",
    birthday: new Date(),
    address: "",
    insurance_list: [],
    insurance_order_list: baggageDefault,
    claim_list: []
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
    install(Vue, options) {
        Vue.prototype.$user = user;
        Vue.prototype.$employee = employee;
        Vue.prototype.$administrator = administrator;
    }
}

