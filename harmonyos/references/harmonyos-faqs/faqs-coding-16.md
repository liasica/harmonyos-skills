---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-coding-16
title: DevEco Studio启动报错：“Scan files to index fail”
breadcrumb: FAQ > DevEco Studio > 代码编辑 > DevEco Studio启动报错：“Scan files to index fail”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:04+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:01448f63aa7283fe20f201b4a6f0c7609d2d6e1d8c2e6b550c0fbd0bdfc610ee
---

**问题现象**

在DevEco Studio上打开项目工程时，启动缓慢，且一会儿后报错：“Scan files to index fail”。

**解决措施**

当DevEco Studio打开项目工程时，会启动编辑器Node进程扫描工程代码以建立索引。编辑器Node进程默认内存上限为8G，超过此内存大小时，编辑器Node进程会启动失败，从而报错Scan files to index fail。为避免工程代码量过大导致编辑器启动失败，请根据工程代码量和开发环境内存大小配置合适的Node进程内存上限。内存上限值需要随工程的代码量和复杂程度增长，通常代码量300万行的工程建议配置大于12G，400万行建议配置大于15G，每增加100万行增加3G，可根据具体情况适当增减。

以配置内存上限为12G举例，打开DevEco Studio，通过菜单栏的Help > Edit Custom Properties...，打开idea.properties配置文件。在文件中新增一行 arkts.server.max.old.space.size=12288，然后重启DevEco Studio。编辑器Node进程的内存上限将设置为12288M（即12G）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/3mokty01RaWIRlzeWVywnQ/zh-cn_image_0000002378621596.png?HW-CC-KV=V1&HW-CC-Date=20260428T002903Z&HW-CC-Expire=86400&HW-CC-Sign=4A9CE126497DE1ABF37DFA29A22381C1F263FC327DC8B945A7529C1F6F23BA63)
