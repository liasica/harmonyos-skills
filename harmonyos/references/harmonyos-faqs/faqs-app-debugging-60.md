---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-60
title: DevEco Studio安装HAP时报错“FileTransfer Failed: [Fail]Error opening file: no such file or directory”
breadcrumb: FAQ > DevEco Studio > 应用调试 > DevEco Studio安装HAP时报错“FileTransfer Failed: [Fail]Error opening file: no such file or directory”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:30:10+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:a90ef28fcd3ebf31477cacb777ad8f02e911e5735a45793351fefb7fb4c1f797
---

**问题现象**

DevEco Studio安装HAP时报错“FileTransfer Failed: [Fail]Error opening file: no such file or directory”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/_8sw2kGpSriHTYjDqb5aYw/zh-cn_image_0000002356774736.png?HW-CC-KV=V1&HW-CC-Date=20260428T003009Z&HW-CC-Expire=86400&HW-CC-Sign=116C21A0A26FE6113155B1572431F87D36C3D66105A15B5E9E0C856B45F093B3)

**解决措施**

出现该问题的原因是path路径的安装包不存在，可以检查签名HAP包是否没打包成功，修改签名，正常打出签名HAP包后再运行。

**参考链接**

[对HAP/APP进行签名](../harmonyos-guides/ide-command-line-building-app.md#section103321051433)
