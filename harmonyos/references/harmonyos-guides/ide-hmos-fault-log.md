---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-fault-log
title: FaultLog
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 日志与故障分析 > 故障分析 > FaultLog
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:33+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:4da87c56c4dbd2326639f20164fa403ccc9a4c48d4deae5284ae3ddd5b8aa593
---

当应用运行发生错误使应用进程终止时，应用将会抛出错误日志以通知应用崩溃的原因，开发者可通过查看错误日志分析应用崩溃的原因及引起崩溃的代码位置。

FaultLog由系统自动从设备进行收集，包括如下几类故障信息：

* AppFreeze：应用冻屏。
* CPP Crash：C/C++运行时崩溃。
* JS Crash：JS运行时崩溃。
* System Freeze：系统无响应。
* [ASan](ide-hmos-asan.md)（Address-Sanitizer）：C/C++内存错误检测。
* [HWASan](ide-hmos-hwasan.md)（Hardware-Assisted Address Sanitizer）：硬件辅助的C/C++内存错误检测。
* [TSan](ide-hmos-tsan.md)（ThreadSanitizer）：C/C++线程数据竞争检测。
* [UBSan](ide-hmos-ubsan.md)（Undefined Behavior Sanitizer）：C/C++未定义行为检测。

**说明** 

调试模式（debug和attach）下，DevEco Studio会屏蔽当前工程的AppFreeze和System Freeze等超时检测，避免调试过程出现超时检测影响开发者调试。

当前支持屏蔽的AppFreeze故障类型：

* THREAD\_BLOCK\_3S/THREAD\_BLOCK\_6S：应用主线程卡死检测，卡住3秒/6秒。
* APP\_INPUT\_BLOCK：输入响应超时。

当前支持屏蔽的System Freeze故障类型：

* LIFECYCLE\_TIMEOUT：app、ability生命周期切换超时。

## 查看FaultLog日志

### 查看设备历史抛出的FaultLog日志

点击鸿蒙电脑DevEco Studio底部![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/SRZU9rm8Q96XnXlombQULQ/zh-cn_image_0000002779082817.png "点击放大")图标打开日志面板，选择FaultLog，将显示当前选中设备抛出的所有FaultLog日志。

FaultLog故障信息左侧按照**应用/元服务包名 > 故障类型 > 故障时间**结构组成，选中具体的故障日期，则会在右侧展示详细的故障信息，并对部分关键信息进行高亮展示，便于开发者进行故障定位。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/NAeOEjvYRwiyXBR3gYuBwg/zh-cn_image_0000002749323892.png)

### 查看设备实时抛出的FaultLog日志

当设备抛出FaultLog日志时，DevEco Studio将会弹出消息提示框，点击**Jump To Log**即可跳转至FaultLog窗口查看日志信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/V4Qz7p2hRQ2wEjQ1Fb_ktA/zh-cn_image_0000002749323884.png)

### 自动定位到最新FaultLog日志

在FaultLog窗口点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/E_Dt7h8ASoONQVswBpf2hQ/zh-cn_image_0000002778922971.png)按钮，将自动选中当前最新的日志。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/dNZvlz5vRuCuZOxlkT0T4Q/zh-cn_image_0000002779082829.png)

### 跳转至引起错误的代码行

若抛出的FaultLog中的堆栈信息中的链接或偏移地址指向的是当前工程中的某行代码，该段信息将会被转换为超链接形式，点击后可跳转至对应代码行。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/yDDnYXp-S1ClZXHXqYdBWg/zh-cn_image_0000002749483766.png)

## 导出日志

开发者可将当前显示的日志信息保存到本地，以便进一步分析。可根据需要选择保存当前选中节点的日志或保存所有日志。

* 保存当前选中节点的日志：
  + 在当前选中节点右键点击**导出故障日志**。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/fHix9_6UTuGdwUbPXZuZpg/zh-cn_image_0000002749323890.png)
  + 点击**导出**按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/t0C7cZj2SpSxM0YaNIurdw/zh-cn_image_0000002749483760.png)，弹出子选项后进一步点击**导出选中的故障日志**。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/QQasZ0CoSJKGyLhCcWw8rQ/zh-cn_image_0000002779082823.png)

* 保存所有日志：点击**导出**按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/LMTMtBeoTmqN57hdSB6DAg/zh-cn_image_0000002779082819.png)，弹出子选项后进一步点击**导出所有故障日志**。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/KIx5fU9zQYuVDND7Z2rMPQ/zh-cn_image_0000002779082825.png)
