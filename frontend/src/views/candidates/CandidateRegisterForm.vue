<template>
  <div>
    <!-- color="#7367F0" -->
    <form-wizard
      color="#28a745"
      :title="null"
      :subtitle="null"
      shape="square"
      finish-button-text="Enviar"
      back-button-text="Atras"
      class="m-3"
      @on-complete="formSubmitted"
    >

      <!-- Datos Personales -->
      <!-- :before-change="validationForm" -->
      <tab-content
        title="Datos Personales"
      >
        <validation-observer
          ref="accountRules"
          tag="form"
        >
          <b-row>
            <b-col
              cols="12"
              class="mb-2"
            >
              <h5 class="mb-0">
                Datos Personales
              </h5>
              <small class="text-muted">
                Ingresa los datos personales que se te indican a continuación.
              </small>
            </b-col>
            <b-col md="6">
              <b-form-group
                label="CURP"
                label-for="curp"
              >
                <validation-provider
                  #default="{ errors }"
                  rules="curp|required"
                >
                  <b-form-input
                    id="curp"
                    v-model="form.curp"
                    :state="errors.length > 0 ? false:null"
                    placeholder="CURP"
                  />
                  <small class="text-danger">{{ errors[0] }}</small>
                </validation-provider>
              </b-form-group>
            </b-col>
            <b-col md="6">
              <b-form-group
                label="RFC"
                label-for="rfc"
              >
                <validation-provider
                  #default="{ errors }"
                  name="RFC"
                  rules="rfc|required"
                >
                  <b-form-input
                    id="rfc"
                    v-model="form.rfc"
                    :state="errors.length > 0 ? false:null"
                    placeholder="RFC"
                  />
                  <small class="text-danger">{{ errors[0] }}</small>
                </validation-provider>
              </b-form-group>
            </b-col>
            <b-col md="4">
              <b-form-group
                label="Nombre(s)"
                label-for="name"
              >
                <validation-provider
                  #default="{ errors }"
                  name="name"
                  rules="name|required"
                >
                  <b-form-input
                    id="name"
                    v-model="form.name"
                    :state="errors.length > 0 ? false:null"
                    placeholder="Nombre(s)"
                  />
                  <small class="text-danger">{{ errors[0] }}</small>
                </validation-provider>
              </b-form-group>
            </b-col>
            <b-col md="4">
              <b-form-group
                label="Apellido Paterno"
                label-for="last_name"
              >
                <validation-provider
                  #default="{ errors }"
                  name="last_name"
                  rules="name|required"
                >
                  <b-form-input
                    id="last_name"
                    v-model="form.last_name"
                    :state="errors.length > 0 ? false:null"
                    placeholder="Apellido Paterno"
                  />
                  <small class="text-danger">{{ errors[0] }}</small>
                </validation-provider>
              </b-form-group>
            </b-col>
            <b-col md="4">
              <b-form-group
                label="Apellido Materno"
                label-for="mothers_last_name"
              >
                <validation-provider
                  #default="{ errors }"
                  name="mothers_last_name"
                  rules="name|required"
                >
                  <b-form-input
                    id="mothers_last_name"
                    v-model="form.mothers_last_name"
                    :state="errors.length > 0 ? false:null"
                    placeholder="Apelldio Materno"
                  />
                  <small class="text-danger">{{ errors[0] }}</small>
                </validation-provider>
              </b-form-group>
            </b-col>
            <!-- okas -->
            <b-col md="4">
              <b-form-group
                label="Edad"
                label-for="age"
              >
                <validation-provider
                  #default="{ errors }"
                  name="age"
                  rules="age|required"
                >
                  <b-form-input
                    id="age"
                    v-model="form.age"
                    :state="errors.length > 0 ? false:null"
                    placeholder="Edad"
                  />
                  <small class="text-danger">{{ errors[0] }}</small>
                </validation-provider>
              </b-form-group>
            </b-col>
            <b-col md="4">
              <validation-provider
                #default="{ errors }"
                name="gender"
                rules="required"
              >
                <b-form-group
                  label="Género"
                  label-for="gender"
                  color="#28a745"
                  :state="errors.length > 0 ? false:null"
                >
                  <v-select
                    id="gender"
                    v-model="form.gender"
                    :dir="$store.state.appConfig.isRTL ? 'rtl' : 'ltr'"
                    :options="genderOptions"
                    :selectable="option => ! option.value.includes('select_value')"
                    placeholder="selecciona una opción"
                    label="text"
                  />
                  <b-form-invalid-feedback :state="errors.length > 0 ? false:null">
                    {{ errors[0] }}
                  </b-form-invalid-feedback>
                </b-form-group>
              </validation-provider>
            </b-col>
            <b-col md="4">
              <b-form-group
                label="Estatura"
                label-for="height"
              >
                <validation-provider
                  #default="{ errors }"
                  name="height"
                  rules="height|required"
                >
                  <b-form-input
                    id="height"
                    v-model="form.height"
                    :state="errors.length > 0 ? false:null"
                    placeholder="Estura en [cm], ejemplo 175"
                  />
                  <small class="text-danger">{{ errors[0] }}</small>
                </validation-provider>
              </b-form-group>
            </b-col>
          </b-row>
        </validation-observer>
      </tab-content>

      <!-- Estudios -->
      <!-- :before-change="validationFormInfo" -->
      <tab-content
        title="Estudios"
      >
        <validation-observer
          ref="infoRules"
          tag="form"
        >
          <b-row>
            <b-col
              cols="12"
              class="mb-2"
            >
              <h5 class="mb-0">
                Estudios
              </h5>
              <small class="text-muted">Ingresa los datos sobre el nivel de estudios que se te indican a continuación. </small>
            </b-col>
            <!-- NIVEL DE ESTUDIOS -->
            <b-col md="6">
              <validation-provider
                #default="{ errors }"
                name="stuies"
                rules="required"
              >
                <b-form-group
                  label="Último grado de estudios"
                  label-for="studies"
                  :state="errors.length > 0 ? false:null"
                >
                  <v-select
                    id="stuies"
                    v-model="studies.level_of_studies"
                    :dir="$store.state.appConfig.isRTL ? 'rtl' : 'ltr'"
                    :options="optionsLevelStudies"
                    :selectable="option => ! option.value.includes('select_value')"
                    label="text"
                  />
                  <b-form-invalid-feedback :state="errors.length > 0 ? false:null">
                    {{ errors[0] }}
                  </b-form-invalid-feedback>
                </b-form-group>
              </validation-provider>
            </b-col>

            <!-- TIPO DE ESTUDIOS -->
            <b-col md="6"
              v-if="studies.level_of_studies.value === optionsLevelStudies[0].value"
            >
              <validation-provider
                #default="{ errors }"
                name="type-school"
                rules="required"
              >
                <b-form-group
                  label="Tipo de Bachillerato"
                  label-for="type-school"
                  :state="errors.length > 0 ? false:null"
                >
                  <v-select
                    id="type-school"
                    v-model="studies.details"
                    :dir="$store.state.appConfig.isRTL ? 'rtl' : 'ltr'"
                    :options="typeSchool"
                    :selectable="option => ! option.value.includes('nothing_selected')"
                    label="text"
                  />
                  <b-form-invalid-feedback :state="errors.length > 0 ? false:null">
                    {{ errors[0] }}
                  </b-form-invalid-feedback>
                </b-form-group>
              </validation-provider>
            </b-col>

            <!-- DETALLES LICENCIATURA | MAESTRIA | DOCTORADO -->
            <b-col md="6"
              v-if="studies.level_of_studies.value !== optionsLevelStudies[0].value && studies.level_of_studies.value"
            >
              <b-form-group
                :label="studies.level_of_studies.value"
                label-for="details"
              >
                <validation-provider
                  #default="{ errors }"
                  rules="required"
                >
                  <b-form-input
                    id="details"
                    v-model="form.curp"
                    :state="errors.length > 0 ? false:null"
                    :placeholder="studies.level_of_studies.value + ' en ...'"
                  />
                  <small class="text-danger">{{ errors[0] }}</small>
                </validation-provider>
              </b-form-group>
            </b-col>
          </b-row>
        </validation-observer>
      </tab-content>

      <!-- Dirección  -->
      <!-- :before-change="validationFormAddress" -->
      <tab-content
        title="Dirección"
      >
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

            <!-- BUSQUEDA -->
            <b-col
              cols="12"
              class="mb-2"
            >
              <h3>aqui va la busqueda</h3>
              <search-direction />
            </b-col>

            <!-- LUGAR DE RESIDENCIA -->
            <b-col md="6">
              <validation-provider
                #default="{ errors }"
                name="place-residence"
                rules="required"
              >
                <b-form-group
                  label="Lugar de Residencia"
                  label-for="place-residence"
                  :state="errors.length > 0 ? false:null"
                >
                <!-- :selectable="option => ! option.value.includes('select_value')" -->
                  <v-select
                    id="place-residence"
                    v-model="direction.place_of_residence"
                    :dir="$store.state.appConfig.isRTL ? 'rtl' : 'ltr'"
                    :options="optionsPlaceResidence"
                    :selectable="option => ! option.state.includes('select_value')"
                    label="state"
                    placeholder="Estado"
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
                    placeholder="Delegación o Municipio"
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
                    placeholder="Colonia"
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
                    placeholder="Código Postal"
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
                    placeholder="Calle"
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
                  rules="required"
                >
                  <b-form-input
                    id="num-out"
                    v-model="direction.num_outdoor"
                    :state="errors.length > 0 ? false:null"
                    type="number"
                    placeholder="Num. Exterior"
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
                >
                  <b-form-input
                    id="num-in"
                    v-model="direction.num_inside"
                    :state="errors.length > 0 ? false:null"
                    type="number"
                    placeholder="Num. Interior"
                  />
                  <small class="text-danger">{{ errors[0] }}</small>
                </validation-provider>
              </b-form-group>
            </b-col>
          </b-row>
        </validation-observer>
        <!-- <direction-form /> -->
      </tab-content>

      <!-- Contacto -->
      <!-- :before-change="validationFormSocial" -->
      <tab-content
        title="Forma de Contacto"
      >
        <validation-observer
          ref="socialRules"
          tag="form"
        >
          <b-row>
            <b-col
              cols="12"
              class="mb-2"
            >
              <h5 class="mb-0">
                Contacto
              </h5>
              <small class="text-muted">Ingresa tus formas de contatcto</small>
            </b-col>
            <b-col md="6">
              <b-form-group
                label="Telefono"
                label-for="telephone"
              >
                <validation-provider
                  #default="{ errors }"
                  name="telephone"
                  rules="digits:10|required"
                >
                  <b-form-input
                    id="telephone"
                    v-model="twitterUrl"
                    type="number"
                    :state="errors.length > 0 ? false:null"
                    placeholder=""
                  />
                  <small class="text-danger">{{ errors[0] }}</small>
                </validation-provider>
              </b-form-group>
            </b-col>
            <b-col md="6">
              <b-form-group
                label="Telefono Celular"
                label-for="mobile-telephone"
              >
                <validation-provider
                  #default="{ errors }"
                  name="mobile-telephone"
                  rules="digits:10|required"
                >
                  <b-form-input
                    id="mobile-telephone"
                    v-model="contact.mobile_telephone"
                    :state="errors.length > 0 ? false:null"
                    type="number"
                    placeholder="5511223344"
                  />
                  <small class="text-danger">{{ errors[0] }}</small>
                </validation-provider>
              </b-form-group>
            </b-col>
            <b-col md="6">
              <b-form-group
                label="Correo Electronico"
                label-for="email"
              >
                <validation-provider
                  #default="{ errors }"
                  name="email"
                  rules="required|email"
                >
                  <b-form-input
                    id="email"
                    v-model="contact.email"
                    :state="errors.length > 0 ? false:null"
                    placeholder="corre@dominio.com"
                  />
                  <small class="text-danger">{{ errors[0] }}</small>
                </validation-provider>
              </b-form-group>
            </b-col>
          </b-row>
        </validation-observer>
      </tab-content>

      <!-- Documentos -->
      <!-- :before-change="validationFormDocuments" -->
      <tab-content
        title="Documentos"
      >
        <validation-observer
          ref="documentsRules"
          tag="form"
        >
          <b-row>
            <b-col
              cols="12"
              class="mb-2"
            >
              <h5 class="mb-0">
                Documentos
              </h5>
              <small class="text-muted">Carga tus archivos que se te piden, estos debedn de estar en escaneados y en Formato PDF con un tamaño menor a 2MB</small>
            </b-col>

            <!-- ARCHIVO CURP -->
            <b-col md="6">
              <b-form-group
                label="CURP"
                label-for="file-curp"
              >
              <!-- #default="{ errors }" -->
                <validation-provider
                  #default="{ errors }"
                  name="file-curp"
                  rules="file|required"
                >
                  <b-form-file
                    id="file-curp"
                    v-model="documents.file_curp"
                    accept=".pdf"
                    :state="errors.length > 0 ? false:null"
                    placeholder="Archivo no seleccionado"
                    browse-text="Buscar"
                  />
                  <small class="text-danger">{{ errors[0] }}</small>
                </validation-provider>
              </b-form-group>
            </b-col>
            <!-- ARCHIVO RFC -->
            <b-col md="6">
              <b-form-group
                label="RFC"
                label-for="file-rfc"
              >
              <!-- #default="{ errors }" -->
                <validation-provider
                  #default="{ errors }"
                  name="file-rfc"
                  rules="file|required"
                >
                  <b-form-file
                    id="file-rfc"
                    v-model="documents.file_rfc"
                    accept=".pdf"
                    :state="errors.length > 0 ? false:null"
                    placeholder="Archivo no seleccionado"
                    browse-text="Buscar"
                  />
                  <small class="text-danger">{{ errors[0] }}</small>
                </validation-provider>
              </b-form-group>
            </b-col>
          </b-row>
        </validation-observer>
      </tab-content>

      <!-- Acerca de la convocatoria -->
      <tab-content
        title="Convocatoria"
      >
      </tab-content>
    </form-wizard>

  </div>
</template>

<script>
import { FormWizard, TabContent } from 'vue-form-wizard'
import vSelect from 'vue-select'
import { ValidationProvider, ValidationObserver } from 'vee-validate'
import ToastificationContent from '@core/components/toastification/ToastificationContent.vue'
import 'vue-form-wizard/dist/vue-form-wizard.min.css'
import {
  BRow,
  BCol,
  BFormFile,
  BFormGroup,
  BFormInput,
  BFormInvalidFeedback,
} from 'bootstrap-vue'
import { required, email } from '@validations'
import SearchDirection from './SearchDirection.vue'
import { codeIcon, codeLimiting } from './code'

export default {
  components: {
    // DirectionForm,
    ValidationProvider,
    ValidationObserver,
    FormWizard,
    TabContent,
    BRow,
    BCol,
    BFormFile,
    BFormGroup,
    BFormInput,
    BFormInvalidFeedback,
    vSelect,
    // eslint-disable-next-line vue/no-unused-components
    ToastificationContent,
    SearchDirection,
  },
  data() {
    return {
      showTypeSchool: false,
      form: {
        curp: '',
        rfc: '',
        name: '',
        last_name: '',
        mothers_last_name: '',
        age: '',
        gender: '',
        height: '',
      },
      studies: {
        level_of_studies: '',
        details: '',
      },
      direction: {
        place_of_residence: '',
        delegation: '',
        suburb: '',
        postal_code: '',
        street: '',
        num_outdoor: '',
        num_inside: '',
      },
      contact: {
        telephone: '',
        mobile_telephone: '',
        email: '',
      },
      documents: {
        file_curp: null,
      },
      selectedContry: '',
      selectedLanguage: '',
      name: '',
      emailValue: '',
      PasswordValue: '',
      passwordCon: '',
      first_name: '',
      last_name: '',
      address: '',
      landMark: '',
      pincode: '',
      twitterUrl: '',
      facebookUrl: '',
      googleUrl: '',
      linkedinUrl: '',
      city: '',
      required,
      email,
      codeIcon,
      codeLimiting,
      genderOptions: [
        { value: 'Femenino', text: 'Femenino' },
        { value: 'Masculino', text: 'Masculino' },
      ],
      optionsLevelStudies: [
        { value: 'Bachillerato', text: 'Bachillerato' },
        { value: 'Licenciatura', text: 'Licenciatura' },
        { value: 'Maestría', text: 'Maestría' },
        { value: 'Doctorado', text: 'Doctorado' },
      ],
      typeSchool: [
        { value: 'BACHILLERES', text: 'BACHILLERES' },
        { value: 'CBT', text: 'CBT' },
        { value: 'CBTIS', text: 'CEBETIS' },
        { value: 'CECYT', text: 'CECYT' },
        { value: 'CECYTEM', text: 'CECYTEM' },
        { value: 'CETIS', text: 'CETIS' },
        { value: 'CONALEP', text: 'CONALEP' },
        { value: 'ESC. PARTICULAR', text: 'ESC. PARTICULAR' },
        { value: 'PREPARATORIA DE LA CDMX', text: 'PREPARATORIA DE LA CDMX' },
        { value: 'PREPARTORIA DE LA UNAM', text: 'PREPARTORIA DE LA UNAM' },
        { value: 'PREPARATORIA ESTATAL', text: 'PREPARATORIA ESTATAL' },
        { value: 'SISTEMA ABIERTO', text: 'SISTEMA ABIERTO' },
      ],
      optionsPlaceResidence: [],
      optionsDelegation: [],
    }
  },
  // update: function () {
  //   console.log('Esta actualizando cambios')
  // },
  updated() {
    console.log('Método UPDATE')
    // EN ESTA SECCION SE HACE PETICION A LA API UNIPOL PARA CONSULTAR LAS DELEGACIONES O MUNICIPIOS
    console.log(this.documents.file_curp)
    // if (this.documents.file_curp.size <= 2097152) {
    //   console.log('Archivo Valido')
    // }
  },
  // watch() {
  // },
  methods: {
    showInput() {
      // console.log('>>>>>>')
      // console.log(JSON.stringify(this.studies.level_of_studies.text))
      // console.log(this.showTypeSchool)
      // return this.showTypeSchool
    },
    formSubmitted() {
      this.$toast({
        component: ToastificationContent,
        props: {
          title: 'Form Submitted',
          icon: 'EditIcon',
          variant: 'success',
        },
      })
    },
    validationForm() {
      return new Promise((resolve, reject) => {
        this.$refs.accountRules.validate().then(success => {
          if (success) {
            resolve(true)
          } else {
            reject()
          }
        })
      })
    },
    validationFormInfo() {
      return new Promise((resolve, reject) => {
        this.$refs.infoRules.validate().then(success => {
          if (success) {
            resolve(true)
          } else {
            console.log('Algo salio mal')
            reject()
          }
        })
      })
    },
    validationFormAddress() {
      return new Promise((resolve, reject) => {
        this.$refs.addressRules.validate().then(success => {
          if (success) {
            resolve(true)
          } else {
            reject()
          }
        })
      })
    },
    validationFormSocial() {
      return new Promise((resolve, reject) => {
        this.$refs.socialRules.validate().then(success => {
          if (success) {
            resolve(true)
          } else {
            reject()
          }
        })
      })
    },
  },
  created() {
    // EN ESTA SECCION SE HACE PETICION A LA API UNIPOL PARA CONSULTAR LOS ESTADOS DE LA REPUBLICA
    // console.log('Método CREATED')
    // this.optionsPlaceResidence = states
    // this.optionsDelegation = delegations
    // console.log(this.optionsDelegation)
  },
}
</script>
