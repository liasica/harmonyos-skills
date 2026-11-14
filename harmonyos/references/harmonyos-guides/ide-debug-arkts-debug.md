---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-arkts-debug
title: debug启动调试
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > debug启动调试
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:59+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:8b56acbbbccd3a950c33f90ad2a03c5c57674751a0397e45c107756ee74844dc
---

可以按照如下方式启动调试会话。

1. 如果需要设置断点调试，找到需要暂停的代码片段，点击该代码行的左侧边线，或将光标置于该行上并按Ctrl + F8（macOS为Command+F8）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/VXGeInHLQy61n40HEt59Tg/zh-cn_image_0000002779566786.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=92A8E21B65E4F37BA4CA8069EC7C4C4F35553A9D43AAD9436A75399FE3907A6C)

   设置断点后，调试能够在正确的断点处中断，并高亮显示该行。
2. 在设备选择框中，选择调试的设备。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/wfOtqrxlTNS8x_k_9FhonQ/zh-cn_image_0000002779406804.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=32C7E304396210A873FB1DB0D574A1FA8A67F639ADDF04871E8ABD89D30C3A15)
3. 选择启动调试的配置，在模块选择框中选择需要调试的模块。也可以通过Edit Configurations[配置调试参数](ide-run-debug-configurations.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/DcbjQ38nS9exB7vybawnzw/zh-cn_image_0000002808766369.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=A43C88AFC220AC131C0199D6D230F3AA0A6C5A414DE4484E13A82C009E48ADF9)
4. 在工具栏中，单击Debug![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/YNBGVW9KQJaxlHKpriiRHA/zh-cn_image_0000002808886447.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=F59E5C4C8BAE2A2DE51A840C00F646B9FE3415B371EA3E21BFA86D4C3ACF21DC "点击放大")。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/osPH2ftGTbWM1UZTaBkRVw/zh-cn_image_0000002779406810.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=B553A2F5E1B16B9CD9B40E9CDE61BE30F67DB17E9F38DBBD10000AF0217C2F25)

   或者在工具栏中Run中选择Debug。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/5x84wI1AQQagS-UWgOipAQ/zh-cn_image_0000002779406808.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=2776F22745A69A43168EB407BD3FF40227248CA6BFDFAC2DA77107BFEA09378D)
5. 启动调试后，开发者可以通过[调试器](ide-debug-arkts-debugger.md)进行代码调试。

   如有断点会在断点处高亮，并展示当前断点处的Frames和Variables。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/g37C1-hrTQaDGFmbQLAuJg/zh-cn_image_0000002808766365.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=0B66686F09D5FC1FAFF9A10BB219EE23B5F06F28347AADEC258030105805A497)
