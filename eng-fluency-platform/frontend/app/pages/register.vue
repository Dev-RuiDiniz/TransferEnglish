<script setup lang="ts">
const config = useRuntimeConfig()
const fullName = ref('')
const email = ref('')
const password = ref('')
const orgName = ref('')
const error = ref('')
const isLoading = ref(false)

const handleRegister = async () => {
  isLoading.value = true
  error.value = ''
  try {
    await $fetch(`${config.public.apiBase}/register`, {
      method: 'POST',
      body: {
        email: email.value,
        password: password.value,
        full_name: fullName.value,
        organization_name: orgName.value
      }
    })
    // Redirect to login with success indicator
    navigateTo('/login?registered=true')
  } catch (err: any) {
    error.value = err.data?.detail || 'Registration failed. Please try again.'
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
          Create Account
        </h1>
        <p class="text-slate-400 mt-2">Start your journey to English fluency</p>
      </div>

      <form @submit.prevent="handleRegister" class="space-y-4">
        <div>
          <label class="block text-sm font-medium text-slate-400 mb-1.5">Full Name</label>
          <input 
            v-model="fullName" 
            type="text" 
            required
            class="w-full px-4 py-3 bg-slate-800 border border-slate-700 rounded-xl text-slate-100 focus:outline-none focus:ring-2 focus:ring-indigo-500 transition-all"
            placeholder="John Doe"
          >
        </div>

        <div>
          <label class="block text-sm font-medium text-slate-400 mb-1.5">Email Address</label>
          <input 
            v-model="email" 
            type="email" 
            required
            class="w-full px-4 py-3 bg-slate-800 border border-slate-700 rounded-xl text-slate-100 focus:outline-none focus:ring-2 focus:ring-indigo-500 transition-all"
            placeholder="you@example.com"
          >
        </div>

        <div>
          <label class="block text-sm font-medium text-slate-400 mb-1.5">Organization / School Name</label>
          <input 
            v-model="orgName" 
            type="text" 
            required
            class="w-full px-4 py-3 bg-slate-800 border border-slate-700 rounded-xl text-slate-100 focus:outline-none focus:ring-2 focus:ring-indigo-500 transition-all"
            placeholder="LuckArkman Academy"
          >
        </div>
        
        <div>
          <label class="block text-sm font-medium text-slate-400 mb-1.5">Password</label>
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
          class="w-full py-3 mt-4 bg-gradient-to-r from-indigo-500 to-cyan-500 text-white font-bold rounded-xl hover:opacity-90 transition-all disabled:opacity-50"
        >
          {{ isLoading ? 'Creating Account...' : 'Get Started Now' }}
        </button>
      </form>

      <p class="text-center mt-8 text-slate-500 text-sm">
        Already have an account? 
        <NuxtLink to="/login" class="text-indigo-400 hover:underline">Log in</NuxtLink>
      </p>
    </div>
  </div>
</template>
