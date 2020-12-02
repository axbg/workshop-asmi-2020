<script>
import { Line } from "vue-chartjs";

export default {
  extends: Line,
  props: ["chartdata", "options"],
  mounted() {
    const labels = [
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

    const data = [40, 20, 12, 39, 10, 40, 39, 80, 40, 20, 12, 11];

    this.renderChart({
      labels: labels,
      datasets: [
        {
          label: "Meals",
          backgroundColor: "#b39ddb",
          data: data,
        },
      ],
    });
  },
};
</script>

<style>
</style>