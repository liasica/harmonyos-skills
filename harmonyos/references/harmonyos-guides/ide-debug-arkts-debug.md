---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-arkts-debug
title: debug启动调试
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > debug启动调试
category: harmonyos-guides
scraped_at: 2026-11-07T08:02:22+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:9f436aca545fb37cf336abf91f6627b078661e875b405c111e90794030e38b08
---

可以按照如下方式启动调试会话。

1. 如果需要设置断点调试，找到需要暂停的代码片段，点击该代码行的左侧边线，或将光标置于该行上并按Ctrl + F8（macOS为Command+F8）。如果无法添加断点，请查看FAQ[调试过程中无法添加断点](../harmonyos-faqs/faqs-app-debugging-1.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/rTeSzskdR2SdNLiVTfbTeQ/zh-cn_image_0000002701822706.png)

   设置断点后，调试能够在正确的断点处中断，并高亮显示该行。
2. 在设备选择框中，选择调试的设备。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/RAVCEVkaQ7ONKEIPZvd_lA/zh-cn_image_0000002701662782.png)
3. 选择启动调试的配置，在模块选择框中选择需要调试的模块。也可以通过Edit Configurations[配置调试参数](ide-run-debug-configurations.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/rIVKiU5PSDa0M1Ik8Ve1pQ/zh-cn_image_0000002731541975.png)
4. 在工具栏中，单击Debug![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/o_0Eq9WeTDS5k6V-fltnnA/zh-cn_image_0000002731382003.png "点击放大")。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/E63mH6TZTuCi_H7_iSFpWQ/zh-cn_image_0000002731382007.png)

   或者在工具栏中Run中选择Debug。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/FLSQz7EzSY-dB6kxm5lIXQ/zh-cn_image_0000002731541981.png)
5. 启动调试后，开发者可以通过[调试器](ide-debug-arkts-debugger.md)进行代码调试。

   如有断点会在断点处高亮，并展示当前断点处的Frames和Variables。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/unICTl49QeOJOglU5gJIGg/zh-cn_image_0000002701822704.png)
