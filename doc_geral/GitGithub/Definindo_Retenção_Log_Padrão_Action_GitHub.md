# Tutorial Avançado: Controle de Retenção de Logs e Artefatos no GitHub Actions


## O que são os dois tipos de log

| Tipo                      | Geração automática? | Onde fica?                                       | Quem apaga?                                                     |
| ------------------------- | ------------------- | ------------------------------------------------ | --------------------------------------------------------------- |
| **Log padrão do Actions** | Sim                 | Interface → `Actions → Workflows → Runs → Steps` | GitHub apaga baseado na configuração de retenção do repositório |
| **Artefato `.zip`**       | Não, você gera      | Aba **Artifacts** no run                         | GitHub apaga baseado no `retention-days` do `upload-artifact`   |


## Como funciona o log padrão

Cada step do seu YAML (steps:) gera stdout e stderr.

O GitHub armazena isso automaticamente.

Você não precisa de upload-artifact para vê-los.

Limite de retenção: configurado globalmente para o repositório.

## Configurar retenção do log padrão

Passo a Passo:

- 1️⃣ Vá para o seu repositório no GitHub
- 2️⃣ Clique em Settings
- 3️⃣ Na lateral, clique em Actions
- 4️⃣ Vá até a seção Artifact and log retention
- 5️⃣ Lá tem:

```bash
Retention period for GitHub Actions artifacts and logs
```

O valor padrão é 90 dias
Pode reduzir para 1, 2, 7, 30, etc.

### Clique em Save

**Isso vale para todos os logs padrão de runs e artifacts que não tenham retention-days customizado.**

## Como funciona o upload-artifact

Se você quiser guardar arquivos que o seu pipeline gera (exemplo: log.txt, PDFs, relatórios de cobertura, screenshots), precisa:

1️⃣ Gerar esse arquivo dentro do job:

```yaml
run: echo "Minha saída detalhada" > meu_log.txt
```

2️⃣ Fazer upload com:

```yaml
- name: Upload do log como artefato com retenção de 1 dia
  uses: actions/upload-artifact@v4
  with:
    name: meu-log
    path: ./meu_log.txt
    retention-days: 1
```

Aqui você define retention-days só para este artefato, independente da regra global.

## Principal Diferença

| Recurso            | Você configura `retention-days`? | Onde?                                 |
| ------------------ | -------------------------------- | ------------------------------------- |
| Log padrão do step | ❌                                | Somente pelo **Settings → Actions**   |
| Artefato `.zip`    | ✅                                | Dentro do `upload-artifact` (`with:`) |

## Exemplo Completo

```yaml
name: Exemplo Retenção

on: [push]

jobs:
  teste-retencao:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Gera arquivo de log
        run: |
          echo "Executando meu script" > meu_log.txt
          echo "Erro simulado" >> meu_log.txt

      - name: Upload com retenção curta
        uses: actions/upload-artifact@v4
        with:
          name: artefato-com-log
          path: meu_log.txt
          retention-days: 2
```
Logs padrão: visíveis nos steps da run, expiram conforme Settings.

Artefato artefato-com-log: download na aba Artifacts, expira em 2 dias — mesmo que a configuração global seja 90 dias.

## Boas práticas

Use log padrão para debug de pipeline (rápido, sem custo de storage).

Use upload-artifact para:

    Logs persistentes (se quiser guardar stdout bruto).

    Relatórios que não cabem no log padrão (test coverage, PDF, ZIP).

    Builds binários (artefato real para deploy).


## Resumo

| Se quer controlar...             | Use                                                         |
| -------------------------------- | ----------------------------------------------------------- |
| **Retenção do log dos steps**    | Configure em **Settings → Actions → Retention**             |
| **Retenção de arquivos gerados** | Use `actions/upload-artifact` + `retention-days` no `with:` |
