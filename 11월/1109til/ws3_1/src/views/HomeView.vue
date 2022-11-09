<template>
  <div>
    <h1>Home or About</h1>
    <h2>첫 번째 박스</h2>
    <div class="global">
      <div class="box scoped-box"></div>
    </div>
    <h2>두 번째 박스</h2>
    <div class="global">
      <div class="box scoped-box"></div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'HomeView',
}
</script>
<style>
.box{
  width: 100px;
  height: 100px;
  border: solid 1px black;
}
.global{
  display: inline-block;
  margin: auto;
}
</style>
