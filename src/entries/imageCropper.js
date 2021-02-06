Promise = require('es6-promise').Promise;
window.axios = require('axios');
window.Vue = require('vue');

import getCookie from '../vue_plugins/common.js'

Vue.use(getCookie);

Vue.component('image-cropper', require('../components/imageCropper.vue').default)

const app = new Vue({
    el: '#app'
})
