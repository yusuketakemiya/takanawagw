<template>
  <div class="main" v-bind:style="{ 'background-image': 'url(' + image + ')' }">
    <div id="edit" ref="edit">
      <input id="title" v-model="stationTitle" />
      <input id="subTitle"  v-model="stationSubTitle" />
      <input id="englishTitle" v-model="stationEnglishTitle" />
      <label id="title">{{stationTitle}}</label>
      <label id="subTitle">{{stationSubTitle}}</label>
      <label id="englishTitle">{{stationEnglishTitle}}</label>
    </div>
    <div id="container">
      <button @click="print">print</button>
      <img :src="output">
    </div>
  </div>
</template>

<script>
import store from '../store'

export default {
  name: 'Main',
  data () {
    return {
      image: store.state.station.image,
      output: null
    }
  },
  computed: {
    stationTitle: {
      get () {
        return store.state.station.title
      },
      set (value) {
        store.commit('updateMessageTitle', value)
      }
    },
    stationSubTitle: {
      get () {
        return store.state.station.subTitle
      },
      set (value) {
        store.commit('updateMessageSubTitle', value)
      }
    },
    stationEnglishTitle: {
      get () {
        return store.state.station.englishTitle
      },
      set (value) {
        store.commit('updateMessageEnglishTitle', value)
      }
    }
  },
  methods: {
    print () {
      // const el = this.$refs.edit
      // const el = document.querySelector('#edit')
      const el = document.body
      // alert(this.$refs.edi)
      this.$html2canvas(el).then(canvas => {
        // alert(canvas)
        let imageData = canvas.toDataURL('image/png')
        // alert(imageData)
        this.output = imageData
        // document.querySelector('#container').appendChild(canvas)

        var a = document.createElement('a')
        a.href = imageData
        a.download = this.$store.getters.theme + '.png'
        document.body.appendChild(a)
        a.click()
        document.body.removeChild(a)
      })
    }
  }
}
</script>

<style scoped>
canvas {
  width: 100px;
  height: 100px;;
}
#container {
  top: 90%;
}
.main {
  width: 100%;
  height: 100%;
  background-repeat: no-repeat;
  background-size: contain;
}
input {
  opacity: 0;
  font-weight: bold;
  text-align: center;
}
label {
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
  top: 20%;
  left: 15%;
  font-size: 60px;
  width: 68%;
}
#subTitle {
  top: 31%;
  left: 30%;
  font-size: 30px;
  width: 45%;
}
#englishTitle {
  top: 52%;
  left: 32%;
  font-size: 32px;
  width: 45%;
}
</style>
