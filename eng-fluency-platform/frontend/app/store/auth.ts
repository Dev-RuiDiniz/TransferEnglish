import { defineStore } from 'pinia'

interface User {
    id: string
    email: string
    full_name: string
    tenant_id: string
    role: string
}

export const useAuthStore = defineStore('auth', {
    state: () => ({
        user: null as User | null,
        token: null as string | null,
        tenantId: null as string | null,
        loading: false,
    }),

    actions: {
        async login(email, password) {
            this.loading = true
            const config = useRuntimeConfig()
            try {
                // OAuth2 expects form data for access-token
                const formData = new URLSearchParams()
                formData.append('username', email)
                formData.append('password', password)

                const { data, error } = await useFetch(`${config.public.apiBase}/login/access-token`, {
                    method: 'POST',
                    body: formData,
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded'
                    }
                })

                if (error.value) throw error.value

                this.token = (data.value as any).access_token
                await this.fetchUserProfile()

                const cookie = useCookie('auth_token')
                cookie.value = this.token
            } catch (err) {
                console.error('Login failed:', err)
                throw err
            } finally {
                this.loading = false
            }
        },

        async fetchUserProfile() {
            if (!this.token) return
            const config = useRuntimeConfig()

            try {
                const { data } = await useFetch(`${config.public.apiBase}/me`, {
                    headers: {
                        Authorization: `Bearer ${this.token}`
                    }
                })
                if (data.value) {
                    this.user = data.value as User
                    this.tenantId = (data.value as User).tenant_id
                }
            } catch (err) {
                this.logout()
            }
        },

        logout() {
            this.user = null
            this.token = null
            this.tenantId = null
            const cookie = useCookie('auth_token')
            cookie.value = null
        }
    },

    getters: {
        isAuthenticated: (state) => !!state.token,
    }
})
