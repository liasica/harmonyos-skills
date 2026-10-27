---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-57
title: DevEco如何配置不响应raise捕获到的assert信号
breadcrumb: FAQ > DevEco Studio > 应用调试 > DevEco如何配置不响应raise捕获到的assert信号
category: harmonyos-faqs
scraped_at: 2026-10-28T07:49:00+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:785bac711c6d54d24cfec26c41d6d3829aba16bfe827008710b53d0476bf6add
---

在DevEco Studio RUN/Debug Configurations中的Edit Configurations > Debugger > LLDB Post Attach Commands，添加配置：process handle -p false -s false -n false signal。其中，signal为assert发送的信号。详细步骤如图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/6MbzHc5NSJ6t1wNpYgkhpA/zh-cn_image_0000002654838123.png)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/F8TSXNe9T2G3ygkmP_bZTg/zh-cn_image_0000002624478804.png "点击放大")
