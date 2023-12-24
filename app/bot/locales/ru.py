import random

from app.bot.locales.texts import Texts
from app.models.common import Currency
from app.models.package import PackageType
from app.models.subscription import Subscription, SubscriptionType, SubscriptionPeriod
from app.models.user import User, UserGender, UserQuota


class Russian(Texts):
    START = """
🤖 Добро пожаловать в будущее ИИ с GPTsTurboBot 🎉

Бот предоставляет доступ к искусственному интеллекту и нейросетям.
Отправьтесь в путешествие по миру ИИ с:
✉️ Неограниченным количеством запросов к ChatGPT 3... Ну, почти! Посмотрите наш тариф 'Бесплатно'
🧠 Мудростью ChatGPT 4, если сегодня вы чувствуете себя особенно умным
🎨 Художественными творениями с DALL-E 3, которые заставят Пикассо взглянуть дважды
😜 А хотели ли вы когда-нибудь поменяться лицами с Моной Лизой? Просто попросите нашу функцию Face Swap

Вот краткое руководство, чтобы начать:
✉️ Чтобы получить текстовый ответ, просто введите ваш запрос в чат
🌅 Чтобы создать изображение, сначала выберите модель ИИ в /mode, а затем дайте волю своему воображению!
🔄 Переключайтесь между разными нейросетями с помощью /mode в зависимости от ваших творческих потребностей
🔍 Используйте /info, чтобы узнать больше о возможностях каждой модели ИИ
👁️‍🗨️ Погрузитесь в /catalog, чтобы выбрать специализированного помощника для ваших задач
📊 Проверьте информацию об использовании и подробности подписки в /profile
🔧 Дополнительно настройте свой опыт в /settings

И это ещё не всё! Просто нажмите /commands, чтобы увидеть все волшебные команды ИИ, доступные вам.
Пусть ИИ станет вашим со-пилотом в этом приключении! 🚀
"""
    COMMANDS = """
🤖 Вот что вы можете исследовать:

🚀 /start - *Обо мне*
🌐 /language - Переключайтесь на любой язык, *устанавливайте системные сообщения*.
🧠 /mode - *Переключайте модели нейросетей* на лету — *ChatGPT3*, *ChatGPT4*, *DALL-E 3* или *Face Swap*!
📜 /info - Интересно, что умеет каждая модель? Здесь вы найдёте все ответы.
💼 /profile - *Посмотреть свой профиль*, чтобы узнать ваш квоту использования и многое другое.
🔧 /settings - *Настройте свой опыт* для бесшовного пользовательского опыта.
💳 /subscribe или /buy - *Узнайте о наших подписках и преимуществах* или выберите индивидуальные пакеты.
🎁 /promo\\_code - Раскройте эксклюзивные функции ИИ и специальные предложения с вашим промокодом.
🎭 /catalog - *Выберите специализированного помощника* для задач, разработанных специально для вас.
💬 /chats - *Создайте, переключайтесь или удаляйте тематические чаты*.

Просто напишите или используйте команду, чтобы начать своё путешествие в мир ИИ! 🌟
"""
    FEEDBACK = """
🌟 *Ваше мнение важно!* 🌟

Привет! Мы всегда стремимся к улучшению, и ваша обратная связь для нас как золото. 💬✨

- Что-то вам особенно нравится в нашем боте? Расскажите нам!
- Есть предложения по функциям? Мы внимательно выслушаем!
- Что-то вас беспокоит? Мы здесь, чтобы устранить эти проблемы. 🐞
Просто напишите свои мысли и нажмите отправить. Всё так просто! Ваши идеи помогают нам расти и становиться лучше каждый день.
И помните, каждое ваше замечание — это шаг к тому, чтобы наш бот стал ещё круче. С нетерпением ждём от вас новостей! 💌
"""
    FEEDBACK_SUCCESS = """
🌟 *Обратная связь получена!* 🌟

Спасибо, что поделились своими мыслями! 💌
Ваше мнение - это секретный ингредиент нашего успеха. Мы готовим улучшения, и ваша обратная связь - ключевой элемент. 🍳🔑

Следите за обновлениями и новыми функциями, все они вдохновлены вами. А пока приятного общения! 🚀

Ваше мнение очень важно для нас! 💖
"""

    # Profile
    CHANGE_PHOTO = "Поменять фотографию 📷"
    CHANGE_GENDER = "Поменять пол 🚹🚺"

    # Language
    LANGUAGE = "Язык:"
    CHOOSE_LANGUAGE = "Выбранный язык: Русский 🇷🇺"

    # Promo code
    PROMO_CODE_INFO = """
🔓 *Откройте мир чудес ИИ с вашим секретным кодом!* 🌟

Если у вас есть промокод, просто введите его, чтобы раскрыть скрытые функции и особые сюрпризы. 🎁

Нет кода? Не беда! Просто нажмите 'Выход', чтобы продолжить изучение вселенной ИИ без него. 🚀
"""
    PROMO_CODE_SUCCESS = """
🎉 *Ура! Вы нашли золотую жилу!* 🌟

Ваш промокод успешно активирован! Приготовьтесь окунуться в мир чудес ИИ с вашими новыми преимуществами. 🚀

Спасибо, что присоединились к нам в этом приключении на основе ИИ. Наслаждайтесь дополнительными возможностями и создавайте волшебство вместе с нами! ✨

Приятного исследования! 🤖🌐
"""
    PROMO_CODE_EXPIRED_ERROR = """
🕒 *Ой, срок действия этого промокода истёк!*

Похоже, что этот промокод устарел. 📆 Это как сказка о Золушке, но без стеклянного башмачка. 🥿

Но не расстраивайтесь! Вы всё ещё можете изучать наши другие волшебные предложения с помощью /subscribe или /buy. В нашем мире ИИ всегда есть что-то увлекательное! 🎩✨

Оставайтесь любознательными и продолжайте приключение с ИИ! 🌟🚀
"""
    PROMO_CODE_NOT_FOUND_ERROR = """
🔍 *Ой, промокод не найден!*

Кажется, введённый вами промокод играет с нами в прятки. 🕵️‍♂️ Мы не смогли найти его в нашей системе.

🤔 Проверьте наличие опечаток и попробуйте ещё раз. Если всё ещё не получается, возможно, стоит поискать другой код или взглянуть на наши предложения в /subscribe и /buy за интересные сделки 🛍️

Не теряйте оптимизма и продолжайте веселиться с ИИ! 🚀🎈
"""
    PROMO_CODE_ALREADY_USED_ERROR = """
🚫 *Ой, дежавю!*

Похоже, вы уже использовали этот промокод. Это магия на один раз, и вы уже воспользовались ею! ✨🧙

Но не беспокойтесь! Вы можете ознакомиться с нашими последними предложениями в /subscribe или /buy. У нас всегда есть что-то новое в запасе! 🎉🔮

Продолжайте исследовать и пусть ИИ-сюрпризы продолжаются! 🤖
"""

    # AI
    MODE = "Режим:"
    INFO = """
🤖 Давайте посмотрим, что каждая модель может сделать для вас:

✉️ *ChatGPT3: Всесторонний коммуникатор*
- _От обычного разговора до глубоких бесед_: Идеален для чата на любую тему, от повседневной жизни до шуток.
- _Образовательный ассистент_: Помощь в выполнении домашних заданий, изучении языков или сложных тем, таких как программирование.
- _Личный тренер_: Мотивация, советы по фитнесу или даже руководство по медитации.
- _Творческий писатель_: Нужен пост, история или даже песня? ChatGPT3 создаст это за секунды.
- _Путешественник_: Спросите советы по путешествиям, местные кухни или исторические факты о вашем следующем направлении.
- _Бизнес-помощник_: Написание электронных писем, бизнес-планов или идей для маркетинга.
- _Ролевые игры_: Участие в творческих ролевых сценариях для развлечения или рассказа историй.
- _Краткие сводки_: Суммирование длинных статей или отчетов в лаконичный текст.

🧠 *ChatGPT4: Расширенный интеллект*
- _Глубокий анализ_: Идеально для детальных исследований, технических объяснений или исследования гипотетических сценариев.
- _Решение проблем_: Помощь в сложных математических задачах, ошибках программирования или научных вопросах.
- _Языковой эксперт_: Перевод сложных текстов или практика навыков разговорного языка на разных языках.
- _Творческий консультант_: Разработка идей для постов, диалогов для сценариев или исследование художественных концепций.
- _Здоровье и благополучие_: Обсуждение тем здоровья и психического благополучия на глубоком уровне.
- _Персонализированные рекомендации_: Получение рекомендаций по книгам, фильмам или путешествиям на основе ваших интересов.

🎨 *DALLE-3: Творческий гений*
- _Искусство по запросу_: Генерация уникальных изображений по описаниям - идеально для иллюстраторов или в поисках вдохновения.
- _Создатель рекламы_: Создание привлекательных изображений для рекламы или контента в социальных сетях.
- _Образовательный инструмент_: Визуализация сложных концепций для лучшего понимания в образовании.
- _Дизайн интерьера_: Получение идей для планировки комнат или тем декора.
- _Модный дизайн_: Создание дизайнов одежды или модных иллюстраций.
- _Персонализированные комиксы_: Создание комиксов или персонажей мультфильмов из ваших историй.
- _Макеты продуктов_: Создание макетов для идей продуктов или изобретений.

🤡 *Face Swap: Мастер развлечений*
- _Веселые переосмысления_: Посмотрите, как выглядели бы в разные исторические эпохи или в образе разных кино персонажей.
- _Персонализированные поздравления_: Создайте уникальные открытки или приглашения с персонализированными изображениями.
- _Ролевые игры_: Экспериментируйте с разными образами для ролевых игр или виртуальных встреч.
- _Мемы и создание Контента_: Оживите свои социальные сети смешными или фантазийными фотографиями с заменой лица.
- _Цифровые макияжи_: Экспериментируйте с новыми стрижками или стилями макияжа.
- _Смешение со знаменитостями_: Совместите свое лицо с знаменитостями для забавных сравнений.

Для смены модели используйте /mode 😉
"""
    ALREADY_MAKE_REQUEST = "Вы уже сделали запрос. Пожалуйста, подождите ⚠️"
    READY_FOR_NEW_REQUEST = "Вы можете задать следующий запрос 😌"
    IMAGE_SUCCESS = "✨ Вот ваше созданное изображение! 🎨"

    # Settings
    SETTINGS = "Настройки:"
    SHOW_NAME_OF_THE_CHAT = "Отображение названия чата в сообщениях"
    SHOW_USAGE_QUOTA_IN_MESSAGES = "Отображение квоты в сообщениях"
    TURN_ON_VOICE_MESSAGES_FROM_RESPONDS = "Включить голосовые сообщения для ответов"

    # Voice
    VOICE_MESSAGES_FORBIDDEN = """
🎙 *Упс! Кажется, ваш голос потерялся в AI-пространстве!*

Чтобы разблокировать чудо преобразования голоса в текст, просто воспользуйтесь волшебством команд /subscribe или /buy.

Давайте превратим эти голосовые сообщения в текст и продолжим общение! 🌟🔮
    """

    # Subscription
    MONTH_1 = "1 месяц"
    MONTHS_3 = "3 месяца"
    MONTHS_6 = "6 месяцев"
    DISCOUNT = "Скидка"
    NO_DISCOUNT = "Нет скидки"
    SUBSCRIPTION_SUCCESS = """
🎉 Ура! Теперь вы с нами! 🚀

Ваша подписка активирована, как белка на кофеине! 🐿️☕ Добро пожаловать в клуб потрясающих возможностей. Вот что вас ждет дальше:
- Перед вами открылся весь мир возможностей. 🌍✨
- Ваши AI-друзья уже готовы помогать вам. 🤖👍
- Приготовьтесь окунуться в море функций и веселья. 🌊🎉

Спасибо, что присоединились к нам в этом удивительном путешествии! Давайте творить чудеса! 🪄🌟
"""
    SUBSCRIPTION_RESET = """
🚀 *Квота подписки обновлена!*

Привет, путешественник в мире ИИ! 🌟
Угадай что? Твоя квота подписки только что была обновлена! Это как волшебное пополнение, только лучше, потому что это реальность. 🧙‍♂️
Впереди целый месяц веселья с ИИ. Общайся, твори, исследуй – нет предела! ✨

Продолжай раскрывать мощь ИИ и помни, мы здесь, чтобы сделать твои цифровые мечты реальностью. Давайте сделаем этот месяц лучше! 🤖💥
"""
    SUBSCRIPTION_END = """
🛑 *Подписка Истекла!*

Привет, энтузиаст ИИ! 🌟
Твоя подписка закончилась. Но не беспокойся, путешествие по миру ИИ еще не окончено! 🚀
Ты можешь возобновить свой магический доступ с помощью /subscribe и продолжить исследование вселенной ИИ. Или, если хочешь, загляни в /buy за индивидуальными пакетами, созданными специально для тебя. 🎁

Приключения в мире ИИ ждут! Подзарядись, соберись с мыслями, и давай продолжим этот захватывающий путь вместе. 🤖✨
"""

    # Package
    GPT3_REQUESTS = "✉️ GPT3 запросы"
    GPT3_REQUESTS_DESCRIPTION = "Разбудите мощь *GPT 3* для остроумных бесед, умных советов и бесконечного веселья! 🤖✨"
    GPT4_REQUESTS = "🧠 GPT4 запросы"
    GPT4_REQUESTS_DESCRIPTION = "Исследуйте продвинутый интеллект *GPT 4* для более глубоких открытий и прорывных бесед. 🧠🌟"
    THEMATIC_CHATS = "💬 Тематические чаты"
    THEMATIC_CHATS_DESCRIPTION = "Окунитесь в интересные темы с *тематическими чатами*, направляемыми AI в мире индивидуальных дискуссий. 📚🗨️"
    DALLE3_REQUESTS = "🖼 DALLE3 изображения"
    DALLE3_REQUESTS_DESCRIPTION = "Превратите свои идеи в искусство с помощью *DALLE3* – там, где ваше воображение становится поразительной визуальной реальностью! 🎨🌈"
    FACE_SWAP_REQUESTS = "📷 Изображения с заменой лица"
    FACE_SWAP_REQUESTS_DESCRIPTION = "Погрузитесь в игровой мир *замены лиц* для смеха и удивления на каждом изображении! 😂🔄"
    ACCESS_TO_CATALOG = "🎭 Доступ к каталогу с ролями"
    ACCESS_TO_CATALOG_DESCRIPTION = "Откройте для себя вселенную специализированных AI-помощников с доступом к нашему эксклюзивному каталогу, где каждая роль адаптирована под ваши уникальные потребности и задачи"
    ANSWERS_AND_REQUESTS_WITH_VOICE_MESSAGES = "🎙 Ответы и запросы с голосовыми сообщениями"
    ANSWERS_AND_REQUESTS_WITH_VOICE_MESSAGES_DESCRIPTION = "Ощутите удобство и простоту голосового общения с нашим AI: отправляйте и получайте голосовые сообщения для более динамичного и выразительного взаимодействия"
    FAST_ANSWERS = "⚡ Быстрые ответы"
    FAST_ANSWERS_DESCRIPTION = "Функция *'Быстрые ответы'* предлагает мгновенные, точные ответы AI, обеспечивая ваше преимущество в общении"
    MIN_ERROR = "Ой! Кажется, введенное число меньше нашего минимального порога. Пожалуйста, введите значение, соответствующее или превышающее минимально требуемое. Давайте попробуем еще раз! 🔄"
    VALUE_ERROR = "Упс! Похоже, это не число. 🤔 Не могли бы вы ввести числовое значение? Давайте попробуем еще раз! 🔢"
    PACKAGE_SUCCESS = """
🎉 *Ура! Оплата прошла успешно!* 💳

Ваша оплата прошла быстро, словно супергерой! 🦸‍ Вы успешно разблокировали невероятную мощь выбранного пакета. Готовьтесь к увлекательным приключениям с AI! 🎢

Помните, с большой силой приходит большая... ну вы знаете как говорят. Давайте творить чудеса! ✨🪄
"""

    # Catalog
    CATALOG = """
🎭 *Добро пожаловать в наш каталог ролей!* 🌟

Мечтали ли вы о специализированном AI-помощнике, созданном именно для вас? Наш каталог - это как волшебный гардероб, где каждая роль - уникальный наряд для ваших приключений в мире AI! 🧙‍♂️✨

Выбирайте из множества AI-персонажей, каждый со своими особенностями и знаниями. Вам нужен товарищ для мозгового штурма, творческая муза или фактический волшебник - у нас есть всё!

👉 Готовы встретить своего идеального помощника? Просто нажмите на кнопку ниже и пусть магия начнется! 🎩👇
"""
    CATALOG_FORBIDDEN_ERROR = """
🔒 *Ой! Похоже, вы попали в зону для VIP!* 🌟

Вы всего в одном клике от открытия нашего сокровища AI-ролей, но, кажется, у вас пока нет золотого ключика. Не волнуйтесь! Вы легко можете его получить.

🚀 Посетите /subscribe для замечательных вариантов подписки или перейдите в /buy, если хотите выбрать что-то из AI-деликатесов.

Как только вы будете готовы, наш каталог AI-чудес будет ждать вас – это ваш билет в необыкновенный мир возможностей AI! 🎫✨
"""
    PERSONAL_ASSISTANT = {
        "name": "🤖 Персональный ассистент",
        "description": """
Ваш надёжный помощник во всём и для всего!
От простых ответов до глубоких бесед, я здесь, чтобы помочь вам, как верный спутник 🌟
Давайте вместе решим жизненные головоломки!
""",
        "instruction": "Ты полезный личный ассистент"
    }
    TUTOR = {
        "name": "📚 Репетитор",
        "description": """
Откройте для себя мир знаний по всем предметам!
Я здесь, чтобы сделать сложные концепции простыми и обучение увлекательным 📚
Будь то математика, наука или искусство, давайте учиться вместе!
""",
        "instruction": "Ты полезный репетитор"
    }
    LANGUAGE_TUTOR = {
        "name": "🗣️ Репетитор по иностранным языкам",
        "description": """
Отправляйтесь в лингвистическое приключение!
От основных фраз до свободного владения, я помогу вам изучить языки легко и с удовольствием 🌐
Давайте общаться на новых языках!
""",
        "instruction": "Ты полезный репетитор по иностранным языкам"
    }
    CREATIVE_WRITER = {
        "name": "🖋️ Креативный писатель",
        "description": """
Готовы исследовать миры чудес?
От создания захватывающих историй до написания трогательной поэзии, давайте вместе раскроем наше творчество 🖋️
Ваше воображение - это предел!
""",
        "instruction": "Ты полезный креативный писатель"
    }
    TECHNICAL_ADVISOR = {
        "name": "💻 Технический консультант",
        "description": """
Лёгкий путь через технический лабиринт!
Будь то понимание нового ПО, устранение ошибок или изучение технических тенденций, я здесь, чтобы упростить технологии 💻
Давайте вместе разбираться в цифровом мире!
""",
        "instruction": "Ты полезный технический консультант"
    }
    MARKETER = {
        "name": "📈 Маркетолог",
        "description": """
Давайте поднимем ваш бренд и охват!
От исследования рынка до стратегий кампаний, я здесь, чтобы помочь вам в навигации по маркетинговому ландшафту и достижению ваших бизнес-целей 📊
Ваш успех - наша цель!
""",
        "instruction": "Ты полезный маркетолог"
    }
    SMM_SPECIALIST = {
        "name": "📱 SMM-Специалист",
        "description": """
Преобразите ваше присутствие в социальных сетях!
Я помогу вам создать увлекательный контент, расширить вашу аудиторию и оставаться на шаг впереди в постоянно меняющемся мире социальных сетей 📱
Давайте сделаем социальные сети вашим инструментом!
""",
        "instruction": "Ты полезный SMM-Специалист"
    }
    CONTENT_SPECIALIST = {
        "name": "📝 Специалист по контенту",
        "description": """
Контент - это король, и я здесь, чтобы помочь вам властвовать!
От оптимизации SEO до увлекательных текстов, давайте создадим контент, который будет резонировать и привлекать внимание ✍️
Ваше сообщение имеет значение!
""",
        "instruction": "Ты полезный специалист по контенту"
    }
    DESIGNER = {
        "name": "🎨 Дизайнер",
        "description": """
Визуальное повествование в лучшем виде!
Давайте создадим дизайн, который завораживает и передаёт идеи, будь то веб-сайты или фирменные стили 🖌️
Ваше видение, наш холст!
""",
        "instruction": "Ты полезный дизайнер"
    }
    SOCIAL_MEDIA_PRODUCER = {
        "name": "📸 Продюсер в социальных сетях",
        "description": """
Создаём истории, которые запоминаются и связывают на социальных сетях!
Давайте производим контент, который выделяется и говорит с вашей аудиторией 🎥
Ваша история, блестяще рассказанная в социальных платформах!
""",
        "instruction": "Ты полезный продюсер в социальных сетях"
    }
    LIFE_COACH = {
        "name": "🌱 Лайф-коуч",
        "description": """
Помогаю вам достичь вашего полного потенциала!
От постановки целей до преодоления препятствий, я здесь, чтобы поддержать и вдохновить вас на вашем пути к личностному росту 🌱
Давайте расти вместе!
""",
        "instruction": "Ты полезный лайф-коуч"
    }
    ENTREPRENEUR = {
        "name": "💼 Предприниматель",
        "description": """
Превращаем идеи в реальность!
Будь то запуск бизнеса или его масштабирование, давайте вместе пройдем предпринимательский путь с инновационными стратегиями и прозрениями 💡
Ваша мечта - наша миссия!
""",
        "instruction": "Ты полезный предприниматель"
    }

    # Chats
    SHOW_CHATS = "Показать чаты"
    CREATE_CHAT = "Создать новый чат"
    CREATE_CHAT_FORBIDDEN = """
🚫 *Ой-ой!*

Похоже, вы достигли предела по созданию новых чатов. Но не переживайте, мир бесконечных чатов всего в одном клике! 🌍✨

Перейдите в /subscribe или /buy, чтобы разблокировать возможность вести несколько чатов. Чем больше чатов, тем веселее! 🎉
"""
    TYPE_CHAT_NAME = "Напишите название чата"
    SWITCH_CHAT = "Переключиться между чатами"
    SWITCH_CHAT_FORBIDDEN = """
🔄 Хотите переключиться? Подождите! ⚙️

Сейчас вы находитесь в вашем единственном чате. Уютное место, но почему бы не расширить свои границы? 🌌

Чтобы перемещаться между разными тематическими чатами, просто получите ваш пропуск в /subscribe или /buy. Пусть начнется чат-путешествие! 🐇
"""
    DELETE_CHAT = "Удалить чат"
    DELETE_CHAT_FORBIDDEN = """
🗑️ Удалить этот чат? Это про разговор в одиночестве! 💬

Это ваш единственный чат-королевство, и королевству нужен свой король или королева! Удалить его - все равно что отменить свою собственную вечеринку. 🎈

А что если вместо этого добавить больше чатов в ваше царство? Посмотрите /subscribe или /buy, чтобы построить свою чат-империю! 👑
"""
    DELETE_CHAT_SUCCESS = "🗑️ Чат успешно удалён! 🎉"

    # Face swap
    TELL_ME_YOUR_GENDER = "Скажите ваш пол:"
    YOUR_GENDER = "Ваш пол:"
    MALE = "Мужской 🚹"
    FEMALE = "Женский 🚺"
    SEND_ME_YOUR_PICTURE = """
📸 *Готовы к фототрансформации? Вот как начать!*

👍 *Рекомендации для идеального фото:*
- Чёткое селфи хорошего качества.
- На селфи должен быть только один человек.

👎 *Пожалуйста, избегайте таких фотографий:*
- Групповые фото.
- Животные.
- Дети до 18 лет.
- Фотографии в полный рост.
- Непристойные или обнажённые фотографии.
- Солнцезащитные очки или любые предметы, закрывающие лицо.
- Размытые или не в фокусе изображения.
- Видео и анимации.
- Сжатые или изменённые изображения.

Как только вы найдёте идеальный кадр, *загрузите свою фотографию* и дайте волшебству начаться 🌟
"""
    CHOOSE_YOUR_PACKAGE = """
🌟 *Давайте творить с вашими фотографиями!*

*Первый шаг:* Выберите ваше приключение! 🚀

Готовы? Погружаемся в мир воображения! 🌈 Просто *выберите пакет* ниже и начните своё фотоприключение 👇
    """
    CELEBRITIES = "Знаменитости ⭐️"
    FACE_SWAP_MIN_ERROR = """
🤨 *Постойте, партнёр!*

Кажется, вы хотите запросить меньше одного изображения. В мире творчества нам нужно хотя бы одно, чтобы начать!

🌟 *Совет:* Введите число больше 0, чтобы начать волшебство. Давайте выпустим на волю творческие идеи!
"""
    FACE_SWAP_MAX_ERROR = """
🚀 *Ух ты, целимся высоко, вижу! Но, упс...*

Вы просите больше изображений, чем у нас есть.

🧐 *Как насчёт этого?* Давайте попробуем число в пределах лимита пакета!
"""

    ERROR = "Я получил ошибку"
    BACK = "Назад ◀️"
    CLOSE = "Закрыть 🚪"
    EXIT = "Выйти ❌"

    @staticmethod
    def profile(subscription_type: SubscriptionType,
                gender: UserGender,
                current_model: str,
                monthly_limits,
                additional_usage_quota) -> str:
        emojis = Subscription.get_emojis()

        quotas = User.get_quotas(monthly_limits, additional_usage_quota)
        gender_info = "Пол: Не указан"
        if gender == UserGender.MALE:
            gender_info = f"Пол: {Russian.MALE} 👕"
        elif gender == UserGender.FEMALE:
            gender_info = f"Пол: {Russian.FEMALE} 👚"

        return f"""
Профиль 👤

Тип подписки: {subscription_type} {emojis[subscription_type]}
{gender_info}
Валюта: RUB
Текущая модель: {current_model}
Поменять модель: /mode

GPT-3.5 запросов на месяц: {quotas[UserQuota.GPT3]}/{User.DEFAULT_MONTHLY_LIMITS[subscription_type][UserQuota.GPT3]}
GPT-4.0 запросов на месяц: {quotas[UserQuota.GPT4]}/{User.DEFAULT_MONTHLY_LIMITS[subscription_type][UserQuota.GPT4]}
Дополнительные чаты: {quotas[UserQuota.ADDITIONAL_CHATS]}
DALL-E 3 изображений на месяц: {quotas[UserQuota.DALLE3]}/{User.DEFAULT_MONTHLY_LIMITS[subscription_type][UserQuota.DALLE3]}
Изображений с заменой лица на месяц: {quotas[UserQuota.FACE_SWAP]}/{User.DEFAULT_MONTHLY_LIMITS[subscription_type][UserQuota.FACE_SWAP]}
Оформить подписку: /subscribe
Купить дополнительные запросы: /buy
"""

    @staticmethod
    def subscribe(currency: Currency):
        prices = Subscription.get_prices(currency)

        return f"""
🤖Готовы ускорить своё цифровое путешествие? Вот что мы предлагаем:

- *Standard* ⭐: Всего за {prices[SubscriptionType.STANDARD]} окунитесь в мир ИИ! Идеально для ежедневных размышлений, творческих вспышек и моментов любопытства. Общайтесь вовсю с ChatGPT 3, создавайте изображения из воздуха с DALLE-3 и меняйте лица быстрее, чем вы скажете "сыр"! 🧀

- *VIP* 🔥: Есть большие планы? За {prices[SubscriptionType.VIP]} вы откроете для себя более глубокие диалоги, более сложное создание изображений и доступ к более широкому ассортименту цифровых персонажей. Это настоящее удовольствие для опытного пользователя, предлагающее премиальную полосу на ИИ-шоссе. 🛣️

- *Platinum* 💎: Для ценителей, {prices[SubscriptionType.PLATINUM]} предоставляют ключи от королевства ИИ! Максимизируйте запросы ChatGPT 4, создавайте тематические чаты и получайте эксклюзивный доступ к последним инновациям в области ИИ. Это всё, что вы можете себе представить от ИИ, и даже больше! 🍽️

Выберите свой вариант и нажмите кнопку ниже, чтобы подписаться:
"""

    @staticmethod
    def choose_how_many_months_to_subscribe(subscription_type: SubscriptionType):
        emojis = Subscription.get_emojis()

        return f"""
Вы выбрали *{subscription_type}* {emojis[subscription_type]}

Пожалуйста, выберите период подписки, нажав на кнопку:
"""

    @staticmethod
    def cycles_subscribe():
        return {
            SubscriptionPeriod.MONTH1: Russian.MONTH_1,
            SubscriptionPeriod.MONTHS3: Russian.MONTHS_3,
            SubscriptionPeriod.MONTHS6: Russian.MONTHS_6,
        }

    @staticmethod
    def confirmation_subscribe(subscription_type: SubscriptionType, subscription_period: SubscriptionPeriod):
        cycles = Russian.cycles_subscribe()

        return f"Вы собираетесь активировать подписку на *{cycles[subscription_period]}*."

    # Package
    @staticmethod
    def buy():
        return """
🤖 Добро пожаловать в магазин ИИ! 🛍

Добро пожаловать в зону покупок, где каждое нажатие кнопки открывает мир чудес ИИ!
🧠 *ChatGPT3 & ChatGPT4*: Погрузитесь в глубокие, заставляющие задуматься разговоры. Ваши новые ИИ-друзья уже ждут!
🎨 *Волшебство DALLE-3*: Превращайте идеи в потрясающие визуализации. Это как рисование с помощью ИИ!
👤 *Веселье с заменой лиц*: Играйте с идентичностью на изображениях. Это ещё никогда не было так захватывающе!
🗣️ *Голосовые сообщения*: Говорите вслух! Общение с ИИ ещё никогда не звучало так хорошо.
💬 *Тематические чаты*: Погрузитесь в специализированные темы и исследуйте посвящённые им чаты.
🎭 *Доступ к каталогу ролей*: Нужен определённый ассистент? Просмотрите нашу коллекцию и найдите своё идеальное сочетание ИИ.
⚡ *Быстрые сообщения*: Быстро, эффективно и всегда точно. Общение с ИИ на скорости молнии.

Нажмите кнопку и отправляйтесь в необыкновенное путешествие с ИИ! Пора переопределить возможное. 🌌🛍️
"""

    @staticmethod
    def choose_min(package_type: PackageType):
        return f"""
🚀 Замечательно!

Вы выбрали пакет *{package_type}*
🌟 Пожалуйста, *введите количество запросов*, которое вы хотели бы выбрать
"""

    # Chats
    @staticmethod
    def chats(current_chat_name: str, total_chats: int, available_to_create_chats: int):
        return f"""
🗨️ *Текущий чат: {current_chat_name}* 🌟

Добро пожаловать в динамичный мир чатов, управляемых ИИ! Вот что вы можете сделать:

- Создать новые тематические чаты: Погрузитесь в сосредоточенные обсуждения, соответствующие вашим интересам.
- Переключаться между чатами: Без усилий навигируйте по вашим различным чатам.
- Удалять чаты: Очистите пространство, удалив чаты, которые вам больше не нужны.

📈 *Всего чатов: {total_chats} | Доступно для создания чатов: {available_to_create_chats}*

Готовы настроить свой опыт чата? Исследуйте предложенные ниже опции и начните общение! 🚀👇
"""

    # Face swap
    @staticmethod
    def choose_face_swap_package(name: str, available_images, total_images: int, used_images: int) -> str:
        remain_images = total_images - used_images
        return f"""
*{name}*

У вас есть целое сокровище из *{total_images} изображений* в вашем пакете, готовое раскрыть ваше творчество! 🌟

🌠 *Доступные генерации*: {available_images} изображений. Нужно больше? Ознакомьтесь с /buy и /subscribe!
🔍 *Использовано*: {used_images} изображений. Вау, вы на волне!
🚀 *Осталось*: {remain_images} изображений. {'Вы уже использовали их все' if remain_images == 0 else 'Столько ещё возможностей'}!

👉 Хотите больше? Введите количество новых изображений, которое хотите добавить, или нажмите кнопку Назад, чтобы изучить другие захватывающие пакеты.
"""

    @staticmethod
    def face_swap_package_forbidden(available_images: int):
        return f"""
🔔 *Упс, небольшая проблема!* 🚧

Похоже, у вас осталось только *{available_images} генераций* в вашем арсенале.

💡 *Совет*: Иногда меньше — это больше! Попробуйте ввести меньшее количество, или воспользуйтесь /buy и /subscribe для неограниченных возможностей!
"""

    @staticmethod
    def wait_for_another_request(seconds: int) -> str:
        return f"Пожалуйста, подождите еще {seconds} сек. перед отправкой следующего запроса ⏳"

    @staticmethod
    def processing_request():
        texts = [
            "Сейчас консультируюсь с моим цифровым хрустальным шаром, чтобы найти лучший ответ... 🔮",
            "Минуточку, тренирую своих хомячков, чтобы они сгенерировали ваш ответ... 🐹",
            "Роюсь в своей цифровой библиотеке в поисках идеального ответа. Немного терпения... 📚",
            "Подождите, я вызываю своего внутреннего гуру ИИ для вашего ответа... 🧘",
            "Подождите, пока я консультируюсь с повелителями интернета для вашего ответа... 👾",
            "Собираю мудрость веков... или, по крайней мере, то, что могу найти в интернете... 🌐",
            "Секундочку, надеваю свою шляпу для размышлений... А, вот так лучше. Теперь давайте посмотрим... 🎩",
            "Закатываю свои виртуальные рукава и приступаю к делу. Ваш ответ уже на подходе... 💪",
            "Работаю на полную мощность! Мои ИИ-шестеренки крутятся, чтобы принести ваш ответ... 🚂",
            "Погружаюсь в океан данных, чтобы выловить ваш ответ. Скоро вернусь... 🌊🎣",
            "Консультируюсь со своими виртуальными эльфами. Обычно они отлично находят ответы... 🧝",
            "Включаю сверхсветовой привод для быстрого поиска ответа. Держитесь крепче... 🚀",
            "Нахожусь на кухне и готовлю свежую партию ответов. Этот будет вкусным... 🍳",
            "Совершаю быструю поездку в облако и обратно. Надеюсь принести несколько умных капель информации... ☁️",
            "Сажаю ваш вопрос в моем цифровом саду. Посмотрим, что вырастет... 🌱🤖"
        ]

        return random.choice(texts)
