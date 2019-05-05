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
          src="../assets/img/china-land1.jpg"
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
          src="../assets/img/ireland-land2.jpg"
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
          src="../assets/img/china-land2.jpg"
          alt="image slot"
        >
      </b-carousel-slide>
    </b-carousel>

    <br>

    <!-- note -->
    <div class="note note-lime note-with-right-icon m-b-15">
      <blockquote class="blockquote text-right">
        <h2 style="color: black">{{$t('m.welcome')}} {{$user.username}}</h2>
        <h5 style="color: black !important">{{nowTime}}</h5> <br>
        <h4>
          {{$t('m.get')}} 
            <br>{{$t('m.ybp')}}
        </h4>
        <footer class="blockquote-footer">
          {{$t('m.name')}} {{$t('m.name2')}}
        </footer>
      </blockquote>
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
  data() {
    return {
      slide: 0,
      sliding: null,
      nowTime: "",

      name: ""
    };
  },
  created() {
    this.nowTimes();
  },
  mounted() {
    // if (getCookie("user") == "") {
      // this.$router.push({ path: "/login" });
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
      delCookie("username");
    },
    timeFormate(timeStamp) {
      let year = new Date(timeStamp).getFullYear();
      let month =new Date(timeStamp).getMonth() + 1 < 10? "0" + (new Date(timeStamp).getMonth() + 1): new Date(timeStamp).getMonth() + 1;
      let date =new Date(timeStamp).getDate() < 10? "0" + new Date(timeStamp).getDate(): new Date(timeStamp).getDate();
      let hh =new Date(timeStamp).getHours() < 10? "0" + new Date(timeStamp).getHours(): new Date(timeStamp).getHours();
      let mm =new Date(timeStamp).getMinutes() < 10? "0" + new Date(timeStamp).getMinutes(): new Date(timeStamp).getMinutes();
      this.nowTime = year + "-" + month + "-" + date + " " + hh + ":" + mm;
    },
    nowTimes(){
      this.timeFormate(new Date());
      setInterval(this.nowTimes,30*1000);
    },

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
