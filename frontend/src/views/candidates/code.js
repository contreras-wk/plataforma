export const codeBasic = `
<template>
  <div>
    <!-- search input -->
    <div class="custom-search d-flex justify-content-end">
      <b-form-group>
        <div class="d-flex align-items-center">
          <label class="mr-1">Search</label>
          <b-form-input
            v-model="searchTerm"
            placeholder="Search"
            type="text"
            class="d-inline-block"
          />
        </div>
      </b-form-group>
    </div>

    <!-- table -->
    <vue-good-table
      :columns="columns"
      :rows="rows"
      :rtl="direction"
      :search-options="{
        enabled: true,
        externalQuery: searchTerm }"
      :select-options="{
        enabled: true,
        selectOnCheckboxOnly: true, // only select when checkbox is clicked instead of the row
        selectionInfoClass: 'custom-class',
        selectionText: 'rows selected',
        clearSelectionText: 'clear',
        disableSelectInfo: true, // disable the select info panel on top
        selectAllByGroup: true, // when used in combination with a grouped table, add a checkbox in the header row to check/uncheck the entire group
      }"
      :pagination-options="{
        enabled: true,
        perPage:pageLength
      }"
    >
      <template
        slot="table-row"
        slot-scope="props"
      >

        <!-- Column: Name -->
        <span
          v-if="props.column.field === 'fullName'"
          class="text-nowrap"
        >
          <b-avatar
            :src="props.row.avatar"
            class="mx-1"
          />
          <span class="text-nowrap">{{ props.row.fullName }}</span>
        </span>

        <!-- Column: Status -->
        <span v-else-if="props.column.field === 'status'">
          <b-badge :variant="statusVariant(props.row.status)">
            {{ props.row.status }}
          </b-badge>
        </span>

        <!-- Column: Action -->
        <span v-else-if="props.column.field === 'action'">
          <span>
            <b-dropdown
              variant="link"
              toggle-class="text-decoration-none"
              no-caret
            >
              <template v-slot:button-content>
                <feather-icon
                  icon="MoreVerticalIcon"
                  size="16"
                  class="text-body align-middle mr-25"
                />
              </template>
              <b-dropdown-item>
                <feather-icon
                  icon="Edit2Icon"
                  class="mr-50"
                />
                <span>Edit</span>
              </b-dropdown-item>
              <b-dropdown-item>
                <feather-icon
                  icon="TrashIcon"
                  class="mr-50"
                />
                <span>Delete</span>
              </b-dropdown-item>
            </b-dropdown>
          </span>
        </span>

        <!-- Column: Common -->
        <span v-else>
          {{ props.formattedRow[props.column.field] }}
        </span>
      </template>

      <!-- pagination -->
      <template
        slot="pagination-bottom"
        slot-scope="props"
      >
        <div class="d-flex justify-content-between flex-wrap">
          <div class="d-flex align-items-center mb-0 mt-1">
            <span class="text-nowrap ">
              Showing 1 to
            </span>
            <b-form-select
              v-model="pageLength"
              :options="['3','5','10']"
              class="mx-1"
              @input="(value)=>props.perPageChanged({currentPerPage:value})"
            />
            <span class="text-nowrap"> of {{ props.total }} entries </span>
          </div>
          <div>
            <b-pagination
              :value="1"
              :total-rows="props.total"
              :per-page="pageLength"
              first-number
              last-number
              align="right"
              prev-class="prev-item"
              next-class="next-item"
              class="mt-1 mb-0"
              @input="(value)=>props.pageChanged({currentPage:value})"
            >
              <template #prev-text>
                <feather-icon
                  icon="ChevronLeftIcon"
                  size="18"
                />
              </template>
              <template #next-text>
                <feather-icon
                  icon="ChevronRightIcon"
                  size="18"
                />
              </template>
            </b-pagination>
          </div>
        </div>
      </template>
    </vue-good-table>
  </div>
</template>

<script>
import {
  BAvatar, BBadge, BPagination, BFormGroup, BFormInput, BFormSelect, BDropdown, BDropdownItem,
} from 'bootstrap-vue'
import { VueGoodTable } from 'vue-good-table'
import store from '@/store/index'

export default {
  components: {
    VueGoodTable,
    BAvatar,
    BBadge,
    BPagination,
    BFormGroup,
    BFormInput,
    BFormSelect,
    BDropdown,
    BDropdownItem,
  },
  data() {
    return {
      pageLength: 3,
      dir: false,
      columns: [
        {
          label: 'Name',
          field: 'fullName',
        },
        {
          label: 'Email',
          field: 'email',
        },
        {
          label: 'Date',
          field: 'startDate',
        },
        {
          label: 'Salary',
          field: 'salary',
        },
        {
          label: 'Status',
          field: 'status',
        },
        {
          label: 'Action',
          field: 'action',
        },
      ],
      rows: [],
      searchTerm: '',
      status: [{
        1: 'Current',
        2: 'Professional',
        3: 'Rejected',
        4: 'Resigned',
        5: 'Applied',
      },
      {
        1: 'light-primary',
        2: 'light-success',
        3: 'light-danger',
        4: 'light-warning',
        5: 'light-info',
      }],
    }
  },
  computed: {
    statusVariant() {
      const statusColor = {
        /* eslint-disable key-spacing */
        Current      : 'light-primary',
        Professional : 'light-success',
        Rejected     : 'light-danger',
        Resigned     : 'light-warning',
        Applied      : 'light-info',
        /* eslint-enable key-spacing */
      }

      return status => statusColor[status]
    },
    direction() {
      if (store.state.appConfig.isRTL) {
        // eslint-disable-next-line vue/no-side-effects-in-computed-properties
        this.dir = true
        return this.dir
      }
      // eslint-disable-next-line vue/no-side-effects-in-computed-properties
      this.dir = false
      return this.dir
    },
  },
  created() {
    this.$http.get('/good-table/basic')
      .then(res => { this.rows = res.data })
  },
}
</script>
`

export const codeIcon = `
<template>
  <form-wizard
    color="#5A8DEE"
    :title="null"
    :subtitle="null"
    finish-button-text="Submit"
    @on-complete="formSubmitted"
  >
    <tab-content icon="bx bx-file-blank">
      <b-row>
        <b-col cols="12">
          <h6 class="py-50">
            Enter Your Personal Details
          </h6>
        </b-col>
        <b-col md="6">
          <b-form-group>
            <label for="firstName">First Name</label>
            <b-form-input
              id="firstName"
              type="text"
              placeholder="Enter Your First Name"
            />
          </b-form-group>
        </b-col>
        <b-col md="6">
          <b-form-group>
            <label for="lastName">Last Name</label>
            <b-form-input
              id="lastName"
              type="text"
              placeholder="Enter Your Last Name"
            />
          </b-form-group>
        </b-col>
        <b-col md="6">
          <b-form-group>
            <label for="email">Email</label>
            <b-form-input
              id="email"
              type="email"
              placeholder="Enter Your Email"
            />
          </b-form-group>
        </b-col>
        <b-col md="6">
          <b-form-group>
            <label for="phone">Phone</label>
            <b-form-input
              id="phone"
              type="number"
              placeholder="Enter Your Phone Number"
            />
          </b-form-group>
        </b-col>
        <b-col md="6">
          <b-form-group>
            <label for="age">Age</label>
            <b-form-input
              id="age"
              type="number"
              placeholder="Enter Your Age"
            />
          </b-form-group>
        </b-col>
        <b-col md="6">
          <b-form-group>
            <label>Gender</label>
            <div class="radio">
              <b-form-radio
                v-model="gender"
                class="p-0"
                name="some-radios"
                value="A"
                plain
                inline
              >
                Male
              </b-form-radio>
              <b-form-radio
                v-model="gender"
                name="some-radios"
                value="B"
                plain
                inline
              >
                Female
              </b-form-radio>
            </div>
          </b-form-group>
        </b-col>
      </b-row>
    </tab-content>
    <tab-content icon="bx bxs-truck">
      <b-row>
        <b-col cols="12">
          <h6 class="py-50">
            Enter Your Location
          </h6>
        </b-col>
        <b-col md="6">
          <b-form-group>
            <label for="AddresLine1">Address Line 1</label>
            <b-form-input
              id="AddresLine1"
              type="text"
              placeholder="Enter House no./ Flate no."
            />
          </b-form-group>
        </b-col>
        <b-col md="6">
          <b-form-group>
            <label for="AddresLine2">Address Line 2</label>
            <b-form-input
              id="AddresLine2"
              type="text"
              placeholder="Enter Society name/ Area name"
            />
          </b-form-group>
        </b-col>
        <b-col md="6">
          <b-form-group>
            <label for="landmark">Landmark</label>
            <b-form-input
              id="landmark"
              type="text"
              placeholder="Enter A Landmark"
            />
          </b-form-group>
        </b-col>
        <b-col md="6">
          <b-form-group>
            <label for="town-city">Town/City</label>
            <b-form-input
              id="town-city"
              type="text"
              placeholder="Enter Town/City"
            />
          </b-form-group>
        </b-col>
        <b-col md="6">
          <b-form-group>
            <label for="pincode">Pincode</label>
            <b-form-input
              id="pincode"
              type="number"
              placeholder="Enter Your Pincode"
            />
          </b-form-group>
        </b-col>
        <b-col md="6">
          <b-form-group>
            <label for="state">State</label>
            <b-form-input
              id="state"
              type="text"
              placeholder="Enter Your State"
            />
          </b-form-group>
        </b-col>
        <b-col md="6">
          <b-form-group>
            <label for="country">Country</label>
            <b-form-select
              v-model="selected"
              :options="options"
            />
          </b-form-group>
        </b-col>
        <b-col
          md="6"
          class="d-flex align-items-center"
        >
          <b-form-group>
            <div class="checkbox">
              <b-form-checkbox
                plain
                value="A"
                class="ml-0"
              >
                Permanent Delivery address
              </b-form-checkbox>
            </div>
          </b-form-group>
        </b-col>
      </b-row>
    </tab-content>
    <tab-content icon="bx bx-home">
      <b-row>
        <b-col cols="12">
          <h6 class="py-50">
            Enter Your Payment Methods
          </h6>
        </b-col>
        <b-col cols="12">
          <b-form-group>
            <div class="d-flex justify-content-between flex-wrap align-items-center">
              <div class="vs-radio-con vs-radio-primary">
                <b-img
                  :src="require('@/assets/images/images/pages/bank.png')"
                  height="40"
                  class="d-inline-block"
                />
                <span>Card 12XX XXXX XXXX 0000</span>
              </div>
              <div class="card-holder-name">
                John Doe
              </div>
              <div class="card-expiration-date">
                11/2020
              </div>
              <div>
                <label>Enter CVV</label>
                <b-form-input
                  type="password"
                  placeholder="Enter Your CVV no."
                />
              </div>
            </div>
          </b-form-group>
          <hr>
        </b-col>
        <b-col cols="12 pl-0">
          <b-form-group>
            <div class="radio">
              <b-form-radio-group
                :options="radioOption"
                name="radios-stacked"
                plain
                stacked
              />
            </div>
          </b-form-group>
          <hr class="ml-1">
        </b-col>
        <b-col
          cols="12"
          class="d-flex align-items-center"
        >
          <div class="paypal cursor-pointer d-flex align-items-center">
            <div class="radio">
              <b-form-radio
                class="p-0"
                name="some-radios"
                value="A"
                plain
              >
                <b-img
                  :src="require('@/assets/images/images/pages/PayPal_logo.png')"
                  alt="PayPal Logo"
                />
              </b-form-radio>
            </div>
          </div>
          <div class="googlepay cursor-pointer pl-1 d-flex align-items-center">
            <div class="radio">
              <b-form-radio
                class="p-0"
                name="some-radios"
                value="B"
                plain
              >
                <b-img
                  :src="require('@/assets/images/images/pages/google-pay.png')"
                  height="30"
                  alt="google Logo"
                />
              </b-form-radio>
            </div>
          </div>
        </b-col>
        <b-col md="6">
          <hr>

          <label>Enter Your Promocode</label>
          <b-form-input
            type="text"
            placeholder="Enter Your Promocode"
          />
        </b-col>
      </b-row>
    </tab-content>
  </form-wizard>
</template>

<script>
import AppCard from '@core/components/app-card/AppCard.vue'
import { FormWizard, TabContent } from 'vue-form-wizard'
import 'vue-form-wizard/dist/vue-form-wizard.min.css'
import {
  BRow,
  BCol,
  BFormGroup,
  BFormInput,
  BFormRadio,
  BFormCheckbox,
  BFormSelect,
  BImg,
  BFormRadioGroup,
} from 'bootstrap-vue'

export default {
  components: {
    FormWizard,
    TabContent,
    AppCard,
    BRow,
    BCol,
    BFormGroup,
    BFormInput,
    BFormRadio,
    BFormCheckbox,
    BFormSelect,
    BImg,
    BFormRadioGroup,
  },
  data: () => ({
    selected: null,
    gender: 'A',
    options: [
      { value: null, text: 'Please select an option' },
      { value: 'a', text: 'This is First option' },
      { value: 'b', text: 'Selected Option' },
      { value: { C: '3PO' }, text: 'This is an option with object value' },
      { value: 'd', text: 'This one is disabled', disabled: true },
    ],
    radioOption: [
      { text: 'Credit / Debit / ATM Card', value: 'first' },
      { text: 'Net Banking', value: 'second' },
      { text: 'EMI (Easy Installment)', value: 'third' },
      { text: 'Cash On Delivery', value: 'fourth' },
    ],
    radioOption2: [
      { text: '', value: 'paypal' },
      { text: '', value: 'gpay' },
    ],
  }),
  methods: {
    formSubmitted() {
      // eslint-disable-next-line
      alert('Form submitted!')
    },
  },
}
</script>
`

export const codeLimiting = `
<template>
  <div>
    <div>
      <!-- Accept all image formats by IANA media type wildcard-->
      <label for="wildcard">Accept all image</label>
      <b-form-file
        id="wildcard"
        accept="image/*"
      />

      <!-- Accept specific image formats by IANA type -->
      <label
        for="IANA"
        class="mt-1"
      >Accept specific image formats by IANA type</label>
      <b-form-file
        id="IANA"
        accept="image/jpeg, image/png, image/gif"
      />

      <!-- Accept specific image formats by extension -->
      <label
        for="extension"
        class="mt-1"
      >Accept specific image formats by extension</label>
      <b-form-file
        id="extension"
        accept=".jpg, .png, .gif"
      />
    </div>
  </div>
</template>

<script>
import { BFormFile } from 'bootstrap-vue'

export default {
  components: {
    BCardCode,
    BFormFile,
  },
}
</script>
`

export const codeBasicFormDirection = `
<template>
  <vue-autosuggest
    :suggestions="filteredOptions"
    :limit="10"
    :input-props="{id:'autosuggest__input',class:'form-control', placeholder:'Do you feel lucky?'}"
    @input="onInputChange"
  >
    <template slot-scope="{suggestion}">
      <span class="my-suggestion-item">{{ suggestion.item.name }}</span>
    </template>
  </vue-autosuggest>
</template>

<script>
import { VueAutosuggest } from 'vue-autosuggest'

export default {
  components: {
    VueAutosuggest,
  },
  data() {
    return {
      datasuggest: [],
      filteredOptions: [],
      limit: 10,
      selected: null,
    }
  },
  created() {
    this.$http.get('/autosuggest/data')
      .then(res => { this.datasuggest = res })
  },
  methods: {
    onInputChange(text) {
      if (text === '' || text === undefined) {
        return
      }

      /* Full control over filtering. Maybe fetch from API?! Up to you!!! */
      const filteredDevelopers = this.datasuggest.data[0].developers.filter(item => item.name.toLowerCase().indexOf(text.toLowerCase()) > -1).slice(0, this.limit)
      const filteredDesigner = this.datasuggest.data[0].designers.filter(item => item.name.toLowerCase().indexOf(text.toLowerCase()) > -1).slice(0, this.limit)
      const filteredData = filteredDevelopers.concat(filteredDesigner)
      this.filteredOptions = [{
        data: filteredData,
      }]
    },
  },
}
</script>
`

export const codeAjax = `
<template>
  <div>
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
  </div>
</template>

<script>
/* eslint-disable vue/no-unused-components */
/* eslint no-unused-expressions: ["error", { "allowShortCircuit": true }] */
import { BCard, BCardText, BAvatar } from 'bootstrap-vue'
import { VueAutosuggest } from 'vue-autosuggest'
import axios from 'axios'

export default {
  components: {
    VueAutosuggest,
    BCard,
    BCardText,
    BAvatar,
  },
  data() {
    return {
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
`
