---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-1
title: 编译报错“JS heap out of memory”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“JS heap out of memory”
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:20+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:d7ab224987e012d59ab47372e059117e7b9cba6198712ad33e6eb001da7d3cc9
---

**问题现象**

编译构建时，出现报错“JS heap out of memory”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/ZzyVZI7dTEmDInUMJ4mA2Q/zh-cn_image_0000002194158628.png?HW-CC-KV=V1&HW-CC-Date=20260429T062018Z&HW-CC-Expire=86400&HW-CC-Sign=AA1BD2BF5D2708D925CE7A6FE161FBD115B55983C158D512208AA064DD78F18E)

**解决措施**

出现该报错的原因是hvigor运行时内存不足。在使用3.1.0及以上版本的hvigor时，可通过以下方式修改hvigor运行时内存的最大值。

勾选 Enable the Daemon for tasks：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/ifd8oN51Sbio3aemIHKfTw/zh-cn_image_0000002194318244.png?HW-CC-KV=V1&HW-CC-Date=20260429T062018Z&HW-CC-Expire=86400&HW-CC-Sign=5257776D1DBCEB0B9B364490C21E4F25E87AA6740CDBEAABB6E34C7CBC21BC02)

在hvigor-config.json5中修改maxOldSpaceSize字段，根据工程大小适当增大，例如设置为 8192。
