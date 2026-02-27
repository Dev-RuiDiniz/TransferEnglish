<template>
  <div class="min-h-screen bg-slate-900 text-white font-sans">
    <header class="border-b border-slate-800 bg-slate-900/50 backdrop-blur-md sticky top-0 z-50">
      <nav class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
        <div class="flex items-center gap-2">
          <div class="w-8 h-8 bg-indigo-600 rounded-lg flex items-center justify-center font-bold text-xl">L</div>
          <span class="text-xl font-bold tracking-tight">LuckArkman</span>
        </div>
        <div class="hidden md:flex items-center gap-8 text-sm font-medium text-slate-400">
          <NuxtLink to="/" class="hover:text-white transition-colors">Dashboard</NuxtLink>
          <NuxtLink to="/practice" class="hover:text-white transition-colors">Practice</NuxtLink>
          <NuxtLink to="/profile" class="hover:text-white transition-colors">Profile</NuxtLink>
        </div>
        <div class="flex items-center gap-4">
          <button class="px-4 py-2 text-sm font-semibold bg-indigo-600 hover:bg-indigo-500 rounded-full transition-all shadow-lg shadow-indigo-500/20">
            Sign In
          </button>
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
