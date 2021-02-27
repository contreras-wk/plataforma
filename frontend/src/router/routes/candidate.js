export default [

  {
    path: '/prebecarios-registro',
    name: 'prebecarios-registro',
    component: () => import('@/views/candidates/CandidateRegister.vue'),
    meta: {
      requiresAuth: false,
      layout: 'full',
    },
  },
  {
    path: '/prebecarios-seleccion',
    name: 'prebecarios-seleccion',
    component: () => import('@/views/candidates/CandidatesSelection.vue'),
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
]
