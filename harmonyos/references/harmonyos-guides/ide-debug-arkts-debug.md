---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-arkts-debug
title: debug启动调试
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > debug启动调试
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:46+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:eb7a3cff0901fa89e56763d64ce459edbe2df429b78d40af0dcb94033ca058e4
---

可以按照如下方式启动调试会话。

1. 如果需要设置断点调试，找到需要暂停的代码片段，点击该代码行的左侧边线，或将光标置于该行上并按Ctrl + F8（macOS为Command+F8）。如果无法添加断点，请查看FAQ[调试过程中无法添加断点](../harmonyos-faqs/faqs-app-debugging-1.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/v67Toa4ySP6ZSRlj76XgQA/zh-cn_image_0000002530912932.png?HW-CC-KV=V1&HW-CC-Date=20260427T235645Z&HW-CC-Expire=86400&HW-CC-Sign=E6E43561FF499271A82293CE76C0E02C975D75C884F11FBFBC840895904D61AA)

   设置断点后，调试能够在正确的断点处中断，并高亮显示该行。
2. 在设备选择框中，选择调试的设备。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/loq05x_9S6mQugpR95Q4Cw/zh-cn_image_0000002530752928.png?HW-CC-KV=V1&HW-CC-Date=20260427T235645Z&HW-CC-Expire=86400&HW-CC-Sign=93BC0618A6B67619E893E21A5694D9CD65BAC8E7F9A0AA3D3EA0A7F5204CE367)
3. 选择启动调试的配置，在模块选择框中选择需要调试的模块。也可以通过Edit Configurations[配置调试参数](ide-run-debug-configurations.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/8197HXkVQLCVQ0yJmhz9yg/zh-cn_image_0000002530752940.png?HW-CC-KV=V1&HW-CC-Date=20260427T235645Z&HW-CC-Expire=86400&HW-CC-Sign=E31A492DE0C29564720CC9CA7DEF7D2D980C026B5D5BB121A022CD92921C50A0)
4. 在工具栏中，单击Debug![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/a-u_jz87R5mKWss8Sype1g/zh-cn_image_0000002530912928.png?HW-CC-KV=V1&HW-CC-Date=20260427T235645Z&HW-CC-Expire=86400&HW-CC-Sign=EA26368058D5DC1227B35D51610E5837BCBC43685989254A1E0B0883218B6388)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/Apgy6XGuQ9i6hCrFK4pn7A/zh-cn_image_0000002561832861.png?HW-CC-KV=V1&HW-CC-Date=20260427T235645Z&HW-CC-Expire=86400&HW-CC-Sign=096F4D122EDF135950F77A87C3473A600E6773A602F2541C0B3D1CB18C288578)

   或者在工具栏中Run中选择Debug。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/iw0SYCDHSJSLlUz8lIRhhQ/zh-cn_image_0000002561832855.png?HW-CC-KV=V1&HW-CC-Date=20260427T235645Z&HW-CC-Expire=86400&HW-CC-Sign=64F866C5E7C4677043A49B32DCD96E1333663945F9E0A67926F3D37F84F70495)
5. 启动调试后，开发者可以通过[调试器](ide-debug-arkts-debugger.md)进行代码调试。

   如有断点会在断点处高亮，并展示当前断点处的Frames和Variables。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/FPVUY3uRQbWpEMSr83ENZA/zh-cn_image_0000002530912926.png?HW-CC-KV=V1&HW-CC-Date=20260427T235645Z&HW-CC-Expire=86400&HW-CC-Sign=24D4235903AE0DD75C80A9406223250575880BA1891B95B6E9F2AEC69C0EF34B)
