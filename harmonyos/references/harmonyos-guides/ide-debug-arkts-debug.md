---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-arkts-debug
title: debug启动调试
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > debug启动调试
category: harmonyos-guides
scraped_at: 2026-10-11T07:23:02+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:75cfd3268715f999242beb42505eb2a0b51ef19b787896f61df500d865810191
---

可以按照如下方式启动调试会话。

1. 如果需要设置断点调试，找到需要暂停的代码片段，点击该代码行的左侧边线，或将光标置于该行上并按Ctrl + F8（macOS为Command+F8）。如果无法添加断点，请查看FAQ[调试过程中无法添加断点](../harmonyos-faqs/faqs-app-debugging-1.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/9_wpw0KlSPqk8miMRV9KpA/zh-cn_image_0000002701822706.png)

   设置断点后，调试能够在正确的断点处中断，并高亮显示该行。
2. 在设备选择框中，选择调试的设备。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/CubIBVc_QPuVjoPELCLCMw/zh-cn_image_0000002701662782.png)
3. 选择启动调试的配置，在模块选择框中选择需要调试的模块。也可以通过Edit Configurations[配置调试参数](ide-run-debug-configurations.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/r3wfXHaeR4qfvJwx5rNx8g/zh-cn_image_0000002731541975.png)
4. 在工具栏中，单击Debug![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/F1duzmJ8SE6aN57DQvafrw/zh-cn_image_0000002731382003.png "点击放大")。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/gvVM8ScOSrm0XJGlhARlGQ/zh-cn_image_0000002731382007.png)

   或者在工具栏中Run中选择Debug。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/UD-1xVZtSFCHw0jgzIBaEQ/zh-cn_image_0000002731541981.png)
5. 启动调试后，开发者可以通过[调试器](ide-debug-arkts-debugger.md)进行代码调试。

   如有断点会在断点处高亮，并展示当前断点处的Frames和Variables。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/WKFBXiDYRW2I-t_GbpKPLw/zh-cn_image_0000002701822704.png)
