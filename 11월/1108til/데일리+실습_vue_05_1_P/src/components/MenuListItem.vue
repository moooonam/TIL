<template>
  <div class="d-grid gap-2 col-11 mx-auto my-3" >
    <button @click="pickMenu"  
    class="btn btn-outline-success text-dark " type="button" 
    :class="{ 'picked' : menu.selected }"
    style="width:350px"> <img :src="menu.image" class="float-start" height="40" width="40">  
        {{ menu.title }}  
        {{ menu.price }}원
    
    </button>
  
  </div>
</template>

<script>
export default {
  name: 'MenuListItem',
  props: {
    menu: Object,
  },
  methods:{
    pickMenu(){
      this.$store.dispatch('pickMenu', this.menu)
    }
  }
}
</script>

<style>
  .picked{
    background-color: #198754;
  }
</style>