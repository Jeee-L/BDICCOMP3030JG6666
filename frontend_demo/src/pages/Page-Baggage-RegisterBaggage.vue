<template>
  <div>
    <div class="card card-default" style="margin: 10px">
      <div class="card-header">
        <h3>Register Baggages Before Travelling</h3>
        <br>
        <p>
          Please register baggages in need before your trip.
          <br>Only insured baggages can get due compensation once lost.
        </p>
      </div>
      <div class="card-body">
        <div id="info" v-show="!showForm">
          <div class="row">
            <div>
              <pie-chart
                :data="pieChart.data"
                :options="pieChart.options"
                class="height-sm"
                id="pie"
              ></pie-chart>
              <h6 style="margin-left: 50px; width: 100%">
                This pie chart shows the proportions of your previous orders.
                <br>
                <br>Please note that the black section marks your balance.
                <br>If your newly registered baggage order exceeds the balance,
                <br>application will be rejected.
              </h6>
              <button
                type="button"
                class="btn btn-lime"
                v-on:click="changeFormStatus"
                style="margin-left: 130px; margin-top: 30px; font-size: 15px; padding: 15px"
              >Register Baggages Now</button>
            </div>
            <div class="col-xl-6" id="inforTable">
              <div class="row">
                <!-- begin col-3 -->
                <div style="margin-left: 20px; width: 45% !important">
                  <div class="widget widget-stats bg-gradient-blue">
                    <div class="stats-icon stats-icon-lg">
                      <i class="fa fa-archive fa-fw"></i>
                    </div>
                    <div class="stats-content">
                      <div class="stats-title">Time Remaining</div>
                      <div class="stats-number">11 Days</div>
                      <div class="stats-progress progress">
                        <div class="progress-bar" style="width: 40.5%;"></div>
                      </div>
                      <div class="stats-desc">Better than last week (40.5%)</div>
                    </div>
                  </div>
                </div>
                <!-- end col-3 -->
                <!-- begin col-3 -->
                <div style="margin-left: 20px; width: 45% !important">
                  <div class="widget widget-stats bg-gradient-purple">
                    <div class="stats-icon stats-icon-lg">
                      <i class="fa fa-dollar-sign fa-fw"></i>
                    </div>
                    <div class="stats-content">
                      <div class="stats-title">Insurance Balance</div>
                      <div class="stats-number">900 EUR</div>
                      <div class="stats-progress progress">
                        <div class="progress-bar" style="width: 76.3%;"></div>
                      </div>
                      <div class="stats-desc">Better than last week (76.3%)</div>
                    </div>
                  </div>
                </div>
                <!-- end col-3 -->
              </div>
              <br>
              <h6>
                Please check your remaing time and balance before creating new orders.
                <br>
                <br>The table below shows your detailed purchasing records, and helps keep track of your spendings and accounts.
              </h6>
              <br>
              <div class="card card-default">
                <div class="card-header">Baggage Registration Records</div>
                <div class="card-body">
                  <b-table responsive striped hover :items="itemsFields" :fields="parameters"></b-table>
                </div>
              </div>
            </div>
          </div>
        </div>

        <form-wizard
          @on-compvare="submitOrderForm"
          color="#80acdf"
          shape="circle"
          title="Register Baggages"
          subtitle="Please compvare required baggage information and provide your appraisal."
          v-show="showForm"
        >
          <!-- Headers -->
          <tab-content title="Baggage Information">
            <b-card class="mb-3">
              <!-- begin fieldset -->
              <fieldset>
                <!-- begin row -->
                <div class="row">
                  <!-- begin col-8 -->
                  <div class="col-md-8 offset-md-2">
                    <legend
                      class="no-border f-w-700 p-b-0 m-t-0 m-b-20 f-s-16 text-inverse"
                    >Please compvare baggage information and upload photos as required</legend>
                    <!-- begin form-group -->
                    <div class="form-group row m-b-10">
                      <label class="col-md-3 col-form-label text-md-right">
                        Baggage Width
                        <span class="text-danger">*</span>
                      </label>
                      <div class="col-md-6">
                        <input
                          type="number"
                          class="form-control"
                          placeholder="Baggage Width (in centimeter)"
                          name="baggage_width"
                          v-model="formData.baggage_width"
                          required
                        >
                      </div>
                    </div>
                    <!-- end form-group -->
                    <!-- begin form-group -->
                    <div class="form-group row m-b-10">
                      <label class="col-md-3 col-form-label text-md-right">
                        Baggage Height
                        <span class="text-danger">*</span>
                      </label>
                      <div class="col-md-6">
                        <input
                          type="number"
                          name="baggage_height"
                          placeholder="Baggage Height (in centimeter)"
                          class="form-control"
                          v-model="formData.baggage_height"
                          required
                        >
                      </div>
                    </div>
                    <!-- end form-group -->
                    <!-- begin form-group -->
                    <div class="form-group row m-b-10">
                      <label class="col-md-3 col-form-label text-md-right">
                        Baggage Color
                        <span class="text-danger">*</span>
                      </label>
                      <div class="col-md-6">
                        <input
                          type="text"
                          name="baggage_color"
                          placeholder="Baggage Color"
                          class="form-control"
                          v-model="formData.baggage_color"
                          required
                        >
                      </div>
                    </div>
                    <br>
                    <br>
                    <!-- end form-group -->
                    <!-- begin form-group -->
                    <div class="form-group row m-b-10">
                      <label class="col-md-3 col-form-label text-md-right">
                        Baggage Outside Image
                        <span class="text-danger">*</span>
                      </label>
                      <div class="col-md-6">
                        <!-- <label class="btn btn-primary mb-2 mr-2" for="upload-out"> -->
                        <input
                          type="file"
                          accept="image/png, image/jpeg, image/gif, image/jpg"
                          @change="selectOutImg"
                          id="upload-out"
                        >
                        <!-- </label> -->
                      </div>
                    </div>
                    <!-- end form-group -->
                    <!-- begin form-group -->
                    <div class="form-group row m-b-10">
                      <label class="col-md-3 col-form-label text-md-right">
                        Baggage Inside Image
                        <span class="text-danger">*</span>
                      </label>
                      <div class="col-md-6">
                        <!-- <label class="btn btn-primary mb-2 mr-2" for="upload-in"> -->
                        <input
                          type="file"
                          accept="image/png, image/jpeg, image/gif, image/jpg"
                          @change="selectInImg"
                          id="upload-in"
                        >
                        <!-- </label> -->
                      </div>
                    </div>
                    <!-- end form-group -->
                  </div>
                  <!-- end col-8 -->
                </div>
                <!-- end row -->
              </fieldset>
              <!-- end fieldset -->
            </b-card>
          </tab-content>
          <tab-content title="Upload Item Images in Your Baggage">
            <b-card class="mb-3">
              <!-- begin step-2 -->
              <div id="step-2">
                <!-- begin fieldset -->
                <fieldset>
                  <!-- begin row -->
                  <div class="row">
                    <!-- begin col-8 -->
                    <legend
                      class="no-border f-w-700 p-b-0 m-t-0 m-b-20 f-s-16 text-inverse"
                    >Please select one proper project (product)</legend>

                    <div class="container-md" style="width: 100% !important">
                      <div class="row">
                        <div class="col-xl-8">
                          <b-modal
                            v-model="cropImg.previewModalShow"
                            :ok-only="true"
                            ok-title="Close"
                            ok-variant="secondary"
                            :hide-header="true"
                          >
                            <img
                              :src="cropImg.previewImage"
                              alt="Modal Preview Image"
                              class="img-fluid d-block mx-auto"
                            >
                          </b-modal>
                          <div
                            class="mb-3"
                            :class="{ 'd-none': !cropImg.imageSrc }"
                            style="height: 400px;"
                          >
                            <vueCropper
                              ref="cropper"
                              :img="cropImg.imageSrc"
                              :outputSize="cropImg.outputSize"
                              :outputType="cropImg.outputType"
                              :info="true"
                              @realTime="previewRealTime"
                            />
                          </div>
                          <div class="btn-group flex-wrap">
                            <label class="btn btn-primary mb-2 mr-2" for="change-image">
                              <input
                                class="sr-only"
                                type="file"
                                id="change-image"
                                accept="image/png, image/jpeg, image/gif, image/jpg"
                                @change="changeImage($event)"
                              > Change Image
                            </label>
                            <b-btn
                              class="mr-2 mb-2"
                              @click="startCrop"
                              v-if="!cropImg.crap"
                              :disabled="!cropImg.imageSrc"
                            >Start Crop</b-btn>
                            <b-btn
                              class="mr-2 mb-2"
                              @click="stopCrop"
                              variant="danger"
                              v-else
                              :disabled="!cropImg.imageSrc"
                            >Stop Crop</b-btn>
                            <b-btn
                              class="mr-2 mb-2"
                              @click="clearCrop"
                              :disabled="!cropImg.imageSrc"
                            >Clear</b-btn>
                          </div>
                          <br>
                          <br>
                          <div class="btn-group flex-wrap">
                            <b-btn
                              class="mr-2 mb-4"
                              @click="storeItemImage('base64')"
                              :disabled="!cropImg.imageSrc"
                            >Select Item</b-btn>
                          </div>
                        </div>
                        <div class="col-xl-4">
                          <p>Output Preview</p>
                          <div
                            :style="{'width': cropImg.realTimePreviewData.w + 'px', 'height': cropImg.realTimePreviewData.h + 'px', 'overflow': 'hidden', 'margin': '5px'}"
                          >
                            <!-- v-for="item in itemImg" :key="item.id" -->
                            <div :style="cropImg.realTimePreviewData.div">
                              <img
                                :src="cropImg.realTimePreviewData.url"
                                :style="cropImg.realTimePreviewData.img"
                              >
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                  <!-- end row -->
                </fieldset>
                <!-- end fieldset -->
              </div>
              <!-- end step-2 -->
            </b-card>
          </tab-content>
          <tab-content title="Remarks and Questions">
            <b-card class="mb-3">
              <!-- begin step-3 -->
              <div id="step-3">
                <!-- begin fieldset -->
                <fieldset>
                  <!-- begin row -->
                  <div class="row">
                    <!-- begin col-8 -->
                    <div class="col-md-8 offset-md-2">
                      <legend
                        class="no-border f-w-700 p-b-0 m-t-0 m-b-20 f-s-16 text-inverse"
                      >Please leave Remarks if your have any questions</legend>
                      <p>
                        <br>In this section, please leave messages, if your have any special requirements.
                        <br>We will provide supports or solutions according to your remarks and questions.
                      </p>
                      <br>
                      <!-- begin form-group -->
                      <div class="form-group row m-b-10">
                        <label class="col-md-3 col-form-label text-md-right">Remark</label>
                        <div class="col-md-6">
                          <textarea
                            class="form-control m-b-10"
                            rows="12"
                            placeholder="Please speficy your personal needs or other feedbacks in this field. If your have any questions, please also var us know."
                            v-model="formData.remark"
                          ></textarea>
                        </div>
                      </div>
                      <!-- end form-group -->
                    </div>
                    <!-- end col-8 -->
                  </div>
                  <!-- end row -->
                </fieldset>
                <!-- end fieldset -->
              </div>
              <!-- end step-3 -->
            </b-card>
          </tab-content>
          <!-- Directions -->
          <b-btn variant="secondary" slot="prev">Back</b-btn>
          <b-btn variant="secondary" slot="next">Next</b-btn>
          <b-btn variant="info" slot="finish">Submit Insurance Order</b-btn>
        </form-wizard>
      </div>
    </div>
  </div>
</template>

<script>
import PieChart from "../components/vue-chartjs/PieChart";
import { FormWizard, TabContent, WizardStep } from "vue-form-wizard";
import axios from "axios";
import { constants } from "crypto";

export default {
  components: {
    PieChart,
    FormWizard,
    TabContent,
    WizardStep
  },
  data() {
    return {
      pieChart: {
        data: {
          labels: ["Order 1", "Order 2", "Order 3", "Order 4", "Remaining"],
          datasets: [
            {
              data: [300, 50, 100, 40, 120],
              backgroundColor: [
                "rgba(255, 91, 87, 0.7)",
                "rgba(245, 156, 26, 0.7)",
                "rgba(240, 243, 244, 0.7)",
                "rgba(182, 194, 201, 0.7)",
                "rgba(45, 53, 60, 0.7)"
              ],
              borderColor: [
                "#ff5b57",
                "#f59c1a",
                "#b4b6b7",
                "#b6c2c9",
                "#2d353c"
              ],
              borderWidth: 2,
              label: "My dataset"
            }
          ]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false
        }
      },
      parameters: ["Order_ID", "Registration_Time", "Compensation"],
      itemsFields: [
        {
          isActive: true,
          Order_ID: 1,
          Registration_Time: "2019-01-08",
          Compensation: "800"
        },
        {
          isActive: false,
          Order_ID: 2,
          Registration_Time: "2019-02-16",
          Compensation: "1000"
        },
        {
          isActive: false,
          Order_ID: 3,
          Registration_Time: "2019-02-24",
          Compensation: "1000"
        },
        {
          isActive: true,
          Order_ID: 4,
          Registration_Time: "2019-04-13",
          Compensation: "200"
        }
      ],
      cropImg: {
        imageSrc: "img/mb-sample.jpg",
        outputSize: 1,
        outputType: "jpeg",
        realTimePreviewData: {},
        crap: false,
        previewImage: null,
        previewModalShow: false,
        fileName: ""
      },
      itemImg: [],
      showForm: false,
      formData: {
        username: this.$user.username,
        baggage_width: "",
        baggage_height: "",
        baggage_outImg: null,
        baggage_inImg: null,
        remark: ""
      }
    };
  },
  computed: {
    isFormInvalid() {
      return Object.keys(this.fields).some(key => this.fields[key].invalid);
    }
  },
  methods: {
    changeFormStatus() {
      this.showForm = true;
    },
    checkProjectValue(e) {
      var value = e.target.value.split("-");
      this.formData.product_id = value[0];
      this.formData.project_id = value[1];
    },
    submitOrderForm() {
      const fd = new FormData();
      fd.append("image", this.baggage_outImg, this.baggage_outImg.name);

      if (!this.isFormInvalid && this.formData.project_id != "") {
        var obj = JSON.stringify(this.formData);
        axios
          .post("/luggage/order/create", obj)
          .then(res => {
            var response = JSON.parse(JSON.stringify(res.data));
            alert(response);
          })
          .catch(function(error) {
            console.log(error);
          });
      } else if (!this.isFormInvalid && this.formData.project_id != "") {
        alert("Please select one product.");
      } else {
        alert("Please enter valid information in all required fields.");
      }
    },
    selectOutImg(event) {
      this.baggage_outImg = event.target.files[0];
    },
    selectInImg(event) {
      this.baggage_inImg = event.target.files[0];
    },
    startCrop() {
      this.cropImg.crap = true;
      this.$refs.cropper.startCrop();
    },
    stopCrop() {
      this.cropImg.crap = false;
      this.$refs.cropper.stopCrop();
    },
    clearCrop() {
      this.$refs.cropper.clearCrop();
    },
    previewRealTime(data) {
      this.cropImg.realTimePreviewData = data;
    },
    storeItemImage(type) {
      if (type === "blob") {
        this.$refs.cropper.getCropBlob(data => {
          this.itemImg[this.itemImg.length] = { imgUrl: this.cropImg.imageSrc };
        });
      } else {
        this.$refs.cropper.getCropData(data => {
          this.itemImg[this.itemImg.length] = {
            imgUrl: this.cropImg.realTimePreviewData.url
          };
        });
      }
    },
    changeImage(e) {
      var file = e.target.files[0];
      this.fileName = file.name;
      if (!/\.(gif|jpg|jpeg|png|bmp|GIF|JPG|PNG)$/.test(e.target.value)) {
        alert(
          "Please one of the following extensions: gif, jpeg, jpg, png, bmp"
        );
        return false;
      }
      var reader = new FileReader();
      reader.onload = e => {
        var data;
        if (typeof e.target.result === "object") {
          data = window.URL.createObjectURL(new Blob([e.target.result]));
        } else {
          data = e.target.result;
        }
        this.cropImg.imageSrc = data;
      };
      reader.readAsArrayBuffer(file);
    }
  }
};
</script>

<style scoped>
#pie {
  margin-top: 40px;
  margin-left: 40px;
  margin-bottom: 40px;
}

#inforTable {
  margin: 40px;
}

#info {
  background: #edfaa225;
}

.mb-3 {
  background-color: #80acdf11 !important;
}
</style>
