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
        <template :slot="$t('m.remark')" slot-scope="props">
          <div>
            <b-btn
              variant="outline-dark"
              class="btn-xs"
              v-on:click="showModalData(props.row, 'Remark')"
            >{{$t('m.check1')}}</b-btn>
          </div>
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
        this.$t("m.cpt"),
        this.$t("m.cdate"),
        this.$t("m.cstate"),
        this.$t("m.remark")
      ];
    },
    lanChange() {
      this.updateData();
      return this.$t("m.date_lan") == "en";
    }
  },
  watch: {
    lanChange: {
      load: function() {
        this.updateData();
      },
      deep: true
    }
  },
  data() {
    return {
      rawData: [],
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
    };
  },
  created() {
    PageOptions.pageWithTopMenu = true;
    PageOptions.pageWithoutSidebar = true;

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
        this.modalContent = row[this.$t("m.remark")];
        this.modalTitle = "Remark: " + row[this.$t("m.cid")];
        this.modalShow = true;
      }
    },
    updateData() {
      this.rawData = [];
      axios
        .post("/check_all_insurance/")
        .then(res => {
          if (res.data != null) {
            var response = JSON.parse(JSON.stringify(res.data));
            for (var i = 0; i < response.length; i++) {
              this.rawData[this.rawData.length] = {
                [this.$t("m.cid")]: response[i].id,
                [this.$t("m.cun")]: response[i].username,
                [this.$t("m.cpt")]: response[i].amount_of_money,
                [this.$t("m.cdate")]: response[i].date,
                [this.$t("m.cstate")]: response[i].state,
                [this.$t("m.remark")]: response[i].remark
              };
            }
          }
          if (this.rawData != null) {
            this.tableData = this.rawData.map((item, index) => {
              item[this.$t("m.index")] = index;
              return item;
            });
          }
        })
        .catch(err => console.log(err));
    },
    show(group, type = "") {
      const text = this.$t('m.note_insurance');
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
      alert(`Editing row id: ${row[this.$t("m.remark")]}`);
    },
    retryData() {
      var timer;
      axios
        .post("/check_all_insurance/")
        .then(res => {
          if (res.data != null) {
            var response = JSON.parse(JSON.stringify(res.data));
            if (response.length != this.rawData.length) {
              this.show("bottom-right", "error");
            }
            timer = setInterval(() => {
              clearInterval(timer);
              this.retryData();
            }, 20000);
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
