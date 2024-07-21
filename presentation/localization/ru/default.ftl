BACK = Назад
MAIN_MENU = Главное меню

BOT_IS_NO_ADMIN_THAT_CHANNEL = Бот не является администратором этого канала 😕
CHANNEL_ALREADY_ADDED_TO_YOU = Канал уже добавлен ✅
CHANNEL_ERROR_ADD = Не удалось добавить канал 😞
CHANNEL_JUST_ADDED = Канал только что добавлен! 🎉

USER-HELLO = Привет, переходи в канал и ищи свой фильм по коду под видео, для этого можешь воспользоваться поиском! 🔍
USER-OPEN_CHANNEL = Перейти в канал 👉

ADMIN-ALL_USERS = Пользователи 👥
ADMIN-MESSAGING = Рассылка ✉️
ADMIN-CHANNELS = Каналы 📺

# USERS
ADMIN-USER_LIST_EMPTY = Нет пользователей ❌
ADMIN-USER_TEMPLATE = Username: <b>{$username}</b>
    Telegram ID: <b><code>{$userid}</code></b>
    Имя: <b>{$name} {$lastname}</b>
    Язык: <b>{$lang}</b>
    Присоединился: <b>{$date}</b>

# Messaging
ADMIN-CHOICE_TYPE_MESSAGE = Выберите, кому рассылка 📣
ADMIN-MESSAGE_ALL_CLIENTS = Всем клиентам 🌐
ADMIN-MESSAGE_INDIVIDUAL = Лично по Telegram ID 👤

ADMIN-SET_USER_ID = Введите Telegram ID пользователя:
ADMIN-SET_MESSAGE = Ваше сообщение (можно использовать формат Telegram):
ADMIN-SET_MEDIA = Отправьте Фото/Видео/Гифку по желанию:
ADMIN-MEDIA_WRONG = Неверный формат, отправьте (Фото/Видео/Гифку) в сжатом формате ❌
ADMIN-SET_BUTTON = Хотите добавить кнопку? 🔘
ADMIN-SET_BUTTON_TEXT = Текст для кнопки (желательно 20-30 символов):
ADMIN-BUTTON_TEXT_ERROR = Укоротите хотя бы до 50 символов, сейчас {$count} ❗️
ADMIN-SET_BUTTON_URL = Ссылка для кнопки:
ADMIN-BUTTON_URL_ERROR = Ссылка имеет неправильный формат, должна начинаться с https:// и содержать сайт или настоящий контакт в ТГ и т.д. ❗️
ADMIN-SET_BUTTON_NEXT = Хотите добавить еще одну кнопку? ➕
ADMIN-PREVIEW_MESSAGING = Если все правильно, можете отправлять! ✅
ADMIN-SEND = Отправить 🚀
ADMIN-RESTART = Начать сначала 🔄

ADMIN-RESULT_NOTIFICATION = <b>-Результат рассылки-</b>

    Получили сообщение: {$send}\{$users}
    Заблокировали бота: {$block}
    Другое: {$other}

# CHANNELS
ADMIN-CHANNEL-LIST_EMPTY = Нет каналов ❌
ADMIN-CHANNEL-TEMPLATE = ID Канала: <b><code>{$channel_id}</code></b>
    Название: <b>{$channel_name}</b>
    Добавлен: <b>{$date}</b>

    Активных ссылок: <b>{$link_count}</b>
    Пользователей присоединилось: <b>{$user_count}</b>
ADMIN-CHANNEL-DELETE = Удалить канал ❌
ADMIN-CHANNEL-CREATE_LINK = Создать ссылку 🔗
ADMIN-CHANNEL-MANAGE_LINK = Управлять ссылками 🔄
ADMIN-CHANNEL-DELETE_SUCCESS = Канал удален ✅
ADMIN-CHANNEL-DELETE_FAIL = Не удалось удалить канал ❌

# LINKS
ADMIN-LINK-LIST_EMPTY = Нет ссылок ❌
ADMIN-LINK = Ссылка канала: <b>{$channel_name}</b>
ADMIN-LINK-SET_NAME = Имя для ссылки:
ADMIN-LINK-CREATE_SUCCESS = Ссылка создана ✅
ADMIN-LINK-CREATE_FAIL = Не удалось создать ссылку ❌
ADMIN-LINK-TEMPLATE = {$title}
    ━━━━━━━━━━━━━━━━
    Канал: <b>{$channel}</b> (<code>{$channel_id}</code>)
    Ссылка: <b><code>{$link}</code></b>

    Пользователей присоединилось: <b>{$count_user}</b>
    Создано: <b>{$date}</b>
ADMIN-LINK-DELETE = Удалить ссылку ❌
ADMIN-LINK-DELETE_SUCCESS = Ссылка удалена ✅
ADMIN-LINK-DELETE_FAIL = Не удалось удалить ссылку ❌

# Notification
NOTIFICATION-NEW_USER = 👤 <b>Новый пользователь присоединился к боту!</b>
    ━━━━━━━━━━━━━━━━
    Имя: <b>@{$username}</b>
    Телеграм ID: <code>{$user_id}</code>
    Присоединился: <b>{$join_at}</b>
NOTIFICATION-NEW_USER_BY_LINK = 👤 <b>Новый пользователь присоединился к боту через ссылку!</b>
    ━━━━━━━━━━━━━━━━
    Имя: <b>@{$username}</b>
    Телеграм ID: <code>{$user_id}</code>
    Присоединился: <b>{$join_at}</b>
