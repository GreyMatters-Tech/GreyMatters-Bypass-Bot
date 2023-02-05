from asyncio import get_event_loop, set_event_loop, new_event_loop, sleep
from base64 import b64decode
from contextlib import suppress
from math import ceil, floor
from secrets import choice
from time import time
from traceback import print_exc
from urllib.parse import unquote, urlparse, parse_qs
from requests import Session, head, session
from httpx import AsyncClient, ReadTimeout, Timeout
from re import compile as compiler
from re import DOTALL, findall, match, search, sub
from json import loads
from json.decoder import JSONDecodeError
from bs4 import BeautifulSoup
from pyrogram import Client, filters
from pyrogram.enums import MessageEntityType, ChatMemberStatus
from pyrogram.errors import RPCError, FloodWait, UserNotParticipant
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

pbot = Client(
    "bypasserbot",
    api_id=,
    api_hash="",
    bot_token="",
)
drivebuzz_crypt = ""
drivefire_crypt = ""
jiodrive_crypt = ""
gadrive_crypt = ""
kolop_crypt = ""
katdrive_crypt = ""
gdtot_crypt = ""
appdrive_email = ""
appdrive_password = ""
hubdrive_crypt = ""
sharerpw_xsrf_token = ""
sharerpw_laravel_session = ""
channel_id = -1001601615641
http = AsyncClient(http2=True, timeout=Timeout(10.0))
try:
    loop = get_event_loop()
except RuntimeError:
    set_event_loop(new_event_loop())
    loop = get_event_loop()

MAIN_REGEX = {
    r"https?://(gplinks\.co\/)\S+": ["gplinks", "gplinks_bypass"],
    r"https?://(try2link\.com\/)\S+": ["try2link", "try2link_bypass"],
    r"https?://(adf\.ly/)\S+": ["adfly", "adfly_bypass"],
    r"https?://(bit\.ly\/)\S+": ["bitly", "bitly_bypass"],
    r"https?://(ouo\.press\/)\S+": ["ouo", "ouo_bypass"],
    r"https?://(www\.shortly\.xyz\/)\S+": ["shortly", "shortly_bypass"],
    r"https?://(tinyurl\.com\/)\S+": ["tinyurl", "tinyurl_bypass"],
    r"https?://(thinfi\.com\/)\S+": ["thinfi", "thinfi_bypass"],
    r"https?://(hypershort\.com\/)\S+": ["hypershort", "hypershort_bypass"],
    r"https?://(safeurl\.sirigan\.my\.id/)\S+": ["sirigan", "sirigan_bypass"],
    r"https?://(gtlinks\.me\/)\S+": ["gtlinks", "gtlinks_bypass"],
    r"https?://(loan\.kinemaster\.cc\/\?token=)\S+":
        ["gtlinks", "gtlinks_bypass"],
    r"https?://(www\.theforyou\.in\/\?token=)\S+":
        ["theforyou", "gtlinks_bypass"],
    r"https?://(linkvertise\.com/)\S+": ["linkvertise", "linkvertise_bypass"],
    r"https?://(shorte|festyy|gestyy|corneey|destyy|ceesty)\.(st|com)\/\S+": [
        "shortest",
        "shortest_bypass",
    ],
    r"https?://(pkin\.me/)\S+": ["pkin", "pkin_bypass"],
    r"https?://(earn4link\.in/)\S+": ["earn4link", "shortner_type_two_bypass"],
    r"https?://(tekcrypt\.in/tek/)\S+":
        ["tekcrypt", "shortner_type_one_bypass"],
    r"https?://(link\.short2url\.in/)\S+":
        ["short2url", "shortner_type_one_bypass"],
    r"https?://(go\.rocklinks\.net/)\S+":
        ["rocklinks", "shortner_type_one_bypass"],
    r"https?://(rocklinks\.net/)\S+":
        ["rocklinks", "shortner_type_one_bypass"],
    r"https?://(earn\.moneykamalo\.com/)\S+": [
        "moneykamalo",
        "shortner_type_one_bypass",
    ],
    r"https?://(m\.easysky\.in/)\S+": ["easysky", "shortner_type_one_bypass"],
    r"https?://(indianshortner\.in/)\S+": [
        "indianshortner",
        "shortner_type_one_bypass",
    ],
    r"https?://(open\.crazyblog\.in/)\S+":
        ["crazyblog", "shortner_type_one_bypass"],
    r"https?://(link\.tnvalue\.in/)\S+":
        ["tnvalue", "shortner_type_one_bypass"],
    r"https?://(shortingly\.me/)\S+":
        ["shortingly", "shortner_type_one_bypass"],
    r"https?://(open2get\.in/)\S+": ["open2get", "shortner_type_two_bypass"],
    r"https?://(dulink\.in/)\S+": ["dulink", "shortner_type_one_bypass"],
    r"https?://(bindaaslinks\.com/)\S+":
        ["bindaaslinks", "shortner_type_one_bypass"],
    r"https?://(pdiskshortener\.com/)\S+": [
        "pdiskshortener",
        "shortner_type_one_bypass",
    ],
    r"https?://(mdiskshortner\.link/)\S+": [
        "mdiskshortner",
        "shortner_type_one_bypass",
    ],
    r"https?://(go\.earnl\.xyz/)\S+": ["earnl", "shortner_type_one_bypass"],
    r"https?://(g\.rewayatcafe\.com/)\S+":
        ["rewayatcafe", "shortner_type_one_bypass"],
    r"https?://(ser2\.crazyblog\.in/)\S+":
        ["crazyblog", "shortner_type_one_bypass"],
    r"https?://(bitshorten\.com/)\S+": [
        "bitshorten", "shortner_type_one_bypass"
    ],
    r"http?://(rocklink\.in/)\S+": ["rocklink", "shortner_type_one_bypass"],
    r"https?://(droplink\.co/)\S+": ["droplink", "shortner_type_two_bypass"],
    r"https?://(tnlink\.in\/)\S+": ["tnlink", "shortner_type_two_bypass"],
    r"https?://(ez4short\.com/)\S+": ["ez4short", "shortner_type_two_bypass"],
    r"https?://(xpshort\.com/)\S+": ["xpshort", "shortner_type_two_bypass"],
    r"http?://(vearnl\.in/)\S+": ["vearnl", "shortner_type_two_bypass"],
    r"https?://(adrinolinks\.in/)\S+": [
        "adrinolinks", "shortner_type_two_bypass"
    ],
    r"https?://(techymozo\.com/)\S+": [
        "techymozo", "shortner_type_two_bypass"
    ],
    r"https?://(urlsopen\.com/)\S+": ["urlopen", "shortner_type_two_bypass"],
    r"https?://(linkbnao\.com/)\S+": ["linkbnao", "shortner_type_two_bypass"],
    r"https?://(linksxyz\.in/)\S+": ["linksxyz", "shortner_type_two_bypass"],
    r"https?://(short\-jambo\.com/)\S+": [
        "short-jambo", "shortner_type_two_bypass"
    ],
    r"https?://(ads\.droplink\.co\.in/)\S+": [
        "droplink", "shortner_type_two_bypass"
    ],
    r"https?://(linkpays\.in/)\S+": ["linkpays", "shortner_type_two_bypass"],
    r"https?://(pi\-l\.ink/)\S+": ["pi-l", "shortner_type_two_bypass"],
    r"https?://(link\.tnlink\.in/)\S+": ["tnlink", "shortner_type_two_bypass"],
    r"https?://(anonfiles\.com)\S+": ["anonfiles", "anonfiles_bypass"],
    r"https?://(antfiles\.com\/\?dl\=)\S+": ["antfiles", "antfiles_bypass"],
    r"https?://(pjointe|dl4free|tenvoi|piecejointe|mesfichiers|desfichiers|megadl|dfichiers|alterupload|cjoint|1fichier|\.com/\?)\S+":
        [
            "1fichier",
            "fichier_bypass",
        ],
    r"https?://(gofile\.io\/d/)\S+": ["gofile", "gofile_bypass"],
    r"https?://(hxfile\.co/)\S+": ["hxfile", "hxfile_bypass"],
    r"https?://krakenfiles\.com/\S+": ["krakenfiles", "krakenfiles_bypass"],
    r"https?://(mdisk\.me\/convertor)\S+": ["mdisk", "mdisk_bypass"],
    r"https?://(www\.mediafire\.com\/download/)\S+": [
        "mediafire", "mediafire_bypass"
    ],
    r"https?://(pixeldrain\.com\/(l|u)\/)\S+": [
        "pixeldrain", "pixeldrain_bypass"
    ],
    r"https?://(racaty\.(net|io)/)\S+": ["racaty", "racaty_bypass"],
    r"https?://(send\.cm/)\S+": ["sendcm", "sendcm_bypass"],
    r"https?://(sfile\.mobi/)\S+": ["sfile", "sfile_bypass"],
    r"https?://(www\.solidfiles\.com/v/)\S+": [
        "solidfiles", "solidfiles_bypass"
    ],
    r"https?://(sourceforge\.net/)\S+": ["sourceforge", "sourceforge_bypass"],
    r"https?://(uploadbaz\.me/)\S+": ["uploadbaz", "uploadbaz_bypass"],
    r"https?://(www\.upload\.ee/)\S+": ["uploadee", "uploadee_bypass"],
    r"https?://(uppit\.com/)\S+": ["uppit", "uppit_bypass"],
    r"https?://(userscloud\.com/)\S+": ["userscloud", "userscloud_bypass"],
    r"https?://(we\.tl/)\S+": ["wetransfer", "wetransfer_bypass"],
    r"https?://(yadi.sk|disk.yandex.com)\S+": ["yandex", "yandex_bypass"],
    r"https?://www\d+\.zippyshare\.com/v/[^/]+/file\.html": [
        "zippyshare",
        "zippyshare_bypass",
    ],
    r"https?://(fembed|femax20|fcdn|feurl|naniplay|mm9842|layarkacaxxi|naniplay\.nanime|fembed\-hd)\.(com|net|stream|icu|in|biz)\S+":
        [
            "fembed",
            "fembed_bypass",
        ],
    r"https?://(www\.mp4upload\.com/)\S+": ["mp4upload", "mp4upload_bypass"],
    r"https?://(streamlare|sltube\.(com|org)\/v/)\S+": [
        "streamlare",
        "streamlare_bypass",
    ],
    r"https?://(watchsb|streamsb)\.(com|net)\/\S+": [
        "streamsb", "streamsb_bypass"
    ],
    r"https?://(streamtape\.(com|to|xyz)/)\S+": [
        "streamtape", "streamtape_bypass"
    ],
    r"https?://(anidrive|driveroot|driveflix|indidrive|drivehub|appdrive|driveapp|driveace|gdflix|drivelinks|drivebit|drivesharer|drivepro)\.\S+": [
        "appdrive", "appdrive_bypass"
    ],
    r"https?://(drivebuzz)\S+": ["drivebuzz", "drivebuzz_bypass"],
    r"https?://(drivefire)\S+": ["drivefire", "drivefire_bypass"],
    r"https?://(gadrive)\S+": ["gadrive", "gadrive_bypass"],
    r"https?://(jiodrive)\S+": ["jiodrive", "jiodrive_bypass"],
    r"https?://(katdrive)\S+": ["katdrive", "katdrive_bypass"],
    r"https?://(kolop)\S+": ["kolop", "kolop_bypass"],
    r"https?://(.+)\.gdtot\.(.+)\/\S+\/\S+": ["gdtot", "gdtot_bypass"],
    r"https?://(hubdrive)\S+": ["hubdrive", "hubdrive_bypass"],
    r"https?://(sharer\.pw\/file)\S+": ["sharerpw", "sharerpw_bypass"],
}


class Httpx:

    @staticmethod
    async def get(url: str, headers: dict = None, red: bool = True):
        async with AsyncClient() as ses:
            return await ses.get(url, headers=headers, follow_redirects=red, timeout=Timeout(10.0))


@pbot.on_message(filters.command("start") & filters.private)
async def start(_: pbot, m: Message):
    await m.reply_text("""
**Hey there i'm alive! I can bypass many URL Shortener website links**
You just need to send me the message containing the links! I will replace the un shorted link and send you back!
Do wait for 10 seconds for each link to process and bypass after sending the links!

**Support: @GreyMatter_Bots!**

**Subscribe: https://youtube.com/@GreyMattersYT**""")
    return


async def handle_force_sub(bot: Client, cmd: Message):
    try:
        user = await bot.get_chat_member(chat_id=channel_id,
                                         user_id=cmd.from_user.id)
        if user.status in (ChatMemberStatus.BANNED,
                           ChatMemberStatus.RESTRICTED):
            await cmd.reply_text(
                text=
                "Sorry, You are Banned to use me. Contact my [Support Group](https://t.me/greymatters_bots_discussion).",
                disable_web_page_preview=True,
            )
            return 0
    except UserNotParticipant:
        try:
            await cmd.reply_text(
                text="**Please Join My Updates Channel to use me!**\n\n"
                "Due to Overload, Only Channel Subscribers can use the Bot!",
                reply_markup=InlineKeyboardMarkup([
                    [
                        InlineKeyboardButton(
                            "🤖 Join Updates Channel",
                            url="t.me/GreyMatter_Bots",
                        )
                    ],
                ]),
            )
            return 0
        except RPCError as e:
            print(e.MESSAGE)
    except FloodWait as ee:
        await sleep(ee.value + 3)
        await cmd.reply_text("Try later flooded!")
        return 0
    except Exception:
        await cmd.reply_text(
            text=
            "Something went Wrong! Contact my [Support Group](https://t.me/greymatters_bots_discussion)",
            disable_web_page_preview=True,
        )
        return 0
    return 1


async def verifylink(url: str) -> int:
    return 1 if url and "//t.me/" not in url and url.startswith("https://") else 0


async def shourturl(url):
    client = cloudscraper.create_scraper(allow_brotli=False)
    DOMAIN = "https://short.url2go.in/RJOVAq30CU7lINo9AwG4oT3eISn7"
    url = url[:-1] if url[-1] == '/' else url
    code = url.split("/")[-1]
    final_url = f"{DOMAIN}/{code}"
    ref = "https://blog.textpage.xyz/"
    h = {"referer": ref}
    resp = client.get(final_url,headers=h)
    soup = BeautifulSoup(resp.content, "html.parser")
    inputs = soup.find_all("input")
    data = { input.get('name'): input.get('value') for input in inputs }
    h = { "x-requested-with": "XMLHttpRequest" }
    time.sleep(8)
    r = client.post(f"{DOMAIN}/links/go", data=data, headers=h)
    try:
        return r.json()['url']
    except: return "Something went wrong :("


async def sharerpw_bypass(url: str) -> str:
    client = Session()
    client.cookies["XSRF-TOKEN"] = sharerpw_xsrf_token
    client.cookies["laravel_session"] = sharerpw_laravel_session
    res = client.get(url)
    token = findall("_token\s=\s'(.*?)'", res.text, DOTALL)[0]
    data = {'_token': token, 'nl': 1}
    try:
        response = client.post(url + '/dl', headers={'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                                                     'x-requested-with': 'XMLHttpRequest'}, data=data).json()
        return response
    except:
        if response["message"] == "OK":
            return ""
        else:
            return response["message"]


async def account_login(client, url: str):
    data = {
        'email': appdrive_email,
        'password': appdrive_password,
    }
    client.post(f'https://{urlparse(url).netloc}/login', data=data)


async def gen_payload(data, boundary=f'{"-" * 6}_'):
    data_string = ''
    for item in data:
        data_string += f'{boundary}\r\n'
        data_string += f'Content-Disposition: form-data; name="{item}"\r\n\r\n{data[item]}\r\n'
    data_string += f'{boundary}--\r\n'
    return data_string


async def appdrive_lookalike(client, drive_link: str):
    try:
        response = client.get(drive_link).text
        soup = BeautifulSoup(response, "html.parser")
        new_drive_link = soup.find(class_="btn").get("href")
        return new_drive_link
    except:
        return drive_link


async def hubdrive_bypass(url: str) -> str:
    url = url[:-1] if url[-1] == '/' else url
    parsed_url = urlparse(url)
    client = Session()
    client.cookies.update({'crypt': hubdrive_crypt})
    req_url = f"{parsed_url.scheme}://{parsed_url.netloc}/ajax.php?ajax=download"
    try:
        res = client.post(req_url, headers={'x-requested-with': 'XMLHttpRequest'},
                          data={'id': url.split('/')[-1]}).json()[
            'file']
        gd_id = findall('gd=(.*)', res, DOTALL)[0]
    except:
        return ""

    return f"https://drive.google.com/open?id={gd_id}"


async def gdtot_bypass(url: str) -> str:
    url = url[:-1] if url[-1] == '/' else url
    client = Session()
    matc = findall(r"https?://(.+)\.gdtot\.(.+)\/\S+\/\S+", url)[0]
    client.cookies.update({"crypt": gdtot_crypt})
    response = client.get(f"https://{matc[0]}.gdtot.{matc[1]}/dld?id={url.split('/')[-1]}")
    url = findall(r'URL=(.*?)"', response.text)[0]
    params = parse_qs(urlparse(url).query)
    if "gd" not in params or not params["gd"] or params["gd"][0] == "false":
        return ""
    else:
        try:
            decoded_id = b64decode(str(params["gd"][0])).decode("utf-8")
        except:
            return ""
    return f"https://drive.google.com/open?id={decoded_id}"


async def appdrive_bypass(url: str) -> str:
    client = Session()
    client.headers.update({
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
    })

    url = client.get(url).url
    response = client.get(url)
    try:
        key = findall(r'"key",\s+"(.*?)"', response.text)[0]
        soup = BeautifulSoup(response.text, "html.parser")
        ddl_btn = soup.find(id="drc")
    except:
        return ""

    headers = {"Content-Type": f"multipart/form-data; boundary={'-' * 4}_"}
    data = {'type': 1, 'key': key, 'action': 'original'}

    if ddl_btn is not None:
        data['action'] = 'direct'
    else:
        await account_login(client, url)

    while data['type'] <= 3:
        try:
            response = client.post(url, data=await gen_payload(data), headers=headers).json();
            break
        except:
            data['type'] += 1

    if 'url' in response:
        drive_link = response["url"]
        if urlparse(url).netloc in (
                "driveapp.in", "drivehub.in", "gdflix.pro", "drivesharer.in", "drivebit.in", "drivelinks.in",
                "driveace.in",
                "drivepro.in", "gdflix.top"):
            return await appdrive_lookalike(client, drive_link)
        else:
            return drive_link

    elif 'error' in response and response['error']:
        return response['message']
    else:
        return ""


async def jiodrive_bypass(url: str) -> str:
    url = url[:-1] if url[-1] == '/' else url
    parsed_url = urlparse(url)
    client = Session()
    client.cookies.update({'crypt': jiodrive_crypt})
    req_url = f"{parsed_url.scheme}://{parsed_url.netloc}/ajax.php?ajax=download"
    try:
        res = client.post(req_url, headers={'x-requested-with': 'XMLHttpRequest'},
                        data={'id': url.split('/')[-1]}).json()[
                'file']
        gd_id = findall('gd=(.*)', res, DOTALL)[0]
    except:
        return ""

    drive_link = f"https://drive.google.com/open?id={gd_id}"
    return drive_link


async def kolop_bypass(url: str) -> str:
    url = url[:-1] if url[-1] == '/' else url
    parsed_url = urlparse(url)
    client = Session()
    client.cookies.update({'crypt': kolop_crypt})
    req_url = f"{parsed_url.scheme}://{parsed_url.netloc}/ajax.php?ajax=download"
    try:
        res = client.post(req_url, headers={'x-requested-with': 'XMLHttpRequest'},
                          data={'id': url.split('/')[-1]}).json()[
            'file']
        gd_id = findall('gd=(.*)', res, DOTALL)[0]
    except:
        return ""
    drive_link = f"https://drive.google.com/open?id={gd_id}"
    return drive_link


async def katdrive_bypass(url: str) -> str:
    url = url[:-1] if url[-1] == '/' else url
    parsed_url = urlparse(url)
    client = Session()
    client.cookies.update({'crypt': katdrive_crypt})
    req_url = f"{parsed_url.scheme}://{parsed_url.netloc}/ajax.php?ajax=download"
    try:
        res = client.post(req_url, headers={'x-requested-with': 'XMLHttpRequest'},
                        data={'id': url.split('/')[-1]}).json()[
                'file']
        gd_id = findall('gd=(.*)', res, DOTALL)[0]
    except:
        return ""

    drive_link = f"https://drive.google.com/open?id={gd_id}"
    return drive_link


async def gadrive_bypass(url: str) -> str:
    url = url[:-1] if url[-1] == '/' else url
    parsed_url = urlparse(url)
    client = Session()
    client.cookies.update({'crypt': gadrive_crypt})
    req_url = f"{parsed_url.scheme}://{parsed_url.netloc}/ajax.php?ajax=download"
    try:
        res = \
        client.post(req_url, headers={'x-requested-with': 'XMLHttpRequest'}, data={'id': url.split('/')[-1]}).json()[
            'file']
        gd_id = findall('gd=(.*)', res, DOTALL)[0]
    except:
        return ""
    drive_link = f"https://drive.google.com/open?id={gd_id}"
    return drive_link


async def drivefire_bypass(url: str) -> str:
    url = url[:-1] if url[-1] == '/' else url
    parsed_url = urlparse(url)
    client = Session()
    client.cookies.update({'crypt': drivefire_crypt})
    req_url = f"{parsed_url.scheme}://{parsed_url.netloc}/ajax.php?ajax=download"
    try:
        res = client.post(req_url, headers={'x-requested-with': 'XMLHttpRequest'},
                        data={'id': url.split('/')[-1]}).json()[
                'file']
        gd_id = res.rsplit("/", 1)[-1]
    except:
        return ""

    drive_link = f"https://drive.google.com/open?id={gd_id}"
    return drive_link


async def drivebuzz_bypass(url: str) -> str:
    url = url[:-1] if url[-1] == '/' else url
    parsed_url = urlparse(url)
    client = Session()
    client.cookies.update({'crypt': drivebuzz_crypt})
    req_url = f"{parsed_url.scheme}://{parsed_url.netloc}/ajax.php?ajax=download"
    try:
        res = client.post(req_url, headers={'x-requested-with': 'XMLHttpRequest'},
                        data={'id': url.split('/')[-1]}).json()[
                'file']
        gd_id = res.rsplit("=", 1)[-1]
    except:
        return ""

    drive_link = f"https://drive.google.com/open?id={gd_id}"
    return drive_link


async def anonfiles_bypass(anonfiles_url: str) -> str:
    soup = BeautifulSoup((await Httpx.get(anonfiles_url)).content,
                         "html.parser")
    return dlurl["href"] if (dlurl := soup.find(id="download-url")) else ""


async def antfiles_bypass(antfiles_url: str) -> str:
    soup = BeautifulSoup((await Httpx.get(antfiles_url)).content,
                         "html.parser")
    if a := soup.find(class_="main-btn", href=True):
        return "{0.scheme}://{0.netloc}/{1}".format(urlparse(antfiles_url),
                                                    a["href"])
    return ""


async def fichier_bypass(url: str) -> str:
    client = Session()
    response = client.get(url, timeout=5)
    soup = BeautifulSoup(response.text, "html.parser")
    data = {"adz": soup.find("input").get("value")}

    rate_limit = soup.find("div", {"class": "ct_warn"})
    if "you must wait" in str(rate_limit).lower():
        try:
            numbers = [
                int(word) for word in str(rate_limit).split()
                if word.isdigit()
            ]
            return f"1fichier.com is on limit for my ip. please wait {numbers[0]} min before trying again."
        except:
            return "1fichier.com is on limit for my ip. please wait few minutes/hour before trying again."

    else:
        r = client.post(url, json=data, timeout=5)
        soup = BeautifulSoup(r.text, "html.parser")
        return soup.find(class_="ok btn-general btn-orange").get("href")


async def krakenfiles_bypass(url: str) -> str:
    soup = BeautifulSoup((await Httpx.get(url)).content, "html.parser")
    token = soup.find("input", id="dl-token")["value"]
    hashes = [
        item["data-file-hash"]
        for item in soup.find_all("div", attrs={"data-file-hash": True})
    ]
    if not hashes:
        return ""
    dl_hash = hashes[0]
    payload = f'------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name="token"\r\n\r\n{token}\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--'
    headers = {
        "content-type":
            "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
        "cache-control": "no-cache",
        "hash": dl_hash,
    }
    dl_link_resp = session().post(
        f"https://krakenfiles.com/download/{hash}",
        data=payload,
        headers=headers,
        timeout=5,
    )
    dl_link_json = dl_link_resp.json()
    download_url = dl_link_json["url"]
    return download_url.replace(" ", "%20")


async def mdisk_bypass(url: str) -> str:
    url = url[:-1] if url[-1] == "/" else url
    token = url.split("/")[-1]
    api = f"https://diskuploader.entertainvideo.com/v1/file/cdnurl?param={token}"
    try:
        response = (await Httpx.get(api)).json()
    except JSONDecodeError:
        return ""
    return response["download"].replace(" ", "%20")


async def mediafire_bypass(mediafire_url: str) -> str:
    link = search(r"\bhttps?://.*mediafire\.com\S+", mediafire_url)[0]
    page = BeautifulSoup((await Httpx.get(link)).content, "html.parser")
    return page.find("a", {"aria-label": "Download file"}).get("href")


async def pixeldrain_bypass(pixeldrain_url: str) -> str:
    pixeldrain_url = (pixeldrain_url[:-1]
                      if pixeldrain_url[-1] == "/" else pixeldrain_url)
    file_id = pixeldrain_url.split("/")[-1]
    return (f"https://pixeldrain.com/api/list/{file_id}/zip"
            if pixeldrain_url.split("/")[-2] == "l" else
            f"https://pixeldrain.com/api/file/{file_id}")


async def racaty_bypass(url: str) -> str:
    client = Session()
    url = client.get(url, timeout=5).url
    url = url[:-1] if url[-1] == "/" else url
    token = url.split("/")[-1]
    headers = {
        "content-type":
            "application/x-www-form-urlencoded",
        "user-agent":
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    }
    data = {
        "op": "download2",
        "id": token,
        "rand": "",
        "referer": "",
        "method_free": "",
        "method_premium": "",
    }
    response = client.post(url, headers=headers, data=data, timeout=5)
    soup = BeautifulSoup(response.text, "html.parser")
    if btn := soup.find(class_="btn btn-dow"):
        return btn["href"]
    return unique["href"] if (unique := soup.find(
        id="uniqueExpirylink")) else ""


async def sendcm_bypass(url: str) -> str:
    base_url = "https://send.cm/"
    client = Session()
    headers = {
        "Content-Type":
            "application/x-www-form-urlencoded",
        "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
    }
    response = (await Httpx.get(url)).text
    soup = BeautifulSoup(response, "html.parser")
    inputs = soup.find_all("input")
    file_id = inputs[1]["value"]
    pars = {"op": "download2", "id": file_id, "referer": url}
    resp = client.post(base_url,
                       data=pars,
                       headers=headers,
                       allow_redirects=False,
                       timeout=5)
    return resp.headers["Location"]


async def sfile_bypass(url: str) -> str:
    headers = {
        "User-Agent":
            "Mozilla/5.0 (Linux; Android 8.0.1; SM-G532G Build/MMB29T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3239.83 Mobile Safari/537.36"
    }
    url = url[:-1] if url[-1] == "/" else url
    token = url.split("/")[-1]
    soup = BeautifulSoup(
        (await Httpx.get(f"https://sfile.mobi/download/{token}",
                         headers=headers)).content,
        "html.parser",
    )

    return soup.find("p").a.get("href")


async def solidfiles_bypass(solidfiles_url: str) -> str:
    json_file = search(r"'viewerOptions\'\,\ (.*?)\)\;",
                       (await Httpx.get(solidfiles_url)).text)[1]
    return loads(json_file)["downloadUrl"]


async def sourceforge_bypass(url: str) -> str:
    link = findall(r"\bhttps?://sourceforge\.net\S+", url)[0]
    file_path = findall(r"files(.*)/download", link)[0]
    project = findall(r"projects?/(.*?)/files", link)[0]
    mirrors = (f"https://sourceforge.net/settings/mirror_choices?"
               f"projectname={project}&filename={file_path}")
    page = BeautifulSoup((await Httpx.get(mirrors)).content, "html.parser")
    info = page.find("ul", {"id": "mirrorList"}).findAll("li")
    for mirror in info[1:]:
        return f'https://{mirror["id"]}.dl.sourceforge.net/project/{project}/{file_path}?viasf=1'
    return ""


async def uploadbaz_bypass(url: str) -> str:
    url = url[:-1] if url[-1] == "/" else url
    token = url.split("/")[-1]
    client = Session()
    headers = {
        "content-type":
            "application/x-www-form-urlencoded",
        "user-agent":
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    }
    data = {
        "op": "download2",
        "id": token,
        "rand": "",
        "referer": "",
        "method_free": "",
        "method_premium": "",
    }
    response = client.post(url,
                           headers=headers,
                           data=data,
                           allow_redirects=False,
                           timeout=5)
    return response.headers["Location"]


async def uploadee_bypass(url: str) -> str:
    soup = BeautifulSoup((await Httpx.get(url)).content, "html.parser")
    link = soup.find("a", attrs={"id": "d_l"})
    return link["href"]


async def uppit_bypass(url: str) -> str:
    url = url[:-1] if url[-1] == "/" else url
    token = url.split("/")[-1]
    client = Session()
    headers = {
        "content-type":
            "application/x-www-form-urlencoded",
        "user-agent":
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    }
    data = {
        "op": "download2",
        "id": token,
        "rand": "",
        "referer": "",
        "method_free": "",
        "method_premium": "",
    }
    response = client.post(url, headers=headers, data=data, timeout=5)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup.find(
        "span",
        {
            "style": "background:#f9f9f9;border:1px dotted #bbb;padding:7px;"
        },
    ).a.get("href")


async def userscloud_bypass(url: str) -> str:
    url = url[:-1] if url[-1] == "/" else url
    token = url.split("/")[-1]
    client = Session()
    headers = {
        "content-type":
            "application/x-www-form-urlencoded",
        "user-agent":
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    }
    data = {
        "op": "download2",
        "id": token,
        "rand": "",
        "referer": "",
        "method_free": "",
        "method_premium": "",
    }
    response = client.post(url,
                           headers=headers,
                           data=data,
                           allow_redirects=False,
                           timeout=5)
    return response.headers["Location"]


async def yandex_bypass(url: str) -> str:
    api = f"https://cloud-api.yandex.net/v1/disk/public/resources/download?public_key={url}"
    return (await Httpx.get(api)).json()["href"]


async def zippyshare_bypass(url: str) -> str:
    client = Session()
    response = client.get(url, timeout=5)
    if dlbutton := search(r'href = "([^"]+)" \+ \(([^)]+)\) \+ "([^"]+)',
                          response.text):
        folder, math_chall, filename = dlbutton.groups()
        math_chall = eval(math_chall)
        return f'{search("https?://[^/]+", response.url).group(0)}{folder}{math_chall}{filename}'

    soup = BeautifulSoup(response.content, "html.parser")
    if script := soup.find("script", text=compiler(r"(?si)\s*var a = \d+;")):
        sc = str(script)
        var = findall(r"var [ab] = (\d+)", sc)
        omg = findall(r"\.omg (!?=) [\"']([^\"']+)", sc)
        file = findall(r'"(/[^"]+)', sc)

        if var and omg:
            a, b = var
            if eval(f"{omg[0][1]!r} {omg[1][0]} {omg[1][1]!r}") or 1:
                a = ceil(int(a) // 3)
            else:
                a = floor(int(a) // 3)
            divider = int(findall(r"(\d+)%b", sc)[0])
            return search(r"(^https://www\d+.zippyshare.com)",
                          response.url).group(1) + "".join(
                [file[0],
                 str(a + (divider % int(b))), file[1]])
    return ""


async def fembed_bypass(url: str) -> str:
    url = url[:-1] if url[-1] == "/" else url
    token = url.split("/")[-1]
    return (
        await
        http.post(f"https://fembed-hd.com/api/source/{token}")).json()["data"]


async def mp4upload_bypass(url: str) -> str:
    url = url[:-1] if url[-1] == "/" else url
    headers = {"referer": "https://mp4upload.com"}
    token = url.split("/")[-1]
    data = {
        "op": "download2",
        "id": token,
        "rand": "",
        "referer": "https://www.mp4upload.com/",
        "method_free": "",
        "method_premium": "",
    }
    response = await http.post(url, headers=headers, data=data)
    return str({
        "bypassed_url": response.headers["Location"],
        "headers ": headers
    })


async def streamlare_bypass(url: str) -> str:
    CONTENT_ID = compiler(r"/[ve]/([^?#&/]+)")
    API_LINK = "https://sltube.org/api/video/download/get"
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4136.7 Safari/537.36"
    client = Session()
    content_id = CONTENT_ID.search(url).group(1)
    r = client.get(url, timeout=5).text
    soup = BeautifulSoup(r, "html.parser")
    csrf_token = soup.find("meta", {"name": "csrf-token"}).get("content")
    xsrf_token = client.cookies.get_dict()["XSRF-TOKEN"]
    headers = {
        "x-requested-with": "XMLHttpRequest",
        "x-csrf-token": csrf_token,
        "x-xsrf-token": xsrf_token,
        "referer": url,
        "user-agent": user_agent,
    }
    payload = {"id": content_id}
    result = client.post(API_LINK, headers=headers, data=payload,
                         timeout=5).json()["result"]
    result["headers"] = {"user-agent": user_agent}
    return result


async def rand_str():
    array = "abcdefghijklmnopqrstuvwqyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    return "".join([choice(array) for _ in range(12)])


async def hex_encode(string: str):
    return string.encode("utf-8").hex()


async def streamsb_bypass(url: str):
    url = url[:-1] if url[-1] == "/" else url
    if ".html" in url:
        url_id = url.split("/")[-1].split(".")[-2]
    else:
        url_id = url.split("/")[-1]
    part_one = f"{await rand_str()}||{url_id}||{await rand_str()}||streamsb"
    final_url = f"https://watchsb.com/sources48/{await hex_encode(part_one)}"
    headers = {
        "watchsb":
            "sbstream",
        "referer":
            "url",
        "user-agent":
            "Mozilla/5.0 (Linux; Android 11; 2201116PI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36",
    }
    return (await Httpx.get(final_url,
                            headers=headers)).json()["stream_data"]["file"]


async def streamtape_bypass(url: str) -> str:
    response = await Httpx.get(url)
    if videolink := findall(r"document.*((?=id\=)[^\"']+)", response.text):
        return f"https://streamtape.com/get_video?{videolink[-1]}"
    return ""


async def wetransfer_bypass(url: str) -> str:
    if url.startswith("https://we.tl/"):
        r = head(url, allow_redirects=True)
        url = r.url
    recipient_id = None
    params = urlparse(url).path.split("/")[2:]
    if len(params) == 2:
        transfer_id, security_hash = params
    elif len(params) == 3:
        transfer_id, recipient_id, security_hash = params
    else:
        return ""
    j = {
        "intent": "entire_transfer",
        "security_hash": security_hash,
    }
    if recipient_id:
        j["recipient_id"] = recipient_id
    s = Session()
    r = s.get("https://wetransfer.com/", timeout=5)
    m = search(r'name="csrf-token" content="([^"]+)"', r.text)
    s.headers.update({
        "x-csrf-token": m[1],
        "x-requested-with": "XMLHttpRequest"
    })
    r = s.post(
        f"https://wetransfer.com/api/v4/transfers/{transfer_id}/download",
        json=j,
        timeout=5,
    )
    j = r.json()
    return j["direct_link"]


async def gofile_bypass(url: str) -> str:
    api_uri = "https://api.gofile.io"
    url = url[:-1] if url[-1] == "/" else url
    client = Session()
    response = client.get(f"{api_uri}/createAccount", timeout=5).json()
    data = {
        "contentId": url.split("/")[-1],
        "token": response["data"]["token"],
        "websiteToken": 12345,
        "cache": "true",
    }
    response = client.get(f"{api_uri}/getContent", params=data,
                          timeout=5).json()
    for item in response["data"]["contents"].values():
        if download_url := item["link"]:
            return download_url
    return ""


async def hxfile_bypass(url: str) -> str:
    url = url[:-1] if url[-1] == "/" else url
    token = url.split("/")[-1]
    client = Session()
    headers = {
        "content-type":
            "application/x-www-form-urlencoded",
        "user-agent":
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    }

    data = {
        "op": "download2",
        "id": token,
        "rand": "",
        "referer": "",
        "method_free": "",
        "method_premium": "",
    }
    response = client.post(url, headers=headers, data=data, timeout=5)
    soup = BeautifulSoup(response.text, "html.parser")
    if btn := soup.find(class_="btn btn-dow"):
        return btn["href"]
    return unique["href"] if (unique := soup.find(
        id="uniqueExpirylink")) else ""


class BypasserNotFoundError(Exception):
    """
    Raise when there is no bypasser of the giver url.
    """


class UrlConnectionError(Exception):
    """
    Raise when response code of given url is not equal to 200
    """


class UnableToBypassError(Exception):
    """
    Raise when script is unable to bypass the given url.
    ( possible reason can be wrong link, wrong parameters or script is patched)
    """


async def redirect_function(url: str, bypasser_function: str):
    try:
        bypassed_value = await globals()[bypasser_function](url)
    except (JSONDecodeError, KeyError, ReadTimeout, TimeoutError):
        raise UnableToBypassError(
            "Can not bypass the given url. possible reason can be wrong link, wrong parameters or script is patched"
        )
    except Exception:
        print_exc()
        raise UnableToBypassError(
            "Can not bypass the given url. possible reason can be wrong link, wrong parameters or script is patched"
        )

    if not bypassed_value:
        raise UnableToBypassError(
            "Can not bypass the given url. possible reason can be wrong link, wrong parameters or script is patched"
        )
    return bypassed_value


async def decrypt_url(code: str):
    a, b = "", ""
    for i, item in enumerate(code):
        if i % 2 == 0:
            a += item
        else:
            b = item + b

    key = list(a + b)
    i = 0

    while i < len(key):
        if key[i].isdigit():
            for j in range(i + 1, len(key)):
                if key[j].isdigit():
                    u = int(key[i]) ^ int(key[j])
                    if u < 10:
                        key[i] = str(u)
                    i = j
                    break
        i += 1

    key = "".join(key)
    decrypted = b64decode(key)[16:-16]

    return decrypted.decode("utf-8")


async def adfly_bypass(ourl: str) -> str:
    res = (await Httpx.get(ourl)).text
    try:
        ysmm = findall(r"ysmm\s+=\s+['|\"](.*?)['|\"]", res)[0]
    except:
        return ""
    url = decrypt_url(ysmm)
    if search(r"go\.php\?u\=", url):
        url = b64decode(sub(r"(.*?)u=", "", url)).decode()
    elif "&dest=" in url:
        url = unquote(sub(r"(.*?)dest=", "", url))
    return url


async def bitly_bypass(bitly_url: str) -> str:
    return str((await Httpx.get(bitly_url)).url)


async def gtlinks_bypass(url: str) -> str:
    url = url[:-1] if url[-1] == "/" else url
    if "theforyou.in" not in url:
        url = str((await Httpx.get(url)).url)
    token = url.split("=")[-1]
    domain = "https://go.theforyou.in/"
    client = Session()
    response = client.get(domain + token,
                          headers={"referer": domain + token},
                          timeout=5)
    soup = BeautifulSoup(response.content, "html.parser")
    inputs = soup.find(id="go-link").find_all(name="input")
    data = {inp.get("name"): inp.get("value") for inp in inputs}
    await sleep(5)
    headers = {"x-requested-with": "XMLHttpRequest"}
    return client.post(f"{domain}links/go",
                       data=data,
                       headers=headers,
                       timeout=5).json()["url"]


async def hypershort_bypass(hypershort_url: str):
    client = Session()
    response = client.get(hypershort_url, timeout=5)
    soup = BeautifulSoup(response.content, "html.parser")
    token_response = client.get(
        "https://blog.miuiflash.com/links/createToken.js", timeout=5).text
    token_regex = search(r"itsToken\.value = \S+", token_response)
    if not token_regex:
        return ""
    token = token_regex[0].split("=")[1].removesuffix('"').removeprefix(' "')
    inputs = soup.find(id="re-form").find_all(name="input")
    data = {inp.get("name"): inp.get("value") for inp in inputs}["getData"]
    next_page_link = soup.find("form").get("action")
    resp = client.post(
        next_page_link,
        data={
            "itsToken": token,
            "get2Data": data
        },
        headers={"referer": next_page_link},
        timeout=5,
    )
    soup = BeautifulSoup(resp.content, "html.parser")
    await sleep(4)
    tokenize_url = soup.find(name="iframe", id="anonIt").get("src")
    tokenize_url_resp = client.get(tokenize_url)
    soup = BeautifulSoup(tokenize_url_resp.content, "html.parser")
    await sleep(3)
    inputs = soup.find(id="go-link").find_all(name="input")
    data = {inp.get("name"): inp.get("value") for inp in inputs}
    return client.post(
        "https://blog.miuiflash.com/blog/links/go",
        data=data,
        cookies=tokenize_url_resp.cookies,
        headers={
            "x-requested-with": "XMLHttpRequest",
            "referer": tokenize_url,
        },
        timeout=5,
    ).json()["url"]


async def linkvertise_bypass(url: str) -> str:
    linkvertise_bypassurl = f"https://bypass.pm/bypass2?url={url}"
    return (await
            Httpx.get(linkvertise_bypassurl)).json()["destination"]


async def recaptchav3(url: str):
    url_base = "https://www.google.com/recaptcha/"
    post_data = "v={}&reason=q&c={}&k={}&co={}"
    client = Session()
    client.headers.update(
        {"content-type": "application/x-www-form-urlencoded"})
    matches = findall(r"([api2|enterprise]+)\/anchor\?(.*)", url)[0]
    url_base += f"{matches[0]}/"
    params = matches[1]
    res = client.get(f"{url_base}anchor", params=params, timeout=5)
    token = findall(r'"recaptcha-token" value="(.*?)"', res.text)[0]
    params = dict(pair.split("=") for pair in params.split("&"))
    post_data = post_data.format(params["v"], token, params["k"], params["co"])
    res = client.post(f"{url_base}reload",
                      params=f'k={params["k"]}',
                      data=post_data,
                      timeout=5)
    return findall(r'"rresp","(.*?)"', res.text)[0]


async def ouo_bypass(url: str):
    client = Session()
    tempurl = url.replace("ouo.press", "ouo.io")
    p = urlparse(tempurl)
    idd = tempurl.split("/")[-1]
    res = client.get(tempurl, timeout=5)
    next_url = f"{p.scheme}://{p.hostname}/go/{idd}"
    for _ in range(2):
        if res.headers.get("Location"):
            break
        bs4 = BeautifulSoup(res.content, "html.parser")
        inputs = bs4.form.findAll("input", {"name": compiler(r"token$")})
        data = {inp.get("name"): inp.get("value") for inp in inputs}
        data["x-token"] = await recaptchav3(
            "https://www.google.com/recaptcha/api2/anchor?ar=1&k=6Lcr1ncUAAAAAH3cghg6cOTPGARa8adOf-y9zv2x&co=aHR0cHM6Ly9vdW8uaW86NDQz&hl=en&v=1B_yv3CBEV10KtI2HJ6eEXhJ&size=invisible&cb=4xnsug1vufyr")
        res = client.post(
            next_url,
            data=data,
            headers={"content-type": "application/x-www-form-urlencoded"},
            allow_redirects=False,
            timeout=5,
        )
        next_url = f"{p.scheme}://{p.hostname}/xreallcygo/{idd}"
    if res.headers.get("Location"):
        return str(res.headers.get("Location"))
    return ""


async def shortest_bypass(url: str) -> str:
    parsed_url = urlparse(url)
    client = Session()
    resp = client.get(url, headers={"referer": url}, timeout=5)
    session_id = findall(r"""sessionId(?:\s+)?:(?:\s+)?['|"](.*?)['|"]""",
                         resp.text)[0]
    final_url = f"{parsed_url.scheme}://{parsed_url.netloc}/shortest-url/end-adsession"
    params = {"adSessionId": session_id, "callback": "_"}
    await sleep(5)
    response = client.get(final_url,
                          params=params,
                          headers={"referer": url},
                          timeout=5)
    return findall('"(.*?)"', response.text)[1].replace(r"\/", "/")


async def shortly_bypass(shortly_url: str) -> str:
    shortly_url = shortly_url[:-1] if shortly_url[-1] == "/" else shortly_url
    token = shortly_url.split("/")[-1]
    shortly_bypass_api = "https://www.shortly.xyz/getlink.php/"
    return (await http.post(
        shortly_bypass_api,
        data={"id": token},
        headers={"referer": "https://www.shortly.xyz/link"},
    )).text


shortner_dict = {
    "https://tekcrypt.in/tek/": [
        r"https?://(tekcrypt\.in/tek/)\S+",
        "https://tekcrypt.in/tek/",
        20,
    ],
    "https://link.short2url.in/": [
        r"https?://(link\.short2url\.in/)\S+",
        "https://technemo.xyz/blog/",
        10,
    ],
    "https://go.rocklinks.net/": [
        r"https?://(go\.rocklinks\.net/)\S+",
        "https://dwnld.povathemes.com/",
        10,
    ],
    "https://rocklinks.net/": [
        r"https?://(rocklinks\.net/)\S+",
        "https://dwnld.povathemes.com/",
        10,
    ],
    "https://earn.moneykamalo.com/": [
        r"https?://(earn\.moneykamalo\.com/)\S+",
        "https://go.moneykamalo.com//",
        5,
    ],
    "https://m.easysky.in/": [
        r"https?://(m\.easysky\.in/)\S+",
        "https://techy.veganab.co/",
        5,
    ],
    "https://indianshortner.in/": [
        r"https?://(indianshortner\.in/)\S+",
        "https://indianshortner.com/",
        5,
    ],
    "https://open.crazyblog.in/": [
        r"https?://(open\.crazyblog\.in/)\S+",
        "https://hr.vikashmewada.com/",
        7,
    ],
    "https://link.tnvalue.in/": [
        r"https?://(link\.tnvalue\.in/)\S+",
        "https://internet.webhostingtips.club/",
        5,
    ],
    "https://shortingly.me/": [
        r"https?://(shortingly\.me/)\S+",
        "https://go.techyjeeshan.xyz/",
        5,
    ],
    "https://dulink.in/": [
        r"https?://(dulink\.in/)\S+",
        "https://tekcrypt.in/tek/",
        20,
    ],
    "https://bindaaslinks.com/": [
        r"https?://(bindaaslinks\.com/)\S+",
        "https://www.techishant.in/blog/",
        5,
    ],
    "https://pdiskshortener.com/": [
        r"https?://(pdiskshortener\.com/)\S+",
        "https://pdiskshortener.com/",
        10,
    ],
    "https://mdiskshortner.link/": [
        r"https?://(mdiskshortner\.link/)\S+",
        "https://mdiskshortner.link/",
        15,
    ],
    "http://go.earnl.xyz/": [
        r"https?://(go\.earnl\.xyz/)\S+",
        "https://v.earnl.xyz/",
        5,
    ],
    "https://g.rewayatcafe.com/": [
        r"https?://(g\.rewayatcafe\.com/)\S+",
        "https://course.rewayatcafe.com/",
        7,
    ],
    "https://ser2.crazyblog.in/": [
        r"https?://(ser2\.crazyblog\.in/)\S+",
        "https://ser3.crazyblog.in/",
        12,
    ],
    "http://rocklink.in/":
        [r"http?://(rocklink\.in/)\S+", "https://rocklink.in/", 6],
}


async def shortner_bypass(shortner_url: str,
                          domain: str,
                          sleep_time: int,
                          referer: str = "") -> str:
    shortner_url = shortner_url[:-1] if shortner_url[
                                            -1] == "/" else shortner_url
    token = shortner_url.split("/")[-1]
    client = Session()
    response = client.get(
        domain + token,
        headers={"referer": referer or domain + token},
        timeout=5,
    )
    soup = BeautifulSoup(response.content, "html.parser").find(id="go-link")
    if not soup:
        return ""
    inputs = soup.find_all(name="input")
    data = {inp.get("name"): inp.get("value") for inp in inputs}
    await sleep(sleep_time)
    headers = {"x-requested-with": "XMLHttpRequest"}
    return client.post(f"{domain}links/go",
                       data=data,
                       headers=headers,
                       timeout=5).json()["url"]


async def shortner_type_one_bypass(shortner_url: str) -> str:
    for (_, value) in shortner_dict.items():
        if bool(match(Rf"{value[0]}", shortner_url)):
            return await shortner_bypass(shortner_url=shortner_url,
                                         domain=value[1],
                                         sleep_time=value[2])
    return ""


shortner_dict2 = {
    "https://droplink.co/": [
        r"https?://(droplink\.co/)\S+",
        "https://droplink.co/",
        "https://yoshare.net",
        4,
    ],
    "https://tnlink.in/": [
        r"https?://(tnlink\.in\/)\S+",
        "https://gadgets.usanewstoday.club/",
        "https://usanewstoday.club/",
        9,
    ],
    "https://ez4short.com/nzcU": [
        r"https?://(ez4short\.com/)\S+",
        "https://ez4short.com/",
        "https://techmody.io/",
        5,
    ],
    "https://xpshort.com/": [
        r"https?://(xpshort\.com/)\S+",
        "https://push.bdnewsx.com/",
        "https://veganho.co/",
        10,
    ],
    "http://vearnl.in/": [
        r"http?://(vearnl\.in/)\S+",
        "https://go.urlearn.xyz/",
        "https://v.modmakers.xyz/",
        5,
    ],
    "https://adrinolinks.in/": [
        r"https?://(adrinolinks\.in/)\S+",
        "https://adrinolinks.in/",
        "https://wikitraveltips.com/",
        5,
    ],
    "https://techymozo.com/": [
        r"https?://(techymozo\.com/)\S+",
        "https://push.bdnewsx.com/",
        "https://veganho.co/",
        8,
    ],
    "https://linkbnao.com/": [
        r"https?://(linkbnao\.com/)\S+",
        "https://go.linkbnao.com/",
        "https://doibihar.org/",
        2,
    ],
    "https://linksxyz.in/": [
        r"https?://(linksxyz\.in/)\S+",
        "https://blogshangrila.com/insurance/",
        "https://cypherroot.com/",
        13,
    ],
    "https://short-jambo.com/": [
        r"https?://(short\-jambo\.com/)\S+",
        "https://short-jambo.com/",
        "https://aghtas.com/how-to-create-a-forex-trading-plan/",
        10,
    ],
    "https://ads.droplink.co.in/": [
        r"https?://(ads\.droplink\.co\.in/)\S+",
        "https://go.droplink.co.in/",
        "https://go.droplink.co.in/",
        5,
    ],
    "https://linkpays.in/": [
        r"https?://(linkpays\.in/)\S+",
        "https://m.techpoints.xyz//",
        "https://www.filmypoints.in/",
        10,
    ],
    "https://pi-l.ink/": [
        r"https?://(pi\-l\.ink/)\S+",
        "https://go.pilinks.net/",
        "https://poketoonworld.com/",
        5,
    ],
    "https://link.tnlink.in/": [
        r"https?://(link\.tnlink\.in/)\S+",
        "https://gadgets.usanewstoday.club/",
        "https://usanewstoday.club/",
        8,
    ],
    "https://earn4link.in/": [
        r"https?://(earn4link\.in/)\S+",
        "https://m.open2get.in/",
        "https://ezeviral.com/2022/03/01/why-is-cloud-hosting-the-ideal-solution/",
        3,
    ],
    "https://open2get.in/": [
        r"https?://(open2get\.in/)\S+",
        "https://m.open2get.in/",
        "https://ezeviral.com/2022/03/01/why-is-cloud-hosting-the-ideal-solution/",
        3,
    ],
}


async def shortner_type_two_bypass(shortner_url: str) -> str:
    for (_, value) in shortner_dict2.items():
        if bool(match(Rf"{value[0]}", shortner_url)):
            return await shortner_bypass(
                shortner_url=shortner_url,
                domain=value[1],
                referer=value[2],
                sleep_time=value[3],
            )
    return ""


async def sirigan_bypass(srigan_link: str) -> str:
    client = Session()
    response = client.get(srigan_link, timeout=5)
    url = response.url.split("=", maxsplit=1)[-1]
    url = b64decode(url).decode("utf-8")
    while 1:
        try:
            url = b64decode(url).decode("utf-8")
        except:
            break
    return url.split("url=")[-1]


async def thinfi_bypass(thinfi_url: str) -> str:
    response = await Httpx.get(thinfi_url)
    return BeautifulSoup(response.content, "html.parser").p.a.get("href")


async def tinyurl_bypass(tinyurl_url: str) -> str:
    return str((await Httpx.get(tinyurl_url)).url)


async def try2link_bypass(url: str):
    client = Session()
    url = url[:-1] if url[-1] == "/" else url
    params = (("d", int(time()) + (60 * 4)),)
    r = client.get(url,
                   params=params,
                   headers={"Referer": "https://newforex.online/"},
                   timeout=5)
    soup = BeautifulSoup(r.text, "html.parser")
    inputs = soup.find(id="go-link").find_all(name="input")
    data = {inp.get("name"): inp.get("value") for inp in inputs}
    await sleep(7)
    headers = {
        "Host": "try2link.com",
        "X-Requested-With": "XMLHttpRequest",
        "Origin": "https://try2link.com",
        "Referer": url,
    }
    bypassed_url = client.post(
        "https://try2link.com/links/go",
        headers=headers,
        data=data,
        timeout=5,
    )
    return bypassed_url.json()["url"]


async def bypasser(url: str, name: str = ""):
    if not any(
            ("ouo.press" in url, "linkbnao.com" in url, "go.earnl.xyz" in url)):
        try:
            response = await Httpx.get(url)
        except Exception:
            raise UrlConnectionError(
                "Can not establish a successful connection with the given url."
            )

        if response.status_code != 200:
            raise UrlConnectionError(
                "Can not establish a successful connection with the given url."
            )

    bypasser_function = ""
    for (key, value) in MAIN_REGEX.items():
        if name:
            if name.lower() == value[0]:
                bypasser_function = value[1]
                break
            raise BypasserNotFoundError(
                "Can not find any bypasser script for the given url.")
        else:
            if bool(search(Rf"{key}", url)):
                bypasser_function = value[1]

    if bypasser_function:
        return await redirect_function(url, bypasser_function)
    raise BypasserNotFoundError(
        "Can not find any bypasser script for the given url")


async def pkin_bypass(url: str) -> str:
    url = url[:-1] if url[-1] == "/" else url
    domain = "https://go.paisakamalo.in/"
    referer = "https://techkeshri.com/"
    token = url.split("/")[-1]
    user_agent = "Mozilla/5.0 (Linux; Android 11; 2201116PI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36"
    client = Session()
    response = client.get(
        domain + token,
        headers={
            "referer": referer,
            "user-agent": user_agent
        },
        timeout=5,
    )
    soup = BeautifulSoup(response.content, "html.parser")
    inputs = soup.find(id="go-link").find_all(name="input")
    data = {inp.get("name"): inp.get("value") for inp in inputs}
    await sleep(3)
    headers = {"x-requested-with": "XMLHttpRequest", "user-agent": user_agent}
    bypassed_url = client.post(domain + "links/go",
                               data=data,
                               headers=headers,
                               timeout=5).json()["url"]
    return bypassed_url


async def bypass(url: str, name: str = ""):
    with suppress(BypasserNotFoundError, UnableToBypassError,
                  UrlConnectionError):
        if "https://ouo.io/" in url:
            url = url.replace("https://ouo.io/", "https://ouo.press/")
        return await bypasser(url, name)
    return ""


async def parselinks(m: Message):
    ent = m.caption_entities or m.entities
    if not ent:
        return []
    tex = m.text or m.caption
    return [
        tex[x.offset:(x.offset + x.length)] for x in ent
        if x.type == MessageEntityType.URL and await verifylink(tex[x.offset:(x.offset + x.length)])
    ]


async def processor(c: Client, m: Message):
    links = await parselinks(m)
    if not links:
        return
    if not await handle_force_sub(c, m):
        return
    preserved = m.text or m.caption
    wk = 0
    for link in links:
        plink = 0
        with suppress(BypasserNotFoundError, UrlConnectionError):
            plink = await bypass(link)
        if not plink:
            continue
        preserved = preserved.replace(link, plink)
        wk = 1
    if not wk:
        return
    with suppress(RPCError):
        if m.caption:
            await m.copy(m.chat.id, preserved)
        else:
            await m.reply_text(preserved, disable_web_page_preview=True)
    return


@pbot.on_message(filters.text | filters.caption & ~filters.command("start") & ~filters.me & filters.private)
async def worker(c: pbot, m: Message):
    with suppress(RuntimeError):
        loop.create_task(processor(c, m))
    return


print("Started!")
pbot.run()
print("Bye!")
