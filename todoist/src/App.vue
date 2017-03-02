<template>
    <v-app sidebar-under-toolbar id="app">
        <v-toolbar>
            <v-toolbar-side-icon @click.native.stop="nav = !nav" />
            <v-toolbar-title>Todoist</v-toolbar-title>
        </v-toolbar>
        <main>
            <v-content>
                <v-sidebar left fixed drawer v-model="nav">
                    <v-list>
                        <v-list-item>
                            <v-list-tile>
                                <v-list-tile-title>Home</v-list-tile-title>
                            </v-list-tile>
                        </v-list-item>
                    </v-list>
                </v-sidebar>
                <v-container fluid>
                    <router-view></router-view>
                </v-container>
            </v-content>
        </main>
        <v-footer>Copyleft 2017</v-footer>
    </v-app>
</template>

<script>
  export default {
    name: 'app',
    data () {
      return {
        nav: false
      }
    }
  }
  </script>

<style>
#app {
      font-family: 'Avenir', Helvetica, Arial, sans-serif;
  }
  </style>
