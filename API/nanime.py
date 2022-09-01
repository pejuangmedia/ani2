
from curses.ascii import alt
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import requests

class gogoanime():
    def __init__(self, query, animeid, episode_num):
        self.query = query
        self.animeid = animeid
        self.episode_num = episode_num

    # Cari Batch
    def get_search_results(query):
        try:
            url1 = f"https://t.me/s/downloadanimebatch?q={query}%20MAL"
            session = HTMLSession()
            response = session.get(url1)
            response_html = response.text
            soup = BeautifulSoup(response_html, 'html.parser')
            link = []
            title = []
            for i in soup.findAll("a"):
                if i.has_attr("class") and "tgme_widget_message_photo_wrap" in i["class"]:
                    link.append(i["href"])
            for i in soup.findAll("div", {"class": "tgme_widget_message_text js-message_text"}):
                    title.append(i.text.split("(")[1].split(")")[0])
            res_list_search = []
            if len(link)==len(title):
                for i in range(0, len(link)):
                    res_list_search.append({"name": title[i],"animeid": link[i]})
                #res_list_search.append({"name":f"{tit}","animeid":f"{r[2]}"})
            if res_list_search == []:
                return {"status":"204", "reason":"No search results found for the query"}
            else:
                return res_list_search
        except requests.exceptions.ConnectionError:
            return {"status":"404", "reason":"Check the host's network Connection"}

    #Cari Kuronime    
    def cari_kuronime(query):
        try:
            url1 = f"https://45.12.2.2/?s={query}"
            session = HTMLSession()
            response = session.get(url1)
            response_html = response.text
            soup = BeautifulSoup(response_html, 'html.parser')
            animes = soup.find("div", {"class": "listupd"}).find_all("a", title=True)
            res_list_search = []
            for anime in animes:
                tit = anime["title"]
                urll = anime["href"]
                r = urll.split('/')
                res_list_search.append({"name":f"{tit}","animeid":f"{r[-2]}"})
            if res_list_search == []:
                return {"status":"204", "reason":"No search results found for the query"}
            else:
                return res_list_search
        except requests.exceptions.ConnectionError:
            return {"status":"404", "reason":"Check the host's network Connection"}
    
    #Cari Meownime    
    def cari_meownime(query):
        try:
            url1 = f"https://meownime.ltd/?s={query}"
            session = HTMLSession()
            response = session.get(url1)
            response_html = response.text
            soup = BeautifulSoup(response_html, 'html.parser')
            animes = soup.find("div", {"class": "main-content-inner col-sm-12 col-md-8"}).find_all("a", title=True)
            res_list_search = []
            for anime in animes:
                tit = anime["title"]
                urll = anime["href"]
                r = urll.split('/')
                res_list_search.append({"name":f"{tit}","animeid":f"{urll}"})
            if res_list_search == []:
                return {"status":"204", "reason":"No search results found for the query"}
            else:
                return res_list_search
        except requests.exceptions.ConnectionError:
            return {"status":"404", "reason":"Check the host's network Connection"}
    
    #Cari Moenime    
    def cari_moenime(query):
        try:
            url1 = f"https://moenime.web.id/?s={query}"
            session = HTMLSession()
            response = session.get(url1)
            response_html = response.text
            soup = BeautifulSoup(response_html, 'html.parser')
            animes = soup.find("div", {"class": "main-content-inner  col-sm-12"}).find_all("a", rel="bookmark")
            res_list_search = []
            for anime in animes:
                tit = anime["title"]
                urll = anime["href"]
                r = urll.split('/')
                res_list_search.append({"name":f"{tit}","animeid":f"{urll}"})
            if res_list_search == []:
                return {"status":"204", "reason":"No search results found for the query"}
            else:
                return res_list_search
        except requests.exceptions.ConnectionError:
            return {"status":"404", "reason":"Check the host's network Connection"}

    
    #Cari gatsunime    
    def cari_gatsunime(query):
        try:
            url1 = f"https://gatsunime.my.id/?s={query}"
            session = HTMLSession()
            response = session.get(url1)
            response_html = response.text
            soup = BeautifulSoup(response_html, 'html.parser')
            animes = soup.find("div", {"class": "listupd"}).find_all("a", title=True)
            res_list_search = []
            for anime in animes:
                tit = anime["title"]
                urll = anime["href"]
                r = urll.split('/')
                res_list_search.append({"name":f"{tit}","animeid":f"{r[-2]}"})
            if res_list_search == []:
                return {"status":"204", "reason":"No search results found for the query"}
            else:
                return res_list_search
        except requests.exceptions.ConnectionError:
            return {"status":"404", "reason":"Check the host's network Connection"}

    def get_anime_details1(animeid):
        try:
            animelink = 'https://185.231.223.254/anime/{}'.format(animeid)
            response = requests.get(animelink)
            plainText = response.text
            soup = BeautifulSoup(plainText, "lxml")
            source_url = soup.find("div", {"class": "con"}).img
            imgg = source_url.get('src')
            tit_url = soup.find("h1").text
            #lis = soup.find_all('p', {"class": "type"}
            #plot_sum = lis[1]
            #pl = plot_sum.get_text().split(':')
            #pl.remove(pl[0])
            #sum = ""
            #plot_summary = sum.jsoin(pl)
            #type_of_show = lis[0].a['title']
            #ai = lis[2].find_all('a')
            #genres = []
#             for link in ai:
#                 genres.append(link.get('title'))
            #year1 = lis[3].get_text()
            #year2 = year1.split(" ")
            #year = year2[1]
            #status = lis[4].a.get_text()
            #oth_names = lis[5].get_text()
            #lnk = soup.find(id="episode_page")
            #ep_str = str(lnk.contents[-2])
            #a_tag = ep_str.split("\n")[-2]
            #a_tag_sliced = a_tag[:-4].split(">")
            #last_ep_range = a_tag_sliced[-1]
            #y = last_ep_range.split("-")
            #ep_num = y[-1]
            res_detail_search = {"title":f"{tit_url}", "image_url":f"{imgg}"}
            return res_detail_search
        except AttributeError:
            return {"status":"400", "reason":"Invalid animeid"}
        except requests.exceptions.ConnectionError:
            return {"status":"404", "reason":"Check the host's network Connection"}

    def get_anime_details(ids):
        try:
            animelink = 'https://185.231.223.254/{}'.format(ids)
            response = requests.get(animelink)
            plainText = response.text
            soup = BeautifulSoup(plainText, "lxml")
            source_url = soup.find("div", {"class": "item meta"}).img
            imgg = source_url.get('src')
            tit_url = soup.find("h1", {"class": "entry-title"}).text
            urldownload = soup.find("div", {"class", "soraurl"})
            res_detail_search = {"title":f"{tit_url}", "image_url":f"{imgg}", "linkdownload":f"{urldownload}"}
            return res_detail_search
        except AttributeError:
            return {"status":"400", "reason":"Invalid animeid"}
        except requests.exceptions.ConnectionError:
            return {"status":"404", "reason":"Check the host's network Connection"}

    def get_episodes_link(animeid, episode_num):
        try:
            animelink = f'https://nanimex.org/anime/{animeid}'
            response = requests.get(animelink)
            plainText = response.text
            soup = BeautifulSoup(plainText, "lxml")
            lnk = soup.find(id="episode_page")
            source_url = lnk.find("li").a
            tit_url = soup.find("h1").text
            URL_PATTERN = 'https://nanimex.org/episode/{}-episode-{}'
            url = URL_PATTERN.format(animeid, episode_num)
            srcCode = requests.get(url)
            plainText = srcCode.text
            soup = BeautifulSoup(plainText, "lxml")
            source_url = soup.find("li", {"class": "dowloads"}).a
            vidstream_link = source_url.get('href')
            URL = vidstream_link
            dowCode = requests.get(URL)
            data = dowCode.text
            soup = BeautifulSoup(data, "lxml")

            dow_url = []
            for i in range(11):
                try:
                    dow_url.append(soup.findAll('div', {'class': 'box-body episode_list'})[i].find('a'))
                except:
                    pass

            downloadlink = []
            qualityname = []
            for i in range(len(dow_url)):
                downloadlink.append(dow_url[i].get('href'))
                string = dow_url[i].string
                string_spl = string.split()
                string_spl.remove(string_spl[0])
                string_original = ''
                qualityname.append(string_original.join(string_spl))
            episode_res_link = {}
            for i in range(len(qualityname)):
                episode_res_link[qualityname[i]] = downloadlink[i]

            return episode_res_link

        except AttributeError:
            return {"status":"400", "reason":"Invalid animeid or episode_num"}
        except requests.exceptions.ConnectionError:
            return {"status":"404", "reason":"Check the host's network Connection"}

    def meownime():
        try:
            url = 'https://meownime.ltd/status/ongoing/'
            session = HTMLSession()
            response = session.get(url)
            response_html = response.text

            soup = BeautifulSoup(response_html, 'lxml')
            res_list_search =[]
            animes =  soup.find_all('img', alt=True)
            for anime in animes:
                tit = anime["title"]
                urll = anime["href"]
                res_list_search.append({"name":f"{tit}","Id-Epnum":f"{urll}"})
            if res_list_search == []:
                return {"status":"204", "reason":"I have No Idea what the fuck went wrong"}
            else:
                return res_list_search
        except requests.exceptions.ConnectionError:
            return {"status":"404", "reason":"Check the host's network Connection"}  

    def moenime():
        try:
            url = 'https://moenime.web.id/tag/ongoing/'
            session = HTMLSession()
            response = session.get(url)
            response_html = response.text

            soup = BeautifulSoup(response_html, 'lxml')
            res_list_search =[]
            animes =  soup.find("div", {"class": "main-content-inner  col-sm-12"}).find_all("a", rel="bookmark")
            for anime in animes:
                tit = anime["title"]
                urll = anime["href"]
                res_list_search.append({"name":f"{tit}","Id-Epnum":f"{urll}"})
            if res_list_search == []:
                return {"status":"204", "reason":"I have No Idea what the fuck went wrong"}
            else:
                return res_list_search
        except requests.exceptions.ConnectionError:
            return {"status":"404", "reason":"Check the host's network Connection"}  
        
    
    def gatsunime():
        try:
            url = 'https://gatsunime.my.id/'
            session = HTMLSession()
            response = session.get(url)
            response_html = response.text

            soup = BeautifulSoup(response_html, 'lxml')
            res_list_search =[]
            animes =  soup.find("div", {"class": "listupd"}).find_all("a", title=True)
            for anime in animes:
                tit = anime["title"]
                urll = anime["href"]
                res_list_search.append({"name":f"{tit}","Id-Epnum":f"{urll}"})
            if res_list_search == []:
                return {"status":"204", "reason":"I have No Idea what the fuck went wrong"}
            else:
                return res_list_search
        except requests.exceptions.ConnectionError:
            return {"status":"404", "reason":"Check the host's network Connection"}

    def kuronime():
        try:
            url = 'https://45.12.2.2/'
            session = HTMLSession()
            response = session.get(url)
            response_html = response.text

            soup = BeautifulSoup(response_html, 'lxml')
            res_list_search =[]
            animes =  soup.find("div", {"class": "listupd"}).find_all("a", title=True)
            for anime in animes:
                tit = anime["title"]
                urll = anime["href"]
                res_list_search.append({"name":f"{tit}","Id-Epnum":f"{urll}"})
            if res_list_search == []:
                return {"status":"204", "reason":"I have No Idea what the fuck went wrong"}
            else:
                return res_list_search
        except requests.exceptions.ConnectionError:
            return {"status":"404", "reason":"Check the host's network Connection"}

    def kuronimez():
        try:
            url = 'https://45.12.2.2/'
            session = HTMLSession()
            response = session.get(url)
            response_html = response.text

            soup = BeautifulSoup(response_html, 'lxml')
            res_list_search =[]
            for urljudul in soup.find("div", {"class": "listupd"}).find_all("a", title=True):
                urljudul.append(urljudul["href"])
            for judul in soup.find("div", {"class": "listupd"}).find_all("div", {"class": "bsuxtt"}):
                judul.append(judul)  
                res_list_search.append({"name":f"{judul}","Id-Epnum":f"{urljudul}"})
            if res_list_search == []:
                return {"status":"204", "reason":"I have No Idea what the fuck went wrong"}
            else:
                return res_list_search
        except requests.exceptions.ConnectionError:
            return {"status":"404", "reason":"Check the host's network Connection"}                 
    
    # LIST ANIME A
    def a_list():
        try:
            url = 'https://t.me/s/listbatch?q=daftar+isi%20[%20A%20]'
            session = HTMLSession()
            response = session.get(url)
            response_html = response.text

            soup = BeautifulSoup(response_html, 'lxml')
            res_list_search =[]
            animes =  soup.find("div", {"class": "tgme_widget_message_bubble"}).find_all("a", onclick=True)
            for anime in animes:
                tit = anime.text
                urll = anime["href"]
                res_list_search.append({"name":f"{tit}","Id-Epnum":f"{urll}"})
            if res_list_search == []:
                return {"status":"204", "reason":"I have No Idea what the fuck went wrong"}
            else:
                return res_list_search
        except requests.exceptions.ConnectionError:
            return {"status":"404", "reason":"Check the host's network Connection"}

    # LIST ANIME A - 01      
    def a_list1():
        try:
            url = 'https://t.me/s/listbatch?q=daftar%20anime%20a%20-%201'
            session = HTMLSession()
            response = session.get(url)
            response_html = response.text

            soup = BeautifulSoup(response_html, 'lxml')
            res_list_search =[]
            animes =  soup.find("div", {"class": "tgme_widget_message_bubble"}).find_all("a", onclick=True)
            for anime in animes:
                tit = anime.text
                urll = anime["href"]
                res_list_search.append({"name":f"{tit}","Id-Epnum":f"{urll}"})
            if res_list_search == []:
                return {"status":"204", "reason":"I have No Idea what the fuck went wrong"}
            else:
                return res_list_search
        except requests.exceptions.ConnectionError:
            return {"status":"404", "reason":"Check the host's network Connection"}        

    # LIST ANIME B
    def b_list1():
        try:
            url1 = 'https://t.me/s/downloadanimebatch?q=Daftar+Isi+%3A+%5B+B+%5D%20BANANA'
            session = HTMLSession()
            response = session.get(url1)
            response_html = response.text

            soup = BeautifulSoup(response_html, 'lxml')
            res_list_search =[]
            animes =  soup.find("div", {"class": "tgme_widget_message_bubble"}).find_all("a", onclick=True)
            for anime in animes:
                tit = anime.text
                urll = anime["href"]
                res_list_search.append({"name":f"{tit}","Id-Epnum":f"{urll}"})
            if res_list_search == []:
                return {"status":"204", "reason":"I have No Idea what the fuck went wrong"}
            else:
                return res_list_search
        except requests.exceptions.ConnectionError:
            return {"status":"404", "reason":"Check the host's network Connection"}        

        # Query kuronime
    def anime_episode(animeid):
        try:
            url1 = 'https://45.12.2.2/anime/{}'.format(animeid)
            session = HTMLSession()
            response = session.get(url1)
            response_html = response.text

            soup = BeautifulSoup(response_html, 'lxml')
            res_list_search =[]
            animes = soup.find("div", {"class": "bixbox bxcl"}).find_all("span", {"class": "lchx"})
            for anime in animes:
                tit = anime.text
                urll = anime.a['href']
                res_list_search.append({"name":f"{tit}","Id-Epnum":f"{urll}"})
            if res_list_search == []:
                return {"status":"204", "reason":"I have No Idea what the fuck went wrong"}
            else:
                return res_list_search
        except requests.exceptions.ConnectionError:
            return {"status":"404", "reason":"Check the host's network Connection"}   



    
    def jugad(animeid, episode_num):
        url = f"https://nanimex.org/episode/{animeid}-episode-{episode_num}"
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

        response = requests.get(url, headers=headers)
        plainText = response.text
        with open("test.html", "w", encoding="utf-8") as f:
            f.write(plainText)
        soup = BeautifulSoup(plainText, "lxml")
        links = soup.find("div", {"class":"anime_muti_link"}).find_all("li")
        result = {}
        for link in links:
            server = link.text
            server = server.replace("Choose this server", "")
            server = server.replace("\n", "")
            ep_url = link.a["data-video"]
            if ep_url.startswith("//"):
                ep_url = ep_url[2:]
            result[server] = ep_url
        return result 
    
    
    
