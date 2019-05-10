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
          <b>{{$t('m.name')}}</b>
          {{$t('m.name2')}}
          <small>{{$t('m.pbt')}}</small>
        </div>
      </div>
      <!-- end brand -->
      <!-- begin login-content -->
      <div class="login-content">
        <div class="form-group m-b-20">
          <input
            type="text"
            class="form-control form-control-lg"
            :placeholder="$t('m.un')"
            v-model="formData.username"
            required
          >
        </div>
        <div class="form-group m-b-20">
          <input
            type="password"
            class="form-control form-control-lg"
            :placeholder="$t('m.password')"
            v-model="formData.password"
            required
          >
        </div>
        <p v-show="showNotification" style="color: red;">{{notification}}</p>
        <div class="login-buttons">
          <button v-on:click="login" class="btn btn-success btn-block btn-lg">{{$t('m.sign')}}</button>
        </div>
        <div class="m-t-20" style="color: black; font-size: 13px">
          {{$t('m.mem')}}
          <a href="javascript:;" v-on:click="toRegister">{{$t('m.here')}}</a>
          {{$t('m.reg')}}
        </div>
        <div class="m-t-20" style="color: black; font-size: 13px">
          {{$t('m.mem_password')}}
          <a
            href="javascript:;"
            v-b-modal.modalDialog1
          >{{$t('m.here_password')}}</a>
        </div>
      </div>
      <!-- end login-content -->
    </div>
    <!-- end login -->

    <!-- begin change password modal -->
    <b-modal
      id="modalDialog1"
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
          {{$t('m.un')}}
          <span class="text-danger">*</span>
        </label>
        <br>
        <small>{{$t('m.theun')}}</small>
        <br>
        <br>
        <div class="row m-b-15">
          <div class="col-md-12">
            <input
              type="text"
              class="form-control"
              :placeholder="$t('m.un')"
              name="user name"
              v-validate="{ required: true, regex:/^[_a-zA-Z0-9\u4E00-\u9FA5]{2,10}$/ }"
              v-bind:class="{'is-invalid': errors.has('user name')}"
              v-model="formData.username"
            >
            <span style="color: red !important;">{{ errors.first('user name') }}</span>
            <br>
            <div class="input-group mb-3">
              <input
                type="text"
                class="form-control"
                :placeholder="$t('m.verc')"
                aria-describedby="button-addon2"
                v-bind:class="{'is-valid': this.verification_field}"
                v-model="verification_input"
              >
              <div class="input-group-append">
                <button
                  type="button"
                  class="btn btn-sm btn-white"
                  :disabled="disabled"
                  @click="sendCode"
                >{{btntxt}}</button>
              </div>
            </div>
          </div>
        </div>
        <form action="#" v-show="verification_input">
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
                name="password"
                ref="password"
                v-validate="{ required: true, regex:/^[_!?,.*#a-zA-Z0-9]{6,20}$/ }"
                v-bind:class="{'is-invalid': errors.has('password')}"
                v-model="password"
              >
              <span style="color: red !important;">{{ errors.first('password') }}</span>
            </div>
          </div>
          <label class="control-label">
            {{$t('m.confirm')}}
            <span class="text-danger">*</span>
          </label>
          <div class="row m-b-15">
            <div class="col-md-12">
              <input
                v-validate="'required|confirmed:password'"
                name="confirm_password"
                type="password"
                class="form-control"
                :placeholder="$t('m.ppag')"
                data-vv-as="password"
                v-bind:class="{'is-invalid': errors.has('confirm_password')}"
                v-model="confirm_password"
              >
              <div
                v-if="errors.has('confirm_password')"
                style="color: red;"
              >{{ errors.first('confirm_password') }}</div>
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
import PageOptions from "../config/PageOptions.vue";

import axios from "axios";
import { setCookie, getCookie } from "../assets/js/cookie.js";
import { setTimeout } from "timers";

export default {
  data() {
    return {
      notification: "",
      showNotification: false,
      formData: {
        username: "",
        password: ""
      },

      // Required information
      old_username: this.$store.getters.username,
      password: "",
      confirm_password: "",

      // Variables for email validation
      btntxt: this.$t("m.bsvc"),
      showPasswordCard: false,
      disabled: false,
      time: 0,
      verify: "",
      verification_code: 1,
      verification_input: "",
      verification_field: false
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
        alert(this.$t("m.alv"));
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
            this.notification =
              "Welcome to the Employee Page, " + this.$employee.username + ".";
            this.showNotification = true;
            this.$store.commit("handleEmployee", response);
            alert(this.$store.state.employee_id);
            this.$router.push("/employee/insurance");
          } else {
            for (var key in response) {
              if (response[key] == "null") {
                response[key] = "";
              }
            }
            this.$store.commit("handleCustomerInfo", response);

            // setCookie("user", response, 1000 * 60);
            this.$router.push("/home");
          }
        });
      }
    },
    toRegister() {
      this.$router.push("/register");
    },
    isEmpty(s) {
      var v = null;
      if (typeof s == "object") {
        if (s == null) {
          alert("null");
          return true;
        }
        if (typeof s.getValue != "undefined") {
          alert("undefined");
          v = s.getValue();
        } else {
          alert("else");
          v = s.value;
        }
      } else {
        v = s;
      }
      if (v == null || v == "" || v == "NaN" || v == "undefined") {
        return true;
      } else {
        return false;
      }
    },
    sendCode() {
      this.verify = 0;
      this.verification_input = "";
      this.verification_field = false;

      var params = {
        username: this.formData.username,
        verify: this.verify
      };
      var obj = JSON.stringify(params);

      axios
        .post("/customer/info/update_password", obj)
        .then(res => {
          if (res.data == 0) {
            alert(this.$t("m.als"));
          } else {
            this.time = 60;
            this.disabled = true;
            this.timer();
            this.verification_code = res.data;
            alert(res.data);
          }
        })
        .catch(function(error) {
          console.log(error);
        });
    },
    timer() {
      if (this.time > 0) {
        if (
          this.verification_input == this.verification_code &&
          this.verification_input != ""
        ) {
          this.verification_field = true;
        }

        this.time--;
        this.btntxt = this.$t("m.r_bsvc") + this.time + this.$t("m.r_other");
        setTimeout(this.timer, 1000);
      } else {
        this.time = 0;
        this.btntxt = this.$t("m.bsvc");
        this.disabled = false;
      }
    },
    cancelChange() {
      this.btntxt = this.$t("m.bsvc");
      this.showPasswordCard = false;
      this.disabled = false;
      this.email = "";
      this.time = 0;
      this.verify = "";
      this.verification_code = 1;
      this.verification_input = "";
      this.verification_field = false;
    },
    submitPassword() {
      this.verify = 1;

      var params = {
        username: this.$store.getters.username,
        password: this.password,
        confirm_password: this.confirm_password,
        verify: this.verify
      };
      var obj = JSON.stringify(params);

      axios
        .post("/customer/info/update_password", obj)
        .then(res => {
          var response = JSON.parse(JSON.stringify(res.data));
          if (response.state == 0) {
            this.swalNotification('error', response.error_msg);
          } else {
            this.swalNotification('success', '');
          }
        })
        .catch(function(error) {
          console.log(error);
        });
      this.cancelChange();
    },
    swalNotification(swalType, error_msg) {
      if (swalType == "success") {
        this.$swal({
          title: this.$t("m.password_s_title"),
          timer: 2000,
          showConfirmButton: false,
          type: swalType
        }).then(
          setTimeout(() => {
          }, 2000)
        );
      } else {
        this.$swal({
          title: this.$t("m.password_f_title"),
          text: error_msg,
          timer: 2000,
          showConfirmButton: false,
          type: swalType
        }).then();
      }
    }
  }
};
</script>

<style scoped>
.login-cover-image {
  background-image: url("../assets/img/login.jpg");
}

.is-valid {
  background-color: #f2fff0 !important;
}
</style>
