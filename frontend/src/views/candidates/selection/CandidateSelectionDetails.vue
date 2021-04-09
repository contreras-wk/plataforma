<template>
  <section class="invoice-preview-wrapper">

    <!-- Alerta, no hay carga de datos -->
    <b-alert
      variant="danger"
      :show="candidateData === undefined"
    >
      <h4 class="alert-heading">
        Error No se lograron cargar los datos
      </h4>
      <div class="alert-body">
        No invoice found with this invoice id. Check
        <b-link
          class="alert-link"
          :to="{ name: 'prebecarios-seleccion'}"
        >
          Invoice List
        </b-link>
        for other invoices.
      </div>
    </b-alert>

    <b-row
      v-if="candidateData"
      class="invoice-preview"
    >

      <!-- Col: Left (Invoice Container) -->
      <b-col
        cols="12"
        xl="9"
        md="8"
      >
        <b-card
          no-body
          class="invoice-preview-card"
        >
          <!-- Header -->
          <b-card-body class="invoice-padding pb-0">
            <div class="d-flex justify-content-between flex-md-row flex-column invoice-spacing mt-0">
              <!-- Header: Left Content -->
              <div>
                <div class="logo-wrapper">
                  <logo />
                  <h3 class="text-success invoice-logo">
                    Unipol
                  </h3>
                </div>
                <h3 class="card-text mb-25">
                  {{ `${candidateData.name}  ${candidateData.last_name} ${candidateData.mothers_last_name}` }}
                </h3>
              </div>

              <!-- Header: Right Content -->
              <div class="mt-md-0 mt-2">
                <h4 class="invoice-title">
                  Prebecario
                  <span class="invoice-number">#{{ candidateData.id }}</span>
                </h4>
                <div class="invoice-date-wrapper">
                  <p class="invoice-date-title">
                    Fecha :
                  </p>
                  <p class="invoice-date">
                    {{ candidateData.date_create }}
                  </p>
                </div>
              </div>
            </div>
          </b-card-body>

          <hr class="invoice-spacing">

          <!-- Datos Personales -->
          <b-row>
            <b-col cols="3">
              <h5 class="alert-body ml-4">
                Datos Personales
              </h5>
            </b-col>
            <b-col
              xl="6"
              cols="4"
              class="p-0 mt-xl-0 mt-2 justify-content-xl-end"
            >
              <div>
                <table>
                  <tbody>
                    <tr>
                      <td class="pr-1">
                        CURP
                      </td>
                      <td><span class="font-weight-bold">{{ candidateData.curp }}</span></td>
                    </tr>
                    <tr>
                      <td class="pr-1">
                        RFC:
                      </td>
                      <td><span class="font-weight-bold">{{ candidateData.rfc }}</span></td>
                    </tr>
                    <tr>
                      <td class="pr-1">
                        Edad:
                      </td>
                      <td><span class="font-weight-bold">{{ candidateData.age }}</span></td>
                    </tr>
                    <tr>
                      <td class="pr-1">
                        Estatura:
                      </td>
                      <td><span class="font-weight-bold">{{ candidateData.height }}</span></td>
                    </tr>
                    <tr>
                      <td class="pr-1">
                        Genero:
                      </td>
                      <td><span class="font-weight-bold">{{ candidateData.gender }}</span></td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </b-col>
            <b-col
              align-self="center"
              cols="3"
            >
              <b-button
                class="mb-1"
                variant="outline-success"
                @click="showCurp"
              >Ver CURP</b-button>
              <b-button
                class="mb-1 ml-1"
                variant="success"
              >Ver RFC</b-button>
              <b-button
                variant="success"
              >Ver ActaN</b-button>
              <b-button
                class="ml-1"
                variant="success"
              >Ver INE</b-button>
            </b-col>
          </b-row>

          <hr class="invoice-spacing">

          <!-- Nivel de estudios -->
          <b-row>
            <b-col cols="3">
              <h5 class="alert-body ml-4 mb-0">
                Estudios
              </h5>
            </b-col>
            <b-col
              xl="6"
              cols="6"
              class="p-0 mt-xl-0 mt-2 justify-content-xl-end"
            >
              <div>
                <table>
                  <tbody>
                    <tr>
                      <td class="">
                        Nivel de estudios:
                      </td>
                      <td><span class="font-weight-bold">{{ candidateData.studies.level_of_studies }}</span></td>
                    </tr>
                    <tr>
                      <td class="pr-1">
                        Detalles:
                      </td>
                      <td><span class="font-weight-bold">{{ candidateData.studies.details }}</span></td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </b-col>
            <b-col
              align-self="center"
              cols="3"
            >
              <b-button
                class="m-1"
                variant="outline-success"
              >Ver comprobante de estudios</b-button>
            </b-col>
          </b-row>

          <hr class="invoice-spacing">

          <!-- Dirección -->
          <b-row>
            <b-col cols="3">
              <h5 class="alert-body ml-4 my-0">
                Dirección
              </h5>
            </b-col>
            <b-col
              xl="6"
              cols="6"
              class="p-0 mt-xl-0 mt-2 justify-content-xl-end"
            >
              <div>
                <table>
                  <tbody>
                    <tr>
                      <td class="pr-1">
                        Lugar de residencia:
                      </td>
                      <td><span class="font-weight-bold">{{ candidateData.direction.place_of_residence }}</span></td>
                    </tr>
                    <tr>
                      <td class="pr-1">
                        Delegación o Municipio:
                      </td>
                      <td><span class="font-weight-bold">{{ candidateData.direction.delegation }}</span></td>
                    </tr>
                    <tr>
                      <td class="pr-1">
                        Colonia:
                      </td>
                      <td><span class="font-weight-bold">{{ candidateData.direction.suburb }}</span></td>
                    </tr>
                    <tr>
                      <td class="pr-1">
                        Código Postal:
                      </td>
                      <td><span class="font-weight-bold">{{ candidateData.direction.postal_code }}</span></td>
                    </tr>
                    <tr>
                      <td class="pr-1">
                        Calle:
                      </td>
                      <td><span class="font-weight-bold">{{ candidateData.direction.street }}</span></td>
                    </tr>
                    <tr>
                      <td class="pr-1">
                        Número Exterior:
                      </td>
                      <td><span class="font-weight-bold">{{ candidateData.direction.num_outdoor }}</span></td>
                    </tr>
                    <tr>
                      <td class="pr-1">
                        Número Interior:
                      </td>
                      <td><span class="font-weight-bold">{{ candidateData.direction.num_inside }}</span></td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </b-col>
            <b-col
              align-self="center"
              cols="3"
            >
              <b-button
                class="m-1"
                variant="outline-success"
              >Ver comprobante de domicilio</b-button>
            </b-col>
          </b-row>

          <hr class="invoice-spacing">

          <!-- Contacto -->
          <b-row>
            <b-col cols="3">
              <h5 class="alert-body ml-4">
                Contacto
              </h5>
            </b-col>
            <b-col
              xl="6"
              cols="6"
              class="p-0 mt-xl-0 mt-2 justify-content-xl-end"
            >
              <div>
                <table>
                  <tbody>
                    <tr>
                      <td class="pr-1">
                        Telefono:
                      </td>
                      <td><span class="font-weight-bold">{{ candidateData.contact.telephone }}</span></td>
                    </tr>
                    <tr>
                      <td class="pr-1">
                        Telefono Móvil:
                      </td>
                      <td><span class="font-weight-bold">{{ candidateData.contact.mobile_telephone }}</span></td>
                    </tr>
                    <tr>
                      <td class="pr-1">
                        Correo Electronico:
                      </td>
                      <td><span class="font-weight-bold">{{ candidateData.contact.email }}</span></td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </b-col>
          </b-row>

          <hr class="invoice-spacing">
        </b-card>
      </b-col>

      <!-- Right Col: Card -->
      <b-col
        cols="12"
        md="4"
        xl="3"
        class="invoice-actions"
      >
        <b-card>

          <!-- Button: Send Invoice -->
          <!-- <b-button
            v-ripple.400="'rgba(255, 255, 255, 0.15)'"
            v-b-toggle.sidebar-send-invoice
            variant="primary"
            class="mb-75"
            block
          >
            Send Invoice
          </b-button> -->
          <!-- Button: Print -->
          <b-button
            v-ripple.400="'rgba(186, 191, 199, 0.15)'"
            variant="outline-success"
            class="mb-75"
            block
            @click="printInvoice"
          >
            Imprimir
          </b-button>

          <!-- Button: Rechazar -->
          <b-button
            v-ripple.400="'rgba(186, 191, 199, 0.15)'"
            variant="outline-danger"
            class="mb-75"
            block
            @click="deniesCandidate"
          >
            Rechazar
          </b-button>

          <!-- Button: Pendiente -->
          <!-- :to="{ name: '', params: { id: $route.params.id } }" -->
          <b-button
            v-ripple.400="'rgba(186, 191, 199, 0.15)'"
            variant="outline-warning"
            class="mb-75"
            block
            @click="show"
          >
            Pendiente
          </b-button>

          <!-- Button: Add Payment -->
          <!-- v-b-toggle.sidebar-invoice-add-payment -->
          <b-button
            v-ripple.400="'rgba(255, 255, 255, 0.15)'"
            variant="success"
            class="mb-75"
            block
            @click="addScholar"
          >
            Aceptar
          </b-button>
          <div>
            <b-form-textarea
              v-if="showDetails"
              rows="10"
              placeholder="Ingresa el motivo"
              v-model="details"
            >Small:</b-form-textarea>
          </div>
          <b-button
            v-if="showDetails"
            v-ripple.400="'rgba(186, 191, 199, 0.15)'"
            variant="info"
            class="my-75"
            block
            @click="earringCandidate"
          >
            Guardar
          </b-button>
        </b-card>
      </b-col>
    </b-row>

    <!-- <invoice-sidebar-send-invoice />
    <invoice-sidebar-add-payment /> -->
  </section>
</template>

<script>
import { ref, onUnmounted } from '@vue/composition-api'
import store from '@/store'
import router from '@/router'
import {
  BRow, BCol, BCard, BCardBody, BButton, BAlert, BLink, VBToggle, BFormTextarea,
} from 'bootstrap-vue'
import Logo from '@core/layouts/components/Logo.vue'
import Ripple from 'vue-ripple-directive'
import useJwt from '@/auth/jwt/useJwt'
import invoiceStoreModule from './invoiceStoreModule'

// import InvoiceSidebarSendInvoice from './InvoiceSidebarSendInvoice.vue'
// import InvoiceSidebarAddPayment from './InvoiceSidebarAddPayment.vue'

export default {
  directives: {
    Ripple,
    'b-toggle': VBToggle,
  },
  components: {
    BRow,
    BCol,
    BCard,
    BCardBody,
    BButton,
    BAlert,
    BLink,
    BFormTextarea,

    Logo,
    // InvoiceSidebarAddPayment,
    // InvoiceSidebarSendInvoice,
  },
  setup() {
    const candidateData = ref(null)
    const paymentDetails = ref({})

    // Invoice Description
    // ? Your real data will contain this information
    const invoiceDescription = [
      {
        taskTitle: 'Native App Development',
        taskDescription: 'Developed a full stack native app using React Native, Bootstrap & Python',
        rate: '$60.00',
        hours: '30',
        total: '$1,800.00',
      },
      {
        taskTitle: 'UI Kit Design',
        taskDescription: 'Designed a UI kit for native app using Sketch, Figma & Adobe XD',
        rate: '$60.00',
        hours: '20',
        total: '$1200.00',
      },
    ]

    const INVOICE_APP_STORE_MODULE_NAME = 'app-candidate'

    // Register module
    if (!store.hasModule(INVOICE_APP_STORE_MODULE_NAME)) store.registerModule(INVOICE_APP_STORE_MODULE_NAME, invoiceStoreModule)

    // UnRegister on leave
    onUnmounted(() => {
      if (store.hasModule(INVOICE_APP_STORE_MODULE_NAME)) store.unregisterModule(INVOICE_APP_STORE_MODULE_NAME)
    })
    const parametro = router.currentRoute.params
    const { id } = parametro
    store.dispatch('app-candidate/fetchCandidate', { key: id })
      .then(response => {
        candidateData.value = response.data
        console.table(candidateData.documents)
      })
      .catch(error => {
        if (error.response.status === 404) {
          console.log('error 404')
          candidateData.value = undefined
        }
      })

    const printInvoice = () => {
      window.print()
    }

    return {
      candidateData,
      paymentDetails,
      invoiceDescription,
      printInvoice,
    }
  },
  data: () => ({
    showDetails: false,
    details: '',
  }),
  methods: {
    show() {
      this.showDetails = !this.showDetails
    },
    updateStatusData(newStatus, newDetails) {
      const dataUpdate = {
        id: this.candidateData.id,
        curp: this.candidateData.curp,
        rfc: this.candidateData.rfc,
        name: this.candidateData.name,
        last_name: this.candidateData.last_name,
        mothers_last_name: this.candidateData.mothers_last_name,
        gender: this.candidateData.gender,
        age: this.candidateData.age,
        height: this.candidateData.height,
        belongs_other_corporation: this.candidateData.belongs_other_corporation,
        date_create: this.candidateData.date_create,
        status: newStatus,
        details: newDetails,
      }
      return dataUpdate
    },
    updateStatusCandidate(status, details = '') {
      const data = this.updateStatusData(status, details)
      useJwt.updateCandidate(this.$route.params.id, data)
        .then(() => {
          console.log('Datos actualizados')
        })
        .catch(error => {
          console.log(error)
        })
    },
    addScholar() {
      console.log('Aceptado')
      useJwt.saveScholar({ candidate: this.$route.params.id })
        .then(() => {
          console.log('Prebecario Aceptado')
          const data = this.updateStatusCandidate('ACEPTADO')
          console.table(data)
        })
        .catch(error => {
          console.log(error)
        })
    },
    deniesCandidate() {
      this.updateStatusCandidate('RECHAZADO')
    },
    earringCandidate() {
      if (this.details !== '') {
        this.updateStatusCandidate('PENDIENTE', this.details)
      }
    },
    showCurp() {
      console.log(this.candidateData.documents.file_curp.split('/')[5])
      const fileName = this.candidateData.documents.file_curp.split('/')[5]
      useJwt.getDocument(fileName)
        .then(response => {
          // console.log('------ Visualizacion del documento')
          console.table(response)
          const blob = new Blob([response.data], { type: 'application/pdf' })
          const url = URL.createObjectURL(blob)
          window.open(url, 'Documnet', 'width=700,height=900')
        })
        .catch(error => {
          console.log(error)
        })
    },
  },
}
</script>

<style lang="scss" scoped>
@import "~@core/scss/base/pages/app-invoice.scss";
</style>

<style lang="scss">
@media print {

  // Global Styles
  body {
    background-color: transparent !important;
  }
  nav.header-navbar {
    display: none;
  }
  .main-menu {
    display: none;
  }
  .header-navbar-shadow {
    display: none !important;
  }
  .content.app-content {
    margin-left: 0;
    padding-top: 2rem !important;
  }
  footer.footer {
    display: none;
  }
  .card {
    background-color: transparent;
    box-shadow: none;
  }
  .customizer-toggle {
    display: none !important;
  }

  // Invoice Specific Styles
  .invoice-preview-wrapper {
    .row.invoice-preview {
      .col-md-8 {
        max-width: 100%;
        flex-grow: 1;
      }

      .invoice-preview-card {
        .card-body:nth-of-type(2) {
          .row {
              > .col-12 {
              max-width: 50% !important;
            }

            .col-12:nth-child(2) {
              display: flex;
              align-items: flex-start;
              justify-content: flex-end;
              margin-top: 0 !important;
            }
          }
        }
      }
    }

    // Action Right Col
    .invoice-actions {
      display: none;
    }
  }
}
</style>
