<template>
  <div class="border">
    <h2>{{ msg }}</h2>
    <br>
    <h3>{{ msg2 }}</h3>
    <div>
      <button :class="{btn:true, red:isRed, blue:isBlue }" v-for="(time,index) in times" :key="index" @click="pick(time)">{{ time }}</button>
    </div>
    
    <br>

    <hr width="400px" size="5px" color="black">

    <br>
    <div>
      선택시간: {{ pickData }}
    </div>

  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String,
    msg2: String,
  
  },
  data: function() {
    return{
      pickData:[],
      pickCnt: 0,
      isRed : false,
      isBlue : true,
      times: [
  "09:00","09:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30",
  "14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30","18:00","18:30",
  "19:00","19:30","20:00","20:30","21:00","21:30","22:00","22:30","23:00","23:30",
],
    }
  },
  methods: {
    pick(picked){
      // console.log(picked)
      console.log(this.pickData.includes(picked))
      console.log(!this.pickData.includes(picked))
      if(this.pickData.includes(picked)){
        for(let i = 0; i < this.pickData.length; i++) {
          if(this.pickData[i] === picked)  {
            this.pickData.splice(i, 1);
            i--;
            
          }
        }
        this.pickCnt -= 1
      }else if(!this.pickData.includes(picked) && this.pickCnt < 6){
        
        this.pickCnt += 1
        this.pickData.push(picked)
        this.isBlue = !this.isBlue
        this.isRed = !this.isRed

      } else if (this.pickCnt > 4) {
        alert('5개 이하만 선택해')
        
        
      }

    }
    

  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
  .border {
    border: solid;
    height: 600px;
    width: 600px;
    margin: auto;
    text-align: center;
  }
  .btn {
    float: left;
    border: solid thin;
    width: 70px;
    margin: 20px;
  }
  .blue{
    background-color: rgb(94, 178, 247);
  }

  .red{
    background-color: rgb(255, 106, 106);
  }

</style>
