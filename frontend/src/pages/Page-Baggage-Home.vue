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
              <p>€90+</p>
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
                <td>€1000</td>
                <td>€2000</td>
              </tr>
              <tr>
                <td>Sum Insured Per Time</td>
                <td>€1000</td>
                <td>€2000</td>
              </tr>
              <tr>
                <td>Price</td>
                <td>€90</td>
                <td>€180</td>
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
              <p>€270+</p>
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
                <td>€2600</td>
                <td>€4000</td>
                <td>€8000</td>
              </tr>
              <tr>
                <td>Sum Insured Per Time</td>
                <td>€1000</td>
                <td>€2000</td>
                <td>€4000</td>
              </tr>
              <tr>
                <td>Price</td>
                <td>€270</td>
                <td>€360</td>
                <td>€700</td>
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
              <p>€400+</p>
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
                <td>€2600</td>
                <td>€4000</td>
                <td>€8000</td>
              </tr>
              <tr>
                <td>Sum Insured Per Time</td>
                <td>€1000</td>
                <td>€2000</td>
                <td>€4000</td>
              </tr>
              <tr>
                <td>Price</td>
                <td>€400</td>
                <td>€700</td>
                <td>€1000</td>
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
              <p>€1100+</p>
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
                <td>€2600</td>
                <td>€4000</td>
                <td>€8000</td>
              </tr>
              <tr>
                <td>Sum Insured Per Time</td>
                <td>€1000</td>
                <td>€2000</td>
                <td>€4000</td>
              </tr>
              <tr>
                <td>Price</td>
                <td>€1100</td>
                <td>€1500</td>
                <td>€2000</td>
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
      <b-tab active>
        <template slot="title">
          <span class="d-sm-none">Pills 1</span>
          <span class="d-sm-block d-none">Pills Tab 1</span>
        </template>

        <h3 class="m-t-10">Nav Pills Tab 1</h3>
      </b-tab>
      <b-tab>
        <template slot="title">
          <span class="d-sm-none">Pills 2</span>
          <span class="d-sm-block d-none">Pills Tab 2</span>
        </template>

        <h3 class="m-t-10">Nav Pills Tab 2</h3>
        <p>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit.
          Integer ac dui eu felis hendrerit lobortis. Phasellus elementum, nibh eget adipiscing porttitor,
          est diam sagittis orci, a ornare nisi quam elementum tortor.
          Proin interdum ante porta est convallis dapibus dictum in nibh.
          Aenean quis massa congue metus mollis fermentum eget et tellus.
          Aenean tincidunt, mauris ut dignissim lacinia, nisi urna consectetur sapien,
          nec eleifend orci eros id lectus.
        </p>
      </b-tab>
      <b-tab>
        <template slot="title">
          <span class="d-sm-none">Pills 3</span>
          <span class="d-sm-block d-none">Pills Tab 3</span>
        </template>

        <h3 class="m-t-10">Nav Pills Tab 3</h3>
        <p>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit.
          Integer ac dui eu felis hendrerit lobortis. Phasellus elementum, nibh eget adipiscing porttitor,
          est diam sagittis orci, a ornare nisi quam elementum tortor.
          Proin interdum ante porta est convallis dapibus dictum in nibh.
          Aenean quis massa congue metus mollis fermentum eget et tellus.
          Aenean tincidunt, mauris ut dignissim lacinia, nisi urna consectetur sapien,
          nec eleifend orci eros id lectus.
        </p>
      </b-tab>
    </b-tabs>
    <!-- end nav-tabs-pills -->
  </div>
</template>