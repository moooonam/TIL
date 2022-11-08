<template>
  <div class="d-flex justify-content-between my-5">
    <div class="d-flex">
      <img :src="order.image" height="50" width="50">
      <div>
        <div>
          {{order.title}} 
        </div>
        <div>
          사이즈: {{order.size}} 
        </div>
      </div>
    </div>
     <div class="mx-5">
        가격: {{order.price}}원    
        <div class="d-flex" 
        v-for="(orderedOption, index) in order.option"
        :key="index"
        style="font-size:small"
        >
          {{ orderedOption.type }}: {{ orderedOption.count }}회
        </div>
        <div>
          <button @click="deleteOrder" class="btn btn-outline-danger">주문취소</button>
        </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'OrderListItem',
  props: {
    order: Object,
  },
  computed: {
    // totalPrice: function () {
    // },
  },
  methods:{
    deleteOrder() {
      this.$store.dispatch('deleteOrder', this.order)
    }
  }
}
</script>

<style>
</style>