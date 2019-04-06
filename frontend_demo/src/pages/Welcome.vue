<template>
  <div>
    <!-- begin #header -->
    <div id="header" class="header navbar-default">
      <!-- begin navbar-header -->
      <div class="navbar-header">
        <router-link to="/dashboard/v2" class="navbar-brand">
          <span class="navbar-logo"></span>
          <b>Hibernia-Sino</b> Travel Insurance
        </router-link>
        <button
          type="button"
          class="navbar-toggle p-0 m-r-0"
          v-on:click="toggleMobileMegaMenu"
          v-if="pageOptions.pageWithMegaMenu"
        >
          <span class="fa-stack fa-lg text-inverse m-t-2">
            <i class="far fa-square fa-stack-2x"></i>
            <i class="fa fa-cog fa-stack-1x"></i>
          </span>
        </button>
      </div>
      <!-- end navbar-header -->

      <header-mega-menu v-if="pageOptions.pageWithMegaMenu"></header-mega-menu>

      <!-- begin header-nav -->
      <ul class="navbar-nav navbar-right">
        <li class="nav-item">
          <a class="nav-link" href="/home">Sign In to Customer Center</a>
        </li>
        <li
          v-if="!pageOptions.pageWithLanguageBar"
          v-bind:class="{ 'hidden-sm': pageOptions.pageWithMegaMenu }"
        >
          <form class="navbar-form" v-on:submit="checkForm">
            <div class="form-group">
              <input type="text" class="form-control" placeholder="Enter keyword">
              <button type="submit" class="btn btn-search">
                <i class="fa fa-search"></i>
              </button>
            </div>
          </form>
        </li>
        <li class="dropdown navbar-language" v-if="pageOptions.pageWithLanguageBar">
          <b-dropdown variant="link" menu-class="p-b-0">
            <template slot="button-content">
              <span class="flag-icon flag-icon-us" title="us"></span>
              <span class="name">EN</span>
              <b class="caret"></b>
            </template>
            <b-dropdown-item href="javascript:;">
              <span class="flag-icon flag-icon-us" title="us"></span> English
            </b-dropdown-item>
            <b-dropdown-item href="javascript:;">
              <span class="flag-icon flag-icon-cn" title="cn"></span> Chinese
            </b-dropdown-item>
            <b-dropdown-item href="javascript:;">
              <span class="flag-icon flag-icon-jp" title="jp"></span> Japanese
            </b-dropdown-item>
            <b-dropdown-item href="javascript:;">
              <span class="flag-icon flag-icon-be" title="be"></span> Belgium
            </b-dropdown-item>
            <b-dropdown-divider class="m-b-0"></b-dropdown-divider>
            <b-dropdown-item href="javascript:;" class="text-center">more options</b-dropdown-item>
          </b-dropdown>
        </li>
      </ul>
      <!-- end header navigation right -->
    </div>
    <!-- end #header -->

    <!-- begin sliding bar -->
    <div style="margin: 20px">
      <b-carousel
        id="carousel1"
        style="text-shadow: 1px 1px 2px #333;"
        controls
        indicators
        background="#ababab"
        :interval="3000"
        img-width="1024"
        img-height="480"
        v-model="slide"
        @sliding-start="onSlideStart"
        @sliding-end="onSlideEnd"
      >
        <!-- Slides with img slot -->
        <b-carousel-slide>
          <img
            slot="img"
            class="d-block img-fluid w-100"
            width="1024"
            height="480"
            src="../assets/img/china-land1.jpg"
            alt="image slot"
          >
        </b-carousel-slide>

        <!-- Slides with img slot -->
        <b-carousel-slide>
          <img
            slot="img"
            class="d-block img-fluid w-100"
            width="1024"
            height="480"
            src="../assets/img/ireland-land2.jpg"
            alt="image slot"
          >
        </b-carousel-slide>

        <!-- Slides with img slot -->
        <!-- Note the classes .d-block and .img-fluid to prevent browser default image alignment -->
        <b-carousel-slide>
          <img
            slot="img"
            class="d-block img-fluid w-100"
            width="1024"
            height="480"
            src="../assets/img/china-land2.jpg"
            alt="image slot"
          >
        </b-carousel-slide>
      </b-carousel>
    </div>
    <!-- end sliding bar -->
  </div>
</template>

<script>
import PageOptions from "../config/PageOptions.vue";

export default {
  name: "Welcome",
  data() {
    return {
      pageOptions: PageOptions
    };
  },
  methods: {
    toggleMobileSidebar() {
      this.pageOptions.pageMobileSidebarToggled = !this.pageOptions
        .pageMobileSidebarToggled;
    },
    toggleMobileRightSidebar() {
      this.pageOptions.pageMobileRightSidebarToggled = !this.pageOptions
        .pageMobileRightSidebarToggled;
    },
    toggleMobileTopMenu() {
      this.pageOptions.pageMobileTopMenu = !this.pageOptions.pageMobileTopMenu;
    },
    toggleMobileMegaMenu() {
      this.pageOptions.pageMobileMegaMenu = !this.pageOptions
        .pageMobileMegaMenu;
    },
    toggleRightSidebar() {
      this.pageOptions.pageRightSidebarToggled = !this.pageOptions
        .pageRightSidebarToggled;
    },
    checkForm: function(e) {
      e.preventDefault();
      this.$router.push({ path: "/extra/search" });
    }
  },
  created() {
    PageOptions.pageEmpty = true;
  },
  beforeRouteLeave(to, from, next) {
    PageOptions.pageEmpty = false;
    next();
  }
};
</script>

<style scoped>
</style>

