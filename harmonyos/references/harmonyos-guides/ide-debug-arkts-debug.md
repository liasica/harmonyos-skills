---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-arkts-debug
title: debug启动调试
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > debug启动调试
category: harmonyos-guides
scraped_at: 2026-04-29T13:46:40+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:f06498ab974bea7c7d0afb65b2dc5326c7634673b943a53ea41dbcd6072283ee
---

可以按照如下方式启动调试会话。

1. 如果需要设置断点调试，找到需要暂停的代码片段，点击该代码行的左侧边线，或将光标置于该行上并按Ctrl + F8（macOS为Command+F8）。如果无法添加断点，请查看FAQ[调试过程中无法添加断点](../harmonyos-faqs/faqs-app-debugging-1.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/IyIgMG6gTaKqofZoWP1EQA/zh-cn_image_0000002530912932.png?HW-CC-KV=V1&HW-CC-Date=20260429T054639Z&HW-CC-Expire=86400&HW-CC-Sign=BB447DB0BB27F70F62B5EA367FD09DF71FCD38372DE6842A7EA243C86D5E9F8D)

   设置断点后，调试能够在正确的断点处中断，并高亮显示该行。
2. 在设备选择框中，选择调试的设备。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/8B9ISgbDS0SwrdZhMHueiA/zh-cn_image_0000002530752928.png?HW-CC-KV=V1&HW-CC-Date=20260429T054639Z&HW-CC-Expire=86400&HW-CC-Sign=D84D4C86CB2D4B806B4F09AD99B6A473D15909118A8850150B8709449AD20690)
3. 选择启动调试的配置，在模块选择框中选择需要调试的模块。也可以通过Edit Configurations[配置调试参数](ide-run-debug-configurations.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/celCFX4qTr2dxr6to_8z-A/zh-cn_image_0000002530752940.png?HW-CC-KV=V1&HW-CC-Date=20260429T054639Z&HW-CC-Expire=86400&HW-CC-Sign=E799D2BBBBC5227DEC95AF3C6C4CE79B9EC79389BD62AE50C799F7E4F1C37898)
4. 在工具栏中，单击Debug![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/tuQaprD-RNyKSOYMkcx4yw/zh-cn_image_0000002530912928.png?HW-CC-KV=V1&HW-CC-Date=20260429T054639Z&HW-CC-Expire=86400&HW-CC-Sign=81A189D01CDF5CA9C30EF290EA6356AF686F58D56920C09CFC855AE7C46F9404)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/GTWUdBEpTt2CtDESJ4tpog/zh-cn_image_0000002561832861.png?HW-CC-KV=V1&HW-CC-Date=20260429T054639Z&HW-CC-Expire=86400&HW-CC-Sign=AD9AD96A7D66CF15F52925859C8EFCC527C7E758B1D563D8F360E1B86953F6BB)

   或者在工具栏中Run中选择Debug。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/761fk-FvRk-gMlx2yOi9ZQ/zh-cn_image_0000002561832855.png?HW-CC-KV=V1&HW-CC-Date=20260429T054639Z&HW-CC-Expire=86400&HW-CC-Sign=BDD520817E92CE7E3BBDACB88A78A78DE8E0B580F4470701D051B9CD542A6DAA)
5. 启动调试后，开发者可以通过[调试器](ide-debug-arkts-debugger.md)进行代码调试。

   如有断点会在断点处高亮，并展示当前断点处的Frames和Variables。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/MwkrvM2FTZGiycPvz7vnAQ/zh-cn_image_0000002530912926.png?HW-CC-KV=V1&HW-CC-Date=20260429T054639Z&HW-CC-Expire=86400&HW-CC-Sign=4C1CFD185C49C49A17C006B1940B29213A271DCAC78E923D8C9F82238F189195)
