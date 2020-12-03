<script>
import { Bar } from "vue-chartjs";

export default {
  extends: Bar,
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