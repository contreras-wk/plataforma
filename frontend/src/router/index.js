import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '@/store'

// ROUTES
import candidate from './routes/candidate'

Vue.use(VueRouter)

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  scrollBehavior() {
    return { x: 0, y: 0 }
  },
  routes: [
    // PATH BASICS - NOT AUTHENTICATED
    {
      path: '/',
      name: 'home',
      component: () => import('@/views/Home.vue'),
      meta: {
        requiresAuth: false,
        layout: 'full',
      },
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('@/views/auth/Login.vue'),
      meta: {
        requiresAuth: false,
        layout: 'full',
      },
    },
    {
      path: '/error-404',
      name: 'error-404',
      component: () => import('@/views/error/Error404.vue'),
      meta: {
        requiresAuth: false,
        layout: 'full',
      },
    },
    {
      path: '*',
      redirect: 'error-404',
    },
    ...candidate,
  ],
})
router.beforeEach((to, from, next) => {
  const auth = to.meta.requiresAuth
  const logged = !store.state.user.isAuthenticated

  console.log(`path: ${to.path} | auth: ${auth} | logged: ${logged}`)
  console.log('#######################')

  if (auth && logged) {
    console.log('Entro -> Login')
    return next({ name: 'login' })
  }
  console.log('Default')
  return next()
})

export default router

// {
//   path: '/second-page',
//   name: 'second-page',
//   component: () => import('@/views/SecondPage.vue'),
//   meta: {
//     requiresAuth: true,
//     pageTitle: 'Second Page',
//     breadcrumb: [
//       {
//         text: 'Second Page',
//         active: true,
//       },
//     ],
//   },
// },
