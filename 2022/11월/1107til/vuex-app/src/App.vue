<template>
  <div id="app">
    <h1>{{ message }}</h1>
    <h2>{{ messageLength }}</h2>
    <input type="text" @keyup.enter="changeMessage" v-model="inputData">
  </div>
</template>

<script>


export default {
  name: 'App',
  components: {
  },
  computed: {
    message() {
      return this.$store.state.message
    },
    messageLength(){
      return this.$store.getters.messageLength
    }
  },
  data(){
    return {
      inputData: null,
    }
  },
  methods: {
    changeMessage() {
      const newMessage = this.inputData
      this.$store.dispatch('changeMessage', newMessage)
      this.inputData = null
      // console.log(this)
    },

  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
