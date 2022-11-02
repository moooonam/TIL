<template>
  <div class = "border">
    <h1>이거는 내가 만든 새로운 컴포넌트다!</h1>
    <MyComponentItem msg="하위 컴포넌트"
    :dynamic-props="dynamicProps"
    @child-to-parent="parentGetEvent"
    @child-input="getDynamicData"
    />
    
  </div>
</template>

<script>
// 1. 불러오기
import MyComponentItem from '@/components/MyComponentItem'
export default {
    name: 'MyComponent' ,
    // 2. 등록하기
    components: {
      MyComponentItem,
    },
    data: function () {
      return{
        dynamicProps: 'It`s in data'
      }
    },
    methods: {
      parentGetEvent: function(inputData) {
        console.log("자식 컴포넌트에서 발생한 이벤트!")
        console.log(`child component로부터 ${inputData}를 받음!`)
      },
      getDynamicData: function(childInputData) {
        console.log(`사용자가 입력한 것은 ${childInputData}입니당`)
      }
    },


}
</script>

<style>
  .border {
    border: solid 1px blue;
  }
</style>