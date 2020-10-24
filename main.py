from telegram.ext import Updater, CommandHandler
import logging


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


updater = Updater(token='1375902392:AAFPqf7WRftghnnGQdf8y1uYwWPMuRrhjgI')


def start(upd, ctx):
    ctx.bot.send_message(
        chat_id=upd.effective_chat.id,
        text="Hello world!",
    )

def one(upd, ctx):
    ctx.bot.send_message(
        chat_id=upd.effective_chat.id,
        text="Bye!"
    )


start_handler_ = CommandHandler('bye',one)
start_handler = CommandHandler('go',start)
updater.dispatcher.add_handler(start_handler)

if __name__ == '__main__':
    updater.start_polling()