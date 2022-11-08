<template>
  <div id="app">
    <div class="d-flex mx-auto" >
      <img src="https://www.shinsegaegroupnewsroom.com/wp-content/uploads/2021/07/%EC%8A%A4%ED%83%80%EB%B2%85%EC%8A%A4_%EB%B3%B8%EB%AC%B89002-1.png" width=230px height=200px class="mx-auto">
    </div>
      <h1 class="text-center" >Coffee Order App</h1>
    <br>
    <div class="d-flex justify-content-between mx-5">
      <MenuList/>
      <SizeList/>
      <OptionList/>
    </div>
    <button 
    class="btn  btn-outline-success text-dark col-12 mx-6 my-2"
    @click="addOrder">장바구니에 담기</button>
    <OrderList/>
  </div>
</template>

<script>
import MenuList from '@/components/MenuList'
import SizeList from '@/components/SizeList'
import OrderList from '@/components/OrderList'
import OptionList from '@/components/OptionList'

export default {
  name: 'App',
  components:{
    MenuList,
    SizeList,
    OrderList,
    OptionList
  },
  methods:{
    addOrder() {
      this.$store.dispatch('addOrder')
    }
  },
 
}
</script>

<style>
* {
  box-sizing: border-box;
  font-family: 'Noto Sans KR', sans-serif;
  padding: 0;
  margin: 0;
}

ul {
  list-style: none;
}
</style>
