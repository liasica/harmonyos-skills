---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-20
title: 修改代码后使用Hot Reload不支持情况说明
breadcrumb: FAQ > DevEco Studio > 应用调试 > 修改代码后使用Hot Reload不支持情况说明
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:59+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:7880994eb9d62a354c291ddbe8bfe7cf80222ee0936d98c27253836f3abc0eee
---

**问题现象**

执行热重载过程中，如果当前修改不支持热重载，控制台会打印蓝色重启链接，提示重新安装并重启。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/fwRyX8auQimP0zuPQDYcNw/zh-cn_image_0000002654798153.png "点击放大")

**解决措施**

DevEco Studio的热重载功能支持特定的代码场景。如果修改的代码超出支持范围，系统将提示“当前修改不支持”，并要求重启。具体支持的代码范围，请参阅[Hot Reload使用约束](../harmonyos-guides/ide-hot-reload.md#section995453874915)。

**常见不支持代码场景**

* 不支持@Entry装饰器的struct Index内成员变量和成员函数的新增或修改。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/v-vgVzk9QcKxERnaolIPnA/zh-cn_image_0000002624638696.png "点击放大")
* 不支持@Entry入口文件内class成员函数的新增。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/TCXKXXEUSzWRQhocFM8eSA/zh-cn_image_0000002654838107.png "点击放大")
* 不支持@Entry入口文件内枚举的修改。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/wvMiqP5pRz2QhF_cRJftRg/zh-cn_image_0000002624478790.png "点击放大")
* 不支持import未加载的模块的新增、修改。

  若一个代码文件在热重载启动时未被当前文件导入，则不支持在热重载过程中新增对该代码文件的导入。如下图所示，TestC.ets在热重载启动时未在Index.ets中导入，则在热重载过程中不支持在Index.ets中新增导入TestC.ets的语句。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/4RXRtS_aQ-CpgDeeBAByhw/zh-cn_image_0000002654798157.png "点击放大")

  如果热重载启动之前import语句处于置灰状态，此文件在编译过程中将不会被编译，属于未加载的模块。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/440N3k_pQPaCxzUXE0rmXg/zh-cn_image_0000002624638698.png "点击放大")
* 不支持顶层闭包变量的修改（但支持顶层闭包的新增、删除）。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/siS4WaXnT-Ka1iBI0OGkmw/zh-cn_image_0000002654838109.png "点击放大")
* 支持class类继承，但class继承类和被继承类都不可以放在@Entry入口文件中，建议将class写在非@Entry入口文件中。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/SGmMz1UzQ3K3CyhPxQKSXg/zh-cn_image_0000002624478792.png "点击放大")
* 不支持@Entry入口文件内大部分装饰器的修改。

  当前Hot Reload不支持大部分装饰器的修改。@Entry入口文件内支持@Styles装饰器的新增和修改，支持@Builder装饰器的修改，但不支持新增，不支持@State装饰器的新增和修改。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/jHoRNaf7Tj6dHKvfLzKCJA/zh-cn_image_0000002654798159.png "点击放大")
* 不支持在@Entry文件内新增、修改其他struct自定义组件。建议以import方式引入。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/XyK1d0RZR3CtU-bNTsqlOA/zh-cn_image_0000002624638700.png "点击放大")
* 不支持在@Entry文件内新增、修改与@State变量重名的class或函数。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/jkCsvjS_QTir7IXzWDmP2g/zh-cn_image_0000002654838113.png "点击放大")
* 不支持修改非ets/ts代码文件。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/I9_p5_GEQQqTCvkPHz39gw/zh-cn_image_0000002624478794.png "点击放大")
* 不支持修改worker线程文件。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/WFQ0abjoSo-LPpMzaQx23g/zh-cn_image_0000002654798161.png "点击放大")
