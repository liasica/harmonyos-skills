---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-cross-language-debugging
title: 跨语言调试
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > 跨语言调试
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:fd2119bc6edbaa5e69e38c023b77e8db41031908557c36386256b57dd8cc06fa
---

DevEco Studio支持C++和ArkTS的跨语言调试，可以同时调试这两种语言。整体操作体验与单一语言调试一致，无需额外在对应语言添加断点，提升了使用两种语言混合开发的调试效率。

1. 将DevEco Studio与设备进行连接。如果使用真机设备，请先对应用/元服务进行签名，具体请参考[为应用/元服务进行签名](ide-signing.md)。
2. 在菜单栏单击**Run > Edit Configurations**，选择**Application**下的模块名（如entry），然后在右侧窗口中选择**Debugger**，将**Debug type**设置为“Dual(ArkTS/JS + Native)”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/tG8m2TlXSbeM57PnJevqXQ/zh-cn_image_0000002808767121.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=249B04D07016795229A6AE2D907BB71F7364E0E0BF4A19D4EC4C9ED8A8F403A9)
3. 代码调试执行到ArkTS调用C++方法处，点击Step Into可以进入到对应的C++方法的第一行代码处。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/u1LOKSQ2TfK4gqJPeUouqQ/zh-cn_image_0000002779567544.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=16484113E9D8A0BAD9DD13B0CDEBA7269DA4FD43E39628889EF6B5061588DDC9)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/M6O0D9PMReicVkCO7Xw27Q/zh-cn_image_0000002779407570.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=F309F647C3DBF080DC659613FD67C841C9FB35889A6965C4578C99564CCD52C7)
4. 进入到C++代码后，可以从左下角Frames区域查看C++的调用栈，如需查看对应的ArkTS调用栈，在Frames区域中单击鼠标右键，勾选**Show ArkTS Stack Frame。**点击调用栈可以跳转到对应的代码行。

   **说明** 

   从DevEco Studio 6.0.0 Beta3版本开始，支持查看ArkTS变量，其他变量相关的操作暂不支持。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/zlNYhpJXTQG5ljKvoSV4Fg/zh-cn_image_0000002779567546.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=58C85F1F4B483B4213A4CA25BEEE17E5C1BD0FD5C6771599F13B78AEB043B884)
5. ArkTS调用C++方法之后的代码存在断点时，点击Resume可以回到下一个ArkTS断点处，继续进行ArkTS代码调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/YAWtcCQrRTeYRTb6M0stYQ/zh-cn_image_0000002808887209.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=A6233C110DA37D2E07A1F4E6CD3D03A50D894DFD7AC97FC4FC86541ABC406CD5)
