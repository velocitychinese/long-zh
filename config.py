"""VELOCITY LONGFORM - 16:9 chapter lesson, brand and motion constants."""

import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

OUTPUT_DIR = BASE_DIR / "output"
LESSONS_DIR = OUTPUT_DIR / "lessons"
HISTORY_DIR = OUTPUT_DIR / "history"
SCENE_DIR = BASE_DIR / "scene"

VIDEO_WIDTH = 1920
VIDEO_HEIGHT = 1080
FPS = 30

TARGET_CHAPTERS = 8
PHRASES_PER_CHAPTER = 7
TARGET_PHRASES = TARGET_CHAPTERS * PHRASES_PER_CHAPTER

# ---------------------------------------------------------------- brand

BRAND = "VELOCITY CHINESE"
BRAND_LOCKUP_TOP = "VELOCITY"
BRAND_LOCKUP_BOTTOM = "CHINESE"
HANDLE = "@velocitychinese"
MASCOT_NAME = "Velo"

# ==== LANGUAGE PACK START ====
LANGUAGE = {'code': 'zh',
 'name': 'Chinese',
 'native_name': '中文',
 'history_key': 'chinese',
 'english_voice': 'en-US-AvaNeural',
 'english_fallback_voice': 'en-US-GuyNeural',
 'native_voice': 'zh-CN-XiaoxiaoNeural',
 'native_fallback_voice': 'zh-CN-YunxiNeural',
 'native_engine': 'edge',
 'native_lang_code': 'zh',
 'english_rate': '-4%',
 'native_rate': '-10%',
 'english_pitch': '+0Hz',
 'native_pitch': '+0Hz',
 'native_label': '中文',
 'translit_label': 'PINYIN',
 'flag': 'cn',
 'greeting': '你好！',
 'encouragement': '太棒了！',
 'rtl': False,
 'char_tiles': True,
 'script_font': 'Script.ttf',
 'glyphs': '中文汉语学习每天进步你好世界'}
# ==== LANGUAGE PACK END ====

# ==== CATEGORIES START ====
CATEGORIES = {'Motivation': '动力',
 'Love': '爱',
 'Success': '成功',
 'Wisdom': '智慧',
 'Happiness': '幸福',
 'Self Improvement': '自我提升',
 'Gratitude': '感恩',
 'Friendship': '友谊',
 'Hope': '希望',
 'Creativity': '创造力',
 'Inner Peace': '内心平静',
 'Confidence': '自信',
 'Perseverance': '毅力',
 'Inspiration': '灵感',
 'Positive Life': '积极人生',
 'Courage': '勇气',
 'Kindness': '善良',
 'Patience': '耐心',
 'Forgiveness': '宽恕',
 'Strength': '力量',
 'Joy': '快乐',
 'Balance': '平衡',
 'Growth': '成长',
 'Purpose': '目标',
 'Mindfulness': '正念',
 'Travel & Airport': '旅行与机场',
 'Ordering Food & Dining': '点餐与用餐',
 'Shopping & Prices': '购物与价格',
 'Asking for Directions': '问路',
 'Hotel & Accommodation': '酒店与住宿',
 'Daily Routine': '日常生活',
 'Meeting People & Greetings': '认识新朋友与问候',
 'Emergency & Health': '紧急情况与健康',
 'Public Transportation': '公共交通',
 'Work & Office': '工作与办公室',
 'Weather & Small Talk': '天气与闲聊',
 'Coffee Shop & Bakery': '咖啡馆与面包店',
 'Family & Home': '家庭与家居',
 'Hobbies & Free Time': '爱好与休闲',
 'Dating & Romance': '约会与浪漫',
 'Phone Calls & Messages': '电话与短信',
 'Banking & Money': '银行与金钱',
 'Doctor & Pharmacy': '医生与药房',
 'Sports & Fitness': '运动与健身',
 'Celebrations & Parties': '庆祝活动与派对',
 'Feelings & Emotions': '感受与情绪',
 'Agreeing & Disagreeing': '同意与反对',
 'Making Plans': '制定计划',
 'Common Native Slang': '常用本土俚语',
 'Cultural Traditions': '文化传统'}
# ==== CATEGORIES END ====

CATEGORY_NAMES = list(CATEGORIES.keys())

AI_MODEL = os.getenv("AI_MODEL", "openai/gpt-5.4-nano")
AI_FALLBACK_MODEL = os.getenv("AI_FALLBACK_MODEL", "gemini-fast")
POLLINATIONS_API_KEY = os.getenv("POLLINATIONS_API_KEY", "")

# ---------------------------------------------------------------- timing (seconds)

INTRO_DURATION = 7.2
CHAPTER_INTRO_DURATION = 4.4
OUTRO_DURATION = 13.0

EN_CARD_IN = 0.70
GAP_EN_NATIVE = 0.60
NATIVE_CARD_LEAD = 0.40
GAP_BEFORE_REPEAT = 1.00
TAIL_HOLD = 1.30

# ---------------------------------------------------------------- palette

INK = "#30303A"
MUTED = "#8A8A8A"
CREAM = "#FFF8E7"
GREEN = "#58CC02"
GREEN_DARK = "#46A302"
GREEN_DEEP = "#3D8F00"
BLUE = "#1CB0F6"
PURPLE = "#7C5CFF"
ORANGE = "#FF7A00"
RED = "#FF4B4B"
YELLOW = "#F5A700"
TEAL = "#00A889"
PINK = "#E056A0"

# ==== HASHTAGS START ====
HASHTAGS = ['#learnchinese',
 '#chineselessons',
 '#chineseforbeginners',
 '#languagelearning',
 '#chinesevocabulary',
 '#velocitychinese',
 '#dailychinese',
 '#chinese',
 '#learnlanguages',
 '#speakchinese']
# ==== HASHTAGS END ====
