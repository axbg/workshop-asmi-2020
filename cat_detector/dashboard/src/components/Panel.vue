<template>
  <div class="panel-container">
    <h2>Cat Observer</h2>
    <div class="range-container">
      <p>Change the number of observed days</p>
      <md-field class="md-custom-field">
        <label>Day</label>
        <md-input
          class="md-custom-input"
          min="1"
          max="365"
          v-model="range"
          type="number"
        ></md-input>
      </md-field>
      <md-button class="md-custom-button md-raised" @click="this.rangeChanged"
        >Ok</md-button
      >
    </div>
    <div class="date-container">
      <p>Observe a specific date</p>
      <date-picker
        v-model="date"
        valueType="format"
        placeholder="Select a date"
        @input="this.dateChanged"
      ></date-picker>
    </div>
  </div>
</template>

<script>
import DatePicker from "vue2-datepicker";
import "vue2-datepicker/index.css";

export default {
  name: "Panel",
  components: {
    DatePicker,
  },
  data() {
    return {
      date: null,
      range: 10,
    };
  },
  methods: {
    rangeChanged() {
      if (this.range < 1 || this.range > 365) {
        this.range = 10;
        alert("Allowed range is between 1 and 365");
        return;
      }

      this.$emit("range-changed", this.range);
    },
    dateChanged() {
      if (this.date != null) {
        this.$emit("date-changed", this.date.split("-"));
      }
    },
  },
};
</script>

<style scoped>
.panel-container {
  height: 100%;
  background-color: #e6ceff;
  text-align: center;
  box-sizing: border-box;
  padding: 50px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.12), 0 1px 2px rgba(0, 0, 0, 0.24);
}

.md-custom-button {
  background-color: #b39ddb !important;
  padding: 10px;
}

.md-custom-field {
  margin: 0 auto;
  width: 20%;
  display: inline-block;
}

.md-custom-input {
  width: 100%;
}

.range-container {
  margin-top: 10vh;
}

.date-container {
  margin-top: 10vh;
}
</style>