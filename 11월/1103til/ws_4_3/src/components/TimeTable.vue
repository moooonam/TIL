<template>
  <div>
    <h2>예약 페이지</h2>
    <h3>선생님 선택</h3>
    <button class="name-btn" style="margin-right: 60px" @click="selectName('정무남')"> 정무남 </button>
    <button class="name-btn" @click="selectName('김송섭')"> 김송섭 </button>
    <h3>시간 선택</h3>
    <div class="timebox">
      <span class = "btn" v-for="(time, index) in times" 
      :key="index"
      @click="selectTime(time)" 
      >
      {{ time }}
      </span>
    </div>
    <br>
    <button class="name-btn">예약확정</button>
  </div>
</template>

<script>
export default {
  name: 'TimeTable',
  data() {
    return{
      times: [
  "09:00","09:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30",
  "14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30","18:00","18:30",
  "19:00","19:30","20:00","20:30","21:00","21:30","22:00","22:30","23:00","23:30",
  ],
    }
  },
  methods:{
    selectTime(time){
      this.$emit('select-time', time)

    },
    selectName(name){
      this.$emit('select-name', name)
    }
  }


}
</script>

<style>
.btn {
    float: left;
    border: solid thin;
    width: 60px;
    margin: 5px 10px;
    background-color: rgb(146, 217, 245);
}

.name-btn{
  background-color: rgb(146, 217, 245);
  font-size: large;
}

</style>