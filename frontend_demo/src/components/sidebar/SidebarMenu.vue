<script>
export default {
  data(){
    return{
       sidebarMenu: [
        { path: "/home", icon: "fa fa-th", title: this.$t("m.home") },
        {
          path: "/baggage",
          icon: "fa fa-hdd",
          title: this.$t("m.sbi"),
          children: [
           { path: "/baggage/home", title: this.$t("m.spi") },
           { path: "/baggage/insurance", title: this.$t("m.ssbi") },
           { path: "/baggage/register", title: this.$t("m.srb") },
           { path: "/baggage/claim", title: this.$t("m.sclb") },
           { path: "/baggage/result", title: this.$t("m.scpr") }
          ]
        }
      ]
    }
  }
};
</script>
