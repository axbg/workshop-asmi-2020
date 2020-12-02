<script>
import { Line } from "vue-chartjs";

export default {
  extends: Line,
  props: ["labels", "meals"],
  methods: {
    renderCustomChart() {
      this.renderChart({
        labels: this.labels,
        datasets: [
          {
            label: "Meals",
            backgroundColor: "#b39ddb",
            data: this.meals,
          },
        ],
      });
    },
  },
  mounted() {
    this.renderCustomChart();
  },
  watch: {
    meals() {
      this.$data._chart.destroy();
      this.renderCustomChart();
    },
  },
};
</script>

<style>
</style>