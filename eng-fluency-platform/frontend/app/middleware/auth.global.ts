export default defineNuxtRouteMiddleware((to, from) => {
    const auth = useAuthStore()

    // If user is at / and is logged in, send to dashboard
    if (to.path === '/' && auth.isAuthenticated) {
        return navigateTo('/app/dashboard')
    }

    // Protection for /app/* routes
    if (to.path.startsWith('/app') && !auth.isAuthenticated) {
        return navigateTo('/login')
    }
})
