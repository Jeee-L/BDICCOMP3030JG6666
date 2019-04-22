<template>
  <div>
    <!-- begin login-cover -->
    <div class="login-cover">
      <div class="login-cover-image"></div>
      <div class="login-cover-bg"></div>
    </div>
    <!-- end login-cover -->

    <!-- begin login -->
    <div class="login login-v2" data-pageload-addclass="animated fadeIn">
      <!-- begin brand -->
      <div class="login-header">
        <div class="brand">
          <span class="logo"></span>
          <b>Hibernia-Sino</b> Travel Insurance
          <small>providing the best travel experience between China and Ireland</small>
        </div>
      </div>
      <!-- end brand -->
      <!-- begin login-content -->
      <div class="login-content">
        <div class="form-group m-b-20">
          <input
            type="text"
            class="form-control form-control-lg"
            placeholder="User Name"
            v-model="formData.username"
            required
          >
        </div>
        <div class="form-group m-b-20">
          <input
            type="password"
            class="form-control form-control-lg"
            placeholder="Password"
            v-model="formData.password"
            required
          >
        </div>
        <p v-show="showNotification" style="color: red;">{{notification}}</p>
        <!-- <div class="checkbox checkbox-css m-b-20">
          <input type="checkbox" id="remember_checkbox">
          <label for="remember_checkbox">Remember Me</label>
        </div>-->
        <div class="login-buttons">
          <button v-on:click="login" class="btn btn-success btn-block btn-lg">Sign me in</button>
        </div>
        <div class="m-t-20">
          Not a member yet? Click
          <a href="javascript:;" v-on:click="toRegister">here</a> to register.
        </div>
      </div>
      <!-- end login-content -->
    </div>
    <!-- end login -->
  </div>
</template>

<script>
import PageOptions from "../config/PageOptions.vue";

import axios from "axios";
import { setCookie, getCookie } from "../assets/js/cookie.js";
// import { setTimeout } from "timers";

export default {
  data() {
    return {
      notification: "",
      showNotification: false,
      formData: {
        username: "",
        password: ""
      }
    };
  },
  created() {
    PageOptions.pageEmpty = true;
  },
  beforeRouteLeave(to, from, next) {
    PageOptions.pageEmpty = false;
    next();
  },
  mounted() {
    if (getCookie("username")) {
      this.$router.push({ path: "/home" });
    }
  },
  methods: {
    login() {
      if (this.formData.username == "" || this.formData.password == "") {
        alert("Please enter valid User Name and Password.");
      } else {
        var obj = JSON.stringify(this.formData);
        axios.post("http://localhost:5000/login/", obj).then(res => {
          var response = JSON.parse(JSON.stringify(res.data));
          if (response.state == "-1") {
            this.notification = response.error_msg;
            this.showNotification = true;
          } else if (response.state == "0") {
            this.notification = response.error_msg;
            this.showNotification = true;
          } else if (response.state == "3") {
            this.$administrator.username = this.username;
            this.$administrator.password = this.password;
            this.notification =
              "Welcome to the Administration Page, " +
              this.$administrator.username +
              ".";
            this.showNotification = true;
          } else if (response.state == "2") {
            this.$employee.username = this.username;
            this.$employee.password = this.password;
            this.notification =
              "Welcome to the Employee Page, " + this.$employee.username + ".";
            this.showNotification = true;
          } else {
            this.$user.first_name = response.first_name;
            this.$user.last_name = response.last_name;
            this.$user.username = this.formData.username;
            this.$user.password = this.formData.password;
            this.$user.phone_num = response.phone_num;
            this.$user.passport_num = response.passport_num;
            this.$user.email = response.email;
            this.$user.birthday = response.birthday;
            this.$user.address = response.address;
            this.$user.order_list = response.order_list;

            alert(this.$user.email + this.$user.phone_num);

            setCookie("username", this.username, 1000 * 60);
            this.$router.push("/home");
          }
        });
      }
    },
    toRegister() {
      this.$router.push("/register");
    }
  }
};
</script>

<style scoped>
.login-cover-image {
  background-image: url("../assets/img/china-ireland.jpg");
}
</style>
