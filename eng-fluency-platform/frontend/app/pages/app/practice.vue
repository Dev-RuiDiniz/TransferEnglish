<script setup lang="ts">
const authStore = useAuthStore()
const config = useRuntimeConfig()
const router = useRouter()

const scenarios = ref([])
const loading = ref(true)

interface Scenario {
  id: string
  title: string
  description: string
  level: string
}

onMounted(async () => {
  if (!authStore.isAuthenticated) {
    router.push('/login')
    return
  }

  try {
    const { data } = await useFetch(`${config.public.apiBase}/linguistics/scenarios`, {
      headers: {
        Authorization: `Bearer ${authStore.token}`
      }
    })
    if (data.value) {
      scenarios.value = data.value as Scenario[]
    }
  } catch (err) {
    console.error('Failed to fetch scenarios:', err)
  } finally {
    loading.value = false
  }
})

// Mock data if empty for demo
const mockScenarios = [
  { id: '1', title: 'Job Interview', description: 'Practice a formal interview for a software role.', level: 'Advanced' },
  { id: '2', title: 'Coffee Shop', description: 'Order your favorite drink and chat with the barista.', level: 'Beginner' },
  { id: '3', title: 'Airport Check-in', description: 'Navigate the check-in process and baggage claim.', level: 'Intermediate' }
]

const displayedScenarios = computed(() => {
  return scenarios.value.length > 0 ? scenarios.value : mockScenarios
})
</script>

<template>
  <div class="min-h-screen bg-slate-950 text-slate-100 p-6 md:p-12">
    <div class="max-w-6xl mx-auto">
      <header class="mb-12">
        <h1 class="text-4xl font-bold bg-gradient-to-r from-indigo-400 to-cyan-400 bg-clip-text text-transparent mb-4">
          Fluency Practice
        </h1>
        <p class="text-slate-400 text-lg">Choose a scenario to start your AI-powered conversation session.</p>
      </header>

      <div v-if="loading" class="flex justify-center p-20">
        <div class="w-12 h-12 border-4 border-indigo-500 border-t-transparent rounded-full animate-spin"></div>
      </div>

      <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div 
          v-for="scenario in displayedScenarios" 
          :key="scenario.id"
          class="group bg-slate-900 border border-slate-800 rounded-3xl p-8 hover:border-indigo-500/50 hover:bg-slate-800/50 transition-all cursor-pointer relative overflow-hidden"
        >
          <div class="absolute top-0 right-0 p-4 flex gap-2">
            <span class="px-3 py-1 bg-cyan-500/10 border border-cyan-500/20 text-cyan-400 text-[10px] rounded-full uppercase font-bold tracking-wider flex items-center gap-1">
              <span class="w-2 h-2 bg-cyan-400 rounded-full animate-pulse"></span>
              Gemini AI
            </span>
            <span class="px-3 py-1 bg-indigo-500/10 border border-indigo-500/20 text-indigo-400 text-xs rounded-full uppercase font-bold tracking-wider">
              {{ scenario.level }}
            </span>
          </div>

          <h3 class="text-2xl font-bold mb-4 group-hover:text-indigo-400 transition-colors">{{ scenario.title }}</h3>
          <p class="text-slate-400 mb-8 leading-relaxed">{{ scenario.description }}</p>
          
          <button 
            @click="router.push({ path: '/app/conversation', query: { scenarioId: scenario.id } })"
            class="w-full py-4 bg-indigo-600 text-white rounded-2xl font-bold hover:bg-indigo-500 transition-all flex items-center justify-center gap-2"
          >
            Start Session
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z" clip-rule="evenodd" />
            </svg>
          </button>
        </div>
      </div>

      <!-- Quick Tips -->
      <footer class="mt-20 p-8 bg-indigo-500/5 border border-indigo-500/10 rounded-3xl">
        <h4 class="text-indigo-400 font-bold mb-4 flex items-center gap-2">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
            <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clip-rule="evenodd" />
          </svg>
          Fluency Tip
        </h4>
        <p class="text-slate-400">
          Try to speak naturally. Our AI tracks your "Initial Fluency Point" (IFP) by analyzing pauses, fillers, and sentence structure. 
          Don't worry about perfect grammar!
        </p>
      </footer>
    </div>
  </div>
</template>
