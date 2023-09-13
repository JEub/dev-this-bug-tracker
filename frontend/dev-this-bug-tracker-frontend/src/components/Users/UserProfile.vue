<script setup>
    import { ref, onMounted } from 'vue';
    const userActive = ref(true)
    const userFormVisable = ref(false);
    const userProfileVisable = ref(false);
    const userData = ref({
        id: 1, name: 'username',
        id: 2, name: 'email',
        id: 3, name: 'groups',
        id: 4, name: 'tickets',
        id: 5, name: 'securityQuestion',
        id: 6, name: 'securityAnswer',
    })
// edit profile should open user edit maybe add emit use here? 
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
    // CLOSE MODAL
    function closeClick() {
        emit('close');
    }
    // onSubmit(event) {
        //     event.preventDefault()
        //     alert(JSON.stringify(this.form))
        //  save ticket data to ref or state here
    // },
    // onReset(event) {
    //     event.preventDefault()
    //     // Reset our form values
    //     this.form.email = ''
    //     this.form.name = ''
    //     this.form.food = null
    //     this.form.checked = []
    //     // Trick to reset/clear native browser form validation state
    //     this.show = false
    //     this.$nextTick(() => {
    //     this.show = true
    //     })
    // },

    onMounted(() => console.log(userActive))
</script>
<template>
    <div id="modal-dialog">
        <div class="modal-content">
            <div class="modal-row">
                <div class="header-row">
                    <h3>Welcome </h3>
                    <button type="button" class="btn btn-danger" 
                    @click="$emit('close')">Close</button>
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
                    <button  type="button" class="btn btn-success" @click="showModal('userForm')">Edit Profile</button>
                    <button type="button" class="btn btn-danger" 
                    @click="$emit('close')">Close</button>
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