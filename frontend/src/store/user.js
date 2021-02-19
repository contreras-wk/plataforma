const user = {
  namespaced: true,
  state: {
    isAuthenticated: false,
    token: null,
    refresh: null,
  },
  getters: {
    getToken(state) {
      return state.token
    },
    isLogged(state) {
      return state.isAuthenticated
    },
  },
  mutations: {
    setToken(state, payload) {
      state.token = payload
      state.isAuthenticated = true
    },
    setRefresh(state, payload) {
      state.refresh = payload
    },
    logout(state) {
      state.token = null
      state.refresh = null
      state.isAuthenticated = false
    },
  },
  actions: {
    setToken(commit, payload) {
      commit('setToken', payload)
    },
    setRefresh({ commit }, payload) {
      commit('setRefresh', payload)
    },
    logout({ commit }) {
      commit('logout')
    },
  },
}

export default user
