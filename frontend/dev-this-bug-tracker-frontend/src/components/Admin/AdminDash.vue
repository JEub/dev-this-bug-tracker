<script setup>
import { ref } from 'vue';
import axios from 'axios';
import CreateEditUser from '../Users/CreateEditUser.vue';
import UserProfile from '../Users/UserProfile.vue';
// const users = ref([null]);
</script>
<script>
    
    export default {
        name: 'AdminDashboard',
        components: {
            CreateEditUser,
            UserProfile
        },
        data () {
            return {
                userFormVisable: false,
                userProfileVisable:false,
                users: [],
                error: false,
            }
        },
        methods: {
            showModal(modalType) {
                switch(modalType) {
                    case 'userForm':
                        console.log('Opening User Form modal!');
                        // this.modalData = ticketData;
                        this.userFormVisable = true;
                        this.userProfileVisable = false;
                        break;
                    case 'userProfile':
                        console.log('Opening User Profile modal!');
                        // this.modalData = userData;
                        this.userProfileVisable = true;
                        this.userFormVisable = false;
                        break;
                }
            },
            closeModal(modalType) {
                switch(modalType) {
                    case 'userForm':
                        console.log('Opening User Form modal!');
                        // this.modalData = ticketData;
                        this.userFormVisable = false;
                    case 'userProfile':
                        console.log('Closing User Profile modal!');
                        // this.modalData = userData;
                        this.userProfileVisable = false;
                        break;
                }
            },
            getAllUsers() {
                axios
                    .get('http://127.0.0.1:8000/user/')
                    .then(response => {
                        console.log(response);
                        const usersData = response.data;
                        console.log(usersData);
                        this.users = usersData;
                        console.log("Success!" + this.users);
                    })
                    .catch(error => {
                        console.log(error);
                        console.log('Try again');
                        this.error = true;
                    })

            }
        },
        // created: () => {
        //     this.getAllUsers();
        //     }
    };
</script>
<template>
    <div>
        <button @click="showModal('userForm')" class="btn btn-outline-secondary">Create User</button>
        <button @click="getAllUsers()"
        class="btn btn-outline-success"
        >Profile</button>
    </div>
    <div class="dashboard">
        <div class="dashboard-header">
            <p>Do we need some kind of filter for users here</p>
        </div>
        <table>
            <thead>
                <tr>
                    <th>
                        <h2>Username</h2>
                    </th>
                    <th>
                        <!--Sub table when clicked for all tickets assigned to this user-->
                        <h2>Assigned ticket count</h2>
                    </th>
                    <th>
                        <h2>More details</h2>
                    </th>
                    <th>
                        <h2>and more details</h2>
                    </th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td></td>
                    <td></td>
                </tr>
            </tbody>
            <nav>
                <div>
                    <p>Pagination here too?</p>
                </div>
            </nav>
        </table>
    </div>
    <!--Opens User Create Modal-->
    <CreateEditUser
        v-if="userFormVisable" 
        @close="closeModal('userForm')"
        :openUserProfile="showModal"
    />
    <!--Opens user profile-->
    <UserProfile
        v-if="userProfileVisable"
        @close="closeModal('userProfile')"
        :openEditUser="showModal"
    />
</template>