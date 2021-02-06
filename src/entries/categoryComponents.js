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
        nameCoockie: 'plWs'
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
            let data = Cookies.get('plWs');
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
