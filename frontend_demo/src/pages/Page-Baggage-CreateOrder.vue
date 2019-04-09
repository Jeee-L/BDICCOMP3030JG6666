<template>
  <ContentWrapper>
    <div class="card card-default" style="margin: 30px">
      <div class="card-header">Create Order</div>
      <div class="card-body">
        <form-wizard @on-complete="backLogin" color="#66CDAA">
          <template slot="step" slot-scope="props">
            <!-- By using a custom header markup we can pass html in title attribute -->
            <wizard-step
              :tab="props.tab"
              @click.native="props.navigateToTab(props.index)"
              @keyup.enter.native="props.navigateToTab(props.index)"
              :transition="props.transition"
              :index="props.index"
            >
              <span
                slot="title"
                :class="{'text-danger':props.tab.validationError}"
                v-html="props.tab.title"
              ></span>
            </wizard-step>
          </template>
          <!-- Headers -->
          <tab-content title="<div>FIRST STEP</div><div>Customer Personal Information</div>">
            <b-card class="mb-3">
              <!-- begin fieldset -->
              <fieldset>
                <!-- begin row -->
                <div class="row">
                  <!-- begin col-8 -->
                  <div class="col-md-8 offset-md-2">
                    <legend
                      class="no-border f-w-700 p-b-0 m-t-0 m-b-20 f-s-16 text-inverse"
                    >Please complete personal information for security</legend>
                    <!-- begin form-group -->
                    <div class="form-group row m-b-10">
                      <label class="col-md-3 col-form-label text-md-right">
                        First Name
                        <span class="text-danger">*</span>
                      </label>
                      <div class="col-md-6">
                        <input
                          type="text"
                          class="form-control"
                          placeholder="First Name"
                          name="first name"
                          v-validate="{ required: true, regex:/^[_a-zA-Z0-9\u4E00-\u9FA5]{2,30}$/ }"
                          v-bind:class="{'is-invalid': errors.has('first name')}"
                          v-model="formData.first_name"
                        >
                        <span style="color: red !important;">{{ errors.first('first name') }}</span>
                      </div>
                    </div>
                    <!-- end form-group -->
                    <!-- begin form-group -->
                    <div class="form-group row m-b-10">
                      <label class="col-md-3 col-form-label text-md-right">
                        Last Name
                        <span class="text-danger">*</span>
                      </label>
                      <div class="col-md-6">
                        <input
                          type="text"
                          name="last name"
                          placeholder="Last Name"
                          class="form-control"
                          v-validate="{ required: true, regex:/^[_a-zA-Z0-9\u4E00-\u9FA5]{2,30}$/ }"
                          v-bind:class="{'is-invalid': errors.has('last name')}"
                          v-model="formData.last_name"
                        >
                        <span style="color: red !important;">{{ errors.first('last name') }}</span>
                      </div>
                    </div>
                    <!-- end form-group -->
                    <!-- begin form-group -->
                    <div class="form-group row m-b-10">
                      <label class="col-md-3 col-form-label text-md-right">
                        User Name
                        <span class="text-danger">*</span>
                      </label>
                      <div class="col-md-6">
                        <input
                          type="text"
                          name="user name"
                          placeholder="User Name"
                          class="form-control"
                          v-validate="{ required: true, regex:/^[_a-zA-Z0-9\u4E00-\u9FA5]{2,10}$/ }"
                          v-bind:class="{'is-invalid': errors.has('user name')}"
                          v-model="formData.username"
                        >
                        <span style="color: red !important;">{{ errors.first('user name') }}</span>
                      </div>
                    </div>
                    <!-- end form-group -->
                    <!-- begin form-group -->
                    <div class="form-group row m-b-10">
                      <label class="col-md-3 col-form-label text-md-right">
                        Email
                        <span class="text-danger">*</span>
                      </label>
                      <div class="col-md-6">
                        <input
                          type="text"
                          name="email"
                          placeholder="Email"
                          class="form-control"
                          v-validate="{ required: true, regex:/^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,})$/ }"
                          v-bind:class="{'is-invalid': errors.has('email')}"
                          v-model="formData.email"
                        >
                        <span style="color: red !important;">{{ errors.first('email') }}</span>
                      </div>
                    </div>
                    <!-- end form-group -->
                    <!-- begin form-group -->
                    <div class="form-group row m-b-10">
                      <label
                        class="col-md-3 col-form-label text-md-right"
                        for="inputContact8"
                      >Birthday</label>
                      <div class="col-md-6">
                        <datepicker
                          placeholder="Select Date"
                          :value="formData.birthday"
                          input-class="form-control bg-white"
                        ></datepicker>
                      </div>
                    </div>
                    <!-- end form-group -->
                    <!-- begin form-group -->
                    <div class="form-group row m-b-10">
                      <label class="col-md-3 col-form-label text-md-right">
                        Mobile Phone Number
                        <span class="text-danger">*</span>
                      </label>
                      <div class="col-md-6">
                        <input
                          type="text"
                          name="phone number"
                          placeholder="Mobile Phone Number"
                          class="form-control"
                          v-validate="{ required: true, regex:/^\d{8,9}$/ }"
                          v-bind:class="{'is-invalid': errors.has('phone number')}"
                          v-model="formData.phone_num"
                        >
                        <span style="color: red !important;">{{ errors.first('phone number') }}</span>
                      </div>
                    </div>
                    <!-- end form-group -->
                    <!-- begin form-group -->
                    <div class="form-group row m-b-10">
                      <label class="col-md-3 col-form-label text-md-right">
                        Passport Number
                        <span class="text-danger">*</span>
                      </label>
                      <div class="col-md-6">
                        <input
                          type="text"
                          class="form-control"
                          placeholder="Passport Number"
                          name="passport"
                          v-validate="{ required: false, regex:/^\d{8,9}$/ }"
                          v-bind:class="{'is-invalid': errors.has('passport')}"
                          v-model="formData.passport_num"
                        >
                        <span style="color: red !important;">{{ errors.first('passport') }}</span>
                      </div>
                    </div>
                    <!-- begin form-group -->
                    <div class="form-group row m-b-10">
                      <label class="col-md-3 col-form-label text-md-right">Address</label>
                      <div class="col-md-9">
                        <textarea
                          class="form-control m-b-10"
                          rows="3"
                          placeholder="Address"
                          v-model="formData.address"
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
            </b-card>
          </tab-content>
          <tab-content title="<div>SECOND STEP</div><div>Select Insurance Project</div>">
            <b-card class="mb-3">
              <!-- begin step-2 -->
              <div id="step-2">
                <!-- begin fieldset -->
                <fieldset>
                  <!-- begin row -->
                  <div class="row">
                    <!-- begin col-8 -->
                    <div class="col-md-8 md-offset-2">
                      <legend
                        class="no-border f-w-700 p-b-0 m-t-0 m-b-20 f-s-16 text-inverse"
                      >Please select one proper project (product)</legend>
                      <div class="card b mb-2">
                          <b-collapse v-model="collapse2" id="acc1collapse2">
                            <table
                              class="table m-b-0"
                              style="margin-left: 20px; margin-right: 20px"
                            >
                              <thead>
                                <tr>
                                  <th>#</th>
                                  <th>Product Name</th>
                                  <th>Project Information</th>
                                  <th>Product Description</th>
                                </tr>
                              </thead>
                              <tbody>
                                <tr>
                                  <td>1</td>
                                  <td>
                                    <div>1 Time</div>
                                    <div>
                                      <br>
                                      <button
                                        type="button"
                                        class="btn btn-default m-r-5 m-b-5"
                                        href="javascript:;"
                                        v-b-modal.modalDialog
                                      >Detail</button>
                                    </div>
                                  </td>
                                  <td>
                                    <div class="form-check">
                                      <p>
                                        <input
                                          class="form-check-input"
                                          type="radio"
                                          name="default_radio"
                                          id="defaultRadio"
                                          value
                                          checked
                                        >
                                        <label
                                          class="form-check-label"
                                          for="defaultRadio"
                                        >Project 1 - (18 EUR)</label>
                                      </p>
                                    </div>
                                    <div class="form-check">
                                      <p>
                                        <input
                                          class="form-check-input"
                                          type="radio"
                                          name="default_radio"
                                          id="defaultRadio"
                                          value
                                          checked
                                        >
                                        <label
                                          class="form-check-label"
                                          for="defaultRadio"
                                        >Project 2 - (36 EUR)</label>
                                      </p>
                                    </div>
                                  </td>
                                  <td>
                                    <!-- TODO -->
                                    <p>This product is a single-off travel insurance.</p>
                                  </td>
                                </tr>
                                <tr>
                                  <td>1</td>
                                  <td>
                                    <div>1 Time</div>
                                    <div>
                                      <br>
                                      <button
                                        type="button"
                                        class="btn btn-default m-r-5 m-b-5"
                                        href="javascript:;"
                                        v-b-modal.modalDialog2
                                      >Detail</button>
                                    </div>
                                  </td>
                                  <td>
                                    <div class="form-check">
                                      <p>
                                        <input
                                          class="form-check-input"
                                          type="radio"
                                          name="default_radio"
                                          id="defaultRadio"
                                          value
                                          checked
                                        >
                                        <label
                                          class="form-check-label"
                                          for="defaultRadio"
                                        >Project 1 - (18 EUR)</label>
                                      </p>
                                    </div>
                                    <div class="form-check">
                                      <p>
                                        <input
                                          class="form-check-input"
                                          type="radio"
                                          name="default_radio"
                                          id="defaultRadio"
                                          value
                                          checked
                                        >
                                        <label
                                          class="form-check-label"
                                          for="defaultRadio"
                                        >Project 2 - (36 EUR)</label>
                                      </p>
                                    </div>
                                  </td>
                                  <td>
                                    <!-- TODO -->
                                    <p>This product is a single-off travel insurance.</p>
                                  </td>
                                </tr>
                                <tr>
                                  <td>1</td>
                                  <td>
                                    <div>1 Time</div>
                                    <div>
                                      <br>
                                      <button
                                        type="button"
                                        class="btn btn-default m-r-5 m-b-5"
                                        href="javascript:;"
                                        v-b-modal.modalDialog3
                                      >Detail</button>
                                    </div>
                                  </td>
                                  <td>
                                    <div class="form-check">
                                      <p>
                                        <input
                                          class="form-check-input"
                                          type="radio"
                                          name="default_radio"
                                          id="defaultRadio"
                                          value
                                          checked
                                        >
                                        <label
                                          class="form-check-label"
                                          for="defaultRadio"
                                        >Project 1 - (18 EUR)</label>
                                      </p>
                                    </div>
                                    <div class="form-check">
                                      <p>
                                        <input
                                          class="form-check-input"
                                          type="radio"
                                          name="default_radio"
                                          id="defaultRadio"
                                          value
                                          checked
                                        >
                                        <label
                                          class="form-check-label"
                                          for="defaultRadio"
                                        >Project 2 - (36 EUR)</label>
                                      </p>
                                    </div>
                                  </td>
                                  <td>
                                    <!-- TODO -->
                                    <p>This product is a single-off travel insurance.</p>
                                  </td>
                                </tr>
                                <tr>
                                  <td>1</td>
                                  <td>
                                    <div>1 Time</div>
                                    <div>
                                      <br>
                                      <button
                                        type="button"
                                        class="btn btn-default m-r-5 m-b-5"
                                        href="javascript:;"
                                        v-b-modal.modalDialog4
                                      >Detail</button>
                                    </div>
                                  </td>
                                  <td>
                                    <div class="form-check">
                                      <p>
                                        <input
                                          class="form-check-input"
                                          type="radio"
                                          name="default_radio"
                                          id="defaultRadio"
                                          value
                                          checked
                                        >
                                        <label
                                          class="form-check-label"
                                          for="defaultRadio"
                                        >Project 1 - (18 EUR)</label>
                                      </p>
                                    </div>
                                    <div class="form-check">
                                      <p>
                                        <input
                                          class="form-check-input"
                                          type="radio"
                                          name="default_radio"
                                          id="defaultRadio"
                                          value
                                          checked
                                        >
                                        <label
                                          class="form-check-label"
                                          for="defaultRadio"
                                        >Project 2 - (36 EUR)</label>
                                      </p>
                                    </div>
                                  </td>
                                  <td>
                                    <!-- TODO -->
                                    <p>This product is a single-off travel insurance.</p>
                                  </td>
                                </tr>
                              </tbody>
                            </table>
                            <div class="pt-2 clearfix">
                              <p class="float-right text-sm">
                                <i>Fields marked with (*) are required</i>
                              </p>
                              <div class="float-left">
                                <button
                                  class="btn btn-primary"
                                  type="button"
                                  @click="collapse2 = false; collapse3 = true"
                                >Continue</button>
                              </div>
                            </div>
                          </b-collapse>

                        <!-- beign product detail modal -->
                        <!-- begin product modal 1 -->
                        <b-modal
                          id="modalDialog"
                          cancel-title="Buy Now"
                          cancel-variant="danger"
                          ok-title="Cancel"
                          ok-variant="white"
                          title="1 Time Insurance"
                        >
                          <p>For claimed items without original receipts, payment of loss will be calculated based upon 75% of the Actual Cash Value at the time of loss, not to exceed €250.</p>
                          <br>
                          <table class="table m-b-0">
                            <thead>
                              <tr class="danger">
                                <th>Porject Name</th>
                                <th>Porject 1</th>
                                <th>Project 2</th>
                              </tr>
                            </thead>
                            <tbody>
                              <tr>
                                <td>Total Sum Insured</td>
                                <td>1000 EUR</td>
                                <td>2000 EUR</td>
                              </tr>
                              <tr>
                                <td>Sum Insured Per Time</td>
                                <td>1000 EUR</td>
                                <td>2000 EUR</td>
                              </tr>
                              <tr>
                                <td>Price</td>
                                <td>18 EUR</td>
                                <td>36 EUR</td>
                              </tr>
                            </tbody>
                          </table>
                          <br>
                        </b-modal>
                        <!-- end product modal 1 -->
                        <!-- begin product modal 2 -->
                        <b-modal
                          id="modalDialog2"
                          cancel-title="Buy Now"
                          cancel-variant="warning"
                          ok-title="Cancel"
                          ok-variant="white"
                          title="15 days Insurance"
                        >
                          <p>For claimed items without original receipts, payment of loss will be calculated based upon 75% of the Actual Cash Value at the time of loss, not to exceed €250.</p>
                          <br>
                          <table class="table m-b-0">
                            <thead>
                              <tr class="warning">
                                <th>Porject Name</th>
                                <th>Porject 1</th>
                                <th>Project 2</th>
                                <th>Project 3</th>
                              </tr>
                            </thead>
                            <tbody>
                              <tr>
                                <td>Total Sum Insured</td>
                                <td>2600 EUR</td>
                                <td>4000 EUR</td>
                                <td>8000 EUR</td>
                              </tr>
                              <tr>
                                <td>Sum Insured Per Time</td>
                                <td>1000 EUR</td>
                                <td>2000 EUR</td>
                                <td>4000 EUR</td>
                              </tr>
                              <tr>
                                <td>Price</td>
                                <td>54 EUR</td>
                                <td>72 EUR</td>
                                <td>144 EUR</td>
                              </tr>
                            </tbody>
                          </table>
                          <br>
                        </b-modal>
                        <!-- end product modal 2 -->
                        <!-- begin product modal 3 -->
                        <b-modal
                          id="modalDialog3"
                          cancel-title="Buy Now"
                          cancel-variant="grey"
                          ok-title="Cancel"
                          ok-variant="white"
                          title="30 days Insurance"
                        >
                          <p>For claimed items without original receipts, payment of loss will be calculated based upon 75% of the Actual Cash Value at the time of loss, not to exceed €250.</p>
                          <br>
                          <table class="table m-b-0">
                            <thead>
                              <tr class="active">
                                <th>Porject Name</th>
                                <th>Porject 1</th>
                                <th>Project 2</th>
                                <th>Project 3</th>
                              </tr>
                            </thead>
                            <tbody>
                              <tr>
                                <td>Total Sum Insured</td>
                                <td>2600 EUR</td>
                                <td>4000 EUR</td>
                                <td>8000 EUR</td>
                              </tr>
                              <tr>
                                <td>Sum Insured Per Time</td>
                                <td>1000 EUR</td>
                                <td>2000 EUR</td>
                                <td>4000 EUR</td>
                              </tr>
                              <tr>
                                <td>Price</td>
                                <td>80 EUR</td>
                                <td>150 EUR</td>
                                <td>200 EUR</td>
                              </tr>
                            </tbody>
                          </table>
                          <br>
                        </b-modal>
                        <!-- end product modal 3 -->
                        <!-- begin product modal 4 -->
                        <b-modal
                          id="modalDialog4"
                          cancel-title="Buy Now"
                          cancel-variant="info"
                          ok-title="Cancel"
                          ok-variant="white"
                          title="1 Year Insurance"
                        >
                          <p>For claimed items without original receipts, payment of loss will be calculated based upon 75% of the Actual Cash Value at the time of loss, not to exceed €250.</p>
                          <br>
                          <table class="table m-b-0">
                            <thead>
                              <tr class="info">
                                <th>Porject Name</th>
                                <th>Porject 1</th>
                                <th>Project 2</th>
                                <th>Project 3</th>
                              </tr>
                            </thead>
                            <tbody>
                              <tr>
                                <td>Total Sum Insured</td>
                                <td>2600 EUR</td>
                                <td>4000 EUR</td>
                                <td>8000 EUR</td>
                              </tr>
                              <tr>
                                <td>Sum Insured Per Time</td>
                                <td>1000 EUR</td>
                                <td>2000 EUR</td>
                                <td>4000 EUR</td>
                              </tr>
                              <tr>
                                <td>Price</td>
                                <td>225 EUR</td>
                                <td>350 EUR</td>
                                <td>500 EUR</td>
                              </tr>
                            </tbody>
                          </table>
                          <br>
                        </b-modal>
                        <!-- end product modal 4 -->
                        <!-- end product detail modal -->
                      </div>
                    </div>
                    <!-- end col-8 -->
                  </div>
                  <!-- end row -->
                </fieldset>
                <!-- end fieldset -->
              </div>
              <!-- end step-2 -->
            </b-card>
          </tab-content>
          <tab-content title="<div>THIRD STEP TITLE</div><div>Step subtitle</div>">
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
                      >Select your login username and password</legend>
                      <!-- begin form-group -->
                      <div class="form-group row m-b-10">
                        <label class="col-md-3 col-form-label text-md-right">
                          Username
                          <span class="text-danger">*</span>
                        </label>
                        <div class="col-md-6">
                          <input
                            type="text"
                            name="username"
                            placeholder="johnsmithy"
                            class="form-control"
                            data-parsley-group="step-3"
                            data-parsley-required="true"
                            data-parsley-type="alphanum"
                          >
                        </div>
                      </div>
                      <!-- end form-group -->
                      <!-- begin form-group -->
                      <div class="form-group row m-b-10">
                        <label class="col-md-3 col-form-label text-md-right">
                          Pasword
                          <span class="text-danger">*</span>
                        </label>
                        <div class="col-md-6">
                          <input
                            type="password"
                            name="password"
                            placeholder="Your password"
                            class="form-control"
                            data-parsley-group="step-3"
                            data-parsley-required="true"
                          >
                        </div>
                      </div>
                      <!-- end form-group -->
                      <!-- begin form-group -->
                      <div class="form-group row m-b-10">
                        <label class="col-md-3 col-form-label text-md-right">
                          Confirm Pasword
                          <span class="text-danger">*</span>
                        </label>
                        <div class="col-md-6">
                          <input
                            type="password"
                            name="password2"
                            placeholder="Confirmed password"
                            class="form-control"
                            data-parsley-group="step-3"
                            data-parsley-required="true"
                          >
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
          <b-btn variant="info" slot="finish">Proceed to Login Page</b-btn>
        </form-wizard>
      </div>
    </div>
  </ContentWrapper>
</template>

<script>
import { FormWizard, TabContent, WizardStep } from "vue-form-wizard";
import PageOptions from "../config/PageOptions.vue";

export default {
  data() {
    return {
      formData: {
        first_name: "",
        last_name: "",
        username: "",
        email: "",
        birthday: new Date(),
        phone_num: "",
        passport_num: "",
        address: "",
        product_id: "",
        project_id: "",
        baggage_image_outside: "",
        baggage_image_inside: "",
        baggage_width: "",
        baggage_height: "",
        remark: ""
      }
    };
  },
  components: {
    FormWizard,
    TabContent,
    WizardStep
  },
  methods: {
    backLogin() {
      this.$router.push("/login");
    }
  }
};
</script>

<style src="vue-form-wizard/dist/vue-form-wizard.min.css"></style>
