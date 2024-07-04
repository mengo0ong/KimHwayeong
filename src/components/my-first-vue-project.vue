<template>
  <div id="app">
    <h1>{{ msgA }}</h1>
    <h1>{{ msgB }}</h1>
    <button @click="changeMessage()">Change Message</button>
  </div>
</template>


<script >
  export default ({
    data() {
      return {
        msgA: "Hello Vue 3!"
      };
    },
    methods: {
      /* 반응형 확인 */
      changeMessage() {
        this.msgA = "Changed message A!";
        this.msgB = 'Changed message B!';
      }
    },
    /* computed: 기존에 정의했던 데이터를 추가적으로 계산해서 렌더링 됨 */
    computed: {},
    /* 데이터 반응을 관찰 -> 설정한 데이터가 변경될 때 마다 실행함 */
    watch: {
      msgA(value){ // msgA가 변경될 때마다 그 값을 콘솔에 표기한다.
        console.log(value)
      }
    },
    /* 라이프 사이클 */
    created() {

    },
    mounted(){

    }
  });
</script>

<style scoped>

</style>