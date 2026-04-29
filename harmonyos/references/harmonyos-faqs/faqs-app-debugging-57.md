---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-57
title: DevEco如何配置不响应raise捕获到的assert信号
breadcrumb: FAQ > DevEco Studio > 应用调试 > DevEco如何配置不响应raise捕获到的assert信号
category: harmonyos-faqs
scraped_at: 2026-04-29T14:21:27+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:f722327f5f93cfc25247679cac69b5a6a5afcb6c8bf0e82dd50aeac06da3260e
---

在DevEco Studio RUN/Debug Configurations中的Edit Configurations > Debugger > LLDB Post Attach Commands，添加配置：process handle -p false -s false -n false signal。其中，signal为assert发送的信号。详细步骤如图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/Pl-rOc0eQ6aZ8Vq18e8NcQ/zh-cn_image_0000002194158524.png?HW-CC-KV=V1&HW-CC-Date=20260429T062127Z&HW-CC-Expire=86400&HW-CC-Sign=D48C77B0162FB2F17B70987E820E5C9CD3B62FA4EC5B537B1082F71729CA79B1)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/nnKe7eCPRP-MqNDjsWEY0w/zh-cn_image_0000002229603925.png?HW-CC-KV=V1&HW-CC-Date=20260429T062127Z&HW-CC-Expire=86400&HW-CC-Sign=E56C6A2BFD872CD7A5FC7445BFF2C60B952C5D0E70D3F1D49794CD2A913F0F43 "点击放大")
