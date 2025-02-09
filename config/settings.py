import os
from dotenv import load_dotenv

load_dotenv()

# GitHub API Configuration
GITHUB_API_TOKEN = os.getenv('GITHUB_TOKEN')
GITHUB_API_BASE_URL = 'https://api.github.com'

# OpenAI Configuration
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
OPENAI_MODEL = 'gpt-3.5-turbo'

# Database Configuration
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///agentorb.db')

# Web Application Settings
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
HOST = os.getenv('HOST', '0.0.0.0')
PORT = int(os.getenv('PORT', 8000))

# Cache Settings
CACHE_TTL = 3600  # 1 hour
REDIS_URL = os.getenv('REDIS_URL')