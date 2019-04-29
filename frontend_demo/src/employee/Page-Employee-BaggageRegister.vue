<template>
  <div class="card card-default">
    <div class="card-header">
      <h3>Record for Insurance Orders</h3>
    </div>
    <div class="card-body">
      <v-client-table :data="tableData" :columns="columns" :options="options">
        <template slot="action" slot-scope="props">
          <div>
            <b-btn
              variant="outline-info mr-2"
              class="btn-xs"
              @click.prevent="edit(props.row)"
            >check order info</b-btn>
            <b-btn
              variant="outline-danger"
              class="btn-xs"
              @click.prevent="remove(props.row)"
            >process</b-btn>
          </div>
        </template>
        <template slot="child_row" slot-scope="props">
          <div>
            <strong>Platform:</strong>
            {{props.row.platform}}
          </div>
          <div>
            <strong>Grade:</strong>
            {{props.row.grade}}
          </div>
        </template>
      </v-client-table>
      <div class="text-right">
        <b-btn @click="clear()" class="mr-2">Clear Table</b-btn>
        <b-btn @click="reload()">Reload Table</b-btn>
      </div>
    </div>
  </div>
</template>
<script>
import PageOptions from '../config/PageOptions.vue'
import Vue from "vue";
import { ClientTable } from "vue-tables-2";

Vue.use(ClientTable);

const tableData = [
  {
    Username: "Trident",
    Insurance_Code: "7DEFNA458",
    Purchase_Date: "2019-04-14",
    Product_ID: "2",
    Project_ID: "1",
    browser: "Internet Explorer 4.0",
    platform: "Win 95+",
    version: "4",
    grade: "X"
  },
  {
    Username: "Trident",
    Insurance_Code: "67GHBIWQ",
    Purchase_Date: "2019-04-14",
    Product_ID: "3",
    Project_ID: "2",
    browser: "Internet Explorer 5.0",
    platform: "Win 95+",
    version: "5",
    grade: "C"
  },
  {
    Username: "Trident",
    Insurance_Code: "98UITGHIU",
    Purchase_Date: "2019-04-13",
    Product_ID: "2",
    Project_ID: "1",
    browser: "Internet Explorer 5.5",
    platform: "Win 95+",
    version: "5.5",
    grade: "A"
  },
  {
    Username: "Trident",
    Insurance_Code: "OU789UIDC",
    Purchase_Date: "2019-04-13",
    Product_ID: "1",
    Project_ID: "1",
    browser: "Internet Explorer 6",
    platform: "Win 98+",
    version: "6",
    grade: "A"
  },
  {
    Username: "Trident",
    Insurance_Code: "IUHJDF5RGH",
    Purchase_Date: "2019-04-13",
    Product_ID: "1",
    Project_ID: "2",
    browser: "Internet Explorer 7",
    platform: "Win XP SP2+",
    version: "7",
    grade: "A"
  },
  {
    Username: "Trident",
    Insurance_Code: "8877HJSDIY",
    Purchase_Date: "2019-04-12",
    Product_ID: "1",
    Project_ID: "1",
    browser: "AOL browser (AOL desktop)",
    platform: "Win XP",
    version: "6",
    grade: "A"
  },
  {
    Username: "Gecko",
    Insurance_Code: "IUYHJ678DE",
    Purchase_Date: "2019-04-11",
    Product_ID: "4",
    Project_ID: "1",
    browser: "Firefox 1.0",
    platform: "Win 98+ / OSX.2+",
    version: "1.7",
    grade: "A"
  },
  {
    Username: "Gecko",
    Insurance_Code: "PJKLDFG34D",
    Purchase_Date: "2019-04-10",
    Product_ID: "4",
    Project_ID: "3",
    browser: "Firefox 1.5",
    platform: "Win 98+ / OSX.2+",
    version: "1.8",
    grade: "A"
  },
  {
    Username: "Gecko",
    Insurance_Code: "IUJ980OJKL",
    Purchase_Date: "2019-04-08",
    Product_ID: "1",
    Project_ID: "1",
    browser: "Firefox 2.0",
    platform: "Win 98+ / OSX.2+",
    version: "1.8",
    grade: "A"
  },
  {
    Username: "Gecko",
    Insurance_Code: "OIUYHJD45",
    Purchase_Date: "2019-04-08",
    Product_ID: "2",
    Project_ID: "1",
    browser: "Firefox 3.0",
    platform: "Win 2k+ / OSX.3+",
    version: "1.9",
    grade: "A"
  },
  {
    Username: "Gecko",
    browser: "Camino 1.0",
    platform: "OSX.2+",
    version: "1.8",
    grade: "A"
  },
  {
    Username: "Gecko",
    browser: "Camino 1.5",
    platform: "OSX.3+",
    version: "1.8",
    grade: "A"
  },
  {
    Username: "Trident",
    browser: "Internet Explorer 4.0",
    platform: "Win 95+",
    version: "4",
    grade: "X"
  },
  {
    Username: "Trident",
    browser: "Internet Explorer 5.0",
    platform: "Win 95+",
    version: "5",
    grade: "C"
  },
  {
    Username: "Trident",
    browser: "Internet Explorer 5.5",
    platform: "Win 95+",
    version: "5.5",
    grade: "A"
  },
  {
    Username: "Trident",
    browser: "Internet Explorer 6",
    platform: "Win 98+",
    version: "6",
    grade: "A"
  },
  {
    Username: "Trident",
    browser: "Internet Explorer 7",
    platform: "Win XP SP2+",
    version: "7",
    grade: "A"
  },
  {
    Username: "Trident",
    browser: "AOL browser (AOL desktop)",
    platform: "Win XP",
    version: "6",
    grade: "A"
  },
  {
    Username: "Gecko",
    browser: "Firefox 1.0",
    platform: "Win 98+ / OSX.2+",
    version: "1.7",
    grade: "A"
  },
  {
    Username: "Gecko",
    browser: "Firefox 1.5",
    platform: "Win 98+ / OSX.2+",
    version: "1.8",
    grade: "A"
  },
  {
    Username: "Gecko",
    browser: "Firefox 2.0",
    platform: "Win 98+ / OSX.2+",
    version: "1.8",
    grade: "A"
  },
  {
    Username: "Gecko",
    browser: "Firefox 3.0",
    platform: "Win 2k+ / OSX.3+",
    version: "1.9",
    grade: "A"
  },
  {
    Username: "Gecko",
    browser: "Camino 1.0",
    platform: "OSX.2+",
    version: "1.8",
    grade: "A"
  },
  {
    Username: "Gecko",
    browser: "Camino 1.5",
    platform: "OSX.3+",
    version: "1.8",
    grade: "A"
  },
  {
    Username: "Trident",
    browser: "AOL browser (AOL desktop)",
    platform: "Win XP",
    version: "6",
    grade: "A"
  }
];

export default {
  components: {
    ClientTable
  },
  data() {
    return {
      tableData: [],
      columns: [
        "Insurance_Code",
        "Username",
        "Purchase_Date",
        "Product_ID",
        "Project_ID",
        "action"
      ],
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
    
    // Add IDs for child rows functionality
    this.tableData = tableData.map((item, index) => {
      item["id"] = index;
      return item;
    });
  },
  beforeRouteLeave (to, from, next) {
		PageOptions.pageWithTopMenu = false;
		PageOptions.pageWithoutSidebar = false;
		next();
	},
  methods: {
    edit(row) {
      alert(`Editing row id: ${row.id}`);
    },
    remove(row) {
      this.tableData = this.tableData.filter(item => row.id !== item.id);
    },
    reload() {
      this.tableData = tableData;
    },
    clear() {
      this.tableData = [];
    }
  }
};
</script>
