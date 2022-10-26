from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import modul as md


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'/hello\n/help\n/view_horiz\n/view_vert\n'
                                    f'/export_to_txt\n/export_to_json\n'
                                    f'/import_from_txt\n/import_from_json')

async def view_horiz(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    data_base, fields, count_entrys = md.unload('phonebook.csv')
    for row in data_base:
        await update.message.reply_text(f'{fields[0]}: {row[0]}, {fields[1]}: {row[1]}, '
                                        f'{fields[2]}: {row[2]}, {fields[3]}: {row[3]}')

async def view_vert(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    data_base, fields, count_entrys = md.unload('phonebook.csv')
    for row in data_base:
        await update.message.reply_text(f'{fields[0]}: {row[0]}\n{fields[1]}: {row[1]}\n'
                                        f'{fields[2]}: {row[2]}\n{fields[3]}: {row[3]}')

async def export_to_txt(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    data_base, fields, count_entrys = md.unload('phonebook.csv')
    md.export_txt('phonebook.txt', data_base, fields, count_entrys)
    await update.message.reply_text('Контакты успешно экспортированы из телефонной книги')

async def export_to_json(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    data_base, fields, count_entrys = md.unload('phonebook.csv')
    md.export_json('phonebook.json', data_base, fields, count_entrys)
    await update.message.reply_text('Контакты успешно экспортированы из телефонной книги')

async def import_from_txt(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    md.data_to_csv('phonebook.csv', md.import_txt('phonebook.txt'))
    await update.message.reply_text('Контакты успешно импортированы в телефонную книгу')

async def import_from_json(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    md.data_to_csv('phonebook.csv', md.import_json('phonebook.json'))
    await update.message.reply_text('Контакты успешно импортированы в телефонную книгу')

app = ApplicationBuilder().token("5572512702:AAEQRusfhs2v-ptodehDezryf-kCSXmp7c8").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("view_horiz", view_horiz))
app.add_handler(CommandHandler("view_vert", view_vert))
app.add_handler(CommandHandler("export_to_txt", export_to_txt))
app.add_handler(CommandHandler("export_to_json", export_to_json))
app.add_handler(CommandHandler("import_from_txt", import_from_txt))
app.add_handler(CommandHandler("import_from_json", import_from_json))

app.run_polling()

