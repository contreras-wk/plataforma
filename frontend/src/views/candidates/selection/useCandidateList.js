import { ref, watch, computed } from '@vue/composition-api'
import store from '@/store'

// Notification
import { useToast } from 'vue-toastification/composition'
import ToastificationContent from '@core/components/toastification/ToastificationContent.vue'

export default function useCandidateList() {
  // Use toast
  const toast = useToast()

  const refCandidateListTable = ref(null)

  // Table Handlers
  const tableColumns = [
    { key: 'id', label: '#', sortable: false },
    { key: 'curp', label: 'CURP', sortable: false },
    { key: 'name', label: 'Nombre', sortable: true },
    { key: 'last_name', label: 'Paterno', sortable: true },
    { key: 'mothers_last_name', label: 'Materno', sortable: true },
    { key: 'age', label: 'Edad', sortable: true },
    { key: 'height', label: 'Estatura', sortable: true },
    { key: 'date_create', label: 'Fecha Registro', sortable: true },
    { key: 'status', label: 'Estado Solicitud', sortable: true },
    { key: 'actions' },

  ]
  // const tableColumns = [
  //   { key: 'id', label: '#', sortable: true },
  //   { key: 'invoiceStatus', sortable: true },
  //   { key: 'client', sortable: true },
  //   { key: 'total', sortable: true, formatter: val => `$${val}` },
  //   { key: 'issuedDate', sortable: true },
  //   { key: 'balance', sortable: true },
  //   { key: 'actions' },
  // ]
  const perPage = ref(20)
  const totalInvoices = ref(0)
  const currentPage = ref(1)
  const perPageOptions = [20, 50, 100]
  const searchQuery = ref('')
  const sortBy = ref('id')
  const isSortDirDesc = ref(true)
  const statusFilter = ref(null)

  const dataMeta = computed(() => {
    const localItemsCount = refCandidateListTable.value ? refCandidateListTable.value.localItems.length : 0
    return {
      from: perPage.value * (currentPage.value - 1) + (localItemsCount ? 1 : 0),
      to: perPage.value * (currentPage.value - 1) + localItemsCount,
      of: totalInvoices.value,
    }
  })

  const refetchData = () => {
    refCandidateListTable.value.refresh()
  }

  watch([currentPage, perPage, searchQuery, statusFilter], () => {
    refetchData()
  })

  const fetchCandidates = (ctx, callback) => {
    store
      .dispatch('app-prebecarios/fetchCandidates', {
        q: searchQuery.value,
        perPage: perPage.value,
        page: currentPage.value,
        sortBy: sortBy.value,
        sortDesc: isSortDirDesc.value,
        status: statusFilter.value,
      })
      .then(response => {
        console.log(response)
        const { results, count } = response.data

        callback(results)
        totalInvoices.value = count
      })
      .catch(error => {
        console.log(error)
        toast({
          component: ToastificationContent,
          props: {
            title: 'Error al cargar los datos prebecarios',
            icon: 'AlertTriangleIcon',
            variant: 'danger',
          },
        })
      })
  }

  // *===============================================---*
  // *--------- UI ---------------------------------------*
  // *===============================================---*

  const resolveCandidateStatusVariantAndIcon = status => {
    if (status === 'Partial Payment') return { variant: 'warning', icon: 'PieChartIcon' }
    if (status === 'Paid') return { variant: 'success', icon: 'CheckCircleIcon' }
    if (status === 'Downloaded') return { variant: 'info', icon: 'ArrowDownCircleIcon' }
    if (status === 'Draft') return { variant: 'primary', icon: 'SaveIcon' }
    if (status === 'Aceptado') return { variant: 'secondary', icon: 'SendIcon' }
    if (status === 'Rechazado') return { variant: 'danger', icon: 'InfoIcon' }
    return { variant: 'secondary', icon: 'XIcon' }
  }

  const resolveClientAvatarVariant = status => {
    if (status === 'Partial Payment') return 'primary'
    if (status === 'Paid') return 'danger'
    if (status === 'Downloaded') return 'secondary'
    if (status === 'Draft') return 'warning'
    if (status === 'Sent') return 'info'
    if (status === 'Past Due') return 'success'
    return 'primary'
  }

  const statusCandidateVaiant = status => {
    if (status === 'RECHAZADO') return 'danger'
    if (status === 'PENDIENTE') return 'warning'
    if (status === 'ACEPTADO') return 'success'
    return 'info'
  }

  return {
    fetchCandidates,
    tableColumns,
    perPage,
    currentPage,
    totalInvoices,
    dataMeta,
    perPageOptions,
    searchQuery,
    sortBy,
    isSortDirDesc,
    refCandidateListTable,

    statusFilter,

    resolveCandidateStatusVariantAndIcon,
    resolveClientAvatarVariant,
    statusCandidateVaiant,

    refetchData,
  }
}
