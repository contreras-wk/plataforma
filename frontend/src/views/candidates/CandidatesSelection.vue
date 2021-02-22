<template>
  <b-row>
    <b-col cols="12">
      <candidate-selection-table />
    </b-col>
  </b-row>
</template>

<script>
import { BRow, BCol } from 'bootstrap-vue'
import CandidateSelectionTable from './CandidateSelectionTable.vue'

export default {
  components: {
    BRow,
    BCol,
    CandidateSelectionTable,
  },
}
</script>

<style lang="scss" >
@import '@core/scss/vue/libs/vue-good-table.scss';
</style>
