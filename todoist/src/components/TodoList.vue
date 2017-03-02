<template>
    <div>
        <input class="new-todo" autofocus autocomplete="off" placeholder="What needs to be done?" v-model="newTodo" @keyup.enter="addTodo">
        <ol v-if="todos">
            <li v-for="todo in todos">
                <input type="checkbox" id="checkbox" v-on:click="updateTodo(todo)" v-model="todo.done">
                {{ todo.text }}
                <i v-on:click="deleteTodo(todo)"> ✖ </i>
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
      axios.post('http://localhost:5000/api/todo', todo)
      this.newTodo = ''
      this.getTodos()
    },
    getTodos: function () {
      var vm = this
      axios.get('http://localhost:5000/api/todo').then(function (response) {
        vm.todos = response['data']['objects']
      })
    },
    updateTodo: function (todo) {
      axios.put('http://localhost:5000/api/todo/' + todo.id, todo)
    },
    deleteTodo: function (todo) {
      axios.delete('http://localhost:5000/api/todo/' + todo.id)
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
</style>
