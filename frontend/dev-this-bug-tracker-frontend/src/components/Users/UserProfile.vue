<script setup>
    import { ref, onMounted } from 'vue';
    const userActive = ref(true)
    onMounted(() => console.log(userActive))
</script>
<script>
    export default {
        name: 'UserProfile',
        props: {    
            userData: {
                "Username": String,
                "email": String,
                "groups": String,
                "tickets": String,
                "security_question": String,
                "security_answer": String,
            },
            openEditUser: {
                type: Function
            },
        },
        methods: {
            close() {
                this.$emit('close');
            },
        },
    };
</script>
<template>
    <div id="modal-dialog">
        <div class="modal-content">
            <div class="modal-row">
                <div class="header-row">
                    <h3>Welcome </h3>
                    <button type="button" class="btn btn-danger" @click="close">Close</button>
                </div>
                <div class="row">
                    <a href="" alternate="User Profile Picture"></a>
                    <h4>Username: </h4>
                    <p></p>
                </div>
                <div class="row">
                    <h4>Email: </h4>
                    <p></p>
                </div>
                <div class="row">
                    <h4>Groups: </h4>
                    <p></p>
                </div>
                <div class="row">
                    <h4>Ticket Queues: </h4>
                    <p></p>
                </div>
                <div class="row">
                    <h4>Security Question: </h4>
                    <p></p>
                </div>
                <!--Dont display Security answer on profile page. This is a password type that should be hashed in database-->
                <div class="dismiss-row">
                    <!--Open edit user pass in userData?-->
                    <button  type="button" class="btn btn-success"
                    @click="openEditUser('userForm')">Edit Profile</button>
                    <button type="button" class="btn btn-danger" @click="close">Close</button>
                    <!--Add function above to deactivaet user here-->
                    <button type="button" class="btn outline-danger">Deactivate Account</button>
                </div>
            </div>
        </div>
    </div>
</template>
<style>
    @import './UserFormStyle.css';
</style>