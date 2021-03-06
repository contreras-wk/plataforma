<template>
  <section class="invoice-preview-wrapper">

    <!-- Alert: No item found -->
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
          :to="{ name: 'apps-invoice-list'}"
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
                <b-col>

                </b-col>
              </div>
            </div>
          </b-card-body>

          <!-- Spacer -->
          <b-alert
          variant="secondary"
          show
          class="mb-0"
        >
          <h5 class="alert-body">
            Datos Personales
          </h5>
        </b-alert>
          <!-- <hr class="invoice-spacing"> -->

          <!-- Invoice Client & Payment Details -->
          <b-card-body
            v-if="candidateData"
            class="invoice-padding pt-0"
          >
            <b-row class="invoice-spacing">

              <!-- Col: Invoice To -->
              <b-col
                cols="12"
                xl="6"
                class="p-0"
              >
                <h6 class="mb-0">
                  CURP:
                </h6>
                <p class="card-text mb-25">
                  {{ candidateData.curp }}
                </p>
                <h6 class="card-text mb-0">
                  RFC:
                </h6>
                <p class="card-text mb-10">
                  {{ candidateData.rfc }}
                </p>
              </b-col>

              <!-- Col: Payment Details -->
              <b-col
                xl="6"
                cols="12"
                class="p-0 mt-xl-0 mt-2 d-flex justify-content-xl-end"
              >
                <div>
                  <table>
                    <tbody>
                      <tr calss="mb-1">
                        <td class="mb-1 pr-1">
                          Edad:
                        </td>
                        <td><span class="font-weight-bold">{{ candidateData.age }}</span></td>
                      </tr>
                      <tr>
                        <td class="pr-1">
                          Estatura:
                        </td>
                        <td><span class="font-weight-bold">{{ candidateData.height }} [cm]</span></td>
                      </tr>
                      <tr>
                        <td class="pr-1">
                          Genéro:
                        </td>
                        <td><span class="font-weight-bold" >{{ candidateData.gender }}</span></td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </b-col>
            </b-row>
          </b-card-body>

          <!-- Nivel de Studios -->
          <b-alert
            variant="secondary"
            show
            class="mb-0"
          >
            <h5 class="alert-body">
              Estudios
            </h5>
          </b-alert>

          <b-row class="invoice-spacing">
            <b-col
                xl="6"
                cols="12"
                class="p-0 mt-xl-0 mt-2 d-flex justify-content-xl-end"
              >
                <div>
                  <table>
                    <tbody>
                      <tr>
                        <td class="pr-1">
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
          </b-row>

          <!-- Dirección -->
          <b-alert
            variant="secondary"
            show
            class="mb-0"
          >
            <h5 class="alert-body">
              Dirección
            </h5>
          </b-alert>

          <b-row class="invoice-spacing">
            <b-col
                xl="6"
                cols="12"
                class="p-0 mt-xl-0 mt-2 d-flex justify-content-xl-end"
              >
                <div>
                  <table>
                    <tbody>
                      <tr>
                        <td class="pr-1">
                          Ligar de residencia:
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
                        <td><span class="font-weight-bold" >{{ candidateData.direction.suburb }}</span></td>
                      </tr>
                      <tr>
                        <td class="pr-1">
                          Código Postal:
                        </td>
                        <td><span class="font-weight-bold" >{{ candidateData.direction.postal_code }}</span></td>
                      </tr>
                      <tr>
                        <td class="pr-1">
                          Calle:
                        </td>
                        <td><span class="font-weight-bold" >{{ candidateData.direction.street }}</span></td>
                      </tr>
                      <tr>
                        <td class="pr-1">
                          Número Exterior:
                        </td>
                        <td><span class="font-weight-bold" >{{ candidateData.direction.num_outdoor }}</span></td>
                      </tr>
                      <tr>
                        <td class="pr-1">
                          Número Interior:
                        </td>
                        <td><span class="font-weight-bold" >{{ candidateData.direction.num_inside }}</span></td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </b-col>
          </b-row>

          <!-- Invoice Description: Table -->
          <b-table-lite
            responsive
            :items="invoiceDescription"
            :fields="['taskDescription', 'rate', 'hours', 'total']"
          >
            <template #cell(taskDescription)="data">
              <b-card-text class="font-weight-bold mb-25">
                {{ data.item.taskTitle }}
              </b-card-text>
              <b-card-text class="text-nowrap">
                {{ data.item.taskDescription }}
              </b-card-text>
            </template>
          </b-table-lite>

          <!-- Invoice Description: Total -->
          <b-card-body class="invoice-padding pb-0">
            <b-row>

              <!-- Col: Sales Persion -->
              <b-col
                cols="12"
                md="6"
                class="mt-md-0 mt-3"
                order="2"
                order-md="1"
              >
                <b-card-text class="mb-0">
                  <span class="font-weight-bold">Salesperson:</span>
                  <span class="ml-75">Alfie Solomons</span>
                </b-card-text>
              </b-col>

              <!-- Col: Total -->
              <b-col
                cols="12"
                md="6"
                class="mt-md-6 d-flex justify-content-end"
                order="1"
                order-md="2"
              >
                <div class="invoice-total-wrapper">
                  <div class="invoice-total-item">
                    <p class="invoice-total-title">
                      Subtotal:
                    </p>
                    <p class="invoice-total-amount">
                      $1800
                    </p>
                  </div>
                  <div class="invoice-total-item">
                    <p class="invoice-total-title">
                      Discount:
                    </p>
                    <p class="invoice-total-amount">
                      $28
                    </p>
                  </div>
                  <div class="invoice-total-item">
                    <p class="invoice-total-title">
                      Tax:
                    </p>
                    <p class="invoice-total-amount">
                      21%
                    </p>
                  </div>
                  <hr class="my-50">
                  <div class="invoice-total-item">
                    <p class="invoice-total-title">
                      Total:
                    </p>
                    <p class="invoice-total-amount">
                      $1690
                    </p>
                  </div>
                </div>
              </b-col>
            </b-row>
          </b-card-body>

          <!-- Spacer -->
          <hr class="invoice-spacing">

          <!-- Note -->
          <b-card-body class="invoice-padding pt-0">
            <span class="font-weight-bold">Note: </span>
            <span>It was a pleasure working with you and your team. We hope you will keep us in mind for future freelance
              projects. Thank You!</span>
          </b-card-body>
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
          <b-button
            v-ripple.400="'rgba(255, 255, 255, 0.15)'"
            v-b-toggle.sidebar-send-invoice
            variant="primary"
            class="mb-75"
            block
          >
            Send Invoice
          </b-button>

          <!-- Button: DOwnload -->
          <b-button
            v-ripple.400="'rgba(186, 191, 199, 0.15)'"
            variant="outline-secondary"
            class="mb-75"
            block
          >
            Download
          </b-button>

          <!-- Button: Print -->
          <b-button
            v-ripple.400="'rgba(186, 191, 199, 0.15)'"
            variant="outline-secondary"
            class="mb-75"
            block
            @click="printInvoice"
          >
            Imprimir
          </b-button>

          <!-- Button: Edit -->
          <b-button
            v-ripple.400="'rgba(186, 191, 199, 0.15)'"
            variant="outline-secondary"
            class="mb-75"
            block
            :to="{ name: 'apps-invoice-edit', params: { id: $route.params.id } }"
          >
            Pendiente
          </b-button>

          <!-- Button: Add Payment -->
          <b-button
            v-b-toggle.sidebar-invoice-add-payment
            v-ripple.400="'rgba(255, 255, 255, 0.15)'"
            variant="success"
            class="mb-75"
            block
          >
            Aceptar
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
  BRow, BCol, BCard, BCardBody, BTableLite, BCardText, BButton, BAlert, BLink, VBToggle,
} from 'bootstrap-vue'
import Logo from '@core/layouts/components/Logo.vue'
import Ripple from 'vue-ripple-directive'
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
    BTableLite,
    BCardText,
    BButton,
    BAlert,
    BLink,

    Logo,
    // InvoiceSidebarAddPayment,
    // InvoiceSidebarSendInvoice,
  },
  data: () => ({
    gender: '',
  }),
  setup() {
    console.log('ENTRO AL SETUP')
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

    const INVOICE_APP_STORE_MODULE_NAME = 'app-invoice'

    // Register module
    if (!store.hasModule(INVOICE_APP_STORE_MODULE_NAME)) store.registerModule(INVOICE_APP_STORE_MODULE_NAME, invoiceStoreModule)

    // UnRegister on leave
    onUnmounted(() => {
      if (store.hasModule(INVOICE_APP_STORE_MODULE_NAME)) store.unregisterModule(INVOICE_APP_STORE_MODULE_NAME)
    })
    console.log('zzzzzzzzzzzzzzzzzz')
    console.log(router.currentRoute.params.id)
    store.dispatch('app-invoice/fetchCandidate', { id: router.currentRoute.params.id })
      .then(response => {
        console.log('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        console.log(response)
        candidateData.value = response.data
        // paymentDetails.value = response.data.paymentDetails
        console.log('///////////////////////////////////////////////')
        console.log(candidateData)
      })
      .catch(error => {
        if (error.response.status === 404) {
          console.log('error 404')
          candidateData.value = undefined
        }
        console.log('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        console.log(error)
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
