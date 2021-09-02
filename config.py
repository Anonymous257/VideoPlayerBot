"""
VideoPlayerBot, Telegram Video Chat Bot
Copyright (c) 2021  Asm Safone <https://github.com/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import os
import re
from dotenv import load_dotenv

load_dotenv()

class Config:
    ADMIN = os.environ.get("AUTH_USERS", "1847068212 1939166467")
    ADMINS = [int(admin) if re.search('^\d+$', admin) else admin for admin in (ADMIN).split()]
    API_ID = int(os.environ.get("API_ID", "4094043"))
    CHAT_ID = int(os.environ.get("CHAT_ID", "-1001415962984"))
    API_HASH = os.environ.get("API_HASH", "6782c95f70f6a40c57bbc471545db5c3")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "1810104491:AAHeDROgzamKjsnT17Y15Q7cnrzs0CDHteo")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Danger_music_robot")
    REPLY_MESSAGE = os.environ.get("REPLY_MESSAGE", "DIE BITCHES")
    if REPLY_MESSAGE:
        REPLY_MESSAGE = REPLY_MESSAGE
    else:
        REPLY_MESSAGE = None
    SESSION_STRING = os.environ.get("SESSION_STRING", "BQBIz73r3S2Yb3o4ykhoN89F59Nabxpq1mNESeF_vN-mQjUpnj1s24VVXT8u0o0q2kW-Kx1mlfMb_QPWY0HYzYq5XCWR4-KH8jwiCUGRWpwnRVJq1ycNlWMSbB00C7j0iau4bo3hR6aND8ed82oi9Kn5TNoWzriqLx6IAypVPac2F_4IieJZbZu3u1UH2gxOKaJ4wQtyvSqFP_Bw8jhqtwIlGkNAjwgy-u5Gr8cIEGWACnKD5NMhNqKERlx3xkaXV_1KPtrRhqnFxhEhc3CQxJY6HUnOrLezRtZO1OsrzsW0-Wp9hqhZ0aRRTg9WP2KOMdWWfNFSATVQNKaxdIY05DQSdgdWiQA")
