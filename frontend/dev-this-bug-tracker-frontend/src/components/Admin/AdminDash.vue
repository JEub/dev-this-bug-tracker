<script setup>
    import { ref } from 'vue';
    import axios from 'axios';
    import CreateEditUser from '../Users/CreateEditUser.vue';
    import UserProfile from '../Users/UserProfile.vue';

    const users = ref([]);
    const userFormVisable =  ref(false);
    const userProfileVisable = ref(false);
    const errors = ref(false);

    // submit should open user profile
    function showModal(modalType) {
        switch(modalType) {
            case 'userForm':
                // modalData.value = userData;
                userFormVisable.value = true;
                userProfileVisable.value = false;
                break;
            case 'userProfile':
                // modalData.value = userData;
                userProfileVisable.value = true;
                userFormVisable.value = false;
                break;
        }
    }
    function closeModal(modalType){
        switch(modalType) {
            case 'userForm':
                // modalData.value = userData;
                userFormVisable.value = false;
            case 'userProfile':
                // modalData.value = userData;
                userProfileVisable.value = false;
                break;
        }
    }
    function getAllUsers() {
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
    // CLOSE MODAL
    function close() {
    // uses Options API to emit a custom event
        this.$emit('close');
    }

</script>
<template>
    <div id="container">
        <div id="nav">
            <button @click="showModal('userForm')" class="btn btn-outline-secondary">Create User</button>
            <button @click="showModal('userProfile')"
            class="btn btn-outline-success"
            >Profile</button>
        </div>
        <div class="dashboard" id="admin">
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