// about.vue

<template>
  <b-container id="about">
    <b-row class="justify-content-center">
      <b-col md="9">
        <h1 class="h3 mb-4">
          About
        </h1>
        <p class="font-weight-lighter">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas eget
          pulvinar est. Sed gravida neque justo, pellentesque finibus velit
          scelerisque eu. Curabitur et dolor luctus, convallis magna at, mollis
          purus. Nunc tincidunt risus quis nisl bibendum volutpat. Praesent ut
          tincidunt ex. Interdum et malesuada fames ac ante ipsum primis in
          faucibus. Praesent porta ante id aliquet pretium. Nam sit amet
          malesuada elit. Mauris pharetra lorem in sollicitudin rutrum. Proin
          euismod dolor in enim porta consequat hendrerit quis augue. Phasellus
          commodo purus non aliquam rutrum.
        </p>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
  export default {
    name: "About",
    mounted() {
      document.title = "about - example app";
    },
  };
</script>

<style lang="scss">
</style>
