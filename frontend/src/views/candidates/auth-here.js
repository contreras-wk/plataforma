import crypto from 'crypto'
import oauth1a from 'oauth-1.0a'

const CONSUMERKEY = 'RMu6HpfLnl1B5Fo9atsyNA'
const CONSUMERSECRET = 'OGV-YkjRT1smYlvqaKB1jzpf5pRu4BVbgGRE7reH8c-pkG1OHcKD3mfMDyYAsQFBYdGgaSuNPN_IeR2tABGj5g'
const TOKENKEY = ''
const TOKENSECRET = ''

class Oauth1Helper {
  static getAuthHeaderForRequest(request) {
    const oauth = oauth1a({
      consumer: { key: CONSUMERKEY, secret: CONSUMERSECRET },
      signature_method: 'HMAC-SHA256',
      hash_function(baseString, key) {
        return crypto
          .createHmac('sha256', key)
          .update(baseString)
          .digest('base64')
      },
    })

    const authorization = oauth.authorize(request, {
      key: TOKENKEY,
      secret: TOKENSECRET,
    })

    return oauth.toHeader(authorization)
    // return oauth
  }
}

export default Oauth1Helper
