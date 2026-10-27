---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-running-29
title: 设备管理点击“新建模拟器”按钮无响应
breadcrumb: FAQ > DevEco Studio > 应用运行 > 设备管理点击“新建模拟器”按钮无响应
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:58+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:97152fe6bf293d5394e2522cc3ad79bbfe761019cd2b5ab2f815f12664ff7ae3
---

**问题现象**

点击New Emulator按钮无响应。

**解决措施**

1. 打开本地计算机的设置，查找“**可选功能**”，然后选择“**添加可选功能**”。
2. 搜索wmic，然后点击安装。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/2PlaYocFRQ2E0XHEj_uaTA/zh-cn_image_0000002654798127.png "点击放大")
3. 配置系统环境变量，以Win10为例，点击**此电脑 > 属性 > 高级系统设置 > 高级 > 环境变量**，在系统Path变量中添加%SystemRoot%\\System32\\Wbem。
