BACK = Back
MAIN_MENU = Main Menu

BOT_IS_NO_ADMIN_THAT_CHANNEL = The bot is not an admin of this channel 😕
CHANNEL_ALREADY_ADDED_TO_YOU = Channel already added ✅
CHANNEL_ERROR_ADD = Failed to add channel 😞
CHANNEL_JUST_ADDED = Channel just added! 🎉

USER-HELLO = Hi, join the channel and find your movie by the code under the video, you can use the search for this! 🔍
USER-OPEN_CHANNEL = Join the channel 👉

ADMIN-ALL_USERS = Users 👥
ADMIN-MESSAGING = Messaging ✉️
ADMIN-CHANNELS = Channels 📺

# USERS
ADMIN-USER_LIST_EMPTY = No users ❌
ADMIN-USER_TEMPLATE = Username: <b>{$username}</b>
    Telegram ID: <b><code>{$userid}</code></b>
    Name: <b>{$name} {$lastname}</b>
    Language: <b>{$lang}</b>
    Joined: <b>{$date}</b>

# Messaging
ADMIN-CHOICE_TYPE_MESSAGE = Choose who to message 📣
ADMIN-MESSAGE_ALL_CLIENTS = To all clients 🌐
ADMIN-MESSAGE_INDIVIDUAL = Individually by Telegram ID 👤

ADMIN-SET_USER_ID = Enter the user's Telegram ID:
ADMIN-SET_MESSAGE = Your message (Telegram format allowed):
ADMIN-SET_MEDIA = Send a Photo/Video/GIF if desired:
ADMIN-MEDIA_WRONG = Incorrect format, send (Photo/Video/GIF) in compressed format ❌
ADMIN-SET_BUTTON = Do you want to add a button? 🔘
ADMIN-SET_BUTTON_TEXT = Button text (preferably 20-30 characters):
ADMIN-BUTTON_TEXT_ERROR = Shorten to at least 50 characters, currently {$count} ❗️
ADMIN-SET_BUTTON_URL = URL for the button:
ADMIN-BUTTON_URL_ERROR = The link has an incorrect format, it must start with https:// and contain a site or a real contact in TG etc ❗️
ADMIN-SET_BUTTON_NEXT = Do you want to add another button? ➕
ADMIN-PREVIEW_MESSAGING = If everything is correct, you can send it! ✅
ADMIN-SEND = Send 🚀
ADMIN-RESTART = Restart 🔄

ADMIN-RESULT_NOTIFICATION = <b>-Messaging Result-</b>

    Message received: {$send}\{$users}
    Bot blocked: {$block}
    Other: {$other}

# CHANNELS
ADMIN-CHANNEL-LIST_EMPTY = No channels ❌
ADMIN-CHANNEL-TEMPLATE = Channel ID: <b><code>{$channel_id}</code></b>
    Name: <b>{$channel_name}</b>
    Added: <b>{$date}</b>

    Active links: <b>{$link_count}</b>
    Users joined: <b>{$user_count}</b>
ADMIN-CHANNEL-DELETE = Delete channel ❌
ADMIN-CHANNEL-CREATE_LINK = Create link 🔗
ADMIN-CHANNEL-MANAGE_LINK = Manage links 🔄
ADMIN-CHANNEL-DELETE_SUCCESS = Channel deleted ✅
ADMIN-CHANNEL-DELETE_FAIL = Failed to delete channel ❌

# LINKS
ADMIN-LINK-LIST_EMPTY = No links ❌
ADMIN-LINK = Channel link: <b>{$channel_name}</b>
ADMIN-LINK-SET_NAME = Name for the link:
ADMIN-LINK-CREATE_SUCCESS = Link created ✅
ADMIN-LINK-CREATE_FAIL = Failed to create link ❌
ADMIN-LINK-TEMPLATE = {$title}
    ━━━━━━━━━━━━━━━━
    Channel: <b>{$channel}</b> (<code>{$channel_id}</code>)
    Link: <b><code>{$link}</code></b>

    Users joined: <b>{$count_user}</b>
    Created: <b>{$date}</b>
ADMIN-LINK-DELETE = Delete link ❌
ADMIN-LINK-DELETE_SUCCESS = Link deleted ✅
ADMIN-LINK-DELETE_FAIL = Failed to delete link ❌

# Notification
NOTIFICATION-NEW_USER = 👤 <b>A new user joined the bot!</b>
    ━━━━━━━━━━━━━━━━
    Name: <b>@{$username}</b>
    Telegram ID: <code>{$user_id}</code>
    Joined: <b>{$join_at}</b>
NOTIFICATION-NEW_USER_BY_LINK = 👤 <b>A new user joined the bot via link!</b>
    ━━━━━━━━━━━━━━━━
    Name: <b>@{$username}</b>
    Telegram ID: <code>{$user_id}</code>
    Joined: <b>{$join_at}</b>

# POST CHANNEL
ADMIN-POST = Create post 📌
ADMIN-POST-CHOICE_CHANNEL = Choose a channel for posting 📢
ADMIN-POST-SET_NAME = Movie title: 🎬
ADMIN-POST-SET_YEAR = Specify the release year: 📅
ADMIN-POST-SET_TEMP = Movie duration: ⏳
ADMIN-POST-SET_DESC = Movie description (up to 1000 characters): 📖
ADMIN-POST-SET_DESC_ERROR = Description length is <b>{$size}</b>, but should be no more than 1000 ❗️
ADMIN-POST-SET_MEDIA = Media file (video\image): 🖼️🎥
ADMIN-POST-SET_MEDIA_ERROR = Incorrect format, send (Photo\Video) in compressed format: ❌
ADMIN-POST-SET_BUTTON = Add a button to the post? 🔘
ADMIN-POST-SET_BUTTON_TEXT = Button text (preferably 20-30 characters): ✏️
ADMIN-POST-BUTTON_TEXT_ERROR = Shorten to at least 50 characters, currently {$count} ❗️
ADMIN-POST-SET_BUTTON_URL = Button link: 🔗
ADMIN-POST-BUTTON_URL_ERROR = The link has an incorrect format, it must start with https:// and contain a site or a real contact in TG etc ❌
ADMIN-POST-SET_BUTTON_NEXT = Do you want to add another button? ➕
ADMIN-POST-PREVIEW_POST = If everything is correct, you can send it! ✅
ADMIN-POST-SEND = Send 🚀
ADMIN-POST-SEND_ERROR_DB = Failed to send (database) ❌
ADMIN-POST-SEND_ERROR_TG = Failed to send (telegram) ❌
ADMIN-POST-SEND_SUCCESS = Post successfully published! 🎉

ADMIN-POST-CODE_REPLACE = Code will be generated upon publication

ADMIN-POST-TEMPLATE = <b>{$name}</b> | code: <code>{$code}</code>
    ━━━━━━━━━━━━━━━━
    🎬 <b>Movie title:</b> {$name}
    📅 <b>Release year:</b> {$year}
    🕒 <b>Duration:</b> {$temp}

    📖 <b>Description:</b>
    {$desc}

    🔍 <b>Search code:</b> <code>{$code}</code>
