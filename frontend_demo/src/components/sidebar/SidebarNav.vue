<template>
  <!-- begin sidebar nav -->
  <ul class="nav" v-if="menus">
    <li class="nav-header">{{$t('m.navigation')}}</li>
    <template v-for="menu in menus">
      <sidebar-nav-list
        ref="sidebarNavList"
        v-bind:menu="menu"
        v-bind:scrollTop="scrollTop"
        v-bind:key="menu.path"
        v-bind:status="menu.status"
        v-on:collapse-other="handleCollapseOther(menu)"
      ></sidebar-nav-list>
    </template>
    <!-- begin sidebar minify button -->
    <li>
      <a href="javascript:;" class="sidebar-minify-btn" v-on:click="handleSidebarMinify()">
        <i class="fa fa-angle-double-left"></i>
      </a>
    </li>
    <!-- end sidebar minify button -->
  </ul>
  <!-- end sidebar nav -->
</template>

<script>
import SidebarNavList from "./SidebarNavList.vue";
import PageOptions from "../../config/PageOptions.vue";

export default {
  name: "SidebarNav",
  props: ["scrollTop"],
  components: {
    SidebarNavList
  },
  data() {
    return {
      menus: [
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
      ],
      pageOptions: PageOptions
    };
  },
  methods: {
    handleCollapseOther: function(menu) {
      for (var i = 0; i < this.menus.length; i++) {
        this.$refs.sidebarNavList[i].collapse(menu);
      }
    },
    handleSidebarMinify: function() {
      this.pageOptions.pageSidebarMinified = !this.pageOptions
        .pageSidebarMinified;
    }
  }
};
</script>
