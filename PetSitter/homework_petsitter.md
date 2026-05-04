# Homework: PetSitter Marketplace API

Build a Django + DRF API for a pet services marketplace inspired by [Rover.com](https://www.rover.com/) — where pet owners can find and book pet sitters.

## Entity Relationship Diagram

```
┌─────────────────┐       ┌─────────────────────┐       ┌─────────────┐
│      User       │       │    SitterProfile     │       │   Service   │
│  (built-in)     │       │                      │       │             │
│─────────────────│       │──────────────────────│       │─────────────│
│ id           PK │──1:1──│ id                PK │       │ id       PK │
│ username        │       │ user_id    FK unique │       │ name unique │
│ email           │       │ bio                  │       │ description │
│ first_name      │       │ city                 │       └──────┬──────┘
│ last_name       │       │ years_experience     │              │
│ password        │       └──────────┬───────────┘              │
└────────┬────────┘                  │                          │
         │                           │ 1:N                      │ N:1
         │ 1:N                       ▼                          │
         │                 ┌─────────────────────┐              │
         │                 │   SitterService      │◄─────────────┘
         │                 │                      │
         │                 │──────────────────────│
         │                 │ id                PK │
         │                 │ sitter_id         FK │
         │                 │ service_id        FK │
         │                 │ price_per_day        │
         │                 │                      │
         │                 │ UNIQUE(sitter,service)│
         │                 └──────────┬───────────┘
         │                            │
         │                            │ 1:N
         ▼                            ▼
┌─────────────────┐       ┌──────────────────────────┐
│      Pet        │       │         Booking           │
│                 │       │                           │
│─────────────────│       │───────────────────────────│
│ id           PK │       │ id                     PK │
│ owner_id     FK │       │ owner_id               FK │
│ name            │  M:N  │ sitter_service_id      FK │
│ species         │◄─────►│ start_date                │
│ breed           │       │ end_date                  │
│ age             │       │ status                    │
└─────────────────┘       │ notes                     │
                          │ created_at                │
                          └───────────────────────────┘
```

## Entity Details

### User (Django built-in — `django.contrib.auth.models.User`)

Don't create this model — Django provides it. It already has `id`, `username`, `email`, `first_name`, `last_name`, `password`, and authentication. Import it with `from django.contrib.auth.models import User`.

### SitterProfile

A user who offers pet-sitting services. Not every user is a sitter — only those with a profile.

| Field | Type | Notes |
|-------|------|-------|
| user | OneToOneField → User | Each user can have at most one sitter profile. `on_delete=CASCADE`. |
| bio | TextField | Free-text introduction. Can be blank. |
| city | CharField(100) | Where the sitter is based. Used for searching. |
| years_experience | PositiveIntegerField | Default 0. |

`__str__`: Return something like `"Alice Johnson — Amsterdam"`

### Service

Predefined service types that sitters can offer.

| Field | Type | Notes |
|-------|------|-------|
| name | CharField(100) | Unique. Examples: `"Dog Walking"`, `"Boarding"`, `"Drop-in Visit"`. |
| description | TextField | What the service includes. Can be blank. |

Seed data: Create 3–4 services via the admin or a data migration.

### SitterService

The link between a sitter and a service — **with a price**. One sitter can offer multiple services, each at a different rate.

| Field | Type | Notes |
|-------|------|-------|
| sitter | ForeignKey → SitterProfile | `on_delete=CASCADE`. Use `related_name="services"`. |
| service | ForeignKey → Service | `on_delete=CASCADE`. |
| price_per_day | DecimalField(max_digits=8, decimal_places=2) | e.g., `25.00` |

Constraint: A sitter can only have **one price per service** → `unique_together = ("sitter", "service")`

`__str__`: Return something like `"Alice — Dog Walking ($25.00/day)"`

### Pet

A pet belonging to an owner (user).

| Field | Type | Notes |
|-------|------|-------|
| owner | ForeignKey → User | `on_delete=CASCADE`. Use `related_name="pets"`. |
| name | CharField(100) | e.g., `"Buddy"` |
| species | CharField(20) | Use `choices`: `dog`, `cat`, `bird`, `other`. |
| breed | CharField(100) | Can be blank. e.g., `"Golden Retriever"`. |
| age | PositiveIntegerField | Age in years. |

`__str__`: Return something like `"Buddy (Dog)"`

Tip: Use `get_species_display()` to get the human-readable label from choices.

### Booking

A pet owner books a sitter for a specific service, for one or more pets, over a date range.

| Field | Type | Notes |
|-------|------|-------|
| owner | ForeignKey → User | The person making the booking. `related_name="bookings"`. |
| sitter_service | ForeignKey → SitterService | Which sitter + which service. `related_name="bookings"`. |
| pets | ManyToManyField → Pet | Which pets are being cared for. `related_name="bookings"`. |
| start_date | DateField | |
| end_date | DateField | |
| status | CharField(20) | Use `choices`: `pending` (default), `confirmed`, `completed`, `cancelled`. |
| notes | TextField | Special instructions. Can be blank. |
| created_at | DateTimeField | `auto_now_add=True` — set automatically on creation. |

Add two `@property` methods:
- `num_days` → `(end_date - start_date).days or 1`
- `total_price` → `price_per_day × num_days`

## What to Build

### Phase 1: Models & Admin

- [ ] Create a Django project (`petsitter`) and an app (`marketplace`)
- [ ] Implement all 5 models based on the schema above
- [ ] Run `makemigrations` and `migrate`
- [ ] Register all models in `admin.py` with useful `list_display` and `search_fields`
- [ ] Create a superuser, seed sample data through the admin:
  - 3+ users (some sitters, some owners, some both)
  - 3–4 services
  - Sitters offering different services at different prices
  - Pets belonging to owner users
  - A few bookings

### Phase 2: DRF API

Install DRF (`uv add djangorestframework`) and build the following endpoints:

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/sitters/` | List all sitters (include city, services with prices) |
| GET | `/api/sitters/<id>/` | Sitter detail (bio, all services, prices) |
| GET | `/api/sitters/?city=amsterdam` | Filter sitters by city |
| GET | `/api/sitters/?service=boarding` | Filter sitters by service type |
| GET | `/api/pets/` | List current user's pets |
| POST | `/api/pets/` | Add a pet (auto-assign `owner` to current user) |
| GET | `/api/bookings/` | List current user's bookings |
| POST | `/api/bookings/` | Create a booking (validate dates, calculate price) |

For each endpoint:
- [ ] Create a serializer (use `ModelSerializer`)
- [ ] Create a view (use `@api_view` or `APIView`)
- [ ] Wire up URLs
- [ ] Test via DRF's browsable API at `http://127.0.0.1:8000/api/`

### Phase 3: Validation & Permissions

- [ ] Booking validation: `end_date` must be after `start_date`
- [ ] Booking validation: pets must belong to the booking owner
- [ ] Sitter list: nested serializer to include services with prices
- [ ] Permission: only authenticated users can create bookings / pets
- [ ] Permission: users can only see their own bookings and pets
- [ ] Auto-set `owner` on booking/pet creation from `request.user`

### Phase 4 (Stretch)

- [ ] Search sitters by **city + service + max price** in a single query
- [ ] Add a `PATCH /api/bookings/<id>/` to update booking status (sitter can confirm/cancel)
- [ ] Add pagination to sitter list
- [ ] Dockerize the project with `compose.yaml` + PostgreSQL
- [ ] Write tests for at least one endpoint using Django's test client

## Concepts You'll Practice

| Concept | Where |
|---------|-------|
| `OneToOneField` | User → SitterProfile |
| `ForeignKey` | Pet → User, SitterService → SitterProfile |
| `ManyToManyField` | Booking → Pet |
| `DecimalField` | Prices |
| `choices` | Pet species, Booking status |
| `unique_together` | One price per sitter per service |
| `@property` | Calculated `total_price`, `num_days` |
| `related_name` | Reverse lookups (`user.pets.all()`) |
| `auto_now_add` | `created_at` timestamp |
| `ModelSerializer` | DRF serialization |
| Nested serializers | Sitter with services list |
| `@api_view` / `APIView` | DRF views |
| `request.user` | Auto-assigning owner |
| Serializer validation | Date checks, ownership checks |
| `IsAuthenticated` | Protecting endpoints |
| Query params filtering | `/api/sitters/?city=amsterdam` |

## Getting Started

```bash
uv init petsitter && cd petsitter
uv add django djangorestframework
uv run django-admin startproject petsitter .
uv run python manage.py startapp marketplace
# → Add "marketplace" and "rest_framework" to INSTALLED_APPS
# → Start building your models in marketplace/models.py
```

## Tips

- Start with Phase 1. Get the admin working first — it's the fastest way to verify your models work.
- Use `uv run python manage.py shell` to experiment with ORM queries before building the API.
- For filtering, use `request.query_params.get("city", "")` in your DRF view and chain `.filter()` calls.
- Test everything via the browsable API — no frontend needed.
- Don't worry about user registration/login for now. Create users via the admin and use DRF's session auth (login at `/admin/` then browse the API).
