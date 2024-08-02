from sample_config import Config
#config = Config()
import os 
#from sample_config import Config
from dotenv import load_dotenv
load_dotenv()

class Development(Config):
    
    # ضـع اكـوادك تحت مكـان الكـلام العـربي  .. امسـح الكلام العربي اللي بين " " فقـط وضع اكـوادك
    #APP_ID = 6 #ضع كود الايبي ايدي الصغيـر مكان الرقم 6 نسخ لصق   
    APP_ID = int(os.environ.get("APP_ID", 6))
    #API_HASH = "ضع كود الايبي هاش"
    API_HASH = os.environ.get("API_HASH") or None
    #ALIVE_NAME = "اسم حسابك التلي"
    ALIVE_NAME = os.environ.get("ALIVE_NAME", None)
    DB_URI = os.environ.get("DATABASE_URL", None)
    #DB_URI = DB_URI #"postgresql://postgres:hFQbrQKWpYRqwPOvFccHonzPsQarhaGr@roundhouse.proxy.rlwy.net:28541/railway"
    #STRING_SESSION = "كود تيرمــكس"
    STRING_SESSION = os.environ.get("STRING_SESSION", None)
    #TG_BOT_TOKEN = "توكـن البـوت الخـاص بك"
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN")
    
    PRIVATE_GROUP_BOT_API_ID = -1002211195485  # ضـع ايـدي كـروب السجـل بجـانب العـدد -100 لا تمسـح العـدد هـذا
    COMMAND_HAND_LER = "."  # اتركهــا كمـا هـي
    SUDO_COMMAND_HAND_LER = "."  # اتركهــا كمـا هـي
    TZ = "Asia/Baghdad"  # اتركهــا كمـا هـي
