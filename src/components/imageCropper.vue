<!-- Загрузка картинки в админке пользователя -->
<template>
<div class="card-body">
    <div class="form-group row">
    <div class="col-md-12" :class="[errors.name ? 'has-error' : '']">
        <label>Предложите свое название срисовке</label>
        <input
            type="text"
            placeholder="Предложите свое название"
            maxlength="150"
            class="form-control"
            v-model="name"
        >
        <span v-if="errors.name" class="form-text text-danger">
            <i class="icon-cancel-circle2 mr-2"></i>
            {{ errors.name.message }}
        </span>
        <span v-else class="form-text text-muted">
            Название должно быть уникальное
        </span>
    </div>
    </div>
    <div class="form-group">
        <label>Загрузите свою срисовку</label>
        <input type="file" @change="selectFile">
    </div>

    <div class="d-flex flex-lg-row flex-column-reverse">
        <div class="image-cropper-container mb-4">
            <img :src="src" ref="image">
        </div>
        <div class="mb-3 text-center" v-if="showImage">
            <div class="eg-preview d-md-flex justify-content-md-center align-items-md-center text-center">
                <!-- <div class="preview preview-lg d-md-inline-block mt-3 mx-auto mr-md-0 mt-md-0 ml-md-3 overflow-hidden rounded"></div> -->
                <div class="preview preview-lg d-md-inline-block mt-3 mx-auto mr-md-0 mt-md-0 ml-md-3 border overflow-hidden rounded"></div>
            </div>
        </div>
    </div>

    <div class="row">
        <div class="col-md-12">
            <div class="form-group">
                <label class="font-weight-semibold">Управление:</label>
                <div class="btn-group btn-group-justified">
                    <div class="btn-group">
                        <button type="button" class="btn bg-blue btn-icon" title="Zoom In" @click="zoomIn()">
                            <span class="icon-zoomin3"></span>
                        </button>
                    </div>

                    <div class="btn-group">
                        <button type="button" class="btn bg-blue btn-icon" title="Zoom Out" @click="zoomOut()">
                            <span class="icon-zoomout3"></span>
                        </button>
                    </div>

                    <div class="btn-group">
                        <button type="button" class="btn bg-blue btn-icon" title="Rotate Left" @click="rotateLeft()">
                            <span class="icon-rotate-ccw3"></span>
                        </button>
                    </div>

                    <div class="btn-group">
                        <button type="button" class="btn bg-blue btn-icon" title="Rotate Right" @click="rotateRight()">
                            <span class="icon-rotate-cw3"></span>
                        </button>
                    </div>

                    <div class="btn-group">
                        <button type="button" class="btn bg-blue btn-icon" title="Flip Horizontal" @click="scaleX()">
                            <span class="icon-flip-vertical4"></span>
                        </button>
                    </div>

                    <div class="btn-group">
                        <button type="button" class="btn bg-blue btn-icon" title="Flip Vertical" @click="scaleY()">
                            <span class="icon-flip-vertical3"></span>
                        </button>
                    </div>
                </div>
            </div>
            <div class="form-group">
                
                <div class="btn-group btn-group-justified">

                    <div class="btn-group">
                        <button type="button" class="btn bg-blue btn-icon" title="Левее" @click="moveLeft()">
                            <span class="icon-arrow-left13"></span>
                        </button>
                    </div>

                    <div class="btn-group">
                        <button type="button" class="btn bg-blue btn-icon" title="Правее" @click="moveRight()">
                            <span class="icon-arrow-right14"></span>
                        </button>
                    </div>

                    <div class="btn-group">
                        <button type="button" class="btn bg-blue btn-icon" title="Выше" @click="moveUp()">
                            <span class="icon-arrow-up13"></span>
                        </button>
                    </div>

                    <div class="btn-group">
                        <button type="button" class="btn bg-blue btn-icon" title="Ниже" @click="moveDown()">
                            <span class="icon-arrow-down132"></span>
                        </button>
                    </div>

                    <div class="btn-group">
                        <button type="button" class="btn bg-green btn-icon" title="Crop" @click="cropImage()">
                            <span class="icon-checkmark"></span>
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
</template>


<script>

import Cropper from 'cropperjs';
export default {
    data() {
        return {
            src: '',
            image: {},
            showImage: false,
            cropper: {},
            name: null,
            errors: {
                name: null,
                image: null
            },
            paramX: 1,
            paramY: 1,
        }
    },
    mounted() {
        this.cropper = new Cropper(this.$refs.image, {
            zoomable: true,
            scalable: true,
            aspectRatio: 1,
            preview: '.preview'
        });
    },
    methods: {
        setDeafault() {
            this.name = null;
            this.cropper.clear();
        },
        selectFile(e) {
            this.errors.name = null
            const file = (e.target.files || e.dataTransfer.files)[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = e => this.cropper.replace(e.target.result);
                reader.readAsDataURL(file);
                this.showImage = true
            }
        },
        cropImage() {
            this.cropper.getCroppedCanvas({
                width: 800,
                height: 800,
                minWidth: 256,
                minHeight: 256,
                maxWidth: 800,
                maxHeight: 800,
                fillColor: '#fff',
            })
            .toBlob((blob) => {
                let formData = new FormData();  
                formData.append('image', blob, 'image.jpeg');
                if (this.name) formData.append('name', this.name);
                axios({
                    method: 'POST',
                    url: '/accounts/profile/add_post/',
                    xsrfHeaderName: 'X-CSRFToken',
                    headers: {
                        'Content-Type': 'multipart/form-data',
                        'X-CSRFToken': this.$getCookie('csrftoken')
                    },
                    data: formData
                })
                .then(response => {
                    if (response.data.ok) {
                        console.log('ok')
                        wstanley.jG_notifications_success('Круто!', 'Ваша картинка отправлена на модерацию.')
                        this.setDeafault()
                        this.errors.name = null;
                    } else {
                        let err = JSON.parse(response.data.errors);
                        err.name ? this.errors.name = err.name[0] : this.errors.name = null;
                        wstanley.jG_notifications_warning('Ошибка!', 'Исправьте ошибки на форме.')
                    }
                })
                .catch(error => console.log(error))
            }, 'image/jpeg', 0.90)
        },
        moveLeft() {
            this.cropper.move(-10,0);
        },
        moveRight() {
            this.cropper.move(10,0);
        },
        moveDown() {
            this.cropper.move(0,10);
        },
        moveUp() {
            this.cropper.move(0,-10);
        },
        zoomIn() {
            this.cropper.zoom(0.1);
        },
        zoomOut() {
            this.cropper.zoom(-0.1);
        },
        rotateLeft() {
            this.cropper.rotate(-30);
        },
        rotateRight() {
            this.cropper.rotate(30);
        },
        scaleX() {
            this.paramX == 1 ? this.paramX = -1 : this.paramX = 1
            this.cropper.scale(this.paramX, this.paramY);
        },
        scaleY() {
            this.paramY == 1 ? this.paramY = -1 : this.paramY = 1
            this.cropper.scale(this.paramX, this.paramY);
        },
    },
}
</script>

<style scoped>
.eg-preview .preview-lg {
    width: 230px;
    height: 230px;
}
</style>