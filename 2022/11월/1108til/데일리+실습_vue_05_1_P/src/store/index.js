import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    orderList: [],
    menuList: [
      {
        title:'아메리카노',
        price: 4100,
        selected: false,
        image:'https://image.istarbucks.co.kr/upload/store/skuimg/2021/04/[110563]_20210426095937808.jpg'
      },
      {
        title: '카페라떼',
        price: 4600,
        selected: false,
        image: 'https://image.istarbucks.co.kr/upload/store/skuimg/2021/04/[110569]_20210415143035989.jpg'
      },
      {
        title:'자몽허니블랙티',
        price: 5300,
        selected: false,
        image: 'https://image.istarbucks.co.kr/upload/store/skuimg/2021/04/[9200000000190]_20210419131723532.jpg'
      }
    ],
    sizeList: [
      {
        name: 'Tall',
        price: 0,
        selected: true
      },
      {
        name: 'Grande',
        price: 500,
        selected: false
      },
      {
        name: 'Venti',
        price: 1000,
        selected: false
      },
    ],
    optionList: [
      {
        type: '샷',
        price: 500,
        count:0
      },
      {
        type: '바닐라 시럽',
        price: 300,
        count:0
      },
      {
        type: '카라멜 시럽',
        price: 200,
        count:0
      },
    ]
  },
  getters: {
    totalOrderCount(state){
      return state.orderList.length
    },
    totalOrderPrice(state){
      let totalprice = 0
      state.orderList.forEach((order) =>{
        totalprice += order.price
      })
      return totalprice
    }
  },
  mutations: {
    PICK_MENU(state, pickedMenu){
      state.menuList = state.menuList.map((menu) =>{
        if (menu === pickedMenu) {
          menu.selected = !menu.selected
        }
        else {
          menu.selected = false
        }
        return menu
      })
    },
    PICK_SIZE(state, pickedSize){
      state.sizeList = state.sizeList.map((size) =>{
        if (size === pickedSize) {
          size.selected = !size.selected
        }
        else{
          size.selected = false
        }
        return size
      })
    },
    ADD_ORDER(state){
      // console.log(state.menuList)
      let totalPrice = 0
      let pickedMenuPrice = 0
      let pickedMenu = ""
      let pickedSize = ""
      let pickImage = ""
      let pickedOption =[]
      state.menuList.forEach((menu) => {
        if (menu.selected) {
          totalPrice += menu.price
          pickedMenuPrice = menu.price
          pickedMenu = menu.title
          pickImage = menu.image
        }
      }
        )
      if (pickedMenuPrice === 0){
        alert('메뉴를 골라!')
      }
      state.sizeList.forEach((size) => {
        if (size.selected) {
          totalPrice += size.price
          pickedSize = size.name
        }
      })
      if (pickedMenu != "" && pickedSize!= ""){
        state.optionList.forEach((option) =>{
          if (option.count != 0) {
            totalPrice += option.count * option.price
            pickedOption.push({type:option.type, count:option.count})
          }
        })
        console.log(pickedOption)
        state.orderList.push({
          title: pickedMenu,
          size: pickedSize,
          price: totalPrice,
          image: pickImage,
          option: pickedOption 
        })
        state.sizeList.map((size) =>{
          if(size.name === 'Tall'){
            size.selected = true
          }else{
            size.selected = false
          }
        })
        state.menuList.map((menu) =>{
          menu.selected = false
        })
        state.optionList.map((option) =>{
          option.count = 0
        })

      }

      },
      INCREASE(state, pickedoption){
        // console.log(optionType)
        state.optionList.forEach((option) =>{
          if(option.type === pickedoption.type){
            option.count+=1
          }
        })
      },
      DECREASE(state, pickedoption){
        state.optionList.forEach((option) =>{
          if(option.type === pickedoption.type && option.count > 0){
            option.count-=1
          }
        })
      },
      DELETE_ORDER(state, pickedDeleteOrder){
        const index =state.orderList.indexOf(pickedDeleteOrder)
        state.orderList.splice(index,1)
      },
    },
  actions: {
    pickMenu(context, pickedMenu){
      console.log(pickedMenu)
      context.commit('PICK_MENU', pickedMenu)
    },
    pickSize(context, pickedSize){
      context.commit('PICK_SIZE', pickedSize)
    },
    addOrder(context){
      context.commit('ADD_ORDER')
    },
    increase(context, pickedoption){
      context.commit('INCREASE', pickedoption)
    },
    decrease(context, pickedoption){
      context.commit('DECREASE', pickedoption)
    },
    deleteOrder(context, pickedDeleteOrder){
      context.commit('DELETE_ORDER', pickedDeleteOrder)
    }
  },
  modules: {
  }
}
)