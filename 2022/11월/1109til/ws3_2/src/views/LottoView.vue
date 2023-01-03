<template>
  <div>
    <h1>로또</h1>
    <button @click="pickNum">랜덤 번호 받기</button>
    <p> {{ pickedNum }}</p>
  </div>
</template>

<script>
export default {
  name: 'LottoView',
  data(){
    return{
      pickedNum:[]
    }
  },
  methods:{
    pickNum(){
      this.pickedNum=[]
      for (let i=0; i<7; i++) {
      let randomNum = Math.floor(Math.random() * 24)
      if (this.pickedNum.indexOf(randomNum) === -1) {
      this.pickedNum.push(randomNum)
    } else { 
      i--
    }
      }
    },
  }
};
</script>

<style>
</style>