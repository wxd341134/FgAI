from PIL import Image, ImageEnhance, ImageFilter, ImageDraw, ImageOps
import pytesseract
import cv2
import numpy as np

# 设置Tesseract路径（根据你的实际安装路径修改）
pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files\Tesseract-OCR\tesseract.exe'


def advanced_preprocess(image):
    """
    高级验证码预处理流程（针对数字验证码优化）
    处理步骤：
    1. 图像放大增强
    2. 自适应二值化
    3. 去噪处理
    4. 形态学操作
    5. 边缘增强
    """
    # 转换为OpenCV格式
    img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    # 步骤1：图像放大（使用LANCZOS插值）
    scale_factor = 3
    img = cv2.resize(img, None, fx=scale_factor, fy=scale_factor,
                     interpolation=cv2.INTER_LANCZOS4)

    # 步骤2：灰度化+自适应阈值
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY_INV, 11, 5)

    # 步骤3：去噪（中值滤波）
    denoised = cv2.medianBlur(thresh, 3)

    # 步骤4：形态学操作（闭合小孔洞）
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    morph = cv2.morphologyEx(denoised, cv2.MORPH_CLOSE, kernel)

    # 步骤5：边缘增强
    edges = cv2.Canny(morph, 50, 150)
    enhanced = cv2.addWeighted(morph, 0.7, edges, 0.3, 0)

    return Image.fromarray(enhanced)


def recognize_captcha(image_path):
    """
    验证码识别主函数
    :param image_path: 验证码图片路径
    :return: 识别结果
    """
    # 1. 加载图片
    original = Image.open(image_path)

    # 2. 高级预处理
    processed = advanced_preprocess(original)
    processed.save("debug_processed.png")  # 保存处理后的图片用于调试

    # 3. OCR识别配置（多模式尝试）
    custom_configs = [
        r'--oem 3 --psm 7 -c tessedit_char_whitelist=0123456789',
        r'--oem 3 --psm 8 -c tessedit_char_whitelist=0123456789',
        r'--oem 3 --psm 10 -c tessedit_char_whitelist=0123456789'
    ]

    # 4. 多配置尝试识别
    best_text = ""
    for config in custom_configs:
        text = pytesseract.image_to_string(processed, config=config).strip()
        if len(text) >= 4 and text.isdigit():
            best_text = text
            break

    # 5. 结果后处理
    if not best_text:
        # 如果自动识别失败，尝试获取原始识别结果
        raw_text = pytesseract.image_to_string(processed,
                                               config=r'--oem 3 --psm 7').strip()
        # 提取所有数字
        digits = [c for c in raw_text if c.isdigit()]
        best_text = "".join(digits[:4]) if digits else ""

    return best_text


if __name__ == '__main__':
    # 测试识别
    captcha_path = "captchas/original_captcha_5.png"  # 替换为你的验证码图片路径
    result = recognize_captcha(captcha_path)

    print(f"原始图片: {captcha_path}")
    print(f"识别结果: {result if result else '识别失败'}")

    # 显示处理前后的对比（需要安装matplotlib）
    try:
        import matplotlib.pyplot as plt

        fig, (ax1, ax2) = plt.subplots(1, 2)
        ax1.imshow(Image.open(captcha_path))
        ax1.set_title('Original')
        ax2.imshow(Image.open("debug_processed.png"))
        ax2.set_title('Processed')
        plt.show()
    except:
        print("提示：安装matplotlib可显示图片对比（pip install matplotlib）")