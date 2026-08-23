import os, sys, asyncio, importlib.util, tempfile, subprocess, json
os.environ.setdefault("AI_MODEL", "gemini-fast")
os.environ.setdefault("POLLINATIONS_API_KEY", "dummy")

spec = importlib.util.spec_from_file_location('m', os.path.join(os.getcwd(), 'youtube_longform_automation.py'))
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

OUT = tempfile.mkdtemp(prefix="zh_dur_")
print("Work dir:", OUT)

# 30 REAL Chinese phrases (english + chinese + pinyin)
phrases = [
 {"english":"Believe in yourself.","chinese":"相信自己。","romaji":"Xiāngxìn zìjǐ."},
 {"english":"You are capable of amazing things.","chinese":"你有能力做不可思议的事。","romaji":"Nǐ yǒu nénglì zuò bùkěsīyì de shì."},
 {"english":"Dream big, start small.","chinese":"敢于梦想，从小处着手。","romaji":"Gǎnyú mèngxiǎng, cóng xiǎochù zhuóshǒu."},
 {"english":"Your future is created by your actions.","chinese":"你的未来由你的行动创造。","romaji":"Nǐ de wèilái yóu nǐ de xíngdòng chuàngzào."},
 {"english":"Never give up on your dreams.","chinese":"永远不要放弃你的梦想。","romaji":"Yǒngyuǎn búyào fàngqì nǐ de mèngxiǎng."},
 {"english":"Small steps lead to big changes.","chinese":"一小步也能带来大改变。","romaji":"Yī xiǎo bù yě néng dàilái dà gǎibiàn."},
 {"english":"You are stronger than you think.","chinese":"你比自己想象的更强大。","romaji":"Nǐ bǐ zìjǐ xiǎngxiàng de gèng qiángdà."},
 {"english":"Love yourself first.","chinese":"先爱自己。","romaji":"Xiān ài zìjǐ."},
 {"english":"Love makes everything possible.","chinese":"爱让一切成为可能。","romaji":"Ài ràng yíqiè chéngwéi kěnéng."},
 {"english":"My heart beats for you.","chinese":"我的心为你跳动。","romaji":"Wǒ de xīn wèi nǐ tiàodòng."},
 {"english":"You are my everything.","chinese":"你是我的一切。","romaji":"Nǐ shì wǒ de yíqiè."},
 {"english":"Success comes from hard work.","chinese":"成功来自努力。","romaji":"Chénggōng láizì nǔlì."},
 {"english":"Keep going, you're getting there.","chinese":"继续前进，你快到了。","romaji":"Jìxù qiánjìn, nǐ kuài dào le."},
 {"english":"Winners never quit.","chinese":"赢家永不放弃。","romaji":"Yíngjiā yǒngbù fàngqì."},
 {"english":"Knowledge is power.","chinese":"知识就是力量。","romaji":"Zhīshi jiùshì lìliang."},
 {"english":"Learn from yesterday, live for today.","chinese":"从昨天学习，为今天而活。","romaji":"Cóng zuótiān xuéxí, wèi jīntiān ér huó."},
 {"english":"Happiness is a choice.","chinese":"幸福是一种选择。","romaji":"Xìngfú shì yì zhǒng xuǎnzé."},
 {"english":"Find joy in the little things.","chinese":"在小事中发现快乐。","romaji":"Zài xiǎoshì zhōng fāxiàn kuàilè."},
 {"english":"Thank you for everything.","chinese":"谢谢你的一切。","romaji":"Xièxiè nǐ de yíqiè."},
 {"english":"I appreciate your help.","chinese":"我感激你的帮助。","romaji":"Wǒ gǎnjī nǐ de bāngzhù."},
 {"english":"True friends stick together.","chinese":"真正的朋友并肩同行。","romaji":"Zhēnzhèng de péngyǒu bìngjiān tóngxíng."},
 {"english":"There is always hope.","chinese":"总会有希望。","romaji":"Zǒng huì yǒu xīwàng."},
 {"english":"Better days are coming.","chinese":"更好的日子会到来。","romaji":"Gèng hǎo de rìzi huì dàolái."},
 {"english":"Create something beautiful today.","chinese":"今天创造美好的事物。","romaji":"Jīntiān chuàngzào měihǎo de shìwù."},
 {"english":"Find peace within yourself.","chinese":"在内心寻找平静。","romaji":"Zài nèixīn xúnzhǎo píngjìng."},
 {"english":"Breathe, relax, let go.","chinese":"呼吸，放松，放下。","romaji":"Hūxī, fàngsōng, fàngxià."},
 {"english":"You are enough, just as you are.","chinese":"你现在的样子就足够好。","romaji":"Nǐ xiànzài de yàngzi jiù zúgòu hǎo."},
 {"english":"Stand tall, speak up.","chinese":"昂首挺胸，勇敢发声。","romaji":"Ángshǒu tǐngxiōng, yǒnggǎn fāshēng."},
 {"english":"Be kind to everyone you meet.","chinese":"对你遇到的每个人都友善。","romaji":"Duì nǐ yùdào de měi gè rén dōu yǒushàn."},
 {"english":"Good things take time.","chinese":"美好的事物需要时间。","romaji":"Měihǎo de shìwù xūyào shíjiān."},
]

N = len(phrases)
print(f"Testing {N} real Chinese phrases...")
audio_files = m.generate_all_audio(phrases, OUT)
print(f"Generated {len(audio_files)} audios")

# blank images (content irrelevant for duration)
from PIL import Image
imgs = []
for i in range(N):
    p = os.path.join(OUT, f"img_{i:03d}.jpg")
    Image.new('RGB', (1920,1080), (40,30,60)).save(p)
    imgs.append(p)

final = os.path.join(OUT, "narration.mp3")
m.create_final_narration(audio_files, final)
video = os.path.join(OUT, "zh_sample.mp4")
m.create_video_from_images_audio(imgs, audio_files, final, video)

def dur(p):
    r = subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","default=noprint_wrappers=1:nokey=1", p], capture_output=True, text=True)
    return float(r.stdout.strip())

vd = dur(video)
avg = vd / N
print(f"\n=== RESULT ===")
print(f"Sample video duration: {vd:.1f}s for {N} phrases")
print(f"Avg per phrase: {avg:.2f}s")
for target in (600, 610):
    need = int(target/avg) + 1
    print(f"  For >= {target}s need ~{need} phrases (predicted {need*avg:.0f}s = {need*avg/60:.1f} min)")
