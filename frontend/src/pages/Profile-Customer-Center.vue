<template>
  <div>
    <div class="card card-block" id="intelligent-system">
      <h3>Intelligent Consulting System</h3>
      <p>Food truck quinoa nesciunt laborum eiusmod. Brunch 3 wolf moon tempor, sunt aliqua put a bird on it squid single-origin coffee nulla assumenda shoreditch et. Nihil anim keffiyeh helvetica, craft beer labore wes anderson cred nesciunt sapiente ea proident. Ad vegan excepteur butcher vice lomo. Leggings occaecat craft beer farm-to-table, raw denim aesthetic synth nesciunt you probably haven't heard of them accusamus labore sustainable VHS.</p>

      <!-- begin widget-chat -->
      <div
        class="widget-chat widget-chat-rounded m-b-30"
        v-bind:class="{ 'inverse-mode': inverseMode }"
      >
        <!-- begin widget-chat-header -->
        <div class="widget-chat-header">
          <div class="widget-chat-header-icon">
            <i
              class="fab fa-earlybirds width-30 height-30 f-s-20 bg-yellow text-inverse text-center rounded-corner"
              style="line-height: 30px"
            ></i>
          </div>
          <div class="widget-chat-header-content">
            <h4 class="widget-chat-header-title">Hibernia-Sino Intelligent Chatbot</h4>
            <p class="widget-chat-header-desc">quick answers about insurance services questions</p>
          </div>
        </div>
        <!-- end widget-chat-header -->
        <!-- begin widget-chat-body -->
        <div class="widget-chat-body overflow-scroll" style="height: 500px;">
          <!-- begin widget-chat-item -->
          <div class="widget-chat-item with-media left">
            <div class="widget-chat-media">
              <img alt src="/assets/img/user/user-1.jpg">
            </div>
            <div class="widget-chat-info">
              <div class="widget-chat-info-container">
                <div class="widget-chat-name text-indigo">Hudson Mendes</div>
                <div class="widget-chat-message">Should we plan for a company trip this year?</div>
                <div class="widget-chat-time">6:00PM</div>
              </div>
            </div>
          </div>
          <!-- end widget-chat-item -->
          <!-- begin widget-chat-item -->
          <div class="widget-chat-item with-media left">
            <div class="widget-chat-media">
              <img alt src="/assets/img/user/user-2.jpg">
            </div>
            <div class="widget-chat-info">
              <div class="widget-chat-info-container">
                <div class="widget-chat-name text-primary">Sam Sugerman</div>
                <div class="widget-chat-message">ok let's do it</div>
                <div class="widget-chat-time">6:01PM</div>
              </div>
            </div>
          </div>
          <!-- end widget-chat-item -->
          <!-- begin widget-chat-item -->
          <div class="widget-chat-item right">
            <div class="widget-chat-info">
              <div class="widget-chat-info-container">
                <div class="widget-chat-message">i'm ok with it</div>
                <div class="widget-chat-time">6:05PM</div>
              </div>
            </div>
          </div>
          <!-- end widget-chat-item -->
          <div class="text-center text-muted m-10 f-w-600">Today</div>
          <!-- begin widget-chat-item -->
          <div class="widget-chat-item with-media left">
            <div class="widget-chat-media">
              <img alt src="/assets/img/user/user-3.jpg">
            </div>
            <div class="widget-chat-info">
              <div class="widget-chat-info-container">
                <div class="widget-chat-name text-orange">Jaxon Allwood</div>
                <div class="widget-chat-message">Here is some images for New Zealand
                  <div class="row row-space-2 m-t-5">
                    <div class="col-md-4">
                      <a href="javascript:;" class="widget-card widget-card-sm square m-b-2">
                        <div
                          class="widget-card-cover"
                          style="background-image: url(/assets/img/gallery/gallery-51-thumb.jpg)"
                        ></div>
                      </a>
                      <a href="javascript:;" class="widget-card widget-card-sm square m-b-2">
                        <div
                          class="widget-card-cover"
                          style="background-image: url(/assets/img/gallery/gallery-52-thumb.jpg)"
                        ></div>
                      </a>
                    </div>
                    <div class="col-md-4">
                      <a href="javascript:;" class="widget-card widget-card-sm square m-b-2">
                        <div
                          class="widget-card-cover"
                          style="background-image: url(/assets/img/gallery/gallery-53-thumb.jpg)"
                        ></div>
                      </a>
                      <a href="javascript:;" class="widget-card widget-card-sm square m-b-2">
                        <div
                          class="widget-card-cover"
                          style="background-image: url(/assets/img/gallery/gallery-54-thumb.jpg)"
                        ></div>
                      </a>
                    </div>
                    <div class="col-md-4">
                      <a href="javascript:;" class="widget-card widget-card-sm square m-b-2">
                        <div
                          class="widget-card-cover"
                          style="background-image: url(/assets/img/gallery/gallery-59-thumb.jpg)"
                        ></div>
                      </a>
                      <a href="javascript:;" class="widget-card widget-card-sm square m-b-2">
                        <div
                          class="widget-card-cover"
                          style="background-image: url(/assets/img/gallery/gallery-60-thumb.jpg)"
                        ></div>
                      </a>
                    </div>
                  </div>
                </div>
                <div class="widget-chat-time">6:20PM</div>
              </div>
            </div>
          </div>
          <!-- end widget-chat-item -->
        </div>
        <!-- end widget-chat-body -->
        <!-- begin widget-input -->
        <div class="widget-input widget-input-rounded">
          <form action method="POST" name>
            <div class="widget-input-container">
              <div class="widget-input-icon">
                <a href="javascript:;" class="text-grey">
                  <i class="fa fa-camera"></i>
                </a>
              </div>
              <div class="widget-input-box">
                <input
                  type="text"
                  class="form-control form-control-sm"
                  placeholder="Write a message..."
                >
              </div>
              <div class="widget-input-icon">
                <a href="javascript:;" class="text-grey">
                  <i class="fa fa-smile"></i>
                </a>
              </div>
              <div class="widget-input-divider"></div>
              <div class="widget-input-icon">
                <a href="javascript:;" class="text-grey">
                  <i class="fa fa-microphone"></i>
                </a>
              </div>
            </div>
          </form>
        </div>
        <!-- end widget-input -->
      </div>
      <!-- end widget-chat -->
    </div>
    <!-- end intelligent system -->
    <!-- begin col-6 -->
    <div class="col-lg-6 card card-block">
      <h4>Frequently Asked Questions</h4>
      <br>
      <!-- begin #accordion -->
      <div id="accordion" class="card-accordion">
        <!-- begin b-card -->
        <b-card no-body>
          <b-card-header
            header-tag="header"
            class="card-header bg-light-light-green text-green pointer-cursor"
            v-b-toggle.accordion1
          >Collapsible Group Item #1</b-card-header>
          <b-collapse id="accordion1" visible accordion="my-accordion">
            <b-card-body>Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus terry richardson ad squid. 3 wolf moon officia aute, non cupidatat skateboard dolor brunch. Food truck quinoa nesciunt laborum eiusmod. Brunch 3 wolf moon tempor, sunt aliqua put a bird on it squid single-origin coffee nulla assumenda shoreditch et. Nihil anim keffiyeh helvetica, craft beer labore wes anderson cred nesciunt sapiente ea proident. Ad vegan excepteur butcher vice lomo. Leggings occaecat craft beer farm-to-table, raw denim aesthetic synth nesciunt you probably haven't heard of them accusamus labore sustainable VHS.</b-card-body>
          </b-collapse>
        </b-card>
        <!-- end b-card -->
        <!-- begin b-card -->
        <b-card no-body>
          <b-card-header
            header-tag="header"
            class="card-header bg-light-light-green text-green pointer-cursor"
            v-b-toggle.accordion2
          >Collapsible Group Item #2</b-card-header>
          <b-collapse id="accordion2" accordion="my-accordion">
            <b-card-body>Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus terry richardson ad squid. 3 wolf moon officia aute, non cupidatat skateboard dolor brunch. Food truck quinoa nesciunt laborum eiusmod. Brunch 3 wolf moon tempor, sunt aliqua put a bird on it squid single-origin coffee nulla assumenda shoreditch et. Nihil anim keffiyeh helvetica, craft beer labore wes anderson cred nesciunt sapiente ea proident. Ad vegan excepteur butcher vice lomo. Leggings occaecat craft beer farm-to-table, raw denim aesthetic synth nesciunt you probably haven't heard of them accusamus labore sustainable VHS.</b-card-body>
          </b-collapse>
        </b-card>
        <!-- end b-card -->
        <!-- begin b-card -->
        <b-card no-body>
          <b-card-header
            header-tag="header"
            class="card-header bg-light-light-green text-green pointer-cursor"
            v-b-toggle.accordion3
          >Collapsible Group Item #3</b-card-header>
          <b-collapse id="accordion3" accordion="my-accordion">
            <b-card-body>Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus terry richardson ad squid. 3 wolf moon officia aute, non cupidatat skateboard dolor brunch. Food truck quinoa nesciunt laborum eiusmod. Brunch 3 wolf moon tempor, sunt aliqua put a bird on it squid single-origin coffee nulla assumenda shoreditch et. Nihil anim keffiyeh helvetica, craft beer labore wes anderson cred nesciunt sapiente ea proident. Ad vegan excepteur butcher vice lomo. Leggings occaecat craft beer farm-to-table, raw denim aesthetic synth nesciunt you probably haven't heard of them accusamus labore sustainable VHS.</b-card-body>
          </b-collapse>
        </b-card>
        <!-- end b-card -->
        <!-- begin b-card -->
        <b-card no-body>
          <b-card-header
            header-tag="header"
            class="card-header bg-light-light-green text-green pointer-cursor"
            v-b-toggle.accordion4
          >Collapsible Group Item #4</b-card-header>
          <b-collapse id="accordion4" accordion="my-accordion">
            <b-card-body>Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus terry richardson ad squid. 3 wolf moon officia aute, non cupidatat skateboard dolor brunch. Food truck quinoa nesciunt laborum eiusmod. Brunch 3 wolf moon tempor, sunt aliqua put a bird on it squid single-origin coffee nulla assumenda shoreditch et. Nihil anim keffiyeh helvetica, craft beer labore wes anderson cred nesciunt sapiente ea proident. Ad vegan excepteur butcher vice lomo. Leggings occaecat craft beer farm-to-table, raw denim aesthetic synth nesciunt you probably haven't heard of them accusamus labore sustainable VHS.</b-card-body>
          </b-collapse>
        </b-card>
        <!-- end b-card -->
        <!-- begin b-card -->
        <b-card no-body>
          <b-card-header
            header-tag="header"
            class="card-header bg-light-light-green text-green pointer-cursor"
            v-b-toggle.accordion5
          >Collapsible Group Item #5</b-card-header>
          <b-collapse id="accordion5" accordion="my-accordion">
            <b-card-body>Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus terry richardson ad squid. 3 wolf moon officia aute, non cupidatat skateboard dolor brunch. Food truck quinoa nesciunt laborum eiusmod. Brunch 3 wolf moon tempor, sunt aliqua put a bird on it squid single-origin coffee nulla assumenda shoreditch et. Nihil anim keffiyeh helvetica, craft beer labore wes anderson cred nesciunt sapiente ea proident. Ad vegan excepteur butcher vice lomo. Leggings occaecat craft beer farm-to-table, raw denim aesthetic synth nesciunt you probably haven't heard of them accusamus labore sustainable VHS.</b-card-body>
          </b-collapse>
        </b-card>
        <!-- end b-card -->
        <!-- begin b-card -->
        <b-card no-body>
          <b-card-header
            header-tag="header"
            class="card-header bg-light-light-green text-green pointer-cursor"
            v-b-toggle.accordion6
          >Collapsible Group Item #6</b-card-header>
          <b-collapse id="accordion6" accordion="my-accordion">
            <b-card-body>Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus terry richardson ad squid. 3 wolf moon officia aute, non cupidatat skateboard dolor brunch. Food truck quinoa nesciunt laborum eiusmod. Brunch 3 wolf moon tempor, sunt aliqua put a bird on it squid single-origin coffee nulla assumenda shoreditch et. Nihil anim keffiyeh helvetica, craft beer labore wes anderson cred nesciunt sapiente ea proident. Ad vegan excepteur butcher vice lomo. Leggings occaecat craft beer farm-to-table, raw denim aesthetic synth nesciunt you probably haven't heard of them accusamus labore sustainable VHS.</b-card-body>
          </b-collapse>
        </b-card>
        <!-- end b-card -->
        <!-- begin b-card -->
        <b-card no-body>
          <b-card-header
            header-tag="header"
            class="card-header bg-light-light-green text-green pointer-cursor"
            v-b-toggle.accordion7
          >Collapsible Group Item #7</b-card-header>
          <b-collapse id="accordion7" accordion="my-accordion">
            <b-card-body>Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus terry richardson ad squid. 3 wolf moon officia aute, non cupidatat skateboard dolor brunch. Food truck quinoa nesciunt laborum eiusmod. Brunch 3 wolf moon tempor, sunt aliqua put a bird on it squid single-origin coffee nulla assumenda shoreditch et. Nihil anim keffiyeh helvetica, craft beer labore wes anderson cred nesciunt sapiente ea proident. Ad vegan excepteur butcher vice lomo. Leggings occaecat craft beer farm-to-table, raw denim aesthetic synth nesciunt you probably haven't heard of them accusamus labore sustainable VHS.</b-card-body>
          </b-collapse>
        </b-card>
        <!-- end b-card -->
      </div>
      <!-- end #accordion -->
    </div>
    <!-- end col-6 -->
  </div>
  <!-- end this page division -->
</template>

<script>
export default {
  name: "Customer_Center"
};
</script>

<style scoped>
#intelligent-system {
    background-color: #c1f8ec9c;
}
</style>

