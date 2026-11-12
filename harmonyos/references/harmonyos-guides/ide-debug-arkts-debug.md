---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-arkts-debug
title: debug启动调试
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > debug启动调试
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:2ea208f983a5824b67a0f941ec1b81a5e4a7d7e2e0006388be250ccc5d9dc618
---

可以按照如下方式启动调试会话。

1. 如果需要设置断点调试，找到需要暂停的代码片段，点击该代码行的左侧边线，或将光标置于该行上并按Ctrl + F8（macOS为Command+F8）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/kEI8OVODTV2uEEFB0nDPyw/zh-cn_image_0000002779566786.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=47CCF2E93BEE105ACDD8D5956F56F3FD8DB842AF922F939F4E78383CC65DBA6A)

   设置断点后，调试能够在正确的断点处中断，并高亮显示该行。
2. 在设备选择框中，选择调试的设备。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/DN0grNkrSxaoS8mc5YDDqw/zh-cn_image_0000002779406804.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=EA1A062008D6C3840EF2C93AC538C0E8FC5BD0368F9FF4379325F94BE1F8F28C)
3. 选择启动调试的配置，在模块选择框中选择需要调试的模块。也可以通过Edit Configurations[配置调试参数](ide-run-debug-configurations.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/azixopwTS8GKboW9vtAsSw/zh-cn_image_0000002808766369.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=CF5A95A4F331B2BEB0AD942D1C8DB99212E48360C2E2586F67AF4A60BA735B75)
4. 在工具栏中，单击Debug![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/JfOVtGZrSR6BXqICAiilOA/zh-cn_image_0000002808886447.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=F623031BCBA5E6C7D3A019F85043CBEE3D110B427C23B87FBACDC952A057954E "点击放大")。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/d5uHWkeHQEm4q6JZ8PHrNQ/zh-cn_image_0000002779406810.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=8DF86A0EEE3F86C95B20B902A0DE2D98971AE518E620EBCC5CA326294D7D8C5A)

   或者在工具栏中Run中选择Debug。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/2tFA1F0FSWub2I5S-T6QzQ/zh-cn_image_0000002779406808.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=77EEE7058B83B243E7EDF90054EB36B07983F45AC32F007B1CC0AFCDE437FDC6)
5. 启动调试后，开发者可以通过[调试器](ide-debug-arkts-debugger.md)进行代码调试。

   如有断点会在断点处高亮，并展示当前断点处的Frames和Variables。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/BXLEI26PRhq0rQ6S-BEFgA/zh-cn_image_0000002808766365.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=70AFD2A4841463011267750ED27B4090FD5A3C9C0B140D2B3E109FD690BADDE8)
