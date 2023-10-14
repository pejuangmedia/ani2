from telethon import events, Button
#from API.gogoanimeapi import gogoanime as gogo
from API.nanime import gogoanime as gogo
import Helper.formating_results as format
from config import bot
from Helper.helper_functions import *
from telethon.tl.types import InputUserSelf
from telethon.tl.types import InputUser
import random
 

class Anime():

    # Daftar list Anime
    @bot.on(events.NewMessage(pattern="/b_list", func=lambda e: e.is_private))
    async def event_handler_latest(event):
        a_list = gogo.a_list()
        (names, ids, epnums) = format.format_home_results(a_list)
        buttonss = []
        for i in range(len(names)):
            try:
                buttonss.append(
                    [Button.url(names[i], url=f"{ids[i]}")])
            except:
                pass
        await bot.send_message(
            event.chat_id,
            'Sekarang Kalian Bisa Mencari Daftar Urutan Anime file Via Bot.\nGunakan Perintah /list_(huruf/angka)_(nomor halaman) .\nSeperti ini : \n\nHuruf : /list_a_00\nAngka: /list_2_00 \n\nNOTE: Gunakan huruf kecil semua.',
            file='https://telegra.ph/file/162aee1681fcc7ff5b3b3.mp4'
            )

    # LIST ANIME A 
    @bot.on(events.NewMessage(pattern="/list_a_00"))
    async def event_handler_latest(event):
        a_list = gogo.a_list()
        (names, ids, epnums) = format.format_home_results(a_list)
        buttonss = []
        for i in range(len(names)):
            try:
                buttonss.append(
                    [Button.url(names[i], url=f"{ids[i]}")])
            except:
                pass
        await bot.send_message(
            event.chat_id,
            'Daftar Anime Berdasarkan Pencarian :\nGunakan perintah /list_(huruf/angka)_(nomor halaman) .  \nSeperti ini : \n\nHuruf : `/list_a_00` \nAngka: `/list_2_00` \n\nNOTE: Gunakan huruf kecil semua. ',
            buttons=buttonss
            )

    # LIST ANIME A 
    @bot.on(events.NewMessage(pattern="/list_a_01"))
    async def event_handler_latest(event):
        a_list1 = gogo.a_list1()
        (names, ids, epnums) = format.format_home_results(a_list1)
        buttonss = []
        for i in range(len(names)):
            try:
                buttonss.append(
                    [Button.url(names[i], url=f"{ids[i]}")])
            except:
                pass
        await bot.send_message(
            event.chat_id,
            'Daftar Anime Berdasarkan Pencarian :\nGunakan perintah /list_(huruf/angka)_(nomor halaman) .  \nSeperti ini : \n\nHuruf : `/list_a_00` \nAngka: `/list_2_00` \n\nNOTE: Gunakan huruf kecil semua. ',
            buttons=buttonss
            )        

    # LIST ANIME B        
    @bot.on(events.NewMessage(pattern="/b-list"))
    async def event_handler_latest(event):
        b_list1 = gogo.b_list1()
        (names, ids, epnums) = format.format_home_results(b_list1)
        buttonss = []
        for i in range(len(names)):
            try:
                buttonss.append(
                    [Button.url(names[i], url=f"{ids[i]}")])
            except:
                pass
        await bot.send_message(
            event.chat_id,
            'Daftar Anime Berdasarkan Pencarian :\nGunakan perintah /list_(huruf/angka)_(nomor halaman) .  \nSeperti ini : \n\nHuruf : `/list_a_00` \nAngka: `/list_2_00` \n\nNOTE: Gunakan huruf kecil semua. ',
            buttons=buttonss
            ) 
            

    #mencari kuronime
    @bot.on(events.NewMessage(pattern=r"^/kuronime|^/kuronime@cipdbot"))
    async def event_handler_anime(event):
        kuronime = gogo.kuronime()
        (names, ids, epnums) = format.format_home_results(kuronime)
        buttonss = [[], [Button.inline(
                    "Tutup", data=f"close_data")]]
        for i in range(len(names)):
            if len(names[i]) > 1:
                try:
                    buttonss.append(
                        [Button.url(names[i], url=f"{ids[i]}")])
                except:
                    pass
        if '/kuronime' == event.raw_text:
            await bot.send_message(
                event.chat_id,
                'Berikut Daftar Anime Terbaru Dari Sumber Kuronime:\nUntuk Mencari Anime Silahkan Gunakan Perintah `/kuronime judul anime`\n\n',
                 buttons=buttonss,
            )
        elif '/kuronime' in event.raw_text:
            text = event.raw_text.split()
            text.pop(0)
            anime_name = " ".join(text)
            cari_kuronime = gogo.cari_kuronime(anime_name)
            try:
                (names, ids) = format.format_search_results(cari_kuronime)
                buttons1 = [[], [Button.inline(
                    "Tutup", data=f"close_data")]]
                for i in range(len(names)):
                    if len(names[i]) > 40:
                        try:
                            buttons1.append([Button.inline(
                                f"{names[i][:20]}. . .{names[i][-20:]}", data=f"dets:{ids[i]}"), Button.inline(Check, f"!a {names[i]}", "switch_inline_query_current_chat")])
                        except:
                            bot.send_message(
                                event.chat_id,
                                "Name u searched for is too long",
                                file='https://media.giphy.com/media/4pk6ba2LUEMi4/giphy.gif'
                            )
                    else:
                        buttons1.append(
                            [Button.inline(names[i], data=f"dets:{ids[i]}")])

                await bot.send_message(
                    event.chat_id,
                    f'Hasil Yang Tersedia:\n\n',
                    buttons=buttons1)
            except:
                await bot.send_message(
                    event.chat_id,
                    'Not Found, Check for Typos or search Japanese name',
                    file='https://media.giphy.com/media/4pk6ba2LUEMi4/giphy.gif'
                )  

    #mencari meownime
    @bot.on(events.NewMessage(pattern=r"^/meownime|^/meownime@cipdbot"))
    async def event_handler_anime(event):
        meownime = gogo.meownime()
        (names, ids, epnums) = format.format_home_results(meownime)
        buttonss = [[], [Button.inline(
                    "Tutup", data=f"close_data")]]
        for i in range(len(names)):
            try:
                buttonss.append(
                    [Button.url(names[i], url=f"{ids[i]}"), Button.switch_inline('🔎', f"!a {names[i]}", "switch_inline_query_current_chat")])
            except:
                pass
        if '/meownime' == event.raw_text:
            await bot.send_message(
                event.chat_id,
                'Berikut Daftar Anime Terbaru Dari Sumber Meownime:\nUntuk Mencari Anime Silahkan Gunakan Perintah `/meownime judul anime`\n\n',
                 buttons=buttonss,
            )
        elif '/meownime' in event.raw_text:
            text = event.raw_text.split()
            text.pop(0)
            anime_name = " ".join(text)
            cari_meownime = gogo.cari_meownime(anime_name)
            try:
                (names, ids) = format.format_search_results(cari_meownime)
                buttons1 = [[], [Button.inline(
                    "Tutup", data=f"close_data")]]
                for i in range(len(names)):
                    if len(names[i]) > 55:
                        try:
                            buttons1.append([Button.url(
                                f"{names[i][:22]}. . .{names[i][-22:]}", url=f"split:{anime_name}:{ids[i]}"), Button.switch_inline('🔎', f"!a {names[i]}", "switch_inline_query_current_chat")])
                        except:
                            bot.send_message(
                                event.chat_id,
                                "Name u searched for is too long",
                                file='https://media.giphy.com/media/4pk6ba2LUEMi4/giphy.gif'
                            )
                    else:
                        buttons1.append(
                            [Button.url(names[i], url=f"{ids[i]}"), Button.switch_inline('🔎', f"!a {names[i]}", "switch_inline_query_current_chat")])

                await bot.send_message(
                    event.chat_id,
                    f'Hasil Yang Tersedia:\n\n',
                    buttons=buttons1)
            except:
                await bot.send_message(
                    event.chat_id,
                    'Not Found, Check for Typos or search Japanese name',
                    file='https://media.giphy.com/media/4pk6ba2LUEMi4/giphy.gif'
                )
    

    #mencari moenime
    @bot.on(events.NewMessage(pattern=r"^/moenime|^/moenime@cipdbot"))
    async def event_handler_anime(event):
        moenime = gogo.moenime()
        (names, ids, epnums) = format.format_home_results(meownime)
        buttonss = [[], [Button.inline(
                    "Tutup", data=f"close_data")]]
        for i in range(len(names)):
            try:
                buttonss.append(
                    [Button.url(names[i], url=f"{ids[i]}"), Button.switch_inline('🔎', f"!a {names[i]}", "switch_inline_query_current_chat")])
            except:
                pass
        if '/meownime' == event.raw_text:
            await bot.send_message(
                event.chat_id,
                'Berikut Daftar Anime Terbaru Dari Sumber Meownime:\nUntuk Mencari Anime Silahkan Gunakan Perintah `/moenime judul anime`\n\n',
                 buttons=buttonss,
            )
        elif '/meownime' in event.raw_text:
            text = event.raw_text.split()
            text.pop(0)
            anime_name = " ".join(text)
            cari_moenime = gogo.cari_moenime(anime_name)
            try:
                (names, ids) = format.format_search_results(cari_moenime)
                buttons1 = [[], [Button.inline(
                    "Tutup", data=f"close_data")]]
                for i in range(len(names)):
                    if len(names[i]) > 55:
                        try:
                            buttons1.append([Button.url(
                                f"{names[i][:22]}. . .{names[i][-22:]}", url=f"split:{anime_name}:{ids[i]}"), Button.switch_inline('🔎', f"!a {names[i]}", "switch_inline_query_current_chat")])
                        except:
                            bot.send_message(
                                event.chat_id,
                                "Name u searched for is too long",
                                file='https://media.giphy.com/media/4pk6ba2LUEMi4/giphy.gif'
                            )
                    else:
                        buttons1.append(
                            [Button.url(names[i], url=f"{ids[i]}"), Button.switch_inline('🔎', f"!a {names[i]}", "switch_inline_query_current_chat")])

                await bot.send_message(
                    event.chat_id,
                    f'Hasil Yang Tersedia:\n\n',
                    buttons=buttons1)
            except:
                await bot.send_message(
                    event.chat_id,
                    'Not Found, Check for Typos or search Japanese name',
                    file='https://media.giphy.com/media/4pk6ba2LUEMi4/giphy.gif'
                ) 

    #mencari meownime
    @bot.on(events.NewMessage(pattern=r"^/gatsunime|^/gatsunime@cipdbot"))
    async def event_handler_anime(event):
        gatsunime = gogo.gatsunime()
        (names, ids, epnums) = format.format_home_results(gatsunime)
        buttonss = [[], [Button.inline(
                    "Tutup", data=f"close_data")]]
        for i in range(len(names)):
            try:
                buttonss.append(
                    [Button.url(names[i], url=f"{ids[i]}")])
            except:
                pass
        if '/gatsunime' == event.raw_text:
            await bot.send_message(
                event.chat_id,
                'Berikut Daftar Anime Terbaru Dari Sumber Gatsunime:\nUntuk Mencari Anime Silahkan Gunakan Perintah `/gatsunime judul anime`\n\n',
                 buttons=buttonss,
            )
        elif '/gatsunime' in event.raw_text:
            text = event.raw_text.split()
            text.pop(0)
            anime_name = " ".join(text)
            cari_gatsunime = gogo.cari_gatsunime(anime_name)
            try:
                (names, ids) = format.format_search_results(cari_gatsunime)
                buttons1 = [[], [Button.inline(
                    "Tutup", data=f"close_data")]]
                for i in range(len(names)):
                    if len(names[i]) > 55:
                        try:
                            buttons1.append([Button.inline(
                                f"{names[i][:20]}. . .{names[i][-20:]}", data=f"dets:{ids[i]}")])
                        except:
                            bot.send_message(
                                event.chat_id,
                                "Name u searched for is too long",
                                file='https://media.giphy.com/media/4pk6ba2LUEMi4/giphy.gif'
                            )
                    else:
                        buttons1.append(
                            [Button.inline(names[i], data=f"dets:{ids[i]}")])

                await bot.send_message(
                    event.chat_id,
                    f'Hasil Yang Tersedia:\n\n',
                    buttons=buttons1)
            except:
                await bot.send_message(
                    event.chat_id,
                    'Not Found, Check for Typos or search Japanese name',
                    file='https://media.giphy.com/media/4pk6ba2LUEMi4/giphy.gif'
                )

        
    @bot.on(events.NewMessage(pattern=r"^/file"))
    async def event_handler_anime(event):

        if '/file' == event.raw_text:
            await bot.send_message(
                event.chat_id,
                'Perintah harus digunakan seperti ini:\n/file <nama anime>\ncontoh: /file Dororo\n\n**Note:** Ketik Judul dengan benar, kalian juga bisa menambahkan genre, tag, tipe dll secara bersamaan.\nSeperti ini : `/file comedy romance harem movie`\nDan sebagiannya, Maksimal akan ditampilkan 20 Hasil dari yang terbaru.',
                file='https://telegra.ph/file/4972450b960f17a8e4abb.jpg',
                buttons=([Button.inline(
                    "Tutup", data=f"close_data")])
                
            )
        elif '/file@cipdbot' == event.raw_text:
            await bot.send_message(
                event.chat_id,
                'Perintah harus digunakan seperti ini:\n/file <nama anime>\ncontoh: /file Dororo\n\n**Note:** Ketik Judul dengan benar, kalian juga bisa menambahkan genre, tag, tipe dll secara bersamaan.\nSeperti ini : `/file comedy romance harem movie`\nDan sebagiannya, Maksimal akan ditampilkan 20 Hasil dari yang terbaru.',
                file='https://telegra.ph/file/4972450b960f17a8e4abb.jpg',
                
            )
        
        elif '/file' in event.raw_text:
            text = event.raw_text.split()
            text.pop(0)
            anime_name = " ".join(text)
            search_result = gogo.get_search_results(anime_name)
            try:
                (names, ids) = format.format_search_results(search_result)
                buttons1 = [[], [Button.inline(
                    "Tutup", data=f"close_data")]]
                buttons2 = [Button.inline(
                    "Download", data=f"Download")]
                for i in range(len(names)):
                    if len(names[i]) > 100:
                        try:
                            buttons1.append([Button.url(
                                f"{names[i][:22]}. . .{names[i][-22:]}", url=f"split:{anime_name}:{[i][-25:]}")])
                        except:
                            bot.send_message(
                                event.chat_id,
                                "Mohon maaf, gunakan kata kunci yang benar.",
                                file='https://media.giphy.com/media/4pk6ba2LUEMi4/giphy.gif'
                            )
                    else:
                        buttons1.append(
                            [Button.url(names[i], url=f"{ids[i]}"), Button.switch_inline('🔎', f"!a {names[i]}", "switch_inline_query_current_chat")])
                            

                await bot.send_message(
                    event.chat_id,
                    'Hasil Pencarian Terkait Kata Kunci yang dicari:',
                    buttons=buttons1
                    )
            except:
                await bot.send_message(
                    event.chat_id,
                    'Tidak ditemukan kata kunci yang dicari.\n**Note:** Gunakan Kata Kunci yang jelas. atau anime tidak tersedia dichannel. Silahkan cari di channel @panimeid',
                    file='https://media.giphy.com/media/4pk6ba2LUEMi4/giphy.gif',
                )  

    @bot.on(events.NewMessage(pattern="/filep"))
    async def event_handler_file(event):
        if event.chat_id < 0:
            await event.reply("If you want to download in file contact me in pm\n@Anime_Gallery_Robot")
            return
        try:
            text = event.raw_text.split()
            text.pop(0)
            anime_name = " ".join(text)
            split_data = anime_name.split(":")
            if int(split_data[2]) - int(split_data[1]) > 15:
                await event.reply(
                    "file Download is capped at 15 episodes due to performance issues\nPlease download in filees of less than 15 for now"
                )

            else:
                for i in range(int(split_data[1]), (int(split_data[2]) + 1)):
                    if await send_download_link(event, split_data[0], i) == False:
                        break

        except:
            await event.reply("Something went wrong.....\nCheck if you entered command properly\n\nUse /help or go to \n@Anime_Gallery_Robot_Support if you have any doubts")

    @bot.on(events.NewMessage(pattern="/download"))
    async def event_handler_file(event):
        try:
            text = event.raw_text.split()
            text.pop(0)
            anime_name = " ".join(text)
            split_data = anime_name.split(":")
            if int(split_data[2]) - int(split_data[1]) > 100:
                await event.reply(
                    "file Download is capped at 100 episodes due to performance issues\nPlease download in filees of less than 100 for now"
                )
                return
            list_of_links = []
            await event.reply("Be Patient this is a slow process....")
            for i in range(int(split_data[1]), (int(split_data[2]) + 1)):
                list_of_links.append(gogo.get_episodes_link(split_data[0], i))
            format.file_download_txt(split_data[0], list_of_links)
            await bot.send_message(
                event.chat_id,
                "Import this file in **1DM** app.",
                file= f"{split_data[0]}.txt"

            )

        except:
            await event.reply("Something went wrong.....\nCheck if you entered command properly\n\nUse /help or go to \n@Anime_Gallery_Robot_Support if you have any doubts")         

    @bot.on(events.CallbackQuery(pattern=b"lt:"))
    async def callback_for_latest(event):
        data = event.data.decode('utf-8')
        split_data = data.split(":")
        animeid = split_data[-1]
        await send_details(event, animeid)

    @bot.on(events.CallbackQuery(pattern=b"Download"))
    async def callback_for_download(event):
        data = event.data.decode('utf-8')
        x = data.split(":")
        button2 = [[]]
        current_row = 0
        if int(float(x[2])) < 101:
            for i in range(int(float(x[2]))):
                button2[current_row].append(Button.inline(
                    str(i+1), data=f'ep:{i+1}:{x[1]}'))
                if (i+1) % 5 == 0:
                    button2.append([])
                    current_row = current_row + 1
            await event.edit(
                buttons=button2
            )
        else:
            num_of_buttons = (int(x[2]) // 100)
            for i in range(num_of_buttons):
                button2[current_row].append(Button.inline(
                    f'{i}01 - {i+1}00', data=f'btz:{i+1}00:{x[1]}'))
                if (i+1) % 3 == 0:
                    button2.append([])
                    current_row = current_row + 1
            if int(x[2]) % 100 == 0:
                pass
            else:
                button2[current_row].append(Button.inline(
                    f'{num_of_buttons}01 - {x[2]}', data=f'etz:{x[2]}:{x[1]}'))
            await event.edit(
                buttons=button2
            )

    @bot.on(events.CallbackQuery(pattern=b"longdl"))
    async def callback_for_download_long(event):
        data = event.data.decode('utf-8')
        x = data.split(":")
        button2 = [[]]
        current_row = 0
        search_results = gogo.get_search_results(x[1])
        (names, ids) = format.format_search_results(search_results)
        for i in ids:
            if i[-25:] == x[2]:
                id = i
                break
        for i in range(int(x[3])):
            button2[current_row].append(Button.inline(
                str(i+1), data=f'spp:{i+1}:{x[2]}:{x[1]}'))
            if (i+1) % 5 == 0:
                button2.append([])
                current_row = current_row + 1
        await event.edit(
            f'Choose Episode:',
            buttons=button2
        )

    @bot.on(events.CallbackQuery(pattern=b"btz:"))
    async def callback_for_choosebuttons(event):
        data = event.data.decode('utf-8')
        data_split = data.split(':')
        button3 = [[]]
        current_row = 0
        endnum = data_split[1]
        startnum = int(f'{int(endnum[0])-1}01')
        for i in range(startnum, (int(endnum)+1)):
            button3[current_row].append(Button.inline(
                str(i), data=f'ep:{i}:{data_split[2]}'))
            if i % 5 == 0:
                button3.append([])
                current_row = current_row + 1
        await event.edit(
            buttons=button3
        )

    @bot.on(events.CallbackQuery(pattern=b"etz:"))
    async def callback_for_choosebuttons1(event):
        data = event.data.decode('utf-8')
        data_split = data.split(':')
        button3 = [[]]
        current_row = 0
        endnum = int(data_split[1])
        startnum = int(f'{endnum//100}01')
        for i in range(startnum, (int(endnum)+1)):
            button3[current_row].append(Button.inline(
                str(i), data=f'ep:{i}:{data_split[2]}'))
            if i % 5 == 0:
                button3.append([])
                current_row = current_row + 1
        await event.edit(
            buttons=button3
        )

    @bot.on(events.CallbackQuery(pattern=b"ep:"))
    async def callback_for_downlink(event):
        data = event.data.decode('utf-8')
        try:
            data_split = data.split(':')
            await send_download_link(event, data_split[2], data_split[1])
        except:
            pass

    @bot.on(events.CallbackQuery(pattern=b"spp:"))
    async def callback_for_downlink_long(event):
        data = event.data.decode('utf-8')
        x = data.split(":")
        search_results = gogo.get_search_results(x[3])
        (names, ids) = format.format_search_results(search_results)
        for i in ids:
            if i[-25:] == x[2]:
                id = i
                break
        await send_download_link(event, id, x[1])

    @bot.on(events.CallbackQuery(pattern=b"dets:"))
    async def callback_for_details(event):
        data = event.data.decode('utf-8')
        x = data.split(":")
        await send_details(event, x[1])
    
    @bot.on(events.CallbackQuery(pattern=b"det:"))
    async def callback_for_details(event):
        data = event.data.decode('utf-8')
        x = data.split(":")
        await send_detailss(event, x[1])

    @bot.on(events.CallbackQuery(pattern=b"split:"))
    async def callback_for_details_long(event):
        data = event.data.decode('utf-8')
        await send_details(event, data)
