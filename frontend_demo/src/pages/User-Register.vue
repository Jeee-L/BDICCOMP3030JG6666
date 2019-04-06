<template>
  <ContentWrapper>
    <div class="card card-default" style="margin: 30px">
      <div class="card-header">Classic</div>
      <div class="card-body">
        <form-wizard  @on-complete="backLogin" color="#66CDAA">
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
                    >Personal info about yourself</legend>
                    <!-- begin form-group -->
                    <div class="form-group row m-b-10">
                      <label class="col-md-3 col-form-label text-md-right">
                        First Name
                        <span class="text-danger">*</span>
                      </label>
                      <div class="col-md-6">
                        <input
                          type="text"
                          name="firstname"
                          placeholder="John"
                          data-parsley-group="step-1"
                          data-parsley-required="true"
                          class="form-control"
                        >
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
                          name="lastname"
                          placeholder="Smith"
                          data-parsley-group="step-1"
                          data-parsley-required="true"
                          class="form-control"
                        >
                      </div>
                    </div>
                    <!-- end form-group -->
                    <!-- begin form-group -->
                    <div class="form-group row m-b-10">
                      <label class="col-md-3 col-form-label text-md-right">
                        Date of Birth
                        <span class="text-danger">&nbsp;</span>
                      </label>
                      <div class="col-md-6">
                        <div class="row row-space-6">
                          <div class="col-4">
                            <select class="form-control" name="year">
                              <option>-- Year --</option>
                            </select>
                          </div>
                          <div class="col-4">
                            <select class="form-control" name="month">
                              <option>-- Month --</option>
                            </select>
                          </div>
                          <div class="col-4">
                            <select class="form-control" name="day">
                              <option>-- Day --</option>
                            </select>
                          </div>
                        </div>
                      </div>
                    </div>
                    <!-- end form-group -->
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
  components: {
    FormWizard,
    TabContent,
    WizardStep
  },
  created() {
    PageOptions.pageEmpty = true;
  },
  beforeRouteLeave(to, from, next) {
    PageOptions.pageEmpty = false;
    next();
  },
  methods: {
    backLogin() {
        this.$router.push("/login");
    }
  }
};
</script>

<style src="vue-form-wizard/dist/vue-form-wizard.min.css"></style>
