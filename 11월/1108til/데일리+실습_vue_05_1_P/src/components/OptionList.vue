<template>
  <div>
    <h2>3. 옵션을 고르세요.</h2>
    <OptionListItem
      v-for="(option,index) in optionList"
      :key="index"
      :option="option"
    />
  </div>
</template>

<script>
import OptionListItem from '@/components/OptionListItem'

export default {
  name: 'OptionList',
  components: {
    OptionListItem,
  },
  computed: {
    optionList() {
      return this.$store.state.optionList
    },
  },
  // methods: {
  //   increase: function () {
  //   },
  //   decrease: function () {
  //   },
  // },
}
</script>

<style>
</style>