<template>
  <validation-observer
    ref="addressRules"
    tag="form"
  >
    <b-row>
      <b-col
        cols="12"
        class="mb-2"
      >
        <h5 class="mb-0">
          Dirección
        </h5>
        <small class="text-muted">Ingresa los datos sobre tu dirección</small>
      </b-col>

      <!-- LUGAR DE RESIDENCIA -->
      <b-col md="6">
        <validation-provider
          #default="{ errors }"
          name="place residence"
          rules="required"
        >
          <b-form-group
            label="Lugar de Residencia"
            label-for="place residence"
            :state="errors.length > 0 ? false:null"
          >
            <v-select
              id="place-residence"
              v-model="direction.place_of_residence"
              :dir="$store.state.appConfig.isRTL ? 'rtl' : 'ltr'"
              :options="optionsPlaceResidence"
              :selectable="option => ! option.value.includes('select_value')"
              label="text"
            />
            <b-form-invalid-feedback :state="errors.length > 0 ? false:null">
              {{ errors[0] }}
            </b-form-invalid-feedback>
          </b-form-group>
        </validation-provider>
      </b-col>

      <!-- DELEGACION o MUNICIPIO -->
      <b-col md="6">
        <validation-provider
          #default="{ errors }"
          name="delegation"
          rules="required"
        >
          <b-form-group
            label="Delegación o Municipio"
            label-for="delegation"
            :state="errors.length > 0 ? false:null"
          >
            <v-select
              id="delegation"
              v-model="direction.delegation"
              :dir="$store.state.appConfig.isRTL ? 'rtl' : 'ltr'"
              :options="optionsDelegation"
              :selectable="option => ! option.value.includes('select_value')"
              label="text"
            />
            <b-form-invalid-feedback :state="errors.length > 0 ? false:null">
              {{ errors[0] }}
            </b-form-invalid-feedback>
          </b-form-group>
        </validation-provider>
      </b-col>

      <!-- COLONIA -->
      <b-col md="6">
        <b-form-group
          label="Colonia"
          label-for="suburb"
        >
          <validation-provider
            #default="{ errors }"
            name="suburb"
            rules="required"
          >
            <b-form-input
              id="suburb"
              v-model="direction.suburb"
              :state="errors.length > 0 ? false:null"
              placeholder="Delegación o Municipio"
            />
            <small class="text-danger">{{ errors[0] }}</small>
          </validation-provider>
        </b-form-group>
      </b-col>

      <!-- CÓDIGO POSTAL -->
      <b-col md="6">
        <b-form-group
          label="Código Postal"
          label-for="postal-code"
        >
          <validation-provider
            #default="{ errors }"
            name="postal-code"
            rules="required"
          >
            <b-form-input
              id="postal-code"
              v-model="direction.postal_code"
              :state="errors.length > 0 ? false:null"
              type="number"
              placeholder="57000"
            />
            <small class="text-danger">{{ errors[0] }}</small>
          </validation-provider>
        </b-form-group>
      </b-col>

      <!-- CALLE -->
      <b-col md="6">
        <b-form-group
          label="Calle"
          label-for="street"
        >
          <validation-provider
            #default="{ errors }"
            name="street"
            rules="required"
          >
            <b-form-input
              id="street"
              v-model="direction.street"
              :state="errors.length > 0 ? false:null"
              placeholder="98 Borough bridge Road, Birmingham"
            />
            <small class="text-danger">{{ errors[0] }}</small>
          </validation-provider>
        </b-form-group>
      </b-col>

    <!-- NUMERO EXTERIOR -->
      <b-col md="3">
        <b-form-group
          label="Numero Exterior"
          label-for="num-out"
        >
          <validation-provider
            #default="{ errors }"
            name="num-out"
          >
            <b-form-input
              id="num-out"
              v-model="direction.num_outdoor"
              :state="errors.length > 0 ? false:null"
              type="number"
              placeholder="Birmingham"
            />
            <small class="text-danger">{{ errors[0] }}</small>
          </validation-provider>
        </b-form-group>
      </b-col>

      <!-- NUMERO INTERIOR -->
      <b-col md="3">
        <b-form-group
          label="Numero exterior"
          label-for="num-in"
        >
          <validation-provider
            #default="{ errors }"
            name="num-in"
            rules="required"
          >
            <b-form-input
              id="num-in"
              v-model="direction.num_inside"
              :state="errors.length > 0 ? false:null"
              type="number"
              placeholder="Borough bridge"
            />
            <small class="text-danger">{{ errors[0] }}</small>
          </validation-provider>
        </b-form-group>
      </b-col>
    </b-row>
  </validation-observer>
</template>

<script>
import vSelect from 'vue-select'
import { ValidationProvider, ValidationObserver } from 'vee-validate'
import ToastificationContent from '@core/components/toastification/ToastificationContent.vue'
import 'vue-form-wizard/dist/vue-form-wizard.min.css'
import {
  BRow,
  BCol,
  BFormGroup,
  BFormInput,
  BFormInvalidFeedback,
} from 'bootstrap-vue'
import { required, email } from '@validations'
import { codeIcon } from '../code'

export default {
  components: {
    ValidationProvider,
    ValidationObserver,
    BRow,
    BCol,
    BFormGroup,
    BFormInput,
    vSelect,
    BFormInvalidFeedback,
    // eslint-disable-next-line vue/no-unused-components
    ToastificationContent,
  },
  data: () => ({
    direction: {
      place_of_residence: '',
      delegation: '',
      suburb: '',
      postal_code: '',
      street: '',
      num_outdoor: '',
      num_inside: '',
    },
    required,
    email,
    codeIcon,
    optionsPlaceResidence: [
      { value: 'PR1', text: 'opcion1' },
      { value: 'PR2', text: 'opcion2' },
    ],
    optionsDelegation: [
      { value: 'D1', text: 'opcion1' },
      { value: 'D2', text: 'opcion2' },
    ],
  }),
}
</script>

<style>

</style>
