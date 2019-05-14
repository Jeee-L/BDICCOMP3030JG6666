<template>
  <div>
    <!-- begin page-header -->
    <div class="card card-block">
      <h1 class="page-header">{{$t('m.pi')}}</h1>
      <p>
        {{$t('m.travel')}}
        <br>{{$t('m.travel1')}}
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
              <h4>{{$t('m.time1')}}</h4>
              <p>$90+</p>
            </div>
            <div class="stats-link">
              <a href="javascript:;" v-b-modal.modalDialog>
                {{$t('m.view')}}
                <i class="fa fa-arrow-alt-circle-right"></i>
              </a>
            </div>
          </div>
        </div>
        <!-- end col-3 -->
        <!-- #modal-dialog -->
        <b-modal
          id="modalDialog"
          :cancel-title="$t('m.tbn')"
          cancel-variant="danger"
          @cancel="buyInsurance()"
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

        <!-- begin col-3 -->
        <div class="col-lg-3 col-md-6">
          <div class="widget widget-stats bg-orange">
            <div class="stats-icon">
              <i class="fa fa-link"></i>
            </div>
            <div class="stats-info">
              <h4>{{$t('m.time2')}}</h4>
              <p>$270+</p>
            </div>
            <div class="stats-link">
              <a href="javascript:;" v-b-modal.modalDialog2>
                {{$t('m.view')}}
                <i class="fa fa-arrow-alt-circle-right"></i>
              </a>
            </div>
          </div>
        </div>

        <b-modal
          id="modalDialog2"
          :cancel-title="$t('m.tbn')"
          cancel-variant="warning"
          @cancel="buyInsurance()"
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
        <!-- end col-3 -->
        <!-- begin col-3 -->
        <div class="col-lg-3 col-md-6">
          <div class="widget widget-stats bg-grey-darker">
            <div class="stats-icon">
              <i class="fa fa-users"></i>
            </div>
            <div class="stats-info">
              <h4>{{$t('m.time3')}}</h4>
              <p>$400+</p>
            </div>
            <div class="stats-link">
              <a href="javascript:;" v-b-modal.modalDialog3>
                {{$t('m.view')}}
                <i class="fa fa-arrow-alt-circle-right"></i>
              </a>
            </div>
          </div>
        </div>

        <b-modal
          id="modalDialog3"
          :cancel-title="$t('m.tbn')"
          cancel-variant="grey"
          @cancel="buyInsurance()"
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
        <!-- end col-3 -->
        <!-- begin col-3 -->
        <div class="col-lg-3 col-md-6">
          <div class="widget widget-stats bg-blue">
            <div class="stats-icon">
              <i class="fa fa-clock"></i>
            </div>
            <div class="stats-info">
              <h4>{{$t('m.time4')}}</h4>
              <p>$1100+</p>
            </div>
            <div class="stats-link">
              <a href="javascript:;" v-b-modal.modalDialog4>
                {{$t('m.view')}}
                <i class="fa fa-arrow-alt-circle-right"></i>
              </a>
            </div>
          </div>
        </div>

        <b-modal
          id="modalDialog4"
          :cancel-title="$t('m.tbn')"
          cancel-variant="info"
          @cancel="buyInsurance()"
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
                style="font-size:15px">{{$t('m.coverage')}}</span>
        </template>

        <ul style="font-size:15px;padding:0;margin:0;list-style:none">
            
           <li> <i class="fa fa-check" aria-hidden="true"
               style="margin:10px"> {{$t('m.c1')}}</i></li>
           <li> <i class="fa fa-check" aria-hidden="true"
               style="margin:10px"> {{$t('m.c2')}}</i></li>
            <li><i class="fa fa-check" aria-hidden="true"
               style="margin:10px"> {{$t('m.c3')}}</i></li>
            <li><i class="fa fa-check" aria-hidden="true"
               style="margin:10px"> {{$t('m.c4')}}</i></li>
        </ul>
      </b-tab>
      <b-tab>
        <template slot="title">
          <span class="d-sm-none">Pills 2</span>
          <span class="d-sm-block d-none"
                style="font-size:15px">{{$t('m.disclaimer')}}</span>
        </template>

        <h5 class="m-t-10">{{$t('m.dis1')}}</h5>
        <ul style="font-size:15px;padding:0;margin:0;list-style:none">
            
           <li> <i class="fa fa-times" aria-hidden="true"
               style="margin:10px"> {{$t('m.dis2')}}</i></li>
           <li> <i class="fa fa-times" aria-hidden="true"
               style="margin:10px"> {{$t('m.dis3')}}</i></li>
           <li><i class="fa fa-times" aria-hidden="true"
               style="margin:10px"> {{$t('m.dis4')}}</i></li>
        </ul>

        <h5 class="m-t-10">{{$t('m.dis5')}}</h5>
        <ul style="font-size:15px;padding:0;margin:0;list-style:none">
           <li> <i class="fa fa-times" aria-hidden="true"
               style="margin:10px"> {{$t('m.dis6')}}</i></li>
           <li> <i class="fa fa-times" aria-hidden="true"
               style="margin:10px"> {{$t('m.dis7')}}</i></li>
           <li><i class="fa fa-times" aria-hidden="true"
               style="margin:10px"> {{$t('m.dis8')}}</i></li>
           <li> <i class="fa fa-times" aria-hidden="true"
               style="margin:10px"> {{$t('m.dis9')}}</i></li>
           <li><i class="fa fa-times" aria-hidden="true"
               style="margin:10px"> {{$t('m.dis10')}}</i></li>
           <li><i class="fa fa-times" aria-hidden="true"
               style="margin:10px"> {{$t('m.dis11')}}</i></li>
        </ul>
      </b-tab>
      <b-tab active>
        <template slot="title">
          <span class="d-sm-none">Pills 3</span>
          <span class="d-sm-block d-none"
                style="font-size:15px">{{$t('m.faq')}}</span>
        </template>

        <!-- begin b-card -->
        <b-card no-body>
          <b-card-header
            header-tag="header"
            class="card-header bg-light-light-green text-green pointer-cursor"
            v-b-toggle.accordion1
          >{{$t('m.faq1')}}</b-card-header>
          <b-collapse id="accordion1" visible accordion="my-accordion">
            <b-card-body>{{$t('m.faq2')}}</b-card-body>
          </b-collapse>
        </b-card>
        <!-- end b-card -->
        <!-- begin b-card -->
        <b-card no-body>
          <b-card-header
            header-tag="header"
            class="card-header bg-light-light-green text-green pointer-cursor"
            v-b-toggle.accordion2
          >{{$t('m.faq3')}}</b-card-header>
          <b-collapse id="accordion2" accordion="my-accordion">
            <b-card-body>{{$t('m.faq4')}}</b-card-body>
          </b-collapse>
        </b-card>
        <!-- end b-card -->
        <!-- begin b-card -->
        <b-card no-body>
          <b-card-header
            header-tag="header"
            class="card-header bg-light-light-green text-green pointer-cursor"
            v-b-toggle.accordion3
          >{{$t('m.faq5')}}</b-card-header>
          <b-collapse id="accordion3" accordion="my-accordion">
            <b-card-body>{{$t('m.faq6')}}</b-card-body>
          </b-collapse>
        </b-card>
        <!-- end b-card -->
        <!-- begin b-card -->
        <b-card no-body>
          <b-card-header
            header-tag="header"
            class="card-header bg-light-light-green text-green pointer-cursor"
            v-b-toggle.accordion4
          >{{$t('m.faq7')}}</b-card-header>
          <b-collapse id="accordion4" accordion="my-accordion">
            <b-card-body>{{$t('m.faq8')}}</b-card-body>
          </b-collapse>
        </b-card>
        <!-- end b-card -->
        <!-- begin b-card -->
        <b-card no-body>
          <b-card-header
            header-tag="header"
            class="card-header bg-light-light-green text-green pointer-cursor"
            v-b-toggle.accordion5
          >{{$t('m.faq9')}}</b-card-header>
          <b-collapse id="accordion5" accordion="my-accordion">
            <b-card-body>{{$t('m.faq10')}}</b-card-body>
          </b-collapse>
        </b-card>
        <!-- end b-card -->
        <!-- begin b-card -->
        <b-card no-body>
          <b-card-header
            header-tag="header"
            class="card-header bg-light-light-green text-green pointer-cursor"
            v-b-toggle.accordion6
          >{{$t('m.faq11')}}</b-card-header>
          <b-collapse id="accordion6" accordion="my-accordion">
            <b-card-body>{{$t('m.faq12')}}</b-card-body>
          </b-collapse>
        </b-card>
        <!-- end b-card -->
        
      </b-tab>
    </b-tabs>
    <!-- end nav-tabs-pills -->
  </div>
</template>

<script>
export default {
  methods:{
    buyInsurance(){
      this.$router.push("/baggage/insurance");
    }
  }
}
</script>
