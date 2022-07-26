import os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.tl.types import ChannelParticipantAdmin
from telethon.tl.types import ChannelParticipantCreator
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.errors import UserNotParticipantError

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = int(os.environ.get("APP_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("TOKEN")
client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)
spam_chats = []

@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  await event.reply(
    "__**𝗜'𝗠 𝗞𝗔𝗔𝗟 𝗠𝗘𝗡𝗧𝗜𝗢𝗡 𝗕𝗢𝗧**, 𝖨 𝖢𝖠𝖭 𝖬𝖤𝖭𝖳𝖨𝖮𝖭 𝖠𝖫𝖬𝖮𝖲𝖳 𝖠𝖫𝖫 𝖬𝖤𝖬𝖡𝖤𝖱𝖲 𝖨𝖭 𝖠 𝖦𝖱𝖮𝖴𝖯 𝖮𝖱 𝖢𝖧𝖠𝖭𝖭𝖤𝖫 👻\n𝖢𝖫𝖨𝖢𝖪 **/help** 𝖥𝖮𝖱 𝖬𝖮𝖱𝖤 𝖨𝖭𝖥𝖮𝖱𝖬𝖠𝖳𝖨𝖮𝖭__\n\n 𝖬𝖤𝖲𝖲𝖠𝖦𝖤 [𝗞𝗔𝗔𝗟](https://T.me/garw_mishra) 𝖨𝖥 𝖳𝖧𝖤𝖱𝖤 𝖨𝖲 𝖠𝖭𝖸 𝖣𝖮𝖴𝖡𝖳𝖲",
    link_preview=False,
    buttons=(
      [
        Button.url('😎𝗢𝗪𝗡𝗘𝗥😎', 'https://t.me/GARW_MISHRA'),
        Button.url(' 𝗦𝗢𝗨𝗥𝗖𝗘 𝗖𝗢𝗗𝗘💝', 'https://github.com/GARWMISHRA/KAALMENTION')
      ]
    )
  )

@client.on(events.NewMessage(pattern="^/help$"))
async def help(event):
  helptext = "**𝖧𝖤𝖫𝖯 𝖬𝖤𝖭𝖴 𝖮𝖥 𝖪𝖠𝖠𝖫 𝖬𝖤𝖭𝖳𝖨𝖮𝖭 𝖡𝖮𝖳**\n\n𝖢𝖮𝖬𝖬𝖠𝖭𝖣: /utag\n__𝖸𝖮𝖴 𝖢𝖠𝖭 𝖴𝖲𝖤 𝖳𝖧𝖨𝖲 𝖢𝖮𝖬𝖬𝖠𝖭𝖣 𝖶𝖨𝖳𝖧 𝖳𝖤𝖷𝖳 𝖶𝖧𝖠𝖳 𝖸𝖮𝖴 𝖶𝖠𝖭𝖳 𝖳𝖮 𝖬𝖤𝖭𝖳𝖨𝖮𝖭 𝖮𝖳𝖧𝖤𝖱𝖲.__\n`/utag Good Morning!`\n__𝖸𝖮𝖴 𝖢𝖠𝖭 𝖴𝖲𝖤 𝖳𝖧𝖨𝖲 𝖢𝖮𝖬𝖬𝖠𝖭𝖣 𝖠𝖲 𝖠 𝖱𝖤𝖯𝖫𝖸 𝖳𝖮 𝖠𝖭𝖸 𝖬𝖤𝖲𝖲𝖠𝖦𝖤. 𝖡𝖮𝖳 𝖶𝖨𝖫𝖫 𝖳𝖠𝖦 𝖴𝖲𝖤𝖱𝖲 𝖳𝖮 𝖳𝖧𝖠𝖳 𝖱𝖤𝖯𝖫𝖨𝖤𝖣 𝖬𝖤𝖲𝖲𝖠𝖦𝖤__.\n\n𝖬𝖤𝖲𝖲𝖠𝖦𝖤 [𝗞𝗔𝗔𝗟](https://T.me/garw_mishra) 𝖨𝖥 𝖳𝖧𝖤𝖱𝖤 𝖨𝖲 𝖠𝖭𝖸 𝖣𝖮𝖴𝖡𝖳𝖲"
  await event.reply(
    helptext,
    link_preview=False,
    buttons=(
      [
        Button.url('😎𝗢𝗪𝗡𝗘𝗥😎', 'https://t.me/GARW_MISHRA'),
        Button.url('𝗦𝗢𝗨𝗥𝗖𝗘 𝗖𝗢𝗗𝗘💝', 'https://github.com/GARWMISHRA/KAALMENTION')
      ]
    )
  )
  
@client.on(events.NewMessage(pattern="^/utag ?(.*)"))
async def Mentionall(event):
  chat_id = event.chat_id
  if event.is_private:
    return await event.respond("__𝖳𝖧𝖨𝖲 𝖢𝖮𝖬𝖬𝖠𝖭𝖣 𝖢𝖠𝖭 𝖡𝖤 𝖴𝖲𝖤 𝖨𝖭 𝖦𝖱𝖮𝖴𝖯𝖲 𝖠𝖭𝖣 𝖢𝖧𝖠𝖭𝖭𝖤𝖫𝖲!__")
  
  is_admin = False
  try:
    partici_ = await client(GetParticipantRequest(
      event.chat_id,
      event.sender_id
    ))
  except UserNotParticipantError:
    is_admin = False
  else:
    if (
      isinstance(
        partici_.participant,
        (
          ChannelParticipantAdmin,
          ChannelParticipantCreator
        )
      )
    ):
      is_admin = True
  if not is_admin:
    return await event.respond("__𝖮𝖭𝖫𝖸 𝖠𝖣𝖬𝖨𝖭𝖲 𝖢𝖠𝖭 𝖬𝖤𝖭𝖳𝖨𝖮𝖭 𝖠𝖫𝖫!__")
  
  if event.pattern_match.group(1) and event.is_reply:
    return await event.respond("__𝖦𝖨𝖵𝖤 𝖬𝖤 𝖠𝖭 𝖠𝖱𝖦𝖴𝖬𝖤𝖭𝖳!__")
  elif event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.is_reply:
    mode = "text_on_reply"
    msg = await event.get_reply_message()
    if msg == None:
        return await event.respond("__𝖨 𝖢𝖠𝖭'𝖳 𝖬𝖤𝖭𝖳𝖨𝖮𝖭 𝖬𝖤𝖬𝖡𝖤𝖱𝖲 𝖥𝖮𝖱 𝖮𝖫𝖣𝖤𝖱 𝖬𝖤𝖲𝖲𝖠𝖦𝖤𝖲! (𝖬𝖤𝖲𝖲𝖠𝖦𝖤𝖲 𝖶𝖧𝖨𝖢𝖧 𝖠𝖱𝖤 𝖲𝖤𝖭𝖳 𝖡𝖤𝖥𝖮𝖱𝖤 𝖨'𝖬 𝖠𝖣𝖣𝖤𝖣 𝖳𝖮 𝖦𝖱𝖮𝖴𝖯)__")
  else:
    return await event.respond("__𝖱𝖤𝖯𝖫𝖸 𝖳𝖮 𝖠 𝖬𝖤𝖲𝖲𝖠𝖦𝖤 𝖮𝖱 𝖦𝖨𝖵𝖤 𝖬𝖤 𝖲𝖮𝖬𝖤 𝖳𝖤𝖷𝖳 𝖳𝖮 𝖬𝖤𝖭𝖳𝖨𝖮𝖭 𝖮𝖳𝖧𝖤𝖱𝖲!__")
  
  spam_chats.append(chat_id)
  usrnum = 0
  usrtxt = ''
  async for usr in client.iter_participants(chat_id):
    if not chat_id in spam_chats:
      break
    usrnum += 1
    usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) "
    if usrnum == 5:
      if mode == "text_on_cmd":
        txt = f"{usrtxt}\n\n{msg}"
        await client.send_message(chat_id, txt)
      elif mode == "text_on_reply":
        await msg.reply(usrtxt)
      await asyncio.sleep(2)
      usrnum = 0
      usrtxt = ''
  try:
    spam_chats.remove(chat_id)
  except:
    pass

@client.on(events.NewMessage(pattern="^/cancel$"))
async def cancel_spam(event):
  if not event.chat_id in spam_chats:
    return await event.respond('__𝖳𝖧𝖤𝖱𝖤 𝖨𝖲 𝖭𝖮 𝖯𝖱𝖮𝖢𝖤𝖲𝖲 𝖮𝖭 𝖦𝖮𝖨𝖭𝖦...__')
  else:
    try:
      spam_chats.remove(event.chat_id)
    except:
      pass
    return await event.respond('__𝖪𝖠𝖠𝖫𝖬𝖤𝖭𝖳𝖨𝖮𝖭_𝖲𝖳𝖮𝖯𝖯𝖤𝖣.__')

print(">> 𝖪𝖠𝖠𝖫𝖬𝖤𝖭𝖳𝖨𝖮𝖭_𝖲𝖳𝖠𝖱𝖳𝖤𝖣 <<")
client.run_until_disconnected()
