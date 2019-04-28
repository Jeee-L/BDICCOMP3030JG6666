<template>
  <ul class="nav">
    <li class="nav-profile">
      <a href="javascript:;" v-on:click="expand()">
        <div class="cover with-shadow"></div>
        <div class="image image-icon bg-black text-grey-darker">
          <i class="fa fa-user"></i>
        </div>
        <div class="info">
          <b class="caret pull-right"></b>
          {{$user.username}}
          <small>Insured customer</small>
        </div>
      </a>
    </li>
    <li>
      <ul
        class="nav nav-profile"
        v-bind:class="{ 'd-block': this.stat == 'expand', 'd-none': this.stat == 'collapse' }"
      >
        <li>
          <router-link to="/customer/info">
            <i class="fa fa-pencil-alt"></i>User Profile
          </router-link>
        </li>
        <li>
          <router-link to="/customer/center">
            <i class="fa fa-question-circle"></i>Customer Service Center
          </router-link>
        </li>
      </ul>
    </li>
  </ul>
</template>

<script>
export default {
  name: "SidebarNavProfile",
  data() {
    return {
      stat: ""
    };
  },
  methods: {
    expand: function() {
      this.stat = this.stat == "expand" ? "collapse" : "expand";
    }
  }
};
</script>
