<template>
  <div>
    <!-- begin #header -->
    <div id="header" class="header navbar-default">
      <!-- begin navbar-header -->
      <div class="navbar-header">
        <button
          type="button"
          class="navbar-toggle pull-right"
          v-on:click="toggleMobileRightSidebar"
          v-if="pageOptions.pageWithTwoSidebar"
        >
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
        </button>
        <button
          type="button"
          class="navbar-toggle pull-left"
          v-on:click="toggleMobileSidebar"
          v-if="pageOptions.pageWithTwoSidebar"
        >
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
        </button>
        <router-link to="/dashboard/v2" class="navbar-brand">
          <span class="navbar-logo"></span>
          <b>{{$t('m.name')}}</b>
          {{$t('m.name2')}}
        </router-link>
        <button
          type="button"
          class="navbar-toggle"
          v-on:click="toggleMobileSidebar"
          v-if="!pageOptions.pageWithTwoSidebar && (!pageOptions.pageWithTopMenu && !pageOptions.pageWithoutSidebar)"
        >
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
        </button>
        <button
          type="button"
          class="navbar-toggle"
          v-on:click="toggleMobileTopMenu"
          v-if="pageOptions.pageWithTopMenu && pageOptions.pageWithoutSidebar"
        >
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
        </button>
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
        <li>
          <form class="navbar-form" v-on:submit="checkForm">
            <div class="form-group">
              <input type="text" class="form-control" :placeholder="$t('m.pek')">
              <button type="submit" class="btn btn-search">
                <i class="fa fa-search"></i>
              </button>
            </div>
          </form>
        </li>
        <li class="dropdown navbar-language" v-if="pageOptions.pageWithLanguageBar">
          <b-dropdown variant="link" menu-class="p-b-0">
            <template slot="button-content">
              <span
                class="flag-icon"
                title="language"
                v-bind:class="{'flag-icon-ie': this.$t('m.language') == 'English', 'flag-icon-cn': this.$t('m.language') == '简体中文'}"
              ></span>
              <span class="name">{{$t('m.language')}}</span>
              <b class="caret"></b>
            </template>
            <b-dropdown-item
              href="javascript:;"
              v-on:click="changeLangEn()"
              style="margin-bottom: 10px"
            >
              <span class="flag-icon flag-icon-ie" title="us"></span> English
            </b-dropdown-item>
            <b-dropdown-item
              href="javascript:;"
              v-on:click="changeLangCn()"
              style="margin-bottom: 10px"
            >
              <span class="flag-icon flag-icon-cn" title="cn"></span> 简体中文
            </b-dropdown-item>
          </b-dropdown>
        </li>
        <li class="dropdown navbar-user">
          <b-dropdown variant="link" menu-class="dropdown-menu-right">
            <template slot="button-content">
              <span class="d-none d-md-inline">{{$store.state.username}}</span>
              <b class="caret"></b>
            </template>
            <b-dropdown-item href="javascript:;">{{$t('m.edit')}}</b-dropdown-item>
            <b-dropdown-divider></b-dropdown-divider>
            <b-dropdown-item href="javascript:;" v-on:click="logout()">{{$t('m.logout')}}</b-dropdown-item>
          </b-dropdown>
        </li>
        <li class="divider d-none d-md-block" v-if="pageOptions.pageWithTwoSidebar"></li>
      </ul>
      <!-- end header navigation right -->
    </div>
    <!-- end #header -->
  </div>
</template>

<script>
import PageOptions from "../../config/PageOptions.vue";
import { delCookie } from "../../assets/js/cookie.js";
import axios from "axios";

export default {
  name: "Header",
  data() {
    return {
      pageOptions: PageOptions,
    };
  },
  methods: {
    changeLangEn() {
      localStorage.setItem("locale", "en");
      this.$i18n.locale = localStorage.getItem("locale");
    },
    changeLangCn() {
      localStorage.setItem("locale", "cn");
      this.$i18n.locale = localStorage.getItem("locale");
    },
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
    },
    logout() {
      axios
        .post("/logout/", obj)
        .then(res)
        .catch(function(error) {
          console.log(error);
        });
      delCookie("user");
      this.$router.push("/");
    }
  }
};
</script>
