<script setup lang="ts">
const auth = useAuthStore()
const config = useRuntimeConfig()

const { data: progress } = await useFetch(`${config.public.apiBase}/analytics/me`, {
  headers: {
    Authorization: `Bearer ${auth.token}`
  }
})

const { data: mission } = await useFetch(`${config.public.apiBase}/recommendation/next-mission`, {
  headers: {
    Authorization: `Bearer ${auth.token}`
  }
})
</script>

<template>
  <div class="min-h-screen bg-slate-950 text-slate-100 p-8">
    <div class="max-w-6xl mx-auto">
      <header class="flex justify-between items-center mb-12">
        <div>
          <h1 class="text-4xl font-bold">Welcome, {{ auth.user?.full_name?.split(' ')[0] }}</h1>
          <p class="text-slate-400 mt-1">Your fluency journey is progressing well.</p>
        </div>
        <div class="flex items-center gap-4">
          <div class="text-right">
            <div class="text-xs font-bold uppercase tracking-widest text-indigo-400">Current IFP</div>
            <div class="text-2xl font-mono font-bold">{{ progress?.current_ifp || 0 }}%</div>
          </div>
          <button @click="auth.logout(); navigateTo('/login')" class="p-2 bg-slate-800 rounded-lg hover:bg-slate-700 transition-colors">
            Logout
          </button>
        </div>
      </header>

      <div class="grid grid-cols-1 lg:grid-cols-3 gap-8 mb-12">
        <!-- Next Mission Card -->
        <div class="lg:col-span-2 p-8 bg-gradient-to-br from-indigo-600 to-violet-700 rounded-3xl shadow-xl relative overflow-hidden group">
          <div class="relative z-10">
            <span class="px-3 py-1 bg-white/20 rounded-full text-xs font-bold uppercase tracking-widest mb-4 inline-block">Recommended Mission</span>
            <h2 class="text-3xl font-bold mb-2">{{ mission?.scenario || 'General Conversation' }}</h2>
            <p class="text-indigo-100 mb-6 max-w-md">{{ mission?.objective || 'Practice your spontaneous response skills.' }}</p>
            <NuxtLink to="/app/conversation" class="inline-flex items-center gap-2 px-6 py-3 bg-white text-indigo-600 font-bold rounded-xl hover:bg-indigo-50 transition-all">
              Start Session
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
            </NuxtLink>
          </div>
          <!-- Decorative SVG -->
          <svg class="absolute right-0 bottom-0 opacity-10 w-64 h-64 -mb-16 -mr-16 group-hover:scale-110 transition-transform" viewBox="0 0 200 200" fill="currentColor">
            <path d="M40,-62C53.3,-54.1,66.7,-43.3,73.1,-29.7C79.5,-16.1,78.9,0.3,73.5,14.6C68.1,28.9,57.9,41.1,45.4,50.1C33,59.2,18.3,65.1,2.8,61.3C-12.7,57.5,-28.9,44.1,-41,31.2C-53.1,18.3,-61,5.9,-61.8,-7.4C-62.5,-20.8,-56.1,-35.1,-45.5,-43.8C-35,-52.4,-20.3,-55.4,-5.2,-58.3C9.9,-61.2,19.8,-63.9,40,-62Z" transform="translate(100 100)" />
          </svg>
        </div>

        <!-- Metrics Side Card -->
        <div class="bg-slate-900 border border-slate-800 rounded-3xl p-6 flex flex-col justify-between">
          <div>
            <h3 class="text-lg font-bold mb-4">Mastery Graph</h3>
            <div class="h-40 flex items-end gap-2 px-2">
              <div v-for="(v, i) in progress?.fluency_evolution || [40, 55, 52, 65, 78]" :key="i"
                class="flex-1 bg-indigo-500/20 rounded-t-lg relative group transition-all"
                :style="{ height: `${v}%` }"
              >
                <div class="absolute -top-8 left-1/2 -translate-x-1/2 bg-slate-800 text-[10px] px-2 py-1 rounded opacity-0 group-hover:opacity-100 transition-opacity">
                  {{ v }}%
                </div>
                <div class="absolute inset-x-0 bottom-0 bg-indigo-500 rounded-t-lg h-1 group-hover:h-full transition-all opacity-50"></div>
              </div>
            </div>
            <div class="flex justify-between mt-2 text-[10px] text-slate-500 font-bold uppercase">
              <span>Start</span>
              <span>Current</span>
            </div>
          </div>
          
          <div class="mt-6 pt-6 border-t border-slate-800">
            <div class="flex justify-between items-center text-sm">
              <span class="text-slate-400">Total Sessions</span>
              <span class="font-mono text-indigo-400 font-bold">{{ progress?.sessions_count || 0 }}</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Quick Actions -->
      <section>
        <h3 class="text-xl font-bold mb-6">Continue Learning</h3>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          <div v-for="action in [
            { title: 'Phonetic Review', desc: 'Improve your vowel reduction', icon: '🎙️' },
            { title: 'Pressure Practice', desc: 'Survive the blitz mode', icon: '⚡' },
            { title: 'Scenario Library', desc: 'Pick your own challenge', icon: '📚' },
            { title: 'Enterprise Stats', desc: 'View B2B performance', icon: '🏢', link: '/app/admin/dashboard' }
          ]" :key="action.title" class="p-6 bg-slate-900/50 border border-slate-800 rounded-2xl hover:border-indigo-500/50 transition-all cursor-pointer group">
            <div class="text-2xl mb-4 grayscale group-hover:grayscale-0 transition-all">{{ action.icon }}</div>
            <h4 class="font-bold mb-1">{{ action.title }}</h4>
            <p class="text-xs text-slate-500">{{ action.desc }}</p>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>
