import Vue from 'vue'
import App from './App.vue'
import router from './router.js'
import { createApp } from 'vue'

new Vue({
  router, 
  render: h => h(App)
}).$mount('#app');

createApp(App).mount('#app')
