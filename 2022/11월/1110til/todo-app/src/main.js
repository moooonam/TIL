import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'
import "bootstrap"
import "bootstrap-icons/font/bootstrap-icons.css"
Vue.config.productionTip = false

new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app')
