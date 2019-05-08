<template>
  <div class="card card-body">
    <h3 class="page-header">{{$t('m.iblc')}}</h3>
    <p style="font-size: 15px">
      {{$t('m.display')}}
      <br>{{$t('m.according')}}
      <br>{{$t('m.br')}}
      <br>
      <br>
    </p>
    <div
      class="card card-body row order-whole"
      v-for="item in order_list"
      :key="item.insurance_order_id"
    >
      <div class="order-card">
        <div class="card-header" v-if="(item.claim_id == null) && (item.insurance_order_id != null)">{{item.insurance_order_id}}</div>
        <div class="card-header text-success" v-else-if="(item.claim_id != null) && (item.insurance_order_id != null)">{{$t('m.init')}}</div>
        <div class="card-header text-danger" v-else>{{$t('m.br')}}</div>
        <div class="row align-items-center" style="margin: 30px">
          <div class="col-5 text-center">
            <img
              class="img-thumbnail circle img-fluid thumb96"
              :src="item.luggage_image_inside"
              onerorr="this.src='../components/img/baggage_interior.png'"
              :alt="$t('m.altimage')"
            >
          </div>
          <div class="col-7">
            <div class="table-responsive">
              <h6>{{$t('m.odi')}}</h6>
              <p>{{$t('m.check')}}</p>
              <table class="table m-b-0">
                <thead>
                  <tr>
                    <th>{{$t('m.bi')}}</th>
                    <th>{{$t('m.other')}}</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>{{$t('m.width')}} {{item.luggage_width}}</td>
                    <td>{{$t('m.usn')}} {{$store.state.username}}</td>
                  </tr>
                  <tr>
                    <td>{{$t('m.height')}} {{item.luggage_height}}</td>
                    <td>
                      <b class="text-danger">{{$t('m.sp')}} {{item.sumPrice}}</b>
                    </td>
                  </tr>
                  <tr>
                    <td></td>
                    <td>{{$t('m.flight')}} {{item.flight_number}}</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
        <div class="card-footer d-flex">
          <b-button
            size="sm"
            class="mb-1 mr-1 right-button ml-auto"
            variant="outline-primary"
            type="button"
            v-on:click="showModalData(item.insurance_order_id)"
            :disabled="(item.claim_id != null) || (item.insurance_order_id == null)"
          >{{$t('m.clb')}}</b-button>
        </div>
      </div>
    </div>

    <!-- Modal template -->
    <b-modal
      id="modals-default"
      :ok-title="$t('m.tsc')"
      ok-variant="danger"
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
    <!-- end order card -->
  </div>
</template>


<script>
import axios from "axios";

export default {
  data() {
    return {
      formData: {
        check: "1",
        insurance_order_id: "",
        lost_time: "",
        lost_place: "",
        reason: "",
        remark: ""
      },
      order_list: this.$store.state.insurance_order_list,
      modalShow: false
    };
  },
  created() {
    requireInfo = {
      username: this.$store.state.username,
    }
    var obj = JSON.stringify(requireInfo);
    axios
      .post("/list_user_all_insurance_order", obj)
      .then(res => {
        var response = JSON.parse(JSON.stringify(res.data));
        this.$store.state.insurance_order_list = response;
      })
      .catch(function(error) {
        console.log(error);
      });
  },
  mounted() {},
  computed: {
    isFormInvalid() {
      return Object.keys(this.fields).some(key => this.fields[key].invalid);
    }
  },
  methods: {
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
            if (response.state) {
              if (response.state == "1") {
                this.swalNotification("success", "");
              } else {
                this.swalNotification("error", response.error_msg);
              }
            }
          })
          .catch(function(error) {
            console.log(error);
          });
      } else {
        alert(this.$t('m.alpe'));
      }
    },
    swalNotification(swalType, error_msg) {
      if (swalType == "success") {
        this.$swal({
          title: this.$t("m.claim_s_title"),
          text: this.$t("m.claim_s_text"),
          timer: 2000,
          showConfirmButton: false,
          type: swalType
        }).then();
      } else {
        this.$swal({
          title: this.$t("m.claim_f_title"),
          text: error_msg,
          timer: 2000,
          showConfirmButton: false,
          type: swalType
        }).then();
      }
    }
  }
};
</script>


<style scoped>
.baggage-img {
  width: auto !important;
  height: 20% !important;
  margin-bottom: 15px;
}

.order-card {
  background-color: rgba(253, 238, 224, 0.349) !important;
}

ul {
  font-size: 15px;
}

.group-img {
  /* margin-left: 10px !important; */
  /* margin-right: 10px !important; */
  width: 40% !important;
  height: 80% !important;
  max-height: 80% !important;
}

.table-responsive {
  margin-left: 35px !important;
  width: 90% !important;
}

.order-whole {
  border: 5px !important;
  border-color: bisque !important;
}

.baggage-table {
  margin-top: 2%;
  margin-bottom: 2%;
  /* margin-left: 8% */
}

.order-part {
  max-width: 50% !important;
}
</style>
