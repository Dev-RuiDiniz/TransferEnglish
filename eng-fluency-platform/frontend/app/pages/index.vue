<script setup lang="ts">
// Home / Landing page
</script>

<template>
  <div class="space-y-8">
    <section class="text-center py-16">
      <h1 class="text-5xl font-extrabold tracking-tight mb-4 bg-gradient-to-r from-indigo-400 to-cyan-400 bg-clip-text text-transparent">
        Master English with AI
      </h1>
      <p class="text-xl text-slate-400 max-w-2xl mx-auto mb-8">
        Functional fluency in 6 months using Linguistic Transfer, Phonetic Analysis, and our unique Pressure Index.
      </p>
      <div class="flex gap-4 justify-center">
        <NuxtLink to="/login" class="px-6 py-3 bg-indigo-600 hover:bg-indigo-500 rounded-full font-semibold transition-all shadow-lg shadow-indigo-500/20">
          Get Started
        </NuxtLink>
        <NuxtLink to="/app/dashboard" class="px-6 py-3 bg-slate-800 hover:bg-slate-700 rounded-full font-semibold transition-all border border-slate-700">
          Go to Dashboard
        </NuxtLink>
      </div>
    </section>
    
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
      <div class="p-6 bg-slate-800/50 rounded-2xl border border-slate-700 hover:border-indigo-500 transition-all group">
        <div class="text-3xl mb-4">🗣️</div>
        <h3 class="text-lg font-bold mb-2 group-hover:text-indigo-400 transition-colors">Linguistic Transfer</h3>
        <p class="text-slate-400 text-sm">Leverage your native Portuguese with 500+ strategic cognates.</p>
      </div>
      <div class="p-6 bg-slate-800/50 rounded-2xl border border-slate-700 hover:border-indigo-500 transition-all group">
        <div class="text-3xl mb-4">🎙️</div>
        <h3 class="text-lg font-bold mb-2 group-hover:text-indigo-400 transition-colors">Phonetic Engine</h3>
        <p class="text-slate-400 text-sm">Real-time feedback on rhythm, stress, and vowel reduction.</p>
      </div>
      <div class="p-6 bg-slate-800/50 rounded-2xl border border-slate-700 hover:border-indigo-500 transition-all group">
        <div class="text-3xl mb-4">⚡</div>
        <h3 class="text-lg font-bold mb-2 group-hover:text-indigo-400 transition-colors">Pressure Mode</h3>
        <p class="text-slate-400 text-sm">Flash immersion tests to build spontaneous conversational skill.</p>
      </div>
    </div>
  </div>
</template>

