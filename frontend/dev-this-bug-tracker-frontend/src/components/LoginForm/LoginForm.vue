<script setup>
  import { ref} from 'vue';
  import { loggedUser } from '../LoginForm/loginUser.js';
  import { store } from '../../store/index.js';
  const userFormVisable = ref(false);
  const existingUser = ref(false);
  const user = ref([ 
        {id:"email", name: null},
        {id:"username", name: 'Guest User'},
        {id:"password", name: null}
    ]);
  const form = ref({
    email:"",
    username:"",
    password:""
  })
  // import user edit modal
// create password edit modal
  function submit(e){
    e.preventDefault();
    this.$store.commit('login', this.user.email);
    console.log( this.$store.state.email)
    }
  function showModal(modalType) {
    switch(modalType) {
      case 'userForm':
        // modalData.value = userData;
        userFormVisable.value = true;
        existingUser.value = true;
        break;
      case 'userProfile':
        // modalData.value = userData;
        userProfileVisable.value = true;
        userFormVisable.value = false;
        break;
    }
  }
</script>

<template>
  <div id="modal-dialog">
    <div class="modal-content">
      <!--action to login = /user/login
      need redirect in python controller to nav to "/"-->
      <form @submit.prevent="submit" action="/user/login" method="post" class="modal-row">
        <div class="header-row">
          <h2>Login</h2>
          <button type="button" class="btn btn-danger" @click="$emit('close')">X</button>
        </div>
        <div class="row">
          <h2>Email: </h2>
          <input v-model="loggedUser.email" required/>
        </div>
        <div class="row">
          <h2>Username: </h2>
          <input  v-model="loggedUser.username" required/>
        </div>
        <div class="row">
          <h2>Password: </h2>
          <input placeholder="********" type="password" v-model="loggedUser.password" required/>
        </div>
        <!--{{ $store.state.email }}-->
        <div class="dismiss-row">
            <!--how to reset? edit password modal on verification of email?-->
            <button class="btn btn-danger">Forgot Password</button>
            <!-- login goes to dashboard-->
            <!--Register goes to user edit modal then once complete to dashboard-->
          
            <button type="submit" class="btn btn-success">Login</button>
            
        </div>
        
      </form>
      <div>
        <!--<div v-if="user" class="row">
          <h2 >User logged in: {{ loggedUser.username }}</h2>
        </div>-->
        <button @click="showModal('userForm')" type="button" class="btn btn-primary">Register Instead</button>
      </div>
    </div>
  </div>
</template>

<style>
    @import '../Users/UserFormStyle.css';
</style>
