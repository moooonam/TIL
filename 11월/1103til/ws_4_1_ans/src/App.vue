<template>
  <div id="app">
    <header>
      <h1>SSAFY 상담 예약 시스템</h1>
    </header>
    <div style=" display:flex">
      <section style="margin: 0px 80px;">
          <div>
            <h2>예약 페이지</h2>
            <h3>선생님 선택</h3>
            <button class="name-btn" style="margin-right: 30px" 
            @click="selectName('정무남')"
            :class="{'selected-btn': isSelectedName('정무남')}"
            >정무남</button>
            <button class="name-btn" @click="selectName('김송섭')" :class="{'selected-btn': isSelectedName('김송섭')}">김송섭</button>
            <h3>시간 선택</h3>
            <div class="timebox">
              <span class = "btn" v-for="(time, index) in times" 
              :key="index" 
              @click="selectTime(time)"
              :class="{'selected-btn': isSelected(time)}"
              >
              {{ time }}
            </span>
          </div>
        </div>
      </section>
      <section>
        <div>
          <h2>상담 신청 현황</h2>
          <h3>상담 선생님</h3>
          <div>성함: {{ selectedName }}</div>
          <hr>
          <h3>예약 현황</h3>
          <div>시간들: {{ changed }}</div>
          <img src="./assets/ssafy-logo.png" width="400" height="300">
          <!-- <div class="timebox">

          </div> -->

        </div>
      </section>
    </div>
  </div>
</template>

<script>

export default {
  name: 'App',
  components: {
  },
  data(){
    return{
      selectedTimes: [],
      selectiedMooTimes:[],
      selectiedSubTimes:[],
      selectedName: "",
      times: [
  "09:00","09:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30",
  "14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30","18:00","18:30",
  "19:00","19:30","20:00","20:30","21:00","21:30","22:00","22:30","23:00","23:30",
  ],
    }
  },
  computed: {
    changed() {
      let timeString = ""
      this.selectedTimes.forEach((time)=>{
        timeString += time + " "
      })
      return timeString
    }
  },
  methods: {
    selectTime(time){
      if (this.selectedName === ""){
        alert('선생님을 선택하세요!!!')
        return
      }
      if (this.selectedTimes.includes(time)){
        const time_idx = this.selectedTimes.indexOf(time)
        this.selectedTimes.splice(time_idx, 1)
        return
      }
      if (this.selectedTimes.length >= 5) {
        alert('5까지만 가능')
        return
      }
      this.selectedTimes.push(time)
      // console.log(time)
    },
    isSelected(time) {
      if (this.selectedTimes.includes(time)){
        return true
      } else {
        return false
      }
    },
    isSelectedName(name){
      if (this.selectedName=== name){
        return true
      } else {
        return false
      }
    },
    selectName(name){
      this.selectedName = name
      // console.log(name)
      if (this.selectedName === '정무남') {
        this.selectedTimes=this.selectiedMooTimes
      } else if (this.selectedName === '김송섭') {
        this.selectedTimes=this.selectiedSubTimes
      } else {
        return
      }      
    }
  }
}
</script>

<style>
#app {
  min-width: 900px;
  text-align: center;
}

.btn {
    float: left;
    border: solid thin;
    width: 70px;
    margin: 20px;
    background-color: aquamarine;
}
.name-btn{
  background-color: rgb(236, 252, 236);
}
.selected-btn{
  background-color: rgb(240, 119, 119);
  border: 1px solid black;
}
.selected-name{
  background-color: rgb(106, 248, 153);
  border: 1px solid black;
}

.timebox {
    border: solid;
    height: 400px;
    width: 600px;
    margin: auto;
    text-align: center;
  }
* {font-family: 'Nanum Pen Script', cursive;
  }  
</style>
