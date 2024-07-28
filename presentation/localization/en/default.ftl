BACK = Back
SKIP = Skip
MAIN_MENU = Main Menu
YES = Yes
NO = No

BOT_IS_NO_ADMIN_THAT_CHANNEL = The bot is not an admin of this channel 😕
CHANNEL_ALREADY_ADDED_TO_YOU = Channel already added ✅
CHANNEL_ERROR_ADD = Failed to add channel 😞
CHANNEL_JUST_ADDED = Channel just added! 🎉

USER-HELLO = Hello, go to the channel and search for your movie by the code under the video, for this you can use the search! 🔍
USER-OPEN_CHANNEL = Go to channel 👉

ADMIN-ALL_USERS = Users 👥
ADMIN-MESSAGING = Mailing ✉️
ADMIN-CHANNELS = Channels 📺

# USERS
ADMIN-USER_LIST_EMPTY = No users ❌
ADMIN-USER_TEMPLATE = Username: <b>{$username}</b>
 Telegram ID: <b><code>{$userid}</code></b>
 Name: <b>{$name} {$lastname}</b>
 Language: <b>{$lang}</b>
 Joined: <b>{$date}</b>

# Messaging
ADMIN-CHOICE_TYPE_MESSAGE = Choose who the newsletter is for 📣
ADMIN-MESSAGE_ALL_CLIENTS = To all clients 🌐
ADMIN-MESSAGE_INDIVIDUAL = Personally by Telegram ID 👤

ADMIN-SET_USER_ID = Enter Telegram user ID:
ADMIN-SET_MESSAGE = Your message (Telegram format can be used):
ADMIN-SET_MEDIA = Send Photo/Video/Gif as desired:
ADMIN-MEDIA_WRONG = Incorrect format, send (Photo/Video/Gif) in compressed format ❌
ADMIN-SET_BUTTON = Want to add a button? 🔘
ADMIN-SET_BUTTON_TEXT = Text for the button (20-30 characters preferred):
ADMIN-BUTTON_TEXT_ERROR = Cut to at least 50 characters, now {$count} ❗️
ADMIN-SET_BUTTON_URL = URL for button:
ADMIN-BUTTON_URL_ERROR = The link has the wrong format, it must start with https:// and contain a site or real contact in tg, etc. ❗️
ADMIN-SET_BUTTON_NEXT = Do you want to add another button? ➕
ADMIN-PREVIEW_MESSAGING = If everything is correct, you can send! ✅
ADMIN-SEND = Send 🚀
ADMIN-RESTART = Start over 🔄

ADMIN-RESULT_NOTIFICATION = <b>-Notification result-</b>

 Message received: {$send}\{$users}
 Bot blocked: {$block}
 Other: {$other}

# CHANNELS
ADMIN-CHANNEL-LIST_EMPTY = No channels ❌
ADMIN-CHANNEL-TEMPLATE = Channel ID: <b><code>{$channel_id}</code></b>
 Name: <b>{$channel_name}</b>
 Added: <b>{$date}</b>

 Active links: <b>{$link_count}</b>
 Added users: <b>{$user_count}</b>
ADMIN-CHANNEL-DELETE = Delete channel ❌
ADMIN-CHANNEL-CREATE_LINK = Create link 🔗
ADMIN-CHANNEL-MANAGE_LINK = Manage links 🔄
ADMIN-CHANNEL-DELETE_SUCCESS = Channel deleted ✅
ADMIN-CHANNEL-DELETE_FAIL = Failed to delete channel ❌

# LINKS
ADMIN-LINK-LIST_EMPTY = No links ❌
ADMIN-LINK = Channel link: <b>{$channel_name}</b>
ADMIN-LINK-SET_NAME = Name for link:
ADMIN-LINK-CREATE_SUCCESS = Link created ✅
ADMIN-LINK-CREATE_FAIL = Failed to create link ❌
ADMIN-LINK-TEMPLATE = {$title}
 ━━━━━━━━━━━━━━━━
 Channel: <b>{$channel}</b> (<code>{$channel_id}</code>)
 Link: <b><code>{$link}</code></b>

 Added users: <b>{$count_user}</b>
 Created: <b>{$date}</b>
ADMIN-LINK-DELETE = Delete link ❌
ADMIN-LINK-DELETE_SUCCESS = Link deleted ✅
ADMIN-LINK-DELETE_FAIL = Failed to delete link ❌

# Notification
NOTIFICATION-NEW_USER = 👤 <b>A new user has joined the bot!</b>
 ━━━━━━━━━━━━━━━━
 Name: <b>@{$username}</b>
 Telegram ID: <code>{$user_id}</code>
 Joined by: <b>{$join_at}</b>
NOTIFICATION-NEW_USER_BY_LINK = 👤 <b>A new user has joined the bot via a link!</b>
 ━━━━━━━━━━━━━━━━
 Name: <b>@{$username}</b>
 Telegram ID: <code>{$user_id}</code>
 Joined by: <b>{$join_at}</b>

# POST CHANNEL
ADMIN-POST = Create a post 📌
ADMIN-POST-CHOICE_CHANNEL = Choose a channel to publish a post 📢
ADMIN-POST-SET_NAME = Movie Name: 🎬
ADMIN-POST-SET_YEAR = Enter year of release: 📅
ADMIN-POST-SET_TEMP = Movie duration: ⏳
ADMIN-POST-SET_DESC = Movie description (up to 1000 characters): 📖
ADMIN-POST-SET_DESC_ERROR = The length of the description is <b>{$size}</b>, but it should not be more than 1000 ❗️
ADMIN-POST-SET_MEDIA = Media file (video\picture): 🖼️🎥
ADMIN-POST-SET_MEDIA_ERROR = Invalid format, send (Photo\Video) in compressed format: ❌
ADMIN-POST-SET_BUTTON = Add button to post? 🔘
ADMIN-POST-SET_BUTTON_TEXT = Text for the button (20-30 characters preferred): ✏️
ADMIN-POST-BUTTON_TEXT_ERROR = Cut to at least 50 characters, now {$count} ❗️
ADMIN-POST-SET_BUTTON_URL = URL for button: 🔗
ADMIN-POST-BUTTON_URL_ERROR = The link is in the wrong format, it must start with https:// and contain a site or real contact in tg, etc. ❌
ADMIN-POST-SET_BUTTON_NEXT = Do you want to add another button? ➕
ADMIN-POST-PREVIEW_POST = If everything is correct, you can send! ✅
ADMIN-POST-SEND = Send 🚀
ADMIN-POST-SEND_ERROR_DB = Failed to send (database) ❌
ADMIN-POST-SEND_ERROR_TG = Failed to send (telegram) ❌
ADMIN-POST-SEND_SUCCESS = Post successfully published! 🎉

ADMIN-POST-CODE_REPLACE = Code will be generated on post

ADMIN-POST-TEMPLATE = <b>{$name}</b> | code: <code>{$code}</code>
 ━━━━━━━━━━━━━━━━
 🎬 <b>Movie name:</b> {$name}
 📅 <b>Year of issue:</b> {$year}
 🕒 <b>Duration:</b> {$temp}

 📖 <b>Description:</b>
 {$desc}

 🔍 <b>Search code:</b> <code>{$code}</code>