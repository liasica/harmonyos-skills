---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-61
title: "DevEco Studio安装HAP时报错“FileTransfer Failed: [Fail]Error opening file: operation not permitted”"
breadcrumb: "FAQ > DevEco Studio > 应用调试 > DevEco Studio安装HAP时报错“FileTransfer Failed: [Fail]Error opening file: operation not permitted”"
category: harmonyos-faqs
scraped_at: 2026-10-28T07:49:00+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:dd311d174d2c84639b129230ef43c56ec8930571ec3a8128c9e7d660e476edb8
---

**问题现象**

DevEco Studio安装HAP时报错“FileTransfer Failed: [Fail]Error opening file: operation not permitted”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/bUZCye27RtOW0HdKP6cY1Q/zh-cn_image_0000002654838121.png)

**解决措施**

出现该问题的原因是安装包HAP所在路径没有权限。

1、Windows系统建议将工程移出C盘，然后重新运行。

2、MAC系统为DevEco Studio获取完全磁盘访问权，请进入**“系统设置”>“隐私与安全性”>“完全磁盘访问权限”**，在列表中勾选DevEco Studio软件并重启。
