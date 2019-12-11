<template>

  <div>

    <header>header</header>

    <main >
      <router-view />
    </main>

    <footer>footer</footer>

  </div>

</template>

<script>
  export default {
    components: { }
  };
</script>

<style lang="scss">

  // import custom bootstrap theme and base styling for app
  @import '../css/_variables.scss';
  @import '../css/custom.scss';
  @import '../css/base.scss';

</style>
