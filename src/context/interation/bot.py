from ..config import get_db


class Bot:
    def __init__(self):
        self.db = get_db()

    def _get_skills(self):
        return self.db.all()

    def send_skills_to_choose(self):
        ...

    def get_choosed_skills(self):
        ...

    def get_vacant(self):
        ...

    def send_vacant(self):
        ...