<script>
import Welcome from "../pages/Welcome.vue";
import Home from "../pages/Home.vue";
import BaggageHome from "../pages/Page-Baggage-Home.vue";
import BaggageOrder from "../pages/Page-Baggage-BuyInsurance.vue";
import BaggageRegister from "../pages/Page-Baggage-RegisterBaggage.vue";
import CustomerCenter from "../pages/Profile-Customer-Center.vue";
import CustomerInfo from "../pages/Profile-Customer-Info.vue";
import Login from "../pages/User-Login.vue";
import Register from "../pages/User-Register.vue";
import Claim from "../pages/Page-Baggage-Claim.vue";
import ProcessResult from "../pages/Page-Baggage-ProcessResult.vue";

import EmployeeHome from "../employee/Page-Employee-Home.vue";
import EmployeeOrder from "../employee/Page-Employee-Insurance.vue";
import EmployeeBaggage from "../employee/Page-Employee-BaggageRegister.vue";
import EmployeeClaim from "../employee/Page-Employee-Claim.vue";

const routes = [
  {path: "/", component: Welcome},
  { path: "/home", component: Home },
  { path: "/baggage/home", component: BaggageHome },
  { path: "/baggage/insurance", component: BaggageOrder },
  { path: "/baggage/register", component: BaggageRegister },
  { path: "/baggage/claim", component: Claim },
  { path: "/baggage/result", component: ProcessResult },
  { path: "/login", component: Login },
  { path: "/register", component: Register },
  { path: "/employee/home", component: EmployeeHome },
  { path: "/employee/insurance", component: EmployeeOrder },
  { path: "/employee/baggage", component: EmployeeBaggage },
  { path: "/employee/claim", component: EmployeeClaim },

  // Profile Pages
  { path: "/customer/center", component: CustomerCenter },
  { path: "/customer/info", component: CustomerInfo }
];

export default routes;
</script>
