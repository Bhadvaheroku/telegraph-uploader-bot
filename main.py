
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
            InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴘᴇʀ 🥀", url="https://t.me/TryToLiveAlon"),
            InlineKeyboardButton("ʀᴇᴘᴏʀᴛ ʙᴜɢs 🤖", url="https://t.me/deathchatting_world")
        ],
        [
            InlineKeyboardButton("Jᴏɪɴ ᴄʜᴀɴɴᴇʟ 🌐", url="https://t.me/deathking_botworld")
        ]
    ]
)

ERROR_BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("ʀᴇᴘᴏʀᴛ ʙᴜɢs 🤖", url="https://t.me/deathchatting_world"),
            InlineKeyboardButton("ʟᴇᴀʀɴ ʙᴏᴛ 🙂", url="https://t.me/deathchatting_world")
        ]
    ]
)


@bot.on_message(filters.command("start") & filters.private)
async def start(bot, message):
    text = f"Hello {message.from_user.first_name}!\n\nWelcome to the Telegraph uploader bot.\nYou can send me any " \
           f"image, video, animation and I will upload it to telegraph and send you a generated link. But the file must be LESS THAN 5MB!!\n\n" \
           f"<a href=https://t.me/deathchatting_world>Feel free to leave a feedback</a>"
    image_url = "URL_TO_YOUR_IMAGE"
    await message.reply_photo(photo=image_url, caption=text, reply_markup=INLINE_SELECT, disable_web_page_preview=True)
    

@bot.on_message(filters.photo & filters.private)
async def photo_upload(bot, message):
    msg = await message.reply("Uploading", quote=True)
    download_path = await bot.download_media(
        message=message, file_name="image/jetg"
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
            "File must be less than 5mb, please try another file or <a href=https://t.me/deathchatting_world>LEARN THIS BOT FIRST!</a>",
            disable_web_page_preview=True, reply_markup=ERROR_BUTTON)
    else:
        t = await msg.edit_text(generated_link, disable_web_page_preview=True)
        await t.edit_text(
            f"Link - `{generated_link} `\n\n<a href=https://t.me/deathchatting_world>Feel free to leave a feedback</a>\n\n Join - @DeathxBotz",
            reply_markup=IN_BUTTON,
            disable_web_page_preview=True)
    finally:
        os.remove(download_path)


## UPLOAD VIDEOS

@bot.on_message(filters.video & filters.private)
async def video_upload(bot, message):
    msg = await message.reply("Your file is been uploading...", quote=True)
    download_path = await bot.download_media(message=message, file_name="image/jetg")
    try:
        link = upload_file(download_path)
        generated_Link = "https://telegra.ph" + "".join(link)

        IN_BUTTON = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("ᴍᴏʀᴇ 🥀", url="https://t.me/TryToLiveAlon"),
                    InlineKeyboardButton("ʀᴇᴘᴏʀᴛ ʙᴜɢs 🤖", url="https://t.me/deathchatting_world")
                ],
                [
                    InlineKeyboardButton("ᴡᴇʙ ᴘʀᴇᴠɪᴇᴡ 🌐", url=generated_Link)
                ]
            ]
        )
    except:
        await msg.edit_text(
            "File must be less than 5mb, please try another file or <a href=https://t.me/deathchatting_world>LEARN THIS BOT FIRST!</a>",
            disable_web_page_preview=True, reply_markup=ERROR_BUTTON)
    else:
        t = await msg.edit_text(generated_Link, disable_web_page_preview=True)
        await t.edit_text(
            f"Link - `{generated_Link} `\n\n<a href=https://t.me/deathchatting_world>Feel free to leave a feedback</a>\n\n Join - @DeathxBotz",
            reply_markup=IN_BUTTON,
            disable_web_page_preview=True)
    finally:
        os.remove(download_path)


## UPLOAD GIF

@bot.on_message(filters.animation & filters.private)
async def animation_upload(bot, message):
    msg = await message.reply("Your file is been uploading...", quote=True)
    download_path = await bot.download_media(message=message, file_name="gif/jetg")
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
            "File must be less than 5mb, please try another file or <a href=https://t.me/deathchatting_world>LEARN THIS BOT FIRST!</a>",
            reply_markup=INLINE_SELECT,
            disable_web_page_preview=True)
    else:
        t = await msg.edit_text(generated_link, disable_web_page_preview=True)
        await t.edit_text(
            f"Link - `{generated_link} `\n\n<a href=https://t.me/deathchatting_world>Feel free to leave a feedback</a>\n\n Join - @DeathxBotz",
            reply_markup=IN_BUTTON,
            disable_web_page_preview=True)
    finally:
        os.remove(download_path)


##UPLOAD ANIMATIONS TO THE TELEGRAPH IN GROUPS

@bot.on_message(filters.group & filters.animation)
async def animation_upload_groups(bot, message):
    msg = await message.reply("Your file is been uploading...", quote=True)
    download_path = await bot.download_media(message=message, file_name="gif/jetg")
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
            "File must be less than 5mb, please try another file or <a href=https://t.me/deathchatting_world>LEARN THIS BOT FIRST!</a>",
            reply_markup=INLINE_SELECT,
            disable_web_page_preview=True)
    else:
        t = await msg.edit_text(generated_link, disable_web_page_preview=True)
        await t.edit_text(
            f"Link - `{generated_link} `\n\n<a href=https://t.me/deathchatting_world>Feel free to leave a feedback</a>\n\n Join - @DeathxBotz",
            reply_markup=IN_BUTTON,
            disable_web_page_preview=True)
    finally:
        os.remove(download_path)


## UPLOAD PHOTOS TO TELEGRAPH IN GROUPS

@bot.on_message(filters.group & filters.photo)
async def photo_upload_groups(bot, message):
    msg = await message.reply("Your file is been uploading...", quote=True)
    download_path = await bot.download_media(message=message, file_name="gif/jetg")
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
            "File must be less than 5mb, please try another file or <a href=https://t.me/deathchatting_world>LEARN THIS BOT FIRST!</a>",
            reply_markup=INLINE_SELECT,
            disable_web_page_preview=True)
    else:
        t = await msg.edit_text(generated_link, disable_web_page_preview=True)
        await t.edit_text(
            f"Link - `{generated_link} `\n\n<a href=https://t.me/deathchatting_world>Feel free to leave a feedback</a>\n\n Join - @DeathxBotz",
            reply_markup=IN_BUTTON,
            disable_web_page_preview=True)
    finally:
        os.remove(download_path)


## VIDEO UPLOAD TO THE TELEGRAPH IN GROUPS

@bot.on_message(filters.group & filters.video)
async def video_upload_group(bot, message):
    msg = await message.reply("Your file is been uploading...", quote=True)
    download_path = await bot.download_media(message=message, file_name="gif/jetg")
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
            "File must be less than 5mb, please try another file or <a href=https://t.me/deathchatting_world>LEARN THIS BOT FIRST!</a>",
            reply_markup=INLINE_SELECT,
            disable_web_page_preview=True)
    else:
        t = await msg.edit_text(generated_link, disable_web_page_preview=True)
        await t.edit_text(
            f"Link - `{generated_link} `\n\n<a href=https://t.me/deathchatting_world>Feel free to leave a feedback</a>\n\n Join - @DeathxBotz",
            reply_markup=IN_BUTTON,
            disable_web_page_preview=True)
    finally:
        os.remove(download_path)


## STICKER UPLOAD


@bot.on_message(filters.sticker)
async def sticker_upload(bot, message):
    msg = await message.reply("Your file is been uploading...", quote=True)
    download_path = await bot.download_media(message=message, file_name="gif/jetg")
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
    except Exception as a:
        await msg.edit_text(
            f"❌ This sticker was unable to upload. Please try another file or <a href=https://t.me/deathchatting_world>LEARN THIS BOT FIRST!</a>\n\n<i>Caused error - {a}</i>",
            reply_markup=INLINE_SELECT,
            disable_web_page_preview=True)
    else:
        t = await msg.edit_text(generated_link, disable_web_page_preview=True)
        await t.edit_text(
            f"Link - `{generated_link} `\n\n<a href=https://t.me/deathchatting_world>Feel free to leave a feedback</a>\n\n Join - @DeathxBotz",
            reply_markup=IN_BUTTON,
            disable_web_page_preview=True)
    finally:
        os.remove(download_path)


## UPLOAD STICKERS TO TELEGRAPH IN GROUPS

@bot.on_message(filters.group & filters.sticker)
async def sticker_upload_group(bot, message):
    msg = await message.reply("Your file is been uploading...", quote=True)
    download_path = await bot.download_media(message=message, file_name="gif/jetg")
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
    except Exception as a:
        await msg.edit_text(
            f"❌ This sticker was unable to upload. Please try another file or <a href=https://t.me/deathchatting_world>LEARN THIS BOT FIRST!</a>\n\n<i>Caused error - {a}</i>",
            reply_markup=INLINE_SELECT,
            disable_web_page_preview=True)
    else:
        t = await msg.edit_text(generated_link, disable_web_page_preview=True)
        await t.edit_text(
            f"Link - `{generated_link} `\n\n<a href=https://t.me/deathchatting_world>Feel free to leave a feedback</a>\n\n Join - @DeathxBotz",
            reply_markup=IN_BUTTON,
            disable_web_page_preview=True)
    finally:
        os.remove(download_path)

@bot.on_message(filters.private & filters.command("broadcast") & filters.user(Config.ADMIN))
async def broadcast_message(bot, message):
    if len(message.text.split()) > 1:
        broadcast_text = " ".join(message.text.split()[1:])
        async for dialog in bot.iter_dialogs():
            if dialog.chat.type == "private":
                try:
                    await bot.send_message(dialog.chat.id, broadcast_text)
                except Exception as e:
                    print(f"Failed to send broadcast to {dialog.chat.id}: {e}")
        await message.reply("Broadcast completed successfully!")
    else:
        await message.reply("Please provide a message to broadcast!")
        

print("All good")

bot.run()
