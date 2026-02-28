<script setup lang="ts">
const auth = useAuthStore()
const route = useRoute()
const scenarioId = route.query.scenarioId as string
</script>

<template>
  <div class="min-h-screen bg-slate-950 flex flex-col p-4 md:p-8">
    <header class="max-w-4xl w-full mx-auto flex items-center justify-between mb-8">
      <NuxtLink to="/app/dashboard" class="flex items-center gap-2 text-slate-400 hover:text-indigo-400 transition-colors">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path></svg>
        Back to Dashboard
      </NuxtLink>
      <div class="flex items-center gap-2">
        <div class="w-3 h-3 bg-green-500 rounded-full animate-pulse"></div>
        <span class="text-xs font-bold text-slate-500 uppercase tracking-widest">Live Session</span>
      </div>
    </header>

    <main class="flex-grow flex items-center justify-center">
      <AudioConversationCanvas 
        :tenant-id="auth.tenantId || 'default-tenant'" 
        :scenario-id="scenarioId"
      />
    </main>

    <footer class="max-w-4xl w-full mx-auto mt-8 py-6 border-t border-slate-900 text-center text-slate-600 text-[10px] font-bold uppercase tracking-widest">
      LuckArkman Gemini Engine v2.5 (Preview) • Google Generative AI Active
    </footer>
  </div>
</template>
