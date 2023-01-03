<template>
  <div>
    <h1>Lunch</h1>
    <button @click="pickLunch">Pick Lunch</button>
    <p>{{ pickedMenu }}</p>
    <h1>Lotto 뽑으러 가기</h1>
    <button @click="goToLotto">Pick Lotto</button>
  </div>
</template>

<script>

export default {
  name: 'LunchView',
  data : function (){
    return {
      menu: ['국밥','피자','햄버거','짬뽕','초밥'],
      pickedMenu : ""
    }
  },
  methods:{
    pickLunch(){
      this.pickedMenu=this.menu[Math.floor(Math.random()*this.menu.length)]
    },
    goToLotto(){
      this.$router.push({name: 'lotto'})
    }

  }
}


</script>