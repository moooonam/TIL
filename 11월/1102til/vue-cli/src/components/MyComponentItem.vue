<template>
  <div>
    <h3>{{ msg }}</h3>
    <p>{{ dynamicProps }}</p>
    <button @click="childToParent">클릭!</button>
    <input 
    type="text" 
    v-model="childInputData"
    @keyup.enter="childInput">
  </div>
</template>

<script>

export default {
    name: 'MyComponentItem',
    props:{
      msg: String,
      dynamicProps : String
    },
    data : function() {
      return {
        childInputData: null,
      }
    },
    methods: {
      childToParent: function() {
        this.$emit('child-to-parent', 'child data')
      },
      childInput: function() {
        this.$emit('child-input', this.childInputData)
        this.childInputData= null
      },
    },

}
</script>

<style>

</style>