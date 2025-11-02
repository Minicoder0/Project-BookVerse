# 📚 BookVerse - Digital Book Reading Platform

A modern, feature-rich digital book reading platform built with FastAPI and Python. Read PDFs, EPUBs, and MOBI files with beautiful UI, progress tracking, and subscription management.

![BookVerse](https://img.shields.io/badge/Python-3.11+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## ✨ Features

### 📖 Core Features
- **Multi-Format Support**: Read PDF, EPUB, and MOBI files
- **Beautiful PDF Reader**: Integrated native browser PDF viewer with purple gradient UI
- **User Authentication**: Secure signup, login, and session management
- **Reading Progress**: Automatic bookmark and progress tracking
- **Public Library**: Pre-loaded public domain books
- **Book Import**: Import free books from Gutendex (Project Gutenberg)
- **Personal Uploads**: Upload your own books (up to 50MB)

### 💎 Subscription Tiers
- **FREE**: Up to 5 books
- **PREMIUM**: Unlimited books (coming soon)
- **PRO**: Unlimited books + AI features (coming soon)

### 🎨 Modern UI
- Responsive design with Tailwind CSS
- Beautiful purple gradient reader interface
- Clean, intuitive navigation
- Mobile-friendly layout

## 🚀 Quick Deploy to Railway

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template)

### One-Click Deploy:
1. Click the button above
2. Connect GitHub account
3. Add PostgreSQL database
4. Set `SECRET_KEY` environment variable
5. **Done!** App is live in 3 minutes

**Detailed guide**: See [RAILWAY-DEPLOY.md](RAILWAY-DEPLOY.md)

## 💻 Local Development

### Prerequisites
- Python 3.11 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/Project-BookVerse.git
cd Project-BookVerse
```

2. **Create and activate virtual environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
```bash
# Copy example env file
cp .env.example .env

# Edit .env and set your SECRET_KEY
# Generate one with: python -c "import secrets; print(secrets.token_urlsafe(32))"
```

5. **Create storage directories**
```bash
mkdir -p storage/books storage/covers
```

6. **Initialize database**
```bash
alembic upgrade head
```

7. **Run the application**
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

8. **Open in browser**
```
http://localhost:8000
```

## 📖 Usage

### First Time Setup
1. Go to http://localhost:8000
2. Click "Sign Up" to create an account
3. Browse the public library or import free books
4. Click "Read" to start reading any book

### Uploading Books
1. Click "Upload" in the navigation
2. Choose a PDF, EPUB, or MOBI file (max 50MB)
3. Fill in title and author
4. Click "📤 Upload Book"

### Importing Free Books
1. Click "Import" in the navigation
2. Search by keyword or topic
3. Choose how many books to import (1-20)
4. Click "Import" or use "Quick seed" for 5 popular books

## 🛠️ Tech Stack

### Backend
- **FastAPI**: Modern Python web framework
- **SQLAlchemy**: SQL toolkit and ORM
- **Alembic**: Database migrations
- **Passlib**: Password hashing
- **Gunicorn**: Production WSGI server

### Frontend
- **Jinja2**: Template engine
- **Tailwind CSS**: Utility-first CSS (CDN)
- **Native Browser PDF Viewer**: Built-in PDF rendering

### Database
- **SQLite**: Development (default)
- **PostgreSQL**: Production (Railway/Heroku)

### External APIs
- **Gutendex**: Project Gutenberg books API

## 📁 Project Structure

```
Project-BookVerse/
├── app/
│   ├── models/           # Database models
│   ├── routers/          # API endpoints
│   ├── services/         # Business logic
│   ├── templates/        # Jinja2 templates
│   ├── config.py         # Configuration
│   ├── database.py       # Database setup
│   ├── main.py           # FastAPI app
│   └── security.py       # Password hashing
├── alembic/             # Database migrations
├── storage/             # File storage
│   ├── books/          # Book files
│   └── covers/         # Book covers
├── templates/           # HTML templates
├── static/             # Static files
├── Dockerfile          # Docker configuration
├── Procfile            # Railway/Heroku deployment
├── railway.json        # Railway config
├── requirements.txt    # Python dependencies
└── README.md
```

## 🚢 Deployment

### Railway (Recommended)
See detailed guide: [RAILWAY-DEPLOY.md](RAILWAY-DEPLOY.md)

```bash
# Quick deploy
railway init
railway up
```

### Docker
```bash
docker build -t bookverse .
docker run -p 8000:8000 bookverse
```

### Heroku
```bash
heroku create bookverse-app
heroku addons:create heroku-postgresql
git push heroku main
```

## 🔧 Configuration

### Environment Variables

```bash
# Security (Required)
SECRET_KEY=your-super-secret-key-here

# Environment
ENV=development  # or production

# Database
DATABASE_URL=sqlite:///./bookverse.db  # or postgresql://...

# Subscription Limits
FREE_BOOK_LIMIT=5
PREMIUM_BOOK_LIMIT=999999
PRO_BOOK_LIMIT=999999

# Upload Settings
MAX_UPLOAD_MB=50
```

## 📊 Database Schema

### Core Tables
- **users**: User accounts and authentication
- **subscriptions**: User subscription tiers
- **books**: Book metadata and file paths
- **reading_progress**: User reading progress
- **annotations**: User notes
- **highlights**: Text highlights
- **reading_sessions**: Analytics tracking
- **reading_stats**: User statistics

## 🎯 Roadmap

- [x] User authentication
- [x] PDF viewer with progress tracking
- [x] Book upload and import
- [x] Public book library
- [x] Subscription system
- [x] Railway deployment
- [ ] EPUB reader (epub.js)
- [ ] Annotations and highlights
- [ ] Stripe payment integration
- [ ] Reading analytics dashboard
- [ ] Mobile app
- [ ] Social features

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Project Gutenberg](https://www.gutenberg.org/) - Free ebook source
- [Gutendex](https://gutendex.com/) - Project Gutenberg API
- [FastAPI](https://fastapi.tiangolo.com/) - Web framework
- [Tailwind CSS](https://tailwindcss.com/) - CSS framework
- [Railway](https://railway.app/) - Deployment platform

## 📧 Contact

For questions or support, please open an issue on GitHub.

## 🌟 Star History

If you find this project useful, please consider giving it a star! ⭐

---

Made with ❤️ by BookVerse Team
