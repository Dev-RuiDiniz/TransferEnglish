# 🇬🇧 English Fluency Platform with AI

![Status](https://img.shields.io/badge/Status-In_Development-orange)
![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688?logo=fastapi)
![Nuxt 3](https://img.shields.io/badge/Frontend-Nuxt_3-00DC82?logo=nuxt.js)
![PostgreSQL](https://img.shields.io/badge/DB-PostgreSQL_RLS-336791?logo=postgresql)

Uma plataforma educacional disruptiva baseada em **Inteligência Artificial** e **Transferência Linguística**, projetada para levar brasileiros do nível básico à fluência funcional em até seis meses através de imersão fonética e interação de áudio em tempo real.

---

## 🎯 Proposta do Projeto

A maioria dos estudantes de inglês sofre com a "fluência travada" apesar de anos de estudo. Nossa solução foca no condicionamento do cérebro para o processamento automático da língua, utilizando três pilares fundamentais:

1.  **Transferência Linguística Estratégica**: Uso massivo de cognatos (palavras similares entre PT e EN) para reduzir a carga cognitiva e gerar confiança imediata.
2.  **Imersão Fonética Adaptativa**: IA que analisa não apenas o texto, mas a qualidade da fala (ritmo, entonação e redução vocálica).
3.  **Índice de Fluência sob Pressão (IFP)**: Métrica proprietária que mede a capacidade de resposta espontânea em situações imprevisíveis.

---

## 🚀 Principais Recursos

-   🎙️ **Conversação Exclusiva por Áudio**: Interação natural com um tutor de IA em tempo real.
-   📊 **Análise Fonética Profunda**: Feedback visual detalhado sobre pronúncia e ritmo (stress-timed).
-   ⚡ **Testes Relâmpago (Pressure Mode)**: Desafios imersivos surpresa para validar a fluência sob pressão.
-   🛡️ **Arquitetura Multi-tenant**: Isolamento total de dados entre usuários individuais e corporativos (B2B).
-   🎮 **Gamificação Pedagógica**: Desbloqueio de habilidades reais e níveis baseados no CEFR (A1 a C2).
-   📈 **Dashboard de Evolução**: Mapa de calor fonético e histórico de progresso do IFP.

---

## 🛠️ Stack Tecnológica

### Backend (Clean Architecture)
-   **Core**: Python 3.11+ & FastAPI.
-   **Database**: PostgreSQL com **Row-Level Security (RLS)** para multi-tenancy.
-   **Async Operations**: Redis & Celery.
-   **Auth**: JWT com injeção de contexto de tenant.

### Frontend (Modular & High Performance)
-   **Framework**: Nuxt 3 (Vue 3).
-   **Store**: Pinia (Gerenciamento de contexto do Tenant).
-   **Styling**: TailwindCSS.
-   **Audio**: Web Audio API para streaming de baixa latência.

### IA & Processamento de Sinais
-   **ASR (Fala-Texto)**: OpenAI Whisper.
-   **LLM (Lógica)**: GPT-4o.
-   **TTS (Texto-Fala)**: ElevenLabs / OpenAI TTS.
-   **Phonetics**: Azure Speech Services (Análise de pronúncia).

---

## 📄 Licença e Uso
Este projeto é uma propriedade privada focada no mercado educacional SaaS. Para parcerias ou acesso corporativo, entre em contato.
