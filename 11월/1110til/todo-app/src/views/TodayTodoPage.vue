<template>
  <div>
    <h1>오늘 할일</h1>
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
    <hr />
    <TodayTodoItem v-for="todo in todoList" :key="todo.id" :todo="todo" />
  </div>
</template>

<script>
import TodayTodoItem from "@/components/TodayTodoItem";
export default {
  name: "TodayTodoPage",
  components: {
    TodayTodoItem,
  },
  data() {
    return {
      content: null,
    };
  },
  computed: {
    todoList() {
      const myDate = new Date()
      const today =`${myDate.getFullYear()}-${myDate.getMonth()+1}-${myDate.getDate()+1}T00:00`
      const todayTodo = this.$store.state.todo.list.filter((todo) => {
        return !todo.isCompleted && todo.dueDateTime===today
      });
      return todayTodo;
    },
  },
  methods: {
    createTodo() {
      if (this.content != null) {
        this.$store.dispatch("todo/createTodo", this.content);
      }
      this.content = null;
    },
  },
};
</script>

<style>
</style>