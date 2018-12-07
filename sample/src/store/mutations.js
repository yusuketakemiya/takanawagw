// export const STORAGE_KEY = 'todos-vuejs'

// // for testing
// if (navigator.userAgent.indexOf('PhantomJS') > -1) {
//   window.localStorage.clear()
// }

export default {
  updateMessageTitle (state, title) {
    state.station.title = title
  },
  updateMessageSubTitle (state, subtitle) {
    state.station.subTitle = subtitle
  },
  updateMessageEnglishTitle (state, englishtitle) {
    state.station.englishTitle = englishtitle
  }
  // removeTodo (state, todo) {
  //   state.todos.splice(state.todos.indexOf(todo), 1)
  // },
  // editTodo (state, { todo, text = todo.text, done = todo.done }) {
  //   todo.text = text
  //   todo.done = done
  // }
}
