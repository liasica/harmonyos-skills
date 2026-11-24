---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-arkts-debug
title: debug启动调试
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > debug启动调试
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:29+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:4da68dc234ea239a9fbc5fe91e4d6d785e23259cc3dc99f5618deffcf24ccaef
---

可以按照如下方式启动调试会话。

1. 如果需要设置断点调试，找到需要暂停的代码片段，点击该代码行的左侧边线，或将光标置于该行上并按Ctrl + F8（macOS为Command+F8）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/rSCyLkV8Sgy9QxUuaDjYVg/zh-cn_image_0000002779566786.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=2D5A16AB647FED36365C4A6C63ED7414E9328D221B88472F2BD139B8097A58AA)

   设置断点后，调试能够在正确的断点处中断，并高亮显示该行。
2. 在设备选择框中，选择调试的设备。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/XNei1dGZRDu3q816p14gPQ/zh-cn_image_0000002779406804.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=E4CE3C2E569E07737766F051F61D93CBB958F92E09CA9032BBBF63D1D11EEE4E)
3. 选择启动调试的配置，在模块选择框中选择需要调试的模块。也可以通过Edit Configurations[配置调试参数](ide-run-debug-configurations.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/66o5gCzSQQGUFjR8W0Uqog/zh-cn_image_0000002808766369.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=6BBFBC2DBF829A9A2A0935296BFDED6E9DACC5A6B4D06D7A122CF991781FD272)
4. 在工具栏中，单击Debug![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/NPASMgTdQjGT2u5jtDyF8g/zh-cn_image_0000002808886447.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=E482E27CD656C3CDC9B82ED8AA8614FECF93F97EDA33BC6D40C334075E83FFA6 "点击放大")。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/aI0MtbcATKWEDums3jDBow/zh-cn_image_0000002779406810.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=B591E943FCF086BA4297CF98D52D33BA53B57C35E15EDE6A2F273DEC5B4A00A2)

   或者在工具栏中Run中选择Debug。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/3z2pi3TuQD2mVMkk26iBuA/zh-cn_image_0000002779406808.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=94AECBEC56ABEEE9D271356E48A63C9F42B69DD2FBE4287942B71A4C260F730B)
5. 启动调试后，开发者可以通过[调试器](ide-debug-arkts-debugger.md)进行代码调试。

   如有断点会在断点处高亮，并展示当前断点处的Frames和Variables。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/Gkeby9HMQDmjF43KmGnARA/zh-cn_image_0000002808766365.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=2BFAD351B5F6F90ADCF4682F2C6E181949A4EA0DB81F289C1FFECFC5F7EA32CD)
