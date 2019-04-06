<script>
const sidebarMenu = [
  { path: "/home", icon: "fa fa-th", title: "Home" },
  { path: "/baggage", icon: "fa fa-hdd", title: "Baggage Insurance", 
    children: [
      { path: '/baggage/home', title: "Product Information" },
      { path: '/baggage/order', title: "Create Order" },
    ]
  },
  { path: "/employee/order", icon: "fa fa-hdd", title: "Employee Order" },
  { path: "/login", icon: "fa fa-th", title: "Login" },
  { path: "/register", icon: "fa fa-th", title: "Register" }
];

export default sidebarMenu;
</script>
