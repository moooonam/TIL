<template>
  <div class="">
    <h2>Signup</h2>
      <span>username:</span><input 
      type="text" 
      v-model.trim="username" 
      >
      <br>
      <span>password:</span><input 
      type="text" 
      v-model.trim="password" 
      >
      <br>
      <span>passwordconfirm:</span><input 
      type="text" 
      v-model.trim="passwordConfirm" 
      >
      <br>
      <span>email:</span><input 
      type="text" 
      v-model.trim="email"
      @keyup.enter="signup" 
      >
      <button @click="signup">SIGNUP</button>
      <br>
    </div>
</template>

<script>
// import axios from 'axios'

import axios from 'axios';

export default {
  name: 'Singup',
  data: function () {
    return {
      username: null,
      password: null,
      passwordConfirm: null,
      email:null
    }
  },
  methods: {
    signup: function () {
      const username = this.username
      const password = this.password
      const passwordConfirm = this.passwordConfirm
      const email = this.email
      axios({
        method: 'post',
        url:'http://127.0.0.1:8000/accounts/signup/',
        data:{username, password, passwordConfirm, email},
      })
      .then(() =>{
        this.$router.push({name :'Login' })})
      

      
    }
  }
}
</script>

