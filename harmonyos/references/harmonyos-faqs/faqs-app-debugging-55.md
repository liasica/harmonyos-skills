---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-55
title: 应用运行报错：hap path error
breadcrumb: FAQ > DevEco Studio > 应用调试 > 应用运行报错：hap path error
category: harmonyos-faqs
scraped_at: 2026-04-29T14:21:27+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:e940ebcd479c878ec14551ace7af23ba2b06ffdad32eb4c515451a027e5272f9
---

**问题现象**

启动调试或运行应用/服务时，应用运行崩溃，提示错误信息“errorMsg: hap path error”。

**解决措施**

如果依赖的应用包未安装，建议进入**Run/Debug Configurations > Deploy Multi Hap****/Hsp**页签，勾选**Deploy Multi Hap/Hsp Packages**，选择所需依赖的应用包，然后重新运行应用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/V73fFJjZRU6TwojLxeAeNA/zh-cn_image_0000002487797922.png?HW-CC-KV=V1&HW-CC-Date=20260429T062126Z&HW-CC-Expire=86400&HW-CC-Sign=27A4D126A13767D011A90D88B7CDFC100F5FFCF2B6BC48EE6CAD96DAA03CB47A)
