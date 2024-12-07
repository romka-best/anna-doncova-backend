from AnnaDoncovaBot.firebase import db


async def send_email(name: str, email: str):
    mail_ref = db.collection('mails').document()
    await mail_ref.set({
        'id': mail_ref.id,
        'to': email,
        'message': {
            'subject': 'Магия нейросетей начинается здесь: получите доступ к курсу',
            'text': f"""
Здравствуйте, {name}!

Спасибо, что приобрели мой мини-курс «Нейросети для создания контента». Я рада сообщить, что все уроки и материалы готовы, и вы теперь можете приступить к обучению!

Что вас ждёт в курсе:
- Урок 1: Основы нейросетей и эффективные запросы
- Урок 2: Генерация текста, изображений и видео с помощью нейросетей
- Урок 3: Автоматизация процессов и увеличение аудитории и продаж
Каждый урок содержит подробные инструкции, примеры и практические задания, которые помогут вам освоить использование нейросетей в создании контента для социальных сетей.

Как получить доступ:
- Перейдите по ссылке: https://drive.google.com/drive/folders/1nrYz6NYKuAyYfj-7Ml04n8dfoOF9u9xi?usp=sharing
- Начинайте изучать материалы в удобном для вас темпе.
Если у вас возникнут вопросы или потребуется помощь, пожалуйста, не стесняйтесь обращаться ко мне по этой электронной почте или в директ Instagram.

В качестве благодарности, я подготовила для вас бонусный материал:
- Гайд по использованию MidJourney
- Гайд по Распаковки личности
- Библиотека промтов
- Гайд по созданию коротких видео
- Гайд по использованию gamma.app

Ещё раз благодарю вас за выбор моего курса. Надеюсь, что он будет полезным и поможет вам достигать новых высот в создании контента!

С уважением,
Анна Донцова
    """
        },
    })