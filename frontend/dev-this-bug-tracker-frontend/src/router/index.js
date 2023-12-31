import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/admin',
      name: 'admin',
      component: () => import('../views/AdminView.vue')
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/LoginView.vue')
    },
    {
      path: '/ceticket',
      name: 'create edit ticket',

      component: () => import('../components/Tickets/CreateEditTicket.vue')
    },
    {
      path: '/viewticket',
      name: 'view ticket',

      component: () => import('../components/Tickets/SingleTicket.vue')
    },
    {
      path: '/createUser',
      name: 'Create ticket',

      component: () => import('../components/Users/CreateEditUser.vue')
    }
  ]
})

export default router
