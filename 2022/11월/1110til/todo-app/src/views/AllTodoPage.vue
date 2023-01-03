<template>
  <div>
    <h1>모든 할일</h1>
    <div class="input-group mb-3">
      <span class="input-group-text" @click="createTodo">+</span>
      <div class="form-floating">
        <input
          type="text"
          class="form-control"
          id="floatingInputGroup1"
          placeholder="할 일을 입력하세요"
          v-model.trim="content"
          @keyup.enter="createTodo"
        />
        <label for="floatingInputGroup1">할 일을 입력하세요</label>
      </div>
    </div>
    <hr/>
    <TodoItem v-for="todo in todoList" :key="todo.id" :todo="todo" />
    <div class="purple darken-2 text-center">
      <span class="white--text">Lorem ipsum</span>
    </div>
  </div>
</template>

<script>
import TodoItem from "@/components/TodoItem.vue";

export default {
  name: "AllTodoPage",
  components: {
    TodoItem,
  },
  data () {
    return {
      content: null,
    }
  },
  computed: {
    todoList(){
       return this.$store.state.todo.list
	
    }
  },
  methods: {
    createTodo(){
      if (this.content != null){
        this.$store.dispatch('todo/createTodo', this.content)
      }
      this.content=null
    }
  }
};
</script>
