import Vue from 'vue'
import VueX from 'vuex'
import routes from './config/PageRoutes'

// plugins
import VueRouter from 'vue-router'
import VueBootstrap from 'bootstrap-vue'
import VueNVD3 from 'vue-nvd3'
import VueInsProgressBar from 'vue-ins-progress-bar'
import VueEventCalendar from 'vue-event-calendar'
import VueSparkline from 'vue-sparklines'
import * as VueGoogleMaps from 'vue2-google-maps'
import Vueditor from '@agametov/vueditor'
import VueHljs from 'vue-hljs'
import VueSweetalert2 from 'vue-sweetalert2'
import VueNotification from 'vue-notification'
import VuePanel from './plugins/panel/'
import VueDateTimePicker from 'vue-bootstrap-datetimepicker'
import VueSelect from 'vue-select'
import VueDatepicker from "vuejs-datepicker/dist/vuejs-datepicker.esm.js"
import VueMaskedInput from 'vue-maskedinput';
import VueInputTag from 'vue-input-tag';
import VueSlider from 'vue-slider-component';
import VueGoodTable from 'vue-good-table';
import VueFullCalendar from 'vue-full-calendar'
import VueCountdown from '@xkeshi/vue-countdown';
import VueColorpicker from 'vue-pop-colorpicker';
import VueChartJs from 'vue-chartjs';
import validationMessagesEn from 'vee-validate/dist/locale/en';
import validationMessagesCn from 'vee-validate/dist/locale/zh_CN';

// plugins css
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import 'nvd3/build/nv.d3.min.css'
import 'vue-event-calendar/dist/style.css'
import 'vue-hljs/dist/vue-hljs.min.css'
import 'pc-bootstrap4-datetimepicker/build/css/bootstrap-datetimepicker.css';
import 'simple-line-icons/css/simple-line-icons.css'
import 'flag-icon-css/css/flag-icon.min.css'
import 'bootstrap-social/bootstrap-social.css'
import 'ionicons/dist/css/ionicons.min.css'
import 'vue-good-table/dist/vue-good-table.css'
import 'fullcalendar/dist/fullcalendar.css'

// color admin css
import './assets/css/default/style.min.css'
import './assets/css/default/style-responsive.min.css'
import './assets/css/default/theme/default.css'
import './assets/css/style.css'

import axios from 'axios'
import VueAxios from 'vue-axios'

import App from './App.vue'

import VeeValidate from 'vee-validate';

import VueI18n from 'vue-i18n'

Vue.use(VueI18n) // 通过插件的形式挂载

const i18n = new VueI18n({
  locale: localStorage.getItem('locale') || 'en',    // 语言标识
  // this.$i18n.locale // 通过切换locale的值来实现语言切换
  messages: {
    'cn': require('./i18n/langs/cn'),   // 中文语言包
    'en': require('./i18n/langs/en')    // 英文语言包
  }
})

Vue.config.productionTip = false

Vue.use(VueX)
Vue.use(VueRouter)
Vue.use(VueBootstrap)
Vue.use(VueNVD3)
Vue.use(VueEventCalendar, { locale: 'en' })
Vue.use(VueSparkline)
Vue.use(Vueditor)
Vue.use(VueHljs)
Vue.use(VueSweetalert2)
Vue.use(VueNotification)
Vue.use(VuePanel)
Vue.use(VueDateTimePicker)
Vue.use(VueGoodTable)
Vue.use(VueFullCalendar)
Vue.use(VueColorpicker)
Vue.use(VueGoogleMaps, {
  load: {
    key: '',
    libraries: 'places'
  }
})
Vue.use(VueInsProgressBar, {
  position: 'fixed',
  show: true,
  height: '3px'
})
Vue.use(VueAxios, axios);
Vue.use(VeeValidate, {
  i18n,
  i18nRootKey: 'validation',
  dictionary: {
    en: validationMessagesEn,
    cn: validationMessagesCn
  }
});


Vue.component('v-select', VueSelect);
Vue.component('datepicker', VueDatepicker);
Vue.component('masked-input', VueMaskedInput);
Vue.component('input-tag', VueInputTag);
Vue.component('vue-slider', VueSlider);
Vue.component(VueCountdown.name, VueCountdown);

// Global variables configuration
import store from './config/store';
Vue.use(store);

// Vue Cropper for image processing
import VueCropper from 'vue-cropper'
Vue.use(VueCropper);


const router = new VueRouter({
  routes,
  mode: "history",
})

new Vue({
  render: h => h(App),
  router,
  i18n,
}).$mount('#app')
