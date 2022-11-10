<template>
  <div>
		<div class="todo-box my-3 d-flex justify-content-between" @click="goEdit">
			<div id="checkcheck">
				<input class="form-check-input mx-2" type="checkbox" value="" id="flexCheckDefault" v-if="todo.isCompleted" checked @click="checkCompleted">
				<input class="form-check-input mx-2" type="checkbox" value="" id="flexCheckDefault" v-if="!todo.isCompleted" @click="checkCompleted">
				{{ todo.content }}
			</div>
			<div @click="pickImportant">
				<i class="bi bi-star" v-if="!todo.isImportant " style="color:orange"></i>
				<i class="bi bi-star-fill" v-if="todo.isImportant" style="color:orange"></i>
			</div>

		</div>
		<div class="todo-box2" v-if="editmode">
			<input type="text" 
			style="border-radius: 10px; width: 500px;"
			v-model.trim="editcontent" @keyup.enter="editTodo">
			<button type="button" class="btn btn-success" @click="editTodo">수정하기</button>
		</div>
  </div>
</template>

<script>
export default {
	name: 'TodoItem',
	props: {
		todo: Object,
	},
	data(){
		return{
			editmode: false,
			editcontent:null,
		}
	},
	methods:{
		pickImportant(event){
			event.stopPropagation()
			this.$store.dispatch('todo/pickImportant', this.todo)
		},
		checkCompleted(event){
			event.stopPropagation()
			this.$store.dispatch('todo/checkCompleted', this.todo)
		},
		editTodo(){

			this.$store.dispatch('todo/editTodo', {myTodo:this.todo,content:this.editcontent})
			this.editcontent = null
		},
		goEdit(){
			this.editmode = !this.editmode
		}
	},
}
</script>

<style>
.todo-box{
	border: solid black 1px;
	border-radius: 10px;
	padding: 15px;
}
.todo-box2{
	border: solid black 1px;
	border-radius: 10px;
	padding: 15px;
	height: 100px;
	background-color: rgb(177, 245, 245);
}

</style>