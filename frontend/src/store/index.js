import Vue from 'vue'
import Vuex from 'vuex'

import createPersistedState from 'vuex-persistedstate'

// Modules
import app from './app'
import appConfig from './app-config'
import verticalMenu from './vertical-menu'
import user from './user'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    app,
    appConfig,
    verticalMenu,
    user,
  },
  plugins: [createPersistedState(
    {
      key: 'unipoooool',
    },
  )],
  strict: process.env.DEV,
})
