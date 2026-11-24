---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-fault-log
title: FaultLog
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 日志与故障分析 > 故障分析 > FaultLog
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:31+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:86d1512e1f48a64fccfdab3ddc160ca04d3e2ea25340f6866ea8f8a28afbadbf
---

当应用运行发生错误导致应用进程终止时，应用将会抛出错误日志以通知应用崩溃的原因，开发者可通过查看错误日志分析应用崩溃的原因及引起崩溃的代码位置。

FaultLog由系统自动从设备进行收集，包括如下几类故障信息：

* [AppFreeze](ide-faultlog-appfreeze.md)
* CPP Crash
* JS Crash
* System Freeze
* [ASan](ide-asan.md)
* [HWASan](ide-hwasan.md)
* [TSan](ide-tsan.md)
* [UBSan](ide-ubsan.md)

**说明** 

调试模式（debug和attach）下，DevEco Studio会屏蔽当前工程的App Freeze和System Freeze等超时检测，避免调试过程出现超时检测影响开发者调试。

当前支持屏蔽的App Freeze故障类型：

* THREAD\_BLOCK\_3S/THREAD\_BLOCK\_6S：应用主线程卡死检测，卡住3秒/6秒。
* APP\_INPUT\_BLOCK：输入响应超时。

当前支持屏蔽的System Freeze故障类型：

* LIFECYCLE\_TIMEOUT：app、ability生命周期切换超时。

## 查看FaultLog日志

### 查看设备历史抛出的FaultLog日志

打开FaultLog窗口，将显示当前选中设备抛出的所有FaultLog日志。

FaultLog故障信息左侧按照**应用/元服务包名 > 故障类型 > 故障时间**结构组成，选中具体的故障日期，则会在右侧展示详细的故障信息，并对部分关键信息进行高亮展示，便于开发者进行故障定位。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/Q5HIfpJ1Rey_9Qu8-piLjQ/zh-cn_image_0000002779407250.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=107402A954C8B4B506395C7C60AAE626C8B3D189BB550EA24CCBE9D8FAD9DBA5)

### 查看设备实时抛出的FaultLog日志

当设备抛出FaultLog日志时，DevEco Studio将弹出消息提示框，点击**Jump to Log**即可跳转至FaultLog窗口查看日志信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/CoaH4fNjSVywHCKDaJgjNQ/zh-cn_image_0000002779407254.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=DEFDD69AFF2B3C83547841D27C930FE5B53F1BA88076BD9A6692D6293FA21833)

### 跳转至引起错误的代码行

若抛出的FaultLog中的堆栈信息中的链接或偏移地址指向的是当前工程中的某行代码，该段信息将会被转换为超链接形式，点击后可跳转至对应代码行。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/nrF8PCirQ-y77tDReaM4hQ/zh-cn_image_0000002779567230.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=F8B2660B50AC2AFE5CF78DFB8F1DD5C219F3359FC316CF8515B0A17CAB014A3D)

## 导出日志

开发者可将当前显示的日志信息保存到本地，以便进一步分析。可根据需要选择保存当前选中节点的日志或保存所有日志。

* 保存当前选中节点的日志：
  + 在当前选中节点右键点击**Export FaultLog**。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/xe64XTKyRNGbaAIzrADDhg/zh-cn_image_0000002808766815.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=E86575C26FA52E35B4E7548B6CE7FF94857DCC558F58EFE0F3E716A2C508C8A5)
  + 点击Export FaultLog按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/LG4Mef5OQVaWaAqw1xRjtw/zh-cn_image_0000002779567232.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=754A201B2B0D692BD5AB267CA946802DAE0C1B1CDC32AB2F1407B7B2181FC4EA)，弹出子选项后进一步点击**Export Selected FaultLog**。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/HOgHMIKhQJqQ4SpYlQGCsQ/zh-cn_image_0000002808766809.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=8725EAA178528E8523F24F409EA62E4818AAF05BF1A5D4DD56F345552060634B)
* 保存所有日志：点击Export FaultLog按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/3qc4vQk5R2WJ933SfnyAew/zh-cn_image_0000002808886893.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=16F9600CEAD0C6CEFB7C863C5F18E5A3DCBA5C908A455C2AA9959F041B5F5BD9)，弹出子选项后进一步点击**Export All FaultLog**。
