from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Currently Bot Only supports Youtube Download. Just Send Youtube Url"
    await message.reply_text(helptxt)