// home.vue

<template>
  <b-container id="home">
    <hello-world />
    <p>welcome to my example app!</p>
  </b-container>
</template>

<script>
  import HelloWorld from "../components/hello-world.vue";

  export default {
    name: "Home",
    components: {
      "hello-world": HelloWorld
    },
    data() {
      return { };
    },
    mounted() {
      document.title = "home - example app";
    },
    methods: {}
  };
</script>

<style lang="scss">
</style>
