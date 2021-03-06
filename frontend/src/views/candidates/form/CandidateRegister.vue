<template>
  <b-row>
    <b-col cols="12">
      <candidate-register-form />
    </b-col>
  </b-row>
</template>

<script>
import { BRow, BCol } from 'bootstrap-vue'
import CandidateRegisterForm from './CandidateRegisterForm.vue'

export default {
  components: {
    BRow,
    BCol,
    CandidateRegisterForm,
  },
}
</script>

<style lang="scss">
  @import '@core/scss/vue/libs/vue-wizard.scss';
  @import '@core/scss/vue/libs/vue-select.scss';
</style>
