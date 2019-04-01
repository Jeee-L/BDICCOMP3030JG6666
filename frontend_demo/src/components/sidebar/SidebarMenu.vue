<script>
const sidebarMenu = [
  { path: "/", icon: "fa fa-th", title: "Home" },
  { path: "/baggage", icon: "fa fa-hdd", title: "Baggage Insurance", 
    children: [
      { path: '/baggage/home', title: "Product Information" },
      { path: '/baggage/order', title: "Create Order" },
    ]
  },
  { path: "/employee/order", icon: "fa fa-hdd", title: "Employee Order" },
  // { path: "/form", icon: "fa fa-th", title: "Form Insurance" }
];

export default sidebarMenu;
</script>
