<template>
  <!-- <div class="main" v-bind:style="{ 'background-image': 'url(' + image + ')' }"> -->
  <div class="main">
    <div id="edit" ref="edit">
      <img id="image" :src="image" v-bind:style="imageStyle"/>
      <input id="title" v-model="stationTitle" v-bind:style="titleStyle" />
      <input id="subTitle"  v-model="stationSubTitle" v-bind:style="subTitleStyle" />
      <input id="englishTitle" v-model="stationEnglishTitle" v-bind:style="englishTitleStyle" />
      <label id="title" v-bind:style="titleStyle" >{{stationTitle}}</label>
      <label id="subTitle" v-bind:style="subTitleStyle">{{stationSubTitle}}</label>
      <label id="englishTitle" v-bind:style="englishTitleStyle">{{stationEnglishTitle}}</label>
    </div>
    <div id="container">
      <button @click="print">print</button>
      <br/>
      <label id="width">{{width}}</label>
      <br/>
      <label id="height">{{height}}</label>
      <!-- <img :src="output"> -->
    </div>
  </div>
</template>

<script>
import store from '../store'

export default {
  name: 'Main',
  data () {
    this.handleResize()
    return {
      image: store.state.station.image.src
    }
  },
  computed: {
    stationTitle: {
      get () {
        return store.state.station.title.text
      },
      set (value) {
        store.commit('updateMessageTitle', value)
      }
    },
    stationSubTitle: {
      get () {
        return store.state.station.subTitle.text
      },
      set (value) {
        store.commit('updateMessageSubTitle', value)
      }
    },
    stationEnglishTitle: {
      get () {
        return store.state.station.englishTitle.text
      },
      set (value) {
        store.commit('updateMessageEnglishTitle', value)
      }
    },
    width: {
      get () {
        return store.state.window.width
      }
    },
    height: {
      get () {
        return store.state.window.height
      }
    },
    imageStyle: {
      get () {
        return store.state.station.image.style
      }
    },
    titleStyle: {
      get () {
        return store.state.station.title.style
      }
    },
    subTitleStyle: {
      get () {
        return store.state.station.subTitle.style
      }
    },
    englishTitleStyle: {
      get () {
        return store.state.station.englishTitle.style
      }
    }
  },
  methods: {
    print () {
      const el = document.querySelector('#edit')
      this.$html2canvas(el).then(canvas => {
        let imageData = canvas.toDataURL('image/png')

        var a = document.createElement('a')
        a.href = imageData
        a.download = this.$store.getters.theme + '.png'
        document.body.appendChild(a)
        a.click()
        document.body.removeChild(a)
      })
    },
    handleResize () {
      let width = window.innerWidth
      let height = window.innerHeight
      store.commit('updateWindowSize', { width, height })
    }
  }
  // mounted: function () {
  //   window.addEventListener('resize', this.handleResize)
  // }
  // beforeDestroy: function () {
  //   window.removeEventListener('resize', this.handleResize)
  // }
}
</script>

<style scoped>
#image {
  z-index: -1;
  background-size: contain;
  background-color: #ccc;
  background-position: center center;
  background-repeat: no-repeat;
}
#container {
  position: absolute;
  top: 90%;
}
.main {
  position: relative;
  width: 100%;
  height: 100%;
  background-repeat: no-repeat;
  background-size: contain;
}
input {
  position: absolute;
  opacity: 0;
  font-weight: bold;
  text-align: center;
}
label {
  position: absolute;
  opacity: 1;
  font-weight: bold;
  text-align: center;
}
input:hover {
  opacity: 1;
  z-index: 1;
}
label:hover {
  opacity: 0;
  z-index: -1;
}
#title {
  font-size: 60px;
}
#subTitle {
  font-size: 30px;
}
#englishTitle {
  font-size: 32px;
}
</style>
