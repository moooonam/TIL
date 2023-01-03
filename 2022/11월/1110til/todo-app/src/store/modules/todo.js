const state = () => {
    return {
          // todo 리스트 Array
      list: [
              // 개별 todo Object
        {
          id: 1638771553377,                // nowDateObj.getTime()
          content: 'Vue',                   // Todo 내용
          dueDateTime: '2021-12-09T00:00',  // 마감일
          isCompleted: false,               // 완료된 할 일
          isImportant: true,				        // 중요 할 일
        },
        {
          id: 1638771553378,
          content: 'Vue Router',
          dueDateTime: '2021-12-10T00:00',
          isCompleted: false,
          isImportant: true,
        },
        {
          id: 16387715533779,
          content: 'Vuex',
          dueDateTime: '2021-12-11T00:00',
          isCompleted: true,
          isImportant: false,
        },
      ],
    }
  }

const getters = {}


const mutations = {
	PICK_IMPORTANT(state, pickedTodo){
		state.list.forEach((todo)=> {
			if (todo === pickedTodo){
				todo.isImportant =!todo.isImportant
			}
		}
		)
	},
	CREATE_TODO(state, newtodo){
		state.list.push(newtodo)
	},
	CHECK_COMPLETED(state, checkedTodo){
		state.list.forEach((todo)=> {
			if (todo === checkedTodo){
				todo.isCompleted =!todo.isCompleted
			}})
	},
	EDIT_TODO(state, pickedContent){
		state.list.forEach((todo)=> {
			if (todo === pickedContent.myTodo){
				todo.content = pickedContent.content
			}})
	}
}


const actions = {
  pickImportant(context, pickedTodo){
		context.commit('PICK_IMPORTANT', pickedTodo)
	},
	createTodo(context, newContent){
		const myDate = new Date()
		myDate.setHours(23,59,59,59)
		const todo ={
			id: new Date().getTime(),
			content: newContent,
			dueDateTime: `${myDate.getFullYear()}-${myDate.getMonth()+1}-${myDate.getDate()+1}T00:00`,
			isCompleted: false,
			isImportant: false,
		}
		context.commit("CREATE_TODO", todo)
	},
	createImportantTodo(context, newContent){
		const myDate = new Date()
		myDate.setHours(23,59,59,59)
		const todo ={
			id: new Date().getTime(),
			content: newContent,
			dueDateTime: `${myDate.getFullYear()}-${myDate.getMonth()+1}-${myDate.getDate()+1}T00:00`,
			isCompleted: false,
			isImportant: true,
		}
		context.commit("CREATE_TODO", todo)
	},
	checkCompleted(context, checkedTodo){
		context.commit("CHECK_COMPLETED",checkedTodo )
	},
	editTodo(context, pickedContent){
		context.commit("EDIT_TODO", pickedContent)
	}

}

export default {
    namespaced:true,
    state,
    getters,
    mutations,
    actions,
}