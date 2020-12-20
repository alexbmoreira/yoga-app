<template>
  <div class="homepage center">
    <div class="container">
      <h1>Namaste</h1>
      <div class="sequence">
        <div class="sequence-scroll hide-scrollbar">
          <div v-for="(pose, index) in selected" :key="index" class="sequence-chunk">
            <i v-if="index > 0" class="fas fa-angle-double-right"></i>
            <div class="card center">
              <div class="pose center">
                <button @click="removePose(pose)" class="small-button bg-grey close center">
                  <i class="fas fa-times"></i>
                </button>
                <img class="pose-image" :src="getPoseImage(pose)">
              </div>
              <h2>{{ pose.display_name }}</h2>
            </div>
          </div>
        </div>
      </div>
      <div class="add-pose">
        <div class="add-pose-option">
          <h3 class="mr">Add a pose</h3>
          <button @click="dropdown = !dropdown" class="small-button center">
            <i v-if="dropdown == false" class="fas fa-chevron-down"></i>
            <i v-if="dropdown" class="fas fa-chevron-up"></i>
          </button>
        </div>
        <div v-if="dropdown" class="search">
          <input class="pose-search" type="text" v-model="search_term" placeholder="Search for a pose..." />
          <div class="poses-list hide-scrollbar">
            <div v-for="(pose, index) in searchedPoses" :key="index" class="list-pose">
              <p>{{ pose.display_name }}</p>
              <button @click="addPose(pose)" class="small-button center"><i class="fas fa-plus"></i></button>
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
    },
    removePose(pose) {
      var index = this.selected.indexOf(pose)
      this.selected.splice(index, 1)
    },
    getPoseImage(pose) {
      try {
        return require(`../assets/pose_images/${pose.base_name}_L-tnbig.png`)
      }
      catch(ex) {
        return null
      }
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

.mr {
  margin-right: 10px;
}

.container {
  max-width: 1090px;
}

.fa-angle-double-right {
  font-size: 3em;
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
  position: relative;
}

.sequence {
  min-height: 270px;
  min-width: 1090px;
}

.sequence-chunk {
  display: flex;
  align-items: center;
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

.small-button {
  background-color: #c47777;
  border-radius: 50%;
  height: 20px;
  width: 20px;
  border: 0;
  color: #fff;
  cursor: pointer;
}
.bg-grey {
  background-color: #7a7a7a;
}
.close {
  position: absolute;
  top: 10px;
  right: 10px;
}

.pose-image {
  max-width: 100%;
  max-height: 100%;
}

.pose-search {
  height: 2em;
  border-radius: 0.5em;
  border: 1px solid #d6d6d6;
  font-size: 1em;
  padding: 0px 5px;
  width: 100%;
}
.pose-search:focus {
  outline-width: 0;
}

.poses-list {
  max-height: 375px;
  overflow: scroll;
  border: 1px solid #d6d6d6;
  padding: 0px 10px;
  border-radius: 0.5em;
  margin-top: 10px;
  width: 100%;
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
