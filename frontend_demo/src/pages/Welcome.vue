<template>
  <div>
    <!-- begin #header -->
    <div id="header" class="header navbar-default">
      <!-- begin navbar-header -->
      <div class="navbar-header">
        <router-link to="/dashboard/v2" class="navbar-brand">
          <span class="navbar-logo"></span>
          <b>Hibernia-Sino</b> Travel Insurance
        </router-link>
        <button
          type="button"
          class="navbar-toggle p-0 m-r-0"
          v-on:click="toggleMobileMegaMenu"
          v-if="pageOptions.pageWithMegaMenu"
        >
          <span class="fa-stack fa-lg text-inverse m-t-2">
            <i class="far fa-square fa-stack-2x"></i>
            <i class="fa fa-cog fa-stack-1x"></i>
          </span>
        </button>
      </div>
      <!-- end navbar-header -->

      <header-mega-menu v-if="pageOptions.pageWithMegaMenu"></header-mega-menu>

      <!-- begin header-nav -->
      <ul class="navbar-nav navbar-right">
        <li class="nav-item">
          <a class="nav-link" href="/login">
            <i class="fa fa-user-circle fa-lg" aria-hidden="true">Sign In to Customer Center</i>
          </a>
        </li>
        <li
          v-if="!pageOptions.pageWithLanguageBar"
          v-bind:class="{ 'hidden-sm': pageOptions.pageWithMegaMenu }"
        >
          <form class="navbar-form" v-on:submit="checkForm">
            <div class="form-group">
              <input type="text" class="form-control" placeholder="Enter keyword">
              <button type="submit" class="btn btn-search">
                <i class="fa fa-search"></i>
              </button>
            </div>
          </form>
        </li>
        <li class="dropdown navbar-language" v-if="pageOptions.pageWithLanguageBar">
          <b-dropdown variant="link" menu-class="p-b-0">
            <template slot="button-content">
              <span class="flag-icon flag-icon-us" title="us"></span>
              <span class="name">EN</span>
              <b class="caret"></b>
            </template>
            <b-dropdown-item href="javascript:;">
              <span class="flag-icon flag-icon-us" title="us"></span> English
            </b-dropdown-item>
            <b-dropdown-item href="javascript:;">
              <span class="flag-icon flag-icon-cn" title="cn"></span> Chinese
            </b-dropdown-item>
            <b-dropdown-item href="javascript:;">
              <span class="flag-icon flag-icon-jp" title="jp"></span> Japanese
            </b-dropdown-item>
            <b-dropdown-item href="javascript:;">
              <span class="flag-icon flag-icon-be" title="be"></span> Belgium
            </b-dropdown-item>
            <b-dropdown-divider class="m-b-0"></b-dropdown-divider>
            <b-dropdown-item href="javascript:;" class="text-center">more options</b-dropdown-item>
          </b-dropdown>
        </li>
      </ul>
      <!-- end header navigation right -->
    </div>
    <!-- end #header -->

    <!-- begin sliding bar -->
    <div style="margin: 10px 50px;">
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
    </div>
    <!-- end sliding bar -->

    <div class="card card-default" style="margin: 10px 50px">
      <!-- begin about us -->
      <section class="section section-lg">
        <div class="container">
          <div class="row row-grid align-items-center">
            <div class="col-md-6 order-md-2">
              <img
                src="../assets/img/china-ireland.jpg"
                width="550px"
                height="230px"
                margin-top="80px"
              >
            </div>
            <div class="col-md-6 order-md-1">
              <div class="pr-md-5">
                <icon
                  name="ni ni-settings-gear-65"
                  class="mb-5"
                  size="lg"
                  type="success"
                  shadow
                  rounded
                ></icon>
                <h2 class="title" style="margin-top:50px;">Who we are?</h2>
                <p class="description">
                  We are Hibernia-Sino Travel Insurance Company, a travel insurance company
                  who specializes in travel between Ireland and China.Our aim is to provide
                  comprehensive compensation for your luggage protection!
                </p>
              </div>
            </div>
          </div>
        </div>
      </section>
      <!-- end about us -->

      <!-- begin pick us -->
      <div class="section section-team text-center">
        <div class="container">
          <h2 class="title" style="margin-top:50px;">Why pick us?</h2>
          <div class="team">
            <div class="row">
              <div class="col-md-4">
                <div class="team-player">
                  <img
                    style="margin-top:20px; width:130px; height:130px"
                    src="../assets/img/pick1.jpg"
                    alt="Thumbnail Image"
                    class="rounded-circle img-fluid img-raised"
                  >
                  <h4 class="title" style="margin-top:20px;">Guaranteed Best Prices</h4>
                </div>
              </div>
              <div class="col-md-4">
                <div class="team-player">
                  <img
                    style="margin-top:20px; width:130px; height:130px"
                    src="../assets/img/pick2.jpg"
                    alt="Thumbnail Image"
                    class="rounded-circle img-fluid img-raised"
                  >
                  <h4 class="title" style="margin-top:20px;">Fast and Easy to Buy Online</h4>
                </div>
              </div>
              <div class="col-md-4">
                <div class="team-player">
                  <img
                    style="margin-top:20px; width:130px; height:130px"
                    src="../assets/img/pick3.jpg"
                    alt="Thumbnail Image"
                    class="rounded-circle img-fluid img-raised"
                  >
                  <h4 class="title" style="margin-top:20px;">100% Safe and Secure Checkout</h4>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- end pick us -->

      <!-- begin service process -->
      <section class="section section-lg text-center">
        <div class="container">
          <div class="row justify-content-center text-center mb-lg">
            <div class="col-lg-8">
              <h2 class="title" style="margin-top:50px;">Our service process</h2>
              <p class="lead text" style="margin-top:20px;">Buy insurance</p>
            </div>
          </div>
          <div class="row">
            <div class="col-md-6 col-lg-3 mb-5 mb-lg-0">
              <div class="px-4">
                <img
                  src="../assets/img/p11.jpg"
                  class="img-fluid rounded shadow-lg"
                  style="width: 130px;height:100px;"
                >
                <div class="pt-4 text-center">
                  <h4 class="title">
                    <span class="d-block mb-1">Choose project</span>
                    <small class="h4 text">Step 1</small>
                  </h4>
                </div>
              </div>
            </div>
            <div class="col-md-6 col-lg-3 mb-5 mb-lg-0">
              <div class="px-4">
                <img
                  src="../assets/img/p12.jpg"
                  class="img-fluid rounded shadow-lg"
                  style="width: 130px;height:100px"
                >
                <div class="pt-4 text-center">
                  <h4 class="title">
                    <span class="d-block mb-1">Fill in information</span>
                    <small class="h4 text">Step 2</small>
                  </h4>
                </div>
              </div>
            </div>
            <div class="col-md-6 col-lg-3 mb-5 mb-lg-0">
              <div class="px-4">
                <img
                  src="../assets/img/p13.jpg"
                  class="img-fluid rounded shadow-lg"
                  style="width: 130px;height:100px"
                >
                <div class="pt-4 text-center">
                  <h4 class="title">
                    <span class="d-block mb-1">Pay online</span>
                    <small class="h4 text">Step 3</small>
                  </h4>
                </div>
              </div>
            </div>
            <div class="col-md-6 col-lg-3 mb-5 mb-lg-0">
              <div class="px-4">
                <img
                  src="../assets/img/p14.jpg"
                  class="img-fluid rounded shadow-lg"
                  style="width: 130px;height:100px"
                >
                <div class="pt-4 text-center">
                  <h4 class="title">
                    <span class="d-block mb-1">Look up policy</span>
                    <small class="h4 text">Step 4</small>
                  </h4>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section class="section section-lg text-center">
        <div class="container">
          <div class="row justify-content-center text-center mb-lg">
            <div class="col-lg-8">
              <p class="lead text" style="margin-top:20px;">Modify or cancel insurance</p>
            </div>
          </div>
          <div class="row">
            <div class="col-md-6 col-lg-3 mb-5 mb-lg-0">
              <div class="px-4">
                <img
                  src="../assets/img/p21.jpg"
                  class="img-fluid rounded shadow-lg"
                  style="width: 130px;height:100px;"
                >
                <div class="pt-4 text-center">
                  <h4 class="title">
                    <span class="d-block mb-1">Contact us</span>
                    <small class="h4 text">Step 1</small>
                  </h4>
                </div>
              </div>
            </div>
            <div class="col-md-6 col-lg-3 mb-5 mb-lg-0">
              <div class="px-4">
                <img
                  src="../assets/img/p22.jpg"
                  class="img-fluid rounded shadow-lg"
                  style="width: 130px;height:100px"
                >
                <div class="pt-4 text-center">
                  <h4 class="title">
                    <span class="d-block mb-1">Check the rules</span>
                    <small class="h4 text">Step 2</small>
                  </h4>
                </div>
              </div>
            </div>
            <div class="col-md-6 col-lg-3 mb-5 mb-lg-0">
              <div class="px-4">
                <img
                  src="../assets/img/p23.jpg"
                  class="img-fluid rounded shadow-lg"
                  style="width: 130px;height:100px"
                >
                <div class="pt-4 text-center">
                  <h4 class="title">
                    <span class="d-block mb-1">Fill in information</span>
                    <small class="h4 text">Step 3</small>
                  </h4>
                </div>
              </div>
            </div>
            <div class="col-md-6 col-lg-3 mb-5 mb-lg-0">
              <div class="px-4">
                <img
                  src="../assets/img/p24.jpg"
                  class="img-fluid rounded shadow-lg"
                  style="width: 130px;height:100px"
                >
                <div class="pt-4 text-center">
                  <h4 class="title">
                    <span class="d-block mb-1">Wait for result</span>
                    <small class="h4 text">Step 4</small>
                  </h4>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <div class="section section-team text-center">
        <div class="container">
          <div class="row justify-content-center text-center mb-lg">
            <div class="col-lg-8">
              <p class="lead text" style="margin-top:20px;">File claim</p>
            </div>
          </div>
          <div class="team">
            <div class="row">
              <div class="col-md-4">
                <div class="team-player">
                  <img
                    style="width: 130px;height:100px"
                    src="../assets/img/p31.jpg"
                    alt="Thumbnail Image"
                    class="img-fluid rounded shadow-lg"
                  >
                  <div class="pt-4 text-center">
                    <h4 class="title">
                      <span class="d-block mb-1">Report to service hotline</span>
                      <small class="h4 text">Step 1</small>
                    </h4>
                  </div>
                </div>
              </div>
              <div class="col-md-4">
                <div class="team-player">
                  <img
                    style="width: 130px;height:100px"
                    src="../assets/img/p32.jpg"
                    alt="Thumbnail Image"
                    class="img-fluid rounded shadow-lg"
                  >
                  <div class="pt-4 text-center">
                    <h4 class="title">
                      <span class="d-block mb-1">Submit information</span>
                      <small class="h4 text">Step 2</small>
                    </h4>
                  </div>
                </div>
              </div>
              <div class="col-md-4">
                <div class="team-player">
                  <img
                    style="width: 130px;height:100px"
                    src="../assets/img/p33.jpg"
                    alt="Thumbnail Image"
                    class="img-fluid rounded shadow-lg"
                  >
                  <div class="pt-4 text-center">
                    <h4 class="title">
                      <span class="d-block mb-1">Wait for result</span>
                      <small class="h4 text">Step 3</small>
                    </h4>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- end service process -->

      <!-- begin col-6 -->
      <div class="col-md-12">
        <div class="m-b-10 f-s-10 m-t-5 text-center">
          <h2 class="text-inverse" style="margin-top:50px;">Famous Landscapes in China and Ireland</h2>
        </div>
        <!-- begin card-group -->
        <div class="card-group" style="margin-top:30px;">
          <!-- begin card -->
          <div class="card">
            <img class="card-img-top" src="../assets/img/china-land1.jpeg" alt="Card image cap">
            <div class="card-block">
              <h4 class="card-title">The Great Wall</h4>
              <p
                class="card-text"
              >The Great Wall of China is a series of fortifications to protect the Chinese states and empires against the raids and invasions of the various nomadic groups of the Eurasian Steppe with an eye to expansion.</p>
            </div>
          </div>
          <!-- end card -->
          <!-- begin card -->
          <div class="card">
            <img class="card-img-top" src="../assets/img/china-land3.jpg" alt="Card image cap">
            <div class="card-block">
              <h4 class="card-title">West Lake</h4>
              <p
                class="card-text"
              >West Lake is a freshwater lake in Hangzhou, China. It has influenced poets and painters throughout Chinese history for its natural beauty and historic relics, and it has also been among the most important sources of inspiration for Chinese garden designers.</p>
            </div>
          </div>
          <!-- end card -->
          <!-- begin card -->
          <div class="card">
            <img class="card-img-top" src="../assets/img/ireland-land3.jpg" alt="Card image cap">
            <div class="card-block">
              <h4 class="card-title">Cliffs of Moher</h4>
              <p
                class="card-text"
              >The Cliffs of Moher are sea cliffs located at the southwestern edge of the Burren region in County Clare, Ireland.From the cliffs, visitors can see the Aran Islands in Galway Bay, the Maumturks and Twelve Pins mountain ranges to the north in County Galway, and Loop Head to the south.</p>
            </div>
          </div>
          <!-- end card -->
          <!-- begin card -->
          <div class="card">
            <img class="card-img-top" src="../assets/img/ireland-landn.jpg" alt="Card image cap">
            <div class="card-block">
              <h4 class="card-title">Blarney Castle</h4>
              <p
                class="card-text"
              >Blarney Castle is located in the small town of Blarney, Ireland.Built in 1446, it is one of the oldest castles in Ireland and one of the strongest fortresses.The Blarney Stone is among the machicolations of the castle.</p>
            </div>
          </div>
          <!-- end card -->
        </div>
        <!-- end card-group -->
      </div>
    </div>
  </div>
</template>

<script>
import PageOptions from "../config/PageOptions.vue";

export default {
  name: "Welcome",
  data() {
    return {
      pageOptions: PageOptions
    };
  },
  methods: {
    toggleMobileSidebar() {
      this.pageOptions.pageMobileSidebarToggled = !this.pageOptions
        .pageMobileSidebarToggled;
    },
    toggleMobileRightSidebar() {
      this.pageOptions.pageMobileRightSidebarToggled = !this.pageOptions
        .pageMobileRightSidebarToggled;
    },
    toggleMobileTopMenu() {
      this.pageOptions.pageMobileTopMenu = !this.pageOptions.pageMobileTopMenu;
    },
    toggleMobileMegaMenu() {
      this.pageOptions.pageMobileMegaMenu = !this.pageOptions
        .pageMobileMegaMenu;
    },
    toggleRightSidebar() {
      this.pageOptions.pageRightSidebarToggled = !this.pageOptions
        .pageRightSidebarToggled;
    },
    checkForm: function(e) {
      e.preventDefault();
      this.$router.push({ path: "/extra/search" });
    }
  },
  created() {
    PageOptions.pageEmpty = true;
  },
  beforeRouteLeave(to, from, next) {
    PageOptions.pageEmpty = false;
    next();
  }
};
</script>

<style scoped>
.description {
  font-size: 20px;
}
</style>
