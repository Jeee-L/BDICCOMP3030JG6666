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
                  <span class="username">{{$t('m.rid')}} {{item.insurance_order_id}}</span>
                  <span class="pull-right text-muted" style="color: black !important">{{item.date}}</span>
                </div>
                <div class="timeline-content">
                  <div class="col-9">
                    <div class="row">
                      <p class="info-field info-field-left">
                        <b>{{$t('m.iid')}}</b>
                        {{item.insurance_id}}
                      </p>
                      <p class="info-field">
                        <b>{{$t('m.usern')}}</b>
                        {{item.username}}
                      </p>
                    </div>
                    <div class="row">
                      <p class="info-field info-field-left">
                        <b>{{$t('m.eid')}}</b>
                        {{item.employee_id}}
                      </p>
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
                  <div v-if="item.state == '-1'">
                    <p
                      class="text-dark"
                    >{{$t('m.pmd')}}</p>
                    <b-btn
                      variant="outline-info"
                      class="btn-xs"
                      v-on:click="showModalData(item.insurance_order_id)"
                    >{{$t('m.psi')}}</b-btn>
                  </div>
                  <p
                    class="text-success"
                    v-else-if="item.state == '1'"
                  >{{$t('m.ccs')}}</p>
                  <p
                    class="text-danger"
                    v-else
                  >{{$t('m.sorry')}}</p>
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
              v-bind:class="{'is-invalid': errors.has('lost_time')}"
            />
            <span style="color: red !important;">{{ errors.first('lost_time') }}</span>
          </b-form-group>
        </b-form-row>
        <b-form-row>
          <b-form-group :label="$t('m.llp')" class="col">
            <b-input
              :placeholder="$t('m.pp')"
              v-model="formData.lost_place"
              name="lost_place"
              v-validate="{ required: true}"
              v-bind:class="{'is-invalid': errors.has('lost_place')}"
            />
            <span style="color: red !important;">{{ errors.first('lost_place') }}</span>
          </b-form-group>
        </b-form-row>
        <b-form-row>
          <b-form-group :label="$t('m.lrl')" class="col">
            <b-input
              :placeholder="$t('m.pr')"
              v-model="formData.reason"
              name="reason"
              v-validate="{ required: true}"
              v-bind:class="{'is-invalid': errors.has('reason')}"
            />
            <span style="color: red !important;">{{ errors.first('reason') }}</span>
          </b-form-group>
        </b-form-row>
        <b-form-row>
          <b-form-group :label="$t('m.remark')" class="col">
            <b-input
              :placeholder="$t('m.pos')"
              v-model="formData.remark"
            />
          </b-form-group>
        </b-form-row>
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
      claim_list: this.$store.getters.claim_list,

      formData: {
        insurance_order_id: "",
        lost_time: "",
        lost_place: "",
        reason: "",
        remark: ""
      },

      // Variables used for control
      modalShow: false
    };
  },
  created() {
    PageOptions.pageContentFullWidth = true;

    requireInfo = {
      username: this.$store.getters.username
    };
    var obj = JSON.stringify(requireInfo);
    axios
      .post("/list_user_all_claim", obj)
      .then(res => {
        var response = JSON.parse(JSON.stringify(res.data));
        if (response != null){
          this.$store.getters.claim_list = response;
        }
      })
      .catch(function(error) {
        console.log(error);
      });
  },
  methods: {
    changeBackground(item) {
      if (item.state == "-1") {
        return "background-moreinfo";
      } else if (item.state == "1") {
        return "background-success";
      } else {
        return "background-fail";
      }
    },
    showModalData(insurance_order_id) {
      this.formData.insurance_order_id = insurance_order_id;
      this.modalShow = true;
    },
    submitClaim() {
      if (!this.isFormInvalid) {
        var obj = JSON.stringify(this.formData);
        axios
          .post("/luggage/order/list", obj)
          .then(res => {
            var response = JSON.parse(JSON.stringify(res.data));
            if (response.state == "0") {
              alert(response);
            }
          })
          .catch(function(error) {
            console.log(error);
          });
      } else {
        alert(this.$t('m.alpe'));
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
  margin-right: 80px !important;
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
