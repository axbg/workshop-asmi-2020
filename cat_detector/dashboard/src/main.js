import Vue from 'vue'
import App from './App.vue'

import { MdButton, MdField } from 'vue-material/dist/components'
import VueCarousel from 'vue-carousel';
import 'vue-material/dist/vue-material.min.css'
import 'vue-material/dist/theme/default.css'

Vue.config.productionTip = false

Vue.prototype.$baseUrl = "http://192.168.0.190:5000";

Vue.use(MdButton);
Vue.use(MdField);
Vue.use(VueCarousel);

new Vue({
  render: h => h(App),
}).$mount('#app')
