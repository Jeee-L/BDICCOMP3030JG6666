<template>
  <!-- begin register -->
  <div class="register register-with-news-feed">
    <!-- begin news-feed -->
    <div class="news-feed">
      <div class="news-image"></div>
      <div class="news-caption">
        <h4 class="caption-title">
          <b>Hibernia-Sino</b> Travel Insurance
        </h4>
        <p>Travel with peace of mind. Compare the below plans and buy online with our best price guarantee. Our checkout process is 100% safe and secure and you’ll receive your policy within minutes via email.</p>
      </div>
    </div>
    <!-- end news-feed -->
    <!-- begin right-content -->
    <div class="right-content">
      <!-- begin register-header -->
      <h1 class="register-header">
        Registration
        <small>Use the following guidelines for creating a secure Hibernia-Sino Travel Insurance Account.</small>
      </h1>
      <!-- end register-header -->
      <!-- begin register-content -->
      <div class="register-content">
        <form class="margin-bottom-0">
          <label class="control-label">
            User Name
            <span class="text-danger">*</span>
          </label>
          <div class="row row-space-10">
            <div class="col-md-12">
              <input
                type="text"
                class="form-control"
                placeholder="User Name"
                name="user name"
                v-validate="{ required: true, regex:/^[_a-zA-Z0-9\u4E00-\u9FA5]{2,10}$/ }"
                v-bind:class="{'is-invalid': errors.has('user name')}"
                v-model="formData.username"
              >
              <span style="color: red !important;">{{ errors.first('user name') }}</span>
              <br>
              <small class="text-muted">· Username should be between 2 and 10 characters long.</small>
              <br>
              <small
                class="text-muted"
              >· Can contain any Chinese characters, any English letters from a to z (or A to Z).</small>
              <br>
              <small
                class="text-muted"
              >· Can contain any numbers from 0 through 9 and _ (underscore) character.</small>
            </div>
          </div>
          <br>
          <label class="control-label">
            Password
            <span class="text-danger">*</span>
          </label>
          <div class="row m-b-15">
            <div class="col-md-12">
              <input
                type="password"
                class="form-control"
                placeholder="Password"
                name="password"
                ref="password"
                v-validate="{ required: true, regex:/^[_!?,.*#a-zA-Z0-9]{6,20}$/ }"
                v-bind:class="{'is-invalid': errors.has('password')}"
                v-model="formData.password"
              >
              <span style="color: red !important;">{{ errors.first('password') }}</span>
            </div>
          </div>
          <label class="control-label">
            Password Confirmation
            <span class="text-danger">*</span>
          </label>
          <div class="row m-b-15">
            <div class="col-md-12">
              <input
                v-validate="'required|confirmed:password'"
                name="confirm_password"
                type="password"
                class="form-control"
                placeholder="Password, Again"
                data-vv-as="password"
                v-bind:class="{'is-invalid': errors.has('confirm_password')}"
                v-model="formData.password_comfirmation"
              >
              <div
                v-if="errors.has('confirm_password')"
                style="color: red;"
              >{{ errors.first('confirm_password') }}</div>
              <br>
              <small class="text-muted">· Password should be between 6 and 20 characters long.</small>
              <br>
              <small
                class="text-muted"
              >· Can contain any English letters from a to z and any numbers from 0 through 9.</small>
              <br>
              <small
                class="text-muted"
              >· Can contain some special characters, including _ (underscore), ! (exclamation mark), ? (question mark), , (comma), . (period), * (asterisk), # (pound sign).</small>
              <br>
            </div>
          </div>
          <br>
          <label class="control-label">
            Email
            <span class="text-danger">*</span>
          </label>
          <div class="row m-b-15">
            <div class="col-md-12">
              <input
                type="text"
                name="email"
                placeholder="Email"
                v-validate="{ required: true, regex:/^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,})$/ }"
                class="form-control"
                v-bind:class="{'is-invalid': errors.has('email')}"
                v-model="formData.email"
              >
              <span style="color: red !important;">{{ errors.first('email') }}</span>
              <br>
              <div class="input-group mb-3">
                <input
                  type="text"
                  class="form-control"
                  placeholder="Verification Code"
                  aria-label="Recipient's username"
                  aria-describedby="button-addon2"
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
          <br>
          <label class="control-label">
            Phone Number
            <span class="text-danger">*</span>
          </label>
          <div class="row m-b-15">
            <div class="col-md-12">
              <input
                type="text"
                class="form-control"
                placeholder="Phone Number"
                name="phone number"
                v-validate="{ required: true, regex:/^1[34578]\d{9}$/ }"
                v-bind:class="{'is-invalid': errors.has('phone number')}"
                v-model="formData.phone_num"
              >
              <span style="color: red !important;">{{ errors.first('phone number') }}</span>
            </div>
          </div>
          <br>
          <div class="checkbox checkbox-css m-b-30">
            <div class="checkbox checkbox-css m-b-30">
              <input type="checkbox" id="agreement_checkbox" value>
              <label for="agreement_checkbox">
                By clicking Sign Up, you agree to our
                <a href="javascript:;">Terms</a> and that you have read our
                <a href="javascript:;">Data Policy</a>, including our
                <a href="javascript:;">Cookie Use</a>.
              </label>
            </div>
          </div>
          <div class="register-buttons">
            <button
              type="primary"
              @click="submitForm"
              class="btn btn-primary btn-block btn-lg"
            >Sign Up</button>
          </div>
          <div class="m-t-20 m-b-40 p-b-40 text-inverse">
            Already a member? Click
            <a href="/login">here</a> to login.
          </div>
        </form>
      </div>
      <!-- end register-content -->
    </div>
    <!-- end right-content -->
  </div>
  <!-- end register -->
</template>

<script>
import PageOptions from "../config/PageOptions.vue";
import axios from "axios";

export default {
  data() {
    return {
      disabled: false,
      time: 0,
      btntxt: "Send Verification Code",
      formData: {
        username: "",
        password: "",
        password_comfirmation: "",
        email: "",
        phone_num: "",
        verify: 1
      }
    };
  },
  created() {
    PageOptions.pageEmpty = true;
    document.body.className = "bg-white";
  },
  beforeRouteLeave(to, from, next) {
    PageOptions.pageEmpty = false;
    document.body.className = "";
    next();
  },
  methods: {
    submitForm() {
      this.formData.verify = 0;
      var obj = JSON.stringify(this.formData);
      axios
        .post("/register", obj)
        .then(res => {
          if (res.data == 1) {
            // this.swalNotification("success")
            this.$router.push("/login");
          } else {
            // this.swalNotification("danger")
          }
        })
        .catch(function(error) {
          console.log(error);
        });
    },
    sendCode() {
      if (this.fields.email.valid) {
        this.time = 60;
        this.disabled = true;
        this.timer();

        var obj = JSON.stringify(this.formData.email);
        axios
          .post("/register", obj)
          .then(res => {
            if (res.data == 1) {
              res.data.verification
            } else {
              // this.swalNotification("danger")
            }
          })
          .catch(function(error) {
            console.log(error);
          });
      }
    },
    timer() {
      if (this.time > 0) {
        this.time--;
        this.btntxt = "Resend Code after " + this.time + " Seconds";
        setTimeout(this.timer, 1000);
      } else {
        this.time = 0;
        this.btntxt = "Send Verification Code";
        this.disabled = false;
      }
    },
    swalNotification(swalType) {
      if (swalType == "success") {
        this.$swal({
          title: "Successful Registration",
          text: "Automatically proceed to Login page.",
          type: swalType
        });
      } else {
        this.$swal({
          title: "Registration Failed",
          text: "Please double check user information and submit again.",
          type: swalType,
          showCancelButton: true,
          buttonsStyling: false,
          cancelButtonText: "Cancel",
          cancelButtonClass: "btn btn-default"
        });
      }
    }
  }
};
</script>

<style scoped>
.news-feed {
  background-image: url("../assets/img/register.jpg");
  width: 50% !important;
}

.right-content {
  width: 50% !important;
}

.text-muted {
  color: dimgray !important;
}
</style>
