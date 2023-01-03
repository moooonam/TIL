<template>
   <div>
    <h1> 중요 할일</h1>
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
    <hr>
		<ImportantTodoItem
    v-for="todo in todoList"
    :key="todo.id"
    :todo="todo"
    />
  </div>
</template>

<script>
import ImportantTodoItem from '@/components/ImportantTodoItem.vue';
export default {
	name: 'ImportantTodoPage',
	components:{
		ImportantTodoItem
	},
	data () {
    return {
      content: null,
    }
	},
	computed: {
    todoList(){
      const importentTodo = this.$store.state.todo.list.filter((todo) =>{
				return todo.isImportant && !todo.isCompleted
			})
			return importentTodo
    }
  },
	methods: {
    createTodo(){
      if (this.content != null){
        this.$store.dispatch('todo/createImportantTodo', this.content)
      }
      this.content=null
    }
  },
}
</script>

<style>

</style>