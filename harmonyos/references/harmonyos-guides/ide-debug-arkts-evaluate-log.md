---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-arkts-evaluate-log
title: 打印表达式
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > 打印表达式
category: harmonyos-guides
scraped_at: 2026-04-29T13:46:43+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:422e5fc6ad058817733ed45142ef9bfc431d83553e0bf26dc4bb482c7f8e6832
---

开发者可以通过Evaluate and log能力在代码执行到断点行时打印开发者指定的表达式。

1. 在需要打印表达式结果的地方设置断点。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/hFt8f-rtQg67kH4qnlW_9w/zh-cn_image_0000002561832883.png?HW-CC-KV=V1&HW-CC-Date=20260429T054642Z&HW-CC-Expire=86400&HW-CC-Sign=D18DB725BDF8B44CE091151B3E8DD34F843E7ACA9435A6235FD094405E8AB342)
2. 右键断点，然后点击**More**按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/HhUVpnlQQLKorVZT4yBTqQ/zh-cn_image_0000002561752901.png?HW-CC-KV=V1&HW-CC-Date=20260429T054642Z&HW-CC-Expire=86400&HW-CC-Sign=1CA7DD80D84772035C5CBF7F7D26F2E294878FD396A90B518ED28DD830FA781F)
3. 勾选**Evaluate and log**复选框，并在下方输入框输入要打印的表达式。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/K6msGHk-Q0C0Z6Tevu-JsQ/zh-cn_image_0000002530912956.png?HW-CC-KV=V1&HW-CC-Date=20260429T054642Z&HW-CC-Expire=86400&HW-CC-Sign=ACF77207B059561A7A5746B789A157B93A1CDCA47676EFB7FB7205499D0E0A98)
4. 启动调试，程序运行到断点时，切换到调试的Console窗口，表达式的打印结果将在这里展示。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/xeT-MQBGQqSoEK5L0sAC-g/zh-cn_image_0000002561832879.png?HW-CC-KV=V1&HW-CC-Date=20260429T054642Z&HW-CC-Expire=86400&HW-CC-Sign=FFEB7478B8A2D3FF5AD0275ACA9CD5957C1C1BE99A2F37CBEC35E4F3CF23A298)
