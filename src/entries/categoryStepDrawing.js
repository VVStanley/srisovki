import 'jquery';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';

// template plugins
// import '../global_assets/js/plugins/loaders/blockui.min.js';
// import '../global_assets/js/plugins/ui/ripple.min.js';
import '../global_assets/js/plugins/ui/slinky.min.js';
import '../global_assets/js/plugins/ui/sticky.min.js';
import '../global_assets/js/plugins/ui/fab.min.js'
import '../global_assets/js/plugins/notifications/jgrowl.min.js';
import '../global_assets/js/plugins/media/fancybox.min.js';

// template scss
import '../global_assets/scss/shared/icons/icomoon/compile/styles.scss';
import '../global_assets/scss/shared/icons/fontawesome/compile/styles.scss';
import '../global_assets/scss/layouts/layout_5/material/compile/bootstrap.scss';
import '../global_assets/scss/layouts/layout_5/material/compile/bootstrap_limitless.scss';
import '../global_assets/scss/layouts/layout_5/material/compile/components.scss';
import '../global_assets/scss/layouts/layout_5/material/compile/layout.scss';
import '../global_assets/scss/layouts/layout_5/material/compile/colors.scss';

// my app plugins
import '../app_plugins/slick/slick.min.js';
import '../app_plugins/slick/slick.css';
import '../app_plugins/slick/slick-theme.css';

// my app js
import '../app/js/wstanleyObj.js';
import '../app/js/app.js';
import '../app/js/gallery.js';
import '../app/js/custom.js';

// my app css
import '../app/css/files.css';
import '../app/css/sizes.css';
import '../app/css/menu.css';
import '../app/css/bages.css';
import '../app/css/colors.css';
import '../app/css/common.css';
import '../app/css/fonts.css';
import '../app/css/responsive.css';

Promise = require('es6-promise').Promise;
window.axios = require('axios');
window.Vue = require('vue');

import Vuex from 'vuex';
import Cookies from 'js-cookie';

Vue.use(require('vue-cookies'));
Vue.use(Vuex);


const store = new Vuex.Store({
    state: {
        postLiked: null,
        nameCoockie: 'plWsSD'
    },
    getters: {
        postLiked: state => {
            return state.postLiked;
        },
        nameCoockie: state => {
            return state.nameCoockie;
        },
    },
    mutations: {
        setPostLiked: (state, payload) => {
            state.postLiked = payload
        },
    },
    actions: {
        getPostLiked (context) {
            let data = Cookies.get('plWsSD');
            if (data) data = data.split(',')
            context.commit('setPostLiked', data)
        }
    }
});

Vue.component('like-post', require('../components/likePost.vue').default);

const app = new Vue({
    el: '#app',
    store,
    mounted() {
        this.$store.dispatch('getPostLiked');
    },
});
