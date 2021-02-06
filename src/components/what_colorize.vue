<!-- Блок Что раскрасить -->
<template>
<div class="card-body">
    <p class="font-size-base text-muted">Выберите одну или несколько категорий</p>

    <span
        v-for="category in mainCategories"
        :key="category.id"
        class="btn btn-outline bg-indigo-400 text-indigo-400 border-indigo-400 mb-1 mr-1"
        :class=getActive(category)
        @click="showCategory(category)"
    >
        <h4 class="font-size-14 font-weight-semibold mb-0">{{ category.name }}</h4>
    </span>

    <div class="min-400">
        <transition name="fade">
            <div class="row justify-content-center" v-if="post"> 
                <div class="card m-3">
                    <div class="card-body">
                        <div class="card-img-actions mb-3 position-relative">
                            <a
                                :href="post.get_absolute_url"
                                data-popup="lightbox"
                            >
                                <img
                                    class="card-img img-fluid image-print w-200"
                                    :src="post.image_path"
                                    alt="" title="" itemprop="contentUrl"
                                >
                            </a>
                        </div>
                        <h5 class="mb-3 pl-2 text-center">
                            <span class="font-weight-semibold text-default">{{ post.name }}</span>
                        </h5>
                    </div>
                    <div class="card-footer text-center">
                        <a :href="post.get_absolute_url">Перейти к срисовке</a>
                    </div>
                </div>
            </div>
        </transition>
    </div>

    <div class="d-flex justify-content-center">
        <p>Поиск из - {{ countPosts }} шт.</p>
    </div>

    <div class="d-flex justify-content-center">
        <button
            type="button"
            class="btn btn-danger rounded-round"
            @click="showPost()"
        >Другая срисовка</button>
    </div>

</div>
</template>


<script>
// TODO: отключение категории не работает по 2 клику(мобилки)
export default {
    data() {
        return {
            mainCategories: [],
            postId: [],
            post: null
        }
    },
    mounted() {
        axios.get('/apiws/v1/category/', { params: {'first_level': true} })
        .then(response => {
            this.mainCategories.push({
                active: true,
                id: null,
                image_menu: null,
                name: 'Все срисовки'
            });
            response.data.forEach(element => {
                element['active'] = false
                this.mainCategories.push(element)
            });
            this.getIdPosts([]);
        })
        .catch(error => console.log(error.response));
    },
    computed: {
        countPosts() {
            return this.postId.length
        },
    },
    methods: {
        showPost() {
            this.post = null;
            let randPost = this.postId[Math.floor(Math.random()*this.postId.length)];
            this.getPost(randPost.id);
            // ym(55732822, 'reachGoal', 'vr_what_color');
        },
        getActive(category) {
            return category.active ? 'active' : ''
        },
        showCategory(category) {
            this.post = null;
            let act_category = '';
            if (category.id == null) {
                this.mainCategories.forEach((elem) => elem.active = false)
                this.mainCategories[0].active = true;
            } else {
                this.mainCategories[0].active = false;
                category.active = !category.active;
                this.mainCategories.filter((elem) => { if (elem.active) act_category += elem.id + ',' })
            }
            let nonActive = this.mainCategories.filter(elem => elem.active)
            if (nonActive.length == 0) this.mainCategories[0].active = true;
            this.getIdPosts(act_category)
        },
        getIdPosts(act_category) {
            axios.get('/apiws/v1/what_colorize', { params: { act_category } })
            .then(response => {
                this.postId = response.data
                let randPost = this.postId[Math.floor(Math.random()*this.postId.length)]
                this.getPost(randPost.id)
            })
            .catch(error => console.log(error.response));
        },
        getPost(id) {
            axios.get(`/apiws/v1/what_colorize/${id}/`)
            .then(response => this.post = response.data)
            .catch(error => console.log(error.response));
        }
    }
}
</script>


<style scoped>
.fade-enter-active{
    transition: all 1s ease;
}
.fade-leave-active{
    transition: all 1s ease;
}
.fade-enter{
    transform: translateX(500px);
    opacity: 0;
}
.fade-leave-to{
    transform: translateX(-500px);
    opacity: 1;
}
</style>