<template>
  <img alt="Vue logo" src="./assets/logo.png">
<!--  <HelloWorld msg="Welcome to Your Vue.js App"/>-->
  <Project></Project>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import Project from './components/my-first-vue-project.vue'

export default {
  name: 'App',
  components: {
    // HelloWorld
    Project
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
