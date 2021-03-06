<template>
  <!-- <b-card-code title="Ingresa tú dirección "> -->
    <vue-autosuggest
      v-model="selected"
      :suggestions="filteredOptions"
      :limit="10"
      :get-suggestion-value="getSuggestionValue"
      :input-props="{id:'autosuggest__input',class:'form-control', placeholder:'Calle, Número, Código Postal'}"
      @input="onInputChange"
    >
      <template slot-scope="{suggestion}">
        <span class="my-suggestion-item">{{ suggestion.item.title }}</span>
      </template>
    </vue-autosuggest>

    <!-- <template #code>
      {{ codeBasicFormDirection }}
    </template> -->
  <!-- </b-card-code> -->
</template>

<script>
import { VueAutosuggest } from 'vue-autosuggest'
// import BCardCode from '@core/components/b-card-code/BCardCode.vue'
import axios from 'axios'
// import { codeBasicFormDirection } from './code'

export default {
  components: {
    VueAutosuggest,
    // BCardCode,
  },
  data() {
    return {
      datasuggest: [],
      filteredOptions: [],
      limit: 10,
      selected: '',
      direction: null,
      // codeBasicFormDirection,
    }
  },
  beforeUpdate() {
  },
  updated() {
    console.log(this.selected)
  },
  created() {
  },
  methods: {
    onInputChange(text) {
      console.log(this.direction)
      console.log('########################')
      // console.log('onInputChange')
      if (text === '' || text === undefined) {
        this.filteredOptions = []
        this.selected = ''
        this.direction = null
        return
      }
      // GEOCODE
      // const url = `https://geocode.search.hereapi.com/v1/geocode?q=${text}&in=countryCode:MEX&apiKey=WnMOYAfN-NKNdKhRyMWxnXHzg-psiHuRzz576BKAN2g`
      // PLACE
      // const url = `https://places.api.here.com/places/v1/discover/search?at=19.4978,-99.1269&tf=plain&addressFilter=countryCode=MEX&q=${text}&app_id=CPBypQwM5DBlqg0kVMIK&app_code=NXIYJllYjgaayfuimeBPCg`
      // AUTOCOMPLETE
      const url = `https://autocomplete.search.hereapi.com/v1/autocomplete?q=${text}&in=countryCode:MEX&apiKey=WnMOYAfN-NKNdKhRyMWxnXHzg-psiHuRzz576BKAN2g`
      axios.get(url)
        .then(response => {
          if (response.status !== 400) {
            this.datasuggest = response.data.items
            console.log(this.datasuggest)
            this.filteredOptions = [{
              data: this.datasuggest,
            }]
          }
        })
        .catch(error => {
          console.log(error)
        })
      /* Full control over filtering. Maybe fetch from API?! Up to you!!! */
      // const filteredDevelopers = this.datasuggest.data[0].developers.filter(item => item.name.toLowerCase().indexOf(text.toLowerCase()) > -1).slice(0, this.limit)
      // const filteredDesigner = this.datasuggest.data[0].designers.filter(item => item.name.toLowerCase().indexOf(text.toLowerCase()) > -1).slice(0, this.limit)
      // const filteredData = filteredDevelopers.concat(filteredDesigner)
    },
    getSuggestionValue(suggestion) {
      this.direction = suggestion.item.address
      return suggestion.item.title
    },
    // onSelected(selected) {
    //   this.selected = selected
    //   console.log(selected)
    // }
  },
}
</script>
