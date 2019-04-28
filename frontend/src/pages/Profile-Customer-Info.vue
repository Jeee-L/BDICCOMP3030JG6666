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
            <img :src="avatarSRC">
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
            <a
              href="javascript:;"
              v-on:click="show('about')"
              v-bind:class="{ 'active': tab.about }"
              class="nav-link"
              data-toggle="tab"
            >ABOUT</a>
          </li>
          <li class="nav-item">
            <a
              href="javascript:;"
              v-on:click="show('post')"
              v-bind:class="{ 'active': tab.post }"
              class="nav-link"
              data-toggle="tab"
            >POSTS</a>
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
        <!-- begin #profile-post tab -->
        <div class="tab-pane fade" v-bind:class="{ 'show active': tab.post }">
          <!-- begin timeline -->
          <ul class="timeline">
            <li>
              <!-- begin timeline-time -->
              <div class="timeline-time">
                <span class="date">today</span>
                <span class="time">04:20</span>
              </div>
              <!-- end timeline-time -->
              <!-- begin timeline-icon -->
              <div class="timeline-icon">
                <a href="javascript:;">&nbsp;</a>
              </div>
              <!-- end timeline-icon -->
            </li>
            <li>
              <!-- begin timeline-time -->
              <div class="timeline-time">
                <span class="date">yesterday</span>
                <span class="time">20:17</span>
              </div>
              <!-- end timeline-time -->
              <!-- begin timeline-icon -->
              <div class="timeline-icon">
                <a href="javascript:;">&nbsp;</a>
              </div>
              <!-- end timeline-icon -->
            </li>
            <li>
              <!-- begin timeline-time -->
              <div class="timeline-time">
                <span class="date">24 February 2014</span>
                <span class="time">08:17</span>
              </div>
              <!-- end timeline-time -->
              <!-- begin timeline-icon -->
              <div class="timeline-icon">
                <a href="javascript:;">&nbsp;</a>
              </div>
              <!-- end timeline-icon -->
            </li>
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
                  <span class="userimage">
                  </span>
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
            <li>
              <!-- begin timeline-icon -->
              <div class="timeline-icon">
                <a href="javascript:;">&nbsp;</a>
              </div>
              <!-- end timeline-icon -->
              <!-- begin timeline-body -->
              <div class="timeline-body">Loading...</div>
              <!-- begin timeline-body -->
            </li>
          </ul>
          <!-- end timeline -->
        </div>
        <!-- end #profile-post tab -->
        <!-- begin #profile-about tab -->
        <div class="tab-pane fade" v-bind:class="{ 'show active': tab.about }">
          <div class="row">
            <div class="col-lg-4">
              <div class="card card-default">
                <div class="card-body text-center">
                  <div class="py-4">
                    <img
                      class="img-fluid rounded-circle img-thumbnail thumb96"
                      :src="avatarSRC"
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
              <div class="card card-default d-none d-lg-block">
                <div class="card-header">
                  <div class="card-title text-center">Recent Orders</div>
                </div>
                <div class="card-body">
                  <!-- TO DO -->
                </div>
              </div>
            </div>
            <div class="col-lg-8">
              <div class="card card-default">
                <div class="card-header d-flex align-items-center">
                  <div class="d-flex justify-content-center col">
                    <div class="h4 m-0 text-center">Personal Information</div>
                  </div>
                  <div class="d-flex justify-content-end">
                    <b-dropdown id="ddown1" variant="link" no-caret right>
                      <template slot="button-content">
                        <em class="fa fa-ellipsis-v fa-lg text-muted"></em>
                      </template>
                      <b-dropdown-item>
                        <a href="javascript:;" v-b-modal.modalDialog1>Change Password</a>
                      </b-dropdown-item>
                      <b-dropdown-divider></b-dropdown-divider>
                      <b-dropdown-item>Delete contact</b-dropdown-item>
                    </b-dropdown>
                  </div>
                </div>

                <!-- begin change password modal -->
                <b-modal
                  id="modalDialog1"
                  cancel-title="Update Password"
                  cancel-variant="info"
                  ok-title="Cancel"
                  ok-variant="white"
                  title="Change Password"
                >
                  <div class="card-body">
                    <form action="#">
                      <div class="form-group">
                        <label>Current password</label>
                        <input class="form-control" type="password">
                      </div>
                      <div class="form-group">
                        <label>New password</label>
                        <input class="form-control" type="password">
                      </div>
                      <div class="form-group">
                        <label>Confirm new password</label>
                        <input class="form-control" type="password">
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
                      >* Please click the Edit Profile button to update personal information.</p> <br>
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
                              placeholder
                              v-model.lazy="$user.first_name"
                              :disabled="this.update"
                            >
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
                          <div class="col-md-8">
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

export default {
  data() {
    return {
      tab: {
        post: false,
        about: true
      },
      update: true,
      avatarSRC: require("../components/img/avatar.jpg")
    };
  },
  methods: {
    show: function(x) {
      this.tab.post = false;
      this.tab.about = false;

      switch (x) {
        case "about":
          this.tab.about = true;
          break;
        default:
          this.tab.post = true;
          break;
      }
    },
    startEdit(value) {
      this.update = value;
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
</style>
