# Импорт всех SQLAlchemy-моделей проекта.
# Используется для корректной регистрации таблиц в metadata.

from app.models.restaurant import Restaurant
from app.models.menu_item import MenuItem
from app.models.offer import Offer