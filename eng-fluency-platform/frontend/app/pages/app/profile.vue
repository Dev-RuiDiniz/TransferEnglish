<script setup lang="ts">
const authStore = useAuthStore()
const router = useRouter()

// Ensure authenticated
onMounted(async () => {
  if (!authStore.isAuthenticated) {
    router.push('/login')
  } else if (!authStore.user) {
    await authStore.fetchUserProfile()
  }
})

const handleLogout = () => {
  authStore.logout()
  router.push('/login')
}
</script>

<template>
  <div class="min-h-screen bg-slate-950 text-slate-100 p-6 md:p-12">
    <div class="max-w-4xl mx-auto">
      <header class="flex justify-between items-center mb-12">
        <h1 class="text-4xl font-bold bg-gradient-to-r from-indigo-400 to-cyan-400 bg-clip-text text-transparent">
          User Profile
        </h1>
        <button 
          @click="handleLogout"
          class="px-6 py-2 bg-rose-500/10 border border-rose-500/20 text-rose-400 rounded-xl hover:bg-rose-500/20 transition-all font-medium"
        >
          Logout
        </button>
      </header>

      <div v-if="authStore.user" class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <!-- Profile Card -->
        <div class="md:col-span-1 bg-slate-900 border border-slate-800 rounded-3xl p-8 text-center">
          <div class="w-32 h-32 bg-gradient-to-br from-indigo-500 to-cyan-500 rounded-full mx-auto mb-6 flex items-center justify-center text-4xl font-bold">
            {{ authStore.user.full_name.charAt(0) }}
          </div>
          <h2 class="text-2xl font-bold mb-2">{{ authStore.user.full_name }}</h2>
          <p class="text-slate-400 mb-6">{{ authStore.user.role.toUpperCase() }}</p>
          <div class="flex flex-wrap justify-center gap-2">
            <span class="px-3 py-1 bg-indigo-500/10 border border-indigo-500/20 text-indigo-400 text-xs rounded-full">
              Tenant: {{ authStore.user.tenant_id }}
            </span>
          </div>
        </div>

        <!-- Account Settings -->
        <div class="md:col-span-2 bg-slate-900 border border-slate-800 rounded-3xl p-8">
          <h3 class="text-xl font-bold mb-6 border-b border-slate-800 pb-4">Account Information</h3>
          <div class="space-y-6">
            <div>
              <label class="block text-sm font-medium text-slate-400 mb-2">Email Address</label>
              <div class="w-full px-4 py-3 bg-slate-800/50 border border-slate-700/50 rounded-xl text-slate-300">
                {{ authStore.user.email }}
              </div>
            </div>
            <div>
              <label class="block text-sm font-medium text-slate-400 mb-2">Full Name</label>
              <div class="w-full px-4 py-3 bg-slate-800/50 border border-slate-700/50 rounded-xl text-slate-300">
                {{ authStore.user.full_name }}
              </div>
            </div>
            <div class="pt-6">
              <button disabled class="px-6 py-3 bg-slate-800 text-slate-500 border border-slate-700 rounded-xl cursor-not-allowed italic">
                Update functionality coming soon...
              </button>
            </div>
          </div>
        </div>
      </div>

      <div v-else class="flex flex-col items-center justify-center p-20 text-slate-500 italic">
        <div class="w-12 h-12 border-4 border-indigo-500 border-t-transparent rounded-full animate-spin mb-4"></div>
        Loading profile...
      </div>
    </div>
  </div>
</template>
