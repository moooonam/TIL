<template>
  <div class="mx-4">
    <h3>주문 내역</h3>
    <p>총 {{ totalOrderCount }}건: {{ totalOrderPrice }}원 </p>
    <OrderListItem
    v-for="(order, index) in orderList"
    :key="index"
    :order="order"
    />
  </div>
</template>

<script>
import OrderListItem from '@/components/OrderListItem';
export default {
  name: 'OrderList',
  components: {
    OrderListItem 
  },
  computed: {
    orderList() {
      return this.$store.state.orderList
    },
    totalOrderCount() {
      return this.$store.getters.totalOrderCount
    },
    totalOrderPrice(){
      return this.$store.getters.totalOrderPrice
    }
  }
  }

</script>

<style>
</style>