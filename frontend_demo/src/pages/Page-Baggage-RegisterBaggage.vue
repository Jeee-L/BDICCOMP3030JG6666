<template>
  <div>
    <div class="card card-default">
      <div class="card-header">
        <h3>{{$t('m.register')}}</h3>
        <br>
        <p>
          {{$t('m.register1')}}
          <br>
          {{$t('m.register2')}}
        </p>
      </div>
      <div class="card-body">
        <div id="info" v-show="!showForm">
          <div class="row">
            <div style="text-align:center;">
              <pie-chart
                :data="pieChart.data"
                :options="pieChart.options"
                class="height-sm"
                id="pie"
                style="margin-left: -20px !important"
              ></pie-chart>
              <div class="card card-default noti-chart col-xl-11">
                {{$t('m.pie')}}
                <br>
                <br>
                {{$t('m.pie2')}}
                <br>
                {{$t('m.pie3')}}
                <br>
                <button
                  type="button"
                  class="btn btn-lime"
                  v-on:click="changeFormstate"
                  style="margin-left: 210px; margin-top: 30px; font-size: 14px; padding: 15px"
                >{{$t('m.rbn')}}</button>
              </div>
            </div>
            <div
              class="col-xl-6 card card-default"
              id="inforTable"
              style="padding: 10px !important"
            >
              <div class="row">
                <!-- begin col-3 -->
                <div style="margin-left: 10px; width: 45% !important">
                  <div class="widget widget-stats bg-gradient-blue">
                    <div class="stats-icon stats-icon-lg">
                      <i class="fa fa-archive fa-fw"></i>
                    </div>
                    <div class="stats-content">
                      <div class="stats-title">{{$t('m.tr')}}</div>
                      <br>
                      <div
                        class="stats-number"
                        style="font-size: 30px"
                      >{{$store.state.insurance_time[0]}} {{$t('m.days')}}</div>
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
                      <div class="stats-title">{{$t('m.ib')}}</div>
                      <br>
                      <div
                        class="stats-number"
                        style="font-size: 30px"
                      >$ {{$store.state.insurance_amount[0]}}</div>
                    </div>
                  </div>
                </div>
                <!-- end col-3 -->
              </div>
              <br>
              <br>
              <h6>
                {{$t('m.checkt')}}
                <br>
                <br>
                {{$t('m.table')}}
              </h6>
              <br>
              <br>
              <div class="card card-default">
                <div class="card-header">{{$t('m.brr')}}</div>
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
          :title="$t('m.rb')"
          :subtitle="$t('m.subcom')"
          v-show="showForm"
        >
          <!-- Headers -->
          <tab-content :title="$t('m.tbi')">
            <b-card class="mb-3">
              <!-- begin fieldset -->
              <fieldset>
                <!-- begin row -->
                <div class="row">
                  <!-- begin col-8 -->
                  <div class="col-md-8 offset-md-2">
                    <legend
                      class="no-border f-w-700 p-b-0 m-t-0 m-b-20 f-s-16 text-inverse"
                    >{{$t('m.checki')}}</legend>
                    <!-- begin form-group -->
                    <div class="form-group row m-b-10">
                      <label class="col-md-3 col-form-label text-md-right">
                        {{$t('m.fln')}}
                        <span class="text-danger">*</span>
                      </label>
                      <div class="col-md-6">
                        <input
                          type="text"
                          class="form-control"
                          :placeholder="$t('m.pfn')"
                          :name="$t('m.fln')"
                          v-model="formData.flight_number"
                          v-validate="{ required: true, regex:/^[\dA-Z][A-Z]{1,2}\d{2,4}$/}"
                          v-bind:class="{'is-invalid': errors.has($t('m.fln'))}"
                        >
                        <span style="color: red !important;">{{ errors.first($t('m.fln')) }}</span>
                      </div>
                    </div>
                    <!-- end form-group -->
                    <!-- begin form-group -->
                    <div class="form-group row m-b-10">
                      <label class="col-md-3 col-form-label text-md-right">
                        {{$t('m.bw')}}
                        <span class="text-danger">*</span>
                      </label>
                      <div class="col-md-6">
                        <input
                          type="number"
                          class="form-control"
                          :placeholder="$t('m.pbw')"
                          :name="$t('m.bw')"
                          v-model="formData.luggage_width"
                          v-validate="{ required: true}"
                          v-bind:class="{'is-invalid': errors.has($t('m.bw'))}"
                        >
                        <span style="color: red !important;">{{ errors.first($t('m.bw')) }}</span>
                      </div>
                    </div>
                    <!-- end form-group -->
                    <!-- begin form-group -->
                    <div class="form-group row m-b-10">
                      <label class="col-md-3 col-form-label text-md-right">
                        {{$t('m.bh')}}
                        <span class="text-danger">*</span>
                      </label>
                      <div class="col-md-6">
                        <input
                          type="number"
                          :name="$t('m.bh')"
                          :placeholder="$t('m.pbh')"
                          class="form-control"
                          v-model="formData.luggage_height"
                          v-validate="{ required: true}"
                          v-bind:class="{'is-invalid': errors.has($t('m.bh'))}"
                        >
                        <span style="color: red !important;">{{ errors.first($t('m.bh')) }}</span>
                      </div>
                    </div>
                    <!-- end form-group -->
                    <br>
                    <br>
                    <!-- begin form-group -->
                    <div class="form-group row m-b-10">
                      <label class="col-md-3 col-form-label text-md-right">
                        {{$t('m.boi')}}
                        <span class="text-danger">*</span>
                      </label>
                      <div class="col-md-6">
                        <b-form-group :description="$t('m.dtp')">
                          <b-file
                            @change="convertImg($event, 'out')"
                            accept="image/*"
                            :state="'valid'"
                            :name="$t('m.boi')"
                            v-validate="{ required: true}"
                            v-bind:class="{'is-invalid': errors.has($t('m.boi'))}"
                          >
                            <span style="color: red !important;">{{ errors.first($t('m.boi')) }}</span>
                          </b-file>
                        </b-form-group>
                      </div>
                    </div>
                    <!-- end form-group -->
                    <!-- begin form-group -->
                    <div class="form-group row m-b-10">
                      <label class="col-md-3 col-form-label text-md-right">
                        {{$t('m.bii')}}
                        <span class="text-danger">*</span>
                      </label>
                      <div class="col-md-6">
                        <b-form-group :description="$t('m.dpp')">
                          <b-file
                            @change="convertImg($event, 'in')"
                            accept="image/*"
                            :state="'valid'"
                            :name="$t('m.bii')"
                            v-validate="{ required: true}"
                            v-bind:class="{'is-invalid': errors.has($t('m.bii'))}"
                          >
                            <span style="color: red !important;">{{ errors.first($t('m.bii')) }}</span>
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
          <tab-content :title="$t('m.tup')">
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
                    >{{$t('m.spp')}}</legend>

                    <div class="container-md" style="width: 100% !important">
                      <div class="row">
                        <div class="col-xl-8">
                          <div class="card card-body instruct-crop">
                            <b>{{$t('m.belong')}}</b>
                            <br>
                            <br>
                            {{$t('m.b1')}}
                            <br>
                            {{$t('m.b2')}}
                            <br>
                            {{$t('m.b3')}}
                            <br>
                            {{$t('m.b4')}}
                            <br>
                            {{$t('m.b5')}}
                            <br>
                            {{$t('m.b6')}}
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
                              >
                              {{$t('m.ci')}}
                            </label>
                            <b-btn
                              class="mr-2 mb-2"
                              @click="startCrop"
                              v-if="!cropImg.crap"
                              :disabled="!cropImg.imageSrc"
                            >{{$t('m.sc')}}</b-btn>
                            <b-btn
                              class="mr-2 mb-2"
                              @click="stopCrop"
                              variant="danger"
                              v-else
                              :disabled="!cropImg.imageSrc"
                            >{{$t('m.sc1')}}</b-btn>
                          </div>
                          <br>
                          <br>
                          <div class="btn-group flex-wrap">
                            <b-btn
                              class="mr-2 mb-4"
                              @click="storeItemImage('base64')"
                              :disabled="!cropImg.imageSrc"
                            >{{$t('m.submitit')}}</b-btn>
                          </div>
                        </div>
                        <div class="col-xl-4" v-show="!this.showInstruct">
                          <p class="text-danger">
                            {{$t('m.both')}}
                            <b>{{$t('m.appraisal')}}</b>
                            {{$t('m.a')}}
                            <b>"{{$t('m.submitit')}}"</b>
                            {{$t('m.button')}}.
                          </p>
                          <b-form-group :label="$t('m.lin')">
                            <b-input
                              type="text"
                              name="name"
                              :placeholder="$t('m.pen')"
                              v-model="itemName"
                            />
                          </b-form-group>
                          <b-form-group :label="$t('m.ip')">
                            <b-input
                              type="text"
                              name="price"
                              :placeholder="$t('m.ppa')"
                              v-model="itemPrice"
                            />
                          </b-form-group>
                          <br>
                          <br>
                          <p>{{$t('m.op')}}</p>
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
          <tab-content :title="$t('m.tcii')">
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
                    >{{$t('m.dc')}}</legend>
                    <p style="margin-left: 20px !important" class="step-explain">
                      <br>
                      {{$t('m.list')}}
                      <br>
                      {{$t('m.recheck')}}
                      <br>
                      {{$t('m.finish')}}
                    </p>
                    <!-- START table-responsive-->
                    <div class="table-responsive">
                      <table class="table table-striped table-bordered table-hover card card-body">
                        <thead>
                          <tr>
                            <th>{{$t('m.des')}}</th>
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
                                      <b-form-group :label="$t('m.lin')" style="margin-left: 20px">
                                        <b-input
                                          type="text"
                                          id="itemName"
                                          :name="$t('m.lin')"
                                          v-validate="{ required: true}"
                                          v-bind:class="{'is-invalid': errors.has($t('m.lin'))}"
                                          v-model="items.name"
                                          class="form-control"
                                        />
                                        <span
                                          style="color: red !important;"
                                        >{{ errors.first($t('m.lin')) }}</span>
                                      </b-form-group>
                                      <b-form-group :label="$t('m.ip')" style="margin-left: 20px">
                                        <b-input
                                          type="text"
                                          id="itemPrice"
                                          :name="$t('m.ip')"
                                          v-validate="'required'"
                                          v-bind:class="{'is-invalid': errors.has($t('m.ip'))}"
                                          v-model="items.price"
                                          class="form-control"
                                        />
                                        <span
                                          style="color: red !important;"
                                        >{{ errors.first($t('m.ip')) }}</span>
                                      </b-form-group>
                                      <b-form-group
                                        :label="$t('m.remark')"
                                        style="margin-left: 20px; width: 400px"
                                      >
                                        <b-input
                                          type="text"
                                          id="remark"
                                          :name="$t('m.remark')"
                                          :placeholder="$t('m.plr')"
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
                    >{{$t('m.co')}}</b-button>
                    <!-- begin invoice -->
                    <div class="invoice" v-show="this.showOrder">
                      <div
                        class="invoice-company text-inverse f-w-600"
                        style="font-size: 15px"
                      >{{$t('m.ro')}}</div>
                      <!-- begin invoice-content -->
                      <div class="invoice-content card card-body">
                        <!-- begin table-responsive -->
                        <div class="table-responsive">
                          <table class="table table-invoice">
                            <thead>
                              <tr>
                                <th class="text-left" width="30%">{{$t('m.n')}}</th>
                                <th class="text-left" width="30%">{{$t('m.pa')}}</th>
                                <th class="text-left" width="40%">{{$t('m.rem')}}</th>
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
                            <small>{{$t('m.total1')}}</small>
                            <span
                              class="f-w-600"
                              style="font-size: 20px !important"
                            >$ {{formData.sumPrice}}</span>
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
          <tab-content :title="$t('m.tqr')">
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
                      >{{$t('m.remarks')}}</legend>
                      <p class="step-explain">
                        <br>
                        {{$t('m.message')}}
                        <br>
                        {{$t('m.support')}}
                      </p>
                      <br>
                      <!-- begin form-group -->
                      <div class="form-group row m-b-10">
                        <label>{{$t('m.remark')}}</label>
                        <div class="col-md-9">
                          <textarea
                            class="form-control m-b-10"
                            rows="9"
                            :placeholder="$t('m.psp1')"
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
          <b-btn variant="secondary" slot="prev">{{$t('m.back')}}</b-btn>
          <b-btn variant="secondary" slot="next">{{$t('m.next')}}</b-btn>
          <b-btn variant="info" slot="finish">{{$t('m.submitio')}}</b-btn>
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
        username: this.$store.getters.username,
        flight_number: "",
        luggage_width: "",
        luggage_height: "",
        luggage_image_outside: null,
        luggage_image_inside: null,
        remark: "",
        select_img: [],
        sumPrice: ""
      },
      checkedItems: [false, false, false, false, false],

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
      showForm: this.$store.state.insurance_list == "",
      noOrder: this.$store.state.insurance_list == "",
      showInstruct: true,
      itemName: "",
      itemPrice: "",
      showOrder: false
    };
  },
  created() {
    window.addEventListener("beforeunload", this.handler);
    if (this.$store.state.insurance_list == "") {
      this.swalNotification("warning", "");
      this.$router.push("/baggage/insurance");
    }
    this.requestData();
  },
  // mounted
  computed: {
    isFormInvalid() {
      return Object.keys(this.fields).some(key => this.fields[key].invalid);
    },
    lanChange() {
      return this.$t("m.date_lan") == "en";
    },
    parameters() {
      return [this.$t("m.poid"), this.$t("m.pet"), this.$t("m.pc")];
    },
    pieChart() {
      return {
        data: {
          labels: this.$store.state.insurance_order_labels,
          datasets: [
            {
              data: this.$store.state.insurance_order_prices,
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
      };
    },
    itemsFields() {
      return this.loadDataTable();
    }
  },
  methods: {
    handler: function handler(event) {
      alert("refresh");
      this.requestData();
    },
    loadDataTable() {
      var order_label = this.$store.state.insurance_order_labels;
      var order_date = this.$store.state.insurance_order_dates;
      var order_price = this.$store.state.insurance_order_prices;
      var table_dict = [];

      for (var i = 0; i < order_label.length; i++) {
        table_dict.push({
          isActive: true,
          [this.$t("m.poid")]: order_label[i],
          [this.$t("m.pet")]: order_date[i],
          [this.$t("m.pc")]: order_price[i]
        });
      }

      return table_dict;
    },
    onCardRefresh(card, done) {
      setTimeout(done, 3000);
    },
    changeFormstate() {
      this.showForm = true;
    },
    checkProjectValue(e) {
      var value = e.target.value.split("-");
      this.formData.product_id = value[0];
      this.formData.project_id = value[1];
    },
    submitOrderForm() {
      if (!this.isFormInvalid) {
        var obj = JSON.stringify(this.formData);
        axios
          .post("/luggage/order/new_travel", obj)
          .then(res => {
            var response = JSON.parse(JSON.stringify(res.data));
            if (response.state) {
              if (response.state == "1") {
                this.swalNotification("success", "");
                this.showForm = false;
              } else {
                this.swalNotification(
                  "error",
                  this.showError(response.error_msg)
                );
              }
            }
          })
          .catch(function(error) {
            console.log(error);
          });
      } else {
        alert(this.$t("m.alpe"));
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
        alert(this.$t("m.alfe"));
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
      var sumPrice = 0;
      for (var i = 0; i < this.formData.select_img.length; i++) {
        sumPrice += Number(this.formData.select_img[i].price);
      }
      this.formData.sumPrice = sumPrice;
      this.showOrder = true;
    },
    swalNotification(swalType, error_msg) {
      if (swalType == "success") {
        this.$swal({
          title: this.$t("m.baggage_s_title"),
          text: this.$t("m.baggage_s_text"),
          timer: 2000,
          showConfirmButton: false,
          type: swalType
        }).then(
          setTimeout(() => {
            this.$router.push("/baggage/register");
          }, 2000)
        );
      } else if (swalType == "error") {
        this.$swal({
          title: this.$t("m.baggage_f_title"),
          text: error_msg,
          timer: 2000,
          showConfirmButton: false,
          type: swalType
        }).then();
      } else {
        this.$swal({
          title: this.$t("m.insurance_w_title"),
          text: error_msg,
          timer: 2000,
          showConfirmButton: false,
          type: swalType
        }).then();
      }
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
  margin-top: 30px;
  margin-right: 10px;
  margin-left: 10px;
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

.noti-chart {
  margin: 20px !important;
  font-size: 13px;
  width: 430px;
  font-weight: bold;
}
</style>