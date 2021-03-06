import axios from '@axios'
import useJwt from '@/auth/jwt/useJwt'

export default {
  namespaced: true,
  state: {},
  getters: {},
  mutations: {},
  actions: {
    fetchCandidates(queryParams) {
      return new Promise((resolve, reject) => {
        console.log('>>>>>>>>>>>>>>>>>>>>>>')
        console.log(queryParams)
        useJwt.getCandidates(queryParams)
          .then(response => resolve(response))
          .catch(error => reject(error))
      })
    },
    fetchCandidate() {
      return new Promise((resolve, reject) => {
        useJwt.getCandidate(15)
          .then(response => resolve(response))
          .catch(error => reject(error))
      })
    },
    fetchInvoices(ctx, queryParams) {
      return new Promise((resolve, reject) => {
        axios
          .get('/apps/invoice/invoices', { params: queryParams })
          .then(response => resolve(response))
          .catch(error => reject(error))
      })
    },
    fetchInvoice(ctx, { id }) {
      return new Promise((resolve, reject) => {
        axios
          .get(`/apps/invoice/invoices/${id}`)
          .then(response => resolve(response))
          .catch(error => reject(error))
      })
    },
    fetchClients() {
      return new Promise((resolve, reject) => {
        axios
          .get('/apps/invoice/clients')
          .then(response => resolve(response))
          .catch(error => reject(error))
      })
    },
    // addUser(ctx, userData) {
    //   return new Promise((resolve, reject) => {
    //     axios
    //       .post('/apps/user/users', { user: userData })
    //       .then(response => resolve(response))
    //       .catch(error => reject(error))
    //   })
    // },
  },
}
