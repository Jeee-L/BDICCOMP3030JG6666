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
            v-model="username"
            required
          >
        </div>
        <div class="form-group m-b-20">
          <input
            type="password"
            class="form-control form-control-lg"
            placeholder="Password"
            v-model="password"
            required
          >
        </div>
        <p v-show="showNotification" style="color: red;">{{notification}}</p>
        <div class="checkbox checkbox-css m-b-20">
          <input type="checkbox" id="remember_checkbox">
          <label for="remember_checkbox">Remember Me</label>
        </div>
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
      username: "",
      password: "",

      notification: "",
      showNotification: false
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
      if (this.username == "" || this.password == "") {
        alert("Please enter valid User Name and Password.");
      } else {
        let params = new URLSearchParams();
        params.append("username", this.username);
        params.append("password", this.password);

        axios.post("http://localhost:5000/login", params).then(res => {
          if (res.data == -1) {
            this.notification = "Invalid user";
            this.showNotification = true;
          } else if (res.data == 0) {
            this.notification = "Wrong password";
            this.showNotification = true;
          } else if (res.data == 3) {
            this.notification = "Welcome to the Administration Page";
            this.showNotification = true;
          } else if (res.data == 2) {
            this.notification = "Welcome to the Employee Page";
            this.showNotification = true;
          } else {
            this.notification = "Welcome dear customer.";
            this.showNotification = true;
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
