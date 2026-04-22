"""Structured content for the public-facing Hammer Gym homepage."""

INSTAGRAM_URL = "https://www.instagram.com/hammer_pmr/"
INSTAGRAM_HANDLE = "@hammer_pmr"
PRIMARY_PHONE = "+373 778 4-76-29"
PRIMARY_PHONE_HREF = PRIMARY_PHONE.replace(" ", "")
SECONDARY_PHONE = "+373 779 31-553"
SECONDARY_PHONE_HREF = SECONDARY_PHONE.replace(" ", "")
MESSENGER_NOTE = "Telegram / Viber"
WORKING_HOURS = (
    "Пн - Пт: 8:00 - 22:00",
    "Вс: 9:00 - 21:00",
)
WORKING_HOURS_SUMMARY = ", ".join(WORKING_HOURS)

NAV_ITEMS = (
    {"target": "home", "label": "Главная"},
    {"target": "about", "label": "О зале"},
    {"target": "locations", "label": "Филиалы"},
    {"target": "pricing", "label": "Прайс"},
    {"target": "gallery", "label": "Галерея"},
    {"target": "trainers", "label": "Команда"},
    {"target": "contact", "label": "Контакты"},
)

HERO_HIGHLIGHTS = (
    "2 филиала в Тирасполе: ул. Ларионова, 40 и РЦ \"Оскар\"",
    "Самостоятельные и персональные тренировки в понятном формате",
    "Актуальные фото, объявления и жизнь зала — в Instagram",
)

ABOUT_STATS = (
    {"value": "2", "label": "Филиала в Тирасполе"},
    {"value": "11", "label": "Позиций прайса в каждом филиале"},
    {"value": "2", "label": "Публичных номера для связи"},
    {"value": "1", "label": "Форма заявки прямо на сайте"},
)

LOCATIONS = (
    {
        "slug": "larionova",
        "name": "Тирасполь, ул. Ларионова, 40",
        "label": "Филиал 01",
        "description": "Основной филиал для тех, кому нужен понятный рабочий зал: свободные веса, базовые тренажеры и формат без лишней суеты.",
        "phone": PRIMARY_PHONE,
        "hours": WORKING_HOURS,
        "features": (
            "самостоятельные тренировки",
            "персональный формат",
            "силовая и кардио база",
        ),
        "map_url": "https://www.google.com/maps/search/?api=1&query=%D0%A2%D0%B8%D1%80%D0%B0%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%2C+%D1%83%D0%BB.+%D0%9B%D0%B0%D1%80%D0%B8%D0%BE%D0%BD%D0%BE%D0%B2%D0%B0%2C+40",
        "map_label": "Открыть на карте",
    },
    {
        "slug": "oscar",
        "name": "Тирасполь, ул. Одесская, 68, РЦ \"Оскар\"",
        "label": "Филиал 02",
        "description": "Филиал на Балке в РЦ \"Оскар\". Удобный вариант для тех, кто ищет зал рядом с районом и хочет быстро заезжать на тренировку.",
        "phone": PRIMARY_PHONE,
        "hours": WORKING_HOURS,
        "features": (
            "удобно для Балки",
            "понятные абонементы",
            "персональный и базовый формат",
        ),
        "map_url": "https://www.google.com/maps/search/?api=1&query=%D0%A2%D0%B8%D1%80%D0%B0%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%2C+%D0%9E%D0%B4%D0%B5%D1%81%D1%81%D0%BA%D0%B0%D1%8F+68+%D0%9E%D1%81%D0%BA%D0%B0%D1%80",
        "map_label": "Открыть на карте",
    },
)

PRICING = (
    {
        "slug": "larionova",
        "name": "Ларионова",
        "badge": "Тирасполь",
        "entries": (
            ("1 месяц", "300 р"),
            ("3 месяца", "275 р / мес"),
            ("6 месяцев", "250 р / мес"),
            ("Год", "225 р / мес"),
            ("2 тренировки в неделю", "250 р"),
            ("Студенты и школьники", "250 р"),
            ("Семейный", "275 р"),
            ("Корпоративный", "250 р"),
            ("Разовая тренировка", "50 р"),
            ("50 тренировок на год", "1250 р"),
            ("25 тренировок на 6 месяцев", "750 р"),
        ),
    },
    {
        "slug": "oscar",
        "name": "Оскар",
        "badge": "Балка",
        "entries": (
            ("1 месяц", "275 р"),
            ("3 месяца", "250 р / мес"),
            ("6 месяцев", "225 р / мес"),
            ("Год", "200 р / мес"),
            ("2 тренировки в неделю", "225 р"),
            ("Студенты и школьники", "225 р"),
            ("Семейный", "250 р"),
            ("Корпоративный", "225 р"),
            ("Разовая тренировка", "40 р"),
            ("50 тренировок на год", "1250 р"),
            ("25 тренировок на 6 месяцев", "750 р"),
        ),
    },
)

GALLERY_IMAGES = (
    {
        "src": "images/gallery/gallery-placeholder-1.svg",
        "alt": "Визуальный макет широкого фото для галереи Hammer Gym",
        "caption": "Общий вид зала: как выглядит пространство до и во время тренировки.",
    },
    {
        "src": "images/gallery/gallery-placeholder-2.svg",
        "alt": "Визуальный макет вертикального фото для галереи Hammer Gym",
        "caption": "Персональная работа, техника упражнений и атмосфера обычного дня в зале.",
    },
    {
        "src": "images/gallery/gallery-placeholder-3.svg",
        "alt": "Визуальный макет набора фотографий для галереи Hammer Gym",
        "caption": "Смесь кадров с оборудованием, людьми и моментами из Instagram-подачи клуба.",
    },
)

TRAINERS = (
    {
        "initials": "PT",
        "name": "Персональный тренинг",
        "role": "Старт под цель",
        "tag": "Индивидуальный подход",
        "description": "Формат для тех, кому нужен тренер рядом: техника, дисциплина, программа и движение к понятному результату.",
    },
    {
        "initials": "BB",
        "name": "Силовой набор",
        "role": "Масса и база",
        "tag": "Bodybuilding",
        "description": "Подходит для тех, кто делает упор на свободные веса, базовые движения и постепенный набор физической формы.",
    },
    {
        "initials": "WL",
        "name": "Снижение веса",
        "role": "Комфортный вход",
        "tag": "Фитнес-направление",
        "description": "Плавный вход в режим для тех, кто хочет привести себя в форму, не ломая темп жизни и не перегружая себя на старте.",
    },
    {
        "initials": "FT",
        "name": "Функциональный формат",
        "role": "Выносливость и тонус",
        "tag": "Functional training",
        "description": "Подойдет тем, кому нужен баланс между силой, подвижностью, дыханием и общей работоспособностью.",
    },
    {
        "initials": "CR",
        "name": "Кардио и тонус",
        "role": "Ритм и регулярность",
        "tag": "Cardio training",
        "description": "Для тех, кто хочет держать темп, улучшать выносливость и совмещать кардионагрузку с базовой силовой работой.",
    },
    {
        "initials": "WF",
        "name": "Женский фитнес",
        "role": "Комфортный режим",
        "tag": "Для тонуса и формы",
        "description": "Спокойная и понятная подача тренировок с акцентом на самочувствие, ритм и комфортное сопровождение.",
    },
    {
        "initials": "ST",
        "name": "Старт для новичков",
        "role": "Без лишнего стресса",
        "tag": "Первый шаг в зал",
        "description": "Для тех, кто давно собирался начать и хочет попасть в понятную среду, где объяснят базу и помогут закрепиться.",
    },
    {
        "initials": "HG",
        "name": "Команда HAMMER",
        "role": "Под разные цели",
        "tag": "Готово к наполнению",
        "description": "Структура уже готова под реальные фото и профили. Когда будут материалы, карточки можно быстро превратить в живой раздел команды.",
    },
)

ADVANTAGES = (
    {
        "title": "2 филиала",
        "text": "Можно выбрать зал ближе к дому: ул. Ларионова или Балка, РЦ \"Оскар\".",
    },
    {
        "title": "Понятный прайс",
        "text": "На сайте собраны месячные, длительные, льготные и разовые форматы без необходимости уточнять базовые цены в сообщениях.",
    },
    {
        "title": "Связь без барьеров",
        "text": "Есть звонок, Instagram, карты и форма заявки. Для локального зала это выглядит привычно и вызывает больше доверия.",
    },
)

SHOWCASE_STEPS = (
    {
        "title": "Сравнить филиалы",
        "text": "Посетитель сначала понимает, какой зал ему ближе: Ларионова или Балка, и как до него удобнее добираться.",
    },
    {
        "title": "Посмотреть прайс",
        "text": "На одной странице видно, какой формат абонемента подходит под ритм занятий, бюджет и тип посещения.",
    },
    {
        "title": "Оставить заявку",
        "text": "После выбора можно сразу позвонить, перейти в Instagram или оставить заявку на обратную связь.",
    },
)


def get_home_page_context():
    """Return a structured context for the homepage template."""

    return {
        "nav_items": NAV_ITEMS,
        "hero_highlights": HERO_HIGHLIGHTS,
        "about_stats": ABOUT_STATS,
        "instagram_url": INSTAGRAM_URL,
        "instagram_handle": INSTAGRAM_HANDLE,
        "primary_phone": PRIMARY_PHONE,
        "primary_phone_href": PRIMARY_PHONE_HREF,
        "secondary_phone": SECONDARY_PHONE,
        "secondary_phone_href": SECONDARY_PHONE_HREF,
        "messenger_note": MESSENGER_NOTE,
        "working_hours": WORKING_HOURS,
        "working_hours_summary": WORKING_HOURS_SUMMARY,
        "locations": LOCATIONS,
        "pricing": PRICING,
        "gallery_images": GALLERY_IMAGES,
        "trainers": TRAINERS,
        "advantages": ADVANTAGES,
        "showcase_steps": SHOWCASE_STEPS,
    }
