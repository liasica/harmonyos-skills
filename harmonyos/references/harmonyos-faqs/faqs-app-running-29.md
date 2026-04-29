---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-running-29
title: 设备管理点击“新建模拟器”按钮无响应
breadcrumb: FAQ > DevEco Studio > 应用运行 > 设备管理点击“新建模拟器”按钮无响应
category: harmonyos-faqs
scraped_at: 2026-04-29T14:21:19+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:7e61714f73433afd4dd10690c0382ffbcc35813cee65a74c88e10241cea48a0d
---

**问题现象**

点击New Emulator按钮无响应。

**解决措施**

1. 打开本地计算机的设置，查找“**可选功能**”，然后选择“**添加可选功能**”。
2. 搜索wmic，然后点击安装。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/9eKXWdDcRSSDkTmMKp1eGQ/zh-cn_image_0000002229603901.png?HW-CC-KV=V1&HW-CC-Date=20260429T062117Z&HW-CC-Expire=86400&HW-CC-Sign=CC6B447B292F96086D1373375111363A67787DE6C0BE2678FF2A6786AD605355 "点击放大")
3. 配置系统环境变量，以Win10为例，点击**此电脑 > 属性 > 高级系统设置 > 高级 > 环境变量**，在系统Path变量中添加%SystemRoot%\\System32\\Wbem。
