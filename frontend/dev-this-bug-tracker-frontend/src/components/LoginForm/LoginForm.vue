<script setup>
// Figure out functionality for logining in. Also decide if the functions will be located in a different file
  import { ref } from 'vue';
  const user = ref([ 
        {id:"username", name: null},
        {id:"password", name: null}
    ]);
// import user edit modal
// create password edit modal
  function loginSubmit(event) {
    event.preventDefault()
    alert(JSON.stringify(this.form))
    console.log(user.username);
    this.$emit('user', this.user.username)
        //  save ticket data to ref or state here
    }
    
</script>

<template>
  <div id="modal-dialog">
    <div class="modal-content">
      <!--action to login = /users/login
      need redirect in python controller to nav to "/"-->
      <form action="/" class="modal-row">
        <div class="header-row">
          <h2>Login or Register</h2>
        </div>
        <div class="row">
          <h2>Email: </h2>
          <input placeholder="someone@email.com" v-model="user.username" />
        </div>
        <div class="row">
          <h2>Password: </h2>
          <input placeholder="Password" type="password" v-model="user.password"/>
        </div>
        <div class="dismiss-row">
            <!--how to reset? edit password modal on verification of email?-->
            <button class="btn btn-danger">Forgot Password</button>
            <!-- login goes to dashboard-->
            <!--Register goes to user edit modal then once complete to dashboard-->
            <!--@click="loginSubmit(event)"-->
            <button @click="loginSubmit()" type="submit" class="btn btn-success">Login</button>
            <button class="btn btn-primary">Register</button>
        </div>
        <div v-if="user" class="row">
          <h2 >User logged in: {{ user.username }}</h2>
        </div>
      </form>
    </div>
  </div>
</template>

<style>
    @import '../Users/UserFormStyle.css';
</style>
