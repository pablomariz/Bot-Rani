from ..config import get_db

BASE_URL = ""

class SkillsScrapper:
    def __init__(self):
        self.db = get_db()

    def __get_skills_on_internet(self):
        ...

    def __persiste_a_new_categorie(self, categorie):
        ...

    def __persiste_skill_by_categorie(self, skill, categorie):
        ...

    def get_skills(self):
        return ["python", "sql"]

    def get_categories(self):
        ...
    
    def get_skills_by_categorie(self):
        ...