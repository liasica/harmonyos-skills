---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-fault-log
title: FaultLog
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 日志与故障分析 > 故障分析 > FaultLog
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:55+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:855fd583070ffa922c4fd0d434dec21a53d8086232b6c3ab41b50566dc5b9025
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

点击鸿蒙电脑DevEco Studio底部![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/xlzsQdm7RBO-gYabUpMXxg/zh-cn_image_0000002820681109.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=2292F01A7D192101B2B198353AB9B904500287FF1009D9CC7645109F61A84A8C "点击放大")图标打开日志面板，选择FaultLog，将显示当前选中设备抛出的所有FaultLog日志。

FaultLog故障信息左侧按照**应用/元服务包名 > 故障类型 > 故障时间**结构组成，选中具体的故障日期，则会在右侧展示详细的故障信息，并对部分关键信息进行高亮展示，便于开发者进行故障定位。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/5kginW_6TaWX8lkMdRr71w/zh-cn_image_0000002820681105.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=268F401F7FA2D9D5974A72BF433358332D2C325190E9FE42CE577FEF40147504)

### 查看设备实时抛出的FaultLog日志

当设备抛出FaultLog日志时，DevEco Studio将会弹出消息提示框，点击**Jump To Log**即可跳转至FaultLog窗口查看日志信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/93XQgxtjQ1-bXlpXPmM1Vw/zh-cn_image_0000002820681107.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=9216A22DE6D797BA270E44F92C719688BA1A46440678B15758704BCAAFB31B16)

### 自动定位到最新FaultLog日志

在FaultLog窗口点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/4UHeCRtFQduJx-Q5IqADKg/zh-cn_image_0000002820681113.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=3E6E4668B3869917B5AE1FB01F62339A3182CC0134784424857F68108BEDED1B)按钮，将自动选中当前最新的日志。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/kE9NgnYtTHy9nWs0I6WP4Q/zh-cn_image_0000002791841178.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=8E6674861FF3324F16A3FA6F111234B5136F0D6AC4EE236505B268FA151F0F7A)

### 跳转至引起错误的代码行

若抛出的FaultLog中的堆栈信息中的链接或偏移地址指向的是当前工程中的某行代码，该段信息将会被转换为超链接形式，点击后可跳转至对应代码行。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/y-SVu1CfQMevKvSSy-ECMw/zh-cn_image_0000002791841174.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=04DB485ACC1F2028140CFF7C5D37D0DC154145CEB0E02D53550B2BFE48C86920)

## 导出日志

开发者可将当前显示的日志信息保存到本地，以便进一步分析。可根据需要选择保存当前选中节点的日志或保存所有日志。

* 保存当前选中节点的日志：
  + 在当前选中节点右键点击**导出故障日志**。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/Ui5EA9aFRpyG_G0N-RdvKA/zh-cn_image_0000002820681111.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=16A42AA8EFA24D76DA3D7DE122592F865F334A1778F9582E0CED9A8F4199929C)
  + 点击**导出**按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/uK_LZU6uSwyA1XdOyFmHYA/zh-cn_image_0000002791841176.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=D1BDEFC45B76FE5BD3389F51DF71DFC11B46035F0F5AD05B09EA2BB44F65D076)，弹出子选项后进一步点击**导出选中的故障日志**。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/OolSGxDFQdmPJAVlW_uv3Q/zh-cn_image_0000002820681115.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=EE0C031F665E4D3604BBF19C40306440C773BC67524214282BC3BDB3BCB18743)

* 保存所有日志：点击**导出**按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/mTW-8dzVTgO5pqmGEL9RNA/zh-cn_image_0000002791841170.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=E25D3A2BADB1ED8B0E493664136FBAB74F5864571F44C3EB12C5F6B4287CBE24)，弹出子选项后进一步点击**导出所有故障日志**。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/rriUdgttQ7SxRlbWcZh0Pg/zh-cn_image_0000002791841172.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=96B6DE1AE6E0EA0C22ADC237B717AF29D759E21D7616D736937637B94CF8B27F)
