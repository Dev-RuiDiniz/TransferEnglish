<script setup lang="ts">
import { onMounted } from 'vue'
import { useAuthStore } from '~/store/auth'

const auth = useAuthStore()

onMounted(() => {
  const token = useCookie('auth_token').value
  if (token && !auth.token) {
    auth.token = token
    auth.fetchUserProfile()
  }
})
</script>

<template>
  <NuxtLayout>
    <NuxtPage />
  </NuxtLayout>
</template>
