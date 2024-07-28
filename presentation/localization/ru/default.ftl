BACK = Назад
SKIP = Пропустить
MAIN_MENU = Главное меню
YES = Да
NO = Нет

BOT_IS_NO_ADMIN_THAT_CHANNEL = Бот не является админом этого канала 😕
CHANNEL_ALREADY_ADDED_TO_YOU = Канал уже добавлен ✅
CHANNEL_ERROR_ADD = Не удалось добавить канал 😞
CHANNEL_JUST_ADDED = Канал только что добавлен! 🎉

USER-HELLO=Привет, переходи в канал и ищи свой фильм по коду под видео, для этого можешь воспользоваться поиском! 🔍
USER-OPEN_CHANNEL = Перейти в канал 👉

ADMIN-ALL_USERS = Пользователи 👥
ADMIN-MESSAGING = Рассылка ✉️
ADMIN-CHANNELS = Каналы 📺

#USERS
ADMIN-USER_LIST_EMPTY = Нет пользователей ❌
ADMIN-USER_TEMPLATE = Username: <b>{$username}</b>
 Telegram ID: <b><code>{$userid}</code></b>
 Имя: <b>{$name} {$lastname}</b>
 Язык: <b>{$lang}</b>
 Присоединился: <b>{$date}</b>

# Messaging
ADMIN-CHOICE_TYPE_MESSAGE=Выберите для кого рассылка 📣
ADMIN-MESSAGE_ALL_CLIENTS = Всем клиентам 🌐
ADMIN-MESSAGE_INDIVIDUAL = Лично по Telegram ID 👤

ADMIN-SET_USER_ID = Введите Telegram ID пользователя:
ADMIN-SET_MESSAGE = Ваше сообщение (можно использовать формат телеграммы):
ADMIN-SET_MEDIA = Отправьте Фото/Видео/Гифку по желанию:
ADMIN-MEDIA_WRONG = Неверный формат, отправьте (Фото/Видео/Гифку) в сжатом формате ❌
ADMIN-SET_BUTTON = Вы хотите добавить кнопку? 🔘
ADMIN-SET_BUTTON_TEXT = Текст для кнопки (20-30 символов желательно):
ADMIN-BUTTON_TEXT_ERROR=Сократи хотя бы до 50 символов, сейчас {$count} ❗️
ADMIN-SET_BUTTON_URL = Ссылка для кнопки:
ADMIN-BUTTON_URL_ERROR = Ссылка имеет неправильный формат, она должна начинаться с https:// и содержать сайт или настоящий контакт в тг и т.д. ❗️
ADMIN-SET_BUTTON_NEXT = Хотите добавить еще кнопку? ➕
ADMIN-PREVIEW_MESSAGING=Если все правильно, можете отправлять! ✅
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

 Активные ссылки: <b>{$link_count}</b>
 Пользователей присоединилось: <b>{$user_count}</b>
ADMIN-CHANNEL-DELETE = Удалить канал ❌
ADMIN-CHANNEL-CREATE_LINK = Создать ссылку 🔗
ADMIN-CHANNEL-MANAGE_LINK = Управлять ссылками 🔄
ADMIN-CHANNEL-DELETE_SUCCESS = Удаленный канал ✅
ADMIN-CHANNEL-DELETE_FAIL = Не удалось удалить канал ❌

#LINKS
ADMIN-LINK-LIST_EMPTY = Нет ссылок ❌
ADMIN-LINK = Ссылка канала: <b>{$channel_name}</b>
ADMIN-LINK-SET_NAME = Имя для ссылки:
ADMIN-LINK-CREATE_SUCCESS = Ссылка создана ✅
ADMIN-LINK-CREATE_FAIL = Невозможно создать ссылку ❌
ADMIN-LINK-TEMPLATE = {$title}
 ━━━━━━━━━━━━━━━━━
 Канал: <b>{$channel}</b> (<code>{$channel_id}</code>)
 Ссылки: <b><code>{$link}</code></b>

 Пользователей присоединилось: <b>{$count_user}</b>
 Создано: <b>{$date}</b>
ADMIN-LINK-DELETE = Удалить ссылку ❌
ADMIN-LINK-DELETE_SUCCESS = Ссылка удалена ✅
ADMIN-LINK-DELETE_FAIL = Не удалось удалить ссылку ❌

# Notification
NOTIFICATION-NEW_USER = 👤 <b>Новый пользователь подключился к боту!</b>
 ━━━━━━━━━━━━━━━━━
 Имя: <b>@{$username}</b>
 Телеграммы ID: <code>{$user_id}</code>
 Присоединился: <b>{$join_at}</b>
NOTIFICATION-NEW_USER_BY_LINK = 👤 <b>Новый пользователь подключился к боту через ссылку!</b>
 ━━━━━━━━━━━━━━━━━
 Имя: <b>@{$username}</b>
 Телеграммы ID: <code>{$user_id}</code>
 Присоединился: <b>{$join_at}</b>

#POST CHANNEL
ADMIN-POST = Создать пост 📌
ADMIN-POST-CHOICE_CHANNEL = Выберите канал для публикации поста 📢
ADMIN-POST-SET_NAME = Название фильма: 🎬
ADMIN-POST-SET_YEAR = Укажите год выпуска: 📅
ADMIN-POST-SET_TEMP = Продолжительность фильма: ⏳
ADMIN-POST-SET_DESC = Описание фильма (до 1000 символов): 📖
ADMIN-POST-SET_DESC_ERROR = Длина описания <b>{$size}</b>, а должно быть не более 1000 ❗️
ADMIN-POST-SET_MEDIA = Файл медиа (видео\картинка): 🖼️🎥
ADMIN-POST-SET_MEDIA_ERROR = Неверный формат, отправьте (Фото\Видео) в сжатом формате: ❌
ADMIN-POST-SET_BUTTON = Добавить кнопку в пост? 🔘
ADMIN-POST-SET_BUTTON_TEXT = Текст для кнопки (20-30 символов желательно): ✏️
ADMIN-POST-BUTTON_TEXT_ERROR=Сократи хотя бы до 50 символов, сейчас {$count} ❗️
ADMIN-POST-SET_BUTTON_URL = Ссылка для кнопки: 🔗
ADMIN-POST-BUTTON_URL_ERROR = Ссылка имеет неправильный формат, она должна начинаться с https:// и содержать сайт или настоящий контакт в тг и т.д. ❌
ADMIN-POST-SET_BUTTON_NEXT = Хотите добавить еще кнопку? ➕
ADMIN-POST-PREVIEW_POST=Если все правильно, можете отправлять! ✅
ADMIN-POST-SEND = Отправить 🚀
ADMIN-POST-SEND_ERROR_DB = Невозможно отправить (database) ❌
ADMIN-POST-SEND_ERROR_TG = Не удалось отправить (telegram) ❌
ADMIN-POST-SEND_SUCCESS = Пост успешно опубликован! 🎉

ADMIN-POST-CODE_REPLACE=Код будет сгенерирован при публикации

ADMIN-POST-TEMPLATE = <b>{$name}</b> | код: <code>{$code}</code>
 ━━━━━━━━━━━━━━━━━
 🎬 <b>Название фильма:</b> {$name}
 📅 <b>Год выпуска:</b> {$year}
 🕒 <b>Длительность:</b> {$temp}

 📖 <b>Описание:</b>
 {$desc}

 🔍 <b>Код для поиска:</b> <code>{$code}</code>