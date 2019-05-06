<template>
  <div>
    <div class="card card-block" id="intelligent-system">
      <h3>{{$t('m.ics')}}</h3>
      <p>{{$t('m.food')}}</p>

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
            <h4 class="widget-chat-header-title">{{$t('m.name')}} {{$t('m.chatbot')}}</h4>
            <p class="widget-chat-header-desc">{{$t('m.answer')}}</p>
          </div>
        </div>
        <!-- end widget-chat-header -->
        <!-- begin widget-chat-body -->
        <div class="widget-chat-body overflow-scroll" style="height: 500px;">
          <!-- begin widget-chat-item -->
          <div class="widget-chat-item with-media left">
            <div class="widget-chat-media">
              <!-- <img alt src="/assets/img/user/user-1.jpg"> -->
            </div>
            <div class="widget-chat-info">
              <div class="widget-chat-info-container">
                <div class="widget-chat-name text-indigo">{{$t('m.hm')}}</div>
                <div class="widget-chat-message">{{$t('m.con1')}}</div>
                <div class="widget-chat-time">6:00PM</div>
              </div>
            </div>
          </div>
          <!-- end widget-chat-item -->
          <!-- begin widget-chat-item -->
          <div class="widget-chat-item with-media left">
            <div class="widget-chat-media">
              <!-- <img alt src="/assets/img/user/user-2.jpg"> -->
            </div>
            <div class="widget-chat-info">
              <div class="widget-chat-info-container">
                <div class="widget-chat-name text-primary">{{$t('m.ss')}}</div>
                <div class="widget-chat-message">{{$t('m.con2')}}</div>
                <div class="widget-chat-time">6:01PM</div>
              </div>
            </div>
          </div>
          <!-- end widget-chat-item -->
          <!-- begin widget-chat-item -->
          <div class="widget-chat-item right">
            <div class="widget-chat-info">
              <div class="widget-chat-info-container">
                <div class="widget-chat-message">{{$t('m.con3')}}</div>
                <div class="widget-chat-time">6:05PM</div>
              </div>
            </div>
          </div>
          <!-- end widget-chat-item -->
          <div class="text-center text-muted m-10 f-w-600">{{$t('m.t1')}}</div>
          <!-- begin widget-chat-item -->
          <div class="widget-chat-item with-media left">
            <div class="widget-chat-media">
              <!-- <img alt src="/assets/img/user/user-3.jpg"> -->
            </div>
            <div class="widget-chat-info">
              <div class="widget-chat-info-container">
                <div class="widget-chat-name text-orange">{{$t('m.ja')}}</div>
                <div class="widget-chat-message">{{$t('m.con4')}}
                  <div class="row row-space-2 m-t-5">
                    <!-- <div class="col-md-4">
                      <a href="javascript:;" class="widget-card widget-card-sm square m-b-2">
                        <div
                          class="widget-card-cover"
                        ></div>
                      </a>
                      <a href="javascript:;" class="widget-card widget-card-sm square m-b-2">
                        <div
                          class="widget-card-cover"
                        ></div>
                      </a>
                    </div>
                    <div class="col-md-4">
                      <a href="javascript:;" class="widget-card widget-card-sm square m-b-2">
                        <div
                          class="widget-card-cover"
                        ></div>
                      </a>
                      <a href="javascript:;" class="widget-card widget-card-sm square m-b-2">
                        <div
                          class="widget-card-cover"
                        ></div>
                      </a>
                    </div>
                    <div class="col-md-4">
                      <a href="javascript:;" class="widget-card widget-card-sm square m-b-2">
                        <div
                          class="widget-card-cover"
                        ></div>
                      </a>
                      <a href="javascript:;" class="widget-card widget-card-sm square m-b-2">
                        <div
                          class="widget-card-cover"
                        ></div>
                      </a>
                    </div> -->
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
          <form name>
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

