<template>
  <div>
    <div class>
      <div class="profile-header">
        <div class="result-header-cover"></div>
        <div class="profile-header-content">
          <div class="profile-header-info">
            <h4 class="m-t-10 m-b-5">{{$user.username}}</h4>
            <p class="m-b-10">Please check claim process results and records in this section.</p>
          </div>
        </div>
        <ul class="profile-header-tab nav nav-tabs">
          <li class="nav-item">
            <a href="javascript:;" class="nav-link active" data-toggle="tab">Claim Process Result</a>
          </li>
        </ul>
      </div>
    </div>
    <div class="profile-content">
      <div class="tab-content p-0">
        <div class="tab-pane fade show active">
          <!-- begin timeline -->
          <ul class="timeline">
            <li>
              <!-- begin timeline-time -->
              <div class="timeline-time">
                <span class="date">10 January 2014</span>
                <span class="time">20:43</span>
              </div>
              <!-- end timeline-time -->
              <!-- begin timeline-icon -->
              <div class="timeline-icon">
                <a href="javascript:;">&nbsp;</a>
              </div>
              <!-- end timeline-icon -->
              <!-- begin timeline-body -->
              <div class="timeline-body">
                <div class="timeline-header">
                  <span class="userimage"></span>
                  <span class="username">Sean Ngu</span>
                  <span class="pull-right text-muted">1,021,282 Views</span>
                </div>
                <div class="timeline-content"></div>
                <div class="timeline-footer">
                  <a href="javascript:;" class="m-r-15 text-inverse-lighter">
                    <i class="fa fa-thumbs-up fa-fw fa-lg m-r-3"></i> Like
                  </a>
                  <a href="javascript:;" class="m-r-15 text-inverse-lighter">
                    <i class="fa fa-comments fa-fw fa-lg m-r-3"></i> Comment
                  </a>
                  <a href="javascript:;" class="m-r-15 text-inverse-lighter">
                    <i class="fa fa-share fa-fw fa-lg m-r-3"></i> Share
                  </a>
                </div>
              </div>
              <!-- end timeline-body -->
            </li>
          </ul>
          <!-- end timeline -->
        </div>
        <!-- end #profile-post tab -->
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
          new_password: this.password,
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
    }
  },
  created() {
    PageOptions.pageContentFullWidth = true;
  },
  beforeRouteLeave(to, from, next) {
    PageOptions.pageContentFullWidth = false;
    next();
  },
  changeImage(e) {
    let file = e.target.files[0];
    if (!/\.(gif|jpg|jpeg|png|bmp|GIF|JPG|PNG)$/.test(e.target.value)) {
      alert("Please one of the following extensions: gif, jpeg, jpg, png, bmp");
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
      this.imageSrc = data;
    };
    reader.readAsArrayBuffer(file);
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

.profile-header .result-header-cover {
  background-image: url(../assets/css/default/images/result-cover.jpg);
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  position: absolute;
  left: 0;
  right: 0;
  top: 0;
  bottom: 0;
}

.profile-header-info {
  margin-left: 40px !important;
}
</style>
