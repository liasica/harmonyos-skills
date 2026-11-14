---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-cross-language-debugging
title: 跨语言调试
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > 跨语言调试
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:59+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:69a3f786cc40d65cb85f1640d5559041f0c8c2f3dff71cf9e85920eacfa02fbe
---

DevEco Studio支持C++和ArkTS的跨语言调试，可以同时调试这两种语言。整体操作体验与单一语言调试一致，无需额外在对应语言添加断点，提升了使用两种语言混合开发的调试效率。

1. 将DevEco Studio与设备进行连接。如果使用真机设备，请先对应用/元服务进行签名，具体请参考[为应用/元服务进行签名](ide-signing.md)。
2. 在菜单栏单击**Run > Edit Configurations**，选择**Application**下的模块名（如entry），然后在右侧窗口中选择**Debugger**，将**Debug type**设置为“Dual(ArkTS/JS + Native)”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/CBDTgWCuSNWApt8n_03oAw/zh-cn_image_0000002808767121.png?HW-CC-KV=V1&HW-CC-Date=20261114T004859Z&HW-CC-Expire=31536000000&HW-CC-Sign=747A425EF4CD53DA8E73F655FD8B0771952182D57B6E8E797C1D4FEC475D7E89)
3. 代码调试执行到ArkTS调用C++方法处，点击Step Into可以进入到对应的C++方法的第一行代码处。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/0ZFaW56ERWm1IhhqiZN5Eg/zh-cn_image_0000002779567544.png?HW-CC-KV=V1&HW-CC-Date=20261114T004859Z&HW-CC-Expire=31536000000&HW-CC-Sign=F018038DE3226A1A9517324B34B8593448706A62C5C033C98AE7776328AB17AA)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/LEhEFhqkSseXTVen0PH3tQ/zh-cn_image_0000002779407570.png?HW-CC-KV=V1&HW-CC-Date=20261114T004859Z&HW-CC-Expire=31536000000&HW-CC-Sign=7A748C4DE38D944D05E92407EA2004E25FA88638638318BADC2ADB2A295E9BD7)
4. 进入到C++代码后，可以从左下角Frames区域查看C++的调用栈，如需查看对应的ArkTS调用栈，在Frames区域中单击鼠标右键，勾选**Show ArkTS Stack Frame。**点击调用栈可以跳转到对应的代码行。

   **说明** 

   从DevEco Studio 6.0.0 Beta3版本开始，支持查看ArkTS变量，其他变量相关的操作暂不支持。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/mVhGGGn1QZCQvKOVtpWKIw/zh-cn_image_0000002779567546.png?HW-CC-KV=V1&HW-CC-Date=20261114T004859Z&HW-CC-Expire=31536000000&HW-CC-Sign=293D5893266C6744668B1D4D47F3A9E84E2F62BEC6FAC50D3E3620D876A1AD65)
5. ArkTS调用C++方法之后的代码存在断点时，点击Resume可以回到下一个ArkTS断点处，继续进行ArkTS代码调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/OCvIfLb3Rt6DcKgfWWxO3g/zh-cn_image_0000002808887209.png?HW-CC-KV=V1&HW-CC-Date=20261114T004859Z&HW-CC-Expire=31536000000&HW-CC-Sign=8F867D4129A67C187BC2F5AB471D37C788DA874F72A96B59F0956DA21FFE8800)
