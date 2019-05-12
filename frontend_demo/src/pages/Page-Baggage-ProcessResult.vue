<template>
  <div>
    <div class>
      <div class="profile-header">
        <div class="result-header-cover"></div>
        <div class="profile-header-content">
          <div class="profile-header-info">
            <h4 class="m-t-10 m-b-5">{{$store.getters.username}}</h4>
            <p class="m-b-10">{{$t('m.checkc')}}</p>
          </div>
        </div>
        <ul class="profile-header-tab nav nav-tabs">
          <li class="nav-item">
            <a href="javascript:;" class="nav-link active" data-toggle="tab">{{$t('m.cpr')}}</a>
          </li>
        </ul>
      </div>
    </div>
    <div class="profile-content claim-body">
      <div class="tab-content p-0">
        <div class="tab-pane fade show active">
          <!-- begin timeline -->
          <ul class="timeline">
            <li v-for="item in claim_list" :key="item.id">
              <!-- begin timeline-time -->
              <div class="timeline-time">
                <span class="date">{{item.lost_place}}</span>
                <span class="time">{{item.lost_time}}</span>
              </div>
              <!-- end timeline-time -->
              <!-- begin timeline-icon -->
              <div class="timeline-icon">
                <a href="javascript:;">&nbsp;</a>
              </div>
              <!-- end timeline-icon -->
              <!-- begin timeline-body -->
              <div class="timeline-body" :class="changeBackground(item)">
                <div class="timeline-header">
                  <span class="username">{{$t('m.rid')}} {{item.order_id}}</span>
                  <span class="pull-right text-muted" style="color: black !important">{{item.date}}</span>
                </div>
                <div class="timeline-content">
                  <div class="col-12">
                    <div class="row">
                      <p class="info-field info-field-left">
                        <b>{{$t('m.iid')}}</b>
                        {{item.id}}
                      </p>
                      <p class="info-field info-field-left">
                        <b>{{$t('m.usern')}}</b>
                        {{item.username}}
                      </p>
                      <p class="info-field info-field-left">
                        <b>{{$t('m.eid')}}</b>
                        {{item.employee_id}}
                      </p>
                      <p class="info-field">
                        <b-btn
                          variant="outline-dark"
                          class="btn-xs"
                          v-on:click="checkBaggageDetail(item.order_id)"
                        >{{$t('m.check2')}}</b-btn>
                      </p>
                    </div>
                    <div class="row">
                      <p>
                        <b class="info-field">{{$t('m.re')}}</b>
                        {{item.remark}}
                      </p>
                    </div>
                    <p>
                      <b>{{$t('m.reason')}}</b>
                      {{item.reason}}
                    </p>
                  </div>
                </div>
                <div class="timeline-footer">
                  <div v-if="(item.state == '-1' || item.state == '2')">
                    <p class="text-dark" v-show="(item.state == '-1')">{{$t('m.pmd')}}</p>
                    <p
                      class="text-dark"
                      v-show="(item.state == '2')"
                      style="color: #834600 !important"
                    >{{$t('m.pmd2')}}</p>
                    <b-btn
                      variant="outline-warning"
                      class="btn-xs"
                      v-on:click="showModalData(item)"
                      :disabled="(item.state == '2')"
                    >{{$t('m.psi')}}</b-btn>
                  </div>
                  <p class="text-success" v-else-if="item.state == '1'">{{$t('m.ccs')}}</p>
                  <p class="text-danger" v-else>{{$t('m.sorry')}}</p>
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
      <!-- Modal template -->
      <b-modal
        id="modals-default"
        :ok-title="$t('m.tsc')"
        ok-variant="info"
        :cancel-title="$t('m.tcancel')"
        cancel-variant="white"
        @ok="submitClaim()"
        v-model="modalShow"
      >
        <div slot="modal-title">
          {{$t('m.bl1')}}
          <span class="font-weight-light">{{$t('m.cform')}}</span>
          <br>
          <small class="text-muted">{{$t('m.fill')}}</small>
        </div>

        <b-form-row>
          <b-form-group :label="$t('m.llt')" class="col">
            <b-input
              placeholder="YYYY-MM-DD"
              v-model="formData.lost_time"
              name="lost_time"
              v-validate="{ required: true, regex:/^(\d{4})(\-)(\d{2})(\-)(\d{2})$/ }"
              v-bind:class="{'is-invalid': errors.has($t('m.llt'))}"
            />
            <span style="color: red !important;">{{ errors.first($t('m.llt')) }}</span>
          </b-form-group>
        </b-form-row>
        <b-form-row>
          <b-form-group :label="$t('m.llp')" class="col">
            <b-input
              :placeholder="$t('m.pp')"
              v-model="formData.lost_place"
              name="lost_place"
              v-validate="{ required: true}"
              v-bind:class="{'is-invalid': errors.has($t('m.llp'))}"
            />
            <span style="color: red !important;">{{ errors.first($t('m.llp')) }}</span>
          </b-form-group>
        </b-form-row>
        <b-form-row>
          <b-form-group :label="$t('m.lrl')" class="col">
            <b-input
              :placeholder="$t('m.pr')"
              v-model="formData.reason"
              name="reason"
              v-validate="{ required: true}"
              v-bind:class="{'is-invalid': errors.has($t('m.lrl'))}"
            />
            <span style="color: red !important;">{{ errors.first($t('m.lrl')) }}</span>
          </b-form-group>
        </b-form-row>
        <b-form-row>
          <b-form-group :label="$t('m.remark')" class="col">
            <b-input :placeholder="$t('m.pos')" v-model="formData.remark"/>
          </b-form-group>
        </b-form-row>
      </b-modal>

      <!-- Baggage Detail Modal -->
      <b-modal id="modals-default" :title="modalTitle" cancel-only v-model="modalShowBaggage">
        <div class="col-12">
          <p class="info-field">
            <b style="margin-right: 10px">{{$t('m.usern')}}</b>
            {{baggageItem.username}}
          </p>
          <p class="info-field">
            <b style="margin-right: 10px">{{$t('m.flight')}}</b>
            {{baggageItem.flight_number}}
          </p>
          <p class="info-field">
            <b style="margin-right: 10px">{{$t('m.height')}}</b>
            {{baggageItem.luggage_height}}
          </p>
          <p>
            <b class="info-field" style="margin-right: 10px">{{$t('m.width')}}</b>
            {{baggageItem.luggage_width}}
          </p>
          <p>
            <b class="info-field" style="margin-right: 10px">{{$t('m.sp')}}</b>
            {{baggageItem.sumPrice}}
          </p>
          <p>
            <b class="info-field" style="margin-right: 10px">{{$t('m.remark')}}:</b>
            {{baggageItem.remark}}
          </p>
          <!-- START table-responsive-->
          <br>
          <div>
            <table class="table table-striped table-bordered table-hover">
              <thead>
                <tr>
                  <th>{{$t('m.bp')}}</th>
                  <th>{{$t('m.n')}}</th>
                  <th>{{$t('m.price')}}</th>
                  <th>{{$t('m.remark')}}</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="items in baggageItem.select_img" :key="items.id">
                  <td>
                    <div class="media align-items-center">
                      <img
                        class="img-fluid rounded thumb64"
                        :src="items.imgUrl"
                        width="40"
                        height="auto"
                        alt
                      >
                    </div>
                  </td>
                  <td>
                    <p>{{items.name}}</p>
                  </td>
                  <td>
                    <p>{{items.price}}</p>
                  </td>
                  <td>
                    <p>{{items.remark}}</p>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
          <!-- END table-responsive-->
        </div>
      </b-modal>
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
      formData: {
        check: "1",
        insurance_order_id: "",
        old_claim_id: "-1",
        lost_time: "",
        lost_place: "",
        reason: "",
        remark: ""
      },

      // Variables used for control
      modalShow: false,

      // remark and reason for lost
      modalTitle: "",
      modalContent: "",

      // registerd baggage details
      modalShowBaggage: false,

      // variables used for displaying baggage info
      baggageItem: {
        flight_number: "",
        username: "",
        luggage_height: "",
        luggage_width: "",
        remark: "",
        sumPrice: "",
        select_img_return_list: ""
      }
    };
  },
  computed: {
    claim_list() {
      return this.$store.getters.claim_list;
    }
  },
  created() {
    PageOptions.pageContentFullWidth = true;
    this.checkClaim();
  },
  methods: {
    checkClaim() {
      var requireInfo = {
        username: this.$store.getters.username
      };
      var obj = JSON.stringify(requireInfo);
      axios
        .post("/list_user_all_claim", obj)
        .then(res => {
          var response = JSON.parse(JSON.stringify(res.data));
          var claim_list = [];
          for (var i = 0; i < response.length; i++) {
            if (response[i].state != "-2") {
              claim_list[claim_list.length] = response[i];
            }
          }
          this.$store.state.claim_list = claim_list;
        })
        .catch(function(error) {
          console.log(error);
        });
    },
    changeBackground(item) {
      if (item.state == "-1" || item.state == "2") {
        return "background-moreinfo";
      } else if (item.state == "1") {
        return "background-success";
      } else {
        return "background-fail";
      }
    },
    showModalData(item) {
      this.formData.insurance_order_id = item.order_id;
      this.formData.old_claim_id = item.id;
      this.modalShow = true;
    },
    checkBaggageDetail(baggage_id) {
      this.modalTitle = this.$t("m.detail_title") + baggage_id;
      this.modalShowBaggage = true;

      var obj = JSON.stringify(baggage_id);
      axios
        .post("/list_insurance_order_info/", obj)
        .then(res => {
          var response = JSON.parse(JSON.stringify(res.data));
          if (response != null) {
            this.baggageItem.username = response.username;
            this.baggageItem.flight_number = response.flight_number;
            this.baggageItem.luggage_height = response.luggage_height;
            this.baggageItem.luggage_width = response.luggage_width;
            this.baggageItem.remark = response.remark;
            this.baggageItem.sumPrice = response.sumPrice;
            this.baggageItem.select_img = response.select_img;
          }
        })
        .catch(function(error) {
          console.log(error);
        });
    },
    submitClaim() {
      if (!this.isFormInvalid) {
        var obj = JSON.stringify(this.formData);
        axios
          .post("/luggage/order/list", obj)
          .then(res => {
            var response = JSON.parse(JSON.stringify(res.data));
            if (response.state) {
              if (response.state == "1") {
                this.swalNotification("success", "");
                this.checkClaim();
              } else {
                this.swalNotification(
                  "error",
                  this.showError(response.error_msg)
                );
              }
            }
          })
          .catch(function(error) {
            console.log(error);
          });
        this.requestData();
      } else {
        alert(this.$t("m.alpe"));
      }
    }
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

.timeline-footer {
  font-size: 14px !important;
}

.table-responsive {
  margin-left: 35px !important;
  width: 90% !important;
}

.info-field {
  margin-left: 10px !important;
}

.info-field-left {
  margin-right: 50px !important;
}

.background-moreinfo {
  background-color: rgb(243, 243, 226) !important;
}

.background-success {
  background-color: rgb(227, 243, 227) !important;
}

.background-fail {
  background-color: rgb(241, 227, 227) !important;
}

.claim-body {
  background-color: rgb(228, 228, 236) !important;
}
</style>
