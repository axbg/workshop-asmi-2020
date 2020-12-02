<template>
  <carousel >
    <slide v-for="picture of pictures" v-bind:key="picture">
      <img v-bind:src="picture" class="picture">
    </slide>
  </carousel>
</template>

<script>
import { Carousel, Slide } from "vue-carousel";

export default {
  name: "Gallery",
  props: ["pictures"],
  components: {
    Carousel,
    Slide,
  }
};
</script>

<style scoped>
.picture {
  padding: 5px;
  max-height: 180px;
}
</style>