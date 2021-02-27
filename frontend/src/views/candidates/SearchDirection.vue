      codeBasicFormDirection,

<template>
  <b-card-code title="Ajax">
    <vue-autosuggest
      ref="autocomplete"
      v-model="query"
      :suggestions="suggestions"
      :input-props="inputProps"
      :section-configs="sectionConfigs"
      :render-suggestion="renderSuggestion"
      :get-suggestion-value="getSuggestionValue"
      @input="fetchResults"
    />

    <b-card-text class="mt-1">
      Selected element (object):
    </b-card-text>
    <b-card
      class="border"
      no-body
    >
      <pre>{{ JSON.stringify(selected, null, 4) }}</pre>
    </b-card>

    <template #code>
      {{ codeAjax }}
    </template>
  </b-card-code>
</template>

<script>
/* eslint-disable vue/no-unused-components */
/* eslint no-unused-expressions: ["error", { "allowShortCircuit": true }] */
import BCardCode from '@core/components/b-card-code/BCardCode.vue'
import { BCard, BCardText, BAvatar } from 'bootstrap-vue'
import { VueAutosuggest } from 'vue-autosuggest'
import axios from 'axios'
import { codeAjax } from './code'
import Oauth1Helper from './auth-here'

export default {
  components: {
    VueAutosuggest,
    BCardCode,
    BCard,
    BCardText,
    BAvatar,
  },
  data() {
    return {
      Oauth1Helper,
      codeAjax,
      query: '',
      results: [],
      timeout: null,
      selected: null,
      debounceMilliseconds: 250,
      usersUrl: 'https://jsonplaceholder.typicode.com/users',
      photosUrl: 'https://jsonplaceholder.typicode.com/photos',
      inputProps: {
        id: 'autosuggest__input_ajax',
        placeholder: 'Do you feel lucky, punk?',
        class: 'form-control',
        name: 'ajax',
      },
      suggestions: [],
      sectionConfigs: {
        destinations: {
          limit: 6,
          label: 'Destination',
          onSelected: selected => {
            this.selected = selected.item
          },
        },
        hotels: {
          limit: 6,
          label: 'Hotels',
          onSelected: selected => {
            this.selected = selected.item
          },
        },
      },
    }
  },
  created() {
    // const authHeader = Oauth1Helper.getAuthHeaderForRequest(request)
    // authHeader['Content-Type'] = 'application/x-www-form-urlencoded'
    // console.log('CREATED')
    // const request = {
    //   // url: 'https://geocode.ls.hereapi.com/v1/geocode',
    //   url: 'https://geocoder.ls.hereapi.com/search/6.2/geocode.json',
    //   method: 'get',
    // headers: {
    //   'Content-Type': 'application/x-www-form-urlencoded',
    //   Authorization:(token) => {
    //       axios(
    //         {
    //           headers: {

    //           }
    //         }
    //       ).then(
    //         (response)=>{
    //           token = `Bearer ${reponse.data.access_token}`
    //           return token
    //         }
    //       )
    //   }
    // },
    // params: {
    //   languages: 'en-US',
    //   maxresults: 4,
    //   searchtext: 'Sunnyvale',
    //   apiKey: 'Gr3l3IvxE3-kZR46dzMzf0ciKzopbruETT9HICDkIb0',
    // languages: 'es-ES',
    // maxresults: 10,
    // apiKey: 'Gr3l3IvxE3-kZR46dzMzf0ciKzopbruETT9HICDkIb0',
    // qq: 'country=mexico;street=mexico;postalCode=57500',
    // },
    // },
    // console.log(authHeader)
    // request.headers = authHeader
    // 'Content-Type': 'application/x-www-form-urlencoded'
    //  axios(
    //   request.url,
    //   request.body,
    //   request.headers,
    // )
    // axios(
    //   request,
    // )
    //   .then(response => {
    //     console.log('RESPONSE')
    //     console.log(response)
    //   }).catch(error => {
    //     console.log(error)
    //   })
  },
  updated() {
    console.log('UPDATE')
    const apiKey = 'apiKey=WnMOYAfN-NKNdKhRyMWxnXHzg-psiHuRzz576BKAN2g'
    const url = 'https://geocode.search.hereapi.com/v1/geocode?'
    const qq = 'qq=country=mexico&'
    const fullQuery = `${url}q=${this.query}$${qq}${apiKey}`
    console.log(fullQuery)
  },
  methods: {
    fetchResults() {
      const { query } = this

      clearTimeout(this.timeout)
      this.timeout = setTimeout(() => {
        const photosPromise = axios.get(this.photosUrl)
        const usersPromise = axios.get(this.usersUrl)

        Promise.all([photosPromise, usersPromise]).then(values => {
          this.suggestions = []
          this.selected = null

          const photos = this.filterResults(values[0].data, query, 'title')
          const users = this.filterResults(values[1].data, query, 'name')
          users.length && this.suggestions.push({ name: 'destinations', data: users })
          photos.length && this.suggestions.push({ name: 'hotels', data: photos })
        })
      }, this.debounceMilliseconds)
    },
    filterResults(data, text, field) {
      return data.filter(item => {
        if (item[field].toLowerCase().indexOf(text.toLowerCase()) > -1) {
          return item[field]
        }
        return false
      }).sort()
    },
    renderSuggestion(suggestion) {
      if (suggestion.name === 'hotels') {
        const image = suggestion.item
        return (
          <div class="d-flex">
            <div>
              <b-avatar src={image.thumbnailUrl} class="mr-50"></b-avatar>
            </div>
            <div>
              <span>{image.title}</span>
            </div>
          </div>
        )
      }
      return suggestion.item.name
    },
    getSuggestionValue(suggestion) {
      const { name, item } = suggestion
      return name === 'hotels' ? item.title : item.name
    },
  },
}
</script>

<style lang="scss" scoped>
pre{
  min-height: 295px;
  padding: 1.5rem;
  margin-bottom: 0;
  border-radius: .5rem;
}
</style>
