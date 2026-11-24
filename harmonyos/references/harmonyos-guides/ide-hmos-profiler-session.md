---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-profiler-session
title: 会话区
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 优化应用性能 > DevEco Profiler调优工具简介 > 会话区
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:48+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:34483b64178fc6777a22fc221596f56b768c350162588bcde3eee3e82dc2a443
---

DevEco Profiler左侧为会话区，分为两个部分：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/9qMpb0hxTaqgm8K10oSlOg/zh-cn_image_0000002820680955.png?HW-CC-KV=V1&HW-CC-Date=20261124T044248Z&HW-CC-Expire=31536000000&HW-CC-Sign=9DF6DA22EF06FF3B103D854DC927B855AAF3823583FAF2703C3E2F4DB53589FF "点击放大")

① 调优目标选择区域：选择被调优的设备、应用包及应用进程作为后续调优会话的分析对象。

② 会话列表区域：记录当前已创建的调优分析会话，每一个会话都会包含：会话的名称、会话当前状态、会话对应的录制时长信息。单击列表中的会话后，界面右侧数据区将显示其数据内容。

**说明** 

会话录制完成出现![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/jUQS4A_PQf-JcIa6pFWlwg/zh-cn_image_0000002820720959.png?HW-CC-KV=V1&HW-CC-Date=20261124T044248Z&HW-CC-Expire=31536000000&HW-CC-Sign=2278A47F42F21FC9FC79DF1B236B57EE2DA79D07FA52DE9890846BE60D925AD4)图标，表示数据处于解析状态，请耐心等待解析完成。

* **创建会话**：点击会话列表![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/u6AJyfwiS5S20ONolhI-4Q/zh-cn_image_0000002791841022.png?HW-CC-KV=V1&HW-CC-Date=20261124T044248Z&HW-CC-Expire=31536000000&HW-CC-Sign=B474FF59365394408C345CBAA71E1D5ECC533C73FF5F8816592784075E9431A3)图标，在弹窗中选中任意模板，点击下方**新建会话**按钮，即可创建出一个全新的会话。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/YplbHvv2SkyfbVUCdSvk3g/zh-cn_image_0000002820720957.png?HW-CC-KV=V1&HW-CC-Date=20261124T044248Z&HW-CC-Expire=31536000000&HW-CC-Sign=9D9ED1B38FCB2CC3EE030C1628C05DF8398C361099212344C5DDC46D7607024B "点击放大")
* **数据导入**：单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/7uS1SgaQT3uGYUegA8qa4A/zh-cn_image_0000002792000996.png?HW-CC-KV=V1&HW-CC-Date=20261124T044248Z&HW-CC-Expire=31536000000&HW-CC-Sign=B1F03E40F23ED48B6CF22DBB3EA8A804A03EEA21A336E918FBCFDB53EAB54A7C)图标选择.insight文件，即可导入历史数据。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/H8xsYNBzS9iPhdGYLqRJRA/zh-cn_image_0000002820720961.png?HW-CC-KV=V1&HW-CC-Date=20261124T044248Z&HW-CC-Expire=31536000000&HW-CC-Sign=AD4CB71A62C2C3125D61ECF14B5BAF0215CC212F67B83BD3B73BB0411B5DF870 "点击放大")
* **数据导出**：待数据解析完成后，会话便会进入数据展示状态，将数据可视化展示到右侧的数据区中。此时可以点击会话面板中出现的数据导出按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/cCVr5MY6TeusGiLKDoUnfQ/zh-cn_image_0000002792000992.png?HW-CC-KV=V1&HW-CC-Date=20261124T044248Z&HW-CC-Expire=31536000000&HW-CC-Sign=154D335D7E79DACACEBD9C640FD26A3B19A1A74B42C889A65818E06804BF5B30 "点击放大")，将录制到的数据导出到本地进行保存，借助这个能力，开发者可以方便地在团队内共享录制到的性能数据，也可以防止采集到的性能数据丢失。
