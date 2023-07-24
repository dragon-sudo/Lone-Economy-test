from selenium import webdriver
import time

# 设置网站地址
url = "https://www.163.com"  

# 创建 Chrome 浏览器对象，需要安装 Chrome 浏览器和对应版本的 ChromeDriver
driver = webdriver.Chrome()  # 或者使用 Firefox：webdriver.Firefox()

try:
    while True:
        # 打开网页
        driver.get(url)

        # 等待网页加载完成，可以根据需要调整等待时间
        time.sleep(5)

        # 获取当前时间戳
        timestamp = int(time.time())

        # 设置保存的图片文件名
        image_name = f"screenshot_{timestamp}.png"

        # 截取当前网页的屏幕截图并保存为图片
        driver.save_screenshot()
        pic_path="./"+image_name
        bk_img = CV2.imread(pic_path)  # 加载图片

        CV2.putText(bk_img, current_time, (100, 300), CV2.FONT_HERSHEY_SIMPLEX,1.2, (255, 0, 0), 2, CV2.LINE_AA)  # 在图片上添加文字信息

        CV2.waitKey()

        CV2.imwrite(pic_path, bk_img)  # 保存修改后的图片

        print(f"保存图片成功：{image_name}")

        # 每隔5分钟保存一次，可以根据需要调整等待时间
        time.sleep(300)

except KeyboardInterrupt:
    # 当用户按下 Ctrl+C 时，终止脚本并关闭浏览器
    driver.quit()
