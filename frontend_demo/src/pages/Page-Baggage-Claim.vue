<template>
  <div class="card card-body">
    <h3 class="page-header">Initiate Baggage-lost Claim</h3>
    <p style="font-size: 15px">
      This page displays all the baggage registration orders within validity period.
      <br>According to our terms of service, as our customer, you can claim for compensation once already registered baggages are lost.
      <br>It is also worth noticing that once insurance balance is not enough to support a new claim, your application will be rejected.
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
        <div class="card-header text-success" v-else-if="(item.claim_id != null) && (item.insurance_order_id != null)">Claim process has been initiated</div>
        <div class="card-header text-danger" v-else>Baggage registration is waiting for process</div>
        <div class="row align-items-center" style="margin: 30px">
          <div class="col-5 text-center">
            <img
              class="img-thumbnail circle img-fluid thumb96"
              :src="item.luggage_image_inside"
              onerorr="this.src='../components/img/baggage_interior.png'"
              alt="Image"
            >
          </div>
          <div class="col-7">
            <div class="table-responsive">
              <h6>Order Detailed Information</h6>
              <p>Please check the table below before starting your claim.</p>
              <table class="table m-b-0">
                <thead>
                  <tr>
                    <th>Baggage Information</th>
                    <th>Other Information</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>Baggage Width: {{item.luggage_width}}</td>
                    <td>Username: {{$user.username}}</td>
                  </tr>
                  <tr>
                    <td>Baggage Height: {{item.luggage_height}}</td>
                    <td>
                      <b class="text-danger">Sum Price: {{item.sumPrice}}</b>
                    </td>
                  </tr>
                  <tr>
                    <td></td>
                    <td>Flight Number: {{item.flight_number}}</td>
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
          >Claim Lost Baggage</b-button>
        </div>
      </div>
    </div>

    <!-- Modal template -->
    <b-modal
      id="modals-default"
      ok-title="Submit Claim"
      ok-variant="danger"
      @ok="submitClaim()"
      v-model="modalShow"
    >
      <div slot="modal-title">
        Baggage-lost
        <span class="font-weight-light">Claim Form</span>
        <br>
        <small class="text-muted">Please fill in this form and initiate your request.</small>
      </div>

      <b-form-row>
        <b-form-group label="Lost Time" class="col">
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
        <b-form-group label="Lost Place" class="col">
          <b-input
            placeholder="The place where you lost your baggage"
            v-model="formData.lost_place"
            name="lost_place"
            v-validate="{ required: true}"
            v-bind:class="{'is-invalid': errors.has('lost_place')}"
          />
          <span style="color: red !important;">{{ errors.first('lost_place') }}</span>
        </b-form-group>
      </b-form-row>
      <b-form-row>
        <b-form-group label="Reason of Lost" class="col">
          <b-input
            placeholder="Reason of this lost"
            v-model="formData.reason"
            name="reason"
            v-validate="{ required: true}"
            v-bind:class="{'is-invalid': errors.has('reason')}"
          />
          <span style="color: red !important;">{{ errors.first('reason') }}</span>
        </b-form-group>
      </b-form-row>
      <b-form-row>
        <b-form-group label="Remark" class="col">
          <b-input
            placeholder="Other special requirements or illustration"
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
        insurance_order_id: "",
        lost_time: "",
        lost_place: "",
        reason: "",
        remark: ""
      },
      order_list: this.$user.insurance_order_list,
      modalShow: false
    };
  },
  created() {
    requireInfo = {
      username: this.$user.username,
    }
    var obj = JSON.stringify(requireInfo);
    axios
      .post("/list_user_all_insurance_order", obj)
      .then(res => {
        var response = JSON.parse(JSON.stringify(res.data));
        this.$user.insurance_order_list = response;
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
            if (response.state == "0") {
              alert(response);
            }
          })
          .catch(function(error) {
            console.log(error);
          });
      } else {
        alert("Please enter valid information in all required fields.");
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
