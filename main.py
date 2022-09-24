import glob
from PIL import Image

# 輸入
ImgDir = input("請輸入資料夾位址：")
ImgType = input("請輸入圖片格式（png、jpg...）：")
ImgWidth = input("請輸入圖片寬度：")
ImgHeight = input("請輸入圖片高度：")

imgs = glob.glob(f'{ImgDir}/*.{ImgType}')

print("\n開始轉換...")

if len(imgs) == 0:
    print("\nError：沒有找到可轉換的圖片，請確認資料夾路徑或格式是否輸入錯誤！！")
else:

    for i in imgs:
        im = Image.open(i)

        size = im.size
        im2 = im.resize((int(ImgWidth),int(ImgHeight)))  # 調整圖片尺寸

        im2.save(im.filename)  # 調整後存檔

        print(f"\n轉換成功：{im.filename}")

    input("\n轉換已完成，按下任意鍵離開...")