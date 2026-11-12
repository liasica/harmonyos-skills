---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-fault-log
title: FaultLog
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 日志与故障分析 > 故障分析 > FaultLog
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:e923603cf6427256556990ef96da8bf2e0e72b9f945b60f9eb494aaffd624349
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

点击鸿蒙电脑DevEco Studio底部![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/JSeLfbl0QvetlB3dCUyDZA/zh-cn_image_0000002810750815.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=0D35801F7B9CD8D3D4A3D310A6BBEDD8FBDB8C723523A293E4B67A22CE51F65F "点击放大")图标打开日志面板，选择FaultLog，将显示当前选中设备抛出的所有FaultLog日志。

FaultLog故障信息左侧按照**应用/元服务包名 > 故障类型 > 故障时间**结构组成，选中具体的故障日期，则会在右侧展示详细的故障信息，并对部分关键信息进行高亮展示，便于开发者进行故障定位。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/jDnwR5a7QmSwZW-QaAwqDQ/zh-cn_image_0000002781471166.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=99AA360108C8021C709FA6B4A4E41ED0F29C91939F6FA6627DCADF468EAC647F)

### 查看设备实时抛出的FaultLog日志

当设备抛出FaultLog日志时，DevEco Studio将会弹出消息提示框，点击**Jump To Log**即可跳转至FaultLog窗口查看日志信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/DRQAHtD2QpqJHy8uaVHXCQ/zh-cn_image_0000002781311224.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=2242EDBC118EF6EE5C88E476B6426D5888EFDC9AAD59679617A9534F96839B8F)

### 自动定位到最新FaultLog日志

在FaultLog窗口点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/2p2PxrVsTVeR2mO4m3Dgjg/zh-cn_image_0000002810750819.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=3C94CE7CCCC1ADA15885D28D057FC7049417ABED1D426CBDEBD6799547C74475)按钮，将自动选中当前最新的日志。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/8qyiQgDSRPm8zDyMt1DtDg/zh-cn_image_0000002810630721.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=1ADA2C66C534C4407FA20737EC1EEFC3176E6AF0D607A8B29DDB923E0A549904)

### 跳转至引起错误的代码行

若抛出的FaultLog中的堆栈信息中的链接或偏移地址指向的是当前工程中的某行代码，该段信息将会被转换为超链接形式，点击后可跳转至对应代码行。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/LRosOPS5TiCGj113lBXxfQ/zh-cn_image_0000002781311234.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=6A9115FB69EAD7E5256DC89CA0C9BEB7FF465BD4BAF6A7ED563C502110714B50)

## 导出日志

开发者可将当前显示的日志信息保存到本地，以便进一步分析。可根据需要选择保存当前选中节点的日志或保存所有日志。

* 保存当前选中节点的日志：
  + 在当前选中节点右键点击**导出故障日志**。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/Kw8ORBQWT5q_jerzfIqECQ/zh-cn_image_0000002810630715.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=F010C22D00208D622C530F8834C56BECD4ADB1D33F5E218DE404C8153B87E63E)
  + 点击**导出**按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/_-IEGQP0T5KvgxB1T1Eaqg/zh-cn_image_0000002810630713.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=3E36C257D873D686DE81799AAF35EB02D5DE2D875B4A99218FC9D8093C6EF6AB)，弹出子选项后进一步点击**导出选中的故障日志**。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/bdgOODhhR1yevIjRRZ1myA/zh-cn_image_0000002781471162.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=0998C368EA4FC3E10F0694D242A6F37A99BE19021A47E3C123A7535B1A070C77)

* 保存所有日志：点击**导出**按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/VYos4Um6Rji-2qCbN73JoQ/zh-cn_image_0000002781471158.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=02A991C84F5ED9787F39169E89F44B6BD15878CF0DDB3E681FDA45D969A18EB8)，弹出子选项后进一步点击**导出所有故障日志**。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/vBdpddFoQF6i3P1aKPHiXA/zh-cn_image_0000002810630717.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=3F6F43190710CDC7F6341CE21FA06F4AC53F198642FAB0B24DCAF4F72BC3A059)
