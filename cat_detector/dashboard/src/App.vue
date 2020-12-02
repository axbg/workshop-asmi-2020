<template>
  <div class="container">
    <div class="content-holder">
      <Chart :styles="chartStyle" :labels="labels" :meals="meals" />
    </div>
    <div class="content-holder">
      <Panel
        v-on:range-changed="this.handleRangeUpdated"
        v-on:date-changed="this.handleDateUpdated"
      />
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
    this.dayLabels = [
      0,
      1,
      2,
      3,
      4,
      5,
      6,
      7,
      8,
      9,
      10,
      11,
      12,
      13,
      14,
      15,
      16,
      17,
      18,
      19,
      20,
      21,
      22,
      23,
    ];

    this.clearData();
    this.handleRangeUpdated(10);
  },
  methods: {
    clearData() {
      this.labels = [];
      this.meals = [];
    },
    async handleRangeUpdated(range) {
      const response = await fetch(`http://localhost:5000/data?days=${range}`);
      const data = await response.json();

      this.clearData();

      data.map((entry) => {
        this.labels.push(entry[0]);
        this.meals.push(entry[1]);
      });
    },
    async handleDateUpdated(date) {
      const response = await fetch(
        `http://localhost:5000/detail?year=${date[0]}&month=${date[1]}&day=${date[2]}`
      );

      const data = await response.json();
      const emptyDay = Array.apply(null, Array(24)).map(
        Number.prototype.valueOf,
        0
      );
      data.map((entry) => (emptyDay[entry[0]] = entry[1]));

      this.clearData();

      this.labels = this.dayLabels;
      this.meals = emptyDay;
    },
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
  grid-template-columns: 50% 1fr;
}

.content-holder {
  height: 100%;
}
</style>
