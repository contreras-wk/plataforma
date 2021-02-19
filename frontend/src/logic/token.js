import API from '@/logic/api'

export default {

  token(args) {
    return API().post('token/', args)
  },

}
