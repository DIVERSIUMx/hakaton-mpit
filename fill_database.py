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
            "faculty": "Математический факультет",
            "pass_score": "130",
            "required_exams": "ИКТ или Физика",
            "profile": "Дифференциальные уравнения, динамические системы и оптимальное управление"
        },
        {
            "program_name": "Прикладная математика и информатика",
            "faculty": "Факультет прикладной математики, информатики и механики",
            "pass_score": "212",
            "required_exams": "ИКТ или Физика",
            "profile": "Прикладная математика и компьютерные технологии"
        },
        {
            "program_name": "Механика и математическое моделирование",
            "faculty": "Факультет прикладной математики, информатики и механики",
            "pass_score": "181",
            "required_exams": "ИКТ или Физика",
            "profile": "Компьютерный инжиниринг в механике сплошных сред"
        },
        {
            "program_name": "Прикладная математика",
            "faculty": "Математический Факультет",
            "pass_score": "174",
            "required_exams": "ИКТ или Физика",
            "profile": "Применение математических методов к решению инженерных и экономических задач"
        },
        {
            "program_name": "Математика и компьютерные науки",
            "faculty": "Не указано",
            "pass_score": "159",
            "required_exams": "ИКТ или Физика",
            "profile": "Не указано"
        },
        {
            "program_name": "Математика и компьютерные науки",
            "faculty": "Факультет компьютерных наук",
            "pass_score": "187",
            "required_exams": "ИКТ или Физика",
            "profile": "Математическое и программное обеспечение информационных систем и технологий"
        },
        {
            "program_name": "Фундаментальная информатика и информационные технологии",
            "faculty": "Факультет прикладной математики, информатики и механики",
            "pass_score": "236",
            "required_exams": "ИКТ или Физика",
            "profile": "Инженерия программного обеспечения"
        },
        {
            "program_name": "Математическое обеспечение и администрирование информационных систем",
            "faculty": "Факультет прикладной математики, информатики и механики",
            "pass_score": "251",
            "required_exams": "ИКТ или Физика",
            "profile": "Проектирование и разработка информационных систем"
        },
        {
            "program_name": "Физика",
            "faculty": "Физический факультет",
            "pass_score": "136",
            "required_exams": "Физика",
            "profile": "Физика медицинских, лазерных технологий и наноматериалов"
        },
        {
            "program_name": "Радиофизика",
            "faculty": "Передовая инженерная школа «Российская электроника, инфокоммуникации и радиосвязь»",
            "pass_score": "143",
            "required_exams": "Физика",
            "profile": "Радиофизика и электроника"
        },
        {
            "program_name": "Химия",
            "faculty": "Химический факультет",
            "pass_score": "157",
            "required_exams": "Химия",
            "profile": "Без профиля"
        },
        {
            "program_name": "Химия, физика и механика материалов",
            "faculty": "Химический факультет",
            "pass_score": "140",
            "required_exams": "Химия",
            "profile": "Материаловедение и индустрия наносистем"
        },
        {
            "program_name": "Геология",
            "faculty": "Геологический факультет",
            "pass_score": "136",
            "required_exams": "ИКТ или География или Физика",
            "profile": "Геоологическия изыскания"
        },
        {
            "program_name": "География",
            "faculty": "Факультет географии, геоэкологии и туризма",
            "pass_score": "139",
            "required_exams": "География",
            "profile": "География и региональные исследования"
        },
        {
            "program_name": "Экология и природопользование",
            "faculty": "Медико-биологический факультет",
            "pass_score": "152",
            "required_exams": "Биология",
            "profile": "Охрана окружающей среды"
        },
        {
            "program_name": "Экология и природопользование",
            "faculty": "Факультет географии, геоэкологии и туризма",
            "pass_score": "140",
            "required_exams": "ИКТ или Биология или География",
            "profile": "Геоэкология и природопользование"
        },
        {
            "program_name": "Биология",
            "faculty": "Медико-биологический факультет",
            "pass_score": "153",
            "required_exams": "Биология",
            "profile": "Без профиля"
        },
        {
            "program_name": "Почвоведение",
            "faculty": "Медико-биологический факультет",
            "pass_score": "141",
            "required_exams": "Биология",
            "profile": "Управление земельными ресурсаими"
        },
        {
            "program_name": "Информатика и вычислительная техника",
            "faculty": "Передовая инженерная школа «Российская электроника, инфокоммуникации и радиосвязь»",
            "pass_score": "186",
            "required_exams": "ИКТ или Физика",
            "profile": "Программно-аппаратные средства информационных систем"
        },
        {
            "program_name": "Информационные системы и технологии",
            "faculty": "Передовая инженерная школа «Российская электроника, инфокоммуникации и радиосвязь»",
            "pass_score": "235",
            "required_exams": "ИКТ или Физика",
            "profile": "Инженерия информационных систем и технологий"
        },
        {
            "program_name": "Прикладная информатика",
            "faculty": "Факультет прикладной математики, информатики и механики",
            "pass_score": "219",
            "required_exams": "ИКТ или Физика",
            "profile": "Прикладная информатика в информационном обществе"
        },
        {
            "program_name": "Прикладная информатика",
            "faculty": "Факультет компьютерных наук",
            "pass_score": "212",
            "required_exams": "ИКТ или Физика",
            "profile": "Прикладная информатика в экономике"
        },
        {
            "program_name": "Программная инженерия",
            "faculty": "Факультет компьютерных наук",
            "pass_score": "254",
            "required_exams": "ИКТ или Физика",
            "profile": "Информационные системы и сетевые технологии"
        },
        {
            "program_name": "Информационная безопасность",
            "faculty": "Факультет компьютерных наук",
            "pass_score": "215",
            "required_exams": "ИКТ или Физика",
            "profile": "Безопасность компьютерных систем"
        },
        {
            "program_name": "Инфокоммуникационные технологии и системы связи",
            "faculty": "Передовая инженерная школа «Российская электроника, инфокоммуникации и радиосвязь»",
            "pass_score": "200",
            "required_exams": "ИКТ или Физика",
            "profile": "Без профиля"
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

    print(
        f"Успешно создана новая база данных с {len(programs_data)} программами!")


if __name__ == "__main__":
    recreate_database()
