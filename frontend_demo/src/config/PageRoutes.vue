<script>
import Home from "../pages/Home.vue";
import BaggageHome from "../pages/Page-Baggage-Home.vue";
import BaggageOrder from "../pages/Page-Baggage-Order.vue";
import EmployeeOrder from "../pages/Page-Employee-Order.vue";
import CustomerCenter from "../pages/Profile-Customer-Center.vue";
import CustomerInfo from "../pages/Profile-Customer-Info.vue";

const routes = [
  { path: "/", component: Home },
  { path: "/baggage/home", component: BaggageHome },
  { path: "/baggage/order", component: BaggageOrder },
  { path: "/employee/order", component: EmployeeOrder },

  // Profile Pages
  { path: "/customer/center", component: CustomerCenter },
  { path: "/customer/info", component: CustomerInfo }
];

export default routes;
</script>
