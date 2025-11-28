import os
from data import db_session
from data.cources import Cource

def recreate_database():
    # Удаляем старую базу данных
    if os.path.exists("./db/blob.db"):
        os.remove("./db/blob.db")
        print("Старая база данных удалена")
    
    # Создаем новую базу с правильной структурой
    db_session.global_init("./db/blob.db")
    db = db_session.create_session()
    
    # Данные программ
    programs_data = [
        {
            "program_name": "Математика",
            "faculty": "Не указано",
            "pass_score": "130",
            "required_exams": "ИКТФИКТ  или Физика",
            "profile": "Не указано"
        },
        {
            "program_name": "Прикладная математика и информатика",
            "faculty": "Не указано",
            "pass_score": "212",
            "required_exams": "ИКТФИКТ  или Физика",
            "profile": "Не указано"
        },
        {
            "program_name": "Механика и математическое моделирование",
            "faculty": "Не указано",
            "pass_score": "181",
            "required_exams": "ИКТФИКТ  или Физика",
            "profile": "Не указано"
        },
        {
            "program_name": "Прикладная математика",
            "faculty": "Не указано",
            "pass_score": "174",
            "required_exams": "ИКТФИКТ  или Физика",
            "profile": "Не указано"
        },
        {
            "program_name": "Математика и компьютерные науки",
            "faculty": "Не указано",
            "pass_score": "159",
            "required_exams": "ИКТФИКТ  или Физика",
            "profile": "Не указано"
        },
        {
            "program_name": "Математика и компьютерные науки",
            "faculty": "Не указано",
            "pass_score": "187",
            "required_exams": "ИКТФИКТ  или Физика",
            "profile": "Не указано"
        },
        {
            "program_name": "Фундаментальная информатика и информационные технологии",
            "faculty": "Не указано",
            "pass_score": "236",
            "required_exams": "ИКТФИКТ  или Физика",
            "profile": "Не указано"
        },
        {
            "program_name": "Математическое обеспечение и администрирование информационных систем",
            "faculty": "Не указано",
            "pass_score": "251",
            "required_exams": "ИКТФИКТ  или Физика",
            "profile": "Не указано"
        },
        {
            "program_name": "Физика",
            "faculty": "Не указано",
            "pass_score": "136",
            "required_exams": "ФФизика",
            "profile": "Не указано"
        },
        {
            "program_name": "Радиофизика",
            "faculty": "Не указано",
            "pass_score": "143",
            "required_exams": "ФФизика",
            "profile": "Не указано"
        },
        {
            "program_name": "Химия",
            "faculty": "Не указано",
            "pass_score": "157",
            "required_exams": "ХХимия",
            "profile": "Не указано"
        },
        {
            "program_name": "Химия, физика и механика материалов",
            "faculty": "Не указано",
            "pass_score": "140",
            "required_exams": "ХХимия",
            "profile": "Не указано"
        },
        {
            "program_name": "Геология",
            "faculty": "Не указано",
            "pass_score": "136",
            "required_exams": "ИКТГФИКТ  или География  или Физика",
            "profile": "Не указано"
        },
        {
            "program_name": "География",
            "faculty": "Не указано",
            "pass_score": "139",
            "required_exams": "ГГеография",
            "profile": "Не указано"
        },
        {
            "program_name": "Экология и природопользование",
            "faculty": "Не указано",
            "pass_score": "152",
            "required_exams": "ББиология",
            "profile": "Не указано"
        },
        {
            "program_name": "Экология и природопользование",
            "faculty": "Не указано",
            "pass_score": "140",
            "required_exams": "ИКТБГИКТ  или Биология  или География",
            "profile": "Не указано"
        },
        {
            "program_name": "Биология",
            "faculty": "Не указано",
            "pass_score": "153",
            "required_exams": "ББиология",
            "profile": "Не указано"
        },
        {
            "program_name": "Почвоведение",
            "faculty": "Не указано",
            "pass_score": "141",
            "required_exams": "ББиология",
            "profile": "Не указано"
        },
        {
            "program_name": "Информатика и вычислительная техника",
            "faculty": "Не указано",
            "pass_score": "186",
            "required_exams": "ИКТФИКТ  или Физика",
            "profile": "Не указано"
        },
        {
            "program_name": "Информационные системы и технологии",
            "faculty": "Не указано",
            "pass_score": "235",
            "required_exams": "ИКТФИКТ  или Физика",
            "profile": "Не указано"
        },
        {
            "program_name": "Прикладная информатика",
            "faculty": "Не указано",
            "pass_score": "219",
            "required_exams": "ИКТФИКТ  или Физика",
            "profile": "Не указано"
        },
        {
            "program_name": "Прикладная информатика",
            "faculty": "Не указано",
            "pass_score": "212",
            "required_exams": "ИКТФИКТ  или Физика",
            "profile": "Не указано"
        },
        {
            "program_name": "Программная инженерия",
            "faculty": "Не указано",
            "pass_score": "254",
            "required_exams": "ИКТФИКТ  или Физика",
            "profile": "Не указано"
        },
        {
            "program_name": "Информационная безопасность",
            "faculty": "Не указано",
            "pass_score": "215",
            "required_exams": "ИКТФИКТ  или Физика",
            "profile": "Не указано"
        },
        {
            "program_name": "Инфокоммуникационные технологии и системы связи",
            "faculty": "Не указано",
            "pass_score": "200",
            "required_exams": "ИКТФИКТ  или Физика",
            "profile": "Не указано"
        }
    ]
    
    for program in programs_data:
        # Парсим требуемые экзамены
        required_exams = program["required_exams"]
        
        # Определяем какие предметы требуются
        math = "Математика" in required_exams or "ИКТ" in required_exams
        russian_lang = True  # Русский язык всегда требуется
        physics = "Физика" in required_exams
        it = "ИКТ" in required_exams or "Информатика" in required_exams
        sosial = "Обществознание" in required_exams
        chemystry = "Химия" in required_exams
        liter = "Литература" in required_exams
        geography = "География" in required_exams
        forein_lang = "Иностранный" in required_exams
        
        # Обрабатываем проходной балл
        pass_score = program["pass_score"]
        if pass_score == "new":
            c_ball = 200
        else:
            try:
                c_ball = int(pass_score)
            except ValueError:
                c_ball = 200
        
        # Создаем описание
        desc = f"Факультет: {program['faculty']}. Профиль: {program['profile']}. Требуемые ЕГЭ: {program['required_exams']}"
        
        # Создаем объект Cource
        cource = Cource(
            title=program["program_name"],
            desc=desc,
            c_ball=c_ball,
            math=math,
            russian_lang=russian_lang,
            physics=physics,
            it=it,
            sosial=sosial,
            chemystry=chemystry,
            liter=liter,
            geography=geography,
            forein_lang=forein_lang
        )
        
        db.add(cource)
    
    db.commit()
    db.close()
    
    print(f"Успешно создана новая база данных с {len(programs_data)} программами!")

if __name__ == "__main__":
    recreate_database()

