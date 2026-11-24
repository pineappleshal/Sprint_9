from dataclasses import dataclass, field
from pathlib import Path
from uuid import uuid4

from config import ROOT_DIR


@dataclass
class UserData:
    email: str
    username: str
    password: str = field(repr=False)
    first_name: str = 'Валерия'
    last_name: str = 'Кузина'

    @classmethod
    def unique(cls):
        suffix = uuid4().hex[:16]
        return cls(
            email=f'qa9_{suffix}@example.com',
            username=f'qa9_{suffix}@example.com',
            password=f'Fg9!{uuid4().hex[:16]}',
        )


@dataclass
class RecipeData:
    name: str = field(default_factory=lambda: f'Салат {uuid4().hex[:12]}')
    ingredient: str = 'соль'
    amount: str = '2'
    cooking_time: str = '10'
    description: str = 'Нарезать овощи, добавить соль и перемешать.'
    image_path: Path = field(default_factory=lambda: ROOT_DIR / 'assets' / 'recipe.png', repr=False)
