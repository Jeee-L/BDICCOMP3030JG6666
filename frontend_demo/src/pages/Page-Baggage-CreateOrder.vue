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
          <tab-content title="<div>FIRST STEP TITLE</div><div>Step subtitle</div>">
            <b-card class="mb-3">
              <!-- begin fieldset -->
              <fieldset>
                <!-- begin row -->
                <div class="row">
                  <!-- begin col-8 -->
                  <div class="col-md-8 offset-md-2">
                    <legend
                      class="no-border f-w-700 p-b-0 m-t-0 m-b-20 f-s-16 text-inverse"
                    >Customer Personal Information</legend>
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
                          v-validate="{ required: true, regex:/^[_a-zA-Z0-9\u4E00-\u9FA5]{2,10}$/ }"
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
                          v-validate="{ required: true, regex:/^[_a-zA-Z0-9\u4E00-\u9FA5]{2,10}$/ }"
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
                      <div class="col-md-8">
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
                    <label class="control-label">Passport Number</label>
                    <div class="row m-b-15">
                      <div class="col-md-12">
                        <input
                          type="text"
                          class="form-control"
                          placeholder="Passport Number"
                          name="passport"
                          v-validate="{ required: false, regex:/^1[34578]\d{9}$/ }"
                          v-bind:class="{'is-invalid': errors.has('passport')}"
                          v-model="formData.passport_num"
                        >
                        <span style="color: red !important;">{{ errors.first('passport') }}</span>
                      </div>
                    </div>
                    <!-- begin form-group -->
                    <div class="form-group row m-b-10">
                      <label class="col-md-3 col-form-label text-md-right">
                        IC No
                        <span class="text-danger">*</span>
                      </label>
                      <div class="col-md-6">
                        <input
                          type="text"
                          name="ic"
                          placeholder
                          class="form-control"
                          data-parsley-group="step-1"
                          data-parsley-required="true"
                        >
                      </div>
                    </div>
                    <!-- end form-group -->
                    <!-- begin form-group -->
                    <div class="form-group row m-b-10">
                      <label class="col-md-3 col-form-label text-md-right">Address</label>
                      <div class="col-md-9">
                        <input
                          type="text"
                          name="address1"
                          placeholder="Address 1"
                          class="form-control m-b-10"
                        >
                        <input
                          type="text"
                          name="address2"
                          placeholder="Address 2"
                          class="form-control"
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
            </b-card>
          </tab-content>
          <tab-content title="<div>SECOND STEP TITLE</div><div>Step subtitle</div>">
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
                      >You contact info, so that we can easily reach you</legend>
                      <!-- begin form-group -->
                      <div class="form-group row m-b-10">
                        <label class="col-md-3 col-form-label text-md-right">
                          Phone Number
                          <span class="text-danger">*</span>
                        </label>
                        <div class="col-md-6">
                          <input
                            type="number"
                            name="phone"
                            placeholder="123-456-7890"
                            data-parsley-group="step-2"
                            data-parsley-required="true"
                            data-parsley-type="number"
                            class="form-control"
                          >
                        </div>
                      </div>
                      <!-- end form-group -->
                      <!-- begin form-group -->
                      <div class="form-group row m-b-10">
                        <label class="col-md-3 col-form-label text-md-right">
                          Email Address
                          <span class="text-danger">*</span>
                        </label>
                        <div class="col-md-6">
                          <input
                            type="email"
                            name="email"
                            placeholder="someone@example.com"
                            class="form-control"
                            data-parsley-group="step-2"
                            data-parsley-required="true"
                            data-parsley-type="email"
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
