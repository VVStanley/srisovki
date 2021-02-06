<!-- Пустая заготовка блока для компонента -->
<template>
    <li class="mb-1 mr-1 cursor-pointer link-style font-size-lg" title="Избранное" @click="clickWishlist()">
        <i class="icon-heart5 text-pink font-size-20" v-if="postInFavorites"></i>
        <i class="icon-heart6 text-pink font-size-20" v-else></i>
    </li>
</template>


<script>
export default {
    props: {
        inFavorites: {
            default: false
        },
        postId: {
            default: null
        }
    },
    data() {
        return {
            postInFavorites: false
        }
    },
    mounted() {
        this.postInFavorites = this.inFavorites;
    },
    computed: {},
    methods: {
        clickWishlist() {
            axios({
                method: 'POST',
                xsrfHeaderName: 'X-CSRFToken',
                url: this.postInFavorites ? `/post_remove_wishlist/${this.postId}/` : `/post_add_wishlist/${this.postId}/`,
                headers: {
                    'Content-Type': 'text/html; charset=utf-8',
                    'X-CSRFToken': this.$cookies.get('csrftoken') 
                }
            })
            .then(response => console.log(response.data))
            .catch(error => console.log(error.response));
            this.postInFavorites 
                ? wstanley.jG_notifications_warning('Готово!', 'Срисовка удалена из избранного')
                : wstanley.jG_notifications_success('Готово!', 'Срисовка добавлена в избранное');
            this.postInFavorites = !this.postInFavorites;
        },
    }
}
</script>