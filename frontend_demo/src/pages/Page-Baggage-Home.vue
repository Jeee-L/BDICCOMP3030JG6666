<template>
  <div>
    <!-- begin page-header -->
    <div class="card card-block">
      <h1 class="page-header">Production Information</h1>
      <p>
        When you are travelling, your carry-on luggage and checked luggage may encounter theft, robbery, damage, loss and other accidents.
        <br>This product will provide comprehensive compensation for your luggage protection.
      </p>
      <!-- end page-header -->
      <!-- begin row -->
      <div class="row">
        <!-- begin col-3 -->
        <div class="col-lg-3 col-md-6">
          <div class="widget widget-stats bg-red">
            <div class="stats-icon">
              <i class="fa fa-desktop"></i>
            </div>
            <div class="stats-info">
              <h4>1 TIME</h4>
              <p>$90+</p>
            </div>
            <div class="stats-link">
              <a href="javascript:;" v-b-modal.modalDialog>
                View Detail
                <i class="fa fa-arrow-alt-circle-right"></i>
              </a>
            </div>
          </div>
        </div>
        <!-- end col-3 -->
        <!-- #modal-dialog -->
        <b-modal
          id="modalDialog"
          cancel-title="Buy Now"
          cancel-variant="danger"
          ok-title="Cancel"
          ok-variant="white"
          title="1 Time Insurance"
        >
          <p>For claimed items without original receipts, payment of loss will be calculated based upon 75% of the Actual Cash Value at the time of loss, not to exceed $250.</p>
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
                <td>$1000</td>
                <td>$2000</td>
              </tr>
              <tr>
                <td>Sum Insured Per Time</td>
                <td>$1000</td>
                <td>$2000</td>
              </tr>
              <tr>
                <td>Price</td>
                <td>$90</td>
                <td>$180</td>
              </tr>
            </tbody>
          </table>
          <br>
        </b-modal>

        <!-- begin col-3 -->
        <div class="col-lg-3 col-md-6">
          <div class="widget widget-stats bg-orange">
            <div class="stats-icon">
              <i class="fa fa-link"></i>
            </div>
            <div class="stats-info">
              <h4>15 DAYS</h4>
              <p>$270+</p>
            </div>
            <div class="stats-link">
              <a href="javascript:;" v-b-modal.modalDialog2>
                View Detail
                <i class="fa fa-arrow-alt-circle-right"></i>
              </a>
            </div>
          </div>
        </div>

        <b-modal
          id="modalDialog2"
          cancel-title="Buy Now"
          cancel-variant="warning"
          ok-title="Cancel"
          ok-variant="white"
          title="15 days Insurance"
        >
          <p>For claimed items without original receipts, payment of loss will be calculated based upon 75% of the Actual Cash Value at the time of loss, not to exceed $250.</p>
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
                <td>$2600</td>
                <td>$4000</td>
                <td>$8000</td>
              </tr>
              <tr>
                <td>Sum Insured Per Time</td>
                <td>$1000</td>
                <td>$2000</td>
                <td>$4000</td>
              </tr>
              <tr>
                <td>Price</td>
                <td>$270</td>
                <td>$360</td>
                <td>$700</td>
              </tr>
            </tbody>
          </table>
          <br>
        </b-modal>
        <!-- end col-3 -->
        <!-- begin col-3 -->
        <div class="col-lg-3 col-md-6">
          <div class="widget widget-stats bg-grey-darker">
            <div class="stats-icon">
              <i class="fa fa-users"></i>
            </div>
            <div class="stats-info">
              <h4>30 DAYS</h4>
              <p>$400+</p>
            </div>
            <div class="stats-link">
              <a href="javascript:;" v-b-modal.modalDialog3>
                View Detail
                <i class="fa fa-arrow-alt-circle-right"></i>
              </a>
            </div>
          </div>
        </div>

        <b-modal
          id="modalDialog3"
          cancel-title="Buy Now"
          cancel-variant="grey"
          ok-title="Cancel"
          ok-variant="white"
          title="30 days Insurance"
        >
          <p>For claimed items without original receipts, payment of loss will be calculated based upon 75% of the Actual Cash Value at the time of loss, not to exceed $250.</p>
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
                <td>$2600</td>
                <td>$4000</td>
                <td>$8000</td>
              </tr>
              <tr>
                <td>Sum Insured Per Time</td>
                <td>$1000</td>
                <td>$2000</td>
                <td>$4000</td>
              </tr>
              <tr>
                <td>Price</td>
                <td>$400</td>
                <td>$700</td>
                <td>$1000</td>
              </tr>
            </tbody>
          </table>
          <br>
        </b-modal>
        <!-- end col-3 -->
        <!-- begin col-3 -->
        <div class="col-lg-3 col-md-6">
          <div class="widget widget-stats bg-blue">
            <div class="stats-icon">
              <i class="fa fa-clock"></i>
            </div>
            <div class="stats-info">
              <h4>1 YEAR</h4>
              <p>$1100+</p>
            </div>
            <div class="stats-link">
              <a href="javascript:;" v-b-modal.modalDialog4>
                View Detail
                <i class="fa fa-arrow-alt-circle-right"></i>
              </a>
            </div>
          </div>
        </div>

        <b-modal
          id="modalDialog4"
          cancel-title="Buy Now"
          cancel-variant="info"
          ok-title="Cancel"
          ok-variant="white"
          title="1 Year Insurance"
        >
          <p>For claimed items without original receipts, payment of loss will be calculated based upon 75% of the Actual Cash Value at the time of loss, not to exceed $250.</p>
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
                <td>$2600</td>
                <td>$4000</td>
                <td>$8000</td>
              </tr>
              <tr>
                <td>Sum Insured Per Time</td>
                <td>$1000</td>
                <td>$2000</td>
                <td>$4000</td>
              </tr>
              <tr>
                <td>Price</td>
                <td>$1100</td>
                <td>$1500</td>
                <td>$2000</td>
              </tr>
            </tbody>
          </table>
          <br>
        </b-modal>
        <!-- end col-3 -->
      </div>
    </div>
    <!-- end row -->
    <!-- begin nav-tabs-pills -->
    <b-tabs pills>
      <b-tab>
        <template slot="title">
          <span class="d-sm-none">Pills 1</span>
          <span class=" d-sm-block d-none"
                style="font-size:15px">Coverage Details</span>
        </template>

        <ul style="font-size:15px;padding:0;margin:0;list-style:none">
            
           <li> <i class="fa fa-check" aria-hidden="true"
               style="margin:10px"> Coverage for the baggage consigned or carried by the passenger in conformity with the
                requirements of air transport.</i></li>
           <li> <i class="fa fa-check" aria-hidden="true"
               style="margin:10px"> Coverage for the baggage struck by lightning, fire, explosion.</i></li>
            <li><i class="fa fa-check" aria-hidden="true"
               style="margin:10px"> Coverage for the baggage abandoned in transit due to bad weather or other accidents.</i></li>
            <li><i class="fa fa-check" aria-hidden="true"
               style="margin:10px"> Coverage for all or part of the loss caused by collision, capsize, falling or missing accident or other
                external causes.</i></li>
        </ul>
      </b-tab>
      <b-tab>
        <template slot="title">
          <span class="d-sm-none">Pills 2</span>
          <span class="d-sm-block d-none"
                style="font-size:15px">Disclaimer</span>
        </template>

        <h5 class="m-t-10">The following luggages are not the subject of this insurance contract:</h5>
        <ul style="font-size:15px;padding:0;margin:0;list-style:none">
            
           <li> <i class="fa fa-times" aria-hidden="true"
               style="margin:10px"> Securities such as currency, cheque, etc.</i></li>
           <li> <i class="fa fa-times" aria-hidden="true"
               style="margin:10px"> Dangerous goods, glass and ceramics, jewelry, diamonds, artworks, documents, animals, plants
                and other objects that are not easy to identify the value.</i></li>
           <li><i class="fa fa-times" aria-hidden="true"
               style="margin:10px"> Data recorded on disk, memory card, tape, or other similar device.</i></li>
        </ul>

        <h5 class="m-t-10">The insurer shall not be liable for any loss or expense of the insurance subject caused by:</h5>
        <ul style="font-size:15px;padding:0;margin:0;list-style:none">
           <li> <i class="fa fa-times" aria-hidden="true"
               style="margin:10px"> Nuclear radiation, nuclear explosion, nuclear pollution, radioactive pollution, air pollution, land
                pollution and other kinds of pollution.</i></li>
           <li> <i class="fa fa-times" aria-hidden="true"
               style="margin:10px"> Administrative or judicial acts.</i></li>
           <li><i class="fa fa-times" aria-hidden="true"
               style="margin:10px"> Wars, hostile acts, military acts, armed conflicts, strikes, riots and terrorist activities.</i></li>
           <li> <i class="fa fa-times" aria-hidden="true"
               style="margin:10px"> Intentional, gross negligence or criminal acts of the applicant, the insured and their representatives.</i></li>
           <li><i class="fa fa-times" aria-hidden="true"
               style="margin:10px"> Natural wear and tear, inherent defect, improper packing, sound outer packing but short inner
                packing of the insurance subject.</i></li>
           <li><i class="fa fa-times" aria-hidden="true"
               style="margin:10px"> Baggage not conforming to the standards or regulations of air transport airports or airlines, or taken
                on board without the permission of air transport airports or airlines.</i></li>
        </ul>
      </b-tab>
      <b-tab active>
        <template slot="title">
          <span class="d-sm-none">Pills 3</span>
          <span class="d-sm-block d-none"
                style="font-size:15px">Frequently Asked Questions</span>
        </template>

        <!-- begin b-card -->
        <b-card no-body>
          <b-card-header
            header-tag="header"
            class="card-header bg-light-light-green text-green pointer-cursor"
            v-b-toggle.accordion1
          >1. What are the types of travel luggage insurance products?</b-card-header>
          <b-collapse id="accordion1" visible accordion="my-accordion">
            <b-card-body>Our company provides four kinds of travel luggage insurance products for single trip, 15 days, 30 days
            and one year according to the insured time limit. You can choose the insurance products suitable for you
            according to your travel frequency and specific needs.</b-card-body>
          </b-collapse>
        </b-card>
        <!-- end b-card -->
        <!-- begin b-card -->
        <b-card no-body>
          <b-card-header
            header-tag="header"
            class="card-header bg-light-light-green text-green pointer-cursor"
            v-b-toggle.accordion2
          >2. What does the insurance cover?</b-card-header>
          <b-collapse id="accordion2" accordion="my-accordion">
            <b-card-body>During the international air transport, the baggage consigned or carried by the passenger in conformity
            with the requirements of air transport shall be the subject of this insurance contract. The following luggages are not the subject of this insurance contract: 1.Securities such as currency, cheque, etc;2.Dangerous goods, glass and ceramics, jewelry, diamonds, artworks, documents, animals, plants
            and other objects that are not easy to identify the value;3.Data recorded on disk, memory card, tape, or other similar device.</b-card-body>
          </b-collapse>
        </b-card>
        <!-- end b-card -->
        <!-- begin b-card -->
        <b-card no-body>
          <b-card-header
            header-tag="header"
            class="card-header bg-light-light-green text-green pointer-cursor"
            v-b-toggle.accordion3
          >3. In what circumstances can a claim be made?</b-card-header>
          <b-collapse id="accordion3" accordion="my-accordion">
            <b-card-body>The insurance subject is abandoned in transit due to lightning, fire, explosion, or bad weather or other accidents, and all or part of the loss caused by collision, capsize, falling or missing accident or other external causes.</b-card-body>
          </b-collapse>
        </b-card>
        <!-- end b-card -->
        <!-- begin b-card -->
        <b-card no-body>
          <b-card-header
            header-tag="header"
            class="card-header bg-light-light-green text-green pointer-cursor"
            v-b-toggle.accordion4
          >4. What materials should be provided for claim?</b-card-header>
          <b-collapse id="accordion4" accordion="my-accordion">
            <b-card-body>In case of loss within the scope of insurance coverage, the insured must notify the insurer within 48 hours
            after the insured learns of the loss. When the insured applies for claim from the insurer, the following
            documents must be provided:1.Claim application form, original insurance policy or insurance certificate, air ticket;2. Certificate of accident issued by the transport department;3.Luggage loss list;4.One original
            and one photocopy of identity card or passport;5. Lost luggage, original purchase invoices, relevant price
            vouchers or price certificates of similar items, etc.</b-card-body>
          </b-collapse>
        </b-card>
        <!-- end b-card -->
        <!-- begin b-card -->
        <b-card no-body>
          <b-card-header
            header-tag="header"
            class="card-header bg-light-light-green text-green pointer-cursor"
            v-b-toggle.accordion5
          >5. How does trip cancellation and interruption coverage apply?</b-card-header>
          <b-collapse id="accordion5" accordion="my-accordion">
            <b-card-body>It reimburses for forfeited, non-refundable, unused payments or deposits if the insured must cancel or
            interrupt their trip due to covered reasons. The interruption benefit may also include coverage for
            additional transportation expenses.</b-card-body>
          </b-collapse>
        </b-card>
        <!-- end b-card -->
        <!-- begin b-card -->
        <b-card no-body>
          <b-card-header
            header-tag="header"
            class="card-header bg-light-light-green text-green pointer-cursor"
            v-b-toggle.accordion6
          >6. What does the compensation limit mean?</b-card-header>
          <b-collapse id="accordion6" accordion="my-accordion">
            <b-card-body>1.During the period of insurance, the insurer's liability for indemnity for the subject matter insured in each
            accident shall be limited to the limit of indemnity for each accident;2.During the period of insurance, the
            accumulative liability of the insurer for the subject matter insured shall be limited to the accumulative limit
            of indemnity;3.During the period of insurance, when the accumulative indemnity reaches the limit of
            accumulative indemnity, the insurance liability shall be</b-card-body>
          </b-collapse>
        </b-card>
        <!-- end b-card -->
        
      </b-tab>
    </b-tabs>
    <!-- end nav-tabs-pills -->
  </div>
</template>