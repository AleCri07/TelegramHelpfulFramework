#Copyright (C) 2021 AleCri07 
#PROGRAM COME WITH ABSOLUTELY NO WARRANTY! See GNU Lesser General Public License for more details.
#Everyone is permitted to copy and distribute verbatim copies of this license document, but changing it is not allowed.



#!/usr/bin/python3


import EzTG


def callback(bot, update):
    # Questo è il bot
    if 'message' in update:
        # Gestore dei messaggi 
        message_id = update['message']['message_id']  # https://core.telegram.org/bots/api#message
        user_id = update['message']['from']['id']
        chat_id = update['message']['chat']['id']
        text = update['message']['text']

        if text == '/start':
            bot.sendMessage(chat_id=chat_id, text='EzTGPy example bot\n\nCommands:\n/inline\n/keyboard\n/hidekb\n\nYour id: %s\nChat id: %s\nMessage id: %s' %
                            (user_id, chat_id, message_id))  # per i parametri vai a https://core.telegram.org/bots/api#sendmessage

        if text == '/inline':
            keyboard = EzTG.Keyboard('inline')
            keyboard.add('Example', 'callback data')
            keyboard.add('Example 2', 'callback data 2')
            keyboard.newLine()
            keyboard.add('Example 3', 'https://google.it')
            bot.sendMessage(chat_id=chat_id, text='Test',
                            reply_markup=keyboard)

        if text == '/keyboard':
            keyboard = EzTG.Keyboard('keyboard')
            keyboard.add('Example 1')
            keyboard.add('Example 2')
            keyboard.newLine()
            keyboard.add('Example 3')
            bot.sendMessage(chat_id=chat_id, text='Test',
                            reply_markup=keyboard)

        if text == '/hidekb':
            keyboard = EzTG.Keyboard('remove')
            bot.sendMessage(chat_id=chat_id,
                            text='Adios keyboard', reply_markup=keyboard)
    if 'callback_query' in update:
        # callback query "handler"
        message_id = update['callback_query']['message']['message_id']
        user_id = update['callback_query']['from']['id']
        chat_id = update['callback_query']['message']['chat']['id']
        cb_id = update['callback_query']['id']
        cb_data = update['callback_query']['data']

        if cb_data == 'callback data':
            bot.answerCallbackQuery(callback_query_id=cb_id, text='example #1')  # per i "Method parameters" vai a: https://core.telegram.org/bots/api#answercallbackquery
            keyboard = EzTG.Keyboard('inline')
            keyboard.add('Example 2', 'callback data 2')
            bot.editMessageText(chat_id=chat_id, message_id=message_id,
                                text='New message', reply_markup=keyboard)  # per i "Method parameters" vai a: https://core.telegram.org/bots/api#editmessagetext

        if cb_data == 'callback data 2':
            bot.answerCallbackQuery(
                callback_query_id=cb_id, text='example #2 [alert]', show_alert=True)
            bot.editMessageText(chat_id=chat_id, message_id=message_id,
                                text='New message 2', reply_markup={})


bot = EzTG.EzTG(token='token del bot',
                callback=callback)
