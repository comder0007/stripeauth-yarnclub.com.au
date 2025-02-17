import telebot
from telebot import types
from gate import * 
import chardet,colorama,time

BOT_TOKEN = "6316751123:AAGLuAetDS_eA19RtEcUcDvUbqro-bv7nKg"
bot = telebot.TeleBot(BOT_TOKEN,parse_mode="HTML")

@bot.message_handler(commands=['chk'])
def chk_command(message):
    try:
        aux = bot.reply_to(message, "<b>Checking ...</b>", parse_mode="HTML")

        if len(message.text.split()) > 1:
            user_message = message.text.split(None, 1)[1].strip()
            items = user_message.split()

            if len(items) > 10:
                bot.edit_message_text(
                    text="❌ <b>Limit exceeded:</b> Maximum 10 allowed.",
                    chat_id=aux.chat.id,
                    message_id=aux.message_id,
                    parse_mode="HTML"
                )
                return

            results = []
            for user_message in items:
                try:
                    ccx, result = Tele(user_message)
                    safe_ccx = ccx.replace("<", "&lt;").replace(">", "&gt;").replace("&", "&amp;")
                    safe_result = result.replace("<", "&lt;").replace(">", "&gt;").replace("&", "&amp;")
                    if "success" in safe_result or "incorrect." in safe_result:
                        print(Fore.GREEN + f"{safe_ccx} {safe_result}")
                    elif "declined." in safe_result or "No such PaymentMethod: 'None'" in safe_result:
                        print(Fore.RED + f"{safe_ccx} declined")
                    else:
                        print(Fore.GREEN + f"{safe_ccx}{safe_result}")
                    results.append(f"<b>{safe_ccx}</b>\n{safe_result}")

                    # Limit bot API calls by updating after processing multiple cards
                    if len(results) % 2 == 0 or len(results) == len(items):
                        response = "\n\n".join(results)
                        bot.edit_message_text(
                            text=response,
                            chat_id=aux.chat.id,
                            message_id=aux.message_id,
                            parse_mode="HTML"
                        )

                except ValueError:
                    print(f"Invalid format: {user_message} (expected cc)")

        else:
            bot.edit_message_text(
                "<b>Usage:</b> /chk cc_number",
                chat_id=aux.chat.id,
                message_id=aux.message_id,
                parse_mode="HTML"
            )

    except Exception as e:
        bot.reply_to(message, f"❌ Error: {e}")



@bot.message_handler(content_types=['document'])
def handle_file_upload(message):
    try:
        ok, bad, checked = 0, 0, 0
        aux = bot.reply_to(message, "<b>Processing file...</b>", parse_mode='HTML')

        file_info = bot.get_file(message.document.file_id)
        file = bot.download_file(file_info.file_path)

        # 🔹 Detect encoding
        detected_encoding = chardet.detect(file)['encoding']
        if detected_encoding is None:
            detected_encoding = 'utf-8'  # Default to UTF-8 if detection fails

        file_content = file.decode(detected_encoding, errors='ignore')  # Decode using detected encoding
        lines = file_content.splitlines()
        total = len(lines)

        with open("aas.txt", "w", encoding="utf-8") as f:  # Open file in write mode
            for i, line in enumerate(lines, start=1):
                line=line.strip()
                try:
                    ccx, result = Tele(line)  # Assuming Tele() is your checking function
                    checked += 1
                    ccx = ccx.replace("<", "&lt;").replace(">", "&gt;").replace("&", "&amp;")
                    result = result.replace("<", "&lt;").replace(">", "&gt;").replace("&", "&amp;")

                    if "success" in result or "incorrect." in result:
                        print(Fore.GREEN + f"{ccx} {result}")
                        ok += 1
                    elif "declined." in result or "No such PaymentMethod: 'None'" in result:
                        print(Fore.RED + f"{ccx} declined")
                        bad += 1
                    else:
                        print(Fore.GREEN + f"{ccx}{result}")
                        ok += 1

                    # Append results to the file and flush for real-time updates
                    f.write(f"{ccx}\n{result}\n\n")
                    f.flush()

                    # 🔹 Update progress every 10 lines
                    
                    mes = types.InlineKeyboardMarkup(row_width=1)
                    mes.add(
                            types.InlineKeyboardButton(f"• HIT ✅ : [ {ok} ] •", callback_data='u2'),
                            types.InlineKeyboardButton(f"• DEAD ❌ : [ {bad} ] •", callback_data='u1'),
                            types.InlineKeyboardButton(f"• CHECKED : [ {checked} ] •", callback_data='u1'),
                            types.InlineKeyboardButton(f"• TOTAL : [ {total} ] •", callback_data='u1')
                        )

                    bot.edit_message_text(
                            chat_id=aux.chat.id,
                            message_id=aux.message_id,
                            text=f"⏳ Processing... {checked}/{total}",
                            parse_mode='markdown',
                            reply_markup=mes
                        )

                    time.sleep(1)  # Small delay to prevent rate limiting

                except ValueError:
                    print(f"Invalid format: {line}")
                    bad += 1

        # 🔹 Final update when complete
        mes = types.InlineKeyboardMarkup(row_width=1)
        mes.add(
            types.InlineKeyboardButton(f"• HIT ✅ : [ {ok} ] •", callback_data='u2'),
            types.InlineKeyboardButton(f"• DEAD ❌ : [ {bad} ] •", callback_data='u1'),
            types.InlineKeyboardButton(f"• CHECKED : [ {checked} ] •", callback_data='u1'),
            types.InlineKeyboardButton(f"• TOTAL : [ {total} ] •", callback_data='u1')
        )

        bot.edit_message_text(
            chat_id=aux.chat.id,
            message_id=aux.message_id,
            text=f"✅ Checking complete!",
            parse_mode='markdown',
            reply_markup=mes
        )

        # 🔹 Send the file to the user
        with open("aas.txt", "rb") as result_file:
            bot.send_document(message.chat.id, result_file, caption="✅ Here is your checked result.")

    except Exception as e:
        bot.reply_to(message, f"❌ Error: {str(e)}")




if __name__ == "__main__":
    print("Bot is running...")
    bot.polling()