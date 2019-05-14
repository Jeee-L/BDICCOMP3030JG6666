<template>
  <ul class="nav">
    <li class="nav-profile">
      <a href="javascript:;" v-on:click="expand()">
        <div class="cover with-shadow"></div>
        <div
          class="image image-icon bg-black text-grey-darker"
          style="width: 80px !important; height: 80px !important"
        >
          <img class="img-fluid" :src="$store.state.avatar" width="auto" height="80" alt :onerror="this.default">
        </div>
        <div class="info">
          <b class="caret pull-right"></b>
          {{$store.state.username}}
          <small>{{$t('m.insc')}}</small>
        </div>
      </a>
    </li>
    <li>
      <ul
        class="nav nav-profile"
        v-bind:class="{ 'd-block': this.stat == 'expand', 'd-none': this.stat == 'collapse' }"
        v-bind:style="{ marginTop: (pageOptions.pageSidebarMinified) ? - (scrollTop + 40) + 'px' : '' }"
      >
        <li>
          <router-link to="/customer/info">
            <i class="fa fa-pencil-alt"></i>
            {{$t('m.usep')}}
          </router-link>
        </li>
        <!-- <li>
          <router-link to="/customer/center">
            <i class="fa fa-question-circle"></i>
            {{$t('m.csc')}}
          </router-link>
        </li> -->
      </ul>
    </li>
  </ul>
</template>

<script>
import PageOptions from "../../config/PageOptions.vue";

export default {
  name: "SidebarNavProfile",
  props: ["scrollTop"],
  data() {
    return {
      stat: "expand",
      pageOptions: PageOptions,
      default: 'this.src="' + require('./avatar.jpg') + '"'
    };
  },
  methods: {
    expand: function() {
      this.stat = this.stat == "expand" ? "collapse" : "expand";
    }
  }
};
</script>
