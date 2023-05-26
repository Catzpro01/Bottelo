import logging
import requests
import json
import datetime
import time
from telegram import ChatAction
from telegram.ext import Updater
from telegram.ext import Updater, CommandHandler, Job
from telegram import ChatAction



logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

TOKEN = '6272895233:AAFDEhbkUcSq61bFtUWFQWl0JmAPziMWYxc'

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher
job_queue = updater.job_queue






def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Selamat datang bosku!")
    context.bot.send_message(chat_id=update.effective_chat.id, text="/historis, /analisis, /stop")
    
start_handler = CommandHandler('start', start)

def menu(update, context):
    menu_data = menu_format_data()
    context.bot.send_message(chat_id=update.effective_chat.id, text=menu_data)

def menu_format_data():
    pesan = "==========Menu Home==========\n"
    pesan += "/historis\n"
    pesan += "/analisis\n"
    pesan += "========== Interval ============\n"
    pesan += "/int1     /int2     /int3     /int4     /int5\n"
    pesan += "/int6     /int7     /int8     /int9     /int10\n"
    pesan += "==============================\n"
    pesan += "/int20   /int30   /int40   /int50\n"
    pesan += "==============================\n"
    pesan += "/note: setiap diklik otomatis send 2 mnt\n"
    
    return pesan

menu_handler = CommandHandler('menu', menu)


def historis(update, context):
    data_historis = ambil_data_historis()
    pesan = format_data_historis(data_historis)
    context.bot.send_message(chat_id=update.effective_chat.id, text=pesan)
    job = job_queue.run_repeating(send_historis, interval=119., first=0, context=update.effective_chat.id, name='historis')
    context.chat_data['historis_job'] = job
    update.message.reply_text('Pengiriman pesan otomatis dimulai!')
    
historis_handler = CommandHandler('historis', historis)

def analisis(update, context):
    data_analisis = ambil_data_historis()
    pesan = format_data_analisis(data_analisis)
    context.bot.send_message(chat_id=update.effective_chat.id, text=pesan)
    job = job_queue.run_repeating(send_analisis, interval=119, first=0, context=update.effective_chat.id, name='analisis')
    context.chat_data['analisis_job'] = job
    update.message.reply_text('Pengiriman pesan otomatis dimulai!')
    
analisis_handler = CommandHandler('analisis', analisis)

def int1(update, context):
    data_int1 = ambil_data_historis()
    pesan = format_data_int1(data_int1)
    context.bot.send_message(chat_id=update.effective_chat.id, text=pesan)
    job = job_queue.run_repeating(send_int1, interval=119, first=0, context=update.effective_chat.id, name='int1')
    context.chat_data['int1_job'] = job
    update.message.reply_text('Pengiriman pesan otomatis dimulai!')
    
int1_handler = CommandHandler('int1', int1)

#bagian ke 1 untuk mendefinisikan prompt 


#D
def int2(update, context):
    data_int2 = ambil_data_historis()
    pesan = format_data_int2(data_int2)
    context.bot.send_message(chat_id=update.effective_chat.id, text=pesan)
    job = job_queue.run_repeating(send_int2, interval=119, first=0, context=update.effective_chat.id, name='int2')
    context.chat_data['int2_job'] = job
    update.message.reply_text('Pengiriman pesan otomatis dimulai!')
    

int2_handler = CommandHandler('int2', int2)

#E
def int3(update, context):
    data_int3 = ambil_data_historis()
    pesan = format_data_int3(data_int3)
    context.bot.send_message(chat_id=update.effective_chat.id, text=pesan)
    job = job_queue.run_repeating(send_int3, interval=119, first=0, context=update.effective_chat.id, name='int3')
    context.chat_data['int3_job'] = job
    update.message.reply_text('Pengiriman pesan otomatis dimulai!')
    
int3_handler = CommandHandler('int3', int3)

#F
def int4(update, context):
    data_int4 = ambil_data_historis()
    pesan = format_data_int4(data_int4)
    context.bot.send_message(chat_id=update.effective_chat.id, text=pesan)
    job = job_queue.run_repeating(send_int4, interval=119, first=0, context=update.effective_chat.id, name='int4')
    context.chat_data['int4_job'] = job
    update.message.reply_text('Pengiriman pesan otomatis dimulai!')
    
int4_handler = CommandHandler('int4', int4)

#G
def int5(update, context):
    data_int5 = ambil_data_historis()
    pesan = format_data_int5(data_int5)
    context.bot.send_message(chat_id=update.effective_chat.id, text=pesan)
    job = job_queue.run_repeating(send_int5, interval=119, first=0, context=update.effective_chat.id, name='int5')
    context.chat_data['int5_job'] = job
    update.message.reply_text('Pengiriman pesan otomatis dimulai!')
    
int5_handler = CommandHandler('int5', int5)

#H
def int6(update, context):
    data_int6 = ambil_data_historis()
    pesan = format_data_int6(data_int6)
    context.bot.send_message(chat_id=update.effective_chat.id, text=pesan)
    job = job_queue.run_repeating(send_int6, interval=119, first=0, context=update.effective_chat.id, name='int6')
    context.chat_data['int6_job'] = job
    update.message.reply_text('Pengiriman pesan otomatis dimulai!')
    
int6_handler = CommandHandler('int6', int6)

#I
def int7(update, context):
    data_int7 = ambil_data_historis()
    pesan = format_data_int7(data_int7)
    context.bot.send_message(chat_id=update.effective_chat.id, text=pesan)
    job = job_queue.run_repeating(send_int7, interval=119, first=0, context=update.effective_chat.id, name='int7')
    context.chat_data['int7_job'] = job
    update.message.reply_text('Pengiriman pesan otomatis dimulai!')
    
int7_handler = CommandHandler('int7', int7)

#J
def int8(update, context):
    data_int8 = ambil_data_historis()
    pesan = format_data_int8(data_int8)
    context.bot.send_message(chat_id=update.effective_chat.id, text=pesan)
    job = job_queue.run_repeating(send_int8, interval=119, first=0, context=update.effective_chat.id, name='int8')
    context.chat_data['int8_job'] = job
    update.message.reply_text('Pengiriman pesan otomatis dimulai!')
    
int8_handler = CommandHandler('int8', int8)


#K
def int9(update, context):
    data_int9 = ambil_data_historis()
    pesan = format_data_int9(data_int9)
    context.bot.send_message(chat_id=update.effective_chat.id, text=pesan)
    job = job_queue.run_repeating(send_int9, interval=119, first=0, context=update.effective_chat.id, name='int9')
    context.chat_data['int9_job'] = job
    update.message.reply_text('Pengiriman pesan otomatis dimulai!')
    
int9_handler = CommandHandler('int9', int9)

#L
def int10(update, context):
    data_int10 = ambil_data_historis()
    pesan = format_data_int10(data_int10)
    context.bot.send_message(chat_id=update.effective_chat.id, text=pesan)
    job = job_queue.run_repeating(send_int10, interval=119, first=0, context=update.effective_chat.id, name='int10')
    context.chat_data['int10_job'] = job
    update.message.reply_text('Pengiriman pesan otomatis dimulai!')
    
int10_handler = CommandHandler('int10', int10)

#M
def int20(update, context):
    data_int20 = ambil_data_historis()
    pesan = format_data_int20(data_int20)
    context.bot.send_message(chat_id=update.effective_chat.id, text=pesan)
    job = job_queue.run_repeating(send_int20, interval=119, first=0, context=update.effective_chat.id, name='int20')
    context.chat_data['int20_job'] = job
    update.message.reply_text('Pengiriman pesan otomatis dimulai!')
    
int20_handler = CommandHandler('int20', int20)

#N
def int30(update, context):
    data_int30 = ambil_data_historis()
    pesan = format_data_int30(data_int30)
    context.bot.send_message(chat_id=update.effective_chat.id, text=pesan)
    job = job_queue.run_repeating(send_int30, interval=119, first=0, context=update.effective_chat.id, name='int30')
    context.chat_data['int30_job'] = job
    update.message.reply_text('Pengiriman pesan otomatis dimulai!')
    
int30_handler = CommandHandler('int30', int30)

#O
def int40(update, context):
    data_int40 = ambil_data_historis()
    pesan = format_data_int40(data_int40)
    context.bot.send_message(chat_id=update.effective_chat.id, text=pesan)
    job = job_queue.run_repeating(send_int40, interval=119, first=0, context=update.effective_chat.id, name='int40')
    context.chat_data['int40_job'] = job
    update.message.reply_text('Pengiriman pesan otomatis dimulai!')

int40_handler = CommandHandler('int40', int40)

#P
def int50(update, context):
    data_int50 = ambil_data_historis()
    pesan = format_data_int50(data_int50)
    context.bot.send_message(chat_id=update.effective_chat.id, text=pesan)
    job = job_queue.run_repeating(send_int50, interval=119, first=0, context=update.effective_chat.id, name='int50')
    context.chat_data['int50_job'] = job
    update.message.reply_text('Pengiriman pesan otomatis dimulai!')
    
int50_handler = CommandHandler('int50', int50)



def stop(update, context):
    if 'historis_job' in context.chat_data:
        historis_job = context.chat_data['historis_job']
        historis_job.schedule_removal()
        del context.chat_data['historis_job']
    if 'analisis_job' in context.chat_data:
        analisis_job = context.chat_data['analisis_job']
        analisis_job.schedule_removal()
        del context.chat_data['analisis_job']
        
    if 'int1_job' in context.chat_data:
        int1_job = context.chat_data['int1_job']
        int1_job.schedule_removal()
        del context.chat_data['int1_job']
    #D
    if 'int2_job' in context.chat_data:
        int2_job = context.chat_data['int2_job']
        int2_job.schedule_removal()
        del context.chat_data['int2_job']
    
    #E
    if 'int3_job' in context.chat_data:
        int3_job = context.chat_data['int3_job']
        int3_job.schedule_removal()
        del context.chat_data['int3_job']
    
    #F
    if 'int4_job' in context.chat_data:
        int4_job = context.chat_data['int4_job']
        int4_job.schedule_removal()
        del context.chat_data['int4_job']
    
    #G
    if 'int5_job' in context.chat_data:
        int5_job = context.chat_data['int5_job']
        int5_job.schedule_removal()
        del context.chat_data['int5_job']
    
    #H
    if 'int6_job' in context.chat_data:
        int6_job = context.chat_data['int6_job']
        int6_job.schedule_removal()
        del context.chat_data['int6_job']
    
    #I
    if 'int7_job' in context.chat_data:
        int7_job = context.chat_data['int7_job']
        int7_job.schedule_removal()
        del context.chat_data['int7_job']
    
    #J
    if 'int8_job' in context.chat_data:
        int8_job = context.chat_data['int8_job']
        int8_job.schedule_removal()
        del context.chat_data['int8_job']
    
    #K
    if 'int9_job' in context.chat_data:
        int9_job = context.chat_data['int9_job']
        int9_job.schedule_removal()
        del context.chat_data['int9_job']
    
    #L
    if 'int10_job' in context.chat_data:
        int10_job = context.chat_data['int10_job']
        int10_job.schedule_removal()
        del context.chat_data['int10_job']
    
    #M
    if 'int20_job' in context.chat_data:
        int20_job = context.chat_data['int20_job']
        int20_job.schedule_removal()
        del context.chat_data['int20_job']
    
    #N
    if 'int30_job' in context.chat_data:
        int30_job = context.chat_data['int30_job']
        int30_job.schedule_removal()
        del context.chat_data['int30_job']
    
  #O
    if 'int40_job' in context.chat_data:
        int40_job = context.chat_data['int40_job']
        int40_job.schedule_removal()
        del context.chat_data['int40_job']  
    
    #P
    if 'int50_job' in context.chat_data:
        int50_job = context.chat_data['int50_job']
        int50_job.schedule_removal()
        del context.chat_data['int50_job']
    update.message.reply_text('Pengiriman pesan otomatis dihentikan!')
stop_handler = CommandHandler('stop', stop)


def ambil_data_historis():
    url = "https://api.im2019.com/api/game/guess_odd?page=1&limit=50"
    headers = {
        "Host": "api.im2019.com",
        "sec-ch-ua": "\"Not;A-Brand\";v=\"99\", \"Chromium\";v=\"90\"",
        "accept": "application/json, text/plain, */*",
        "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkuaW0yMDE5LmNvbSIsImF1ZCI6ImFwaS5pbTIwMTkuY29tIiwiaWF0IjoxNjgzOTUxNjQwLCJuYmYiOjE2ODM5NTE2NDAsImV4cCI6MTY4NDU1NjQ0MCwianRpIjp7ImlkIjoxNjgyODk2LCJ0eXBlIjoidXNlciJ9fQ.06mmq-9K1c68QFH8MuigaIDleXUKW1TMR70TBxaalYs",
        "sec-ch-ua-mobile": "?0",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://www.im2021.com/",
        "accept-language": "en-US,en;q=0.9",
    }
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    angka_yang_akan_keluar = []
    for item in data['data']:
        angka_yang_akan_keluar.append(item['number'])
    return angka_yang_akan_keluar

def ambil_data_analisis():
    url = "https://api.im2019.com/api/game/guess_odd?page=1&limit=50"
    headers = {
        "Host": "api.im2019.com",
        "sec-ch-ua": "\"Not;A-Brand\";v=\"99\", \"Chromium\";v=\"90\"",
        "accept": "application/json, text/plain, */*",
        "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkuaW0yMDE5LmNvbSIsImF1ZCI6ImFwaS5pbTIwMTkuY29tIiwiaWF0IjoxNjgzOTUxNjQwLCJuYmYiOjE2ODM5NTE2NDAsImV4cCI6MTY4NDU1NjQ0MCwianRpIjp7ImlkIjoxNjgyODk2LCJ0eXBlIjoidXNlciJ9fQ.06mmq-9K1c68QFH8MuigaIDleXUKW1TMR70TBxaalYs",
        "sec-ch-ua-mobile": "?0",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://www.im2021.com/",
        "accept-language": "en-US,en;q=0.9",
    }
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    angka_yang_akan_keluar = []
    for item in data['data']:
        angka_yang_akan_keluar.append(item['number'])
    return angka_yang_akan_keluar

#A
def format_data_historis(data):
    pesan = ""  # Inisialisasi variabel pesan
    my_datetime = datetime.datetime.now()
    for _ in range(6):
        
        pesan += f"============Urutan 1-10 ==========\n\n"
        pesan += f"{my_datetime.strftime('[%Y-%m-%d] [%H:%M]_[%S]')}\n\n"
        total_genap_1_10 = sum(num for num in data[:10] if num % 2 == 0)
        rata_genap_1_10 = total_genap_1_10 / 6
        pesan += f"Genap = {total_genap_1_10} : 6 = {rata_genap_1_10:.2f}\n"
        total_ganjil_1_10 = sum(num for num in data[:10] if num % 2 != 0)
        rata_ganjil_1_10 = total_ganjil_1_10 / 4
        pesan += f"Ganjil = {total_ganjil_1_10} : 4 = {rata_ganjil_1_10:.2f}\n"
        rata_semua_1_10 = sum(data[:10]) / 10
        pesan += f"Rata-rata = {sum(data[:10])} : 10 = {rata_semua_1_10:.2f}\n"
        pesan += "====\n"
        pesan += f"Yang keluar = [{data[-1]}]  \n"
        pesan += "1-5 = " + ", ".join(str(num) for num in data[:5]) + "\n"
        rata_data_1_5 = sum(data[:5]) / 5
        pesan += f"Rata-rata = {sum(data[:5])} : 5 = {rata_data_1_5:.1f}\n"
        pesan += "====\n"
        pesan += f"Yang keluar = [{data[4]}]    \n"
        pesan += "6-10 = " + ", ".join(str(num) for num in data[5:10]) + " \n"
        rata_data_6_10 = sum(data[5:10]) / 5
        pesan += f"Rata-rata = {sum(data[5:10])} : 5 = {rata_data_6_10:.1f}\n\n"
        pesan += "================================\n"
        pesan += f"=============Urutan 11-20 ========\n\n"
        pesan += f"{(my_datetime - datetime.timedelta(minutes=20)).strftime('[%Y-%m-%d] [%H:%M]_[%S]')}\n\n"
        total_genap_11_20 = sum(num for num in data[10:20] if num % 2 == 0)
        rata_genap_11_20 = total_genap_11_20 / 6
        pesan += f"Genap = {total_genap_11_20} : 6 = {rata_genap_11_20:.2f}\n"
        total_ganjil_11_20 = sum(num for num in data[10:20] if num % 2 != 0)
        rata_ganjil_11_20 = total_ganjil_11_20 / 4
        pesan += f"Ganjil = {total_ganjil_11_20} : 4 = {rata_ganjil_11_20:.2f}\n"
        rata_semua_11_20 = sum(data[10:20]) / 10
        pesan += f"Rata-rata = {sum(data[10:20])} : 10 = {rata_semua_11_20:.2f}\n"
        pesan += "====\n"
        pesan += f"Yang keluar = [{data[9]}]     \n"
        pesan += "11-15 = " + ", ".join(str(num) for num in data[10:15]) + "        \n"
        rata_data_11_15 = sum(data[10:15]) / 5
        pesan += f"Rata-rata = {sum(data[10:15])} : 5 = {rata_data_11_15:.1f}\n"
        pesan += "====\n"
        pesan += f"Yang keluar = [{data[14]}]   \n"
        pesan += "16-20 = " + ", ".join(str(num) for num in data[15:20]) + "       \n"
        rata_data_16_20 = sum(data[15:20]) / 5
        pesan += f"Rata-rata = {sum(data[15:20])} : 5 = {rata_data_16_20:.1f}\n\n"
        pesan += "================================\n"
        pesan += f"===========Urutan 21-30 ==========\n\n"
        pesan += f"{(my_datetime - datetime.timedelta(minutes=40)).strftime('[%Y-%m-%d] [%H:%M]_[%S]')}\n\n"
        total_genap_21_30 = sum(num for num in data[20:30] if num % 2 == 0)
        rata_genap_21_30 = total_genap_21_30 / 6
        pesan += f"Genap = {total_genap_21_30} : 6 = {rata_genap_21_30:.2f}\n"
        total_ganjil_21_30 = sum(num for num in data[20:30] if num % 2 != 0)
        rata_ganjil_21_30 = total_ganjil_21_30 / 4
        pesan += f"Ganjil = {total_ganjil_21_30} : 4 = {rata_ganjil_21_30:.2f}\n"
        rata_semua_21_30 = sum(data[20:30]) / 10
        pesan += f"Rata-rata = {sum(data[20:30])} : 10 = {rata_semua_21_30:.2f}\n"
        pesan += "====\n"
        pesan += f"Yang keluar = [{data[19]}]     \n"
        pesan += "21-25 = " + ", ".join(str(num) for num in data[20:25]) + "        ðŸ‘ˆðŸ‘ˆðŸ‘ˆ\n"
        rata_data_21_25 = sum(data[20:25]) / 5
        pesan += f"Rata-rata = {sum(data[20:25])} : 5 = {rata_data_21_25:.1f}\n"
        pesan += "====\n"
        pesan += f"Yang keluar = [{data[24]}]    \n"
        pesan += "26-30 = " + ", ".join(str(num) for num in data[25:30]) + "        \n"
        rata_data_26_30 = sum(data[25:30]) / 5
        pesan += f"Rata-rata = {sum(data[25:30])} : 5 = {rata_data_26_30:.1f}\n\n"
        pesan += "================================\n"
        pesan += f"===========Urutan 31-40 ==========\n\n"
        pesan += f"{(my_datetime - datetime.timedelta(minutes=60)).strftime('[%Y-%m-%d] [%H:%M]_[%S]')}\n"
        total_genap_31_40 = sum(num for num in data[30:40] if num % 2 == 0)
        rata_genap_31_40 = total_genap_31_40 / 6
        pesan += f"Genap = {total_genap_31_40} : 6 = {rata_genap_31_40:.2f}\n"
        total_ganjil_31_40 = sum(num for num in data[30:40] if num % 2 != 0)
        rata_ganjil_31_40 = total_ganjil_31_40 / 4
        pesan += f"Ganjil = {total_ganjil_31_40} : 4 = {rata_ganjil_31_40:.2f}\n"
        rata_semua_31_40 = sum(data[30:40]) / 10
        pesan += f"Rata-rata = {sum(data[30:40])} : 10 = {rata_semua_31_40:.2f}\n"
        pesan += "====\n"
        pesan += f"Yang keluar = [{data[29]}]    \n"
        pesan += "31-35 = " + ", ".join(str(num) for num in data[30:35]) + "      \n"
        rata_data_31_35 = sum(data[30:35]) / 5
        pesan += f"Rata-rata = {sum(data[30:35])} : 5 = {rata_data_31_35:.1f}\n"
        pesan += "====\n"
        pesan += f"Yang keluar = [{data[34]}]\n"
        pesan += "36-40 = " + ", ".join(str(num) for num in data[35:40]) + "\n"
        rata_data_36_40 = sum(data[35:40]) / 5
        pesan += f"Rata-rata = {sum(data[35:40])} : 5 = {rata_data_36_40:.1f}\n\n"
        pesan += "================================\n"
        pesan += f"==========Urutan 41-50 ===========\n\n"
        pesan += f"{(my_datetime - datetime.timedelta(minutes=80)).strftime('[%Y-%m-%d] [%H:%M]_[%S]')}\n\n"
        total_genap_41_50 = sum(num for num in data[40:50] if num % 2 == 0)
        rata_genap_41_50 = total_genap_41_50 / 6
        pesan += f"Genap = {total_genap_41_50} : 6 = {rata_genap_41_50:.2f}\n"
        total_ganjil_41_50 = sum(num for num in data[40:50] if num % 2 != 0)
        rata_ganjil_41_50 = total_ganjil_41_50 / 4
        pesan += f"Ganjil = {total_ganjil_41_50} : 4 = {rata_ganjil_41_50:.2f}\n"
        rata_semua_41_50 = sum(data[40:50]) / 10
        pesan += f"Rata-rata = {sum(data[40:50])} : 10 = {rata_semua_41_50:.2f}\n"
        pesan += "====\n"
        pesan += f"Yang keluar = [{data[39]}]     \n"
        pesan += "41-45 = " + ", ".join(str(num) for num in data[40:45]) + "\n"
        rata_data_41_45 = sum(data[40:45]) / 5
        pesan += f"Rata-rata = {sum(data[40:45])} : 5 = {rata_data_41_45:.1f}\n"
        pesan += "====\n"
        pesan += f"Yang keluar = [{data[44]}]\n"
        pesan += "46-50 = " + ", ".join(str(num) for num in data[45:50]) + "\n"
        rata_data_46_50 = sum(data[45:50]) / 5
        pesan += f"Rata-rata = {sum(data[45:50])} : 5 = {rata_data_46_50:.1f}\n\n"
        pesan += "================================\n"
        pesan += "===========Urutan 1-50===========\n\n"
        pesan += "Ganjil\n"
        total_ganjil_1_50 = sum(num for num in data[:50] if num % 2 != 0)
        rata_ganjil_1_50 = total_ganjil_1_50 / len(data[:50])
        pesan += f"Total ganjil 1-50 = {total_ganjil_1_50}\n"
        pesan += f"Rata-rata ganjil 1-50 = {total_ganjil_1_50} : {len(data[:50])} = {rata_ganjil_1_50:.2f}\n"
        pesan += "====\n"
        pesan += "Genap\n"
        total_genap_1_50 = sum(num for num in data[:50] if num % 2 == 0)
        rata_genap_1_50 = total_genap_1_50 / len(data[:50])
        pesan += f"Total genap 1-50 = {total_genap_1_50}\n"
        pesan += f"Rata-rata genap 1-50 = {total_genap_1_50} : {len(data[:50])} = {rata_genap_1_50:.2f}\n"
        pesan += "====\n"
        rata_semua_1_50 = sum(data[:50]) / len(data[:50])
        pesan += f"Rata-rata 1-50 = {sum(data[:50])} : {len(data[:50])} = {rata_semua_1_50:.2f}\n\n"
        pesan += "================================\n\n"
        pesan += "Urutan angka 1-50 yang keluar dari website\n"
        pesan += "====\n"
        pesan += f"prediksi 2 = {data[-2]}\n"
        pesan += "====\n"
        pesan += f"prediksi 1 = {data[-1]}\n"
        pesan += "====\n"
        pesan += f"Angka Terbaru = {data[0]}\n"
        pesan += "====\n"
        pesan += ", ".join(str(num) for num in data[:50])
        pesan += "\n====\n"
        pesan += f"Angka Terakhir = {data[49]}\n"
        pesan += "\n"
        pesan += "================================\n"
        pesan += f"/menu     /stop     /historis\n"
        pesan += f"                                                                 {(my_datetime - datetime.timedelta(minutes=0)).strftime('%S')}\n"
        return pesan
    
def format_data_analisis(data):
    pesan = ""  # Inisialisasi variabel pesan
    my_datetime = datetime.datetime.now()
    for _ in range(1):
        pesan += f"[{data[0]}]                      /stop  /menu.   {(my_datetime - datetime.timedelta(minutes=0)).strftime('%S')}\n "
                                                            
        
    return pesan
    
#C
def format_data_int1(data):
    pesan = ""  # Inisialisasi variabel pesan
    my_datetime = datetime.datetime.now()
    for _ in range(1):
        
        pesan += f"[{data[0]}] = [{data[1]}]    /stop    /menu \n"
        pesan += f"                                                                 {(my_datetime - datetime.timedelta(minutes=0)).strftime('%S')}\n"
        
    return pesan
   
#D
def format_data_int2(data):
    pesan = ""  # Inisialisasi variabel pesan
    my_datetime = datetime.datetime.now()
    for _ in range(1):
        pesan += f"[{data[0]}]= {data[1:3]}  \n/stop   /menu  \n"
        pesan += f"                                                                 {(my_datetime - datetime.timedelta(minutes=0)).strftime('%S')}\n"
        
    return pesan
    
#E
def format_data_int3(data):
    pesan = ""  # Inisialisasi variabel pesan
    my_datetime = datetime.datetime.now()
    for _ in range(1):
        pesan += f"[{data[0]}]= {data[1:4]}  /stop, /menu \n"
        pesan += f"                                                                 {(my_datetime - datetime.timedelta(minutes=0)).strftime('%S')}\n"
        
    return pesan

#F
def format_data_int4(data):
    pesan = ""  # Inisialisasi variabel pesan
    my_datetime = datetime.datetime.now()
    for _ in range(1):
        pesan += f"[{data[0]}]= {data[1:5]}  /stop, /menu \n"
        pesan += f"                                                                 {(my_datetime - datetime.timedelta(minutes=0)).strftime('%S')}\n"
        
    return pesan

#G
def format_data_int5(data):
    pesan = ""  # Inisialisasi variabel pesan
    my_datetime = datetime.datetime.now()
    for _ in range(1):
        pesan += f"[{data[0]}]= {data[1:6]}  /stop, /menu \n"
        pesan += f"                                                                 {(my_datetime - datetime.timedelta(minutes=0)).strftime('%S')}\n"
        
    return pesan
    
#H
def format_data_int6(data):
    pesan = ""  # Inisialisasi variabel pesan
    my_datetime = datetime.datetime.now()
    for _ in range(1):
        pesan += f"[{data[0]}]= {data[1:7]}  /stop, /menu \n"
        pesan += f"                                                                 {(my_datetime - datetime.timedelta(minutes=0)).strftime('%S')}\n"
        
    return pesan
    
#I
def format_data_int7(data):
    pesan = ""  # Inisialisasi variabel pesan
    my_datetime = datetime.datetime.now()
    for _ in range(1):
        pesan += f"[{data[0]}]= {data[1:8]}  /stop, /menu \n"
        pesan += f"                                                                 {(my_datetime - datetime.timedelta(minutes=0)).strftime('%S')}\n"
        
    return pesan
    
#J
def format_data_int8(data):
    pesan = ""  # Inisialisasi variabel pesan
    my_datetime = datetime.datetime.now()
    for _ in range(1):
        pesan += f"[{data[0]}]= {data[1:9]}  /stop  /menu \n"
        pesan += f"                                                                 {(my_datetime - datetime.timedelta(minutes=0)).strftime('%S')}\n"
        
    return pesan
    
#K
def format_data_int9(data):
    pesan = ""  # Inisialisasi variabel pesan
    my_datetime = datetime.datetime.now()
    for _ in range(1):
        pesan += f"[{data[0]}]= {data[1:10]}  \n/stop  /menu \n"
        pesan += f"                                                                 {(my_datetime - datetime.timedelta(minutes=0)).strftime('%S')}\n"
        
    return pesan
    
#L
def format_data_int10(data):
    pesan = ""  # Inisialisasi variabel pesan
    my_datetime = datetime.datetime.now()
    for _ in range(1):
        pesan += f"[{data[0]}]= {data[1:11]}\n==\n/stop  /menu\n"
        pesan += f"                                                                 {(my_datetime - datetime.timedelta(minutes=0)).strftime('%S')}\n"
        
    return pesan
    
#M
def format_data_int20(data):
    pesan = ""  # Inisialisasi variabel pesan
    my_datetime = datetime.datetime.now()
    for _ in range(1):
        pesan += f"[{data[0]}]= {data[1:11]}\n==\n"
        pesan += f"{(my_datetime - datetime.timedelta(minutes=20)).strftime('%Y-%m-%d %H:%M')}\n"
        pesan += f"[{data[10]}]= {data[11:21]}\n==\n/stop  /menu\n"
        pesan += f"                                                                 {(my_datetime - datetime.timedelta(minutes=0)).strftime('%S')}\n"
        
    return pesan
    
#N
def format_data_int30(data):
    pesan = ""  # Inisialisasi variabel pesan
    my_datetime = datetime.datetime.now()
    for _ in range(1):
        pesan += f"[{data[0]}]= {data[1:11]}\n==\n"
        pesan += f"{(my_datetime - datetime.timedelta(minutes=20)).strftime('%Y-%m-%d %H:%M')}\n"
        pesan += f"[{data[10]}]= {data[11:21]}\n==\n"
        pesan += f"{(my_datetime - datetime.timedelta(minutes=40)).strftime('%Y-%m-%d %H:%M')}\n"
        pesan += f"[{data[20]}]= {data[21:31]}\n==\n/stop  /menu\n"
        pesan += f"Second = [{(my_datetime - datetime.timedelta(minutes=0)).strftime('%S')}]\n"
        
    return pesan
    
#O
def format_data_int40(data):
    pesan = ""  # Inisialisasi variabel pesan
    my_datetime = datetime.datetime.now()
    for _ in range(1):
        pesan += f"{(my_datetime - datetime.timedelta(minutes=0)).strftime('%Y-%m-%d %H:%M')}\n\n"
        pesan += f"[{data[0]}]\n"
        pesan += f"==\n{data[1:11]}\n\n"
        pesan += f"{(my_datetime - datetime.timedelta(minutes=20)).strftime('%Y-%m-%d %H:%M')}\n\n"
        pesan += f"[{data[10]}]\n"
        pesan += f"==\n{data[11:21]}\n\n"
        pesan += f"{(my_datetime - datetime.timedelta(minutes=40)).strftime('%Y-%m-%d %H:%M')}\n\n"
        pesan += f"[{data[20]}]\n"
        pesan += f"==\n{data[21:31]}\n\n"
        pesan += f"{(my_datetime - datetime.timedelta(minutes=60)).strftime('%Y-%m-%d %H:%M')}\n\n"
        pesan += f"[{data[30]}]\n"
        pesan += f"==\n{data[31:41]}\n\n"
        pesan += f"\n==/stop /menu {(my_datetime - datetime.timedelta(minutes=0)).strftime('%S')}\n"

    return pesan

    
#P
def format_data_int50(data):
    pesan = ""  # Inisialisasi variabel pesan
    my_datetime = datetime.datetime.now()
    for _ in range(1):
        pesan += f"[{data[0]}]           =          {(my_datetime - datetime.timedelta(minutes=0)).strftime('%Y-%m-%d %H:%M')}\n\n"
        pesan += f"==\n{data[1:11]}\n\n"
        pesan += f"[{data[10]}]           =          {(my_datetime - datetime.timedelta(minutes=20)).strftime('%Y-%m-%d %H:%M')}\n\n"
        pesan += f"==\n{data[11:21]}\n\n"
        pesan += f"[{data[20]}]           =          {(my_datetime - datetime.timedelta(minutes=40)).strftime('%Y-%m-%d %H:%M')}\n\n"
        pesan += f"==\n{data[21:31]}\n\n"
        pesan += f"[{data[30]}]           =          {(my_datetime - datetime.timedelta(minutes=60)).strftime('%Y-%m-%d %H:%M')}\n\n"
        pesan += f"==\n{data[31:41]}\n\n"
        pesan += f"[{data[40]}]           =          {(my_datetime - datetime.timedelta(minutes=80)).strftime('%Y-%m-%d %H:%M')}\n\n"
        pesan += f"==\n{data[41:51]}\n\n"
        pesan += f"\n==/stop /menu                          {(my_datetime - datetime.timedelta(minutes=80)).strftime('%S')}\n"
        
    return pesan
    
###5
#A
def send_historis(context):
    chat_id = context.job.context
    data_historis = ambil_data_historis()
    pesan = format_data_historis(data_historis)
    context.bot.send_message(chat_id=chat_id, text=pesan)
#B
def send_analisis(context):
    chat_id = context.job.context
    data_analisis = ambil_data_historis()
    pesan = format_data_analisis(data_analisis)
    context.bot.send_message(chat_id=chat_id, text=pesan)
#C
def send_int1(context):
    chat_id = context.job.context
    data_int1 = ambil_data_historis()
    pesan = format_data_int1(data_int1)
    context.bot.send_message(chat_id=chat_id, text=pesan)
#D
def send_int2(context):
    chat_id = context.job.context
    data_int2 = ambil_data_historis ()
    pesan = format_data_int2(data_int2)
    context.bot.send_message(chat_id=chat_id, text=pesan)
    
#E
def send_int3(context):
    chat_id = context.job.context
    data_int3 = ambil_data_historis ()
    pesan = format_data_int3(data_int3)
    context.bot.send_message(chat_id=chat_id, text=pesan)

#F
def send_int4(context):
    chat_id = context.job.context
    data_int4 = ambil_data_historis ()
    pesan = format_data_int4(data_int4)
    context.bot.send_message(chat_id=chat_id, text=pesan)

#G
def send_int5(context):
    chat_id = context.job.context
    data_int5 = ambil_data_historis ()
    pesan = format_data_int5(data_int5)
    context.bot.send_message(chat_id=chat_id, text=pesan)

#H
def send_int6(context):
    chat_id = context.job.context
    data_int6 = ambil_data_historis ()
    pesan = format_data_int6(data_int6)
    context.bot.send_message(chat_id=chat_id, text=pesan)

#I
def send_int7(context):
    chat_id = context.job.context
    data_int7 = ambil_data_historis ()
    pesan = format_data_int7(data_int7)
    context.bot.send_message(chat_id=chat_id, text=pesan)

#J
def send_int8(context):
    chat_id = context.job.context
    data_int8 = ambil_data_historis ()
    pesan = format_data_int8(data_int8)
    context.bot.send_message(chat_id=chat_id, text=pesan)

#K
def send_int9(context):
    chat_id = context.job.context
    data_int9 = ambil_data_historis ()
    pesan = format_data_int9(data_int9)
    context.bot.send_message(chat_id=chat_id, text=pesan)

#L
def send_int10(context):
    chat_id = context.job.context
    data_int10 = ambil_data_historis ()
    pesan = format_data_int10(data_int10)
    context.bot.send_message(chat_id=chat_id, text=pesan)

#M
def send_int20(context):
    chat_id = context.job.context
    data_int20 = ambil_data_historis ()
    pesan = format_data_int20(data_int20)
    context.bot.send_message(chat_id=chat_id, text=pesan)

#N
def send_int30(context):
    chat_id = context.job.context
    data_int30 = ambil_data_historis ()
    pesan = format_data_int30(data_int30)
    context.bot.send_message(chat_id=chat_id, text=pesan)

#O
def send_int40(context):
    chat_id = context.job.context
    data_int40 = ambil_data_historis ()
    pesan = format_data_int40(data_int40)
    context.bot.send_message(chat_id=chat_id, text=pesan)

#P
def send_int50(context):
    chat_id = context.job.context
    data_int50 = ambil_data_historis ()
    pesan = format_data_int50(data_int50)
    context.bot.send_message(chat_id=chat_id, text=pesan)
    
dispatcher.add_handler(menu_handler)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(historis_handler)
dispatcher.add_handler(analisis_handler)
#C
dispatcher.add_handler(int1_handler)
#D
dispatcher.add_handler(int2_handler)
#E
dispatcher.add_handler(int3_handler)
#F
dispatcher.add_handler(int4_handler)
#G
dispatcher.add_handler(int5_handler)
#H
dispatcher.add_handler(int6_handler)
#I
dispatcher.add_handler(int7_handler)
#J
dispatcher.add_handler(int8_handler)
#K
dispatcher.add_handler(int9_handler)
#L
dispatcher.add_handler(int10_handler)
#M
dispatcher.add_handler(int20_handler)
#N
dispatcher.add_handler(int30_handler)
#O
dispatcher.add_handler(int40_handler)
#P
dispatcher.add_handler(int50_handler)
dispatcher.add_handler(stop_handler)

# ...

def run_bot():
    logging.info("Bot is running.")
    updater.start_polling()

def run_as_daemon():
    while True:
        try:
            run_bot()
        except Exception as e:
            logging.error(f"Error occurred: {e}")
            time.sleep(5)

if __name__ == '__main__':
    run_as_daemon()
    	
