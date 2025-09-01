# example-package

A modern Python package with complete CI/CD setup

[![CI/CD](https://github.com/serafinovsky/example-package/actions/workflows/ci.yml/badge.svg)](https://github.com/serafinovsky/example-package/actions/workflows/ci.yml)
[![PyPI version](https://badge.fury.io/py/example-package.svg)](https://badge.fury.io/py/example-package)
[![Python Versions](https://img.shields.io/pypi/pyversions/example-package.svg)](https://pypi.org/project/example-package/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Установка

```bash
pip install example-package
```

## Разработка

### Настройка среды разработки

```bash
# Клонирование репозитория
git clone https://github.com/serafinovsky/example-package.git
cd example-package

# Установка зависимостей
uv sync --dev
```

## Настройка после создания проекта

### 1. Инициализация Git репозитория

```bash
cd your-project-name
git init
git add .
git commit -m "feat: initial commit"
```

### 2. Создание GitHub репозитория

```bash
# Создайте репозиторий на GitHub, затем:
git remote add origin https://github.com/yourusername/your-project-name.git
git branch -M main
git push -u origin main
```

### 3. Настройка PyPI Trusted Publisher

#### 3.1. Быстрая настройка одним кликом

**👉 [Настроить Trusted Publisher для PyPI](https://pypi.org/manage/account/publishing/?provider=github&owner=serafinovsky&repository=example-package&workflow_filename=publish.yml)**

После перехода по ссылке:

1. Войдите в свой аккаунт PyPI (если еще не авторизованы)
2. Форма будет автоматически заполнена данными из вашего проекта:
   - **Provider**: GitHub
   - **Owner**: `serafinovsky`
   - **Repository**: `example-package`
   - **Workflow filename**: `publish.yml`
3. В поле **Project name** введите: `example-package`
4. Нажмите **"Add publisher"**

#### 3.2. Тестирование через TestPyPI (рекомендуется)

**👉 [Настроить на TestPyPI](https://test.pypi.org/manage/account/publishing/?provider=github&owner=serafinovsky&repository=example-package&workflow_filename=publish.yml)**

Сначала протестируйте публикацию на TestPyPI с теми же настройками.

#### 3.3. Как это работает

В вашем проекте уже настроен workflow `publish.yml` с:

- `permissions: id-token: write` - для OpenID Connect аутентификации
- `pypa/gh-action-pypi-publish@release/v1` - для автоматической публикации
- Публикация срабатывает при создании релиза или тега

### 4. Настройка Branch Protection

#### 4.1. Автоматическая настройка (рекомендуется)

Запустите скрипт для настройки защиты основной ветки:

```bash
# Убедитесь, что у вас установлен GitHub CLI
gh auth login

# Запустите скрипт настройки
./scripts/setup-branch-protection.sh
```

### 6. Настройка среды разработки

```bash
# Установите uv, если еще не установлен
curl -LsSf https://astral.sh/uv/install.sh | sh

# Установите зависимости для разработки
make dev-setup
```

## Работа с release-please

Release-please автоматически создает pull request'ы с новыми версиями на основе ваших коммитов.

### Формат коммитов

Используйте [Conventional Commits](https://www.conventionalcommits.org/ru/v1.0.0/) формат:

#### Типы изменений:

- **feat**: новая функциональность (увеличивает MINOR версию)
- **fix**: исправление багов (увеличивает PATCH версию)
- **BREAKING CHANGE**: критические изменения (увеличивает MAJOR версию)
- **docs**: изменения в документации
- **style**: форматирование, отсутствующие точки с запятой и т.д.
- **refactor**: рефакторинг кода
- **test**: добавление тестов
- **chore**: обслуживание, обновление зависимостей

#### Примеры коммитов:

```bash
# Новая функциональность
git commit -m "feat: add user authentication module"

# Исправление бага
git commit -m "fix: resolve memory leak in connection pool"

# Критическое изменение
git commit -m "feat!: change API response format

BREAKING CHANGE: response now returns data in 'result' field instead of 'data'"

# С областью (scope)
git commit -m "feat(api): add new endpoint for user profile"
git commit -m "fix(auth): handle expired tokens correctly"

# Документация
git commit -m "docs: add usage examples to README"

# Тесты
git commit -m "test: add unit tests for user service"

# Обновление зависимостей
git commit -m "chore: update dependencies to latest versions"
```

#### Примеры изменения версий:

- `0.1.0` → `0.1.1`: fix commits
- `0.1.0` → `0.2.0`: feat commits
- `0.1.0` → `1.0.0`: BREAKING CHANGE commits

### Процесс релиза

1. **Создание коммитов** с правильным форматом
2. **Push в main** ветку
3. **Release-please создаст PR** с обновленной версией и CHANGELOG
4. **Ревью и мерж PR** (может быть автоматическим)
5. **Автоматическая публикация** в PyPI при создании релиза

## Полезные ссылки

- [PyPI Trusted Publishing](https://docs.pypi.org/trusted-publishers/)
- [TestPyPI Trusted Publishing](https://test.pypi.org/help/#trusted-publishing)
- [Release Please Documentation](https://github.com/googleapis/release-please)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [GitHub CLI](https://cli.github.com/)
