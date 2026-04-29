---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-cross-language-debugging
title: 跨语言调试
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 代码调试 > 跨语言调试
category: harmonyos-guides
scraped_at: 2026-04-29T13:46:47+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1b8a1dd2c430bd4415b96d1cc8106d4c54a15e94144286dfb5f7c0322ef17337
---

DevEco Studio支持C++和ArkTS的跨语言调试，可以同时调试这两种语言。整体操作体验与单一语言调试一致，无需额外在对应语言去手动添加断点，提升了使用两种语言混合开发的调试效率。

1. 将DevEco Studio与设备进行连接。如果使用真机设备，请先对应用/元服务进行签名，具体请参考[为应用/元服务进行签名](ide-signing.md)。
2. 在菜单栏单击**Run > Edit Configurations**，选择**Application**下的模块名（如entry），然后在右侧窗口中选择**Debugger**，将**Debug type**设置为“Dual(ArkTS/JS + Native)”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/ItuFdoolRgCUHlfgQznFhw/zh-cn_image_0000002561833555.png?HW-CC-KV=V1&HW-CC-Date=20260429T054646Z&HW-CC-Expire=86400&HW-CC-Sign=0E07A2F1479D4A75BD8049B648874DC1A53642320903AD430427C064B8156BA8)
3. 代码调试执行到ArkTS调用C++方法处，点击Step Into可以进入到对应的C++方法的第一行代码处。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/mU8s_nc1T9OJex9IXzThgA/zh-cn_image_0000002561833553.png?HW-CC-KV=V1&HW-CC-Date=20260429T054646Z&HW-CC-Expire=86400&HW-CC-Sign=0CE3EA8A8B320BA6F63093885B3DAEB82454BF301248960FB4C779899671FB1F)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/Ha-SStdgS9WkwxsBJ6wOzQ/zh-cn_image_0000002561833559.png?HW-CC-KV=V1&HW-CC-Date=20260429T054646Z&HW-CC-Expire=86400&HW-CC-Sign=71CF1DCFA892AD349E8531680C6F64DA64E296A126DCFD506EAB2C1B80E70477)
4. 进入到C++代码后，可以从左下角Frames区域查看C++的调用栈，如需查看对应的ArkTS调用栈，在Frames区域中单击鼠标右键，勾选**Show ArkTs Stack Frame。**点击调用栈可以跳转到对应的代码行。

   说明

   从DevEco Studio 6.0.0 Beta3版本开始，支持查看ArkTS变量，其他变量相关的操作暂不支持。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/9TD-MCG9QLuSjC6mR8FmBg/zh-cn_image_0000002530913630.png?HW-CC-KV=V1&HW-CC-Date=20260429T054646Z&HW-CC-Expire=86400&HW-CC-Sign=A7FDB1EBCEAAAC5823BDC248F640B5BCBEF1681B4AB637D3968ECF84E771C938)
5. ArkTS调用C++方法之后的代码存在断点时，点击Resume可以回到下一个ArkTS断点处，继续进行ArkTS代码调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/IrnX8bB6RVS6l2oZi2d9dg/zh-cn_image_0000002530913634.png?HW-CC-KV=V1&HW-CC-Date=20260429T054646Z&HW-CC-Expire=86400&HW-CC-Sign=D2000E17DD672B0ACA57979490DC37D79FB00869A23C157EBFF4EFFEC985ED13)
