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
      <div class="note-icon">
      </div>
      <div class="row">
        <!-- Title Two Pictures -->
        <div class="col-lg-3 col-md-6">
          <!-- begin row -->
          <div class="row row-space-2 m-b-5">
            <!-- begin col-6 -->
            <div class="col-6">
              <a href="javascript:;" class="widget-card widget-card-rounded square m-b-2">
                <div class="widget-card-cover picture-china-home"></div>
              </a>
            </div>
            <!-- end col-6 -->
            <!-- begin col-6 -->
            <div class="col-6">
              <a href="javascript:;" class="widget-card widget-card-rounded square m-b-2">
                <div class="widget-card-cover picture-ireland-home"></div>
              </a>
            </div>
            <!-- end col-6 -->
          </div>
          <!-- end row -->
        </div>

        <div class="note-content text-right div-right">
          <!-- Flag China -->
          <!-- <div class="col-md-1 col-sm-2 col-3 m-b-10 text-center" style="display:inline">
            <h2 class="flag-icon flag-icon-cn width-full m-r-10 m-t-0 m-b-3" title="cn" id="cn"></h2>
            <h2 class="flag-icon flag-icon-ie width-full m-r-10 m-t-0 m-b-3" title="ie" id="ie"></h2>
          </div>-->
          <h2 style="color: black">Hibernia-Sino Travel Insurance</h2>
          <br>
          <h4>
            <b>Choose the best plan and start your journey!</b>
          </h4>
          <p>Travel with peace of mind. Compare the below plans and buy online with our best price guarantee.
            <br>Our checkout process is 100% safe and secure and you’ll receive your policy within minutes via email.
          </p>
        </div>
      </div>
    </div>

    <div class="card">
      <div class="row row-space-10 card-block">
        <h3>Insurance Coverage</h3>
        <p>The Annual Plan was designed to be an industry first by including Trip Cancellation and Trip Interruption coverages with upgradable limits of up to $5,000, Medical & Dental, Emergency Assistance & Transportation (Evacuation), Baggage and Baggage Delay, Accidental Death and Dismemberment coverages, and more.</p>
        <div class="col-md-4">
          <div class="alert alert-primary fade show m-b-10">
            <span class="close" data-dismiss="alert">&times;</span>
            <a href="#" class="alert-link">Trip Cancellation</a>.
          </div>
        </div>
        <div class="col-md-4">
          <div class="alert alert-info fade show m-b-10">
            <span class="close" data-dismiss="alert">&times;</span>
            <a href="#" class="alert-link">Trip Interruption</a>.
          </div>
        </div>
        <div class="col-md-4">
          <div class="alert alert-purple fade show m-b-10">
            <span class="close" data-dismiss="alert">&times;</span>
            <a href="#" class="alert-link">Medical Evacuation</a>.
          </div>
        </div>
        <div class="col-md-4">
          <div class="alert alert-success fade show m-b-10">
            <span class="close" data-dismiss="alert">&times;</span>
            <a href="#" class="alert-link">Baggage Loss</a>.
          </div>
        </div>
        <div class="col-md-4">
          <div class="alert alert-green fade show m-b-10">
            <span class="close" data-dismiss="alert">&times;</span>
            <a href="#" class="alert-link">Flight Accident</a>.
          </div>
        </div>
        <div class="col-md-4">
          <div class="alert alert-secondary fade show m-b-10">
            <span class="close" data-dismiss="alert">&times;</span>
            <a href="#" class="alert-link">Accidental Death</a>.
          </div>
        </div>
        <div class="col-md-4">
          <div class="alert alert-warning fade show m-b-10">
            <span class="close" data-dismiss="alert">&times;</span>
            <a href="#" class="alert-link">Inclement Weather</a>.
          </div>
        </div>
        <div class="col-md-4">
          <div class="alert alert-yellow fade show m-b-10">
            <span class="close" data-dismiss="alert">&times;</span>
            <a href="#" class="alert-link">Theft of Passports or Visas</a>.
          </div>
        </div>
        <div class="col-md-4">
          <div class="alert alert-secondary fade show m-b-10">
            <span class="close" data-dismiss="alert">&times;</span>
            <a href="#" class="alert-link">Mechanical Breakdown of Automobile</a>.
          </div>
        </div>
      </div>
    </div>

  </div>
  <!-- end outer division -->
</template>

<script>
export default {
  data() {
    return {
      slide: 0,
      sliding: null
    };
  },
  methods: {
    onSlideStart(slide) {
      this.sliding = true;
    },
    onSlideEnd(slide) {
      this.sliding = false;
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
</style>
