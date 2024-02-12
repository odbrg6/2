#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# ┌──────────────────────────────────────┐
# │                                   │
# │   > installing guide :               │
# │      $ pip install pyrogram==2.0.41  │
# │      $ pip install asyncio           │
# └──────────────────────────────────────┘
# ملف تم تنشره هادی تنشر اذکر حقوق @w_1_4

import os, random, asyncio, time
from pyrogram import Client, filters, errors
from pyrogram.raw import functions, types
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


#           ---         ---         ---         #
api_id = 11328976 # main api id from my.telegram.org/apps
api_hash = '2ce8a12865422ee9fa352d513151b103' # main api hash from my.telegram.org/apps
bot_token = '6792702663:AAH5c62_IuusASCRGJ8KBX-G4IZhe0qns7w' # main bot token from @botFather
bot_admins = [6024124201, 00] # admin ايدي
#           ---         ---         ---         #
sleeping = 2 # main sleep time in sec ***[DO NOT EDIT]***
step = None # current step ***[DO NOT EDIT]***
tempClient = dict() # temporary client holder ***[DO NOT EDIT]***
isWorking = list() # Temporary Active Eval Names ***[DO NOT EDIT]***
#           ---         ---         ---         #


if not os.path.isdir('sessions') :
    os.mkdir('sessions')


if not os.path.isfile('app.txt') :
    with open('app.txt', 'w', encoding='utf-8') as file:
        file.write(str(api_id) + ' ' + api_hash)


async def randomString() -> str:
    '''Return a random string'''
    size = random.randint(4, 8)
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVLXYZ') for _ in range(size))


async def randomAPP():
    with open('app.txt', 'r', encoding='utf-8') as file:
        file = file.read().split('\n')
        app_id, app_hash = random.choice(file).split()
    return app_id, app_hash


async def accountList() :
    return [myFile.split('.')[0] for myFile in os.listdir('sessions') if os.path.isfile(os.path.join('sessions', myFile))]


async def remainTime(TS):
    TS = time.time() - TS
    if TS < 60 :
        return str(int(TS)) + ' ثانیه'
    else :
        min = int(TS/60)
        sec = TS%60
        return str(int(min)) + ' دقیقه و ' + str(int(sec)) + ' ثانیه'


bot = Client(
    "LampStack",
    bot_token = bot_token,
    api_id = api_id,
    api_hash = api_hash
)


try :
    os.system("clear")
except :
    os.system("cls")
print('Bot is Running ...')


#           StartCommand            #
@bot.on_message(filters.command(['start', 'cancel']) & filters.private & filters.user(bot_admins))
async def StartResponse(client, message):
    global step, tempClient, isWorking
    try:
        tempClient['client'].disconnect()
    except:
        pass
    tempClient = {}
    step = None
    my_keyboard = [
        [InlineKeyboardButton('-إضِافَة حَسَآب.', callback_data='addAccount'), InlineKeyboardButton('-مَسَح حِسَاب.', callback_data='removeAccount')],
        [InlineKeyboardButton('-انضَم لِـ قنَاة.', callback_data='joinEval'), InlineKeyboardButton('-مُغَادَرَة قَنَاة.', callback_data='leftEval')],
        [InlineKeyboardButton('-مُشَاهدَات مَنشُور.', callback_data='viewEval'), InlineKeyboardButton('-تَفَاعُلَات.', callback_data='reActionEval')],
        [InlineKeyboardButton('-تَصوِيت استِفتَاء.', callback_data='voteEval'), InlineKeyboardButton('-ابلَاغ مَنشُور.', callback_data='reportPostPublic')],
        [InlineKeyboardButton('-بلُوك.', callback_data='blockEval')],
        [InlineKeyboardButton('-عَدَد الحِسَابَات.', callback_data='accountsList'), InlineKeyboardButton('-فَحِص.', callback_data='checkAccounts')],
        [InlineKeyboardButton('-عَدَد الثوَانِي.', callback_data='setTime'), InlineKeyboardButton('-الغَاء الطَلبَات.', callback_data='endAllEvals')],
    ]
    await message.reply('<b>>مرحبا بك في بوت بيدو للرشق:</b>', reply_markup=InlineKeyboardMarkup(my_keyboard), quote=True)

#           StopEval            #
@bot.on_message(filters.regex('^/stop_\w+') & filters.private & filters.user(bot_admins))
async def StopEval(client, message):
    global step, isWorking
    my_keyboard = [
        [InlineKeyboardButton('🔙', callback_data='backToMenu')],
    ]
    evalID = message.text.replace('/stop_', '')
    if evalID in isWorking:
        isWorking.remove(evalID)
        await message.reply(f'<b>اكتملت العملية بالمعرف {evalID} بنجاح</b>', reply_markup=InlineKeyboardMarkup(my_keyboard), quote=True)
    else:
        await message.reply(f'<b>لم يتم العثور على العملية المطلوبة!</b>', reply_markup=InlineKeyboardMarkup(my_keyboard), quote=True)



#           callback query            #
@bot.on_callback_query()
async def callbackQueries(client, query):
    global step, bot_admins, tempClient, isWorking, sleeping
    chat_id = query.message.chat.id
    message_id = query.message.id
    data = query.data
    query_id = query.id
    if chat_id in bot_admins:
        if data == 'backToMenu':
            try:
                tempClient['client'].disconnect()
            except:
                pass
            tempClient = {}
            step = None
            my_keyboard = [
        [InlineKeyboardButton('-إضِافَة حَسَآب.', callback_data='addAccount'), InlineKeyboardButton('-مَسَح حِسَاب.', callback_data='removeAccount')],
        [InlineKeyboardButton('-انضَم لِـ قنَاة.', callback_data='joinEval'), InlineKeyboardButton('-مُغَادَرَة قَنَاة.', callback_data='leftEval')],
        [InlineKeyboardButton('-مُشَاهدَات مَنشُور.', callback_data='viewEval'), InlineKeyboardButton('-تَفَاعُلَات.', callback_data='reActionEval')],
        [InlineKeyboardButton('-تَصوِيت استِفتَاء.', callback_data='voteEval'), InlineKeyboardButton('-ابلَاغ مَنشُور.', callback_data='reportPostPublic')],
        [InlineKeyboardButton('-بلُوك.', callback_data='blockEval')],
        [InlineKeyboardButton('-عَدَد الحِسَابَات.', callback_data='accountsList'), InlineKeyboardButton('-فَحِص.', callback_data='checkAccounts')],
        [InlineKeyboardButton('-عَدَد الثوَانِي.', callback_data='setTime'), InlineKeyboardButton('-الغَاء الطَلبَات.', callback_data='endAllEvals')],
            ]
            await bot.edit_message_text(chat_id, message_id, '<b>> مرحبا بك في بوت بيدو للرشق::</b>', reply_markup=InlineKeyboardMarkup(my_keyboard))

        elif data == 'endAllEvals':
            step = None
            evalsCount = len(isWorking)
            isWorking = list()
            await bot.invoke(functions.messages.SetBotCallbackAnswer(query_id=int(query_id), cache_time=1, alert=True, message=f'تمام {evalsCount} تم إيقاف العمليات النشطة بنجاح'))

        elif data == 'addAccount':
            step = 'getPhoneForLogin'
            my_keyboard = [
                [InlineKeyboardButton('🔙', callback_data='backToMenu')],
            ]
            await bot.edit_message_text(chat_id, message_id, '<b>- لإضافة حساب الرجاء إرسال الرقم المطلوب:</b>', reply_markup=InlineKeyboardMarkup(my_keyboard))
        
        elif data == 'removeAccount':
            step = 'removeAccount'
            my_keyboard = [
                [InlineKeyboardButton('🔙', callback_data='backToMenu')],
            ]
            await bot.edit_message_text(chat_id, message_id, '<b>- لحذف الحساب الرجاء ارسال الرقم المطلوب:</b>', reply_markup=InlineKeyboardMarkup(my_keyboard))

        elif data == 'accountsList':
            if os.path.isfile(f'./accounts.txt'):
                os.unlink(f'./accounts.txt')
            myLen = len((await accountList()))
            if myLen == 0 :
                await bot.invoke(functions.messages.SetBotCallbackAnswer(query_id=int(query_id), cache_time=1, alert=True, message='اکانتی یافت نشد !'))
            else:
                with open(f'./accounts.txt', 'w') as my_file:
                    my_file.write("\n".join(await accountList()))
                try:
                    await bot.send_document(chat_id, f'./accounts.txt', caption=f'عدد الخسابات : {myLen}')
                    os.unlink(f'./accounts.txt')
                except:
                    pass

        elif data == 'checkAccounts':
            if len(await accountList()) == 0 :
                await bot.invoke(functions.messages.SetBotCallbackAnswer(query_id=int(query_id), cache_time=1, alert=True, message='لم يتم العثور على حسابات ❗️'))
            else:
                evalID = await randomString()
                isWorking.append(evalID)
                deleted = 0
                error = 0
                free = 0
                cli = None
                TS = time.time()
                AllCount = len(await accountList())
                await bot.edit_message_text(chat_id, message_id, '<b>بدأت عملية فحص الحسابات...</b>')
                for session in ((await accountList())):
                    if evalID not in isWorking:
                        break
                    try:
                        await cli.disconnect()
                    except:
                        pass
                    await asyncio.sleep(sleeping)
                    try:
                        api_id2, api_hash2 = await randomAPP()
                        cli = Client(f'sessions/{session}', api_id2, api_hash2)
                        await cli.connect()
                        await cli.resolve_peer("@durov")
                        await cli.disconnect()
                    except (errors.SessionRevoked, errors.UserDeactivated, errors.AuthKeyUnregistered, errors.UserDeactivatedBan, errors.Unauthorized):
                        try:
                            await cli.disconnect()
                        except:
                            pass
                        os.unlink(f'sessions/{session}.session')
                        deleted += 1
                    except Exception as e:
                        try:
                            await cli.disconnect()
                        except:
                            pass
                        error += 1
                    else:
                        free += 1
                    finally:
                        spendTime = await remainTime(TS)
                        allChecked = deleted + free + error
                        await bot.edit_message_text(chat_id, message_id, f'''♻️عملية فحص حسابات الروبوت...

• إجمالي الحسابات: {AllCount}
الحسابات التي تم التحقق منها: {allChecked}
• حسابات سليمة: {free}
• الجلسات المتقطعة: {deleted}
• أخطاء غير معروفة: {error}
• الوقت المنقضي: {spendTime}

لإلغاء هذه العملية، استخدم الأمر (/stop_{evalID}).''')
                try:
                    isWorking.remove(evalID)
                except:
                    pass
                allChecked = deleted + free + error
                spendTime = await remainTime(TS)
                my_keyboard = [
                    [InlineKeyboardButton('🔙', callback_data='backToMenu')],
                ]
                await bot.send_message(chat_id, f'''عملیات بررسی اکانت ها با موفقیت به اتمام رسید ✅

• إجمالي الحسابات: {AllCount}
الحسابات التي تم التحقق منها: {allChecked}
• حسابات سليمة: {free}
• الجلسات المتقطعة: {deleted}
• أخطاء غير معروفة: {error}
• الوقت المنقضي: {spendTime}''', reply_markup=InlineKeyboardMarkup(my_keyboard))


        elif data == 'setTime':
            step = 'setTime'
            my_keyboard = [
                [InlineKeyboardButton('🔙', callback_data='backToMenu')],
            ]
            await bot.edit_message_text(chat_id, message_id, f'<b>الفاصل الزمني الحالي هو {sleeping} ثانية، إذا أردت تغيير الفاصل الزمني بين العمليات، أرسل الرقم الجديد:</b>', reply_markup=InlineKeyboardMarkup(my_keyboard))

        elif data == 'joinEval':
            if len(await accountList()) == 0 :
                await bot.invoke(functions.messages.SetBotCallbackAnswer(query_id=int(query_id), cache_time=1, alert=True, message='لم يتم العثور على حسابات ❗️'))
            else:
                step = 'joinAccounts'
                my_keyboard = [
                    [InlineKeyboardButton('🔙', callback_data='backToMenu')],
                ]
                await bot.edit_message_text(chat_id, message_id, '<b>ارسل المعرف او الرابط الخاص:</b>', reply_markup=InlineKeyboardMarkup(my_keyboard))

        elif data == 'leftEval':
            if len(await accountList()) == 0 :
                await bot.invoke(functions.messages.SetBotCallbackAnswer(query_id=int(query_id), cache_time=1, alert=True, message='لم يتم العثور على حسابات ❗️'))
            else:
                step = 'leaveAccounts'
                my_keyboard = [
                    [InlineKeyboardButton('🔙', callback_data='backToMenu')],
                ]
                await bot.edit_message_text(chat_id, message_id, '<b>-لطفا ارسل الرابط لمغادرة القناة :</b>', reply_markup=InlineKeyboardMarkup(my_keyboard))

        elif data == 'viewEval':
            if len(await accountList()) == 0 :
                await bot.invoke(functions.messages.SetBotCallbackAnswer(query_id=int(query_id), cache_time=1, alert=True, message='لم يتم العثور على حسابات ❗️'))
            else:
                step = 'sendViewToPost'
                my_keyboard = [
                    [InlineKeyboardButton('🔙', callback_data='backToMenu')],
                ]
                await bot.edit_message_text(chat_id, message_id, '<b>- ارسل رابط المنشور :</b>', reply_markup=InlineKeyboardMarkup(my_keyboard))

        elif data == 'reportPostPublic':
            step = 'reportPostPublic'
            my_keyboard = [
                    [InlineKeyboardButton('🔙', callback_data='backToMenu')],
                ]
            await bot.edit_message_text(chat_id, message_id, '<b>- ارسل رابط المنشور :</b>', reply_markup=InlineKeyboardMarkup(my_keyboard))

        elif data == 'reActionEval':
            step = 'reActionEval'
            my_keyboard = [
                    [InlineKeyboardButton('🔙', callback_data='backToMenu')],
                ]
            await bot.edit_message_text(chat_id, message_id, '<b> الرجاء إدخال رابط المنشور المطلوب في السطر الأول، في السطر الثاني ضع الرموز التعبيرية وافصل بينها بمسافة، والرقم المطلوب في السطر الثالث.:</b>', reply_markup=InlineKeyboardMarkup(my_keyboard))
        
        elif data == 'voteEval':
            step = 'voteEval'
            my_keyboard = [
                    [InlineKeyboardButton('🔙', callback_data='backToMenu')],
                ]
            await bot.edit_message_text(chat_id, message_id, '<b>ارسل رابط الاستفتاء بالسطر الاول ورقم الصف من 0 بالسطر الثاني:</b>', reply_markup=InlineKeyboardMarkup(my_keyboard))

        elif data == 'blockEval':
            step = 'blockEval'
            my_keyboard = [
                    [InlineKeyboardButton('🔙', callback_data='backToMenu')],
                ]
            await bot.edit_message_text(chat_id, message_id, '<b>يوزر  الشخص المطلوب مع @:</b>', reply_markup=InlineKeyboardMarkup(my_keyboard))


#           Text Response            #
@bot.on_message(filters.text & filters.private & filters.user(bot_admins))
async def TextResponse(client, message):
    global step, isWorking, tempClient, api_hash, api_id, sleeping
    chat_id = message.chat.id
    text = message.text
    my_keyboard = [
        [InlineKeyboardButton('🔙', callback_data='backToMenu')],
    ]

#                       Add Account                       #
    if step == 'getPhoneForLogin' and text.replace('+', '').replace(' ', '').replace('-', '').isdigit():
        phone_number = text.replace('+', '').replace(' ', '').replace('-', '')
        if os.path.isfile(f'sessions/{phone_number}.session'):
            await message.reply('<b>هذا الرقم متاح بالفعل في مجلد الجلسات الخاص بالخادم!</b>', reply_markup=InlineKeyboardMarkup(my_keyboard), quote=True)
        else:
            tempClient['number'] = phone_number
            tempClient['client'] = Client(f'sessions/{phone_number}', int(api_id), api_hash)
            await tempClient['client'].connect()
            try :
                tempClient['response'] = await tempClient['client'].send_code(phone_number)
            except (errors.BadRequest, errors.PhoneNumberBanned, errors.PhoneNumberFlood, errors.PhoneNumberInvalid):
                await message.reply('<b>خطأ حاول مره اخرى!</b>', reply_markup=InlineKeyboardMarkup(my_keyboard), quote=True)
            else:
                step = 'get5DigitsCode'
                await message.reply(f'<b>وصلك كود على هذا الرقم{phone_number} انسخ ال5 ارقام وارسلها✅</b>', reply_markup=InlineKeyboardMarkup(my_keyboard), quote=True)

    elif step == 'get5DigitsCode' and text.replace(' ', '').isdigit():
        telegram_code = text.replace(' ', '')
        try:
            await tempClient['client'].sign_in(tempClient['number'], tempClient['response'].phone_code_hash, telegram_code)
            await tempClient['client'].disconnect()
            tempClient = {}
            step = 'getPhoneForLogin'
            await message.reply('<b>تم تسجيل الحساب بنجاح ✅\nإذا كنت تريد إضافة رقم، أرسل الرقم المطلوب أو استخدم الأمر /cancel.</b>', reply_markup=InlineKeyboardMarkup(my_keyboard), quote=True)
        except errors.PhoneCodeExpired :
            await tempClient['client'].disconnect()
            tempClient = {}
            step = None
            await message.reply('<b>لقد انتهت صلاحية الرمز المرسل، يرجى /cancel العملية والمحاولة مرة أخرى.</b>', reply_markup=InlineKeyboardMarkup(my_keyboard), quote=True)
        except errors.PhoneCodeInvalid :
            await message.reply('<b>الرمز الذي تم إدخاله خاطئ أو منتهي الصلاحية، يرجى استخدام الأمر /cancel أو إرسال الرمز الصحيح.</b>', reply_markup=InlineKeyboardMarkup(my_keyboard), quote=True)
        except errors.BadRequest :
            await message.reply('<b>الرمز الذي تم إدخاله خاطئ أو منتهي الصلاحية، يرجى استخدام الأمر /cancel أو إرسال الرمز الصحيح.</b>', reply_markup=InlineKeyboardMarkup(my_keyboard), quote=True)
        except errors.AuthKeyUnregistered :
            await asyncio.sleep(3)
            name = await randomString()
            try:
                await tempClient['client'].sign_up(tempClient['number'], tempClient['response'].phone_code_hash, name)
            except Exception:
                pass
            await tempClient['client'].disconnect()
            tempClient = {}
            step = 'getPhoneForLogin'
            await message.reply('<b>تم تسجيل الحساب بنجاح ✅\nإذا كنت تريد إضافة رقم، أرسل الرقم المطلوب أو استخدم الأمر /cancel.</b>', reply_markup=InlineKeyboardMarkup(my_keyboard), quote=True)
        except errors.SessionPasswordNeeded:
            step = 'SessionPasswordNeeded'
            await message.reply('<b>ارسل التحقق بخطوتين:</b>', reply_markup=InlineKeyboardMarkup(my_keyboard), quote=True)

    elif step == 'SessionPasswordNeeded':
        twoFaPass = text
        try :
            await tempClient['client'].check_password(twoFaPass)
        except errors.BadRequest:
            await message.reply('<b>كلمة المرور التي تم إدخالها خاطئة، يرجى إرسالها مرة أخرى أو استخدام الأمر /cancel.</b>', reply_markup=InlineKeyboardMarkup(my_keyboard), quote=True)
        else:
            await tempClient['client'].disconnect()
            tempClient = {}
            step = 'getPhoneForLogin'
            await message.reply('<b>تم تسجيل الحساب بنجاح ✅\nإذا كنت تريد إضافة رقم، أرسل الرقم المطلوب أو استخدم الأمر /cancel.</b>', reply_markup=InlineKeyboardMarkup(my_keyboard), quote=True)

#                       Delete Account                       #
    if step == 'removeAccount':
        step = None
        phone_number = text.replace('+', '').replace(' ', '').replace('-', '')
        if not os.path.isfile(f'sessions/{phone_number}.session'):
            await message.reply('<b>لم يتم العثور على الرقم المطلوب على الخادم!</b>', reply_markup=InlineKeyboardMarkup(my_keyboard), quote=True)
        else:
            await bot.send_document(message.chat.id, f'sessions/{phone_number}.session', caption='<b>تم حذف الرقم المطلوب بنجاح وتم إرسال جلسة البيروجرام إلى للأرشفة.</b>', reply_markup=InlineKeyboardMarkup(my_keyboard))
            os.unlink(f'sessions/{phone_number}.session')

#                       set Time                       #
    if step == 'setTime':
        step = None
        sleeping = float(text)
        await message.reply('<b>تم ضبط الوقت الجديد بنجاح</b>', reply_markup=InlineKeyboardMarkup(my_keyboard), quote=True)

#                       join Accounts                       #
    if step == 'joinAccounts':
        step = None
        evalID = await randomString()
        isWorking.append(evalID)
        link = text.split()[0].replace('@', '').replace('+', 'joinchat/')
        allAcccounts = len((await accountList()))
        all = 0
        error = 0
        done = 0
        TS = time.time()
        msg = await message.reply('<b>بدأت عملية الانضمام...</b>')
        for session in ((await accountList())):
            if evalID not in isWorking:
                break
            all += 1
            await asyncio.sleep(sleeping)
            try:
                api_id2, api_hash2 = await randomAPP()
                cli = Client(f'sessions/{session}', api_id2, api_hash2)
                await cli.connect()
                await asyncio.sleep(0.2)
                await cli.join_chat(link)
                await asyncio.sleep(0.2)
                await cli.disconnect()
            except Exception as e:
                try:
                    await cli.disconnect()
                except:
                    pass
                error += 1
            else:
                done += 1
            finally:
                spendTime = await remainTime(TS)
                await bot.edit_message_text(chat_id, msg.id, f'''♻️عملية الانضمام...

• الحسابات التي تم التحقق منها: {all}/{allAcccounts}
ناجح: {done}
خطأ: {error}
• الوقت المنقضي: {spendTime}

لإلغاء هذه العملية، استخدم الأمر (/stop_{evalID}).''')
        try:
            isWorking.remove(evalID)
        except:
            pass
        spendTime = await remainTime(TS)
        await message.reply(f'''<b>عملية الانضمام...✅

• الحسابات التي تم التحقق منها: {all}/{allAcccounts}
ناجح: {done}
خطأ: {error}
• الوقت المنقضي: {spendTime}</b>''', reply_markup=InlineKeyboardMarkup(my_keyboard), quote=True)


#                       Leave Accounts                       #
    if step == 'leaveAccounts':
        step = None
        evalID = await randomString()
        isWorking.append(evalID)
        allAcccounts = len((await accountList()))
        all = 0
        error = 0
        done = 0
        TS = time.time()
        msg = await message.reply('<b>جاري الخروج...</b>', reply_markup=InlineKeyboardMarkup(my_keyboard), quote=True)
        for session in ((await accountList())):
            if evalID not in isWorking:
                break
            all += 1
            await asyncio.sleep(sleeping)
            try:
                api_id2, api_hash2 = await randomAPP()
                cli = Client(f'sessions/{session}', api_id2, api_hash2)
                await cli.connect()
                await asyncio.sleep(0.2)
                await cli.leave_chat(int(link), delete=True)
                await asyncio.sleep(0.2)
                await cli.disconnect()
            except Exception as e:
                try:
                    await cli.disconnect()
                except:
                    pass
                error += 1
            else:
                done += 1
            finally:
                spendTime = await remainTime(TS)
                await bot.edit_message_text(chat_id, msg.id, f'''♻️ عملیات المغادرة...

• الحسابات التي تحقق منها: {all}/{allAcccounts}
• ناجح : {done}
• خطا : {error}
• الوقت : {spendTime}

لإلغاء هذه العملية، استخدم الأمر (/stop_{evalID}).''')
        try:
            isWorking.remove(evalID)
        except:
            pass
        spendTime = await remainTime(TS)
        await message.reply(f'''<b> عملیات المغادرة...

• الحسابات التي تحقق منها: {all}/{allAcccounts}
• ناجح : {done}
• خطا : {error}
• الوقت : {spendTime}''', reply_markup=InlineKeyboardMarkup(my_keyboard), quote=True)

#                       send view                       #
    if step == 'sendViewToPost':
        step = None
        evalID = await randomString()
        isWorking.append(evalID)
        username = text.split('/')[3]
        msg_id = int(text.split('/')[4])
        allAcccounts = len((await accountList()))
        all = 0
        error = 0
        done = 0
        TS = time.time()
        msg = await message.reply('<b>بدأت عميلة ارسال المشاهدات...</b>', reply_markup=InlineKeyboardMarkup(my_keyboard), quote=True)
        for session in ((await accountList())):
            if evalID not in isWorking :
                break
            try:
                await cli.disconnect()
            except:
                pass
            all += 1
            await asyncio.sleep(sleeping)
            try:
                api_id2, api_hash2 = await randomAPP()
                cli = Client(f'sessions/{session}', api_id2, api_hash2)
                await cli.connect()
                await asyncio.sleep(0.2)
                await cli.invoke(functions.messages.GetMessagesViews(peer = await cli.resolve_peer(username), id=[msg_id], increment=True))
                await asyncio.sleep(0.2)
                await cli.disconnect()
            except Exception as e:
                try:
                    await cli.disconnect()
                except:
                    pass
                error += 1
            else:
                done += 1
            finally:
                spendTime = await remainTime(TS)
                await bot.edit_message_text(chat_id, msg.id, f'''♻️ عملية ارسال المشاهدات ...

• الحسابات التي تم التحقق منها: {all}/{allAcccounts}
ناجح: {done}
خطأ: {error}
• الوقت المنقضي: {spendTime}

لإلغاء هذه العملية، استخدم الأمر (/stop_{evalID}).''')
        try:
            isWorking.remove(evalID)
        except:
            pass
        spendTime = await remainTime(TS)
        await message.reply(f'''<b> عملية ارسال المشاهدات ...

• الحسابات التي تم التحقق منها: {all}/{allAcccounts}
ناجح: {done}
خطأ: {error}
• الوقت المنقضي: {spendTime}''', reply_markup=InlineKeyboardMarkup(my_keyboard), quote=True)


#                       send Public Post Roport                       #
    if step == 'reportPostPublic':
        step = None
        evalID = await randomString()
        isWorking.append(evalID)
        if text.split('/')[3] != 'c':
            peerID = '@' + text.split('/')[3]
            peerMessageID = int(text.split('/')[4])
        else:
            peerID = int('-100' + text.split('/')[4])
            peerMessageID = int(text.split('/')[5])
        allAcccounts = len((await accountList()))
        all = 0
        error = 0
        done = 0
        TS = time.time()
        if text.split('/')[3].isdigit():
            await message.reply('<b>الرابط الذي أرسلته لي مرتبط بدردشة خاصة ❗️</b>', reply_markup=InlineKeyboardMarkup(my_keyboard), quote=True)
        else:
            msg = await message.reply('<b>بدأت عملية الابلاغ...</b>', reply_markup=InlineKeyboardMarkup(my_keyboard), quote=True)
            for session in ((await accountList())):
                if evalID not in isWorking:
                    break
                try:
                    await cli.disconnect()
                except:
                    pass
                all += 1
                await asyncio.sleep(sleeping)
                try:
                    api_id2, api_hash2 = await randomAPP()
                    cli = Client(f'sessions/{session}', api_id2, api_hash2)
                    await cli.connect()
                    await asyncio.sleep(0.2)
                    await cli.invoke(functions.messages.Report(peer= await cli.resolve_peer(peerID), id=[peerMessageID], reason=types.InputReportReasonPornography(), message=''))
                    await asyncio.sleep(0.2)
                    await cli.disconnect()
                except Exception as e:
                    try:
                        await cli.disconnect()
                    except:
                        pass
                    error += 1
                else:
                    done += 1
                finally:
                    spendTime = await remainTime(TS)
                    await bot.edit_message_text(chat_id, msg.id, f'''♻️عملية الابلاغ  ...

• الحسابات التي تم التحقق منها: {all}/{allAcccounts}
ناجح: {done}
خطأ: {error}
• الوقت المنقضي: {spendTime}

لإلغاء هذه العملية، استخدم الأمر (/stop_{evalID}).''')
            try:
                isWorking.remove(evalID)
            except:
                pass
            spendTime = await remainTime(TS)
            await message.reply(f'''<b>♻️عملية الابلاغ  ...

• الحسابات التي تم التحقق منها: {all}/{allAcccounts}
ناجح: {done}
خطأ: {error}
• الوقت المنقضي: {spendTime}''', reply_markup=InlineKeyboardMarkup(my_keyboard), quote=True)

#                       send Post reAction                       #
    if step == 'reActionEval':
        step = None
        evalID = await randomString()
        isWorking.append(evalID)
        peerID = '@' + text.split("\n")[0].split('/')[3]
        peerMessageID = int(text.split("\n")[0].split('/')[4])
        emojies = text.split("\n")[1].split()
        countOfWork = int(text.split("\n")[2])
        allAcccounts = len((await accountList()))
        all = 0
        error = 0
        done = 0
        TS = time.time()
        if text.split("\n")[0].split('/')[3].isdigit():
            await message.reply('<b>القناة خاصة❗️</b>', reply_markup=InlineKeyboardMarkup(my_keyboard), quote=True)
        else:
            msg = await message.reply('<b>بدأت عملية التفاعل...</b>', reply_markup=InlineKeyboardMarkup(my_keyboard), quote=True)
            for session in ((await accountList())):
                if all >= countOfWork:
                    break
                if evalID not in isWorking:
                    break
                try:
                    await cli.disconnect()
                except:
                    pass
                all += 1
                await asyncio.sleep(sleeping)
                try:
                    api_id2, api_hash2 = await randomAPP()
                    cli = Client(f'sessions/{session}', api_id2, api_hash2)
                    await cli.connect()
                    await asyncio.sleep(0.2)
                    await cli.send_reaction(peerID, peerMessageID, random.choice(emojies))
                    await asyncio.sleep(0.2)
                    await cli.disconnect()
                except Exception as e:
                    try:
                        await cli.disconnect()
                    except:
                        pass
                    error += 1
                else:
                    done += 1
                finally:
                    spendTime = await remainTime(TS)
                    await bot.edit_message_text(chat_id, msg.id, f'''♻️ عملية التفاعل...
                                                
• الحسابات التي تم التحقق منها: {all}/{allAcccounts}
ناجح: {done}
خطأ: {error}
• الوقت المنقضي: {spendTime}

لإلغاء هذه العملية، استخدم الأمر (/stop_{evalID}).''')
            try:
                isWorking.remove(evalID)
            except:
                pass
            spendTime = await remainTime(TS)
            await message.reply(f'''<b>انتهت العملية✅</b>

• الحسابات التي تم التحقق منها: {all}/{allAcccounts}
ناجح: {done}
خطأ: {error}
• الوقت المنقضي: {spendTime}''', reply_markup=InlineKeyboardMarkup(my_keyboard), quote=True)

#                       send Post vote                       #
    if step == 'voteEval':
        step = None
        evalID = await randomString()
        isWorking.append(evalID)
        peerID = '@' + text.split("\n")[0].split('/')[3]
        peerMessageID = int(text.split("\n")[0].split('/')[4])
        opt = text.split("\n")[1]
        allAcccounts = len((await accountList()))
        all = 0
        error = 0
        done = 0
        TS = time.time()
        if not opt.isdigit():
            await message.reply('<b>الخيار الذي تم إدخاله غير صحيح❗️</b>', reply_markup=InlineKeyboardMarkup(my_keyboard), quote=True)
        else:
            msg = await message.reply('<b>جاري التصويت...</b>', reply_markup=InlineKeyboardMarkup(my_keyboard), quote=True)
            for session in ((await accountList())):
                if evalID not in isWorking:
                    break
                try:
                    await cli.disconnect()
                except:
                    pass
                all += 1
                await asyncio.sleep(sleeping)
                try:
                    api_id2, api_hash2 = await randomAPP()
                    cli = Client(f'sessions/{session}', api_id2, api_hash2)
                    await cli.connect()
                    await asyncio.sleep(0.2)
                    await cli.vote_poll(peerID, peerMessageID, int(opt))
                    await asyncio.sleep(0.2)
                    await cli.disconnect()
                except Exception as e:
                    try:
                        await cli.disconnect()
                    except:
                        pass
                    error += 1
                else:
                    done += 1
                finally:
                    spendTime = await remainTime(TS)
                    await bot.edit_message_text(chat_id, msg.id, f'''♻️ عملية إرسال الاستفتاء...

• الحسابات التي تم التحقق منها: {all}/{allAcccounts}
ناجح: {done}
خطأ: {error}
• الوقت المنقضي: {spendTime}

لإلغاء هذه العملية، استخدم الأمر (/stop_{evalID}).''')
            try:
                isWorking.remove(evalID)
            except:
                pass
            spendTime = await remainTime(TS)
            await message.reply(f'''<b> عملية إرسال الاستفتاء.✅</b>

• الحسابات التي تم التحقق منها: {all}/{allAcccounts}
ناجح: {done}
خطأ: {error}
• الوقت المنقضي: {spendTime}''', reply_markup=InlineKeyboardMarkup(my_keyboard), quote=True)


#                       block users                       #
    if step == 'blockEval':
        step = None
        evalID = await randomString()
        isWorking.append(evalID)
        peerID = text.replace('@', '')
        allAcccounts = len((await accountList()))
        all = 0
        error = 0
        done = 0
        TS = time.time()
        msg = await message.reply('<b>جاري الحظر...</b>', reply_markup=InlineKeyboardMarkup(my_keyboard), quote=True)
        for session in ((await accountList())):
            if evalID not in isWorking:
                break
            try:
                await cli.disconnect()
            except:
                pass
            all += 1
            await asyncio.sleep(sleeping)
            try:
                api_id2, api_hash2 = await randomAPP()
                cli = Client(f'sessions/{session}', api_id2, api_hash2)
                await cli.connect()
                await asyncio.sleep(0.2)
                await cli.block_user(peerID)
                await asyncio.sleep(0.2)
                await cli.disconnect()
            except Exception as e:
                try:
                    await cli.disconnect()
                except:
                    pass
                error += 1
            else:
                done += 1
            finally:
                spendTime = await remainTime(TS)
                await bot.edit_message_text(chat_id, msg.id, f'''♻️ الحظر...

• الحسابات التي تم التحقق منها: {all}/{allAcccounts}
ناجح: {done}
خطأ: {error}
• الوقت المنقضي: {spendTime}

لإلغاء هذه العملية، استخدم الأمر (/stop_{evalID}).''')
        try:
            isWorking.remove(evalID)
        except:
            pass
        spendTime = await remainTime(TS)
        await message.reply(f'''<b>انتهى ارسال الحظر✅</b>

• الحسابات التي تم التحقق منها: {all}/{allAcccounts}
ناجح: {done}
خطأ: {error}
• الوقت المنقضي: {spendTime}''', reply_markup=InlineKeyboardMarkup(my_keyboard), quote=True)

bot.run()
