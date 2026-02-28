<script setup lang="ts">
const auth = useAuthStore()
const email = ref('')
const password = ref('')
const error = ref('')
const isLoading = ref(false)

const handleLogin = async () => {
  isLoading.value = true
  error.value = ''
  try {
    await auth.login(email.value, password.value)
    navigateTo('/app/dashboard')
  } catch (err: any) {
    error.value = err.message || 'Login failed. Please check your credentials.'
  } finally {
    isLoading.value = false
  }
}
</script>

<template>
  <div class="min-h-screen flex items-center justify-center bg-slate-950 p-4">
    <div class="w-full max-w-md bg-slate-900 border border-slate-800 rounded-3xl p-8 shadow-2xl backdrop-blur-xl">
      <div class="text-center mb-8">
        <h1 class="text-3xl font-bold bg-gradient-to-r from-indigo-400 to-cyan-400 bg-clip-text text-transparent">
          Welcome Back
        </h1>
        <p class="text-slate-400 mt-2">Continue your journey to fluency</p>
      </div>

      <div v-if="$route.query.registered" class="mb-6 bg-emerald-500/10 border border-emerald-500/20 text-emerald-400 p-4 rounded-xl text-sm text-center">
        Registration successful! Please log in with your new account.
      </div>

      <form @submit.prevent="handleLogin" class="space-y-6">
        <div>
          <label class="block text-sm font-medium text-slate-400 mb-2">Email Address</label>
          <input 
            v-model="email" 
            type="email" 
            required
            class="w-full px-4 py-3 bg-slate-800 border border-slate-700 rounded-xl text-slate-100 focus:outline-none focus:ring-2 focus:ring-indigo-500 transition-all"
            placeholder="you@example.com"
          >
        </div>
        
        <div>
          <label class="block text-sm font-medium text-slate-400 mb-2">Password</label>
          <input 
            v-model="password" 
            type="password" 
            required
            class="w-full px-4 py-3 bg-slate-800 border border-slate-700 rounded-xl text-slate-100 focus:outline-none focus:ring-2 focus:ring-indigo-500 transition-all"
            placeholder="••••••••"
          >
        </div>

        <div v-if="error" class="bg-rose-500/10 border border-rose-500/20 text-rose-400 p-3 rounded-lg text-sm">
          {{ error }}
        </div>

        <button 
          type="submit" 
          :disabled="isLoading"
          class="w-full py-3 bg-gradient-to-r from-indigo-500 to-cyan-500 text-white font-bold rounded-xl hover:opacity-90 transition-all disabled:opacity-50"
        >
          {{ isLoading ? 'Entering...' : 'Sign In' }}
        </button>
      </form>

      <p class="text-center mt-8 text-slate-500 text-sm">
        Don't have an account? 
        <NuxtLink to="/register" class="text-indigo-400 hover:underline">Sign up for free</NuxtLink>
      </p>
    </div>
  </div>
</template>
