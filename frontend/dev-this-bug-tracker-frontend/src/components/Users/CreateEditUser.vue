<script setup>
    import { ref, onMounted } from 'vue';

    const email = ref('email@email.com')
    const password = ref('password')
    // not saving below to database so do we need to store to ref?
    const confirmPassword = ref('password')
    const userName = ref('The Best UserName')
    const groups = ref(['Retail'])
    const securityQuestion = ref('Please make a selection')
    const securityAnswer= ref('Enter answer here')

    onMounted(() => console.log(securityQuestion.value))
    // Logic to match passwords on front end?
</script>

<template>
    <div id="modal-dialog">
        <form action="" class="modal-content">
            <div class="dismiss-row">
                <h3>Create / Edit User</h3>
            </div>
            <div class="row">
                <label for="">Email: </label>
                <input v-model="email" type="text">
            </div>
            <div class="row">
                <label for="">Password: </label>
                <input v-model="password" type="password"> 
            </div>
            <div class="row">
                <label for="">Confirm Password: </label>
                <input v-model="confirmPassword" type="password">
            </div>
            <div class="row">
                <label for="">UserName</label>
                <input v-model="userName" type="text">
            </div>
            <div>
                <div class="row">
                    <label for="">Groups</label>
                    <input type="checkbox" id="retail" value="Retail" v-model="groups">
                    <label for="retail">Retail </label>
                    <input type="checkbox" id="office" value="Office" v-model="groups">
                    <label for="office">Office </label>
                    <input type="checkbox" id="field" value="Field" v-model="groups">
                    <label for="field">Field </label>
                </div>
                <p>Current Groups: <pre>{{ groups }}</pre></p>
            </div>
            <div>
                <div class="row">
                    <label for="">Security Question</label>
                    <select v-model="securityQuestion"  >
                    <!--<option>Please make a selection</option>-->
                        <option>What was your first pet?</option>
                        <option>Where is your hometown?</option>
                        <option>What is your favorite food?</option>
                    </select>
                </div>
                <p class="row">Selected Question: <pre>{{ securityQuestion }}</pre></p>
            </div>
            <div class="row">
                <label for="">Security Answer</label>
                <input v-model="securityAnswer" type="text">
            </div>
            <div class="row">
                <button id="button" type="submit">Submit!</button>
            </div>
        </form>
    </div>
</template>
<style>
@import './UserFormStyle.css';
</style>