<script setup lang="ts">
const auth = useAuthStore()

onMounted(() => {
  const token = useCookie('auth_token').value
  if (token) {
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
