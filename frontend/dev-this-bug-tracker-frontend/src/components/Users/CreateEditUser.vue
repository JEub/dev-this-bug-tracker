<script setup>
    import { ref, onMounted } from 'vue';
    const groups = ref(['Retail'])
    const securityQuestion = ref('Please make a selection')
    onMounted(() => console.log(securityQuestion.value))
</script>
<script>
    export default {
        name: 'User Form',
        props: {    
            userData: {
                "email": String,
                "password": String,
                "username": String,
                "groups": String,
                "security_question": String,
                "security_answer": String,
            },
            openUserProfile: {
                type: Function
            },
        },
        methods: {
            // uses Options API to emit a custom event
            close() {
                this.$emit('close');
            },
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
        },
    };
</script>
<template>
    <div id="modal-dialog" >
        <div class="modal-content">
            <form action="" class="modal-row">
                <div class="header-row">
                    <h3>Create / Edit User</h3>
                    <button type="button" class="btn btn-danger" @click="close">Close</button>
                </div>
                <div class="row">
                    <label for="">Email: </label>
                    <input  type="text">
                </div>
                <div class="row">
                    <label for="">UserName</label>
                    <input  type="text">
                </div>
                <div class="row">
                    <label for="">Password: </label>
                    <input  type="password"> 
                </div>
                <div class="row">
                    <label for="">Confirm Password: </label>
                    <input  type="password">
                </div>
                <div class="box">
                    <div >
                        <label for="">Groups</label>
                        <input type="checkbox" id="retail" value="Retail" >
                        <label for="retail">Retail </label>
                        <input type="checkbox" id="office" value="Office" >
                        <label for="office">Office </label>
                        <input type="checkbox" id="field" value="Field" >
                        <label for="field">Field </label>
                    </div>
                    <div>
                        <p>Current Groups: <pre>{{ groups }}</pre></p>
                    </div>
                </div>
                <div class="box">
                    <div>
                        <label for="">Security Question</label>
                        <select   >
                        <!--<option>Please make a selection</option>-->
                            <option>What was your first pet?</option>
                            <option>Where is your hometown?</option>
                            <option>What is your favorite food?</option>
                        </select>
                    </div>
                    <p >Selected Question: <pre>{{ securityQuestion }}</pre></p>
                </div>
                <div class="row">
                    <label for="">Security Answer</label>
                    <input  type="text">
                </div>
                <div class="dismiss-row">
                    <!--Submit button should save data. close edit user modal and open user profile modal-->
                    <button  type="submit" class="btn btn-success"
                    @click="openUserProfile('userProfile')">Submit!</button>
                    <button type="button" class="btn btn-danger" @click="close">Close</button>
                </div>
            </form>
        </div>
    </div>
</template>
<style>
    @import './UserFormStyle.css';
</style>