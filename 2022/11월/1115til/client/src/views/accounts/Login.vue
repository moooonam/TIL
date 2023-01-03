<template>
  <div>
    <h2>Login</h2>
    <span>username:</span><input 
      type="text" 
      v-model.trim="username" 
      >
      <span>password:</span><input 
      type="text" 
      v-model.trim="password"
      @keyup.enter="login" 
      >
      <button @click="login">login</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Login',
  data: function () {
    return {
      username: null,
      password: null
    }
  },
  methods: {
    login: function () {
      const username = this.username
      const password = this.password
      axios({
        method: 'post',
        url : 'http://127.0.0.1:8000/api/token/',
        data: {username, password}
      })
      .then((res) => {
        localStorage.setItem("jwt", res.data.access)
        this.$emit("login")
        this.$router.push({name: "TodoList"})
      })
    }
  }
}
</script>
