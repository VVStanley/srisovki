<!-- Попоулярные срисовки -->
<template>
<div class="card-body">
    <p class="font-size-base text-muted">{{ text }}</p>
    <span
        class="btn btn-outline bg-indigo-400 text-indigo-400 border-indigo-400 mb-1 mr-1"
        :class="[views ? 'active' : '']"
        @click="clickViews()"
    >
        <h4 class="fs14 font-weight-semibold mb-0">По просмотрам</h4>
    </span>
    <span
        class="btn btn-outline bg-indigo-400 text-indigo-400 border-indigo-400 mb-1 mr-1"
        :class="[likes ? 'active' : '']"
        @click="clickLikes()"
    >
        <h4 class="fs14 font-weight-semibold mb-0">По лайкам</h4>
    </span>
    <span
        class="btn btn-outline bg-indigo-400 text-indigo-400 border-indigo-400 mb-1 mr-1"
        :class="[comments ? 'active' : '']"
        @click="clickComments()"
    >
        <h4 class="fs14 font-weight-semibold mb-0">По комментариям</h4>
    </span>

    <div class="d-flex flex-wrap mt-3">
        <div
            class="col-12 col-sm-6 col-md-6 col-lg-4 col-xl-4"
            v-for="(post, index) in posts"
            :key="index"
        >
            <div class="card hover-posts">
                <a :href="post.get_absolute_url" class="card-body p-1">
                    <div class="card-img-actions">
                        <img class="card-img img-fluid" :src="post.image">
                    </div>
                </a>
                <h5 class="mb-3 px-1 lineh-18 text-center">
                    <a :href="post.get_absolute_url" class="font-weight-semibold text-default">{{ post.name }}</a>
                </h5>
                <div class="card-footer d-sm-flex justify-content-sm-between align-items-sm-center">
                    <ul class="list-inline list-inline-dotted text-muted mb-3 mb-sm-0">
                        <li class="list-inline-item">
                            <i class="icon-comment-discussion text-pink fs20" title="Комментарии"></i> {{ post.comments.length }} 
                        </li>
                        <li class="list-inline-item">
                            <i class="icon-eye text-pink fs20" title="Просмотры"></i> {{post.click}}
                        </li>
                        <li class="list-inline-item">
                            <i class="icon-heart6 text-pink" title="Понравилась"></i> {{post.like}}
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </div>

</div>
</template>


<script>
export default {
    data() {
        return {
            views: true,
            likes: null,
            comments: null,

            posts: [],

            text: 'Показаны 36 раскрасок отсортированных: по просмотрам'
        }
    },
    mounted() { this.getPosts() },
    watch: {},
    methods: {
        clickViews() {
            this.views = true;
            this.comments = null;
            this.likes = null;
            this.getText();
            this.getPosts();
        },
        clickLikes() {
            this.likes = true;
            this.comments = null;
            this.views = null;
            this.getText();
            this.getPosts();
        },
        clickComments() {
            this.comments = true;
            this.views = null;
            this.likes = null;
            this.getText();
            this.getPosts();
        },
        getPosts() {
            axios
            .get('/apiws/v1/popular',
            {
                params: {
                    'views': this.views,
                    'likes': this.likes,
                    'comments': this.comments}
            })
            .then(response => {
                this.posts = response.data
                console.log(this.posts)
            })
            .catch(error => console.log(error.response));
        },
        getText() {
            this.text = 'Показаны 36 раскрасок отсортированных:'
                + (this.views ? ' по просмотрам,' : '')
                + (this.likes ? ' по лайкам,' : '')
                + (this.comments ? ' по комментариям,' : '')
            this.text = this.text.slice(0, -1)
        },
    },
}
</script>
