---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-fault-log
title: FaultLog
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 日志与故障分析 > 故障分析 > FaultLog
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:00+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:48132bb9ddbb2486d5c6997ae9056181b5a1cba8474e7b69bc192f9abf128d10
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/LEDINCDBSj66hVf6WpIcfw/zh-cn_image_0000002779407250.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=34D61F54795FDB8DD13B8DB031E945B4DE7F61969774CD670A809714EE9EBAD7)

### 查看设备实时抛出的FaultLog日志

当设备抛出FaultLog日志时，DevEco Studio将弹出消息提示框，点击**Jump to Log**即可跳转至FaultLog窗口查看日志信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/-OAGnlBEQL-arbWvVmdxPQ/zh-cn_image_0000002779407254.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=7E6C33E2F923A13F74E0AD62BC5A8F49848AE5F94152C82E99B21028FD1429FB)

### 跳转至引起错误的代码行

若抛出的FaultLog中的堆栈信息中的链接或偏移地址指向的是当前工程中的某行代码，该段信息将会被转换为超链接形式，点击后可跳转至对应代码行。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/BtDn8B6KRhSuBteZOajyYQ/zh-cn_image_0000002779567230.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=4F0D2C79137547A7E5E60F775E994F005592BE3E2814ADF8EFB092195B1D6CF4)

## 导出日志

开发者可将当前显示的日志信息保存到本地，以便进一步分析。可根据需要选择保存当前选中节点的日志或保存所有日志。

* 保存当前选中节点的日志：
  + 在当前选中节点右键点击**Export FaultLog**。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/fuAEPdXjRhCc97xf5QXb3w/zh-cn_image_0000002808766815.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=4C30F92B24B9B143B2A61C5ECDB1CF1FD898A1D59C974E920E2DBBAED6C372AD)
  + 点击Export FaultLog按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/zXg1kzq9RAy5Q3HHH--bhw/zh-cn_image_0000002779567232.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=FEAE90831F203F8C7131ACCA3284E3D1417BF85203BC428B8DB1AC6E1C5707EC)，弹出子选项后进一步点击**Export Selected FaultLog**。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/y3K8dooaQGqBG3mcjSy1Lw/zh-cn_image_0000002808766809.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=58314A341C5423B062058DAC7BDD417ED2797A02B8C299F63003668B203211B6)
* 保存所有日志：点击Export FaultLog按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/Xu4lxG11RPimV0HEkXRbkg/zh-cn_image_0000002808886893.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=50DBCE2231210320D3829F612DB279DDF9B654154EB1909DB0855E07413121DC)，弹出子选项后进一步点击**Export All FaultLog**。
