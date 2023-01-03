<template>
  <div class="d-grid gap-3 col-11 mx-auto my-3" style="border:1px solid #198754; border-radius:5px; height: 50px">
    <div class="d-flex justify-content-between">
      <div class="text-center px-2 py-2">
        {{ option.type }}
      </div>
      <div class=" px-2 py-2">
        <button @click="decrease" class="mx-2" style="border:0"><img src="https://previews.123rf.com/images/martialred/martialred1507/martialred150700933/42621301-%EB%B9%BC%EA%B8%B0-%EC%95%B1-%EB%B0%8F-%EC%9B%B9-%EC%82%AC%EC%9D%B4%ED%8A%B8%EC%9D%98-%EB%9D%BC%EC%9D%B8-%EC%95%84%ED%8A%B8-%EC%95%84%EC%9D%B4%EC%BD%98-%EB%B9%BC%EA%B8%B0-%EB%B0%8F-%EC%A0%9C%EA%B1%B0.jpg" height="30" width="30">
        </button>
        <span>{{ option.count }}</span>
        <button @click="increase" class="mx-2" style="border:0"><img src="https://previews.123rf.com/images/martialred/martialred1507/martialred150700754/42614040-%EC%95%B1-%EB%B0%8F-%EC%9B%B9-%EC%82%AC%EC%9D%B4%ED%8A%B8%EC%97%90-%EB%8C%80%ED%95%9C-%EC%B6%94%EA%B0%80-%EB%B0%8F-%EB%8D%94%ED%95%98%EA%B8%B0-%EB%9D%BC%EC%9D%B8-%EC%95%84%ED%8A%B8-%EC%95%84%EC%9D%B4%EC%BD%98.jpg" height="30" width="30">
        </button>
      </div>
    </div>
    
  </div>
</template>

<script>
export default {
  name: 'OptionListItem',
  props: {
    option: Object,
  },
  methods: {
    increase() {
      
      this.$store.dispatch('increase', this.option)
      // console.log(optionType)
    },
    decrease() {
      
      this.$store.dispatch('decrease', this.option)
    },
  },
}
</script>

<style>
</style>