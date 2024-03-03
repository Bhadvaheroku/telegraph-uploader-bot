import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from telegraph import upload_file
from config import Config

bot = Client(
    "bot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN
)

INLINE_SELECT = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("ᴍᴏʀᴇ 🥀", url="https://t.me/TryToLiveAlon"),
            InlineKeyboardButton("ʀᴇᴘᴏʀᴛ ʙᴜɢs 🤖", url="https://t.me/deathchatting_world")
        ],
        [
            InlineKeyboardButton("Jᴏɪɴ Cʜᴀɴɴᴇʟ 1 🌐", url="https://t.me/Channel1"),
            InlineKeyboardButton("Jᴏɪɴ Cʜᴀɴɴᴇʟ 2 🌐", url="https://t.me/Channel2")
        ]
    ]
)

ERROR_BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("ʀᴇᴘᴏʀᴛ ʙᴜɢs 🤖", url="https://t.me/deathchatting_world"),
            InlineKeyboardButton("Jᴏɪɴ Cʜᴀɴɴᴇʟ 1 🌐", url="https://t.me/Channel1"),
            InlineKeyboardButton("Jᴏɪɴ Cʜᴀɴɴᴇʟ 2 🌐", url="https://t.me/Channel2")
        ]
    ]
)


async def user_in_channels(user_id):
    # Check if the user is a member of both channels
    channel1_member = await bot.get_chat_member("@DeathxBotz", user_id)
    channel2_member = await bot.get_chat_member("@deathking_botworld", user_id)
    return channel1_member.status == "member" and channel2_member.status == "member"


@bot.on_message(filters.command("start") & filters.private)
async def start(bot, message):
    if not await user_in_channels(message.from_user.id):
        # If the user is not a member of one or both channels
        text = "You must join both channels to use this bot. Please join Channel1 and Channel2."
        reply_markup = ERROR_BUTTON
    else:
        # If the user is a member of both channels
        text = f"Hello {message.from_user.first_name}!\n\nWelcome to the Telegraph uploader bot.\nYou can send me any " \
               f"image, video, animation, or sticker and I will upload it to telegraph and send you a generated link. But the file must be LESS THAN 5MB!!\n\n" \
               f"<a href=https://t.me/TryToLiveAlon>Feel free to leave a feedback</a>"
        reply_markup = INLINE_SELECT
    
    await message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )


async def upload_media(bot, message, media_type):
    if not await user_in_channels(message.from_user.id):
        # If the user is not a member of one or both channels
        await message.reply(
            "You must join both channels to use this bot. Please join Channel1 and Channel2.",
            reply_markup=ERROR_BUTTON
        )
        return

    # If the user is a member of both channels
    msg = await message.reply(f"Your {media_type} is being uploaded...", quote=True)
    download_path = await bot.download_media(
        message=message, file_name=f"{media_type}/jetg"
    )
    try:
        link = upload_file(download_path)
        generated_link = "https://telegra.ph" + "".join(link)

        IN_BUTTON = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("ᴍᴏʀᴇ 🥀", url="https://t.me/TryToLiveAlon"),
                    InlineKeyboardButton("ʀᴇᴘᴏʀᴛ ʙᴜɢs 🤖", url="https://t.me/deathchatting_world")
                ],
                [
                    InlineKeyboardButton("ᴡᴇʙ ᴘʀᴇᴠɪᴇᴡ 🌐", url=generated_link)
                ]
            ]
        )
    except:
        await msg.edit_text(
            f"File must be less than 5mb, please try another file or <a href=https://t.me/sanilaassistant_bot>LEARN THIS BOT FIRST!</a>",
            disable_web_page_preview=True, reply_markup=ERROR_BUTTON)
    else:
        t = await msg.edit_text(generated_link, disable_web_page_preview=True)
        await t.edit_text(
            f"Link - `{generated_link} `\n\n<a href=https://t.me/sanilaassistant_bot>Feel free to leave a feedback</a>",
            reply_markup=IN_BUTTON,
            disable_web_page_preview=True)
    finally:
        os.remove(download_path)


@bot.on_message(filters.photo & filters.private)
async def photo_upload(bot, message):
    await upload_media(bot, message, "photo")


@bot.on_message(filters.video & filters.private)
async def video_upload(bot, message):
    await upload_media(bot, message, "video")


@bot.on_message(filters.animation & filters.private)
async def animation_upload(bot, message):
    await upload_media(bot, message, "animation")


@bot.on_message(filters.sticker)
async def sticker_upload(bot, message):
    await upload_media(bot, message, "sticker")


print("All good")

bot.run()
