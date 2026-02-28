// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',
  devtools: { enabled: false },
  modules: ['@nuxtjs/tailwindcss', '@pinia/nuxt'],
  future: {
    compatibilityVersion: 4,
  },
  pinia: {
    storesDirs: ['./app/store/**']
  },
  imports: {
    dirs: [
      'app/store',
      'app/composables',
    ]
  },
  runtimeConfig: {
    public: {
      apiBase: process.env.NUXT_PUBLIC_API_BASE || 'http://localhost:8000/api/v1',
      wsBase: process.env.NUXT_PUBLIC_WS_BASE || 'ws://localhost:8000/ws/audio'
    }
  }
})
