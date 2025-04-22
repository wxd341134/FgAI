import time
import allure
from utils.logger import Logger

logger = Logger().get_logger()

class JSTextSelector:
    """JavaScript文本选择工具类"""

    @staticmethod
    @allure.step("使用JS选中文本: {text}")
    def select_text(driver, text):
        """
        使用JavaScript选中指定文本
        Args:
            driver: WebDriver实例
            text: 要选中的文本
        Returns:
            bool: 是否成功选中文本
        """
        try:
            logger.info(f"尝试使用JS选中文本: {text}")

            js_script = """
            function selectText(searchText) {
                const textNodes = [];

                // 递归查找文本节点
                function findTextNodes(node) {
                    if (node.nodeType === 3) {
                        if (node.textContent.includes(searchText)) {
                            textNodes.push(node);
                        }
                    } else {
                        for (let child of node.childNodes) {
                            findTextNodes(child);
                        }
                    }
                }

                findTextNodes(document.body);

                if (textNodes.length === 0) {
                    return false;
                }

                // 使用第一个匹配的文本节点
                const textNode = textNodes[0];
                const range = document.createRange();
                const content = textNode.textContent;
                const startIndex = content.indexOf(searchText);

                // 设置选区
                range.setStart(textNode, startIndex);
                range.setEnd(textNode, startIndex + searchText.length);

                // 应用选区
                const selection = window.getSelection();
                selection.removeAllRanges();
                selection.addRange(range);

                // 滚动到选区
                const element = textNode.parentElement;
                element.scrollIntoView({
                    behavior: 'smooth',
                    block: 'center'
                });

                return true;
            }

            return selectText(arguments[0]);
            """

            result = driver.execute_script(js_script, text)

            if not result:
                raise Exception(f"未找到文本: {text}")

            time.sleep(1)  # 等待选中效果
            logger.info(f"成功选中文本: {text}")
            return True

        except Exception as e:
            logger.error(f"选中文本失败: {str(e)}")
            allure.attach(
                driver.get_screenshot_as_png(),
                "选中文本失败截图",
                allure.attachment_type.PNG
            )
            raise
