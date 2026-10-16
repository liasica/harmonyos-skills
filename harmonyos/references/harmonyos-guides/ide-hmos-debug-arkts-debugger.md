---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-debug-arkts-debugger
title: 使用调试器
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 应用调试 > 代码调试 > 使用调试器
category: harmonyos-guides
scraped_at: 2026-10-17T06:43:47+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:931078f5d6373517d29f6e2e8508d041958bbafa9ec75fafd05d1957662a7dd9
---

调试界面有两个窗格，分别是“调试器”和“调试器控制台”。第一个窗格“调试器”，用于调试功能；第二个窗格“调试器控制台”用于展示已加载的ets/js。

## 调试器窗格

调试器面板显示三个独立的窗格：

* 左侧区域是堆栈：当应用暂停时，堆栈区会显示当前代码所引用的代码位置。
* 右侧区域是变量：显示当前运行位置上下文变量，开发者可以在此窗口添加需要监控的变量或表达式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/1y3Eod7mTiKyIBK0t41XZg/zh-cn_image_0000002750009740.png)

调试器窗格有多个按钮：

**表1** 调试器按钮

| 按钮 | 名称 | 快捷键 | 功能 |
| --- | --- | --- | --- |
|  | 继续 | **F9** | 当程序执行到断点时停止执行，单击此按钮程序继续执行。 |
|  | 单步跳过 | **F8** | 在单步调试时，直接前进到下一行（如果函数中存在子函数，不会进入子函数内单步执行，而是将整个子函数当作一步执行）。 |
|  | 单步执行 | **F7** | 在单步调试时，遇到子函数后，进入子函数并继续单步执行。 |
|  | 单步停止 | **Shift+F8** | 在单步调试执行到子函数内时，单击单步停止会执行完子函数剩余部分，并跳出返回到上一层函数。 |
|  | 停止 | **Ctrl+F2** | 停止调试任务。 |
|  | 运行到光标处 | **Alt+F6** | 断点执行到鼠标停留处。 |
|  | 重启调试 | **Ctrl+F5** | 重新启动调试。 |

### 继续

点击继续图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/uElaMLUcScqNdK85AFJiYg/zh-cn_image_0000002750009744.png)，如果命中下一个断点，展示对应的堆栈和变量信息；如果未命中断点，设备上的应用正常运行，变量信息会消失。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/wOrk5yh1TFCfr6e7yzI1Wg/zh-cn_image_0000002779728803.png)

### 单步跳过

点击单步跳过![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/DwnIq4RqRFmpPVuV48_oJg/zh-cn_image_0000002750169624.png)，当前代码执行到下一行代码。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/kRfd2YXcRD2ZhT0Qk_fP_w/zh-cn_image_0000002750009746.png)

### 单步执行

点击单步执行![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/5R4C5MdLTPGrskcT66GJWw/zh-cn_image_0000002750169628.png)，当前调试断点进入到方法内部。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/BdOuULz9SHeE5t-ILMwVdg/zh-cn_image_0000002750009738.png)

### 单步停止

点击单步停止![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/VTj9zCeXR-Wcil5J56q0EQ/zh-cn_image_0000002750009736.png)，调试节点会从方法内部回到调用处。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/15MiQRUlQcq1dcqyneWOKQ/zh-cn_image_0000002779728801.png)

### 运行到光标处

点击运行到光标处![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/EU188hZ8Q6iEmx-xG429OA/zh-cn_image_0000002779728799.png)，代码停留在光标停留处。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/ObQSdV-aSBqWVMQqojrVLg/zh-cn_image_0000002779608649.png)

### 重启调试

点击重启调试![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/AOTz0r4zTQKCUZekP4SGmg/zh-cn_image_0000002750009734.png)，重新启动代码调试。

## 调试控制台窗格

用于展示已加载的ets/js。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/oQyBHnqxQuWeGQWVirFB9Q/zh-cn_image_0000002779728797.png)
