<template>
  <div>
    <!-- begin profile -->
    <div class="profile">
      <div class="profile-header">
        <!-- BEGIN profile-header-cover -->
        <div class="profile-header-cover"></div>
        <!-- END profile-header-cover -->
        <!-- BEGIN profile-header-content -->
        <div class="profile-header-content">
          <!-- BEGIN profile-header-img -->
          <div class="profile-header-img">
            <img src="../assets/img/avatar.jpg" alt>
          </div>
          <!-- END profile-header-img -->
          <!-- BEGIN profile-header-info -->
          <div class="profile-header-info">
            <h4 class="m-t-10 m-b-5">Catherine Mooney</h4>
            <p class="m-b-10"></p>
            <a
              a
              href="javascript:;"
              v-on:click="show('update')"
              v-bind:class="{ 'active': tab.update }"
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
              <!-- begin timeline-body -->
              <div class="timeline-body">
                <div class="timeline-header">
                  <span class="userimage">
                    <img src="/assets/img/user/user-12.jpg" alt>
                  </span>
                  <span class="username">
                    <a href="javascript:;">Sean Ngu</a>
                    <small></small>
                  </span>
                  <span class="pull-right text-muted">18 Views</span>
                </div>
                <div class="timeline-content">
                  <p>
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc faucibus turpis quis tincidunt luctus.
                    Nam sagittis dui in nunc consequat, in imperdiet nunc sagittis.
                  </p>
                </div>
                <div class="timeline-likes">
                  <div class="stats-right">
                    <span class="stats-text">259 Shares</span>
                    <span class="stats-text">21 Comments</span>
                  </div>
                  <div class="stats">
                    <span class="fa-stack fa-fw stats-icon">
                      <i class="fa fa-circle fa-stack-2x text-danger"></i>
                      <i class="fa fa-heart fa-stack-1x fa-inverse t-plus-1"></i>
                    </span>
                    <span class="fa-stack fa-fw stats-icon">
                      <i class="fa fa-circle fa-stack-2x text-primary"></i>
                      <i class="fa fa-thumbs-up fa-stack-1x fa-inverse"></i>
                    </span>
                    <span class="stats-total">4.3k</span>
                  </div>
                </div>
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
                <div class="timeline-comment-box">
                  <div class="user">
                    <img src="/assets/img/user/user-12.jpg">
                  </div>
                  <div class="input">
                    <form action>
                      <div class="input-group">
                        <input
                          type="text"
                          class="form-control rounded-corner"
                          placeholder="Write a comment..."
                        >
                        <span class="input-group-btn p-l-10">
                          <button
                            class="btn btn-primary f-s-12 rounded-corner"
                            type="button"
                          >Comment</button>
                        </span>
                      </div>
                    </form>
                  </div>
                </div>
              </div>
              <!-- end timeline-body -->
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
              <!-- begin timeline-body -->
              <div class="timeline-body">
                <div class="timeline-header">
                  <span class="userimage">
                    <img src="/assets/img/user/user-12.jpg" alt>
                  </span>
                  <span class="username">Sean Ngu</span>
                  <span class="pull-right text-muted">82 Views</span>
                </div>
                <div class="timeline-content">
                  <p>Location: United States</p>
                  <GmapMap
                    class="height-sm m-b-10"
                    :zoom="5"
                    :center="{lat: 25.304304, lng: -90.06591800000001}"
                  ></GmapMap>
                </div>
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
              <!-- begin timeline-body -->
              <div class="timeline-body">
                <div class="timeline-header">
                  <span class="userimage">
                    <img src="/assets/img/user/user-12.jpg" alt>
                  </span>
                  <span class="username">Sean Ngu</span>
                  <span class="pull-right text-muted">1,282 Views</span>
                </div>
                <div class="timeline-content">
                  <p class="lead">
                    <i class="fa fa-quote-left fa-fw pull-left"></i>
                    Quisque sed varius nisl. Nulla facilisi. Phasellus consequat sapien sit amet nibh molestie placerat. Donec nulla quam, ullamcorper ut velit vitae, lobortis condimentum magna. Suspendisse mollis in sem vel mollis.
                    <i
                      class="fa fa-quote-right fa-fw pull-right"
                    ></i>
                  </p>
                </div>
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
                    <img src="/assets/img/user/user-12.jpg" alt>
                  </span>
                  <span class="username">Sean Ngu</span>
                  <span class="pull-right text-muted">1,021,282 Views</span>
                </div>
                <div class="timeline-content">
                  <h4 class="template-title">
                    <i class="fa fa-map-marker-alt text-danger fa-fw"></i>
                    795 Folsom Ave, Suite 600 San Francisco, CA 94107
                  </h4>
                  <p>In hac habitasse platea dictumst. Pellentesque bibendum id sem nec faucibus. Maecenas molestie, augue vel accumsan rutrum, massa mi rutrum odio, id luctus mauris nibh ut leo.</p>
                  <p class="m-t-20">
                    <img src="/assets/img/gallery/gallery-5.jpg" alt>
                  </p>
                </div>
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
                      src="../assets/img/avatar.jpg"
                      alt="Contact"
                      onload="if (this.width>140 || this.height>226) if (this.width/this.height>140/226) this.width=140; else this.height=226;"
                    >
                  </div>
                  <h3 class="m-0 text-bold">Catherine Mooney</h3>
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
                      <form class="form-horizontal">
                        <div class="form-group row">
                          <label
                            class="text-bold col-xl-2 col-md-3 col-4 col-form-label text-right"
                            for="inputContact1"
                          >Name</label>
                          <div class="col-xl-10 col-md-9 col-8">
                            <input
                              class="form-control"
                              id="inputContact1"
                              type="text"
                              placeholder
                              value="Catherine Mooney"
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
                              type="email"
                              value="hibernia-sino@hotmail.com"
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
                              type="text"
                              value="@Social"
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
                              ></datepicker>
                            </div>
                        </div>
                        <div class="form-group row">
                          <label
                            class="text-bold col-xl-2 col-md-3 col-4 col-form-label text-right"
                            for="inputContact3"
                          >Mobile (CN)</label>
                          <div class="col-xl-10 col-md-9 col-8">
                            <input
                              class="form-control"
                              id="inputContact3"
                              type="text"
                              value="(86) 15611600577"
                            >
                          </div>
                        </div>
                        <div class="form-group row">
                          <label
                            class="text-bold col-xl-2 col-md-3 col-4 col-form-label text-right"
                            for="inputContact4"
                          >Mobile (IE)</label>
                          <div class="col-xl-10 col-md-9 col-8">
                            <input
                              class="form-control"
                              id="inputContact4"
                              type="text"
                              value="(12) 123 987 465"
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
                              value="EC8325666"
                            >
                          </div>
                        </div>
                        <div class="form-group row">
                          <label
                            class="text-bold col-xl-2 col-md-3 col-4 col-form-label text-right"
                            for="inputContact6"
                          >Address</label>
                          <div class="col-xl-10 col-md-9 col-8">
                            <textarea class="form-control" id="inputContact6" rows="4">Some nice Street, 1234</textarea>
                          </div>
                        </div>
                        <div class="form-group row">
                          <div class="col-md-10">
                            <button class="btn btn-info" type="button">Update</button>
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
        <!-- begin #profile-update tab -->
        <div class="tab-pane fade" v-bind:class="{ 'show active': tab.update }">
          <!-- begin table -->
          <div class="table-responsive">
            <table class="table table-profile">
              <thead>
                <tr>
                  <th></th>
                  <th>
                    <h4>
                      Micheal Meyer
                      <small>Lorraine Stokes</small>
                    </h4>
                  </th>
                </tr>
              </thead>
              <tbody>
                <tr class="highlight">
                  <td class="field">Mood</td>
                  <td>
                    <a href="javascript:;">Add Mood Message</a>
                  </td>
                </tr>
                <tr class="divider">
                  <td colspan="2"></td>
                </tr>
                <tr>
                  <td class="field">Mobile</td>
                  <td>
                    <i class="fa fa-mobile fa-lg m-r-5"></i> +1-(847)- 367-8924
                    <a href="javascript:;" class="m-l-5">Edit</a>
                  </td>
                </tr>
                <tr>
                  <td class="field">Home</td>
                  <td>
                    <a href="javascript:;">Add Number</a>
                  </td>
                </tr>
                <tr>
                  <td class="field">Office</td>
                  <td>
                    <a href="javascript:;">Add Number</a>
                  </td>
                </tr>
                <tr class="divider">
                  <td colspan="2"></td>
                </tr>
                <tr class="highlight">
                  <td class="field">About Me</td>
                  <td>
                    <a href="javascript:;">Add Description</a>
                  </td>
                </tr>
                <tr class="divider">
                  <td colspan="2"></td>
                </tr>
                <tr>
                  <td class="field">Country/Region</td>
                  <td>
                    <select class="form-control input-inline input-xs" name="region">
                      <option value="US" selected>United State</option>
                      <option value="AF">Afghanistan</option>
                      <option value="AL">Albania</option>
                      <option value="DZ">Algeria</option>
                      <option value="AS">American Samoa</option>
                      <option value="AD">Andorra</option>
                      <option value="AO">Angola</option>
                      <option value="AI">Anguilla</option>
                      <option value="AQ">Antarctica</option>
                      <option value="AG">Antigua and Barbuda</option>
                    </select>
                  </td>
                </tr>
                <tr>
                  <td class="field">City</td>
                  <td>Los Angeles</td>
                </tr>
                <tr>
                  <td class="field">State</td>
                  <td>
                    <a href="javascript:;">Add State</a>
                  </td>
                </tr>
                <tr>
                  <td class="field">Website</td>
                  <td>
                    <a href="javascript:;">Add Webpage</a>
                  </td>
                </tr>
                <tr>
                  <td class="field">Gender</td>
                  <td>
                    <select class="form-control input-inline input-xs" name="gender">
                      <option value="male">Male</option>
                      <option value="female">Female</option>
                    </select>
                  </td>
                </tr>
                <tr>
                  <td class="field">Birthdate</td>
                  <td>
                    <select class="form-control input-inline input-xs" name="day">
                      <option value="04" selected>04</option>
                    </select>
                    -
                    <select
                      class="form-control input-inline input-xs"
                      name="month"
                    >
                      <option value="11" selected>11</option>
                    </select>
                    -
                    <select
                      class="form-control input-inline input-xs"
                      name="year"
                    >
                      <option value="1989" selected>1989</option>
                    </select>
                  </td>
                </tr>
                <tr>
                  <td class="field">Language</td>
                  <td>
                    <select class="form-control input-inline input-xs" name="language">
                      <option value selected>English</option>
                    </select>
                  </td>
                </tr>
                <tr class="divider">
                  <td colspan="2"></td>
                </tr>
                <tr class="highlight">
                  <td class="field">&nbsp;</td>
                  <td class="p-t-10 p-b-10">
                    <button type="submit" class="btn btn-primary width-150">Update</button>
                    <button
                      type="submit"
                      class="btn btn-white btn-white-without-border width-150 m-l-5"
                    >Cancel</button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
          <!-- end table -->
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
        about: true,
        update: false
      }
    };
  },
  methods: {
    show: function(x) {
      this.tab.post = false;
      this.tab.about = false;
      this.tab.update = false;

      switch (x) {
        case "about":
          this.tab.about = true;
          break;
        case "update":
          this.tab.update = true;
          break;
        default:
          this.tab.post = true;
          break;
      }
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