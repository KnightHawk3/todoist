<template>
    <div id="todo-list">
        <form id='todo-form' v-on:submit.prevent="addTodo">
            <v-text-input 
                id="new-todo" 
                placeholder="What needs to be done?"
                name="new-todo" 
                label="New Todo" 
                v-model="newTodo"
            ></v-text-input>
            <button type="submit" style="display: none">Submit</button>
        </form>
        <ol id="todos" v-if="todos">
            <li v-for="todo in todos">
                <a v-on:click="deleteTodo(todo)"><v-icon v-on:click="deleteTodo(todo)">close</v-icon></a>
                <v-checkbox :label=todo.text class="todo-check" :id="'todo' + todo.id" v-model="todo.done" v-on:input="updateTodo(todo)"></v-checkbox>
            </li>
        </ol>
    </div>
  </template>

<script>
var axios = require('axios')

export default {
  name: 'TodoList',
  data () {
    return {
      todos: [],
      newTodo: ''
    }
  },
  mounted: function () {
    this.$nextTick(function () {
      this.getTodos()
    })
  },
  methods: {
    addTodo: function () {
      if (!this.newTodo) {
        return
      }
      var todo = {
        text: this.newTodo,
        done: false
      }
      axios.post('/api/todo', todo)
      this.newTodo = ''
      this.getTodos()
    },
    getTodos: function () {
      var vm = this
      axios.get('/api/todo').then(function (response) {
        vm.todos = response['data']['objects']
      })
    },
    updateTodo: function (todo) {
      axios.put('/api/todo/' + todo.id, todo)
    },
    deleteTodo: function (todo) {
      axios.delete('/api/todo/' + todo.id)
      this.todos[todo.id]
      for (let i = this.todos.length - 1; i >= 0; i--) {
        if (this.todos[i].id === todo.id) {
          this.todos.splice(i, 1)
        }
      }
      // this.getTodos()
    }
  }
}
  </script>

<style>
  #todo-list {
      padding: 2rem 35%;
  }
  #todos {
      list-style: none;
  }
  #todos > li > div > label {
      display: inline;
  }
  .todo-check {
      display: inline;
  }
  /* Smartphones (portrait) ----------- */
  @media only screen and (max-width : 500px) {
      #todo-list {
          padding: 2rem 10%;
      }
  }
</style>
