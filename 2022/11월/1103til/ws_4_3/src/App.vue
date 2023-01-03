<template>
  <div id="app">
    <header>
      <h1>SSAFY 상담 예약 시스템</h1>
    </header>
    <div class="wrap-components">
      <TimeTable 
      style="flex:1"
      @select-time="appGetTime"
      @select-name="appGetName"
      />
      <MyBookList 
      style="flex:1"
      :selected="selected"/>
    </div>
  </div>
</template>

<script>
import MyBookList from '@/components/MyBookList'
import TimeTable from '@/components/TimeTable'


export default {
  name: 'App',
  components: {
    MyBookList,
    TimeTable,
    
  },
  data(){
    return{
      selected:{
        selectedName:"",
        selectedTime:[],
        selectiedMooTimes:[],
        selectiedSubTimes:[],
      },
    }
  },
  methods: {
    appGetTime(time){
      if (this.selected.selectedName === ""){
        alert('선생님을 선택하세요!!!')
        return
      }
      if (this.selected.selectedTime.includes(time)){
        const time_idx = this.selected.selectedTime.indexOf(time)
        this.selected.selectedTime.splice(time_idx, 1)
        return
      }
      if (this.selected.selectedTime.length >= 5) {
        alert('5까지만 가능')
        return
      }
      if (this.selected.selectedName === '정무남') {
        this.selected.selectiedMooTimes.push(time)
      } else if (this.selected.selectedName === '김송섭') {
        this.selected.selectiedSubTimes.push(time)
      } else {
        return
      }      
      this.selected.selectedTime.sort()
      
    },
    appGetName(name){
      // console.log(name)
      this.selected.selectedName = name
      if (this.selected.selectedName === '정무남') {
        this.selected.selectedTime=this.selected.selectiedMooTimes
        this.selected.selectedTime.sort()
      } else if (this.selected.selectedName === '김송섭') {
        this.selected.selectedTime=this.selected.selectiedSubTimes
        this.selected.selectedTime.sort()
      } else {
        return
      }      
    }

  }
}
</script>

<style>
#app {
  text-align: center;
}
.wrap-components{
  margin: 0px 200px;
  display:flex;
  border: solid;

}
* {font-family: 'Jua', sans-serif;
}
</style>
