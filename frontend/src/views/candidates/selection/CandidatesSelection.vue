<template>
  <b-row>
    <b-col cols="12">
      <!-- <candidate-selection-table /> -->
      <candidate-selection-table-2 />
    </b-col>
  </b-row>
</template>

<script>
import { BRow, BCol } from 'bootstrap-vue'
// import CandidateSelectionTable from './CandidateSelectionTable.vue'
import CandidateSelectionTable2 from './CandidateSelectionTable2.vue'

export default {
  components: {
    BRow,
    BCol,
    // CandidateSelectionTable,
    CandidateSelectionTable2,
  },
}
</script>

<style lang="scss" >
@import '@core/scss/vue/libs/vue-good-table.scss';
</style>
