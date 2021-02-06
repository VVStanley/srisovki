Promise = require('es6-promise').Promise;
window.axios = require('axios');
window.Vue = require('vue');

Vue.component('what-colorize', require('../components/what_colorize.vue').default)

const app = new Vue({
    el: '#app'
})
