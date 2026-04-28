---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-previewer-operating-5
title: 预览报错“Node service error detected.Reinstall DevEco Studio to fix the error. ”
breadcrumb: FAQ > DevEco Studio > 界面预览 > 预览报错“Node service error detected.Reinstall DevEco Studio to fix the error. ”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:06+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:c231faebb56651ba03e241ae498bd5e84cb0f4939818ed8120c7d591a8f2bb78
---

**问题现象**

预览启动失败，PreviewerLog窗口显示错误信息：“Node service error detected.Reinstall DevEco Studio to fix the error.”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/w6Yh20dWTmCIQ1hsIq1_hA/zh-cn_image_0000002194318348.png?HW-CC-KV=V1&HW-CC-Date=20260428T002905Z&HW-CC-Expire=86400&HW-CC-Sign=440F44F2DD1BC7DC4590A0785E6B9DBD55E10280E19C8492E880C965811535E7 "点击放大")

**解决措施**

* 方案一：DevEco Studio的内置文件已损坏，请重新安装DevEco Studio。
* 方案二：hosts中关于127.0.0.1的配置项有误，请检查hosts配置是否存在127.0.0.1 localhost的配置项。
  + Windows平台配置文件：C:\Windows\System32\drivers\etc\hosts。
  + Mac平台配置文件：/private/etc/hosts。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/fQ8TNN5uTFyJXk7u4bE0xg/zh-cn_image_0000002229758609.png?HW-CC-KV=V1&HW-CC-Date=20260428T002905Z&HW-CC-Expire=86400&HW-CC-Sign=73A34DDE40E9D24E8C2497CB0BA1D4C199812F4871C9C4BAA7839471C88EEA4A "点击放大")
* 方案三：尝试重启winnat服务（Windows平台）。

  以管理员身份打开命令提示符或PowerShell，执行以下命令：

  1. 停止winnat。

     ```
     1. net stop winnat
     ```
  2. 启动winnat。

     ```
     1. net start winnat
     ```
