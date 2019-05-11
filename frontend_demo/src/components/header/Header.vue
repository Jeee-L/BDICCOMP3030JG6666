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
            <b-dropdown-item href="javascript:;" v-on:click="updateProfile()">{{$t('m.edit')}}</b-dropdown-item>
            <b-dropdown-divider></b-dropdown-divider>
            <b-dropdown-item href="javascript:;" v-on:click="logout()">{{$t('m.logout')}}</b-dropdown-item>
          </b-dropdown>
        </li>
        <li class="divider d-none d-md-block" v-if="pageOptions.pageWithTwoSidebar"></li>
      </ul>
      <!-- end header navigation right -->
    </div>
    <!-- end #header -->

    <!-- begin change password modal -->
    <b-modal
      id="modalDialog1"
      v-model="showModal"
      :cancel-title="$t('m.tcancel')"
      cancel-variant="white"
      @cancel="cancelChange()"
      @ok="submitPassword()"
      :ok-title="$t('m.tu')"
      ok-variant="info"
      :title="$t('m.cp')"
    >
      <div class="card-body">
        <label class="control-label">
          {{$t('m.old_password')}}
          <span class="text-danger">*</span>
        </label>
        <br>
        <small>{{$t('m.thepassword')}}</small>
        <br>
        <br>
        <div class="row m-b-15">
          <div class="col-md-12">
            <input
              type="text"
              class="form-control"
              :placeholder="$t('m.old_password')"
              :name="$t('m.old_password')"
              v-validate="{ required: true, regex:/^[_!?,.*#a-zA-Z0-9]{6,20}$/ }"
              v-bind:class="{'is-invalid': errors.has($t('m.old_password'))}"
              v-model="params.old_password"
            >
            <span style="color: red !important;">{{ errors.first($t('m.old_password')) }}</span>
          </div>
        </div>
        <br>
        <form action="#">
          <label class="control-label">
            {{$t('m.password')}}
            <span class="text-danger">*</span>
          </label>
          <div class="row m-b-15">
            <div class="col-md-12">
              <input
                type="password"
                class="form-control"
                :placeholder="$t('m.password')"
                :name="$t('m.password')"
                ref="password"
                v-validate="{ required: true, regex:/^[_!?,.*#a-zA-Z0-9]{6,20}$/ }"
                v-bind:class="{'is-invalid': errors.has($t('m.password'))}"
                v-model="params.new_password"
              >
              <span style="color: red !important;">{{ errors.first($t('m.password')) }}</span>
            </div>
          </div>
          <label class="control-label">
            {{$t('m.confirm')}}
            <span class="text-danger">*</span>
          </label>
          <div class="row m-b-15">
            <div class="col-md-12">
              <input
                v-validate="{required: true, is: params.new_password}"
                :name="$t('m.confirm')"
                type="password"
                class="form-control"
                :placeholder="$t('m.ppag')"
                v-bind:class="{'is-invalid': errors.has('confirm_password')}"
                v-model="params.confirm_password"
              >
              <div
                v-if="errors.has($t('m.confirm'))"
                style="color: red;"
              >{{ errors.first($t('m.confirm')) }}</div>
            </div>
          </div>
          <p>
            <small class="text-muted">* {{$t('m.newpw')}}</small>
          </p>
        </form>
      </div>
    </b-modal>
    <!-- end change password modal -->
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

      showModal: false,

      params: {
        employeeid: "",
        old_password: "",
        new_password: "",
        confirm_password: ""
      }
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
    updateProfile() {
      if (this.$store.state.username == "e@emp123") {
        this.showModal = true;
      } else {
        this.$router.push('/customer/info');
      }
    },
    submitPassword() {
      if (this.params.old_password == this.$store.state.employee_password) {
        var obj = JSON.stringify(this.params);

        axios
          .post("/employee_update_password/", obj)
          .then(res => {
            var response = JSON.parse(JSON.stringify(res.data));
            if (response.state == 0) {
              this.swalNotification(
                "error",
                this.showError(response.error_msg)
              );
            } else {
              this.swalNotification("success", "");
              this.$store.state.employee_password = this.params.new_password;
            }
          })
          .catch(function(error) {
            console.log(error);
          });
        this.cancelChange();
      } else {
        this.swalNotification("error", this.$t("m.e_em_password"));
      }
    },
    swalNotification(swalType, error_msg) {
      if (swalType == "success") {
        this.$swal({
          title: this.$t("m.password_s_title"),
          timer: 2000,
          showConfirmButton: false,
          type: swalType
        }).then(setTimeout(() => {}, 2000));
      } else {
        this.$swal({
          title: this.$t("m.password_f_title"),
          text: error_msg,
          timer: 2000,
          showConfirmButton: false,
          type: swalType
        }).then();
      }
    },
    cancelChange() {
      this.showModal = false;
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
      delCookie("user");
      this.$router.push("/");
    }
  }
};
</script>
