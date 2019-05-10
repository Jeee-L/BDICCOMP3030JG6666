import { setCookie, getCookie } from "../assets/js/cookie.js";
var user = getCookie("user");

var baggageDefault = [{
    insurance_order_id: "MNKD73DR",
    username: "Customer",
    flight_number: "ED234",
    luggage_width: 80,
    luggage_height: 80,
    luggage_image_outside: null,
    luggage_image_inside: "../components/img/baggage_interior.png",
    remark: "This baggage is really expensive.",
    select_img: [],
    sumPrice: 1756,
    claim_id: null,
    date: new Date(),
}]

var claimDefault = [{
    insurance_id: "1739528",
    insurance_order_id: "MNKD73DR",
    username: "Customer",
    employee_id: "e@145",
    reason: "Lost in the airport.",
    state: "-1",
    lost_time: new Date().toISOString().substr(0, 10),
    lost_place: "Beijing Capital Airport",
    date: new Date().toISOString().substr(0, 10),
    remark: ""
},
{
    insurance_id: "1739528",
    insurance_order_id: "MNKD73DR",
    username: "Customer",
    employee_id: "e@145",
    reason: "Lost in the airport.",
    state: "1",
    lost_time: new Date().toISOString().substr(0, 10),
    lost_place: "Beijing Capital Airport",
    date: new Date().toISOString().substr(0, 10),
    remark: ""
},
{
    insurance_id: "1739528",
    insurance_order_id: "MNKD73DR",
    username: "Customer",
    employee_id: "e@145",
    reason: "Lost in the airport.",
    state: "0",
    lost_time: new Date().toISOString().substr(0, 10),
    lost_place: "Beijing Capital Airport",
    date: new Date().toISOString().substr(0, 10),
    remark: ""
}
]



var user = {
    first_name: user.first_name ? user.first_name: "",
    last_name: user.last_name ? user.last_name: "",
    username: user.username ? user.username: "Customer",
    avatar: require("../components/img/avatar.jpg"),
    password: user.password ? user.password: "",
    phone_num: user.phone_num ? user.phone_num: "",
    passport_num: user.passport_num ? user.passport_num: "",
    email: user.email ? user.email: "",
    birthday: user.birthday ? user.birthday: new Date(),
    address: user.address ? user.address: "",
    insurance_list: [],
    insurance_order_list: baggageDefault,
    claim_list: claimDefault
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

