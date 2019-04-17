<script>
const sidebarMenu = [
  { path: "/home", icon: "fa fa-th", title: "Home" },
  { path: "/baggage", icon: "fa fa-hdd", title: "Baggage Insurance", 
    children: [
      { path: '/baggage/home', title: "Product Information" },
      { path: '/baggage/insurance', title: "Buy Insurance" },
      { path: '/baggage/register', title: "Register Buggage" },
      { path: '/baggage/order1', title: "Create Order1" },
    ]
  },
  { path: "/employee/order", icon: "fa fa-hdd", title: "Employee Order" },
  { path: "/employee/insurance/table", icon: "fa fa-hdd", title: "Employee Insurance Table" },
  { path: "/login", icon: "fa fa-th", title: "Login" },
  { path: "/register", icon: "fa fa-th", title: "Register" },
  { path: "/crop", icon: "fa fa-th", title: "Crop" }
];

export default sidebarMenu;
</script>
