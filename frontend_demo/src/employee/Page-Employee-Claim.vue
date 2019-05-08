<template>
  <div class="card card-default">
    <div class="card-header">
      <h3>{{$t('m.crtable')}}</h3>
    </div>
    <div class="card-body" style="font-size: 15px">
      <div>
        {{$t('m.upt')}}
        <br>
        {{$t('m.tip3')}}
        <br>
        {{$t('m.tip4')}}
      </div>
      <div class="btn-update">
        <b-btn
          variant="outline-success"
          class="mb-1 mr-1 right-button"
          @click="updateData()"
        >{{$t('m.uptable')}}</b-btn>
      </div>
    </div>

    <div class="card card-body table-part">
      <v-client-table :data="tableData" :columns="columns" :options="options">
        <template slot="Remark" slot-scope="props">
          <div>
            <b-btn
              variant="outline-dark"
              class="btn-xs"
              v-on:click="showModalData(props.row, 'Remark')"
            >{{$t('m.check1')}}</b-btn>
          </div>
        </template>
        <template slot="Baggage_ID" slot-scope="props">
          <div>
            <b-btn
              variant="outline-dark"
              class="btn-xs"
              v-on:click="showModalData(props.row, 'baggage')"
            >{{props.row.Baggage_ID}}</b-btn>
          </div>
        </template>
        <template slot="Reason" slot-scope="props">
          <div>
            <b-btn
              variant="outline-dark"
              class="btn-xs"
              v-on:click="showModalData(props.row, 'Reason')"
            >{{$t('m.check1')}}</b-btn>
          </div>
        </template>
        <template slot="Process" slot-scope="props">
          <b-btn
            variant="outline-success"
            class="btn-xs btn-decision"
            v-on:click="processDecision(props.row, '1')"
          >{{$t('m.agree')}}</b-btn>
          <b-btn
            variant="outline-warning"
            class="btn-xs btn-decision"
            v-on:click="processDecision(props.row, '-1')"
          >{{$t('m.mored')}}</b-btn>
          <b-btn
            variant="outline-danger"
            class="btn-xs btn-decision"
            v-on:click="processDecision(props.row, '0')"
          >{{$t('m.decline')}}</b-btn>
        </template>
      </v-client-table>
    </div>

    <b-modal id="modals-default" :title="modalTitle" cancel-only v-model="modalShow">
      <p>{{modalContent}}</p>
    </b-modal>

    <b-modal id="modals-default" :title="modalTitle" cancel-only v-model="modalShowBaggage">
      <div class="col-9">
        <p class="info-field">
          <b>{{$t('m.usern')}}</b>
          {{baggageItem.username}}
        </p>
        <p class="info-field">
          <b>{{$t('m.flight')}}</b>
          {{baggageItem.flight_number}}
        </p>
        <p class="info-field">
          <b>{{$t('m.height')}}</b>
          {{baggageItem.luggage_height}}
        </p>
        <p>
          <b class="info-field">{{$t('m.width')}}</b>
          {{baggageItem.luggage_width}}
        </p>
        <p>
          <b class="info-field">{{$t('m.sp')}}</b>
          {{baggageItem.sumPrice}}
        </p>
        <p>
          <b class="info-field">{{$t('m.remark')}}:</b>
          {{baggageItem.remark}}
        </p>
        <!-- START table-responsive-->
        <div class="table-responsive">
          <table class="table table-striped table-bordered table-hover card card-body">
            <thead>
              <tr>
                <th>{{$t('m.bp')}}</th>
                <th>{{$t('m.n')}}</th>
                <th>{{$t('m.price')}}</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="items in baggageItem.select_img_return_list" :key="items.id">
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
              </tr>
            </tbody>
          </table>
        </div>
        <!-- END table-responsive-->
      </div>
    </b-modal>

    <!-- bottom right animation example -->
    <notifications group="bottom-right" position="top right" :speed="500" :duration="2000"/>
  </div>
</template>
<script>
import PageOptions from "../config/PageOptions.vue";
import Vue from "vue";
import axios from "axios";
import { ClientTable } from "vue-tables-2";
import { all } from "q";
import { setTimeout } from "timers";

Vue.use(ClientTable);

var rawData = [];

export default {
  components: {
    ClientTable
  },
  computed: {
    columns() {
      return [
        this.$t("m.index"),
        this.$t("m.ccid"),
        this.$t("m.cbid"),
        this.$t("m.cun"),
        this.$t("m.cre"),
        this.$t("m.clt"),
        this.$t("m.clp"),
        this.$t("m.ccd"),
        this.$t("m.remark"),
        this.$t("m.pro")
      ];
    }
  },
  data() {
    return {
      employee_id: "",
      tableData: [],
      options: {
        pagination: { chunk: 5 },
        sortIcon: {
          is: "fa-sort",
          base: "fas",
          up: "fa-sort-up",
          down: "fa-sort-down"
        }
      },
      // remark and reason for lost
      modalShow: false,
      modalTitle: "",
      modalContent: "",

      // registerd baggage details
      modalShowBaggage: false,

      // variables used for displaying baggage info
      baggageItem: {
        flight_number: "",
        usernmae: "",
        luggage_height: "",
        luggage_width: "",
        remark: "",
        sumPrice: "",
        select_img_return_list: ""
      }
    };
  },
  created() {
    PageOptions.pageWithTopMenu = true;
    PageOptions.pageWithoutSidebar = true;

    this.updateData();
    this.retryData();
  },
  beforeRouteLeave(to, from, next) {
    PageOptions.pageWithTopMenu = false;
    PageOptions.pageWithoutSidebar = false;
    next();
  },
  methods: {
    showModalData(row, tag) {
      if (tag == "Reason") {
        this.modalContent = row.Reason;
        this.modalTitle = "Reason: " + row.Claim_ID;
        this.modalShow = true;
      } else if (tag == "Remark") {
        this.modalContent = row.Remark;
        this.modalTitle = "Remark: " + row.Claim_ID;
        this.modalShow = true;
      } else {
        this.checkBaggageDetail(row.insurance_order_id);
        this.modalTitle = "Registered Baggage Details: " + row.Claim_ID;
        this.modalShowBaggage = true;
      }
    },
    checkBaggageDetail(insurance_order_id) {
      var obj = JSON.stringify(insurance_order_id);
      axios
        .post("/list_insurance_order_info/", obj)
        .then(res => {
          var response = JSON.parse(JSON.stringify(res.data));
          if (response != null) {
            this.baggageItem.username = response.username;
            this.baggageItem.flight_number = response.flight_number;
            this.baggageItem.luggage_height = response.luggage_height;
            this.baggageItem.remark = response.remark;
            this.baggageItem.sumPrice = response.sumPrice;
            this.baggageItem.select_img_return_list =
              response.select_img_return_list;
          }
        })
        .catch(function(error) {
          console.log(error);
        });
    },
    processDecision(data, tag) {
      var decision = {
        claim_id: data.Claim_ID,
        employee_id: this.$employee.username,
        state: tag
      };
      var obj = JSON.stringify(decision);
      axios
        .post("/address_claim/", obj)
        .then(res => {
          var response = JSON.parse(JSON.stringify(res.data));
          alert(response);
        })
        .catch(function(error) {
          console.log(error);
        });
    },
    updateData() {
      rawData = [];
      axios
        .post("/list_all_claim/")
        .then(res => {
          if (res.data != null) {
            var response = JSON.parse(JSON.stringify(res.data));
            for (var i = 0; i < response.length; i++) {
              if (response[i].state == "-1") {
                rawData[rawData.length] = {
                  Claim_ID: response[i].id,
                  Baggage_ID: response[i].insurance_order_id,
                  Username: response[i].username,
                  Reason: response[i].reason,
                  "Lost Time": response[i].lost_time,
                  "Lost Place": response[i].lost_place,
                  "Claim Date": response[i].date,
                  Remark: response[i].remark
                };
              }
            }
          }
          if (rawData != null) {
            this.tableData = rawData.map((item, index) => {
              item["Index"] = index;
              return item;
            });
          }
        })
        .catch(err => console.log(err));
    },
    show(group, type = "") {
      const text = "New claim order awarting for process!";
      this.$notify({
        group,
        text,
        type,
        data: {
          randomNumber: Math.random()
        }
      });
    },
    retryData() {
      var timer;
      axios
        .post("/list_all_claim/")
        .then(res => {
          if (res.data != null) {
            var response = JSON.parse(JSON.stringify(res.data));
            this.show("bottom-right", "success");
            if (response.length != rawData.length) {
              this.show("bottom-right", "success");
            }
            timer = setInterval(() => {
              clearInterval(timer);
              this.retryData();
            }, 10000);
          } else {
            console.log("Periodlically update failed.");
            return;
          }
        })
        .catch(err => console.log(err));
    }
  }
};
</script>

<style scoped>
.table-part {
  background-color: rgba(127, 255, 170, 0.096) !important;
}

.btn-update {
  margin-top: 20px;
}

.btn-decision {
  margin-right: 5px;
}

.info-field {
  margin-left: 10px !important;
}

.info-field-left {
  margin-right: 80px !important;
}
</style>
