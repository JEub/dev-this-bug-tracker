<script setup>
// ##### added ######
// import { ref } from 'vue';
// import CreateEditTicket from '../Tickets/CreateEditTicket.vue';
// const isOpen = ref(false)
// const toggleModal = () => {
//     isOpen.value = !isOpen.value;
//     alert( 'You opened the modal from navbar' );
//     return toggleModal;
// };
</script>
<!-- <script>
    export default {
        name: 'NavBar',
        components: {
            CreateEditTicket
        },
        props: [],
        emit: ['close'],
    };
</script> -->
<template>
    <!-- Temporary -->
    <div class="navbar">
        <div class="buttons-section">
            <button>Create Ticket</button>
            <button>Create User</button>
        </div>
        <div class="user-section">
            <h2 class="username">Welcome, User</h2>
            <div class="user-section-details">
                <img src="../../assets/logo.svg"/>
                <a>Logout</a>
            </div>
        </div>
    </div>
</template>

<style>
    @import './NavBar.css';
</style>
