<template>
  <div class="card card-default">
    <div class="card-header">
      <h3>Claim Record Table</h3>
    </div>
    <div class="card-body" style="font-size: 15px">
      <div>
        Please click button "Update Table" once you want to check new data.
        <br>Once new insurance is created, the system will notfify employees at the top-right corner.
        <br>Requests for data update will be initiated every ten seconds.
      </div>
      <div class="btn-update">
        <b-btn
          variant="outline-info"
          class="mb-1 mr-1 right-button"
          @click="updateData()"
        >Update Table</b-btn>
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
            >Check</b-btn>
          </div>
        </template>
        <template slot="Reason" slot-scope="props">
          <div>
            <b-btn
              variant="outline-dark"
              class="btn-xs"
              v-on:click="showModalData(props.row, 'Reason')"
            >Check</b-btn>
          </div>
        </template>
        <template slot="Process" slot-scope="props">
          <b-btn
            variant="outline-success"
            class="btn-xs btn-decision"
            v-on:click="processDecision(props.row, '1')"
          >Agree</b-btn>
          <b-btn
            variant="outline-warning"
            class="btn-xs btn-decision"
            v-on:click="processDecision(props.row, '2')"
          >More</b-btn>
          <b-btn
            variant="outline-danger"
            class="btn-xs btn-decision"
            v-on:click="processDecision(props.row, '0')"
          >Decline</b-btn>
        </template>
      </v-client-table>
    </div>

    <b-modal id="modals-default" :title="modalTitle" cancel-only v-model="modalShow">
      <p>{{modalContent}}</p>
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
  data() {
    return {
      employee_id: "",
      tableData: [],
      columns: [
        "Index",
        "Claim_ID",
        "Insurance_ID",
        "Username",
        "Reason",
        "Lost Time",
        "Lost Place",
        "Claim Date",
        "Remark",
        "Process"
      ],
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
      modalContent: ""
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
      } else if (tag == "Remark") {
        this.modalContent = row.Remark;
        this.modalTitle = "Remark: " + row.Claim_ID;
      }
      this.modalShow = true;
    },
    processDecision(data, tag) {
      alert("process works");
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
        .get("/list_all_claim/")
        .then(res => {
          if (res.data != null) {
            var response = JSON.parse(JSON.stringify(res.data));
            for (var i = 0; i < response.length; i++) {
              if (response[i].status == "-1") {
                rawData[rawData.length] = {
                  Claim_ID: response[i].id,
                  Insurance_ID: response[i].insurance_id,
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
        .get("/list_all_claim/")
        .then(res => {
          if (res.data != null) {
            var response = JSON.parse(JSON.stringify(res.data));
            this.show("bottom-right", "danger");
            if (response.length != rawData.length) {
              this.show("bottom-right", "danger");
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

<style>
.table-part {
  background-color: rgba(127, 236, 255, 0.096) !important;
}

.btn-update {
  margin-top: 20px;
}

.btn-decision {
  margin-right: 5px;
}
</style>
