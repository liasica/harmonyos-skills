---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/app-debugging-faq-0008
title: DevEco Studio Hot Reload热重载常见问题
breadcrumb: FAQ > DevEco Studio > 应用调试 > 常见问题 > DevEco Studio Hot Reload热重载常见问题
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:59+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:96aa726c876abe86ed7513dd0027e88eeabe2b4e07aa87acf3b0f0440d856a8e
---

**Q：修改代码后使用Hot Reload不支持的情况有哪些？**

**A**：问题现象：执行热重载过程中，如果当前修改不支持热重载，控制台会打印蓝色重启链接，提示重新安装并重启。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/UAmW2ygUQOyhf-KYM6OSqg/zh-cn_image_0000002801279197.png "点击放大")

解决措施：DevEco Studio的热重载功能支持特定的代码场景。如果修改的代码超出支持范围，系统将提示“当前修改不支持”，并要求重启。具体支持的代码范围，请参阅[Hot Reload使用约束](../harmonyos-guides/ide-hot-reload.md#section995453874915)。

常见不支持代码场景：

* 不支持@Entry装饰器的struct Index内成员变量和成员函数的新增或修改。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/Sov4Io3oTtGd7CZfe8TICA/zh-cn_image_0000002772005654.png "点击放大")
* 不支持@Entry入口文件内class成员函数的新增。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/wKazSFQyRg-j52qgwODLew/zh-cn_image_0000002801285505.png "点击放大")
* 不支持@Entry入口文件内枚举的修改。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/yVY2-mTfRGWTYBZj8YrQQQ/zh-cn_image_0000002801405429.png "点击放大")

* 不支持import未加载的模块的新增、修改。

  若一个代码文件在热重载启动时未被当前文件导入，则不支持在热重载过程中新增对该代码文件的导入。如下图所示，TestC.ets在热重载启动时未在Index.ets中导入，则在热重载过程中不支持在Index.ets中新增导入TestC.ets的语句。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/6ke_6yUaQ4OgojXhXAvjNg/zh-cn_image_0000002772165638.png "点击放大")

  如果热重载启动之前import语句处于置灰状态，此文件在编译过程中将不会被编译，属于未加载的模块。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/ymyR1ZiIQO6thbZEEICT_Q/zh-cn_image_0000002772005664.png "点击放大")
* 不支持顶层闭包变量的修改（但支持顶层闭包的新增、删除）。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/v8V5NOOuR3aRDc-lT8ByZw/zh-cn_image_0000002801285515.png "点击放大")
* 支持class类继承，但class继承类和被继承类都不可以放在@Entry入口文件中，建议将class写在非@Entry入口文件中。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/JRsQKF1zQwWWDxQa5-Ag-Q/zh-cn_image_0000002801405463.png "点击放大")
* 不支持@Entry入口文件内大部分装饰器的修改。

  当前Hot Reload不支持大部分装饰器的修改。@Entry入口文件内支持@Styles装饰器的新增和修改，支持@Builder装饰器的修改，但不支持新增，不支持@State装饰器的新增和修改。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/IRFxJhtdQ4yJ9kFb2WLf3g/zh-cn_image_0000002772165676.png "点击放大")
* 不支持在@Entry文件内新增、修改其他struct自定义组件。建议以import方式引入。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/2pIetYYnR02c21mnF8jZLA/zh-cn_image_0000002772005706.png "点击放大")
* 不支持在@Entry文件内新增、修改与@State变量重名的class或函数。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/PI0Dvef_QGOrnpofVX45qg/zh-cn_image_0000002801285559.png "点击放大")
* 不支持修改非ets/ts代码文件。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/Ca5mcueZRWa5vXewTDuJjQ/zh-cn_image_0000002801405487.png "点击放大")

* 不支持修改worker线程文件。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/3wa70e86TSquRYt7NL8g2Q/zh-cn_image_0000002772165700.png "点击放大")
