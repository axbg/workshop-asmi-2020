<template>
  <div class="panel-container">
    <h2>Cat Observer</h2>
    <div class="content-container">
      <p>Change the number of observed days</p>
      <md-field class="md-custom-field">
        <label>Days</label>
        <md-input
          class="md-custom-input"
          min="1"
          max="365"
          v-model="range"
          type="number"
        ></md-input>
      </md-field>
      <md-button
        class="md-custom-button md-raised"
        :md-ripple="false"
        @click="this.rangeChanged"
        >Ok</md-button
      >
    </div>
    <div class="content-container">
      <p>Observe a specific date</p>
      <date-picker
        v-model="date"
        valueType="format"
        placeholder="Select a date"
        @input="this.dateChanged"
      ></date-picker>
    </div>
    <div class="content-container">
      <p>Last pictures</p>
      <Gallery :pictures="pictures" />
    </div>
  </div>
</template>

<script>
import DatePicker from "vue2-datepicker";
import "vue2-datepicker/index.css";
import Gallery from "./Gallery";

export default {
  name: "Panel",
  props: ["pictures"],
  components: {
    DatePicker,
    Gallery,
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

.content-container {
  width: 100%;
  margin-top: 7vh;
}
</style>