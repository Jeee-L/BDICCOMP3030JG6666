<template>
  <div>
    <div class="card card-default" style="margin: 30px">
      <div class="card-header">
        <h3>Create Insurance Order with Humanized Choices</h3>
      </div>
      <div class="card-body">
        <div id="pds" v-show="!showForm">
          <p
            class="text-danger"
          >* Please accept terms and condistions listed as follows, before creating insurance orders.</p>
          <div style="background-color: rgba(213, 223, 219, 0.295) !important; padding: 50px">
            <h4 style="text-align: center !important;">Product Disclosure Statement</h4>
            <br>
            <br>
            <h5>General Principle</h5>
            <div>
              1. This insurance contract is made up of product disclosure statement, insurance
              policies, insurance certificates and endorsements. All provisions relating to this insurance
              contract shall be in writing.
              <br>
              <p style="text-indent: 2em">
                Any customer who holds a valid international air ticket between Ireland and China
                can serve as the applicant or the insured.
              </p>
            </div>
            <h5>Insurance Subject</h5>
            <div>
              2. During the international air transport, the baggage consigned by the passenger
              to the carrier in conformity with the requirements of air transport shall be the subject of this
              insurance contract.
              <br>
              <br>3. During the international air passenger transport, the baggage carried by the
              passenger and placed in the plane luggage compartment or other positions in the closed
              cabin in accordance with the requirements of the airline carrier shall be the subject of this
              insurance contract upon the special agreement between the applicant and the insurer and
              the corresponding premium shall be paid separately.
              <br>
              <br>4. The following luggages are not the subject of this insurance contract:
              <br>（1）Securities such as currency, cheque, etc.
              <br>（2） Dangerous goods, glass and ceramics, jewelry, diamonds, artworks, documents, animals, plants and other objects that are not easy to identify the value.
              <br>（3）Data recorded on disk, memory card, tape, or other similar device.
            </div>
            <br>
            <h5>Insurance Liability</h5>
            <div>
              5. During the period of insurance, the insurer shall be liable for the loss of the
              insurance subject due to the following causes:
              <br>
              <p style="text-indent: 2em">
                The insurance subject is abandoned in transit due to lightning, fire, explosion, or bad
                weather or other accidents, and all or part of the loss caused by collision, capsize, falling
                or missing accident or other external causes.
              </p>6. After the occurrence of the insured event, the insurer shall also be liable for
              the necessary and reasonable expenses paid by the insured to prevent or reduce the loss
              of the insurance subject in accordance with the provisions of this insurance contract.
            </div>
            <br>
            <h5>Disclaimer</h5>
            <div>
              7. The insurer shall not be liable for any loss or expense of the insurance subject
              caused by:
              <br>（1）Nuclear radiation, nuclear explosion, nuclear pollution, radioactive
              pollution, air pollution, land pollution and other kinds of pollution;
              <br>（2）Administrative or judicial acts;
              <br>（3） Wars, hostile acts, military acts, armed conflicts, strikes, riots and
              terrorist activities;
              <br>（4） Intentional, gross negligence or criminal acts of the applicant, the
              insured and their representatives;
              <br>（5） Natural wear and tear, inherent defect, improper packing, sound outer
              packing but short inner packing of the insurance subject;
              <br>（6）Baggage not conforming to the standards or regulations of air transport
              airports or airlines, or taken on board without the permission of air transport airports or
              airlines.
            </div>
            <br>
            <h5>Commencement and Termination of Cover</h5>
            <div>
              8. The period from the commencement to termination of the insurance shall
              commence when the insurance subject is received by the carrier and the policy or
              certificate of insurance is issued by the insurer, and shall terminate when the insured
              leaves the means of transport and receives the baggage from the carrier. If the insured
              fails to take delivery of the insurance subject in time, the termination period of the
              insurance liability shall be extended to no more than 24 hours after the insured leaves the
              means of transport.
            </div>
            <br>
            <h5>Obligation of Insurer</h5>
            <div>
              9. After the conclusion of this insurance contract, the insurer shall issue the
              insurance policy or other insurance certificates to the applicant in time.
              <br>
              <br>10. After the occurrence of an insured event, the insurer shall inform the applicant
              and the insured in a timely manner to supplement the documents and documents provided
              by the applicant and the insured if they are incomplete.
              <br>
              <br>11. After receiving the indemnity claim of the insured, the insurer shall examine
              and verify whether it is an insurance liability in time and inform the insured of the result of
              the examination and verification.
            </div>
            <br>
            <h5>Obligation of the Applicant and the Insured</h5>
            <div>
              12. The applicant should fulfill the obligation that informs according to the facts,
              answer the inquiry that the insurer puts forward to the concerned circumstance of
              insurance subject or the insured according to the facts, fill in application form according to
              the facts.
              <br>
              <br>13. When an insured accident occurs, the insured shall make every effort to
              take necessary measures to prevent or reduce the loss. After knowing the insurance
              accident happened, the applicant and the insured ought to inform the insurer in time.
              <br>
              <br>14. When the insurer exercises the right of indemnity by subrogation against the
              responsible party, the insured shall provide the insurer with the necessary documents and
              the relevant information.
              <br>
            </div>
            <br>
            <h5>Compensation</h5>
            <div>
              15. When the insurance subject suffers a loss within the scope of insurance
              liability, the insurer shall calculate the indemnity according to the actual loss within the
              insured amount, but the indemnity shall not exceed the maximum insured amount.
            </div>
            <br>
            <br>
            <button
              type="button"
              class="btn btn-lime"
              v-on:click="changeFormStatus"
            >I Accept Terms and Conditions Mentioned Above</button>
          </div>
        </div>

        <form-wizard
          @on-complete="submitOrderForm"
          color="#66CDAA"
          shape="circle"
          title="Buy Insurance"
          subtitle="Please complete required personal information and choose your desired product."
          v-show="showForm"
        >
          <!-- Headers -->
          <tab-content title="Customer Personal Information">
            <b-card class="mb-3" style="background-color: rgba(178, 250, 228, 0.151) !important;">
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
          <tab-content title="Select Insurance Project">
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
                    >Please select one proper project (product)</legend>
                    <table class="table m-b-0">
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
                            <div>1 Time Insurance</div>
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
                                  value="1-1-18"
                                  v-on:click="checkProjectValue"
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
                                  value="1-2-36"
                                  v-on:click="checkProjectValue"
                                >
                                <label
                                  class="form-check-label"
                                  for="defaultRadio"
                                >Project 2 - (36 EUR)</label>
                              </p>
                            </div>
                          </td>
                          <td>
                            <p>
                              This single-off insurance product will remain valid in an one-way trip.
                              <br>
                              <br>Customers could get due compensation subject to Sum Insured Per Time after one trip.
                              <br>Within the validity period, customers could claim for compensation all the insured baggages.
                              <br>The total amout of compensation should not exceed the Total Sum Insured.
                            </p>
                          </td>
                        </tr>
                        <tr>
                          <td>2</td>
                          <td>
                            <div>15 Days Insurance</div>
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
                                  value="2-1-54"
                                  v-on:click="checkProjectValue"
                                >
                                <label
                                  class="form-check-label"
                                  for="defaultRadio"
                                >Project 1 - (54 EUR)</label>
                              </p>
                            </div>
                            <div class="form-check">
                              <p>
                                <input
                                  class="form-check-input"
                                  type="radio"
                                  name="default_radio"
                                  id="defaultRadio"
                                  value="2-2-72"
                                  v-on:click="checkProjectValue"
                                >
                                <label
                                  class="form-check-label"
                                  for="defaultRadio"
                                >Project 1 - (72 EUR)</label>
                              </p>
                            </div>
                            <div class="form-check">
                              <p>
                                <input
                                  class="form-check-input"
                                  type="radio"
                                  name="default_radio"
                                  id="defaultRadio"
                                  value="2-3-144"
                                  v-on:click="checkProjectValue"
                                >
                                <label
                                  class="form-check-label"
                                  for="defaultRadio"
                                >Project 3 - (144 EUR)</label>
                              </p>
                            </div>
                          </td>
                          <td>
                            <!-- TODO -->
                            <p>
                              This insurance product will remain valid within 15 days after the order is created.
                              <br>
                              <br>Customers could get due compensation subject to Sum Insured Per Time after one trip.
                              <br>Within the validity period, customers could could claim for compensation all the insured baggages.
                              <br>The total amout of compensation should not exceed the Total Sum Insured.
                            </p>
                          </td>
                        </tr>
                        <tr>
                          <td>3</td>
                          <td>
                            <div>30 Days Insurance</div>
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
                                  value="3-1-80"
                                  v-on:click="checkProjectValue"
                                >
                                <label
                                  class="form-check-label"
                                  for="defaultRadio"
                                >Project 1 - (80 EUR)</label>
                              </p>
                            </div>
                            <div class="form-check">
                              <p>
                                <input
                                  class="form-check-input"
                                  type="radio"
                                  name="default_radio"
                                  id="defaultRadio"
                                  value="3-2-150"
                                  v-on:click="checkProjectValue"
                                >
                                <label
                                  class="form-check-label"
                                  for="defaultRadio"
                                >Project 2 - (150 EUR)</label>
                              </p>
                            </div>
                            <div class="form-check">
                              <p>
                                <input
                                  class="form-check-input"
                                  type="radio"
                                  name="default_radio"
                                  id="defaultRadio"
                                  value="3-3-200"
                                  v-on:click="checkProjectValue"
                                >
                                <label
                                  class="form-check-label"
                                  for="defaultRadio"
                                >Project 3 - (200 EUR)</label>
                              </p>
                            </div>
                          </td>
                          <td>
                            <!-- TODO -->
                            <p>
                              This insurance product will remain valid with 30 days after the order is created.
                              <br>
                              <br>Customers could get due compensation subject to Sum Insured Per Time after one trip.
                              <br>Within the validity period, customers could could claim for compensation all the insured baggages.
                              <br>The total amout of compensation should not exceed the Total Sum Insured.
                            </p>
                          </td>
                        </tr>
                        <tr>
                          <td>4</td>
                          <td>
                            <div>1 Year Insurance</div>
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
                                  value="4-1-225"
                                  v-on:click="checkProjectValue"
                                >
                                <label
                                  class="form-check-label"
                                  for="defaultRadio"
                                >Project 1 - (225 EUR)</label>
                              </p>
                            </div>
                            <div class="form-check">
                              <p>
                                <input
                                  class="form-check-input"
                                  type="radio"
                                  name="default_radio"
                                  id="defaultRadio"
                                  value="4-2-350"
                                  v-on:click="checkProjectValue"
                                >
                                <label
                                  class="form-check-label"
                                  for="defaultRadio"
                                >Project 2 - (350 EUR)</label>
                              </p>
                            </div>
                            <div class="form-check">
                              <p>
                                <input
                                  class="form-check-input"
                                  type="radio"
                                  name="default_radio"
                                  id="defaultRadio"
                                  value="4-3-500"
                                  v-on:click="checkProjectValue"
                                >
                                <label
                                  class="form-check-label"
                                  for="defaultRadio"
                                >Project 3 - (500 EUR)</label>
                              </p>
                            </div>
                          </td>
                          <td>
                            <!-- TODO -->
                            <p>
                              This insurance product will remain valid with one year after the order is created.
                              <br>
                              <br>Customers could get due compensation subject to Sum Insured Per Time after one trip.
                              <br>Within the validity period, customers could could claim for compensation all the insured baggages.
                              <br>The total amout of compensation should not exceed the Total Sum Insured.
                            </p>
                          </td>
                        </tr>
                      </tbody>
                    </table>

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
                    <!-- end col-8 -->
                  </div>
                  <!-- end row -->
                </fieldset>
                <!-- end fieldset -->
              </div>
              <!-- end step-2 -->
            </b-card>
          </tab-content>
          <tab-content title="Remarks and Questions">
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
import { FormWizard, TabContent, WizardStep } from "vue-form-wizard";
import PageOptions from "../config/PageOptions.vue";
import axios from "axios";

export default {
  data() {
    return {
      showForm: false,
      formData: {
        first_name: this.$user.first_name,
        last_name: this.$user.last_name,
        username: this.$user.username,
        email: this.$user.email,
        birthday: this.$user.birthday.toISOString().substr(0, 10),
        phone_num: this.$user.phone_num,
        passport_num: this.$user.passport_num,
        address: this.$user.address,
        product_id:  "",
        project_id: "",
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
      var today = new Date().toISOString().substr(0, 10);
      if (this.formData.birthday == today) {
        this.formData.birthday = new Date("1000-01-01")
          .toISOString()
          .substr(0, 10);
      }

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
