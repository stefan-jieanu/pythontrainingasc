# Practice

1. Clone the repository to your local machine.

2. Create your own branch.

3. Create a new branch using your name (e.g. john-doe). Write your solution in the same file with the task.

4. Commit and push your work.

5. Receive feedback. Mentors will review your solutions and provide feedback.

---

## PetSitter Marketplace API (`petsitter/`)

A Django + DRF REST API for a pet-sitting marketplace, similar to Rover.com. Pet owners can find sitters, register their pets, and create bookings.

### Setup

```bash
cd petsitter
python3 -m venv .venv
source .venv/bin/activate
pip install django djangorestframework
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### Endpoints

| Method | URL | Description |
|--------|-----|-------------|
| GET | `/api/sitters/` | List all sitters |
| GET | `/api/sitters/?city=amsterdam` | Filter sitters by city |
| GET | `/api/sitters/?service=boarding` | Filter sitters by service |
| GET | `/api/sitters/<id>/` | Sitter detail with services |
| GET | `/api/pets/` | List your pets (auth required) |
| POST | `/api/pets/` | Add a pet (auth required) |
| GET | `/api/bookings/` | List your bookings (auth required) |
| POST | `/api/bookings/` | Create a booking (auth required) |

### Admin

Go to `/admin/` to manage all data. Log in with your superuser credentials.
