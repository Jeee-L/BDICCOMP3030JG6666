<template>
  <div class="card card-body">
    <!-- begin page-header -->
    <h1 class="page-header">Insurance Table</h1>
    <!-- end page-header -->
    <vue-good-table
      :columns="columns"
      :rows="rows"
      :lineNumbers="true"
      :search-options="{ enabled: true, placeholder: 'Search this table' }"
      :pagination-options="{ enabled: true,  position: 'bottom' }"
      :selectOptions="{
				enabled: true,
				selectOnCheckboxOnly: true,
				selectionInfoClass: 'alert alert-info m-b-0 no-rounded-corner',
				selectionText: 'rows selected',
				clearSelectionText: 'clear',
			}"
    >
      <div slot="selected-row-actions" style="margin: -2px 0;">
        <button class="btn btn-xs btn-primary m-r-5">Action 1</button>
        <button class="btn btn-xs btn-grey">Action 2</button>
      </div>
      <template slot="table-row" slot-scope="props">
        <span>{{props.formattedRow[props.column.field]}}</span>
      </template>
    </vue-good-table>
  </div>
</template>

<script>
import PageOptions from "../config/PageOptions.vue";
import axios from "axios";

export default {
  created() {
    PageOptions.pageWithTopMenu = true;
    PageOptions.pageWithoutSidebar = true;

    axios
      .get("/check_all_insurance/")
      .then(res => {
        var response = JSON.parse(JSON.stringify(res.data));
        updateData(response);
      })
      .catch(err => console.log(err));
  },
  beforeRouteLeave(to, from, next) {
    PageOptions.pageWithTopMenu = false;
    PageOptions.pageWithoutSidebar = false;
    next();
  },
  data() {
    return {
      columns: [
        {
          label: "Insurance ID",
          field: "insurance_id",
          width: "10%",
          thClass: "text-nowrap",
          tdClass: "text-nowrap"
        },
        {
          label: "Username",
          field: "username",
          width: "10%",
          thClass: "text-nowrap",
          tdClass: "text-nowrap"
        },
        {
          label: "Project ID",
          field: "project_id",
          type: "number",
          width: "10%",
          tdClass: "text-center text-nowrap",
          thClass: "text-center text-nowrap"
        },
        {
          label: "Product ID",
          field: "product_id",
          type: "number",
          width: "10%",
          tdClass: "text-center text-nowrap",
          thClass: "text-center text-nowrap"
        },
        {
          label: "Price Total",
          field: "price_total",
          type: "number",
          width: "10%",
          tdClass: "text-center text-nowrap",
          thClass: "text-center text-nowrap"
        },
        {
          label: "Balance",
          field: "balance",
          type: "number",
          width: "10%",
          tdClass: "text-center text-nowrap",
          thClass: "text-center text-nowrap"
        },
        {
          label: "Date",
          field: "date",
          type: "date",
          dateInputFormat: "YYYY-MM-DD",
          dateOutputFormat: "YYYY-MM-DD",
          width: "10%",
          tdClass: "text-center text-nowrap",
          thClass: "text-center text-nowrap"
        },
        {
          label: "Status",
          field: "status",
          type: "number",
          width: "10%",
          tdClass: "text-center text-nowrap",
          thClass: "text-center text-nowrap"
        },
        {
          label: "Remark",
          type: "remark",
          tdClass: "text-center text-nowrap",
          thClass: "text-center text-nowrap"
        }
      ],
      rows: [
        {
          insurance_id: 'WED768123YU',
          username: 'dearCustomer',
          project_id: 1,
          product_id: 2,
          price_total: 90,
          balance: 240,
          status: 0, 
          date: "2018-10-31",
          remark: "There is no remark.",
        }
      ],
    };
  },
  methods: {
    updateData(response){
      if (response != null){
        this.rows = response;
        alert(response);
      }
    }
  }
};
</script>