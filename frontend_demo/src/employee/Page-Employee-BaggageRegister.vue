<template>
  <div class="card card-default">
    <div class="card-header">
      <h3>{{$t('m.rtable')}}</h3>
    </div>
    <div class="card-body" style="font-size: 15px">
      <div>
        {{$t('m.upt')}}
        <br>
        {{$t('m.tip1')}}
        <br>
        {{$t('m.tip2')}}
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
        <template slot="Order_Details" slot-scope="props">
          <div>
            <b-btn
              variant="outline-dark"
              class="btn-xs"
              v-on:click="showModalData(props.row, 'baggage')"
            >{{$t('m.check1')}}</b-btn>
          </div>
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
        this.$t("m.coid"),
        this.$t("m.cid"),
        this.$t("m.cun"),
        this.$t("m.cod"),
        this.$t("m.ccid"),
        this.$t("m.crd"),
        this.$t("m.remark")
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
      // remark and Order_Details for lost
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
      if (tag == "Remark") {
        this.modalContent = row.Remark;
        this.modalTitle = "Remark: " + row.Claim_ID;
        this.modalShow = true;
      } else {
        this.checkBaggageDetail(row.this.$t("m.coid"));
        this.modalTitle = "Registered Baggage Details: " + row.Claim_ID;
        this.modalShowBaggage = true;
      }
    },
    checkBaggageDetail(baggage_id) {
      var obj = JSON.stringify(baggage_id);
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
    updateData() {
      rawData = [];
      axios
        .post("/list_all_insurance_order")
        .then(res => {
          if (res.data != null) {
            var response = JSON.parse(JSON.stringify(res.data));
            for (var i = 0; i < response.length; i++) {
              rawData[rawData.length] = {
                [this.$t("m.coid")]: response[i].id,
                [this.$t("m.cid")]: response[i].insurance_id,
                [this.$t("m.cun")]: response[i].username,
                [this.$t("m.cod")]: response[i].flight_number,
                [this.$t("m.ccid")]:
                  response[i].claim_id == null ? "0" : response[i].claim_id,
                [this.$t("m.crd")]: response[i].date,
                [this.$t("m.remark")]: response[i].remark
              };
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
      const text = "New claim order are waiting for process!";
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
        .post("/list_all_insurance_order")
        .then(res => {
          if (res.data != null) {
            var response = JSON.parse(JSON.stringify(res.data));
            this.show("bottom-right", "warn");
            if (response.length != rawData.length) {
              this.show("bottom-right", "warn");
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
  background-color: rgba(255, 246, 127, 0.096) !important;
}

.btn-update {
  margin-top: 20px;
}

.btn-decision {
  margin-right: 5px;
}
</style>
