<!-- Комментарии под постом -->
<!-- http://demo.interface.club/limitless/demo/Template/layout_1/LTR/material/full/blog_single.html -->
<template>
<div>
    <div class="card-body">
        <ul class="media-list">
            <li class="media flex-column flex-md-row" v-for="comment in comments" :key="comment.id">
                <div class="mr-md-3 mb-2 mb-md-0">
                    <a href="#">
                        <img :src="getAvatar(comment)" class="rounded-circle" width="38" height="38" alt="">
                    </a>
                </div>
                <div class="media-body">
                    <div class="media-title">
                        <span class="font-weight-semibold">{{ getUsername(comment) }}</span>
                        <span class="text-muted ml-3">{{ getDiffDate(comment.created_at) }}</span>
                        <span class="link-style ml-2 cursor-pointer" @click.prevent="replyComment(comment)">Ответить</span>
                    </div>
                    <p>{{ comment.text }}</p>

                    <dir class="p-0" v-if="comment.children">
                        <div class="media flex-column flex-md-row" v-for="commentChild in comment.children" :key="commentChild.id">
                        <div class="mr-md-3 mb-2 mb-md-0">
                            <a href="#">
                                <img :src="getAvatar(commentChild)" class="rounded-circle" width="38" height="38" alt="">
                            </a>
                        </div>

                        <div class="media-body">
                            <div class="media-title">
                                <span class="font-weight-semibold">{{ getUsername(commentChild) }}</span>
                                <span class="text-muted ml-3">{{ getDiffDate(commentChild.created_at) }}</span>
                                <span class="link-style ml-2 cursor-pointer" @click.prevent="replyComment(commentChild)">Ответить</span>
                            </div>

                            <p>{{ commentChild.text }}</p>

                        </div>
                        </div>
                    </dir>
                    
                </div>
            </li>
        </ul>
    </div>

    <hr class="m-0">

    <div class="card-body">
        <form action="POST">
            <div class="form-group">
                <label>Оставьте комментарий</label>
                <textarea
                    placeholder="Текст комментария"
                    class="form-control"
                    v-model="newComment"
                    ref="textInput"
                ></textarea>
            </div>
            <div class="text-right">
                <button type="submit" @click.prevent="submitComment()" class="btn btn-primary bg-indigo-400">
                    Отправить <i class="icon-paperplane ml-2"></i>
                </button>
            </div>
        </form>
    </div>
</div>
</template>


<script>
export default {
    props: {
        postId: {
            default: null
        }
    },
    data() {
        return {
            comments: [],
            newComment: null,
            reply: null,
            parent: null
        } 
    },
    created() {
        this.getComments();
    },
    mounted() {},
    watch: {
        newComment(newValue, oldValue) {
            if (!newValue) this.setDefault();
        }
    },
    computed: {},
    methods: {
        setDefault() {
            this.newComment = null;
            this.parent = null;
            this.reply = null;
        },
        replyComment(comment) {
            this.$refs.textInput.focus();
            this.newComment = `${comment.user ? comment.user.username : `Гость(${comment.id})`}, `;
            comment.parent ? this.parent = comment.parent : this.parent = comment.id;
        },
        getAvatar(comment) {
            return comment.user ? comment.user.get_avatar : '/static/img/avatar.jpg';
        },
        getUsername(comment) {
            return comment.user ? comment.user.username : `Гость(${comment.id})`;
        },
        getComments() {
            axios.get('/apiws/v1/comments/', { params: { post_id: this.postId } })
            .then(response => this.comments = this.$createTreePID(response.data))
            .catch(error => console.log(error));
        },
        submitComment() {
            axios({
                method: 'POST',
                xsrfHeaderName: 'X-CSRFToken',
                url: '/apiws/v1/comments/',
                headers: {
                    'X-CSRFToken': this.$cookies.get('csrftoken') 
                },
                data: {
                    'parent': this.parent ? this.parent : null,
                    'post': this.postId,
                    'text': this.newComment,
                    'user': null
                }
            })
            .then(response => {
                console.log(response.data);
                this.getComments();
                this.setDefault();
            })
            .catch(error => console.log(error));
        },
        getDiffDate(created_at) {
            let now = new Date();
            created_at = new Date(created_at);

            let millisec = now.getTime() - created_at.getTime();

            let seconds = (millisec / 1000).toFixed(0);
            let minutes = (millisec / (1000 * 60)).toFixed(0);
            let hours = (millisec / (1000 * 60 * 60)).toFixed(0);
            let days = (millisec / (1000 * 60 * 60 * 24)).toFixed(0);
            let month = (millisec / (1000 * 60 * 60 * 24 * 30)).toFixed(0);
            let years = (millisec / (1000 * 60 * 60 * 24 * 365)).toFixed(0);

            if (minutes < 5) return 'Только что';
            if (minutes < 60) return `${minutes} мин назад`;
            if (hours < 24) return `${hours} час ${minutes % 60} мин назад`;
            if (days < 30) return `${days} дней ${hours % 24} час назад`;
            if (month < 12) return `${month} мес назад`;
            if (years >= 1) return 'Более года назад';
        },
    }
}
</script>