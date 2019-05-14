<template>
  <div>
    <b-carousel
      id="carousel1"
      style="text-shadow: 1px 1px 2px #333;"
      controls
      indicators
      background="#ababab"
      :interval="3000"
      img-width="1024"
      img-height="480"
      v-model="slide"
      @sliding-start="onSlideStart"
      @sliding-end="onSlideEnd"
    >
      <!-- Slides with img slot -->
      <b-carousel-slide>
        <img
          slot="img"
          class="d-block img-fluid w-100"
          width="1024"
          height="480"
          :src="welcome1"
          alt="image slot"
        >
      </b-carousel-slide>

      <!-- Slides with img slot -->
      <b-carousel-slide>
        <img
          slot="img"
          class="d-block img-fluid w-100"
          width="1024"
          height="480"
          :src="welcome2"
          alt="image slot"
        >
      </b-carousel-slide>

      <!-- Slides with img slot -->
      <!-- Note the classes .d-block and .img-fluid to prevent browser default image alignment -->
      <b-carousel-slide>
        <img
          slot="img"
          class="d-block img-fluid w-100"
          width="1024"
          height="480"
          :src="welcome3"
          alt="image slot"
        >
      </b-carousel-slide>
    </b-carousel>

    <br>

    <!-- note -->
    <div class="note note-lime note-with-right-icon m-b-15">
      <blockquote class="blockquote text-right">
        <h2 style="color: black">{{$t('m.welcome')}} {{$store.getters.username}}</h2>
        <h5 style="color: black !important">{{nowTime}}</h5>
        <br>
        <h4>
          {{$t('m.get')}}
          <br>
          {{$t('m.ybp')}}
        </h4>
        <footer class="blockquote-footer">{{$t('m.name')}} {{$t('m.name2')}}</footer>
      </blockquote>
    </div>

    <div class="card card-default">
      <!-- begin service process -->
      <section class="section section-lg text-center">
        <div class="container-fluid">
          <div class="row justify-content-center text-center mb-lg">
            <div class="col-lg-8">
              <h2
                class="title bg-success text-white"
                style="margin-top:50px;padding:10px;"
              >{{$t('m.osp')}}</h2>
              <p class="lead text" style="margin-top:20px;">{{$t('m.osp1')}}</p>
            </div>
          </div>
          <div class="row">
            <div class="col-md-6 col-lg-3 col-sm-6 col-6 mb-5 mb-lg-0">
              <div class="px-4">
                <img
                  src="../assets/img/p11.jpg"
                  class="img-fluid rounded shadow-lg"
                  style="width: 120px;height:100px;"
                >
                <div class="pt-4 text-center">
                  <h4 class="title">
                    <span class="d-block mb-1">{{$t('m.osp11')}}</span>
                    <small class="h4 text">{{$t('m.step')}}</small>
                  </h4>
                </div>
              </div>
            </div>
            <div class="col-md-6 col-lg-3 col-sm-6 col-6 mb-5 mb-lg-0">
              <div class="px-4">
                <img
                  src="../assets/img/p12.jpg"
                  class="img-fluid rounded shadow-lg"
                  style="width: 110px;height:100px"
                >
                <div class="pt-4 text-center">
                  <h4 class="title">
                    <span class="d-block mb-1">{{$t('m.osp12')}}</span>
                    <small class="h4 text">{{$t('m.step')}} 2</small>
                  </h4>
                </div>
              </div>
            </div>
            <div class="col-md-6 col-lg-3 col-sm-6 col-6 mb-5 mb-lg-0">
              <div class="px-4">
                <img
                  src="../assets/img/p13.jpg"
                  class="img-fluid rounded shadow-lg"
                  style="width: 120px;height:100px"
                >
                <div class="pt-4 text-center">
                  <h4 class="title">
                    <span class="d-block mb-1">{{$t('m.osp13')}}</span>
                    <small class="h4 text">{{$t('m.step')}} 3</small>
                  </h4>
                </div>
              </div>
            </div>
            <div class="col-md-6 col-lg-3 col-sm-6 col-6 mb-5 mb-lg-0">
              <div class="px-4">
                <img
                  src="../assets/img/p14.jpg"
                  class="img-fluid rounded shadow-lg"
                  style="width: 120px;height:100px"
                >
                <div class="pt-4 text-center">
                  <h4 class="title">
                    <span class="d-block mb-1">{{$t('m.osp14')}}</span>
                    <small class="h4 text">{{$t('m.step')}} 4</small>
                  </h4>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section class="section section-lg text-center">
        <div class="container-fluid">
          <div class="row justify-content-center text-center mb-lg">
            <div class="col-lg-8">
              <p class="lead text" style="margin-top:10px;">{{$t('m.osp2')}}</p>
            </div>
          </div>
          <div class="row">
            <div class="col-md-6 col-lg-3 col-sm-6 col-6 mb-5 mb-lg-0">
              <div class="px-4">
                <img
                  src="../assets/img/p21.jpg"
                  class="img-fluid rounded shadow-lg"
                  style="width: 120px;height:100px;"
                >
                <div class="pt-4 text-center">
                  <h4 class="title">
                    <span class="d-block mb-1">{{$t('m.osp21')}}</span>
                    <small class="h4 text">{{$t('m.step')}} 1</small>
                  </h4>
                </div>
              </div>
            </div>
            <div class="col-md-6 col-lg-3 col-sm-6 col-6 mb-5 mb-lg-0">
              <div class="px-4">
                <img
                  src="../assets/img/p22.jpg"
                  class="img-fluid rounded shadow-lg"
                  style="width: 110px;height:100px"
                >
                <div class="pt-4 text-center">
                  <h4 class="title">
                    <span class="d-block mb-1">{{$t('m.osp22')}}</span>
                    <small class="h4 text">{{$t('m.step')}} 2</small>
                  </h4>
                </div>
              </div>
            </div>
            <div class="col-md-6 col-lg-3 col-sm-6 col-6 mb-5 mb-lg-0">
              <div class="px-4">
                <img
                  src="../assets/img/p23.jpg"
                  class="img-fluid rounded shadow-lg"
                  style="width: 90px;height:100px"
                >
                <div class="pt-4 text-center">
                  <h4 class="title">
                    <span class="d-block mb-1">{{$t('m.osp23')}}</span>
                    <small class="h4 text">{{$t('m.step')}} 3</small>
                  </h4>
                </div>
              </div>
            </div>
            <div class="col-md-6 col-lg-3 col-sm-6 col-6 mb-5 mb-lg-0">
              <div class="px-4">
                <img
                  src="../assets/img/p24.jpg"
                  class="img-fluid rounded shadow-lg"
                  style="width: 110px;height:100px"
                >
                <div class="pt-4 text-center">
                  <h4 class="title">
                    <span class="d-block mb-1">{{$t('m.osp24')}}</span>
                    <small class="h4 text">{{$t('m.step')}} 4</small>
                  </h4>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <div class="section section-team text-center">
        <div class="container-fluid">
          <div class="row justify-content-center text-center mb-lg">
            <div class="col-lg-8">
              <p class="lead text" style="margin-top:10px;">{{$t('m.osp3')}}</p>
            </div>
          </div>
          <div class="team">
            <div class="row">
              <div class="col-md-4 col-sm-4 col-4">
                <div class="team-player">
                  <img
                    style="width: 125px;height:100px"
                    src="../assets/img/p31.jpg"
                    alt="Thumbnail Image"
                    class="img-fluid rounded shadow-lg"
                  >
                  <div class="pt-4 text-center">
                    <h4 class="title">
                      <span class="d-block mb-1">{{$t('m.osp31')}}</span>
                      <small class="h4 text">{{$t('m.step')}} 1</small>
                    </h4>
                  </div>
                </div>
              </div>
              <div class="col-md-4 col-sm-4 col-4">
                <div class="team-player">
                  <img
                    style="width: 110px;height:100px"
                    src="../assets/img/p32.jpg"
                    alt="Thumbnail Image"
                    class="img-fluid rounded shadow-lg"
                  >
                  <div class="pt-4 text-center">
                    <h4 class="title">
                      <span class="d-block mb-1">{{$t('m.osp32')}}</span>
                      <small class="h4 text">{{$t('m.step')}} 2</small>
                    </h4>
                  </div>
                </div>
              </div>
              <div class="col-md-4 col-sm-4 col-4">
                <div class="team-player">
                  <img
                    style="width: 105px;height:100px"
                    src="../assets/img/p33.jpg"
                    alt="Thumbnail Image"
                    class="img-fluid rounded shadow-lg"
                  >
                  <div class="pt-4 text-center">
                    <h4 class="title">
                      <span class="d-block mb-1">{{$t('m.osp33')}}</span>
                      <small class="h4 text">{{$t('m.step')}} 3</small>
                    </h4>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- end service process -->
    </div>

    <div class="card">
      <div class="row row-space-10 card-block">
        <h3>{{$t('m.ic')}}</h3>
        <p>{{$t('m.ap')}}</p>
        <div class="col-md-4">
          <div class="alert alert-primary fade show m-b-10">
            <span class="close" data-dismiss="alert">&times;</span>
            <a href="#" class="alert-link">{{$t('m.tc')}}</a>.
          </div>
        </div>
        <div class="col-md-4">
          <div class="alert alert-info fade show m-b-10">
            <span class="close" data-dismiss="alert">&times;</span>
            <a href="#" class="alert-link">{{$t('m.ti')}}</a>.
          </div>
        </div>
        <div class="col-md-4">
          <div class="alert alert-purple fade show m-b-10">
            <span class="close" data-dismiss="alert">&times;</span>
            <a href="#" class="alert-link">{{$t('m.me')}}</a>.
          </div>
        </div>
        <div class="col-md-4">
          <div class="alert alert-success fade show m-b-10">
            <span class="close" data-dismiss="alert">&times;</span>
            <a href="#" class="alert-link">{{$t('m.bl')}}</a>.
          </div>
        </div>
        <div class="col-md-4">
          <div class="alert alert-green fade show m-b-10">
            <span class="close" data-dismiss="alert">&times;</span>
            <a href="#" class="alert-link">{{$t('m.fa')}}</a>.
          </div>
        </div>
        <div class="col-md-4">
          <div class="alert alert-secondary fade show m-b-10">
            <span class="close" data-dismiss="alert">&times;</span>
            <a href="#" class="alert-link">{{$t('m.ad')}}</a>.
          </div>
        </div>
        <div class="col-md-4">
          <div class="alert alert-warning fade show m-b-10">
            <span class="close" data-dismiss="alert">&times;</span>
            <a href="#" class="alert-link">{{$t('m.iw')}}</a>.
          </div>
        </div>
        <div class="col-md-4">
          <div class="alert alert-yellow fade show m-b-10">
            <span class="close" data-dismiss="alert">&times;</span>
            <a href="#" class="alert-link">{{$t('m.tpv')}}</a>.
          </div>
        </div>
        <div class="col-md-4">
          <div class="alert alert-secondary fade show m-b-10">
            <span class="close" data-dismiss="alert">&times;</span>
            <a href="#" class="alert-link">{{$t('m.mba')}}</a>.
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- end outer division -->
</template>

<script>
import { getCookie, delCookie } from "../assets/js/cookie.js";
export default {
  metaInfo: {
    title: "Hibernia-Sino Travel Insurances"
  },
  data() {
    return {
      slide: 0,
      sliding: null,
      nowTime: "",

      name: "",

      welcome1:
        this.$t("m.date_lan") == "en"
          ? require("../assets/img/welcome1.jpg")
          : require("../assets/img/welcome1_cn.jpg"),
      welcome2:
        this.$t("m.date_lan") == "en"
          ? require("../assets/img/welcome2.jpg")
          : require("../assets/img/welcome2_cn.jpg"),
      welcome3:
        this.$t("m.date_lan") == "en"
          ? require("../assets/img/welcome3.jpeg")
          : require("../assets/img/welcome3_cn.jpeg")
    };
  },
  computed: {
    lanChange() {
      return this.$t("m.date_lan") == "en";
    }
  },
  watch: {
    lanChange() {
      if (this.lanChange == true) {
        this.welcome1 = require("../assets/img/welcome1.jpg");
        this.welcome2 = require("../assets/img/welcome2.jpg");
        this.welcome3 = require("../assets/img/welcome3.jpeg");
      } else {
        this.welcome1 = require("../assets/img/welcome1_cn.jpg");
        this.welcome2 = require("../assets/img/welcome2_cn.jpg");
        this.welcome3 = require("../assets/img/welcome3_cn.jpeg");
      }
    }
  },
  created() {
    this.nowTimes();
  },
  mounted() {
    // if (getCookie("user") == "") {
    //   this.$router.push({ path: "/login" });
    // }
    this.nowTimes();
  },
  methods: {
    onSlideStart() {
      this.sliding = true;
    },
    onSlideEnd() {
      this.sliding = false;
    },
    quit() {
      delCookie("user");
    },
    timeFormate(timeStamp) {
      let year = new Date(timeStamp).getFullYear();
      let month =
        new Date(timeStamp).getMonth() + 1 < 10
          ? "0" + (new Date(timeStamp).getMonth() + 1)
          : new Date(timeStamp).getMonth() + 1;
      let date =
        new Date(timeStamp).getDate() < 10
          ? "0" + new Date(timeStamp).getDate()
          : new Date(timeStamp).getDate();
      let hh =
        new Date(timeStamp).getHours() < 10
          ? "0" + new Date(timeStamp).getHours()
          : new Date(timeStamp).getHours();
      let mm =
        new Date(timeStamp).getMinutes() < 10
          ? "0" + new Date(timeStamp).getMinutes()
          : new Date(timeStamp).getMinutes();
      this.nowTime = year + "-" + month + "-" + date + " " + hh + ":" + mm;
    },
    nowTimes() {
      this.timeFormate(new Date());
      setInterval(this.nowTimes, 30 * 1000);
    }
  }
};
</script>


<style lang="scss" scope>
.picture-china-home {
  background-image: url("../assets/img/china.jpg");
  margin-right: 20px;
  margin-left: 20px;
  margin-top: 15px;
  height: 130px;
  width: 100px;
}

.picture-ireland-home {
  background-image: url("../assets/img/ireland.jpg");
  margin-right: 20px;
  margin-left: 20px;
  margin-top: 15px;
  height: 130px;
  width: 100px;
}

.blockquote {
  margin-top: 0.1% !important;
  margin-bottom: 0.1% !important;
  margin-right: 1% !important;
}
</style>
