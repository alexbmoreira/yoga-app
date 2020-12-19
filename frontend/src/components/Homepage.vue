<template>
  <div class="homepage center">
    <div class="container">
      <h1>Namaste</h1>
      <div class="sequence">
        <div class="sequence-scroll hide-scrollbar">
          <div v-for="(pose, index) in selected" :key="index" class="pose">
            <h2>{{ pose.display_name }}</h2>
          </div>
        </div>
      </div>
      <div class="add-pose">
        <div class="add-pose-option">
          <h3>Add a pose</h3>
          <button @click="dropdown = true" class="add-button center">+</button>
        </div>
        <div v-if="dropdown" class="search">
          <input class="pose-search" type="text" v-model="search_term" />
          <div class="poses-list">
            <div v-for="(pose, index) in searchedPoses" :key="index" class="list-pose">
              <p>{{ pose.display_name }}</p>
              <button @click="addPose(pose)" class="add-button center">+</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import posesApi from "../api/poses";

export default {
  name: "Homepage",
  data() {
    return {
      poses: [],
      selected: [],
      dropdown: false,
      search_term: ""
    };
  },
  methods: {
    addPose(pose) {
      this.selected.push(pose)
    }
  },
  computed: {
    searchedPoses() {
      return this.poses.filter(pose => {
        return pose.display_name.match(this.search_term)
      })
    }
  },
  async mounted() {
    this.poses = await posesApi.getPoses();
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.homepage {
  justify-content: center;
}

.center {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}

.container {
  max-width: 1150px;
}

.pose {
  min-height: 200px;
  height: 200px;
  min-width: 200px;
  width: 200px;
  background-color: #d6d6d6;
  border-radius: 0.5em;
  padding: 10px;
  margin-right: 5px;
  margin-left: 5px;
}

.sequence {
  min-height: 200px;
  min-width: 1150px;
}

.sequence-scroll {
  overflow-x: scroll;
  display: flex;
}
.hide-scrollbar {
  -ms-overflow-style: none; /* IE and Edge */
  scrollbar-width: none; /* Firefox */
}
.hide-scrollbar::-webkit-scrollbar {
  display: none;
}

.add-pose-option {
  display: flex;
  align-items: center;
}

.add-button {
  background-color: #c47777;
  border-radius: 50%;
  height: 20px;
  width: 20px;
  border: 0;
  color: #fff;
  cursor: pointer;
  font-size: 1em;
}

.pose-search {
  height: 2em;
  border-radius: 0.5em;
  width: 100%;
  border: 1px solid #d6d6d6;
  font-size: 1em;
  padding: 0px 5px;
}
.pose-search:focus {
  outline-width: 0;
}

.poses-list {
  max-height: 300px;
  overflow: scroll;
  border: 1px solid #d6d6d6;
  padding: 0px 10px;
  border-radius: 0.5em;
  margin-top: 10px;
}

.list-pose {
  border-bottom: 1px solid #d6d6d6;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.list-pose:nth-last-child(1) {
  border-bottom: 0px solid #d6d6d6;
}
</style>
