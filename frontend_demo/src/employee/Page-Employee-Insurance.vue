<template>
  <div class="card card-default">
    <div class="card-header">
      <h3>{{$t('m.irtable')}}</h3>
    </div>
    <div class="card-body" style="font-size: 15px">
      <div>
        {{$t('m.upt')}}
        <br>
        {{$t('m.tip5')}}
        <br>
        {{$t('m.tip6')}}
      </div>
      <div class="btn-update">
        <b-btn
          variant="outline-info"
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
              @click.prevent="checkRemark(props.row)"
            >{{$t('m.check1')}}</b-btn>
          </div>
        </template>
      </v-client-table>
    </div>

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
        this.$t("m.cid"),
        this.$t("m.cun"),
        this.$t("m.cpid"),
        this.$t("m.cpid2"),
        this.$t("m.cpt"),
        this.$t("m.cdate"),
        this.$t("m.cstate"),
        this.$t("m.remark")
      ];
    }
  },
  data() {
    return {
      tableData: [],
      options: {
        pagination: { chunk: 5 },
        sortIcon: {
          is: "fa-sort",
          base: "fas",
          up: "fa-sort-up",
          down: "fa-sort-down"
        }
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
    updateData() {
      rawData = [];
      axios
        .post("/check_all_insurance/")
        .then(res => {
          if (res.data != null) {
            var response = JSON.parse(JSON.stringify(res.data));
            for (var i = 0; i < response.length; i++) {
              rawData[rawData.length] = {
                "Insurance ID": response[i].id,
                Username: response[i].username,
                "Product ID": response[i].product_id,
                "Project ID": response[i].project_id,
                "Price Total": response[i].amount_of_money,
                Date: response[i].date,
                State: response[i].state,
                Remark: response[i].remark
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
      const text = "New baggage order are waiting for process!";
      this.$notify({
        group,
        text,
        type,
        data: {
          randomNumber: Math.random()
        }
      });
    },
    checkRemark(row) {
      console.log(row);
      alert(`Editing row id: ${row.Remark}`);
    },
    retryData() {
      var timer;
      axios
        .post("/check_all_insurance/")
        .then(res => {
          if (res.data != null) {
            var response = JSON.parse(JSON.stringify(res.data));
            this.show("bottom-right", "error");
            if (response.length != rawData.length) {
              this.show("bottom-right", "error");
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
  background-color: rgba(255, 127, 127, 0.096) !important;
}

.btn-update {
  margin-top: 20px;
}
</style>
