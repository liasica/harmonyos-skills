---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-debug-arkts-debugger
title: 使用调试器
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 应用调试 > 代码调试 > 使用调试器
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:33+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:fe3b3cabccb3d0a47167fa87b1f86247cad614b817d99726cbc38300e8fd2096
---

调试界面有两个窗格，分别是“调试器”和“调试器控制台”。第一个窗格“调试器”，用于调试功能；第二个窗格“调试器控制台”用于展示已加载的ets/js。

## 调试器窗格

调试器面板显示三个独立的窗格：

* 左侧区域是堆栈：当应用暂停时，堆栈区会显示当前代码所引用的代码位置。
* 右侧区域是变量：显示当前运行位置上下文变量，开发者可以在此窗口添加需要监控的变量或表达式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/FZiofaiNR7iqZDnEQ49ilg/zh-cn_image_0000002749323840.png)

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

点击继续图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/WN3QXrJNSjKiIplhHn6sRA/zh-cn_image_0000002778922929.png)，如果命中下一个断点，展示对应的堆栈和变量信息；如果未命中断点，设备上的应用正常运行，变量信息会消失。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/DfqLHnKDQ6OESKd2L0bDJw/zh-cn_image_0000002778922927.png)

### 单步跳过

点击单步跳过![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/J73RiHBiSzGxJXt4Iai5gQ/zh-cn_image_0000002778922921.png)，当前代码执行到下一行代码。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/QZSMVCi0RxWiNAgIDQ8hRw/zh-cn_image_0000002749483718.png)

### 单步执行

点击单步执行![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/GMoW3yeXTu2LNo0ClkHAww/zh-cn_image_0000002779082775.png)，当前调试断点进入到方法内部。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/uCI3pc0tR4mIy2Z5Teidxg/zh-cn_image_0000002779082773.png)

### 单步停止

点击单步停止![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/3hVAJmavT5y6HUabOMtVbQ/zh-cn_image_0000002779082771.png)，调试节点会从方法内部回到调用处。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/AnxMAdjhQ-uZn68aTV0w_A/zh-cn_image_0000002749483712.png)

### 运行到光标处

点击运行到光标处![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/L6ppN9fjSM2xZ--5T29i8A/zh-cn_image_0000002749483710.png)，代码停留在光标停留处。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/wuB0ITvvQgOuycdrgzLaPw/zh-cn_image_0000002749323836.png)

### 重启调试

点击重启调试![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/Qo67r5D4Sfq8kNyZFzlCpQ/zh-cn_image_0000002779082769.png)，重新启动代码调试。

## 调试控制台窗格

用于展示已加载的ets/js。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/l7CkPKOLT0K1ghM_VoHQug/zh-cn_image_0000002749483708.png)
