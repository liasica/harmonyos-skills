---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-57
title: DevEco如何配置不响应raise捕获到的assert信号
breadcrumb: FAQ > DevEco Studio > 应用调试 > DevEco如何配置不响应raise捕获到的assert信号
category: harmonyos-faqs
scraped_at: 2026-04-29T14:21:27+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:394261fff51b105948a3fbc02ba40b0111f6053267076f2c935369066160795c
---

在DevEco Studio RUN/Debug Configurations中的Edit Configurations > Debugger > LLDB Post Attach Commands，添加配置：process handle -p false -s false -n false signal。其中，signal为assert发送的信号。详细步骤如图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/Pl-rOc0eQ6aZ8Vq18e8NcQ/zh-cn_image_0000002194158524.png)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/nnKe7eCPRP-MqNDjsWEY0w/zh-cn_image_0000002229603925.png "点击放大")
