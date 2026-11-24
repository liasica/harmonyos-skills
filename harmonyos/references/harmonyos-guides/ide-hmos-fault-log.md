---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-fault-log
title: FaultLog
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 日志与故障分析 > 故障分析 > FaultLog
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:46+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:00e08efd70411c9d2070c5658cab9a5b16800b9777a71413b7ce7d283ea7843c
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

点击鸿蒙电脑DevEco Studio底部![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/pe3HOh60S4WNQkrjBdJFxw/zh-cn_image_0000002820681109.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=8846099017B3E49BD381AD3BFE7CBB1371EEE81BA72D535BD553957122E14C1E "点击放大")图标打开日志面板，选择FaultLog，将显示当前选中设备抛出的所有FaultLog日志。

FaultLog故障信息左侧按照**应用/元服务包名 > 故障类型 > 故障时间**结构组成，选中具体的故障日期，则会在右侧展示详细的故障信息，并对部分关键信息进行高亮展示，便于开发者进行故障定位。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/ANpa27cHTuKVVH82mhyWNw/zh-cn_image_0000002820681105.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=6440832CD81A52F2EDE0B413054BEC54414238EA2366DB06E92DB7406B316E50)

### 查看设备实时抛出的FaultLog日志

当设备抛出FaultLog日志时，DevEco Studio将会弹出消息提示框，点击**Jump To Log**即可跳转至FaultLog窗口查看日志信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/Ip09YW-_SsqHLUIQLlxxng/zh-cn_image_0000002820681107.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=205F92B3BCB7E49EDADB7A476F7368E23A468FE2731C2B62771AB778CA216548)

### 自动定位到最新FaultLog日志

在FaultLog窗口点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/csDN3ZRfRpmIbmBoEIRaiA/zh-cn_image_0000002820681113.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=20633759F4333DD2B2ECC4E4AC3B9DA9478C5C6523206D79DE6CFF1482E54927)按钮，将自动选中当前最新的日志。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/4CNFYlO_T5-HvarHMabv4Q/zh-cn_image_0000002791841178.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=810462ACC5793EC6A6FBB0154D566722C96ECEC798391F2C73F6DC58A2A3BFCA)

### 跳转至引起错误的代码行

若抛出的FaultLog中的堆栈信息中的链接或偏移地址指向的是当前工程中的某行代码，该段信息将会被转换为超链接形式，点击后可跳转至对应代码行。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/ico4heCHTLGhPT40Xa67tg/zh-cn_image_0000002791841174.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=2B9A7080A08C165255192E067A4A3964FB1DE349F39342EF2E037D6DDDC86A44)

## 导出日志

开发者可将当前显示的日志信息保存到本地，以便进一步分析。可根据需要选择保存当前选中节点的日志或保存所有日志。

* 保存当前选中节点的日志：
  + 在当前选中节点右键点击**导出故障日志**。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/2hyt5qCZTXmB-L2ZvgyH-Q/zh-cn_image_0000002820681111.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=35369B5091C3C0451DD9B498B2A5649EAEF74CD5BF160CD307BA73F4B5ED50C5)
  + 点击**导出**按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/74wHfy9XR5ul2F59HY-K3Q/zh-cn_image_0000002791841176.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=EA72FAFF507B35EDC45E72250C8376ECF611B9A747BCD14969FB191BCCD75945)，弹出子选项后进一步点击**导出选中的故障日志**。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/BAkPz48_RsO0QzqW_BV0gA/zh-cn_image_0000002820681115.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=26F2124D7CEC582A23F53F3D91A7CDC19AAF0D6D9CE2109B26029243E66B5EFD)

* 保存所有日志：点击**导出**按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/V2wlxAC6RwadLVmAy4lN8w/zh-cn_image_0000002791841170.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=CA53D01A872B503B9C08CBBA7E0105357C37028F5B68757B0C55E857D02C9A6E)，弹出子选项后进一步点击**导出所有故障日志**。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/13sGche0Qv2VjXeQ8x4LKA/zh-cn_image_0000002791841172.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=FED8C4C1AD60576A618F5CEF2669CA93C43D13D0C8DB32FFB9C63103AB19E373)
