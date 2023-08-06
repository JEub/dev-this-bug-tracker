<script setup>
import {ref} from 'vue'
const isOpen = ref(false)
const close = () => {
    emit('close');
};
</script>
<script>
    export default {
        name: 'TicketModal',
        props: ['title', 'msg'],
        emit: ['close'],
    }
</script>
<template>
    <div class="modal" v-if="isOpen=true">
        <h2>{{ title }}</h2>
        <p>{{ msg }}</p>
        <button type="button" class="close" @click="close">Close </button>
    </div>
</template>
<style>
    @import '../DashBoard/DashBoard.css';
</style>