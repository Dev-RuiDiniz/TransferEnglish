# Manual de Uso - TransferEnglish

## 1. Estrutura do repositório

- `eng-fluency-platform/backend`: API FastAPI (porta `8000`)
- `eng-fluency-platform/frontend`: app Nuxt 3 (porta `3000`)
- `eng-fluency-platform/docker-compose.yml`: orquestra backend, frontend, postgres e redis

## 2. Pré-requisitos

- Docker Desktop + Docker Compose
- Node.js 20+ (para modo manual)
- Python 3.11+ (para modo manual)

## 3. Subir com Docker (recomendado)

No backend, crie o arquivo `eng-fluency-platform/backend/.env`:

```env
SECRET_KEY=dev-secret-key-local
DATABASE_URL=postgresql://postgres:postgres@db:5432/eng_fluency
REDIS_URL=redis://redis:6379/0
BACKEND_CORS_ORIGINS=["http://localhost:3000","http://localhost:8000"]
```

Depois execute:

```bash
cd eng-fluency-platform
docker compose up --build -d
```

Verificações:

```bash
docker compose ps
curl http://localhost:8000/api/v1/health
curl http://localhost:3000
```

Parar:

```bash
docker compose down
```

## 4. Rodar em modo manual (sem Docker)

### Backend

```bash
cd eng-fluency-platform/backend
python -m venv .venv
.venv/Scripts/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

> Observação: nesse modo você precisa ter PostgreSQL e Redis locais acessíveis pelas variáveis do `.env`.

### Frontend

```bash
cd eng-fluency-platform/frontend
npm install
npm run dev
```

## 5. Testes locais rápidos

Smoke tests:

```bash
curl http://localhost:8000/api/v1/health
curl http://localhost:8000/health
```

Fluxo de autenticação (exemplo):

1. `POST /api/v1/register`
2. `POST /api/v1/login/access-token`
3. `GET /api/v1/me` com `Authorization: Bearer <token>`

## 6. Problemas comuns

- Erro de Docker daemon (`dockerDesktopLinuxEngine`): abrir o Docker Desktop antes do `docker compose up`.
- Erro de `env_file` ausente: criar `eng-fluency-platform/backend/.env`.
- Frontend sem comunicação com API: confirmar `NUXT_PUBLIC_API_BASE=http://localhost:8000/api/v1`.
