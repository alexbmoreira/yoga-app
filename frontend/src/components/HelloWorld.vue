<template>
  <div class="homepage">
  </div>
</template>

<script>
import posesApi from '../api/poses'

export default {
  name: 'Homepage',
  data() {
    return {
      poses: []
    }
  },
  async mounted() {
    this.poses = await posesApi.getPoses();
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
