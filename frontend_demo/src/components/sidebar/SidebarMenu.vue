<script>
const sidebarMenu = [
  { path: "/home", icon: "fa fa-th", title: 'Home' },
  { path: "/baggage", icon: "fa fa-hdd", title: 'Baggage Insurance', 
    children: [
      { path: '/baggage/home', title: 'Product Information'},
      { path: '/baggage/insurance', title: 'Buy Insurance' },
      { path: '/baggage/register', title: 'Register Buggage' },
      { path: '/baggage/claim', title: 'Claim Lost Baggage' },
      { path: '/baggage/result', title: 'Claim Process Result' },
    ]
  },
  { path: "/login", icon: "fa fa-th", title: 'Login' },
  { path: "/register", icon: "fa fa-th", title: 'Register' },
];

export default sidebarMenu;
</script>
