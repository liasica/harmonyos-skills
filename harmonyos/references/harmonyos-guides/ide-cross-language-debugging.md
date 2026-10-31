---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-cross-language-debugging
title: 跨语言调试
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > 跨语言调试
category: harmonyos-guides
scraped_at: 2026-11-01T07:12:54+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:f9919c7d28ed26e4578a45538ec4585ad5a7b9ff2d42f27421f31e40a8bb8445
---

DevEco Studio支持C++和ArkTS的跨语言调试，可以同时调试这两种语言。整体操作体验与单一语言调试一致，无需额外在对应语言添加断点，提升了使用两种语言混合开发的调试效率。

1. 将DevEco Studio与设备进行连接。如果使用真机设备，请先对应用/元服务进行签名，具体请参考[为应用/元服务进行签名](ide-signing.md)。
2. 在菜单栏单击**Run > Edit Configurations**，选择**Application**下的模块名（如entry），然后在右侧窗口中选择**Debugger**，将**Debug type**设置为“Dual(ArkTS/JS + Native)”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/F3PnZLYMRIaUATJ-aM2YhQ/zh-cn_image_0000002731543133.png)
3. 代码调试执行到ArkTS调用C++方法处，点击Step Into可以进入到对应的C++方法的第一行代码处。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/iMb3EGLFQJ2w2Z28N0kcQw/zh-cn_image_0000002731383161.png)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/WZkcPHZJRr6CYUERXPE_ZQ/zh-cn_image_0000002731543131.png)
4. 进入到C++代码后，可以从左下角Frames区域查看C++的调用栈，如需查看对应的ArkTS调用栈，在Frames区域中单击鼠标右键，勾选**Show ArkTS Stack Frame。**点击调用栈可以跳转到对应的代码行。

   **说明** 

   从DevEco Studio 6.0.0 Beta3版本开始，支持查看ArkTS变量，其他变量相关的操作暂不支持。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/f17t9GxjTju4Ka0IpSI5vg/zh-cn_image_0000002701823858.png)
5. ArkTS调用C++方法之后的代码存在断点时，点击Resume可以回到下一个ArkTS断点处，继续进行ArkTS代码调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/oiX_YB6vR3GL5eJgLuaXnA/zh-cn_image_0000002701663936.png)
