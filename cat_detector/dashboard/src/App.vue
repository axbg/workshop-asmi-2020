<template>
  <div class="container">
    <div class="content-holder">
      <Chart :styles="chartStyle" :labels="labels" :meals="meals" />
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
  data() {
    return {
      labels: [],
      meals: [],
    };
  },
  components: {
    Chart,
    Panel,
  },
  mounted() {
    this.labels = [
      "January",
      "February",
      "March",
      "April",
      "May",
      "June",
      "July",
      "August",
      "September",
      "October",
      "November",
      "December",
    ];

    this.meals = [40, 20, 12, 39, 10, 40, 39, 80, 40, 20, 12, 11];
  },
  computed: {
    chartStyle() {
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
