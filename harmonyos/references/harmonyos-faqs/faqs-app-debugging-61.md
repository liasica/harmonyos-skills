---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-61
title: DevEco Studio安装HAP时报错“FileTransfer Failed: [Fail]Error opening file: operation not permitted”
breadcrumb: FAQ > DevEco Studio > 应用调试 > DevEco Studio安装HAP时报错“FileTransfer Failed: [Fail]Error opening file: operation not permitted”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:30:10+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:4f37c2c52c92ea54fc288f7c96c394e04eb5c2b98e7aa585e0fdb22437890854
---

**问题现象**

DevEco Studio安装HAP时报错“FileTransfer Failed: [Fail]Error opening file: operation not permitted”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/cinSBZnnRxq9SF88lE8umw/zh-cn_image_0000002557334391.png?HW-CC-KV=V1&HW-CC-Date=20260428T003009Z&HW-CC-Expire=86400&HW-CC-Sign=8345049D703DDA97DB7EA63B03B2900460E46E7E93C2B1D046A36986C578A732)

**解决措施**

出现该问题的原因是安装包HAP所在路径没有权限。

1、Windows系统建议将工程移出C盘，然后重新运行。

2、MAC系统为DevEco Studio获取完全磁盘访问权，请进入**“系统设置”>“隐私与安全性”>“完全磁盘访问权限”**，在列表中勾选DevEco Studio软件并重启。
