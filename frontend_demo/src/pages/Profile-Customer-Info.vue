<template>
  <div>
    <!-- begin profile -->
    <div class>
      <div class="profile-header">
        <!-- BEGIN profile-header-cover -->
        <div class="profile-header-cover"></div>
        <!-- END profile-header-cover -->
        <!-- BEGIN profile-header-content -->
        <div class="profile-header-content">
          <!-- BEGIN profile-header-img -->
          <div class="profile-header-img">
            <img :src="($store.getters.avatar)">
            <!-- onerror="this.src='../assets/img/china-land1.jpg'" -->
          </div>
          <!-- END profile-header-img -->
          <!-- BEGIN profile-header-info -->
          <div class="profile-header-info">
            <h4 class="m-t-10 m-b-5">{{$store.getters.username}}</h4>
            <p class="m-b-10"></p>
            <a
              a
              href="javascript:;"
              v-on:click="startEdit(false)"
              class="btn btn-xs btn-yellow"
              data-toggle="tab"
            >{{$t('m.ep')}}</a>
          </div>
          <!-- END profile-header-info -->
        </div>
        <!-- END profile-header-content -->
        <!-- BEGIN profile-header-tab -->
        <ul class="profile-header-tab nav nav-tabs">
          <li class="nav-item">
            <a href="javascript:;" class="nav-link active" data-toggle="tab">{{$t('m.usp')}}</a>
          </li>
        </ul>
        <!-- END profile-header-tab -->
      </div>
    </div>
    <!-- end profile -->
    <!-- begin profile-content -->
    <div class="profile-content">
      <!-- begin tab-content -->
      <div class="tab-content p-0">
        <!-- begin #profile-about tab -->
        <div class="tab-pane fade show active">
          <div class="row">
            <div class="col-lg-4">
              <div class="card card-default">
                <div class="card-body text-center">
                  <div class="py-4">
                    <img
                      class="img-fluid rounded-circle img-thumbnail thumb96"
                      :src="($store.getters.avatar)"
                      alt="Contact"
                      onload="if (this.width>140 || this.height>226) if (this.width/this.height>140/226) this.width=140; else this.height=226;"
                    >
                  </div>
                  <h3 class="m-0 text-bold">{{$store.getters.username}}</h3>
                  <div class="my-3">
                    <p>{{$t('m.upl')}}</p>
                  </div>

                  <label class="btn btn-primary mb-2 mr-2" for="change-image">
                    <input
                      class="sr-only"
                      type="file"
                      id="change-image"
                      accept="image/png, image/jpeg, image/gif, image/jpg"
                      @change="changeImage($event)"
                    >
                    {{$t('m.upp')}}
                  </label>
                </div>
              </div>
              <div class="card card-default" v-show="showPasswordCard">
                <div class="d-lg-block password-title card-title text-center">
                  <h5>{{$t('m.cp')}}</h5>
                  {{$t('m.val')}}
                </div>
                <div class="card-body">
                  <label class="control-label">
                    {{$t('m.email')}}
                    <span class="text-danger">*</span>
                  </label>
                  <br>
                  <small>{{$t('m.themail')}}</small>
                  <br>
                  <br>
                  <div class="row m-b-15">
                    <div class="col-md-12">
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
                </div>
              </div>
            </div>
            <div class="col-lg-8">
              <div class="card card-default">
                <div class="card-header d-flex align-items-center">
                  <div class="d-flex justify-content-center col">
                    <div class="h4 m-0 text-center">{{$t('m.person')}}</div>
                  </div>
                  <a href="javascript:;" v-on:click="permitChangePassword">{{$t('m.cp')}}</a>
                </div>

                <!-- begin change password modal -->
                <b-modal
                  v-model="verification_field"
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
                    <!-- <form> -->
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
                    <!-- </form> -->
                  </div>
                </b-modal>
                <!-- end change password modal -->
                <div class="card-body">
                  <div class="row py-4 justify-content-center">
                    <div class="col-12 col-sm-10">
                      <p class="text-danger">* {{$t('m.upi')}}</p>
                      <br>
                      <form class="form-horizontal">
                        <div class="form-group row">
                          <label
                            class="text-bold col-xl-2 col-md-3 col-4 col-form-label text-right"
                            for="inputContact1"
                          >{{$t('m.fn')}}</label>
                          <div class="col-xl-10 col-md-9 col-8">
                            <input
                              class="form-control"
                              id="inputContact1"
                              type="text"
                              :placeholder="$t('m.fn')"
                              name="first name"
                              v-validate="{ required: true, regex:/^[_a-zA-Z0-9\u4E00-\u9FA5]{2,30}$/ }"
                              v-bind:class="{'is-invalid': errors.has('first name')}"
                              v-model.lazy="formData.first_name"
                              :disabled="this.update"
                            >
                            <span style="color: red !important;">{{ errors.first('first name') }}</span>
                          </div>
                        </div>
                        <div class="form-group row">
                          <label
                            class="text-bold col-xl-2 col-md-3 col-4 col-form-label text-right"
                            for="inputContact1"
                          >{{$t('m.ln')}}</label>
                          <div class="col-xl-10 col-md-9 col-8">
                            <input
                              class="form-control"
                              id="inputContact1"
                              type="text"
                              :placeholder="$t('m.ln')"
                              v-model.lazy="formData.last_name"
                              :disabled="this.update"
                            >
                          </div>
                        </div>
                        <div class="form-group row">
                          <label
                            class="text-bold col-xl-2 col-md-3 col-4 col-form-label text-right"
                            for="inputContact7"
                          >{{$t('m.email')}}</label>
                          <div class="col-xl-10 col-md-9 col-8">
                            <input
                              class="form-control"
                              id="inputContact7"
                              type="email"
                              placeholder
                              v-model.lazy="formData.email"
                              :disabled="this.update"
                            >
                          </div>
                        </div>
                        <div class="form-group row">
                          <label
                            class="text-bold col-xl-2 col-md-3 col-4 col-form-label text-right"
                            for="inputContact8"
                          >{{$t('m.birthday')}}</label>
                          <div class="col-xl-10 col-md-9 col-8">
                            <datepicker
                              :language="date_lan"
                              :placeholder="$t('m.date_placeholder')"
                              input-class="form-control bg-white"
                              v-model.lazy="formData.birthday"
                              format="yyyy-MM-dd"
                              :disabled="this.update"
                            ></datepicker>
                          </div>
                        </div>
                        <div class="form-group row">
                          <label
                            class="text-bold col-xl-2 col-md-3 col-4 col-form-label text-right"
                            for="inputContact3"
                          >{{$t('m.num')}}</label>
                          <div class="col-xl-10 col-md-9 col-8">
                            <input
                              class="form-control"
                              id="inputContact3"
                              type="number"
                              placeholder
                              v-model.lazy="formData.phone_num"
                              :disabled="this.update"
                            >
                          </div>
                        </div>
                        <div class="form-group row">
                          <label
                            class="text-bold col-xl-2 col-md-3 col-4 col-form-label text-right"
                            for="inputContact5"
                          >{{$t('m.pid')}}</label>
                          <div class="col-xl-10 col-md-9 col-8">
                            <input
                              class="form-control"
                              id="inputContact5"
                              type="text"
                              placeholder
                              v-model.lazy="formData.passport_num"
                              :disabled="this.update"
                            >
                          </div>
                        </div>
                        <div class="form-group row">
                          <label
                            class="text-bold col-xl-2 col-md-3 col-4 col-form-label text-right"
                            for="inputContact6"
                          >{{$t('m.address')}}</label>
                          <div class="col-xl-10 col-md-9 col-8">
                            <textarea
                              class="form-control"
                              id="inputContact6"
                              rows="4"
                              v-model.lazy="formData.address"
                              :disabled="this.update"
                            ></textarea>
                          </div>
                        </div>
                        <div class="form-group row">
                          <div class="col-md-10">
                            <button
                              class="btn btn-info"
                              type="button"
                              v-on:click="startEdit(true)"
                            >{{$t('m.update1')}}</button>
                          </div>
                        </div>
                      </form>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <!-- end #profile-about tab -->
      </div>
      <!-- end tab-content -->
    </div>
    <!-- end profile-content -->
  </div>
</template>

<script>
import PageOptions from "../config/PageOptions.vue";
import { en, zh } from "vuejs-datepicker/dist/locale";
import axios from "axios";

export default {
  computed: {
    date_lan(){
      return this.$t("m.date_lan") == "en" ? en : zh;
    }
  },
  data() {
    return {
      formData: {
        old_username: this.$store.getters.username,
        first_name: this.$store.getters.first_name,
        last_name: this.$store.getters.last_name,
        username: this.$store.getters.username,
        email: this.$store.getters.email,
        birthday: this.$store.getters.birthday,
        phone_num: this.$store.getters.phone_num,
        passport_num: this.$store.getters.passport_num,
        address: this.$store.getters.address
      },

      // Variables for element control
      update: true,
      tab: {
        about: true
      },

      // Required information
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
  methods: {
    permitChangePassword() {
      this.showPasswordCard = true;
    },
    sendCode() {
      this.verify = 0;
      this.verification_input = "";
      this.verification_field = false;

      var params = {
        username: this.$store.getters.username,
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
      this.cancelChange();
    },
    startEdit(value) {
      this.update = value;
      if (value == false) {
        return;
      }
      var today = new Date().toISOString().substr(0, 10);
      if (this.formData.birthday == today) {
        this.formData.birthday = new Date("1000-01-01")
          .toISOString()
          .substr(0, 10);
      }

      var obj = JSON.stringify(this.formData);
      axios.post("/customer/info/", obj).then(res => {
        var response = JSON.parse(JSON.stringify(res.data));
      });
      this.$store.commit("handleCustomerInfo", this.formData);
    },
    changeImage(e) {
      let file = e.target.files[0];
      if (!/\.(gif|jpg|jpeg|png|bmp|GIF|JPG|PNG)$/.test(e.target.value)) {
        alert(this.$t("m.alfe"));
        return false;
      }
      let reader = new FileReader();
      reader.onload = e => {
        let data;
        if (typeof e.target.result === "object") {
          data = window.URL.createObjectURL(new Blob([e.target.result]));
        } else {
          data = e.target.result;
        }
        this.$store.commit("handleAvatar", data);
      };
      reader.readAsArrayBuffer(file);
    }
  },
  created() {
    PageOptions.pageContentFullWidth = true;
  },
  beforeRouteLeave(to, from, next) {
    PageOptions.pageContentFullWidth = false;
    next();
  }
};
</script>

<style scoped>
input:disabled {
  border: 1px solid #ddd;
  background-color: #f3faf9b4;
  color: #000000;
  opacity: 1;
}

textarea:disabled {
  border: 1px solid #ddd;
  background-color: #f3faf9a8;
  color: #000000;
  opacity: 1;
}

.is-invalid {
  background-color: #facccc7e !important;
}

.is-valid {
  background-color: #f2fff0 !important;
}

.password-title {
  padding: 20px;
  font-size: 10px;
  background-color: #f5f5f3fb;
}
</style>
