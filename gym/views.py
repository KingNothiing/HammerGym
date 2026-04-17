from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import ContactRequestForm


INSTAGRAM_URL = 'https://www.instagram.com/hammer_pmr/'
PRIMARY_PHONE = '111'
WORKING_HOURS = [
    'Пн - Пт: 8:00 - 22:00',
    'Вс: 9:00 - 21:00',
]
LOCATIONS = [
    {
        'slug': 'larionova',
        'name': 'Тирасполь, ул. Ларионова',
        'label': 'Филиал 01',
        'description': 'Основной зал. Просторно, много тренажёров, подходит для регулярных тренировок.',
        'phone': PRIMARY_PHONE,
        'hours': WORKING_HOURS,
        'features': [
            'все виды абонементов',
            'для самостоятельных тренировок',
            'удобен как основной зал',
        ],
        'map_url': 'https://www.google.com/maps/search/?api=1&query=%D0%A2%D0%B8%D1%80%D0%B0%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%2C+%D1%83%D0%BB.+%D0%9B%D0%B0%D1%80%D0%B8%D0%BE%D0%BD%D0%BE%D0%B2%D0%B0',
        'map_label': 'Открыть на карте',
    },
    {
        'slug': 'oscar',
        'name': 'Оскар на Балке',
        'label': 'Филиал 02',
        'description': 'Зал рядом с Балкой. Удобно, доступно, без очередей.',
        'phone': PRIMARY_PHONE,
        'hours': WORKING_HOURS,
        'features': [
            'для жителей Балки',
            'доступные цены',
            'удобный график в будни',
        ],
        'map_url': 'https://www.google.com/maps/search/?api=1&query=%D0%9E%D1%81%D0%BA%D0%B0%D1%80+%D0%BD%D0%B0+%D0%91%D0%B0%D0%BB%D0%BA%D0%B5%2C+%D0%A2%D0%B8%D1%80%D0%B0%D1%81%D0%BF%D0%BE%D0%BB%D1%8C',
        'map_label': 'Открыть на карте',
    },
]
PRICING = [
    {
        'slug': 'larionova',
        'name': 'Ларионова',
        'badge': 'Тирасполь',
        'items': [
            ('1 месяц', '300 р'),
            ('3 месяца', '275 р / мес'),
            ('6 месяцев', '250 р / мес'),
            ('Год', '225 р / мес'),
            ('2 тренировки в неделю', '250 р'),
            ('Студенты и школьники', '250 р'),
            ('Семейный', '275 р'),
            ('Корпоративный', '250 р'),
            ('Разовая тренировка', '50 р'),
            ('50 тренировок на год', '1250 р'),
            ('25 тренировок на 6 месяцев', '750 р'),
        ],
    },
    {
        'slug': 'oscar',
        'name': 'Оскар',
        'badge': 'Балка',
        'items': [
            ('1 месяц', '275 р'),
            ('3 месяца', '250 р / мес'),
            ('6 месяцев', '225 р / мес'),
            ('Год', '200 р / мес'),
            ('2 тренировки в неделю', '225 р'),
            ('Студенты и школьники', '225 р'),
            ('Семейный', '250 р'),
            ('Корпоративный', '225 р'),
            ('Разовая тренировка', '40 р'),
            ('50 тренировок на год', '1250 р'),
            ('25 тренировок на 6 месяцев', '750 р'),
        ],
    },
]
GALLERY_IMAGES = [
    {
        'src': 'images/gallery/gallery-placeholder-1.svg',
        'alt': 'Тестовый широкий кадр для галереи Hammer Gym',
        'caption': 'Общий вид филиала или тренажерного зала',
    },
    {
        'src': 'images/gallery/gallery-placeholder-2.svg',
        'alt': 'Тестовый вертикальный кадр для галереи Hammer Gym',
        'caption': 'Тренер, отдельная зона или акцентный интерьерный кадр',
    },
    {
        'src': 'images/gallery/gallery-placeholder-3.svg',
        'alt': 'Тестовый набор изображений для галереи Hammer Gym',
        'caption': 'Микс из атмосферы, оборудования и команды',
    },
]
TRAINERS = [
    {
        'initials': '01',
        'name': 'Имя тренера',
        'role': 'Силовая подготовка',
        'tag': 'Персональный тренер',
        'description': 'Сюда добавим короткое описание тренера: опыт, специализацию, формат работы и для кого он подходит.',
    },
    {
        'initials': '02',
        'name': 'Имя тренера',
        'role': 'Персональные тренировки',
        'tag': 'Персональный тренер',
        'description': 'Карточка под специалиста, который помогает выстроить понятный тренировочный план и сопровождение под цель клиента.',
    },
    {
        'initials': '03',
        'name': 'Имя тренера',
        'role': 'Снижение веса',
        'tag': 'Фитнес-направление',
        'description': 'Здесь будет реальное описание тренера по снижению веса, дисциплине тренировок и безопасному входу в режим.',
    },
    {
        'initials': '04',
        'name': 'Имя тренера',
        'role': 'Набор формы',
        'tag': 'Силовое направление',
        'description': 'Под это место добавим фото, имя и понятную подачу специализации: набор формы, тонус, базовые силовые задачи.',
    },
    {
        'initials': '05',
        'name': 'Имя тренера',
        'role': 'Женский фитнес',
        'tag': 'Фитнес-направление',
        'description': 'Заглушка под карточку с живым фото, коротким описанием тренера и акцентом на комфортный формат тренировок.',
    },
    {
        'initials': '06',
        'name': 'Имя тренера',
        'role': 'Новички в зале',
        'tag': 'Старт для новичков',
        'description': 'Эта карточка подойдет под тренера, который объясняет базу, технику и помогает без стресса войти в занятия.',
    },
    {
        'initials': '07',
        'name': 'Имя тренера',
        'role': 'Универсальный тренер',
        'tag': 'Резервный слот',
        'description': 'Резервная карточка под реального специалиста с финальным фото, именем, специализацией и кратким описанием.',
    },
]
ADVANTAGES = [
    {
        'title': '2 филиала',
        'text': 'Выбирай зал ближе к дому. Можно чередовать — тренироваться в разных локациях.',
    },
    {
        'title': 'Цены на сайте',
        'text': 'Все абонементы, льготы и разовые посещения видны сразу — без звонков и уточнений.',
    },
    {
        'title': 'Пришёл и начал',
        'text': 'Никаких сложных условий. Посмотрел прайс, выбрал зал, пришел тренироваться.',
    },
]
SHOWCASE_STEPS = [
    'посмотреть цены и выбрать филиал',
    'прийти на тренировку',
    'открыть карту и добраться до зала',
]


def home(request):
    context = _build_home_context(contact_form=ContactRequestForm())
    return render(request, 'gym/home.html', context)


def submit_contact_request(request):
    if request.method != 'POST':
        return redirect('home')

    form = ContactRequestForm(request.POST)
    if not form.is_valid():
        messages.error(request, 'Проверьте форму и попробуйте еще раз.')
        context = _build_home_context(contact_form=form)
        return render(request, 'gym/home.html', context)

    contact_request = form.save()
    _send_contact_email(contact_request)
    messages.success(request, 'Заявка отправлена. Мы свяжемся с вами в ближайшее время.')
    return redirect(f"{reverse('home')}#contact")


def _build_home_context(contact_form):
    return {
        'contact_form': contact_form,
        'instagram_url': INSTAGRAM_URL,
        'primary_phone': PRIMARY_PHONE,
        'working_hours': WORKING_HOURS,
        'locations': LOCATIONS,
        'pricing': PRICING,
        'gallery_images': GALLERY_IMAGES,
        'trainers': TRAINERS,
        'advantages': ADVANTAGES,
        'showcase_steps': SHOWCASE_STEPS,
    }


def _send_contact_email(contact_request):
    subject = 'Новая заявка с сайта HAMMER GYM'
    message = (
        'Новая заявка с сайта:\n\n'
        f'Имя: {contact_request.full_name}\n'
        f'Телефон: {contact_request.phone}\n'
        f'Филиал: {contact_request.get_branch_display()}\n'
        f'Сообщение: {contact_request.message or "-"}\n'
    )
    _send_safe_email(subject, message, settings.ADMIN_NOTIFICATION_EMAIL)


def _send_safe_email(subject, message, recipient):
    try:
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[recipient],
            fail_silently=False,
        )
    except Exception:
        pass
