<template>
    <div class="row">
      <div class="col-lg-3">
        <div class="card b mb-2">
          <div class="card-header bb">
            <h4 class="card-title">Order Summnary</h4>
          </div>
          <div class="card-body bt">
            <h4 class="b0">Order #65487</h4>
          </div>
          <table class="table">
            <tbody>
              <tr>
                <td>Subtotal</td>
                <td>
                  <div class="text-right text-bold">$400</div>
                </td>
              </tr>
              <tr>
                <td>Estimated Tax</td>
                <td>
                  <div class="text-right text-bold">$1.44</div>
                </td>
              </tr>
              <tr>
                <td>Shiping</td>
                <td>
                  <div class="text-right text-bold">$5</div>
                </td>
              </tr>
            </tbody>
          </table>
          <div class="card-body">
            <div class="clearfix">
              <div class="float-right text-right">
                <div class="text-bold">$406.44</div>
                <div class="text-sm">USD</div>
              </div>
              <div class="float-left text-bold text-dark">ORDER TOTAL</div>
            </div>
          </div>
          <div class="card-body">
            <p>
              <button class="btn btn-primary btn-block" type="button">EXPRESS CHECKOUT</button>
            </p>
            <small class="text-muted">* To use this method you must be registered first</small>
          </div>
        </div>
      </div>
      <div class="col-lg-9">
        <div class="container-md">
          <!-- Checkout Process-->
          <form action="#" method="post" novalidate="novalidate">
            <div id="accordion">
              <!-- Billing Information-->
              <div class="card b mb-2">
                <div class="card-header">
                  <h4 class="card-title">
                    <a
                      class="text-inherit"
                      v-b-toggle.acc1collapse1
                    >1. Customer Personal Information</a>
                  </h4>
                </div>
                <b-collapse v-model="collapse1" id="acc1collapse1">
                  <div class="card-body" id="collapse02">
                    <div class="row">
                      <div class="col-xl-6">
                        <div class="form-group">
                          <label>First Name*</label>
                          <input class="form-control" type="text" name="checkout-name" required>
                        </div>
                        <div class="form-group">
                          <label>Mobile (China)</label>
                          <input class="form-control" type="text" name="checkout-company">
                        </div>
                      </div>
                      <div class="col-xl-6">
                        <div class="form-group">
                          <label>Last Name*</label>
                          <input class="form-control" type="text" name="checkout-lastname" required>
                        </div>
                        <div class="form-group">
                          <label>Mobile (Ireland)</label>
                          <input class="form-control" type="text" name="checkout-email" required>
                        </div>
                      </div>
                    </div>
                    <div class="row">
                      <div class="col-xl-12">
                        <div class="form-group">
                          <label>Address</label>
                          <input class="form-control" type="text" name="checkout-address" required>
                        </div>
                      </div>
                    </div>
                    <div class="row">
                      <div class="col-xl-6"></div>
                    </div>
                    <div class="pt-2 clearfix">
                      <p class="float-right text-sm">
                        <i>Fields marked with (*) are required</i>
                      </p>
                      <div class="float-left">
                        <button
                          class="btn btn-primary"
                          type="button"
                          @click="collapse1 = false; collapse2 = true"
                        >Continue</button>
                      </div>
                    </div>
                  </div>
                </b-collapse>
              </div>
              <!-- Shipping Method-->
              <div class="card b mb-2">
                <div class="card-header">
                  <h4 class="card-title">
                    <a class="text-inherit" v-b-toggle.acc1collapse2>2. Product Information</a>
                  </h4>
                </div>
                <div class="card-body" id="collapse02">
                  <b-collapse v-model="collapse2" id="acc1collapse2">
                    <table class="table m-b-0" style="margin-left: 20px; margin-right: 20px">
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
                </div>

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
              <!-- Payment Information-->
              <div class="card b mb-2">
                <div class="card-header">
                  <h4 class="card-title">
                    <a class="text-inherit" v-b-toggle.acc1collapse3>3. Payment Information</a>
                  </h4>
                </div>
                <b-collapse v-model="collapse3" id="acc1collapse3">
                  <div class="card-body" id="collapse05">
                    <div class="row">
                      <div class="col-xl-6">
                        <div class="form-group">
                          <div class="c-radio">
                            <label>
                              <input
                                class="form-control"
                                id="chk-guest7"
                                type="radio"
                                name="checkout-pay"
                                value="paypal"
                                checked="checked"
                              >
                              <span class="fa fa-check"></span> Paypal
                            </label>
                          </div>
                        </div>
                        <div class="form-group">
                          <div class="c-radio">
                            <label>
                              <input
                                class="form-control"
                                id="chk-guest8"
                                type="radio"
                                name="checkout-pay"
                                value="check"
                              >
                              <span class="fa fa-check"></span> Check / Money order
                            </label>
                          </div>
                        </div>
                        <div class="form-group">
                          <div class="c-radio">
                            <label>
                              <input
                                class="form-control"
                                id="chk-guest9"
                                type="radio"
                                name="checkout-pay"
                                value="creditcard"
                              >
                              <span class="fa fa-check"></span> Credit Card (saved)
                            </label>
                          </div>
                        </div>
                        <div class="form-group">
                          <label>Name on Card*</label>
                          <input class="form-control" type="text" name="checkout-cc-name" required>
                        </div>
                        <div class="form-group">
                          <label>Credit Card Type*</label>
                          <select class="form-control" name="checkout-cc-type" required>
                            <option value>- Please Select -</option>
                            <option value="amex">American Express</option>
                            <option value="visa">Visa</option>
                            <option value="master">Mastercard</option>
                          </select>
                        </div>
                        <div class="form-group">
                          <label>Credit Card Number*</label>
                          <input
                            class="form-control"
                            type="text"
                            name="checkout-cc-number"
                            required
                          >
                        </div>
                        <div class="row">
                          <div class="col-xl-5">
                            <div class="form-group">
                              <label>Credit Expiration month*</label>
                              <select class="form-control" name="checkout-cc-exp-month" required>
                                <option value>Month</option>
                                <option value="1">January</option>
                                <option value="2">February</option>
                                <option value="3">March</option>
                                <option value="4">April</option>
                                <option value="5">May</option>
                                <option value="6">June</option>
                                <option value="7">Jule</option>
                                <option value="8">August</option>
                                <option value="9">September</option>
                                <option value="10">October</option>
                                <option value="11">November</option>
                                <option value="12">December</option>
                              </select>
                            </div>
                          </div>
                          <div class="col-xl-5">
                            <div class="form-group">
                              <label>Credit Expiration year*</label>
                              <select class="form-control" name="checkout-cc-exp-year" required>
                                <option value>Year</option>
                                <option value="2016">2016</option>
                                <option value="2017">2017</option>
                                <option value="2018">2018</option>
                                <option value="2019">2019</option>
                                <option value="2020">2020</option>
                                <option value="2021">2021</option>
                                <option value="2022">2022</option>
                                <option value="2023">2023</option>
                              </select>
                            </div>
                          </div>
                          <div class="col-xl-2">
                            <div class="form-group">
                              <label>CNV*</label>
                              <input
                                class="form-control"
                                type="text"
                                name="checkout-cc-verification"
                                required
                              >
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                    <div class="pt-2 clearfix">
                      <p class="float-right text-sm">
                        <i>Fields marked with (*) are required</i>
                      </p>
                      <div class="float-left">
                        <button
                          class="btn btn-primary"
                          type="button"
                          @click="collapse3 = false; collapse4 = true"
                        >Continue</button>
                      </div>
                    </div>
                  </div>
                </b-collapse>
              </div>
              <!-- Order Review-->
              <div class="card b mb-2">
                <div class="card-header">
                  <h4 class="card-title">
                    <a class="text-inherit" v-b-toggle.acc1collapse4>4. Order Review</a>
                  </h4>
                </div>
                <b-collapse v-model="collapse4" id="acc1collapse4">
                  <div class="card-body" id="collapse06">
                    <div class="table-responsive">
                      <table class="table">
                        <colgroup>
                          <col class="order-pic" span="1">
                          <col class="order-item-name" span="1">
                          <col class="order-qty" span="1">
                          <col class="order-price" span="1">
                          <col class="order-tax" span="1">
                          <col class="order-total" span="1">
                        </colgroup>
                        <thead class="bg-gray-lighter">
                          <tr>
                            <th>Product</th>
                            <th>Product Title</th>
                            <th class="wd-xs">Qty</th>
                            <th>Unit Price</th>
                            <th>Tax</th>
                            <th>Total</th>
                          </tr>
                        </thead>
                        <tbody>
                          <tr>
                            <td class="order-pic thumb64">
                              <img src="img/dummy.png" alt="dummy">
                            </td>
                            <td class="order-item-name">Lorem Ipsum dolor</td>
                            <td class="order-qty">
                              <input class="form-control" type="text" name="checkout-qty" value="1">
                            </td>
                            <td class="order-price">$825.00</td>
                            <td class="order-tax">$16.00</td>
                            <td class="order-total">$841.00</td>
                          </tr>
                          <tr>
                            <td class="order-pic">
                              <img src="img/dummy.png" alt="dummy">
                            </td>
                            <td class="order-item-name">Lorem Ipsum dolor</td>
                            <td class="order-qty">
                              <input class="form-control" type="text" name="checkout-qty" value="1">
                            </td>
                            <td class="order-price">$825.00</td>
                            <td class="order-tax">$16.00</td>
                            <td class="order-total">$841.00</td>
                          </tr>
                        </tbody>
                        <tfoot>
                          <tr>
                            <td colspan="5">Subtotal</td>
                            <td>$1540.00</td>
                          </tr>
                          <tr>
                            <td colspan="5">Shipping &amp; Handling (Free)</td>
                            <td>$0.00</td>
                          </tr>
                          <tr>
                            <td colspan="5">Tax</td>
                            <td>$49.00</td>
                          </tr>
                          <tr class="order-subtotal">
                            <td colspan="5">Subtotal</td>
                            <td>$1340.00</td>
                          </tr>
                        </tfoot>
                      </table>
                    </div>
                    <div class="mt-3">
                      <button
                        class="btn btn-info"
                        type="button"
                        @click="collapse4 = false; collapse1 = true"
                      >Submit Order</button>
                    </div>
                  </div>
                </b-collapse>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
</template>
<script>
export default {
  data() {
    return {
      collapse1: true,
      collapse2: false,
      collapse3: false,
      collapse4: false,
      collapse5: false
    };
  }
};
</script>