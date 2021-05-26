from telebot import types
import requests

# Main menu
main_menu = types.InlineKeyboardMarkup(row_width=3)
main_menu.add(
    types.InlineKeyboardButton(text='Каталог', callback_data='catalog'),
    types.InlineKeyboardButton(text='Профиль', callback_data='profile'),
    types.InlineKeyboardButton(text='BTC', callback_data='btc'),
    types.InlineKeyboardButton(text='Информация', callback_data='info'),
    types.InlineKeyboardButton(text='Пополнить баланс', callback_data='replenish_balance'),
)


btc_request = requests.get("https://api.coinbase.com/v2/prices/BTC-USD/spot")
btc_data = btc_request.json()
btc_price = btc_data["data"]["amount"]

btc_menu = types.InlineKeyboardMarkup(row_width=2)
btc_menu.add(types.InlineKeyboardButton(text='Курс Bitcoin', callback_data='Bitcoin'))
btc_menu.add(types.InlineKeyboardButton(text='Курс Litecoin', callback_data='Litecoin'))
btc_menu.add(types.InlineKeyboardButton(text='Курс Ethereum', callback_data='Ethereum'))
btc_menu.add(types.InlineKeyboardButton(text='Курс Ethereum Classic', callback_data='Classic'))
btc_menu.add(types.InlineKeyboardButton(text='Курс Zcash', callback_data='Zcash'))
btc_menu.add(types.InlineKeyboardButton(text='Курс Dash', callback_data='Dash'))
btc_menu.add(types.InlineKeyboardButton(text='Курс Ripple', callback_data='Ripple'))
btc_menu.add(types.InlineKeyboardButton(text='Курс Monero', callback_data='Monero'))
btc_menu.add(types.InlineKeyboardButton(text='Назад', callback_data='exit_to_menu'))
    #coin_response = coins_switcher.get(call.data)
    #if coin_response:
    #    bot.send_message(call.message.chat.id, coin_response)
    #stock_response = stocks_switcher.get(call.data)
    #if stock_response:
       # bot.send_message(call.message.chat.id, stock_response)
    
    

        
# Admin menu
admin_menu = types.InlineKeyboardMarkup(row_width=2)
admin_menu.add(types.InlineKeyboardButton(text='Управление каталогом', callback_data='catalog_control'))
admin_menu.add(types.InlineKeyboardButton(text='Управление товаром', callback_data='section_control'))
admin_menu.add(types.InlineKeyboardButton(text='Изменить баланс', callback_data='give_balance'))
admin_menu.add(types.InlineKeyboardButton(text='Рассылка', callback_data='admin_sending_messages'))
admin_menu.add(types.InlineKeyboardButton(text='Изменить цену товара', callback_data='edit_price'))
admin_menu.add(types.InlineKeyboardButton(text='Вкл/выкл адрес доставки', callback_data='admin_address'))
admin_menu.add(
    types.InlineKeyboardButton(text='Информация', callback_data='admin_info'),
    types.InlineKeyboardButton(text='Выйти', callback_data='exit_admin_menu')
)

# Admin control
admin_menu_control_catalog = types.InlineKeyboardMarkup(row_width=1)
admin_menu_control_catalog.add(
    types.InlineKeyboardButton(text='Добавить раздел в каталог', callback_data='add_section_to_catalog'),
    types.InlineKeyboardButton(text='Удалить раздел из каталога', callback_data='del_section_to_catalog'),
    types.InlineKeyboardButton(text='Назад', callback_data='back_to_admin_menu')
)

# Admin control section
admin_menu_control_section = types.InlineKeyboardMarkup(row_width=1)
admin_menu_control_section.add(
    types.InlineKeyboardButton(text='Добавить товар в раздел', callback_data='add_product_to_section'),
    types.InlineKeyboardButton(text='Удалить товар из раздела', callback_data='del_product_to_section'),
    types.InlineKeyboardButton(text='Загрузить товар', callback_data='download_product'),
    types.InlineKeyboardButton(text='Назад', callback_data='back_to_admin_menu')
)

# Back to admin menu
back_to_admin_menu = types.InlineKeyboardMarkup(row_width=1)
back_to_admin_menu.add(
    types.InlineKeyboardButton(text='Вернуться в админ меню', callback_data='back_to_admin_menu')
)

btn_purchase = types.InlineKeyboardMarkup(row_width=2)
btn_purchase.add(
    types.InlineKeyboardButton(text='Купить', callback_data='buy'),
    types.InlineKeyboardButton(text='Выйти', callback_data='exit_to_menu')
)

btn_ok = types.InlineKeyboardMarkup(row_width=3)
btn_ok.add(
    types.InlineKeyboardButton(text='Понял', callback_data='btn_ok')
)

replenish_balance = types.InlineKeyboardMarkup(row_width=3)
replenish_balance.add(
    types.InlineKeyboardButton(text='🔄 Проверить', callback_data='check_payment'),
    types.InlineKeyboardButton(text='❌ Отменить', callback_data='cancel_payment')
)

to_close = types.InlineKeyboardMarkup(row_width=3)
to_close.add(
    types.InlineKeyboardButton(text='❌', callback_data='to_close')
)

markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
markup.add('Yes', 'No', '/admin')

# cities

cities = types.InlineKeyboardMarkup(row_width=3)
cities.add(
    types.InlineKeyboardButton(text='🇷🇺 Россия', callback_data='ru'),
    types.InlineKeyboardButton(text='🇺🇦 Украина', callback_data='ua'),
)
