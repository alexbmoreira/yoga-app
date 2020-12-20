<template>
  <div id="app">
    <Homepage msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
import Homepage from './components/Homepage'

export default {
  name: 'App',
  components: {
    Homepage
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
}
</style>
