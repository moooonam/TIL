<template>
  <div class="back">
    <h2>상담 신청 현황</h2>
    <h3>상담 선생님</h3>
    <div>성함:{{ selected.selectedName }} </div>
    <hr>
    <h3>예약 현황</h3>
    <div>시간들: {{ selected.selectedTime }}</div>
    <hr>
    <img src="./../assets/ssafy-logo.png">
  </div>
</template>

<script>
export default {
  name: 'MyBookList',
  props: {
    selected: Object,
  },
  data() {
    return{
     
    }
  },

}
</script>

<style>
.back{
  background-color: rgb(146, 217, 245);
}
</style>