<script setup>
// Figure out functionality for logining in. Also decide if the functions will be located in a different file

</script>

<template>
  <form class="authentication-form">
    <div class="authentication-information">
      <div class="authentication-input">
        <h2 class="authentication-header">Email</h2>
        <input class="authentication-input-field" placeholder="Email" />
      </div>
      <div class="authentication-input">
        <h2 class="authentication-header">Password</h2>
        <input class="authentication-input-field" placeholder="Password" type="password" />
      </div>
    </div>
    <div class="buttons-section">
      <div class="buttons primary">
        <button class="button login-button">Login</button>
      </div>
      <div class="buttons secondary">
        <button class="button password-button">Forgot Password</button>
        <button class="button register-button">Register</button>
      </div>
    </div>
  </form>
</template>

<style>
@import './LoginForm.css';
</style>
