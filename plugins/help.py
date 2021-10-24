from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Saat ini hanya Mendukung Unduhan SINGLE atau BUKAN PLAYLIST, Kirimkan Link Video YouTube yang Ingin Diunduh."
    await message.reply_text(helptxt)
