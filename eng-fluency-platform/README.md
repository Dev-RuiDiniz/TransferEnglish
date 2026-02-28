# 🇬🇧 LuckArkman - English Fluency Platform with AI

![Status](https://img.shields.io/badge/Status-Production_Ready-green)
![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688?logo=fastapi)
![Nuxt 3](https://img.shields.io/badge/Frontend-Nuxt_3-00DC82?logo=nuxt.js)
![PostgreSQL](https://img.shields.io/badge/DB-PostgreSQL_RLS-336791?logo=postgresql)
![Kubernetes](https://img.shields.io/badge/Clusters-AWS_EKS-FF9900?logo=kubernetes)

Uma plataforma educacional disruptiva baseada em **Inteligência Artificial** e **Transferência Linguística**, projetada para levar brasileiros do nível básico à fluência funcional em até seis meses através de imersão fonética e interação de áudio em tempo real.

---

## 🎯 Proposta do Projeto

A maioria dos estudantes de inglês sofre com a "fluência travada" apesar de anos de estudo. Nossa solução foca no condicionamento do cérebro para o processamento automático da língua, utilizando três pilares fundamentais:

1.  **Transferência Linguística Estratégica**: Uso massivo de cognatos (palavras similares entre PT e EN) para reduzir a carga cognitiva e gerar confiança imediata.
2.  **Imersão Fonética Adaptativa**: IA que analisa não apenas o texto, mas a qualidade da fala (ritmo, entonação e redução vocálica).
3.  **Índice de Fluência sob Pressão (IFP)**: Métrica proprietária que mede a capacidade de resposta espontânea em situações imprevisíveis.

---

## 🚀 Recursos Finalizados

-   🎙️ **Conversação por Áudio em Tempo Real**: Fluxo completo via WebSockets (Whisper + GPT-4o + ElevenLabs).
-   📊 **Análise Fonética Azure**: Feedback detalhado por fonema e Heatmap de pronúncia.
-   ⚡ **Modo Pressão & Adaptação**: IA que ajusta a dificuldade dinamicamente e testa o aluno sob estresse.
-   🛡️ **Multi-tenancy RLS**: Isolamento total de dados para clientes B2B (Corporativo).
-   🎮 **Sistema de Gamificação**: Conquistas, níveis CEFR e XP integrados.
-   🏢 **Painel Administrativo B2B**: Gestão de funcionários e relatórios agregados via Pandas/PDF.
-   🔒 **Conformidade LGPD**: Sanitização de metadados de áudio e fluxo de purga de dados.
-   💳 **Pagamentos**: Integração com Stripe para assinaturas e licenciamento.

---

## 🛠️ Stack Tecnológica

### Backend
-   **Core**: Python 3.11+ & FastAPI.
-   **Database**: PostgreSQL com **Row-Level Security (RLS)**.
-   **Processing**: Pandas (Relatórios), ReportLab (PDF), Redis (Caching).

### Frontend
-   **Framework**: Nuxt 3 (Vue 3).
-   **Visuals**: Chart.js (Dashboards), TailwindCSS.

---

## 🗺️ Roadmap Finalizado (25 Sprints)

✅ **Fase 1: Fundação** | ✅ **Fase 2: Ciclo de Áudio** | ✅ **Fase 3: Inteligência Fonética** | ✅ **Fase 4: Gamificação** | ✅ **Fase 5: Adaptatividade & B2B** | ✅ **Fase 6: Otimização & Launch**

---

## 📦 Como Rodar (Simplificado)

### Docker Compose (Local)
```bash
docker-compose up --build
```

### Kubernetes (Deploy)
```bash
helm install eng-fluency-platform ./infra/k8s -f ./infra/k8s/values.yaml
```

### Desenvolvimento Manual
```bash
# Backend
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload

# Frontend
cd frontend
npm install
npm run dev
```

---

## 📄 Licença e Uso
Este projeto é uma propriedade privada focada no mercado educacional SaaS. Para parcerias ou acesso corporativo, entre em contato com **LuckArkman**.
