from XDX.queues import QUEUE
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    OWNER_NAME,
)







@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\nÂ» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("ð¡ only admin with manage voice chats permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"âï¸ **settings of** {query.message.chat.title}\n\nÂ°ââ : pause stream\nÂ°â : skip stream\nÂ°â : resume stream\nð : mute userbot\nð : unmute userbot\nÂ°â» : stop stream",
              reply_markup=InlineKeyboardMarkup(
                  [[
                      InlineKeyboardButton("Â°â»", callback_data="cbstop"),
                      InlineKeyboardButton("Â°ââ", callback_data="cbpause"),
                      InlineKeyboardButton("Â°â", callback_data="cbskip"),
                      InlineKeyboardButton("Â°â", callback_data="cbresume"),
                  ],[
                      InlineKeyboardButton("Â°ð", callback_data="cbmute"),
                      InlineKeyboardButton("Â°ð", callback_data="cbunmute"),
                  ],[
                      InlineKeyboardButton("â CÊá´ê±á´", callback_data="cls")],
                  ]
             ),
         )
    else:
        await query.answer("â nothing is currently streaming", show_alert=True)
        
        
#start



@Client.on_callback_query(filters.regex("cb_start"))
async def cb_start(_, query: CallbackQuery):
    await query.edit_message_text(
       f"""Êá´ÊÊá´ [â¨](https://telegra.ph//file/08f70fa9464a522ef465d.jpg) **á´¡á´Êá´á´á´á´ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
 **ââââã [ð«ð'ððð ððð¬](https://t.me/XCodeSupport) ãââââ**
 ** âââââââââââââ 
 **Éª á´á´É´ á´Êá´Ê á´ Éªá´á´á´ & á´á´ê±Éªá´ ÉªÉ´ É¢Êá´á´á´ á´ Éªá´á´á´ á´á´ÊÊ !!**
 ** âââââââââââââ
 â£ Managed By - [S U P P O R T](https://t.me/XCodeSupport) â¥ï¸
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "â Aá´á´ á´á´ ÉªÉ´ Êá´á´Ê GÊá´á´á´",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton(
                    "Â°Cá´á´á´á´É´á´s", callback_data="cb_cmd"),],
                [
                    InlineKeyboardButton("Â°Oá´¡É´á´Ê", url=f"https://t.me/{OWNER_NAME}"),
                    InlineKeyboardButton("Â°Dá´á´ á´Êá´á´á´Ê ", url=f"https://Badnam-xd.github.io/"),
                ],
                [
                    InlineKeyboardButton(
                        "â¢ Sá´á´Êá´á´ â¢", url="https://t.me/XCodeSupport"
                    )
                ],
            ]
        ),
    )

    
    
    
    #Help command
    
    
@Client.on_callback_query(filters.regex("cb_cmd"))
async def cb_cmd(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""â¨ **Hello !**
Â» **Òá´Ê á´É´Ê Êá´Êá´ á´É´á´ á´á´á´á´á´É´á´ á´ÊÉªá´á´ Êá´á´á´á´É´s ð­ !**
â¡ Powered by [O W N E R](https://t.me/{OWNER_NAME})""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("â¢ Má´ê±Éªá´ Cá´á´á´á´É´á´ê±", callback_data="cb_basic"),
                    InlineKeyboardButton("Â°Sá´á´á´ á´ê±á´Ê â¢", callback_data="cb_advance"),
                ],
                [InlineKeyboardButton("Â°Sá´á´x", callback_data="cb_fun")],
               
                [InlineKeyboardButton("â Bá´á´á´", callback_data="cb_start")],
            ]
        ),
    )
    
@Client.on_callback_query(filters.regex("cb_basic"))
async def cb_basic(_, query: CallbackQuery):
    await query.edit_message_text(  
        f"""ðð¦ðªð­ð©ð¢...â­ð¬ðªðªðð«ð¡ð°..
        
        
â¢  `/play (song name)` 
â¢  `/vplay (song name)` 
â¢  `/vstream (song name)` 
â¢  `/skip` - skip the current song
â¢  `/end` - stop music play
â¢  `/pause` - pause song play
â¢  `/resume` - resume song play
â¢  `/mute` - mute assistant in vc
â¢  `/lyrics (song name)`

â Powered By [O W N E R](https://t.me/{OWNER_NAME}) .""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("â Bá´á´á´", callback_data="cb_cmd")]]
        ),
    )
    
    
@Client.on_callback_query(filters.regex("cb_advance"))
async def cb_advance(_, query: CallbackQuery):
    await query.edit_message_text(    
      f"""ððµð±ð¯ð... â­ð¬ðªðªðð«ð¡ð°.
â¢ `/ping` pong !!
â¢ `/start` - Alive msg ~group 
â¢ `/id` - Find out your grp and your id // stickers id also
â¢ `/uptime` - ð»
â¢ `/rmd` clean all downloads
â¢ `/clean` - clear storage 

â Powered By [O W N E R](https://t.me/{OWNER_NAME}) .""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("â Bá´á´á´", callback_data="cb_cmd")]]
        ),
    )
    
    
@Client.on_callback_query(filters.regex("cb_fun"))
async def cb_fun(_, query: CallbackQuery):
    await query.edit_message_text(  
        f"""ðð¢ðµ.. â­ð¬ðªðªðð«ð¡..
â¢ `/truth` ð
â¢ `/dare` ð 
â¢ `/XDX` ð   
â¢ `/tpatp` ð  
â¢ `/OSM` ð  

â Powered By [O W N E R](https://t.me/{OWNER_NAME}) .""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("â Bá´á´á´", callback_data="cb_cmd")]]
        ),
    )
        

    
    
    
        


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("ð¤­ðÉ´Éªá´á´Ê Êsá´á´ á´á´ á´á´á´ÉªÉ´ É´á´ÊÉª Êá´Éª É¢Êá´ á´á´ !", show_alert=True)
    await query.message.delete()
