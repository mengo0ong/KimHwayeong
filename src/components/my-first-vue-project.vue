<template>
  <div id="app">
    <h1>{{ msgA }}</h1>
    <h1>{{ msgB }}</h1>
    <button @click="changeMessage()">Change Message</button>
  </div>
</template>


<script>
  export default {
    data() {
      return {
        msgA: "Hello Vue 3!"
      };
    },
    methods: {
      changeMessage() {
        this.msgA = "Message changed!";
        this.msgB = 'Changed message B!';
      }
    }
  };
</script>



<style scoped>

</style>