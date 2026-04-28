---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-57
title: DevEco如何配置不响应raise捕获到的assert信号
breadcrumb: FAQ > DevEco Studio > 应用调试 > DevEco如何配置不响应raise捕获到的assert信号
category: harmonyos-faqs
scraped_at: 2026-04-28T08:30:11+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:458902fb33791a567ebff31e5a5e6c741aec232450cf2fe2bd3a45d198292b8e
---

在DevEco Studio RUN/Debug Configurations中的Edit Configurations > Debugger > LLDB Post Attach Commands，添加配置：process handle -p false -s false -n false signal。其中，signal为assert发送的信号。详细步骤如图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/Pl-rOc0eQ6aZ8Vq18e8NcQ/zh-cn_image_0000002194158524.png?HW-CC-KV=V1&HW-CC-Date=20260428T003010Z&HW-CC-Expire=86400&HW-CC-Sign=A26DD833776490680AD853D66BF3277957D10E2FCE374C1535BACE270BA5C94A)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/nnKe7eCPRP-MqNDjsWEY0w/zh-cn_image_0000002229603925.png?HW-CC-KV=V1&HW-CC-Date=20260428T003010Z&HW-CC-Expire=86400&HW-CC-Sign=4567C07B20C6006F0F5C94AA4E2176C040A397A54B8E307D987BBF3E84457B2D "点击放大")
