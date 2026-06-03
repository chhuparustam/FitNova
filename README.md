# FitNova - Gym Management System

A comprehensive Gym Management System API built with **Django** and **Django REST Framework**. FitNova provides a modern backend solution for managing all aspects of a gym operation including members, trainers, subscriptions, and more.

## Features

- 👥 **Member Management** - Register and manage gym members
- 🏋️ **Trainer Management** - Manage trainers and their details
- 📅 **Subscription Plans** - Create and manage membership packages
- 💳 **Payment Processing** - Track payments and billing
- 📊 **API-First Design** - RESTful API for seamless integration
- 📚 **Auto-Generated API Documentation** - Interactive Swagger/OpenAPI documentation
- 🔒 **Django Admin Interface** - Built-in admin panel for management

## Tech Stack

- **Backend Framework**: Django 6.0.5+
- **API Framework**: Django REST Framework 3.17.1+
- **API Documentation**: drf-spectacular 0.29.0+
- **Python**: 3.13+
- **Package Manager**: uv
- **Database**: SQLite (development) / Configurable for production

## Project Structure

```
gym_management_system/
├── core/                    # Django project settings
│   ├── settings.py         # Project configuration
│   ├── urls.py            # Main URL routing
│   ├── wsgi.py            # WSGI configuration
│   └── asgi.py            # ASGI configuration
├── member/                 # Member app
│   ├── models.py          # Member models
│   ├── views.py           # Member viewsets/views
│   ├── api/               # API endpoints
│   └── migrations/        # Database migrations
├── trainer/               # Trainer app
│   ├── models.py          # Trainer models
│   ├── views.py           # Trainer viewsets/views
│   ├── api/               # API endpoints
│   └── migrations/        # Database migrations
├── subscription/          # Subscription app
│   ├── models.py          # Subscription models
│   ├── views.py           # Subscription viewsets/views
│   ├── api/               # API endpoints
│   └── migrations/        # Database migrations
├── db.sqlite3             # SQLite database
├── manage.py              # Django management script
├── pyproject.toml         # Project dependencies (uv)
└── README.md             # This file
```

## Installation & Setup

### Prerequisites
- Python 3.13 or higher
- uv (Python package manager)

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/chhuparustam/FitNova.git
   cd gym_management_system
   ```

2. **Install dependencies**
   ```bash
   uv sync
   ```

3. **Run migrations**
   ```bash
   python manage.py migrate
   ```

4. **Create a superuser** (for admin access)
   ```bash
   python manage.py createsuperuser
   ```

5. **Start the development server**
   ```bash
   python manage.py runserver
   ```

The API will be available at `http://localhost:8000`

## Usage

### API Documentation
- **Swagger UI**: `http://localhost:8000/api/schema/swagger-ui/`
- **ReDoc**: `http://localhost:8000/api/schema/redoc/`
- **OpenAPI Schema**: `http://localhost:8000/api/schema/`

### Admin Interface
- **URL**: `http://localhost:8000/admin/`
- Login with your superuser credentials

### Main API Endpoints
- **Members**: `/api/members/`
- **Trainers**: `/api/trainers/`
- **Subscriptions**: `/api/subscriptions/`

## Development

### Running Tests
```bash
python manage.py test
```

### Making Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

## Project Configuration

Key settings are located in `core/settings.py`:
- Database configuration
- Installed apps (member, trainer, subscription)
- REST Framework settings
- CORS and security settings

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Support

For issues, questions, or suggestions, please open an issue on the GitHub repository.

---

**Repository**: [chhuparustam/FitNova](https://github.com/chhuparustam/FitNova)
