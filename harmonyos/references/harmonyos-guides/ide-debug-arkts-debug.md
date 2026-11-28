---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-arkts-debug
title: debug启动调试
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > debug启动调试
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:38+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:333875982d16e13e603a889552dc97033ce9593d57316dad1a19b7dfd436f582
---

可以按照如下方式启动调试会话。

1. 如果需要设置断点调试，找到需要暂停的代码片段，点击该代码行的左侧边线，或将光标置于该行上并按Ctrl + F8（macOS为Command+F8）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/eCKDSgTKTUOBLeFEJofrqg/zh-cn_image_0000002779566786.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=4C965B127E1EF31CC208B6AB994875F2B5D4A4E9C7380190400A9F8858DCD1A8)

   设置断点后，调试能够在正确的断点处中断，并高亮显示该行。
2. 在设备选择框中，选择调试的设备。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/2jXtpNUsQZWzE0_Tw6siCA/zh-cn_image_0000002779406804.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=BBD05F552912D9878764A6E4369EA31BB349F73DC99828A62733612CEC7C30D5)
3. 选择启动调试的配置，在模块选择框中选择需要调试的模块。也可以通过Edit Configurations[配置调试参数](ide-run-debug-configurations.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/H6ziMjwFS2mTe-twBs363A/zh-cn_image_0000002808766369.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=05089FA6C8E007B87413C9612060104B43CB52FFB322503ADDDEA03F10051734)
4. 在工具栏中，单击Debug![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/0NBKc5xrRYK0VTZNZyPMhQ/zh-cn_image_0000002808886447.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=A13BA53B6F2C3DFBBEF456320366BC3914165CFE1EE4DD33D9A0B6A532811ED8 "点击放大")。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/2dBXObNsS1eeLKwM9sUrUQ/zh-cn_image_0000002779406810.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=ACD5B83CBCBC4A8AD9F42909409381D2F901E9884064D80D16E183BA1535EF7E)

   或者在工具栏中Run中选择Debug。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/-qylCwj_Rh-T_BSCMH8dqg/zh-cn_image_0000002779406808.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=9349BD7E7818FE0C9F83C7DC38E8B994D882A84C42F3A723B65E53B6B7A68E31)
5. 启动调试后，开发者可以通过[调试器](ide-debug-arkts-debugger.md)进行代码调试。

   如有断点会在断点处高亮，并展示当前断点处的Frames和Variables。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/fmsLhRm8RRGf7laKD2ckkQ/zh-cn_image_0000002808766365.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=5FD1A7E79C359F04C4C60D2799F4121844948544C066CA0DC7543FA0E5A2A84E)
