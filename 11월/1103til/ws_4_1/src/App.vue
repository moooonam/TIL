<template>
  <div id="app">
    <h1 style="text-align:center">버튼 박스 제작</h1>
    <HelloWorld msg="예약 페이지" msg2="시간 선택"/>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  components: {
    HelloWorld
  }
}
</script>

<style>

</style>
