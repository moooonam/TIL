<template>
  <div>
    <h2>2. 사이즈를 고르세요.</h2>
    <SizeListItem
    v-for="(size, index) in sizeList"
    :key="index"
    :size="size"
    />
  </div>
</template>

<script>
import SizeListItem from '@/components/SizeListItem';

export default {
  name: 'SizeList',
  components: {
    SizeListItem
  },
  methods: {
    onSelectMenu: function () {},
  },
  computed: {
    sizeList() {
      return this.$store.state.sizeList
    },
  },
}
</script>

<style>
</style>