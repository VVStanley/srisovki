<!-- Лайк поста используется как для поста так и для степ поста разница в урлах ПОСТ sendLikePost -->
<template>
    <li class="list-inline-item cursor-pointer">
        <i class="icon-thumbs-up3 text-pink font-size-20" title="Понравилась" @click="likeClick()" v-if="checkLikedPost"></i> 
        <i class="icon-thumbs-up2 text-pink font-size-20" title="Понравилась" @click="likeClick()" v-else></i> 
        {{ postLike }}
    </li>
</template>


<script>
export default {
    props: {
        like: {
            default: 0
        },
        postId: {
            default: null
        },
        appNames: {
            default: []
        }
    },
    data() {
        return {
            postHaveLike: false,
            postLike: 0,

            post_url: '/post_like/',
        }
    },
    mounted() {
        this.postLike = this.like;
        // Так как лайкают 2 приложения (posts, step_drawing) вычисляем урл я отправки лайка
        this.appNames.indexOf('step_drawing') == 0
            ? this.post_url = '/obuchenie/post_step_like/'
            : this.post_url = '/post_like/'
    },
    computed: {
        checkLikedPost() {
            if (this.$store.getters.postLiked) {
                this.postHaveLike = (this.$store.getters.postLiked.indexOf(this.postId.toString()) != -1) ? true : false
            }
            return this.postHaveLike
        }
    },
    methods: {
        likeClick() {
            if (!this.postId) return
            if (this.$store.getters.postLiked) {
                if (this.$store.getters.postLiked.indexOf(this.postId.toString()) != -1) {
                    wstanley.jG_notifications_warning('Ошибка!', 'Только 1 лайк в сутки на один пост');
                    return
                } 
                this.$store.getters.postLiked.push(this.postId.toString());
                this.$cookies.set(this.$store.getters.nameCoockie, this.$store.getters.postLiked, this.getSecondsEndDay());  
            } else{
                this.$cookies.set(this.$store.getters.nameCoockie, this.postId.toString(), this.getSecondsEndDay());
                this.$store.dispatch('getPostLiked');
            }
            this.postHaveLike = true;
            this.postLike = parseInt(this.postLike) + 1;
            this.sendLikePost();
            wstanley.jG_notifications_success('Круто!', 'Спасибо за ваш лайк.');
        },
        getSecondsEndDay() {
            let d = new Date();
            let h = 24 - parseInt(d.getHours());
            let m = 60 - parseInt(d.getMinutes());
            return h * 60 * 60 + m * 60;
        },
        sendLikePost() {
            axios({
                method: 'POST',
                xsrfHeaderName: 'X-CSRFToken',
                url: `${this.post_url}${this.postId}/`,
                headers: {
                    'Content-Type': 'text/html; charset=utf-8',
                    'X-CSRFToken': this.$cookies.get('csrftoken') 
                }
            })
            .then(response => console.log(response.data))
            .catch(error => console.log(error.response));
        }
    }
}
</script>