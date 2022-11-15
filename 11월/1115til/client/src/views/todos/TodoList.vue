<template>
  <div>
    <ul>
      <li v-for="todo in todos" :key="todo.id">
        <span 
          @click="updateTodoStatus(todo)" 
          :class="{ 'is-completed': todo.is_completed }"
        >
        {{ todo.title }}
        </span>
        <button @click="deleteTodo(todo)" class="todo-btn">X</button>
      </li>
    </ul>
    <button @click="getTodos">Get Todos</button>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'TodoList',
  data: function () {
    return {
      todos: null,
    }
  },
  created(){
    this.getTodos()
  },
  methods: {
    getTodos: function () {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/todos/',
      })
        .then(res => {
          // console.log(res)
          this.todos = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },
    deleteTodo: function (todo) {
      const id = todo.id
      axios({
        method: 'DELETE',
        url: `${API_URL}/todos/${id}/`,
        headers:{
          Authorization: `Bearer ${window.localStorage.getItem('jwt')}`
        }
      })
      // .then(() =>{
      //   this.$router.push({ name: 'TodoList' })
      // })
      .then(() => {
        this.getTodos()
      })
    },
    updateTodoStatus: function (todo) {
      const id = todo.id
      const title = todo.title
      const is_completed = !todo.is_completed
      axios({
        method: 'PUT',
        url: `${API_URL}/todos/${id}/`,
        data:{title,is_completed},
        headers:{
          Authorization: `Bearer ${window.localStorage.getItem('jwt')}`
        }
      })
      .then(() => {
        this.getTodos()
      })
    },
  },
}
</script>

<style scoped>
  .todo-btn {
    margin-left: 10px;
  }

  .is-completed {
    text-decoration: line-through;
    color: rgb(112, 112, 112);
  }
</style>
