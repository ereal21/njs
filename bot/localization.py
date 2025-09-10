LANGUAGES = {
    'en': {
        'hello': '👋 Hello, {user}!',
        'balance': '💰 Balance: {balance} EUR',
        'overpay': '💳 Send the exact amount. Overpayments will be credited.',
        'shop': '🛍 Shop',
        'profile': '👤 Profile',
        'top_up': '💸 Top Up',
        'channel': '📢 Channel',
        'price_list': '💲 Price List',
        'language': '🌐 Language',
        'admin_panel': '🎛 Admin Panel',
        'help': '❓ Help',
        'help_info': (
            'Use the main menu to work with the bot:\n'
            '🛍 Shop – browse categories and choose a product.\n'
            '   • Select an item and confirm to purchase it.\n'
            '👤 Profile – view your balance and purchased items.\n'
            '💸 Top Up – choose a payment method and follow the instructions to add funds.\n'
            '🌐 Language – switch the interface language.\n'
            '🎁 Purchased items – available in Profile after you buy something.\n'
            'If you need assistance, contact {helper}.'
        ),
        'admin_help_info': (
            'Admin panel functions:\n'
            '🛠 Assign assistants – manage assistant accounts.\n'
            '📦 View Stock – browse and delete available product stock.\n'
            '🏪 Parduotuvės valdymas – manage shop categories and items.\n'
            '👥 Vartotojų valdymas – manage user balances and roles.\n'
            '📢 Pranešimų siuntimas – send messages to all users.'
        ),
        'assistant_help_info': (
            'Assistant panel functions:\n'
            '🖼 Assign photos – attach photos to items.\n'
            'Use Back to menu to return.'
        ),
        'choose_language': 'Please choose a language',
        'invoice_message': (
            '🧾 <b>Payment Invoice Created</b>\n\n'
            '<b>Amount:</b> <code>{amount}</code> {currency}\n'
            '🏦 <b>Payment Address:</b>\n<code>{address}</code>\n\n'
            '⏳ <b>Expires At:</b> {expires_at} LT\n'
            '⚠️ <b>Payment must be completed within 15 minutes of invoice creation.</b>\n\n'
            '❗️ <b>Important:</b> Send <u>exactly</u> this amount of {currency}.\n\n'
            '✅ <b>Confirmation is automatic via webhook after network confirmation.</b>'
        ),
        'cancel': 'Cancel',
        'cancel_payment': '❌ Cancel Payment',
        'payment_successful': '✅ Payment confirmed. Balance increased by {amount}€',
        'back_home': 'Back Home',
        'invoice_cancelled': 'Payment failed/expired. Your items are no longer reserved.',
        'total_purchases': '📦 Total Purchases: {count}',
        'streak': '🔥 Streak: {days} days',
        'note': '⚠️ Note: No refunds. Please ensure you send the exact amount for payments, as underpayments will not be confirmed.',
        'rate_experience': '⭐ How was your overall experience?',
        'rate_service': 'How was your experience with the service?',
        'rate_product': 'What is your opinion on the product?',
        'ask_feedback_reason': 'Would you like to tell us why?',
        'feedback_reason': 'Please write your feedback:',
        'thanks_feedback': 'Thanks for your feedback!',
        'confirm_purchase': 'Confirm purchase of {item} for {price}€?',
        'purchase_button': 'Purchase',
        'apply_promo': 'Apply promo code',
        'promo_prompt': 'Send promo code:',
        'promo_invalid': '❌ Invalid or expired promo code',
        'promo_applied': '✅ Promo code applied. New price: {price}€',
        'yes': '✅ Yes',
        'no': '❌ No',
        'confirm': '✅ Confirm',
        'rerun': '🔄 Rerun',
        'assign_more': '✅ Photo assigned. Add another?',
        'purchased_items': '📦 Purchased items',
        'purchased_items': '🎁 Purchased items',
        'back_to_menu': '🔙 Back to menu',
        'users_tickets': '🎟️ User tickets:',
        'no_tickets': 'No tickets',
        'lottery_winner': '🎉 Winner: {username}\n🎟️ Tickets: {tickets}\n\n❗️ Confirming will reset all tickets.',
        'lottery_broadcast_prompt': 'Send message to all users?',
        'lottery_enter_message': '✉️ Enter message:',
        'lottery_finished': '✅ Lottery finished.',
        'no_winner': '❌ No winner',
        'tools': '🧰 Tools',
        'lottery': '🎟️ Lottery',
        'insufficient_rights': 'Insufficient rights',
        'use_balance_prompt': 'You have {balance}€. Use it to reduce the price?',
        'choose_crypto': 'Choose payment method:',
        'need_top_up': 'You need to top up {missing}€ to complete the purchase. Choose payment method:',
        'item_reserved': '🔒 Item reserved for you for 15 minutes.',
        'payment_cancelled': '✅ Payment cancelled. Reserved items have been released.',
        'top_up_completed': '✅ Top-up completed.',
        'lottery_ticket_awarded': '🎟️ You received a lottery ticket.',
        'lottery_tickets': '🎟️ <b>Lottery tickets</b> — <code>{tickets}</code>',
        'referral_link': '🤝 <b>Referral link</b> — <code>{link}</code>',
        'referrals': '👥 <b>Referrals</b> — {count}',
        'referral_earnings': '💰 <b>Referral earnings</b> — <code>{amount}</code> €',
        'referral_reward': '🎉 Your referral {user} purchased a product — you earned {amount}€!',
        'gift': '🎁 Gift',
        'gift_prompt': 'Who do you want to gift a product to?',
        'gift_user_not_found': '❌ User not found.',
        'gift_select_category': '🎁 Select a product to gift to {user}:',
        'gift_sent': '🎁 Gift sent to {user}!',
        'gift_received': '🎁 You received {item} from {user}!',

        'stock_notify': '📦 Stock alerts',
        'choose_product_notify': 'Select a product to get notified when restocked:',
        'no_out_of_stock': '✅ All products are currently in stock.',
        'stock_subscribed': '🔔 You will be notified when {item} is back in stock.',
        'stock_already_subscribed': 'ℹ️ You are already waiting for {item}.',
        'stock_back_in': '📦 {item} is back in stock!',
        'choose_subcategory': '🏘️ Choose a district:',
        'select_product': '🏪 Select a product',
        'games': '🎮 Games',
        'blackjack': '🃏 Blackjack',
        'coinflip': '🪙 Coinflip',
        'achievements': '🏆 Achievements',
        'quests': '🧩 Personalized quests',
        'quests_placeholder': '🔧 Quests are coming soon.',
        'blackjack': '🃏 Blackjack',
        'coinflip': '🪙 Coinflip',
        'find_game': '🔍 Find game',
        'create_game': '➕ Create game',
        'play_bot': '🤖 Play against bot',
        'choose_game': 'Choose a game',
        'choose_side': 'Choose side:',
        'enter_bet': 'Enter bet amount:',
        'heads': 'Heads',
        'tails': 'Tails',
        'not_enough_balance': '❌ Not enough balance',
        'win': 'You won {amount}€!',
        'lose': 'You lost {amount}€.',
        'back': '🔙 Back',
        'create': '✅ Create',
        'join': '✅ Join',
        'waiting_opponent': '⏳ Waiting for an opponent...',
        'no_games': '❌ No games available',
        'join_confirm': 'Join {user} for {bet}€ as {side}?',
        'create_confirm': 'Create game for {bet}€ as {side}?',
        'game_cancelled': 'Game cancelled. Bet refunded.',
        'select_room': 'Select a game to join:',
        'achievement_start': 'Write /start in the bot',
        'achievement_first_purchase': 'Make your first purchase',
        'achievement_first_topup': 'Top up your balance',
        'achievement_first_blackjack': 'Play Blackjack',
        'achievement_first_coinflip': 'Play Coinflip',
        'achievement_gift_sent': 'Send a gift',
        'achievement_first_referral': 'Invite a friend',
        'achievement_five_purchases': 'Buy 5 items',
        'achievement_streak_three': '3-day purchase streak',
        'achievement_ten_referrals': 'Refer 10 friends',
        'achievement_unlocked': '🏆 Achievement unlocked: {name}',
        'show_unlocked': 'Show Unlocked',
        'show_locked': 'Show Locked',
        'level_up': '🎉 Congratulations! You reached {level} and received a {discount}% discount for future purchases.',



    },
    'ru': {
        'hello': '👋 Привет, {user}!',
        'balance': '💰 Баланс: {balance} EUR',
        'overpay': '💳 Отправьте точную сумму. Переплаты будут зачислены.',
        'shop': '🛍 Магазин',
        'profile': '👤 Профиль',
        'top_up': '💸 Пополнить',
        'channel': '📢 Канал',
        'price_list': '💲 Прайс-лист',
        'language': '🌐 Язык',
        'admin_panel': '🎛 Админ панель',
        'help': '❓ Помощь',
        'help_info': (
            'Используйте главное меню для работы с ботом:\n'
            '🛍 Магазин – просматривайте категории и выбирайте товар.\n'
            '   • Выберите товар и подтвердите покупку.\n'
            '👤 Профиль – ваш баланс и купленные товары.\n'
            '💸 Пополнить – выберите способ оплаты и следуйте инструкциям.\n'
            '🌐 Язык – сменить язык интерфейса.\n'
            '🎁 Купленные товары – доступны в профиле после покупки.\n'
            'Если нужна помощь, обратитесь к {helper}.'
        ),
        'admin_help_info': (
            'Функции админ-панели:\n'
            '🛠 Назначить ассистентов – управление помощниками.\n'
            '📦 Просмотр склада – список товаров и удаление остатков.\n'
            '🏪 Parduotuvės valdymas – управление магазином.\n'
            '👥 Vartotojų valdymas – управление пользователями.\n'
            '📢 Pranešimų siuntimas – рассылка сообщений.'
        ),
        'assistant_help_info': (
            'Функции панели ассистента:\n'
            '🖼 Привязать фото – добавление фотографий к товарам.\n'
            'Используйте "Назад в меню" для возврата.'
        ),
        'choose_language': 'Пожалуйста, выберите язык',
        'invoice_message': (
            '🧾 <b>Создан инвойс на оплату</b>\n\n'
            '<b>Сумма:</b> <code>{amount}</code> {currency}\n'
            '🏦 <b>Адрес оплаты:</b>\n<code>{address}</code>\n\n'
            '⏳ <b>Действителен до:</b> {expires_at} LT\n'
            '⚠️ <b>Оплата должна быть выполнена в течение 15 минут после создания.</b>\n\n'
            '❗️ <b>Важно:</b> Отправьте <u>ровно</u> это количество {currency}.\n\n'
            '✅ <b>Подтверждение произойдет автоматически через вебхук после подтверждения сети.</b>'
        ),
        'cancel': 'Отмена',
        'cancel_payment': '❌ Отменить оплату',
        'payment_successful': '✅ Платёж подтверждён. Баланс пополнен на {amount}€',
        'back_home': 'Назад домой',
        'invoice_cancelled': 'Оплата не завершена/истекла. Ваши товары больше не зарезервированы.',
        'total_purchases': '📦 Всего покупок: {count}',
        'streak': '🔥 Серия: {days} дн.',
        'note': '⚠️ Возврат средств невозможен. Отправляйте точную сумму, недоплаты не подтверждаются.',
        'rate_experience': '⭐ Как вы оцениваете общий опыт?',
        'rate_service': 'Как вы оцениваете качество сервиса?',
        'rate_product': 'Что вы думаете о товаре?',
        'ask_feedback_reason': 'Хотите написать почему?',
        'feedback_reason': 'Пожалуйста, напишите ваш отзыв:',
        'thanks_feedback': 'Спасибо за отзыв!',
        'confirm_purchase': 'Подтвердить покупку {item} за {price}€?',
        'purchase_button': 'Купить',
        'apply_promo': 'Применить промокод',
        'promo_prompt': 'Введите промокод:',
        'promo_invalid': '❌ Недействительный или просроченный промокод',
        'promo_applied': '✅ Промокод применён. Новая цена: {price}€',
        'yes': '✅ Да',
        'no': '❌ Нет',
        'confirm': '✅ Подтвердить',
        'rerun': '🔄 Перезапустить',
        'assign_more': '✅ Фото добавлено. Добавить ещё?',
        'purchased_items': '📦 Купленные товары',
        'purchased_items': '🎁 Купленные товары',
        'back_to_menu': '🔙 Назад в меню',
        'users_tickets': '🎟️ Билеты пользователей:',
        'no_tickets': 'Нет билетов',
        'lottery_winner': '🎉 Победитель: {username}\n🎟️ Билеты: {tickets}\n\n❗️ Подтверждение сбросит все билеты.',
        'lottery_broadcast_prompt': 'Отправить сообщение всем пользователям?',
        'lottery_enter_message': '✉️ Введите сообщение:',
        'lottery_finished': '✅ Лотерея завершена.',
        'no_winner': '❌ Нет победителя',
        'tools': '🧰 Инструменты',
        'lottery': '🎟️ Лотерея',
        'insufficient_rights': 'Недостаточно прав',
        'use_balance_prompt': 'У вас {balance}€. Использовать их для снижения цены?',
        'choose_crypto': 'Выберите способ оплаты:',
        'need_top_up': 'Вам нужно пополнить {missing}€ для покупки. Выберите способ оплаты:',
        'item_reserved': '🔒 Товар зарезервирован для вас на 15 минут.',
        'payment_cancelled': '✅ Платёж отменён. Резерв снят.',
        'top_up_completed': '✅ Пополнение завершено.',
        'lottery_ticket_awarded': '🎟️ Вы получили лотерейный билет.',
        'lottery_tickets': '🎟️ <b>Лотерейные билеты</b> — <code>{tickets}</code>',
        'referral_link': '🤝 <b>Реферальная ссылка</b> — <code>{link}</code>',
        'referrals': '👥 <b>Рефералы</b> — {count}',
        'referral_earnings': '💰 <b>Заработок с рефералов</b> — <code>{amount}</code> €',
        'referral_reward': '🎉 Ваш реферал {user} совершил покупку — вы получили {amount}€!',
        'gift': '🎁 Подарок',
        'gift_prompt': 'Кому вы хотите подарить товар?',
        'gift_user_not_found': '❌ Пользователь не найден.',
        'gift_select_category': '🎁 Выберите товар для подарка пользователю {user}:',
        'gift_sent': '🎁 Подарок отправлен пользователю {user}!',
        'gift_received': '🎁 Вы получили {item} от {user}!',
        'stock_notify': '📦 Уведомления о наличии',
        'choose_product_notify': 'Выберите товар для уведомления о появлении:',
        'no_out_of_stock': '✅ Все товары в наличии.',
        'stock_subscribed': '🔔 Мы уведомим вас, когда {item} появится.',
        'stock_already_subscribed': 'ℹ️ Вы уже ожидаете {item}.',
        'stock_back_in': '📦 {item} снова в наличии!',

        'choose_subcategory': '🏘️ Выберите район:',
        'select_product': '🏪 Выберите товар',
        'games': '🎮 Игры',
        'blackjack': '🃏 Блэкджек',
        'coinflip': '🪙 Монетка',
        'achievements': '🏆 Достижения',
        'quests': '🧩 Персональные задания',
        'quests_placeholder': '🔧 Задания скоро появятся.',
        'find_game': '🔍 Найти игру',
        'create_game': '➕ Создать игру',
        'play_bot': '🤖 Играть с ботом',
        'choose_game': 'Выберите игру',
        'choose_side': 'Выберите сторону:',
        'enter_bet': 'Введите сумму ставки:',
        'heads': 'Орел',
        'tails': 'Решка',
        'not_enough_balance': '❌ Недостаточно средств',
        'win': 'Вы выиграли {amount}€!',
        'lose': 'Вы проиграли {amount}€.',
        'back': '🔙 Назад',
        'create': '✅ Создать',
        'join': '✅ Присоединиться',
        'waiting_opponent': '⏳ Ожидание оппонента...',
        'no_games': '❌ Нет доступных игр',
        'join_confirm': 'Играть с {user} на {bet}€ за {side}?',
        'create_confirm': 'Создать игру на {bet}€ за {side}?',
        'game_cancelled': 'Игра отменена. Ставка возвращена.',
        'select_room': 'Выберите игру для присоединения:',
        'achievement_start': 'Напишите /start боту',
        'achievement_first_purchase': 'Совершите первую покупку',
        'achievement_first_topup': 'Пополните баланс',

        'achievement_first_blackjack': 'Сыграйте в Блэкджек',
        'achievement_first_coinflip': 'Сыграйте в Монетку',
        'achievement_gift_sent': 'Отправьте подарок',
        'achievement_first_referral': 'Пригласите друга',
        'achievement_five_purchases': 'Купите 5 товаров',
        'achievement_streak_three': 'Покупайте 3 дня подряд',
        'achievement_ten_referrals': 'Пригласите 10 друзей',
        'achievement_unlocked': '🏆 Достижение получено: {name}',
        'show_unlocked': 'Показать полученные',
        'show_locked': 'Показать неполученные',
        'level_up': '🎉 Поздравляем! Вы достигли уровня {level} и получили скидку {discount}% на будущие покупки.',

    },
    'lt': {
        'hello': '👋 Sveiki, {user}!',
        'balance': '💰 Balansas: {balance} EUR',
        'overpay': '💳 Siųskite tikslią sumą. Permokos bus įskaitytos.',
        'shop': '🛍 Parduotuvė',
        'profile': '👤 Profilis',
        'top_up': '💸 Papildyti',
        'channel': '📢 Kanalas',
        'price_list': '💲 Kainoraštis',
        'language': '🌐 Kalba',
        'admin_panel': '🎛 Admin pultas',
        'help': '❓ Pagalba',
        'help_info': (
            'Naudokite pagrindinį meniu darbui su botu:\n'
            '🛍 Parduotuvė – naršykite kategorijas ir pasirinkite prekę.\n'
            '   • Pasirinkite prekę ir patvirtinkite pirkimą.\n'
            '👤 Profilis – jūsų balansas ir nupirktos prekės.\n'
            '💸 Papildyti – pasirinkite mokėjimo būdą ir vykdykite instrukcijas.\n'
            '🌐 Kalba – pakeisti sąsajos kalbą.\n'
            '🎁 Nupirktos prekės – matomos profilyje po pirkimo.\n'
            'Jei reikia pagalbos, susisiekite su {helper}.'
        ),
        'admin_help_info': (
            'Admin pulto funkcijos:\n'
            '🛠 Asistentų priskyrimas – valdykite asistentų paskyras.\n'
            '📦 Peržiūrėti likučius – naršykite prekes ir trinkite likučius.\n'
            '🏪 Parduotuvės valdymas – prekių ir kategorijų valdymas.\n'
            '👥 Vartotojų valdymas – naudotojų balansai ir rolės.\n'
            '📢 Pranešimų siuntimas – siųsti žinutes vartotojams.'
        ),
        'assistant_help_info': (
            'Asistento pulto funkcijos:\n'
            '🖼 Nuotraukų priskyrimas – pridėkite nuotraukas prie prekių.\n'
            'Naudokite „Atgal į meniu“ norėdami grįžti.'
        ),
        'choose_language': 'Pasirinkite kalbą',
        'invoice_message': (
            '🧾 <b>Sukurta mokėjimo sąskaita</b>\n\n'
            '<b>Suma:</b> <code>{amount}</code> {currency}\n'
            '🏦 <b>Mokėjimo adresas:</b>\n<code>{address}</code>\n\n'
            '⏳ <b>Galioja iki:</b> {expires_at} LT\n'
            '⚠️ <b>Mokėjimą reikia atlikti per 15 minučių nuo sąskaitos sukūrimo.</b>\n\n'
            '❗️ <b>Svarbu:</b> Nusiųskite <u>tiksliai</u> tiek {currency} į šį adresą.\n\n'
            '✅ <b>Patvirtinimas vyks automatiškai per webhook po tinklo patvirtinimo.</b>'
        ),
        'cancel': 'Atšaukti',
        'cancel_payment': '❌ Atšaukti mokėjimą',
        'payment_successful': '✅ Mokėjimas patvirtintas. Balansas padidintas {amount}€',
        'back_home': 'Grįžti į pradžią',
        'invoice_cancelled': 'Mokėjimas nepavyko/baigėsi. Jūsų prekės nebėra rezervuotos.',
        'total_purchases': '📦 Viso pirkinių: {count}',
        'streak': '🔥 Serija: {days} d.',
        'note': '⚠️ Pastaba: grąžinimų nėra. Įsitikinkite, kad siunčiate tikslią sumą, nes nepakankamos sumos nebus patvirtintos.',
        'rate_experience': '⭐ Kaip vertinate bendrą patirtį?',
        'rate_service': 'Kaip vertinate aptarnavimo kokybę?',
        'rate_product': 'Kokia jūsų nuomonė apie produktą?',
        'ask_feedback_reason': 'Ar norėtumėte parašyti kodėl?',
        'feedback_reason': 'Prašome parašyti atsiliepimą:',
        'thanks_feedback': 'Ačiū už atsiliepimą!',
        'confirm_purchase': 'Patvirtinti {item} pirkimą už {price}€?',
        'purchase_button': 'Pirkti',
        'apply_promo': 'Taikyti nuolaidos kodą',
        'promo_prompt': 'Įveskite nuolaidos kodą:',
        'promo_invalid': '❌ Neteisingas arba pasibaigęs kodas',
        'promo_applied': '✅ Kodas pritaikytas. Nauja kaina: {price}€',
        'yes': '✅ Taip',
        'no': '❌ Ne',
        'confirm': '✅ Patvirtinti',
        'rerun': '🔄 Perleisti',
        'assign_more': '✅ Nuotrauka pridėta. Pridėti dar?',
        'purchased_items': '📦 Įsigytos prekės',
        'purchased_items': '🎁 Įsigytos prekės',
        'back_to_menu': '🔙 Atgal į meniu',
        'users_tickets': '🎟️ Vartotojų bilietai:',
        'no_tickets': 'Nėra bilietų',
        'lottery_winner': '🎉 Nugalėtojas: {username}\n🎟️ Bilietai: {tickets}\n\n❗️ Patvirtinus, visi bilietai bus ištrinti.',
        'lottery_broadcast_prompt': 'Siųsti pranešimą visiems vartotojams?',
        'lottery_enter_message': '✉️ Įveskite pranešimą:',
        'lottery_finished': '✅ Loterija baigta.',
        'no_winner': '❌ Nėra nugalėtojo',
        'tools': '🧰 Įrankiai',
        'lottery': '🎟️ Loterija',
        'insufficient_rights': 'Nepakanka teisių',
        'use_balance_prompt': 'Turite {balance}€. Panaudoti juos kainai sumažinti?',
        'choose_crypto': 'Pasirinkite mokėjimo būdą:',
        'need_top_up': 'Turite papildyti {missing}€ šiam pirkiniui. Pasirinkite mokėjimo būdą:',
        'item_reserved': '🔒 Prekė rezervuota jums 15 minučių.',
        'payment_cancelled': '✅ Mokėjimas atšauktas. Rezervuotos prekės atlaisvintos.',
        'top_up_completed': '✅ Papildymas baigtas.',
        'lottery_ticket_awarded': '🎟️ Gavote loterijos bilietą.',
        'lottery_tickets': '🎟️ <b>Loterijos bilietai</b> — <code>{tickets}</code>',
        'referral_link': '🤝 <b>Pakvietimo nuoroda</b> — <code>{link}</code>',
        'referrals': '👥 <b>Pakviesti vartotojai</b> — {count}',
        'referral_earnings': '💰 <b>Uždirbta iš pakvietimų</b> — <code>{amount}</code> €',
        'referral_reward': '🎉 Jūsų pakviestas vartotojas {user} įsigijo prekę – gavote {amount}€!',
        'gift': '🎁 Dovana',
        'gift_prompt': 'Kam norite padovanoti produktą?',
        'gift_user_not_found': '❌ Vartotojas nerastas.',
        'gift_select_category': '🎁 Pasirinkite produktą dovanai naudotojui {user}:',
        'gift_sent': '🎁 Dovana išsiųsta naudotojui {user}!',
        'gift_received': '🎁 Gavote {item} nuo {user}!',

        'stock_notify': '📦 Atsargų pranešimai',
        'choose_product_notify': 'Pasirinkite prekę, kurios atsargų laukti:',
        'no_out_of_stock': '✅ Visos prekės turimos.',
        'stock_subscribed': '🔔 Būsite informuoti, kai {item} bus papildyta.',
        'stock_already_subscribed': 'ℹ️ Jūs jau laukiate {item}.',
        'stock_back_in': '📦 {item} vėl sandėlyje!',

        'choose_subcategory': '🏘️ Pasirinkite rajoną:',
        'select_product': '🏪 Pasirinkite prekę',
        'games': '🎮 Žaidimai',
        'blackjack': '🃏 Blackjack',
        'coinflip': '🪙 Monetos metimas',
        'achievements': '🏆 Pasiekimai',
        'quests': '🧩 Asmeniniai uždaviniai',
        'quests_placeholder': '🔧 Uždaviniai greitai atsiras.',
        'find_game': '🔍 Rasti žaidimą',
        'create_game': '➕ Sukurti žaidimą',
        'play_bot': '🤖 Žaisti su botu',
        'choose_game': 'Pasirinkite žaidimą',
        'choose_side': 'Pasirinkite pusę:',
        'enter_bet': 'Įveskite statymo sumą:',
        'heads': 'Herbas',
        'tails': 'Skaičius',
        'not_enough_balance': '❌ Nepakanka lėšų',
        'win': 'Laimėjote {amount}€!',
        'lose': 'Pralaimėjote {amount}€.',
        'back': '🔙 Atgal',
        'create': '✅ Sukurti',
        'join': '✅ Prisijungti',
        'waiting_opponent': '⏳ Laukiama priešininko...',
        'no_games': '❌ Nėra žaidimų',
        'join_confirm': 'Žaisti prieš {user} už {bet}€ kaip {side}?',
        'create_confirm': 'Sukurti žaidimą už {bet}€ kaip {side}?',
        'game_cancelled': 'Žaidimas atšauktas. Statymas grąžintas.',
        'select_room': 'Pasirinkite žaidimą prisijungti:',
        'achievement_start': 'Parašykite /start botui',
        'achievement_first_purchase': 'Atlikite pirmą pirkimą',
        'achievement_first_topup': 'Papildykite balansą',
        'achievement_first_blackjack': 'Sužaiskite Blackjack',
        'achievement_first_coinflip': 'Sužaiskite monetą',
        'achievement_gift_sent': 'Išsiųskite dovaną',
        'achievement_first_referral': 'Pakvieskite draugą',
        'achievement_five_purchases': 'Nupirkite 5 prekes',
        'achievement_streak_three': '3 dienų pirkimų serija',
        'achievement_ten_referrals': 'Pakvieskite 10 draugų',
        'achievement_unlocked': '🏆 Pasiekimas atrakintas: {name}',
        'show_unlocked': 'Rodyti pasiektus',
        'show_locked': 'Rodyti nepasiektus',
        'level_up': '🎉 Sveikiname! Pasiekėte {level} ir gavote {discount}% nuolaidą būsimiems pirkiniams.',


        'achievement_unlocked': '🏆 Pasiekimas atrakintas: {name}',




    },
}

def t(lang: str, key: str, **kwargs) -> str:
    lang_data = LANGUAGES.get(lang, LANGUAGES['en'])
    template = lang_data.get(key, '')
    return template.format(**kwargs)
