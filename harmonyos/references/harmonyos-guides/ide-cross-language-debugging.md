---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-cross-language-debugging
title: 跨语言调试
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 代码调试 > 跨语言调试
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:51+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:02b55583b41e44f1c49a79cc5bf8423e7acf590787a0af5dd7f9eb9dac04578f
---

DevEco Studio支持C++和ArkTS的跨语言调试，可以同时调试这两种语言。整体操作体验与单一语言调试一致，无需额外在对应语言去手动添加断点，提升了使用两种语言混合开发的调试效率。

1. 将DevEco Studio与设备进行连接。如果使用真机设备，请先对应用/元服务进行签名，具体请参考[为应用/元服务进行签名](ide-signing.md)。
2. 在菜单栏单击**Run > Edit Configurations**，选择**Application**下的模块名（如entry），然后在右侧窗口中选择**Debugger**，将**Debug type**设置为“Dual(ArkTS/JS + Native)”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/YurAWsJiQxKHA6vCm5nEhg/zh-cn_image_0000002561833555.png?HW-CC-KV=V1&HW-CC-Date=20260427T235650Z&HW-CC-Expire=86400&HW-CC-Sign=49097CF036C2D18AFE225C7E080B33FCD5178C6DC947E66883B52A9C8972020A)
3. 代码调试执行到ArkTS调用C++方法处，点击Step Into可以进入到对应的C++方法的第一行代码处。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/zOpv57OyTFypi_8iW_j7ig/zh-cn_image_0000002561833553.png?HW-CC-KV=V1&HW-CC-Date=20260427T235650Z&HW-CC-Expire=86400&HW-CC-Sign=7855449D0BBF49F62BB15CC97D13FF4D22651317502BE9DCACFC69628C78898D)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/9nNN_X-kSdmmfsiM1u3kjQ/zh-cn_image_0000002561833559.png?HW-CC-KV=V1&HW-CC-Date=20260427T235650Z&HW-CC-Expire=86400&HW-CC-Sign=CBB005FC3E574C988C42A205D9973BE70C194C757F5CD33736497FA9FAC37390)
4. 进入到C++代码后，可以从左下角Frames区域查看C++的调用栈，如需查看对应的ArkTS调用栈，在Frames区域中单击鼠标右键，勾选**Show ArkTs Stack Frame。**点击调用栈可以跳转到对应的代码行。

   说明

   从DevEco Studio 6.0.0 Beta3版本开始，支持查看ArkTS变量，其他变量相关的操作暂不支持。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/7S4wl9OFT5W8OrFFRlGfgQ/zh-cn_image_0000002530913630.png?HW-CC-KV=V1&HW-CC-Date=20260427T235650Z&HW-CC-Expire=86400&HW-CC-Sign=285350834A53175147204B83484FAE0081A944BEDF0321CA2031869BE554D6A6)
5. ArkTS调用C++方法之后的代码存在断点时，点击Resume可以回到下一个ArkTS断点处，继续进行ArkTS代码调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/re0Ty_YQRtGUiTNcyQMaQw/zh-cn_image_0000002530913634.png?HW-CC-KV=V1&HW-CC-Date=20260427T235650Z&HW-CC-Expire=86400&HW-CC-Sign=260A4122AD39381EBB8123073C388813CB15AC6B9CF2F36357886F55894784EF)
