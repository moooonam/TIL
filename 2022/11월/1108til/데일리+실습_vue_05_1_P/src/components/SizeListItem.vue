<template>
   <div class="d-grid gap-2 col-11 mx-auto my-3">
    <button @click="pickSize"
    class="btn  btn-outline-success text-dark"
    :class="{ 'picked' : size.selected }"
     type="button">{{ size.name }} {{ size.price }}원</button>
  </div>
</template>

<script>
export default {
  name: 'SizeListItem',
  props: {
    size: Object,
  },
  methods:{
    pickSize(){
      this.$store.dispatch('pickSize', this.size)
    }
  }
}
</script>

<style>
  .picked{
    background-color: #198754;
  }
</style>