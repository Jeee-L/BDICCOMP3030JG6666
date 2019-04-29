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
            <img :src="avatar">
            <!-- onerror="this.src='../assets/img/china-land1.jpg'" -->
          </div>
          <!-- END profile-header-img -->
          <!-- BEGIN profile-header-info -->
          <div class="profile-header-info">
            <h4 class="m-t-10 m-b-5">{{$user.username}}</h4>
            <p class="m-b-10"></p>
            <a
              a
              href="javascript:;"
              v-on:click="startEdit(false)"
              class="btn btn-xs btn-yellow"
              data-toggle="tab"
            >Edit Profile</a>
          </div>
          <!-- END profile-header-info -->
        </div>
        <!-- END profile-header-content -->
        <!-- BEGIN profile-header-tab -->
        <ul class="profile-header-tab nav nav-tabs">
          <li class="nav-item">
            <a href="javascript:;" class="nav-link active" data-toggle="tab">User Profile</a>
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
                      :src="avatar"
                      alt="Contact"
                      onload="if (this.width>140 || this.height>226) if (this.width/this.height>140/226) this.width=140; else this.height=226;"
                    >
                  </div>
                  <h3 class="m-0 text-bold">{{$user.username}}</h3>
                  <div class="my-3">
                    <p>Please upload a photo to customize your avatar.</p>
                  </div>

                  <label class="btn btn-primary mb-2 mr-2" for="change-image">
                    <input
                      class="sr-only"
                      type="file"
                      id="change-image"
                      accept="image/png, image/jpeg, image/gif, image/jpg"
                      @change="changeImage($event)"
                    > Upload Photo
                  </label>
                </div>
              </div>
              <div class="card card-default" v-show="showPasswordCard">
                <div class="d-lg-block password-title card-title text-center">
                  <h5>Change Password</h5>Please pass email velidation before changing passord.
                </div>
                <div class="card-body">
                  <label class="control-label">
                    Email
                    <span class="text-danger">*</span>
                  </label>
                  <br>
                  <small>This email should be the email used for registration; otherwise, please update this information first.</small>
                  <br>
                  <br>
                  <div class="row m-b-15">
                    <div class="col-md-12">
                      <input
                        type="text"
                        name="email"
                        placeholder="Email"
                        v-validate="{ required: true, regex:/^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,})$/ }"
                        class="form-control"
                        v-bind:class="{'is-invalid': errors.has('email')}"
                        v-model="email"
                      >
                      <span style="color: red !important;">{{ errors.first('email') }}</span>
                      <br>
                      <div class="input-group mb-3">
                        <input
                          type="text"
                          class="form-control"
                          placeholder="Verification Code"
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
                    <div class="h4 m-0 text-center">Personal Information</div>
                  </div>
                  <a href="javascript:;" v-on:click="permitChangePassword">Change Password</a>
                </div>

                <!-- begin change password modal -->
                <b-modal
                  v-model="verification_field"
                  id="modalDialog1"
                  cancel-title="Cancel"
                  cancel-variant="white"
                  @cancel="cancelChange()"
                  @ok="submitPassword()"
                  ok-title="Update Password"
                  ok-variant="info"
                  title="Change Password"
                >
                  <div class="card-body">
                    <form action="#">
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
                            v-model="password"
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
                            v-model="confirm_password"
                          >
                          <div
                            v-if="errors.has('confirm_password')"
                            style="color: red;"
                          >{{ errors.first('confirm_password') }}</div>
                        </div>
                      </div>
                      <p>
                        <small
                          class="text-muted"
                        >* New password will be requried in the log-in section next time.</small>
                      </p>
                    </form>
                  </div>
                </b-modal>
                <!-- end change password modal -->
                <div class="card-body">
                  <div class="row py-4 justify-content-center">
                    <div class="col-12 col-sm-10">
                      <p
                        class="text-danger"
                      >* Please click the Edit Profile button to update personal information.</p>
                      <br>
                      <form class="form-horizontal">
                        <div class="form-group row">
                          <label
                            class="text-bold col-xl-2 col-md-3 col-4 col-form-label text-right"
                            for="inputContact1"
                          >First Name</label>
                          <div class="col-xl-10 col-md-9 col-8">
                            <input
                              class="form-control"
                              id="inputContact1"
                              type="text"
                              placeholder="First Name"
                              name="first name"
                              v-validate="{ required: true, regex:/^[_a-zA-Z0-9\u4E00-\u9FA5]{2,30}$/ }"
                              v-bind:class="{'is-invalid': errors.has('first name')}"
                              v-model.lazy="$user.first_name"
                              :disabled="this.update"
                            >
                            <span style="color: red !important;">{{ errors.first('first name') }}</span>
                          </div>
                        </div>
                        <div class="form-group row">
                          <label
                            class="text-bold col-xl-2 col-md-3 col-4 col-form-label text-right"
                            for="inputContact1"
                          >Last Name</label>
                          <div class="col-xl-10 col-md-9 col-8">
                            <input
                              class="form-control"
                              id="inputContact1"
                              type="text"
                              placeholder
                              v-model.lazy="$user.last_name"
                              :disabled="this.update"
                            >
                          </div>
                        </div>
                        <div class="form-group row">
                          <label
                            class="text-bold col-xl-2 col-md-3 col-4 col-form-label text-right"
                            for="inputContact2"
                          >User Name</label>
                          <div class="col-xl-10 col-md-9 col-8">
                            <input
                              class="form-control"
                              id="inputContact2"
                              type="text"
                              placeholder
                              v-model.lazy="$user.username"
                              :disabled="this.update"
                            >
                          </div>
                        </div>
                        <div class="form-group row">
                          <label
                            class="text-bold col-xl-2 col-md-3 col-4 col-form-label text-right"
                            for="inputContact7"
                          >Email</label>
                          <div class="col-xl-10 col-md-9 col-8">
                            <input
                              class="form-control"
                              id="inputContact7"
                              type="email"
                              placeholder
                              v-model.lazy="$user.email"
                              :disabled="this.update"
                            >
                          </div>
                        </div>
                        <div class="form-group row">
                          <label
                            class="text-bold col-xl-2 col-md-3 col-4 col-form-label text-right"
                            for="inputContact8"
                          >Birthday</label>
                          <div class="col-xl-10 col-md-9 col-8">
                            <datepicker
                              placeholder="Select Date"
                              input-class="form-control bg-white"
                              v-model.lazy="$user.birthday"
                              :disabled="this.update"
                            ></datepicker>
                          </div>
                        </div>
                        <div class="form-group row">
                          <label
                            class="text-bold col-xl-2 col-md-3 col-4 col-form-label text-right"
                            for="inputContact3"
                          >Phone Num</label>
                          <div class="col-xl-10 col-md-9 col-8">
                            <input
                              class="form-control"
                              id="inputContact3"
                              type="number"
                              placeholder
                              v-model.lazy="$user.phone_num"
                              :disabled="this.update"
                            >
                          </div>
                        </div>
                        <div class="form-group row">
                          <label
                            class="text-bold col-xl-2 col-md-3 col-4 col-form-label text-right"
                            for="inputContact5"
                          >Passport ID</label>
                          <div class="col-xl-10 col-md-9 col-8">
                            <input
                              class="form-control"
                              id="inputContact5"
                              type="text"
                              placeholder
                              v-model.lazy="$user.passport_num"
                              :disabled="this.update"
                            >
                          </div>
                        </div>
                        <div class="form-group row">
                          <label
                            class="text-bold col-xl-2 col-md-3 col-4 col-form-label text-right"
                            for="inputContact6"
                          >Address</label>
                          <div class="col-xl-10 col-md-9 col-8">
                            <textarea
                              class="form-control"
                              id="inputContact6"
                              rows="4"
                              v-model.lazy="$user.address"
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
                            >Update</button>
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
import axios from "axios";

export default {
  data() {
    return {
      // Variables for element control
      update: true,
      tab: {
        about: true
      },

      avatar: this.$user.avatar,

      // Required information
      old_username: this.$user.username,
      password: "",
      confirm_password: "",

      // Variables for email validation
      btntxt: "Send Verification Code",
      showPasswordCard: false,
      disabled: false,
      email: "",
      time: 0,
      verify: "",
      verification_code: 1,
      verification_input: "",
      verification_field: false
    };
  },
  watch: {
    "$user.avatar"(){
      this.avatar = this.$user.avatar;
    }
  },
  methods: {
    permitChangePassword() {
      this.showPasswordCard = true;
    },
    sendCode() {
      this.verify = 0;
      this.verification_input = "";
      this.verification_field = false;

      if (this.fields.email.valid) {
        var params = {
          username: this.$user.username,
          email: this.email,
          verify: this.verify
        };
        var obj = JSON.stringify(params);

        axios
          .post("/customer/info/update_password", obj)
          .then(res => {
            if (res.data == 0) {
              alert("Sorry, sending verification code failed.");
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
        this.btntxt = "Resend Code after " + this.time + " Seconds";
        setTimeout(this.timer, 1000);
      } else {
        this.time = 0;
        this.btntxt = "Send Verification Code";
        this.disabled = false;
      }
    },
    cancelChange() {
      this.btntxt = "Send Verification Code";
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

      if (this.fields.email.valid && this.email == this.$user.email) {
        var params = {
          username: this.$user.username,
          password: this.password,
          confirm_password: this.confirm_password,
          verify: this.verify
        };
        var obj = JSON.stringify(params);

        axios
          .post("/customer/info/update_password", obj)
          .then(res => {
            if (res.data == 0) {
              alert("Sorry, sending verification code failed.");
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
      this.cancelChange();
    },
    startEdit(value) {
      this.update = value;
      if (value == false) {
        return;
      }
      var newInfo = {
        old_username: this.old_username,
        first_name: this.$user.first_name,
        last_name: this.$user.last_name,
        username: this.$user.username,
        email: this.$user.email,
        phone_num: this.$user.phone_num,
        passport_num: this.$user.passport_num,
        birthday: this.$user.birthday.toISOString().substr(0, 10),
        address: this.$user.address
      };
      var obj = JSON.stringify(newInfo);
      axios.post("/customer/info/", obj).then(res => {
        var response = JSON.parse(JSON.stringify(res.data));
      });
      this.old_username = this.$user.username;
    },
    changeImage(e) {
      let file = e.target.files[0];
      if (!/\.(gif|jpg|jpeg|png|bmp|GIF|JPG|PNG)$/.test(e.target.value)) {
        alert(
          "Please one of the following extensions: gif, jpeg, jpg, png, bmp"
        );
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
        this.avatar = data;
        this.$user.avatar = data;
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
