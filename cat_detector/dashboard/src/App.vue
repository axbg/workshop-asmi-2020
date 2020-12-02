<template>
  <div class="container">
    <div class="content-holder">
      <Chart :styles="myStyles" />
    </div>
    <div class="content-holder">
      <Panel />
    </div>
  </div>
</template>

<script>
import Chart from "./components/Chart";
import Panel from "./components/Panel";

export default {
  name: "App",
  components: {
    Chart,
    Panel
  },
  computed: {
    myStyles() {
      return {
        width: "90%",
      };
    },
  },
};
</script>

<style>
html,
body {
  height: 100%;
  margin: 0;
}

.container {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin: 0 auto;
  text-align: center;
  height: 100%;
  width: 100%;
  display: grid;
  grid-template-columns: 50% 50%;
}

.content-holder {
  height: 100%;
}
</style>
