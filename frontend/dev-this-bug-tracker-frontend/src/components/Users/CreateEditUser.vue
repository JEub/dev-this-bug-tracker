<script setup>
    import { ref, onMounted } from 'vue';
    const groups = ref(['Retail'])
    const securityQuestion = ref('Please make a selection')
    onMounted(() => console.log(securityQuestion.value))
    // Logic to match passwords on front end?
</script>

<template>
    <div id="modal-dialog">
        <form action="" class="modal-content">
            <div class="dismiss-row">
                <h3>Create / Edit User</h3>
                <button type="button" class="btn btn-danger" @click="close">Close</button>
            </div>
            <div class="modal-row">
                <label for="">Email: </label>
                <input  type="text">
            </div>
            <div class="modal-row">
                <label for="">UserName</label>
                <input  type="text">
            </div>
            <div class="modal-row">
                <label for="">Password: </label>
                <input  type="password"> 
            </div>
            <div class="modal-row">
                <label for="">Confirm Password: </label>
                <input  type="password">
            </div>
            
            <div>
                <div class="modal-row">
                    <label for="">Groups</label>
                    <input type="checkbox" id="retail" value="Retail" v-model="groups">
                    <label for="retail">Retail </label>
                    <input type="checkbox" id="office" value="Office" v-model="groups">
                    <label for="office">Office </label>
                    <input type="checkbox" id="field" value="Field" v-model="groups">
                    <label for="field">Field </label>
                </div>
                <div>
                    <p>Current Groups: <pre>{{ groups }}</pre></p>
                </div>
            </div>
            <div class="modal-row">
                <div >
                    <label for="">Security Question</label>
                    <select v-model="securityQuestion"  >
                    <!--<option>Please make a selection</option>-->
                        <option>What was your first pet?</option>
                        <option>Where is your hometown?</option>
                        <option>What is your favorite food?</option>
                    </select>
                </div>
                <div>
                    <p class="row">Selected Question: <pre>{{ securityQuestion }}</pre></p>
                </div>
            </div>
            <div class="modal-row">
                <label for="">Security Answer</label>
                <input v-model="securityAnswer" type="text">
            </div>
            <div class="dismiss-row">
                <button type="submit" class="btn btn-success">Submit!</button>
                <button type="button" class="btn btn-danger" @click="close">Close</button>
            </div>
        </form>
    </div>
</template>
<style>
@import './UserFormStyle.css';
</style>