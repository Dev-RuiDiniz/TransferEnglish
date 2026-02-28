<script setup lang="ts">
const authStore = useAuthStore()
</script>

<template>
  <div class="min-h-screen bg-slate-900 text-white font-sans">
    <header class="border-b border-slate-800 bg-slate-900/50 backdrop-blur-md sticky top-0 z-50">
      <nav class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
        <div class="flex items-center gap-2">
          <div class="w-8 h-8 bg-indigo-600 rounded-lg flex items-center justify-center font-bold text-xl">L</div>
          <span class="text-xl font-bold tracking-tight">LuckArkman</span>
        </div>
        <div class="hidden md:flex items-center gap-8 text-sm font-medium text-slate-400">
          <NuxtLink :to="authStore.isAuthenticated ? '/app/dashboard' : '/'" class="hover:text-white transition-colors">Dashboard</NuxtLink>
          <NuxtLink to="/app/practice" class="hover:text-white transition-colors">Practice</NuxtLink>
          <NuxtLink to="/app/profile" class="hover:text-white transition-colors">Profile</NuxtLink>
        </div>
        <div class="flex items-center gap-4">
          <NuxtLink v-if="!authStore.isAuthenticated" to="/login" class="px-4 py-2 text-sm font-semibold bg-indigo-600 hover:bg-indigo-500 rounded-full transition-all shadow-lg shadow-indigo-500/20">
            Sign In
          </NuxtLink>
          <div v-else class="flex items-center gap-2">
            <span class="text-xs text-slate-500 mr-2">{{ authStore.user?.full_name }}</span>
            <NuxtLink to="/app/profile" class="w-8 h-8 bg-slate-800 rounded-full flex items-center justify-center border border-slate-700 hover:border-indigo-500 transition-all">
              {{ authStore.user?.full_name?.[0] || 'U' }}
            </NuxtLink>
          </div>
        </div>
      </nav>
    </header>
    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <slot />
    </main>
  </div>
</template>

<style>
body {
  margin: 0;
  background-color: #0f172a;
}
</style>
