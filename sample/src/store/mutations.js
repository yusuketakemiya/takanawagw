// export const STORAGE_KEY = 'todos-vuejs'

// // for testing
// if (navigator.userAgent.indexOf('PhantomJS') > -1) {
//   window.localStorage.clear()
// }

export default {
  updateMessageTitle (state, title) {
    state.station.title.text = title
  },
  updateMessageSubTitle (state, subtitle) {
    state.station.subTitle.text = subtitle
  },
  updateMessageEnglishTitle (state, englishtitle) {
    state.station.englishTitle.text = englishtitle
  },
  updateWindowSize (state, size) {
    state.window.width = size.width
    state.window.height = size.height

    state.station.image.style.width = size.width + 'px'
    state.station.image.style.height = size.height + 'px'
  }
}
