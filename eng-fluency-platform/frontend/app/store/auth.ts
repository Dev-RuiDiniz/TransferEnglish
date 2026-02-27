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
            try {
                const { data, error } = await useFetch('/api/v1/login/access-token', {
                    method: 'POST',
                    body: { username: email, password },
                })

                if (error.value) throw error.value

                this.token = data.value.access_token
                // Decode JWT manually or fetch user profile
                await this.fetchUserProfile()

                // Save to localStorage or cookie
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

            try {
                const { data } = await useFetch('/api/v1/test-token', {
                    headers: {
                        Authorization: `Bearer ${this.token}`
                    }
                })
                if (data.value) {
                    this.user = data.value
                    this.tenantId = data.value.tenant_id
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
