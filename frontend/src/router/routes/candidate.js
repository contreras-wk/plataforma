export default [

  {
    path: '/prebecarios-registro',
    name: 'prebecarios-registro',
    component: () => import('@/views/candidates/form/CandidateRegister.vue'),
    meta: {
      requiresAuth: false,
      layout: 'full',
    },
  },
  {
    path: '/prebecarios-seleccion',
    name: 'prebecarios-seleccion',
    component: () => import('@/views/candidates/selection/CandidatesSelection.vue'),
    meta: {
      requiresAuth: true,
      pageTitle: 'Prebecarios',
      breadcrumb: [
        {
          text: 'Selección',
          active: true,
        },
      ],
    },
  },
  {
    path: '/prebecario-detalles',
    name: 'prebecario-detalles',
    component: () => import('@/views/candidates/selection/CandidateSelectionDetails.vue'),
    meta: {
      requiresAuth: true,
      pageTitle: 'Prebecarios',
      breadcrumb: [
        {
          text: 'Detalles',
        },
      ],
    },
  },
]
