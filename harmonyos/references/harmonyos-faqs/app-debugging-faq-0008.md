---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/app-debugging-faq-0008
title: DevEco Studio Hot Reload热重载常见问题
breadcrumb: FAQ > DevEco Studio > 应用调试 > 常见问题 > DevEco Studio Hot Reload热重载常见问题
category: harmonyos-faqs
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:96aa726c876abe86ed7513dd0027e88eeabe2b4e07aa87acf3b0f0440d856a8e
---

**Q：修改代码后使用Hot Reload不支持的情况有哪些？**

**A**：问题现象：执行热重载过程中，如果当前修改不支持热重载，控制台会打印蓝色重启链接，提示重新安装并重启。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/UAmW2ygUQOyhf-KYM6OSqg/zh-cn_image_0000002801279197.png?HW-CC-KV=V1&HW-CC-Date=20261112T233141Z&HW-CC-Expire=31536000000&HW-CC-Sign=63FB2451C57C57E962385239850F8D689224D422E72EA6137365178B43780816 "点击放大")

解决措施：DevEco Studio的热重载功能支持特定的代码场景。如果修改的代码超出支持范围，系统将提示“当前修改不支持”，并要求重启。具体支持的代码范围，请参阅[Hot Reload使用约束](../harmonyos-guides/ide-hot-reload.md#section995453874915)。

常见不支持代码场景：

* 不支持@Entry装饰器的struct Index内成员变量和成员函数的新增或修改。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/Sov4Io3oTtGd7CZfe8TICA/zh-cn_image_0000002772005654.png?HW-CC-KV=V1&HW-CC-Date=20261112T233141Z&HW-CC-Expire=31536000000&HW-CC-Sign=8A8F103980FED7E9C2E384DCFA2C2D197073CCF361FEC28EC0D89C2F2FD5C81A "点击放大")
* 不支持@Entry入口文件内class成员函数的新增。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/wKazSFQyRg-j52qgwODLew/zh-cn_image_0000002801285505.png?HW-CC-KV=V1&HW-CC-Date=20261112T233141Z&HW-CC-Expire=31536000000&HW-CC-Sign=117E0DAD0B611620A828C1A0DC20A4333DE80F28D18C890C645CEDF49071B923 "点击放大")
* 不支持@Entry入口文件内枚举的修改。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/yVY2-mTfRGWTYBZj8YrQQQ/zh-cn_image_0000002801405429.png?HW-CC-KV=V1&HW-CC-Date=20261112T233141Z&HW-CC-Expire=31536000000&HW-CC-Sign=395F4BD2273BD78EF1FDD06F0F6F15007A7E50F9C14985BCD6EFFBF48A205186 "点击放大")

* 不支持import未加载的模块的新增、修改。

  若一个代码文件在热重载启动时未被当前文件导入，则不支持在热重载过程中新增对该代码文件的导入。如下图所示，TestC.ets在热重载启动时未在Index.ets中导入，则在热重载过程中不支持在Index.ets中新增导入TestC.ets的语句。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/6ke_6yUaQ4OgojXhXAvjNg/zh-cn_image_0000002772165638.png?HW-CC-KV=V1&HW-CC-Date=20261112T233141Z&HW-CC-Expire=31536000000&HW-CC-Sign=13EC700F15AD275AB8F550B72E50A67BB8B39FBCD0866E024D7DE69CD286B875 "点击放大")

  如果热重载启动之前import语句处于置灰状态，此文件在编译过程中将不会被编译，属于未加载的模块。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/ymyR1ZiIQO6thbZEEICT_Q/zh-cn_image_0000002772005664.png?HW-CC-KV=V1&HW-CC-Date=20261112T233141Z&HW-CC-Expire=31536000000&HW-CC-Sign=771B78D00A0B29BA3849C8736A53F1B2170759E60923A216FE2E1611EE79FFF8 "点击放大")
* 不支持顶层闭包变量的修改（但支持顶层闭包的新增、删除）。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/v8V5NOOuR3aRDc-lT8ByZw/zh-cn_image_0000002801285515.png?HW-CC-KV=V1&HW-CC-Date=20261112T233141Z&HW-CC-Expire=31536000000&HW-CC-Sign=9FF2BD19C114399CB2DD40EC7B7E1BE717651A2E9ED72C9BDA1FD6B3CDE13F7E "点击放大")
* 支持class类继承，但class继承类和被继承类都不可以放在@Entry入口文件中，建议将class写在非@Entry入口文件中。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/JRsQKF1zQwWWDxQa5-Ag-Q/zh-cn_image_0000002801405463.png?HW-CC-KV=V1&HW-CC-Date=20261112T233141Z&HW-CC-Expire=31536000000&HW-CC-Sign=EA347811A551177C8CA4261A7509E7BA1F0411E764F8CFC5C6A783FA31016834 "点击放大")
* 不支持@Entry入口文件内大部分装饰器的修改。

  当前Hot Reload不支持大部分装饰器的修改。@Entry入口文件内支持@Styles装饰器的新增和修改，支持@Builder装饰器的修改，但不支持新增，不支持@State装饰器的新增和修改。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/IRFxJhtdQ4yJ9kFb2WLf3g/zh-cn_image_0000002772165676.png?HW-CC-KV=V1&HW-CC-Date=20261112T233141Z&HW-CC-Expire=31536000000&HW-CC-Sign=7130076D98372DB404D38A74D98EE7B7F0D8166550272E26DE6EF29375A591C5 "点击放大")
* 不支持在@Entry文件内新增、修改其他struct自定义组件。建议以import方式引入。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/2pIetYYnR02c21mnF8jZLA/zh-cn_image_0000002772005706.png?HW-CC-KV=V1&HW-CC-Date=20261112T233141Z&HW-CC-Expire=31536000000&HW-CC-Sign=E6068E7E73CD35975FA6DA1D8AFDEF9070C98FDE8A3395207AC1572A3EE98DD4 "点击放大")
* 不支持在@Entry文件内新增、修改与@State变量重名的class或函数。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/PI0Dvef_QGOrnpofVX45qg/zh-cn_image_0000002801285559.png?HW-CC-KV=V1&HW-CC-Date=20261112T233141Z&HW-CC-Expire=31536000000&HW-CC-Sign=635EE822966828340D32E54AA25EEC0182DB598F9FBB310A235628590EBB56CB "点击放大")
* 不支持修改非ets/ts代码文件。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/Ca5mcueZRWa5vXewTDuJjQ/zh-cn_image_0000002801405487.png?HW-CC-KV=V1&HW-CC-Date=20261112T233141Z&HW-CC-Expire=31536000000&HW-CC-Sign=0DC46F9BA001D186DC8D310B938586EB50A78C39D4791C957EE6E8554F69F26D "点击放大")

* 不支持修改worker线程文件。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/3wa70e86TSquRYt7NL8g2Q/zh-cn_image_0000002772165700.png?HW-CC-KV=V1&HW-CC-Date=20261112T233141Z&HW-CC-Expire=31536000000&HW-CC-Sign=E7C0117AF67D1EBB7765911923E935248786F23D826033A614E9F8467F59B8E9 "点击放大")
