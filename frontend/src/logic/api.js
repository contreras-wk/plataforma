import axios from 'axios'
import store from '@/store'

const UNAUTHORIZED = 401
const axiosInstance = axios.create({
  baseURL: 'http://127.0.0.1:8000/api/v1.0/',
  timeout: 180000,
})

axiosInstance.interceptors.request.use(
  config => {
    const con = config
    console.log(store.state.user.token)
    const { token } = store.state.user.token
    if (token != null) {
      con.headers.Authorization = ['Bearer', token].join(' ')
    }
    console.log('[OK] Configuración')
    return con
  },
  error => Promise.reject(error),
)

axiosInstance.interceptors.response.use(
  response => response.data,
  error => {
    console.log(error)
    const { status } = error.response
    if (status === UNAUTHORIZED) {
      store.dispatch('user/setToken', null)
      // add logic and methods for update the token
    }
    return Promise.reject(error)
  },
)

export default () => axiosInstance
