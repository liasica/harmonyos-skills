---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-arkts-evaluate-log
title: 打印表达式
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > 打印表达式
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:38+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:110a9cc0a22abcab4809d2cabae5e299d19131bab1033eb26d42dc0b8b5235ec
---

开发者可以通过Evaluate and log能力在代码执行到断点行时打印开发者指定的表达式。

1. 在需要打印表达式结果的地方设置断点。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/SUBidijGStm58fWpFr30MQ/zh-cn_image_0000002779566804.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=B988792EDD76A00EE9E83AC6D5BE16B7C4AA6E257AA932566AA2F9E799D95586)
2. 右键断点，然后点击**More**按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/g3OZSCPgS6qfabpkIjDPFg/zh-cn_image_0000002808766389.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=96AC4DC30231F78C3FE03EFB910EB520678B8944CB0751A8E2AA4B700D748BDA)
3. 勾选**Evaluate and log**复选框，并在下方输入框输入要打印的表达式。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/S3rxWSkZSIOcoCrjJZC4lQ/zh-cn_image_0000002779566806.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=E3653AFDDCEABF67EC5D999B5E2F7F15016DF1CA489238F6C820D7E1358DD882)
4. 启动调试，程序运行到断点时，切换到调试的Console窗口，表达式的打印结果将在这里展示。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/MqUMX2jpT4SC0X9TaItLOA/zh-cn_image_0000002779406828.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=EB12DAC75788846C117C9CB927E679A9D42BEF1644320A60A513E4F7791ACEE5)
