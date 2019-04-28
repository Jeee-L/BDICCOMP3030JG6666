<template>
  <div>
    <div class="card card-default">
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
          @on-complete="submitOrderForm"
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
                        Flight Number
                        <span class="text-danger">*</span>
                      </label>
                      <div class="col-md-6">
                        <input
                          type="text"
                          class="form-control"
                          placeholder="Flight Number of the Journey"
                          name="flight_num"
                          v-model="formData.flight_num"
                          v-validate="{ required: true, regex:/^[\dA-Z][A-Z]{1,2}\d{2,4}$/}"
                          v-bind:class="{'is-invalid': errors.has('flight_num')}"
                        >
                        <span style="color: red !important;">{{ errors.first('flight_num') }}</span>
                      </div>
                    </div>
                    <!-- end form-group -->
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
                          name="luggage_width"
                          v-model="formData.luggage_width"
                          v-validate="{ required: true}"
                          v-bind:class="{'is-invalid': errors.has('luggage_width')}"
                        >
                        <span style="color: red !important;">{{ errors.first('luggage_width') }}</span>
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
                          name="luggage_height"
                          placeholder="Baggage Height (in centimeter)"
                          class="form-control"
                          v-model="formData.luggage_height"
                          v-validate="{ required: true}"
                          v-bind:class="{'is-invalid': errors.has('luggage_height')}"
                        >
                        <span style="color: red !important;">{{ errors.first('luggage_height') }}</span>
                      </div>
                    </div>
                    <!-- end form-group -->
                    <br>
                    <br>
                    <!-- begin form-group -->
                    <div class="form-group row m-b-10">
                      <label class="col-md-3 col-form-label text-md-right">
                        Baggage Outside Image
                        <span class="text-danger">*</span>
                      </label>
                      <div class="col-md-6">
                        <b-form-group
                          description="Please take a photo from the outside of your baggage."
                        >
                          <b-file
                            @change="convertImg($event, 'out')"
                            accept="image/*"
                            :state="'valid'"
                            name="baggage_inside_image"
                            v-validate="{ required: true}"
                            v-bind:class="{'is-invalid': errors.has('baggage_inside_image')}"
                          >
                            <span
                              style="color: red !important;"
                            >{{ errors.first('baggage_inside_image') }}</span>
                          </b-file>
                        </b-form-group>
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
                        <b-form-group
                          description="Please provide an iterior photo of your baggage."
                        >
                          <b-file
                            @change="convertImg($event, 'in')"
                            accept="image/*"
                            :state="'valid'"
                            name="baggage_outside_image"
                            v-validate="{ required: true}"
                            v-bind:class="{'is-invalid': errors.has('baggage_outside_image')}"
                          >
                            <span
                              style="color: red !important;"
                            >{{ errors.first('baggage_outside_image') }}</span>
                          </b-file>
                        </b-form-group>
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
                          <div class="card card-body instruct-crop">
                            <b>Instructions for selecting individual belongs</b>
                            <br>
                            <br>1. Click "Change Image" button to upload an interior photo of your baggage.
                            <br>2. Adjust image size by rolling your mouse.
                            <br>3. Click "Start Crop" button to select region of interest.
                            <br>4. Enter name and price in the input fields aside.
                            <br>5. Click "Submit Item" button to submit image and information.
                            <br>6. Click "Stop Crop" button to complete this selection process.
                          </div>
                          <div
                            class="mb-3"
                            :class="{ 'd-none': !cropImg.imageSrc }"
                            style="height: 400px;"
                          >
                            <vueCropper
                              ref="cropper"
                              :img="cropImg.imageSrc"
                              :full="cropImg.full"
                              :outputSize="cropImg.outputSize"
                              :outputType="cropImg.outputType"
                              :autoCropWidth="cropImg.autoCropWidth"
                              :autoCropHeight="cropImg.autoCropHeight"
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
                          </div>
                          <br>
                          <br>
                          <div class="btn-group flex-wrap">
                            <b-btn
                              class="mr-2 mb-4"
                              @click="storeItemImage('base64')"
                              :disabled="!cropImg.imageSrc"
                            >Submit Item</b-btn>
                          </div>
                        </div>
                        <div class="col-xl-4" v-show="!this.showInstruct">
                          <p class="text-danger">
                            Both of the name and your
                            <b>appraisal</b> are necessary for registration. Please provide these information before clicking
                            <b>"Submit Item"</b> button.
                          </p>
                          <b-form-group label="Item Name">
                            <b-input
                              type="text"
                              name="name"
                              placeholder="Please enter name of this belonging"
                              v-model="itemName"
                            />
                          </b-form-group>
                          <b-form-group label="Item Price (EUR)">
                            <b-input
                              type="text"
                              name="price"
                              placeholder="Please provide your appraisal of this belonging"
                              v-model="itemPrice"
                            />
                          </b-form-group>
                          <br>
                          <br>
                          <p>Output Preview</p>
                          <div
                            :style="{'width': cropImg.realTimePreviewData.w + 'px', 'height': cropImg.realTimePreviewData.h + 'px', 'overflow': 'hidden', 'margin': '5px'}"
                          >
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
          <tab-content title="Confirm Item Information">
            <b-card class="mb-3">
              <!-- begin step-3 -->
              <div id="step-3">
                <!-- begin fieldset -->
                <fieldset>
                  <!-- begin row -->
                  <div class="row">
                    <legend
                      class="no-border f-w-700 p-b-0 m-t-0 m-b-20 f-s-16 text-inverse"
                      style="margin-left: 20px !important"
                    >Please double-check item information and comfirm your order</legend>
                    <p style="margin-left: 20px !important" class="step-explain">
                      <br>Items listed below are selected from the previous page.
                      <br>Please recheck relevant information, and extra detailed explanation is appreciated.
                      <br>Once checking is finished, please click the "Create Order" button to generate your order.
                    </p>
                    <!-- START table-responsive-->
                    <div class="table-responsive">
                      <table class="table table-striped table-bordered table-hover card card-body">
                        <thead>
                          <tr>
                            <th>Description</th>
                          </tr>
                        </thead>
                        <tbody>
                          <tr v-for="items in formData.select_img" :key="items.id">
                            <td>
                              <div class="media align-items-center">
                                <div>
                                  <img
                                    class="img-fluid rounded thumb64"
                                    :src="items.imgUrl"
                                    width="70"
                                    height="auto"
                                    alt
                                  >
                                </div>
                                <div class="media-body d-flex row">
                                  <div>
                                    <div style="margin-left: 30px" class="row">
                                      <b-form-group label="Item Name" style="margin-left: 20px">
                                        <b-input
                                          type="text"
                                          id="itemName"
                                          name="itemName"
                                          v-validate="'required'"
                                          v-bind:class="{'is-invalid': errors.has('itemName')}"
                                          v-model="items.name"
                                          class="form-control"
                                        />
                                        <span
                                          style="color: red !important;"
                                        >{{ errors.first('itemName') }}</span>
                                      </b-form-group>
                                      <b-form-group
                                        label="Item Price (EUR)"
                                        style="margin-left: 20px"
                                      >
                                        <b-input
                                          type="text"
                                          id="itemPrice"
                                          name="itemPrice"
                                          v-validate="'required'"
                                          v-bind:class="{'is-invalid': errors.has('itemPrice')}"
                                          v-model="items.price"
                                          class="form-control"
                                        />
                                        <span
                                          style="color: red !important;"
                                        >{{ errors.first('itemPrice') }}</span>
                                      </b-form-group>
                                      <b-form-group
                                        label="Remark"
                                        style="margin-left: 20px; width: 400px"
                                      >
                                        <b-input
                                          type="text"
                                          id="remark"
                                          name="remark"
                                          placeholder="Please leave reasons for appraisal or requirements if needed"
                                          v-model="items.remark"
                                          class="form-control"
                                        />
                                      </b-form-group>
                                    </div>
                                  </div>
                                </div>
                              </div>
                            </td>
                          </tr>
                        </tbody>
                      </table>
                    </div>
                    <!-- END table-responsive-->
                    <b-button
                      size="lg"
                      class="mb-1 mr-1 right-button"
                      variant="outline-primary"
                      type="button"
                      v-on:click="generateOrder"
                    >Create Order</b-button>
                    <!-- begin invoice -->
                    <div class="invoice" v-show="this.showOrder">
                      <div
                        class="invoice-company text-inverse f-w-600"
                        style="font-size: 15px"
                      >Registration Order</div>
                      <!-- begin invoice-content -->
                      <div class="invoice-content">
                        <!-- begin table-responsive -->
                        <div class="table-responsive">
                          <table class="table table-invoice">
                            <thead>
                              <tr>
                                <th class="text-left" width="30%">NAME</th>
                                <th class="text-left" width="30%">PRICE (APPRAISAL)</th>
                                <th class="text-left" width="40%">REMARK</th>
                              </tr>
                            </thead>
                            <tbody>
                              <tr v-for="items in formData.select_img" :key="items.id">
                                <td>
                                  <span class="text-inverse">{{items.name}}</span>
                                </td>
                                <td>
                                  <small class="text-inverse">{{items.price}}</small>
                                </td>
                                <td class="text-inverse">{{items.remark}}</td>
                              </tr>
                            </tbody>
                          </table>
                        </div>
                        <!-- end table-responsive -->
                        <!-- begin invoice-price -->
                        <div
                          class="invoice-price"
                          style="width: 100% !important; height: auto !important"
                        >
                          <div class="invoice-price-left">
                            <div class="invoice-price-row"></div>
                          </div>
                          <div class="invoice-price-right">
                            <small>TOTAL</small>
                            <span
                              class="f-w-600"
                              style="font-size: 25px !important"
                            >{{formData.sum_price}} EUR</span>
                          </div>
                        </div>
                        <!-- end invoice-price -->
                      </div>
                      <!-- end invoice-content -->
                    </div>
                    <!-- end invoice -->
                  </div>
                  <!-- end row -->
                </fieldset>
                <!-- end fieldset -->
              </div>
              <!-- end step-3 -->
            </b-card>
          </tab-content>
          <tab-content title="Questions and Remarks">
            <b-card class="mb-3">
              <!-- begin step-3 -->
              <div id="step-4">
                <!-- begin fieldset -->
                <fieldset>
                  <!-- begin row -->
                  <div class="row">
                    <!-- begin col-8 -->
                    <div class="col-md-8 offset-md-2">
                      <legend
                        class="no-border f-w-700 p-b-0 m-t-0 m-b-20 f-s-16 text-inverse"
                      >Please leave Remarks if your have any questions</legend>
                      <p class="step-explain">
                        <br>In this section, please leave messages, if your have any special requirements.
                        <br>We will provide supports or solutions according to your remarks and questions.
                      </p>
                      <br>
                      <!-- begin form-group -->
                      <div class="form-group row m-b-10">
                        <label>Remark</label>
                        <div class="col-md-9">
                          <textarea
                            class="form-control m-b-10"
                            rows="9"
                            placeholder="Please speficy your personal needs or other feedbacks in this field. If your have any questions, please also let us know."
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
      formData: {
        username: this.$user.username,
        flight_num: "",
        luggage_width: "",
        luggage_height: "",
        luggage_image_outside: null,
        luggage_image_inside: null,
        remark: "",
        select_img: [],
        sum_price: ""
      },
      checkedItems: [false, false, false, false, false],
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
        imageSrc: "",
        full: true,
        outputSize: 1,
        outputType: "jpeg",
        realTimePreviewData: {},
        crap: false,
        previewImage: null,
        autoCropWidth: 200,
        autoCropHeight: 200,
        fileName: ""
      },
      // global variables in this vue file
      showForm: false,
      showInstruct: true,
      itemName: "",
      itemPrice: "",
      showOrder: false
    };
  },
  computed: {
    isFormInvalid() {
      return Object.keys(this.fields).some(key => this.fields[key].invalid);
    }
  },
  methods: {
    onCardRefresh(card, done) {
      setTimeout(done, 3000);
    },
    changeFormStatus() {
      this.showForm = true;
    },
    checkProjectValue(e) {
      var value = e.target.value.split("-");
      this.formData.product_id = value[0];
      this.formData.project_id = value[1];
    },
    submitOrderForm() {
      if (!this.isFormInvalid) {
        this.$user.insurance_order_list[
          this.$user.insurance_order_list.length
        ] = this.formData;

        var obj = JSON.stringify(this.formData);
        axios
          .post("/luggage/order/new_travel", obj)
          .then(res => {
            var response = JSON.parse(JSON.stringify(res.data));
            alert(response);
          })
          .catch(function(error) {
            console.log(error);
          });
      } else {
        alert("Please enter valid information in all required fields.");
      }
    },
    startCrop() {
      this.cropImg.crap = true;
      this.$refs.cropper.startCrop();
    },
    stopCrop() {
      this.cropImg.crap = false;
      this.$refs.cropper.stopCrop();
      this.$refs.cropper.clearCrop();
      this.itemName = "";
      this.itemPrice = "";
    },
    previewRealTime(data) {
      this.cropImg.realTimePreviewData = data;
    },
    storeItemImage(type) {
      if (type === "blob") {
        this.$refs.cropper.getCropBlob(data => {
          this.downloadImgData = window.URL.createObjectURL(data);
          this.formData.select_img[this.formData.select_img.length] = {
            imgUrl: this.downloadImgData
          };
        });
      } else {
        this.$refs.cropper.getCropData(data => {
          var img = new Image();
          img.src = data;
          this.formData.select_img[this.formData.select_img.length] = {
            imgUrl: img.src,
            name: this.itemName,
            price: this.itemPrice,
            remark: ""
          };
        });
      }
    },
    convertImg(e, img) {
      var _this = this;
      let reader = new FileReader();
      reader.readAsDataURL(e.target.files[0]);
      reader.onload = function(e) {
        if (img == "in") {
          _this.formData.luggage_image_inside = e.target.result;
        } else if (img == "out") {
          _this.formData.luggage_image_outside = e.target.result;
        } else {
          return;
        }
      };
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
      this.showInstruct = false;
    },
    generateOrder() {
      var sum_price = 0;
      for (var i = 0; i < this.formData.select_img.length; i++) {
        sum_price += Number(this.formData.select_img[i].price);
      }
      this.formData.sum_price = sum_price;
      this.showOrder = true;
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
.img-fluid {
  margin: 10px;
  margin-right: 20px;
}

.instruct-crop {
  margin: 5px;
  margin-bottom: 40px;
  font-size: 15px;
  background-color: #f5e8bf52 !important;
}

.itemUpdateButton {
  margin: 10px;
  margin-left: 30px;
}

.bt-save {
  background-color: rgba(255, 127, 127, 0.274) !important;
}

.bt-update {
  background-color: rgba(127, 255, 206, 0.267) !important;
}

.bt-remark {
  background-color: rgba(127, 178, 255, 0.267) !important;
}

.media {
  background-color: rgba(226, 224, 224, 0.171) !important;
}

input:disabled {
  border: 1px solid #ddd;
  background-color: #ffffffb6;
  color: #000000;
  opacity: 1;
}

.table-responsive {
  margin: 20px !important;
}

.table-invoice {
  font-size: 13px;
}

.step-explain {
  font-size: 15px;
}

.right-button {
  margin-top: 5px;
  margin-left: 85%;
}

.invoice {
  width: 100% !important;
  margin: 20px;
}
</style>
