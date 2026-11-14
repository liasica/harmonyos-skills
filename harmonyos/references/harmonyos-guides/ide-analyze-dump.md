---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-analyze-dump
title: 解析应用minidump/coredump文件
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 日志与故障分析 > 故障分析 > 解析应用minidump/coredump文件
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:00+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:35151137b14b98bd1da1243326f1cb5675ba56d1450b360fe8d35ac690d7288f
---

从26.0.0版本开始，DevEco Studio支持对应用minidump/coredump文件进行解析，展示堆栈信息，帮助开发者快速定位问题。

## 获取dump文件

* minidump文件：获取方式请参考[OH\_HiAppEvent\_SetEventConfig接口说明](hiappevent-watcher-crash-events.md#oh_hiappevent_seteventconfig接口说明)。
* coredump文件
  1. 应用需要在module.json5中配置[ohos.permission.ALLOW\_COREDUMP权限](permissions-for-all.md#ohospermissionallow_coredump)，配置方式请参考[声明权限](declare-permissions.md)。
  2. 在2in1设备的任务管理器中右键应用进程，选择**创建转储文件**。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/-C3E5M4cRBCHTdi3TuUrCA/zh-cn_image_0000002779567248.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=3FBAC9E0CD64CB41A6CCE368D0BA7A1AFEE530414805A6DFAA3D1AEB36980C2B)
  3. 创建成功后，会提示coredump文件的保存位置。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/GiPMaTw2TN2GwZPjV3xiiw/zh-cn_image_0000002808766833.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=E74329BF5AE3217633B45F1D4F607F9FC23FDA2D99355DBE42101948D3CC73D8)

## 解析dump文件

1. 打开DevEco Studio的**Log**窗口，点击**AnalyzeDump**页签打开界面，选择要解析的dump文件和带调试信息的so目录（默认是模块下的build/{product}/intermediates/libs/{target}/{abi}，其中product和target默认是default，{abi}是设备CPU架构类型，如arm64-v8a），点击**Start Analyze**开始解析。

   **说明** 

   应用产生的dump，需要借助同一次构建生成的so文件中的符号信息才能解析。若使用源码变更后重新构建生成的so目录，可能会因符号不一致导致解析结果不准确或解析失败。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/EF1rWWxgQvinjXmDs8sNqQ/zh-cn_image_0000002779407278.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=098DB87390DF878DC1158A078BB0EA228C6E0EFA532DF74E7C87098BC19F0B77)
2. 等待解析成功后，默认会展示异常线程和对应的堆栈，展开堆栈可查看变量信息，支持切换查看不同线程的堆栈，点击堆栈中的超链接可以跳转到对应的源码。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/VD8ejKftQVKcJGHduFnqCQ/zh-cn_image_0000002779407272.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=52608719103B835679F7E55184B55CF7D5952889C1FB64313AC01F58730E0827)
3. 支持查看指定地址的内存，填写内存地址，点击**View**即可查看。也可以直接右键点击变量查看内存。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/cPjRGvN0Qkq6XDI5YqNuLA/zh-cn_image_0000002779567254.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=12D989AD2FEA681CF699ED56BF052EB1547C16B8B8853B7016E76ECF29000030)

   点击**Settings**，可设置进制、偏移量和展示的内存字节数量。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/ziQNRs0hR1WPb7IdKaiFEA/zh-cn_image_0000002808886917.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=38BBD2A4E79D4BBF54064903B3C1341F1DBF3E7C70E0D81E2ABED7EBD329F300)
