---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-1
title: 编译报错“JS heap out of memory”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“JS heap out of memory”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:07+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:a8eae314176be3550f283af3e4e01bf9d9c16031701785eb0c3fd3cfd8d99707
---

**问题现象**

编译构建时，出现报错“JS heap out of memory”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/ZzyVZI7dTEmDInUMJ4mA2Q/zh-cn_image_0000002194158628.png?HW-CC-KV=V1&HW-CC-Date=20260428T002906Z&HW-CC-Expire=86400&HW-CC-Sign=F707A769748ADED24A411F32E109D6EC04645BB45FF885763216B38ED107C83C)

**解决措施**

出现该报错的原因是hvigor运行时内存不足。在使用3.1.0及以上版本的hvigor时，可通过以下方式修改hvigor运行时内存的最大值。

勾选 Enable the Daemon for tasks：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/ifd8oN51Sbio3aemIHKfTw/zh-cn_image_0000002194318244.png?HW-CC-KV=V1&HW-CC-Date=20260428T002906Z&HW-CC-Expire=86400&HW-CC-Sign=C7ED07C156283D7943171B4DEAFD9E3801681D753988ED0652AD25898FF15D34)

在hvigor-config.json5中修改maxOldSpaceSize字段，根据工程大小适当增大，例如设置为 8192。
