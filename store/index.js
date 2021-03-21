const axios = require('axios')

export const state = () => ({
  url: '',
  title: '',
  trans_title: '',
  summary: '',

  parsed: false,
})

export const mutations = {
  setUrl (state, url) {
    state.url = url
  },
  setTitle (state, title) {
    state.title = title
  },
  setTransTitle (state, transTitle) {
    state.trans_title = transTitle
  },
  setSummary (state, summary) {
    state.summary = summary
  },
  setParsed (state, parsed) {
    state.parsed = parsed
  },
}

export const actions = {
  parse ({ commit, state }) {
    return new Promise((resolve, reject) => {
      commit('setParsed', false)
      commit('setTransTitle', '')
      axios('http://127.0.0.1:5000/parse?url=' + state.url).then((res) => {
        console.log(res)
        commit('setTitle', res.data.title)
        if (res.data.trans_title) {
          commit('setTransTitle', res.data.trans_title)
        }
        commit('setSummary', res.data.summary)
        commit('setParsed', true)
        resolve()
      }).catch(() => {
        reject(new Error('Error parsing!'))
      })
    })
  }
}
