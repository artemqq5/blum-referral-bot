BACK = Назад
SKIP = Пропустити
MAIN_MENU = Головне меню
YES = Так
NO = Ні

BOT_IS_NO_ADMIN_THAT_CHANNEL = Бот не є адміном цього каналу 😕
CHANNEL_ALREADY_ADDED_TO_YOU = Канал вже доданий ✅
CHANNEL_ERROR_ADD = Не вийшло додати канал 😞
CHANNEL_JUST_ADDED = Канал щойно додано! 🎉

USER-HELLO = Привіт, переходь в канал і шукай свій фільм за кодом під відео, для цього можеш скористатися пошуком! 🔍
USER-OPEN_CHANNEL = Перейти в канал 👉

ADMIN-ALL_USERS = Користувачі 👥
ADMIN-MESSAGING = Розсилка ✉️
ADMIN-CHANNELS = Канали 📺

# USERS
ADMIN-USER_LIST_EMPTY = Немає користувачів ❌
ADMIN-USER_TEMPLATE = Username: <b>{$username}</b>
    Telegram ID: <b><code>{$userid}</code></b>
    Ім'я: <b>{$name} {$lastname}</b>
    Мова: <b>{$lang}</b>
    Приєднався: <b>{$date}</b>

# Messaging
ADMIN-CHOICE_TYPE_MESSAGE = Оберіть для кого розсилка 📣
ADMIN-MESSAGE_ALL_CLIENTS = Всім клієнтам 🌐
ADMIN-MESSAGE_INDIVIDUAL = Особисто по Telegram ID 👤

ADMIN-SET_USER_ID = Введіть Telegram ID користувача:
ADMIN-SET_MESSAGE = Ваше повідомлення (Можна використовувати формат телеграма):
ADMIN-SET_MEDIA = Надішліть Фото/Відео/Гіфку за бажанням:
ADMIN-MEDIA_WRONG = Невірний формат, надішліть (Фото/Відео/Гіфку) у стисненому форматі ❌
ADMIN-SET_BUTTON = Бажаєте додати кнопку? 🔘
ADMIN-SET_BUTTON_TEXT = Текст для кнопки (20-30 символів бажано):
ADMIN-BUTTON_TEXT_ERROR = Скороти хоча б до 50 символів, зараз {$count} ❗️
ADMIN-SET_BUTTON_URL = Посилання для кнопки:
ADMIN-BUTTON_URL_ERROR = Посилання має неправильний формат, воно має починатися з https:// та містити сайт або справжній контакт в тг тощо ❗️
ADMIN-SET_BUTTON_NEXT = Бажаєте додати ще кнопку? ➕
ADMIN-PREVIEW_MESSAGING = Якщо все правильно, можете відправляти! ✅
ADMIN-SEND = Відправити 🚀
ADMIN-RESTART = Почати спочатку 🔄

ADMIN-RESULT_NOTIFICATION = <b>-Результат розсилки-</b>

    Отримали повідомлення: {$send}\{$users}
    Заблокували бота: {$block}
    Інше: {$other}

# CHANNELS
ADMIN-CHANNEL-LIST_EMPTY = Немає каналів ❌
ADMIN-CHANNEL-TEMPLATE = ID Каналу: <b><code>{$channel_id}</code></b>
    Назва: <b>{$channel_name}</b>
    Доданий: <b>{$date}</b>

    Активних посилань: <b>{$link_count}</b>
    Користувачів доєдналося: <b>{$user_count}</b>
ADMIN-CHANNEL-DELETE = Видалити канал ❌
ADMIN-CHANNEL-CREATE_LINK = Створити посилання 🔗
ADMIN-CHANNEL-MANAGE_LINK = Управляти посиланнями 🔄
ADMIN-CHANNEL-DELETE_SUCCESS = Канал видалено ✅
ADMIN-CHANNEL-DELETE_FAIL = Не вийшло видалити канал ❌

# LINKS
ADMIN-LINK-LIST_EMPTY = Немає посилань ❌
ADMIN-LINK = Посилання каналу: <b>{$channel_name}</b>
ADMIN-LINK-SET_NAME = Ім'я для посилання:
ADMIN-LINK-CREATE_SUCCESS = Посилання створено ✅
ADMIN-LINK-CREATE_FAIL = Не вдалося створити посилання ❌
ADMIN-LINK-TEMPLATE = {$title}
    ━━━━━━━━━━━━━━━━
    Канал: <b>{$channel}</b> (<code>{$channel_id}</code>)
    Посислання: <b><code>{$link}</code></b>

    Користувачів доєдналося: <b>{$count_user}</b>
    Створено: <b>{$date}</b>
ADMIN-LINK-DELETE = Видалити посилання ❌
ADMIN-LINK-DELETE_SUCCESS = Посилання видалено ✅
ADMIN-LINK-DELETE_FAIL = Не вийшло видалити посиланння ❌

# Notification
NOTIFICATION-NEW_USER = 👤 <b>Новий користувач доєднався до боту!</b>
    ━━━━━━━━━━━━━━━━
    Ім'я: <b>@{$username}</b>
    Телеграм ID: <code>{$user_id}</code>
    Приєднався: <b>{$join_at}</b>
NOTIFICATION-NEW_USER_BY_LINK = 👤 <b>Новий користувач доєднався до боту через посилання!</b>
    ━━━━━━━━━━━━━━━━
    Ім'я: <b>@{$username}</b>
    Телеграм ID: <code>{$user_id}</code>
    Приєднався: <b>{$join_at}</b>

# POST CHANNEL
ADMIN-POST = Створити пост 📌
ADMIN-POST-CHOICE_CHANNEL = Оберіть канал для публікації посту 📢
ADMIN-POST-SET_NAME = Назва фільму: 🎬
ADMIN-POST-SET_YEAR = Вкажіть рік випуску: 📅
ADMIN-POST-SET_TEMP = Тривалість фільму: ⏳
ADMIN-POST-SET_DESC = Опис фільму (до 1000 символів): 📖
ADMIN-POST-SET_DESC_ERROR = Довжина опису <b>{$size}</b>, а має бути не більше 1000 ❗️
ADMIN-POST-SET_MEDIA = Медіа файл (відео\картинка): 🖼️🎥
ADMIN-POST-SET_MEDIA_ERROR = Невірний формат, надішліть (Фото\Відео) у стисненому форматі: ❌
ADMIN-POST-SET_BUTTON = Додати кнопку до посту? 🔘
ADMIN-POST-SET_BUTTON_TEXT = Текст для кнопки (20-30 символів бажано): ✏️
ADMIN-POST-BUTTON_TEXT_ERROR = Скороти хоча б до 50 символів, зараз {$count} ❗️
ADMIN-POST-SET_BUTTON_URL = Посилання для кнопки: 🔗
ADMIN-POST-BUTTON_URL_ERROR = Посилання має неправильний формат, воно має починатися з https:// та містити сайт або справжній контакт в тг тощо ❌
ADMIN-POST-SET_BUTTON_NEXT = Бажаєте додати ще кнопку? ➕
ADMIN-POST-PREVIEW_POST = Якщо все правильно, можете відправляти! ✅
ADMIN-POST-SEND = Відправити 🚀
ADMIN-POST-SEND_ERROR_DB = Не вийшло відправити (database) ❌
ADMIN-POST-SEND_ERROR_TG = Не вийшло відправити (telegram) ❌
ADMIN-POST-SEND_SUCCESS = Пост успішно опубліковано! 🎉

ADMIN-POST-CODE_REPLACE = Код буде згенеровано при публікації

ADMIN-POST-TEMPLATE =
    🎬 <b>Назва фільму:</b> {$name}
    📅 <b>Рік випуску:</b> {$year}
    🕒 <b>Тривалість:</b> {$temp}

    📖 <b>Опис:</b>
    {$desc}

    🔍 <b>Код для пошуку:</b> <code>{$code}</code>
