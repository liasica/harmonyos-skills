---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-fault-log
title: FaultLog
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 日志与故障分析 > 故障分析 > FaultLog
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:17+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:6c98e91c68943cc5bb1b922f0440e05347db6095db75fbeefc12c22b83b190da
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

点击鸿蒙电脑DevEco Studio底部![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/Be0eleUKRRW10V0wVJl8Pg/zh-cn_image_0000002810750815.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=F6ED61B7141658B480293BAE6F2158D1F3DCAC8E9F9E7E3AC2F140B677600F10 "点击放大")图标打开日志面板，选择FaultLog，将显示当前选中设备抛出的所有FaultLog日志。

FaultLog故障信息左侧按照**应用/元服务包名 > 故障类型 > 故障时间**结构组成，选中具体的故障日期，则会在右侧展示详细的故障信息，并对部分关键信息进行高亮展示，便于开发者进行故障定位。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/Gd1FFxkJRN-mG8MG4QQ6Jg/zh-cn_image_0000002781471166.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=378F6929BAD68FE50CFB4B5917F933D55C1C3A1930F6BBB9AC9730F7E3A0C08A)

### 查看设备实时抛出的FaultLog日志

当设备抛出FaultLog日志时，DevEco Studio将会弹出消息提示框，点击**Jump To Log**即可跳转至FaultLog窗口查看日志信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/9Kqb2_0XQUO1-GVq4d-1Vw/zh-cn_image_0000002781311224.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=3710C8661B2903376C3046FF303810E07B757DC27410EDEA4F9EB6E970D1C59B)

### 自动定位到最新FaultLog日志

在FaultLog窗口点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/A_KtyyRyRyWT8DoNuY_KgA/zh-cn_image_0000002810750819.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=CF8F7360509122D676655BC89D77BAC183C9044FEC980AAECA2C25369E76C8BF)按钮，将自动选中当前最新的日志。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/O8LSB1zaQUiCMl8pXIMdsw/zh-cn_image_0000002810630721.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=8DE66CC96A975383A88A8BA037A61009BB9F323B8FBD5028B3292CC8668084A3)

### 跳转至引起错误的代码行

若抛出的FaultLog中的堆栈信息中的链接或偏移地址指向的是当前工程中的某行代码，该段信息将会被转换为超链接形式，点击后可跳转至对应代码行。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/NyNgb9URTu6viR8wssrNnw/zh-cn_image_0000002781311234.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=DFC2EE95478EC445FAEE31329EC88265E5489649E16A9D220EA0EC8FFDBE5A38)

## 导出日志

开发者可将当前显示的日志信息保存到本地，以便进一步分析。可根据需要选择保存当前选中节点的日志或保存所有日志。

* 保存当前选中节点的日志：
  + 在当前选中节点右键点击**导出故障日志**。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/HbHLCgtZQ4OL-7dZj5aybg/zh-cn_image_0000002810630715.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=81DC6B51562A8206BA1152F70D9D6136226EE082F30048D91076CEA71B312A5F)
  + 点击**导出**按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/Ko89UhsGRJCxL-xyjnnsKA/zh-cn_image_0000002810630713.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=8E55BA9460357D17134CFD8799E12BF8D292596B344E0476D2997BCA6B2539CA)，弹出子选项后进一步点击**导出选中的故障日志**。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/q62gEAvtQfeMuQl__aFGfw/zh-cn_image_0000002781471162.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=A3B8A16651D5813A5CEFADCFF607CFC9BDB3DDBBD13EE83C555B5CB47356B5F2)

* 保存所有日志：点击**导出**按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/VXtf5pCSSImJ2A3seIUgRQ/zh-cn_image_0000002781471158.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=C6FB5E3798B2E4ECE713E863A56F0A9205B1C8783D1D4D8A82247767342992BB)，弹出子选项后进一步点击**导出所有故障日志**。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/PQOhBxYDSr-OZ4bCDwN6fw/zh-cn_image_0000002810630717.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=824710C1B5CFB6747A0C215624B79F5EBE2981E719ACFE82E98533B20E8AFA8A)
