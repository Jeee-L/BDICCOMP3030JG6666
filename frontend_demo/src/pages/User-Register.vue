<template>
  <!-- begin register -->
  <div class="register register-with-news-feed">
    <!-- begin news-feed -->
    <div class="news-feed">
      <div class="news-image"></div>
      <div class="news-caption">
        <h4 class="caption-title">
          <b>{{$t('m.name')}}</b>
          {{$t('m.name2')}}
        </h4>
        <p>{{$t('m.peace')}}</p>
      </div>
    </div>
    <!-- end news-feed -->
    <!-- begin right-content -->
    <div class="right-content">
      <!-- begin register-header -->
      <h1 class="register-header">
        {{$t('m.registration')}}
        <small>{{$t('m.guide')}}</small>
      </h1>
      <!-- end register-header -->
      <!-- begin register-content -->
      <div class="register-content">
        <form action class="margin-bottom-0" v-on:submit.prevent="submitForm">
          <label class="control-label">
            {{$t('m.un')}}
            <span class="text-danger">*</span>
          </label>
          <div class="row row-space-10">
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
              <small class="text-muted">· {{$t('m.uns1')}}</small>
              <br>
              <small class="text-muted">· {{$t('m.uns2')}}</small>
              <br>
              <small class="text-muted">· {{$t('m.uns3')}}</small>
            </div>
          </div>
          <br>
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
                v-model="formData.password"
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
                v-model="formData.confirm_password"
              >
              <div
                v-if="errors.has('confirm_password')"
                style="color: red;"
              >{{ errors.first('confirm_password') }}</div>
              <br>
              <small class="text-muted">· {{$t('m.pws1')}}</small>
              <br>
              <small class="text-muted">· {{$t('m.pws2')}}</small>
              <br>
              <small class="text-muted">· {{$t('m.pws3')}}</small>
              <br>
            </div>
          </div>
          <br>
          <label class="control-label">
            {{$t('m.email')}}
            <span class="text-danger">*</span>
          </label>
          <div class="row m-b-15">
            <div class="col-md-12">
              <input
                type="text"
                name="email"
                :placeholder="$t('m.email')"
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
          <br>
          <label class="control-label">
            {{$t('m.pnum')}}
            <span class="text-danger">*</span>
          </label>
          <div class="row m-b-15">
            <div class="col-md-12">
              <input
                type="text"
                class="form-control"
                :placeholder="$t('m.pnum')"
                name="phone number"
                v-validate="{ required: true, regex:/^1[34578]\d{9}$|^\d{8,9}$/ }"
                v-bind:class="{'is-invalid': errors.has('phone number')}"
                v-model="formData.phone_num"
              >
              <span style="color: red !important;">{{ errors.first('phone number') }}</span>
            </div>
          </div>
          <br>
          <div class="register-buttons">
            <button class="btn btn-primary btn-block btn-lg">{{$t('m.signup')}}</button>
          </div>
          <div class="m-t-20 m-b-40 p-b-40 text-inverse">
            {{$t('m.alr')}}
            <a href="/login">{{$t('m.here')}}</a>
            {{$t('m.login2')}}
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
      btntxt: this.$t("m.bsvc"),

      verification_code: "",
      verification_input: "",
      verification_field: false,

      formData: {
        username: "",
        password: "",
        confirm_password: "",
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
  computed: {
    isFormInvalid() {
      return Object.keys(this.fields).some(key => this.fields[key].invalid);
    }
  },
  methods: {
    submitForm() {
      this.swalNotification("success", "");
      if (!this.isFormInvalid && this.verification_field) {
        this.formData.verify = 1;
        var obj = JSON.stringify(this.formData);
        axios
          .post("/register/", obj)
          .then(res => {
            var response = JSON.parse(JSON.stringify(res.data));
            if (response.state == "1") {
              this.swalNotification("success", "");
              this.$router.push("/login");
            } else {
              this.swalNotification("error", response.error_msg);
            }
          })
          .catch(function(error) {
            console.log(error);
          });
      } else if (!this.isFormInvalid && !this.verification_field) {
        alert(this.$t("m.alp"));
      } else {
        alert(this.$t("m.alpe"));
      }
    },
    sendCode() {
      this.formData.verify = 0;
      this.verification_input = "";
      this.verification_field = false;

      if (this.fields.email.valid) {
        var params = {
          email: this.formData.email,
          verify: this.formData.verify
        };
        var obj = JSON.stringify(params);

        axios
          .post("/register/", obj)
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
      }
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
    swalNotification(swalType, error_msg) {
      if (swalType == "success") {
        this.$swal({
          title: this.$t("m.register_s_title"),
          text: this.$t("m.register_s_text"),
          timer: 2000,
          showConfirmButton: false,
          type: swalType
        }).then(
          setTimeout(() => {
            this.$router.push("/login");
          }, 2000)
        );
      } else {
        this.$swal({
          title: this.$t("m.register_f_title"),
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
.news-feed {
  background-image: url("../assets/img/register.jpg");
  width: 40% !important;
}

.right-content {
  width: 60% !important;
}

.text-muted {
  color: dimgray !important;
}

.is-invalid {
  background-color: #facccc62 !important;
}

.is-valid {
  background-color: #e1fcc4be !important;
}
</style>
