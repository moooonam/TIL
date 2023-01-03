import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import HelloView from '@/views/HelloView'
import LoginView from '@/views/LoginView'
import NotFound404 from '@/views/NotFound404'
import DogView from '@/views/DogView'

Vue.use(VueRouter)
const isLoggedIn = true
const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    // lazy-loading 방식 (첫 로딩에 렌더링 하지않고 해당 라우터가 동작할 때 컴포넌트를 렌더링 한다.)
    path: '/about',
    name: 'about',
    component: () => import('../views/AboutView.vue')
  },
  {
    path: '/hello/:userName',
    name: 'hello',
    component: HelloView,
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView,
    beforeEnter(to, from, next){
      if(isLoggedIn === true){
        console.log('이미 로그인함')
        alert('이미 로그인했자나')
        next({name: 'home'})
      } else{
        next()
      }
    }
  },
  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404,
  },
  {
    path: '/dog/:breed',
    name: 'dog',
    component: DogView
  },
  {
    path: '*',
    redirect: '/404',
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

// router.beforeEach((to, from, next) => {
//   const isLoggedIn = false
//   const authPages = ['hello']
//   const isAuthRequired = authPages.includes(to.name)

//   if (isAuthRequired && !isLoggedIn) {
//     alert('로그인해!')
//     next({ name: 'login'})
//   } else {
//     next()
//   }
// })

export default router
