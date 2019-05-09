<template>
  <div>
    <div class="card card-default">
      <div class="card-header">
        <h3>{{$t('m.create')}}</h3>
      </div>
      <div class="card-body">
        <div id="pds" v-show="!showForm">
          <p class="text-danger">{{$t('m.please')}}</p>
          <div style="background-color: rgba(213, 223, 219, 0.295) !important; padding: 50px">
            <h4 style="text-align: center !important;">{{$t('m.pds')}}</h4>
            <br>
            <br>
            <h5>{{$t('m.gp')}}</h5>
            <div>
              {{$t('m.gp1')}}
              <br>
              <p style="text-indent: 2em">{{$t('m.gp2')}}</p>
            </div>
            <h5>{{$t('m.is')}}</h5>
            <div>
              {{$t('m.is2')}}
              <br>
              <br>
              {{$t('m.is3')}}
              <br>
              <br>
              {{$t('m.is4')}}
              <br>
              {{$t('m.is41')}}
              <br>
              {{$t('m.is42')}}
              <br>
              {{$t('m.is43')}}
            </div>
            <br>
            <h5>{{$t('m.il')}}</h5>
            <div>
              {{$t('m.il5')}}
              <br>
              <p style="text-indent: 2em">{{$t('m.il51')}}</p>
              {{$t('m.il6')}}
            </div>
            <br>
            <h5>{{$t('m.disclaimer')}}</h5>
            <div>
              {{$t('m.d7')}}
              <br>
              {{$t('m.d71')}}
              <br>
              {{$t('m.d72')}}
              <br>
              {{$t('m.d73')}}
              <br>
              {{$t('m.d74')}}
              <br>
              {{$t('m.d75')}}
              <br>
              {{$t('m.d76')}}
            </div>
            <br>
            <h5>{{$t('m.ctc')}}</h5>
            <div>{{$t('m.ctc8')}}</div>
            <br>
            <h5>{{$t('m.oi')}}</h5>
            <div>
              {{$t('m.oi9')}}
              <br>
              <br>
              {{$t('m.oi10')}}
              <br>
              <br>
              {{$t('m.oi11')}}
            </div>
            <br>
            <h5>{{$t('m.oai')}}</h5>
            <div>
              {{$t('m.oai12')}}
              <br>
              <br>
              {{$t('m.oai13')}}
              <br>
              <br>
              {{$t('m.oai14')}}
              <br>
            </div>
            <br>
            <h5>{{$t('m.compensation')}}</h5>
            <div>{{$t('m.c15')}}</div>
            <br>
            <br>
            <p
              style="font-size: 15px"
              class="text-danger"
              v-show="!buyInsurance"
            >{{this.$t('m.allow')}}</p>
            <button
              type="button"
              class="btn btn-lime"
              v-on:click="changeFormStatus"
              :disabled="!buyInsurance"
            >{{$t('m.iaccept')}}</button>
          </div>
        </div>

        <form-wizard
          @on-complete="submitOrderForm"
          color="#66CDAA"
          shape="circle"
          :title="$t('m.osp1')"
          :subtitle="$t('m.sub')"
          v-show="showForm"
        >
          <!-- Headers -->
          <tab-content :title="$t('m.tcpi')">
            <b-card class="mb-3" style="background-color: rgba(178, 250, 228, 0.151) !important;">
              <!-- begin fieldset -->
              <fieldset>
                <!-- begin row -->
                <div class="row">
                  <!-- begin col-8 -->
                  <div class="col-md-8 offset-md-2">
                    <legend
                      class="no-border f-w-700 p-b-0 m-t-0 m-b-20 f-s-16 text-inverse"
                    >{{$t('m.complete')}}</legend>
                    <!-- begin form-group -->
                    <div class="form-group row m-b-10">
                      <label class="col-md-3 col-form-label text-md-right">
                        {{$t('m.fn')}}
                        <span class="text-danger">*</span>
                      </label>
                      <div class="col-md-6">
                        <input
                          type="text"
                          class="form-control"
                          :placeholder="$t('m.fn')"
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
                        {{$t('m.ln')}}
                        <span class="text-danger">*</span>
                      </label>
                      <div class="col-md-6">
                        <input
                          type="text"
                          name="last name"
                          :placeholder="$t('m.ln')"
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
                        {{$t('m.email')}}
                        <span class="text-danger">*</span>
                      </label>
                      <div class="col-md-6">
                        <input
                          type="text"
                          name="email"
                          :placeholder="$t('m.email')"
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
                      >{{$t('m.birthday')}}</label>
                      <div class="col-md-6">
                        <datepicker
                          :language="date_lan"
                          :placeholder="$t('m.psd')"
                          v-model="formData.birthday"
                          input-class="form-control bg-white"
                          format="yyyy-MM-dd"
                        ></datepicker>
                      </div>
                    </div>
                    <!-- end form-group -->
                    <!-- begin form-group -->
                    <div class="form-group row m-b-10">
                      <label class="col-md-3 col-form-label text-md-right">
                        {{$t('m.mobile')}}
                        <span class="text-danger">*</span>
                      </label>
                      <div class="col-md-6">
                        <input
                          type="text"
                          name="phone number"
                          :placeholder="$t('m.mobile')"
                          class="form-control"
                          v-validate="{ required: true, regex:/^1[34578]\d{9}$|^\d{8,9}$/ }"
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
                        {{$t('m.passport')}}
                        <span class="text-danger">*</span>
                      </label>
                      <div class="col-md-6">
                        <input
                          type="text"
                          class="form-control"
                          :placeholder="$t('m.passport')"
                          name="passport"
                          v-validate="{ required: false, regex:/^(1[45]|P|E[A-Z])\d{7}$|^[GDE](\d{8})$|^S\d{7,8}$|^[HM]\d{10}$/ }"
                          v-bind:class="{'is-invalid': errors.has('passport')}"
                          v-model="formData.passport_num"
                        >
                        <span style="color: red !important;">{{ errors.first('passport') }}</span>
                      </div>
                    </div>
                    <!-- begin form-group -->
                    <div class="form-group row m-b-10">
                      <label class="col-md-3 col-form-label text-md-right">{{$t('m.address')}}</label>
                      <div class="col-md-9">
                        <textarea
                          class="form-control m-b-10"
                          rows="3"
                          :placeholder="$t('m.address')"
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
          <tab-content :title="$t('m.tsip')">
            <b-card class="mb-3" style="background-color: rgba(178, 250, 228, 0.068) !important;">
              <!-- begin step-2 -->
              <div id="step-2">
                <!-- begin fieldset -->
                <fieldset>
                  <!-- begin row -->
                  <div class="row">
                    <!-- begin col-8 -->
                    <legend
                      class="no-border f-w-700 p-b-0 m-t-0 m-b-20 f-s-16 text-inverse"
                    >{{$t('m.select')}}</legend>
                    <table class="table m-b-0">
                      <thead>
                        <tr>
                          <th>#</th>
                          <th>{{$t('m.pn')}}</th>
                          <th>{{$t('m.pi')}}</th>
                          <th>{{$t('m.pd')}}</th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr>
                          <td>1</td>
                          <td>
                            <div>{{$t('m.pn1')}}</div>
                            <div>
                              <br>
                              <button
                                type="button"
                                class="btn btn-default m-r-5 m-b-5"
                                href="javascript:;"
                                v-b-modal.modalDialog
                              >{{$t('m.detail')}}</button>
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
                                  value="1-1-90"
                                  v-on:click="checkProjectValue"
                                >
                                <label class="form-check-label" for="defaultRadio">{{$t('m.p1')}}</label>
                              </p>
                            </div>
                            <div class="form-check">
                              <p>
                                <input
                                  class="form-check-input"
                                  type="radio"
                                  name="default_radio"
                                  id="defaultRadio"
                                  value="1-2-180"
                                  v-on:click="checkProjectValue"
                                >
                                <label class="form-check-label" for="defaultRadio">{{$t('m.p2')}}</label>
                              </p>
                            </div>
                          </td>
                          <td>
                            <p>
                              {{$t('m.pd1')}}
                              <br>
                              <br>
                              {{$t('m.pd12')}}
                              <br>
                              {{$t('m.pd13')}}
                              <br>
                              {{$t('m.pd14')}}
                            </p>
                          </td>
                        </tr>
                        <tr>
                          <td>2</td>
                          <td>
                            <div>{{$t('m.pn2')}}</div>
                            <div>
                              <br>
                              <button
                                type="button"
                                class="btn btn-default m-r-5 m-b-5"
                                href="javascript:;"
                                v-b-modal.modalDialog2
                              >{{$t('m.detail')}}</button>
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
                                  value="2-1-270"
                                  v-on:click="checkProjectValue"
                                >
                                <label class="form-check-label" for="defaultRadio">{{$t('m.p3')}}</label>
                              </p>
                            </div>
                            <div class="form-check">
                              <p>
                                <input
                                  class="form-check-input"
                                  type="radio"
                                  name="default_radio"
                                  id="defaultRadio"
                                  value="2-2-360"
                                  v-on:click="checkProjectValue"
                                >
                                <label class="form-check-label" for="defaultRadio">{{$t('m.p4')}}</label>
                              </p>
                            </div>
                            <div class="form-check">
                              <p>
                                <input
                                  class="form-check-input"
                                  type="radio"
                                  name="default_radio"
                                  id="defaultRadio"
                                  value="2-3-700"
                                  v-on:click="checkProjectValue"
                                >
                                <label class="form-check-label" for="defaultRadio">{{$t('m.p5')}}</label>
                              </p>
                            </div>
                          </td>
                          <td>
                            <!-- TODO -->
                            <p>
                              {{$t('m.pd21')}}
                              <br>
                              <br>
                              {{$t('m.pd22')}}
                              <br>
                              {{$t('m.pd23')}}
                              <br>
                              {{$t('m.pd24')}}
                            </p>
                          </td>
                        </tr>
                        <tr>
                          <td>3</td>
                          <td>
                            <div>{{$t('m.pn3')}}</div>
                            <div>
                              <br>
                              <button
                                type="button"
                                class="btn btn-default m-r-5 m-b-5"
                                href="javascript:;"
                                v-b-modal.modalDialog3
                              >{{$t('m.detail')}}</button>
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
                                  value="3-1-400"
                                  v-on:click="checkProjectValue"
                                >
                                <label class="form-check-label" for="defaultRadio">{{$t('m.p6')}}</label>
                              </p>
                            </div>
                            <div class="form-check">
                              <p>
                                <input
                                  class="form-check-input"
                                  type="radio"
                                  name="default_radio"
                                  id="defaultRadio"
                                  value="3-2-700"
                                  v-on:click="checkProjectValue"
                                >
                                <label class="form-check-label" for="defaultRadio">{{$t('m.p7')}}</label>
                              </p>
                            </div>
                            <div class="form-check">
                              <p>
                                <input
                                  class="form-check-input"
                                  type="radio"
                                  name="default_radio"
                                  id="defaultRadio"
                                  value="3-3-1000"
                                  v-on:click="checkProjectValue"
                                >
                                <label class="form-check-label" for="defaultRadio">{{$t('m.p8')}}</label>
                              </p>
                            </div>
                          </td>
                          <td>
                            <!-- TODO -->
                            <p>
                              {{$t('m.pd31')}}
                              <br>
                              <br>
                              {{$t('m.pd32')}}
                              <br>
                              {{$t('m.pd33')}}
                              <br>
                              {{$t('m.pd34')}}
                            </p>
                          </td>
                        </tr>
                        <tr>
                          <td>4</td>
                          <td>
                            <div>{{$t('m.pn4')}}</div>
                            <div>
                              <br>
                              <button
                                type="button"
                                class="btn btn-default m-r-5 m-b-5"
                                href="javascript:;"
                                v-b-modal.modalDialog4
                              >{{$t('m.detail')}}</button>
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
                                  value="4-1-1100"
                                  v-on:click="checkProjectValue"
                                >
                                <label class="form-check-label" for="defaultRadio">{{$t('m.p9')}}</label>
                              </p>
                            </div>
                            <div class="form-check">
                              <p>
                                <input
                                  class="form-check-input"
                                  type="radio"
                                  name="default_radio"
                                  id="defaultRadio"
                                  value="4-2-1500"
                                  v-on:click="checkProjectValue"
                                >
                                <label class="form-check-label" for="defaultRadio">{{$t('m.p10')}}</label>
                              </p>
                            </div>
                            <div class="form-check">
                              <p>
                                <input
                                  class="form-check-input"
                                  type="radio"
                                  name="default_radio"
                                  id="defaultRadio"
                                  value="4-3-2000"
                                  v-on:click="checkProjectValue"
                                >
                                <label class="form-check-label" for="defaultRadio">{{$t('m.p11')}}</label>
                              </p>
                            </div>
                          </td>
                          <td>
                            <!-- TODO -->
                            <p>
                              {{$t('m.pd41')}}
                              <br>
                              <br>
                              {{$t('m.pd42')}}
                              <br>
                              {{$t('m.pd43')}}
                              <br>
                              {{$t('m.pd44')}}
                            </p>
                          </td>
                        </tr>
                      </tbody>
                    </table>

                    <!-- beign product detail modal -->
                    <!-- begin product modal 1 -->
                    <b-modal
                      id="modalDialog"
                      :cancel-title="$t('m.tbn')"
                      cancel-variant="danger"
                      :ok-title="$t('m.tcancel')"
                      ok-variant="white"
                      :title="$t('m.tt1')"
                    >
                      <p>{{$t('m.for')}}</p>
                      <br>
                      <table class="table m-b-0">
                        <thead>
                          <tr class="danger">
                            <th>{{$t('m.project')}}</th>
                            <th>{{$t('m.project1')}}</th>
                            <th>{{$t('m.project2')}}</th>
                          </tr>
                        </thead>
                        <tbody>
                          <tr>
                            <td>{{$t('m.tsi')}}</td>
                            <td>$1000</td>
                            <td>$2000</td>
                          </tr>
                          <tr>
                            <td>{{$t('m.sipt')}}</td>
                            <td>$1000</td>
                            <td>$2000</td>
                          </tr>
                          <tr>
                            <td>{{$t('m.price')}}</td>
                            <td>$90</td>
                            <td>$180</td>
                          </tr>
                        </tbody>
                      </table>
                      <br>
                    </b-modal>
                    <!-- end product modal 1 -->
                    <!-- begin product modal 2 -->
                    <b-modal
                      id="modalDialog2"
                      :cancel-title="$t('m.tbn')"
                      cancel-variant="warning"
                      :ok-title="$t('m.tcancel')"
                      ok-variant="white"
                      :title="$t('m.tt2')"
                    >
                      <p>{{$t('m.for')}}</p>
                      <br>
                      <table class="table m-b-0">
                        <thead>
                          <tr class="warning">
                            <th>{{$t('m.project')}}</th>
                            <th>{{$t('m.project1')}}</th>
                            <th>{{$t('m.project2')}}</th>
                            <th>{{$t('m.project3')}}</th>
                          </tr>
                        </thead>
                        <tbody>
                          <tr>
                            <td>{{$t('m.tsi')}}</td>
                            <td>$2600</td>
                            <td>$4000</td>
                            <td>$8000</td>
                          </tr>
                          <tr>
                            <td>{{$t('m.sipt')}}</td>
                            <td>$1000</td>
                            <td>$2000</td>
                            <td>$4000</td>
                          </tr>
                          <tr>
                            <td>{{$t('m.price')}}</td>
                            <td>$270</td>
                            <td>$360</td>
                            <td>$700</td>
                          </tr>
                        </tbody>
                      </table>
                      <br>
                    </b-modal>
                    <!-- end product modal 2 -->
                    <!-- begin product modal 3 -->
                    <b-modal
                      id="modalDialog3"
                      :cancel-title="$t('m.tbn')"
                      cancel-variant="grey"
                      :ok-title="$t('m.tcancel')"
                      ok-variant="white"
                      :title="$t('m.tt3')"
                    >
                      <p>{{$t('m.for')}}</p>
                      <br>
                      <table class="table m-b-0">
                        <thead>
                          <tr class="active">
                            <th>{{$t('m.project')}}</th>
                            <th>{{$t('m.project1')}}</th>
                            <th>{{$t('m.project2')}}</th>
                            <th>{{$t('m.project3')}}</th>
                          </tr>
                        </thead>
                        <tbody>
                          <tr>
                            <td>{{$t('m.tsi')}}</td>
                            <td>$2600</td>
                            <td>$4000</td>
                            <td>$8000</td>
                          </tr>
                          <tr>
                            <td>{{$t('m.sipt')}}</td>
                            <td>$1000</td>
                            <td>$2000</td>
                            <td>$4000</td>
                          </tr>
                          <tr>
                            <td>{{$t('m.price')}}</td>
                            <td>$400</td>
                            <td>$700</td>
                            <td>$1000</td>
                          </tr>
                        </tbody>
                      </table>
                      <br>
                    </b-modal>
                    <!-- end product modal 3 -->
                    <!-- begin product modal 4 -->
                    <b-modal
                      id="modalDialog4"
                      :cancel-title="$t('m.tbn')"
                      cancel-variant="info"
                      :ok-title="$t('m.tcancel')"
                      ok-variant="white"
                      :title="$t('m.tt4')"
                    >
                      <p>{{$t('m.for')}}</p>
                      <br>
                      <table class="table m-b-0">
                        <thead>
                          <tr class="info">
                            <th>{{$t('m.project')}}</th>
                            <th>{{$t('m.project1')}}</th>
                            <th>{{$t('m.project2')}}</th>
                            <th>{{$t('m.project3')}}</th>
                          </tr>
                        </thead>
                        <tbody>
                          <tr>
                            <td>{{$t('m.tsi')}}</td>
                            <td>$2600</td>
                            <td>$4000</td>
                            <td>$8000</td>
                          </tr>
                          <tr>
                            <td>{{$t('m.sipt')}}</td>
                            <td>$1000</td>
                            <td>$2000</td>
                            <td>$4000</td>
                          </tr>
                          <tr>
                            <td>{{$t('m.price')}}</td>
                            <td>$1100</td>
                            <td>$1500</td>
                            <td>$2000</td>
                          </tr>
                        </tbody>
                      </table>
                      <br>
                    </b-modal>
                    <!-- end product modal 4 -->
                    <!-- end product detail modal -->
                    <!-- end col-8 -->
                  </div>
                  <!-- end row -->
                </fieldset>
                <!-- end fieldset -->
              </div>
              <!-- end step-2 -->
            </b-card>
          </tab-content>
          <tab-content :title="$t('m.trq')">
            <b-card class="mb-3" style="background-color: rgba(178, 250, 228, 0.151) !important;">
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
                      >{{$t('m.remarks')}}</legend>
                      <p>
                        <br>
                        {{$t('m.message')}}
                        <br>
                        {{$t('m.support')}}
                      </p>
                      <br>
                      <!-- begin form-group -->
                      <div class="form-group row m-b-10">
                        <label class="col-md-3 col-form-label text-md-right">{{$t('m.remark')}}</label>
                        <div class="col-md-6">
                          <textarea
                            class="form-control m-b-10"
                            rows="12"
                            :placeholder="$t('m.psp')"
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
import { FormWizard, TabContent, WizardStep } from "vue-form-wizard";
import PageOptions from "../config/PageOptions.vue";
import { en, zh } from "vuejs-datepicker/dist/locale";
import axios from "axios";

export default {
  data() {
    return {
      showForm: false,
      formData: {
        first_name: this.$store.getters.first_name,
        last_name: this.$store.getters.last_name,
        username: this.$store.getters.username,
        email: this.$store.getters.email,
        birthday: this.$store.getters.birthday,
        phone_num: this.$store.getters.phone_num,
        passport_num: this.$store.getters.passport_num,
        address: this.$store.getters.address,
        product_id: "",
        project_id: "",
        amount_of_money: "",
        remark: ""
      }
    };
  },
  components: {
    FormWizard,
    TabContent,
    WizardStep
  },
  computed: {
    isFormInvalid() {
      return Object.keys(this.fields).some(key => this.fields[key].invalid);
    },
    buyInsurance() {
      return this.$store.getters.insurance_list == "";
    },
    date_lan() {
      return this.$t("m.date_lan") == "en" ? en : zh;
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
      this.formData.amount_of_money = value[2];
    },
    submitOrderForm() {
      var today = new Date().toISOString().substr(0, 10);
      if (this.formData.birthday == today) {
        this.formData.birthday = new Date("1000-01-01")
          .toISOString()
          .substr(0, 10);
      }

      if (!this.isFormInvalid && this.formData.project_id != "") {
        this.$store.commit("handleCustomerInfo", this.formData);
        var obj = JSON.stringify(this.formData);
        axios
          .post("/luggage/order/create", obj)
          .then(res => {
            var response = JSON.parse(JSON.stringify(res.data));
            if (response.state) {
              if (response.state == "1") {
                this.swalNotification("success", "");
                this.$store.commit("handleInsurance", response.insurance_id);
              } else {
                this.swalNotification("error", response.error_msg);
              }
            }
          })
          .catch(function(error) {
            console.log(error);
          });
      } else if (!this.isFormInvalid && this.formData.project_id != "") {
        alert(this.$t("m.alop"));
      } else {
        alert(this.$t("m.alpe"));
      }
    },
    swalNotification(swalType, error_msg) {
      if (swalType == "success") {
        this.$swal({
          title: this.$t("m.insurance_s_title"),
          text: this.$t("m.insurance_s_text"),
          timer: 2000,
          showConfirmButton: false,
          type: swalType
        }).then(
          setTimeout(() => {
            this.$router.push("/baggage/insurance");
          }, 2000)
        );
      } else {
        this.$swal({
          title: this.$t("m.insurance_f_title"),
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

<style src="vue-form-wizard/dist/vue-form-wizard.min.css">
#step-2 {
  margin: 0 auto !important;
  width: 100% !important;
}

p {
  font-size: 20px;
}

table {
  margin: 10px !important;
}

.field-form {
  background-color: rgba(213, 223, 219, 0.295) !important;
}

.is-invalid {
  background-color: #facccc7e !important;
}

.is-valid {
  background-color: #e1fcc47e !important;
}
</style>
