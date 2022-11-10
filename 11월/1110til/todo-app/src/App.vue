<template>
  <div class="d-flex">
    <div class="fs-1 text-center box mx-3 my-3">
      <router-link to="/">모든</router-link> 
      <br>
      <router-link to="/today">오늘</router-link>
      <br>
      <router-link to="/important">중요</router-link>
    </div>
    <div class="box2 mx-3 my-3 p-4">
      <router-view/>
    </div>
  </div>
</template>

<style>


div a {
  font-weight: bold;
  color: #2c3e50;
  text-decoration: none;
}

div a.router-link-exact-active {
  color: #42b983;
}

.box{
  border: solid black 1px;
  border-radius: 15px;
  width: 300px;
  height: 800px;
  padding: 50px
}
.box2{
  border: solid black 1px;
  border-radius: 15px;
  width: 800px;
  height: 800px;

}
</style>
