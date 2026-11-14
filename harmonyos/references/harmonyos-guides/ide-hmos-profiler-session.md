---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-profiler-session
title: 会话区
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 优化应用性能 > DevEco Profiler调优工具简介 > 会话区
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:20+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:5bdd631ac45d3069f96d19dc1ca85fe7d98dd8905e20da5d314089a1c466ed47
---

DevEco Profiler左侧为会话区，分为两个部分：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/zFfoidkiThukyGtvMHRr9A/zh-cn_image_0000002810630719.png?HW-CC-KV=V1&HW-CC-Date=20261114T004730Z&HW-CC-Expire=31536000000&HW-CC-Sign=B022B5EC5A2A2B0C01DBCE7559610C29908C0EA92F575F416917E6D646DDCB81 "点击放大")

① 调优目标选择区域：选择被调优的设备、应用包及应用进程作为后续调优会话的分析对象。

② 会话列表区域：记录当前已创建的调优分析会话，每一个会话都会包含：会话的名称、会话当前状态、会话对应的录制时长信息。单击列表中的会话后，界面右侧数据区将显示其数据内容。

**说明** 

会话录制完成出现![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/fS61dibuSxCauZzyXk9PoQ/zh-cn_image_0000002810750823.png?HW-CC-KV=V1&HW-CC-Date=20261114T004730Z&HW-CC-Expire=31536000000&HW-CC-Sign=1DACD1777610923D9756CB39435B549DE8F1622A5D16C136EC15ABCD222D2BF7)图标，表示数据处于解析状态，请耐心等待解析完成。

* **创建会话**：点击会话列表![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/j5TXdIxnQW28h_6AX6-mxA/zh-cn_image_0000002810750825.png?HW-CC-KV=V1&HW-CC-Date=20261114T004730Z&HW-CC-Expire=31536000000&HW-CC-Sign=3C9B93F8F33E9E0AFCE86BE9F17569A09014DE1F54647C48B411F58A5368FA5A)图标，在弹窗中选中任意模板，点击下方**新建会话**按钮，即可创建出一个全新的会话。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/YsMsXfRPQlKFgylpnPK83g/zh-cn_image_0000002810750831.png?HW-CC-KV=V1&HW-CC-Date=20261114T004730Z&HW-CC-Expire=31536000000&HW-CC-Sign=85D46F46538455FDA3416D85EDE859A6FF1D516BF2545B3B2A4071A611EC428E "点击放大")
* **数据导入**：单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/Bu9pYPEQQHmRW0UchVHK6Q/zh-cn_image_0000002810750829.png?HW-CC-KV=V1&HW-CC-Date=20261114T004730Z&HW-CC-Expire=31536000000&HW-CC-Sign=5FBB9A78B7954B79B8E2C366F073FCBD960B5E5541CF6317C7E5408B06D2B77A)图标选择.insight文件，即可导入历史数据。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/eG7kTxNjTW2BmnrKCRaVNw/zh-cn_image_0000002810630723.png?HW-CC-KV=V1&HW-CC-Date=20261114T004730Z&HW-CC-Expire=31536000000&HW-CC-Sign=4F6FF6C09523678071BEA36A4BAB083C14945217874AD5A6A4A41CBD29602692 "点击放大")
* **数据导出**：待数据解析完成后，会话便会进入数据展示状态，将数据可视化展示到右侧的数据区中。此时可以点击会话面板中出现的数据导出按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/sB6OCggRRv6x13JbZpdYrA/zh-cn_image_0000002781471168.png?HW-CC-KV=V1&HW-CC-Date=20261114T004730Z&HW-CC-Expire=31536000000&HW-CC-Sign=3263450B37767B0F9471B10BA19D59C9F376040F9DC7542EF680D61D8F53A166 "点击放大")，将录制到的数据导出到本地进行保存，借助这个能力，开发者可以方便地在团队内共享录制到的性能数据，也可以防止采集到的性能数据丢失。
