export const useAudioRecorder = (tenantId: string) => {
    const socket = ref<WebSocket | null>(null)
    const isRecording = ref(false)
    const mediaRecorder = ref<MediaRecorder | null>(null)
    const audioChunks = ref<Blob[]>([])

    const connect = () => {
        const config = useRuntimeConfig()
        const wsUrl = `${config.public.wsBase}/${tenantId}`

        socket.value = new WebSocket(wsUrl)

        socket.value.onopen = () => {
            console.log('Audio WebSocket connected to', wsUrl)
        }

        socket.value.onmessage = (event) => {
            const response = JSON.parse(event.data)
            console.log('WS Message:', response)
        }

        socket.value.onerror = (error) => {
            console.error('WebSocket Error:', error)
        }

        socket.value.onclose = () => {
            console.log('WebSocket closed')
        }
    }

    const startRecording = async () => {
        if (!socket.value || socket.value.readyState !== WebSocket.OPEN) {
            connect()
        }

        try {
            const stream = await navigator.mediaDevices.getUserMedia({ audio: true })
            mediaRecorder.value = new MediaRecorder(stream)

            mediaRecorder.value.ondataavailable = (event) => {
                if (event.data.size > 0 && socket.value?.readyState === WebSocket.OPEN) {
                    socket.value.send(event.data)
                }
            }

            mediaRecorder.value.start(250) // Send chunk every 250ms
            isRecording.value = true
        } catch (err) {
            console.error('Error starting recording:', err)
        }
    }

    const stopRecording = () => {
        if (mediaRecorder.value) {
            mediaRecorder.value.stop()
            mediaRecorder.value.stream.getTracks().forEach(track => track.stop())
        }
        isRecording.value = false
    }

    onUnmounted(() => {
        if (socket.value) {
            socket.value.close()
        }
    })

    return {
        isRecording,
        startRecording,
        stopRecording,
        connect
    }
}
