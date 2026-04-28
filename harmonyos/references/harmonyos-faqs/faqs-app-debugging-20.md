---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-20
title: 修改代码后使用Hot Reload不支持情况说明
breadcrumb: FAQ > DevEco Studio > 应用调试 > 修改代码后使用Hot Reload不支持情况说明
category: harmonyos-faqs
scraped_at: 2026-04-28T08:30:08+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:6da384026c6d92f2a88927e3892b960f611c749b9db2a72e355191c2ec45d77b
---

**问题现象**

执行热重载过程中，如果当前修改不支持热重载，控制台会打印蓝色重启链接，提示重新安装并重启。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/7kESpiYRSxmIEMXHcnuZDw/zh-cn_image_0000002194318220.png?HW-CC-KV=V1&HW-CC-Date=20260428T003007Z&HW-CC-Expire=86400&HW-CC-Sign=60FA46AB6F421F6BA81073C46AC121680EAB8BAC4B7F1812A9C7D2F7960EEB38 "点击放大")

**解决措施**

DevEco Studio的热重载功能支持特定的代码场景。如果修改的代码超出支持范围，系统将提示“当前修改不支持”，并要求重启。具体支持的代码范围，请参阅[Hot Reload使用约束](../harmonyos-guides/ide-hot-reload.md#section995453874915)。

**常见不支持代码场景**

* 不支持@Entry装饰器的struct Index内成员变量和成员函数的新增或修改。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/iJkLFtL6SMCrXwgRTVVw3g/zh-cn_image_0000002229604013.png?HW-CC-KV=V1&HW-CC-Date=20260428T003007Z&HW-CC-Expire=86400&HW-CC-Sign=2C3C2BD186582388C506AD78A9047746CF8F417BF05492943323E42D03FF4198 "点击放大")
* 不支持@Entry入口文件内class成员函数的新增。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/SK87gg-9TciwBsHcBZthWQ/zh-cn_image_0000002194158608.png?HW-CC-KV=V1&HW-CC-Date=20260428T003007Z&HW-CC-Expire=86400&HW-CC-Sign=8A1D7C67F5268592CFCA1D850CA886FAB341070A8B5A85135FD603D639A3B0B7 "点击放大")
* 不支持@Entry入口文件内枚举的修改。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/FNEeBzthTg-f_EpZPELyvQ/zh-cn_image_0000002194158604.png?HW-CC-KV=V1&HW-CC-Date=20260428T003007Z&HW-CC-Expire=86400&HW-CC-Sign=BFFCC048CF8173FBBE2F05EFFF0965C2B168962FAE4C9DA756215E4F48FA073B "点击放大")
* 不支持import未加载的模块的新增、修改。

  若一个代码文件在热重载启动时未被当前文件导入，则不支持在热重载过程中新增对该代码文件的导入。如下图所示，TestC.ets在热重载启动时未在Index.ets中导入，则在热重载过程中不支持在Index.ets中新增导入TestC.ets的语句。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/GCESsr7YQ4WOjb5Ht89McA/zh-cn_image_0000002229604005.png?HW-CC-KV=V1&HW-CC-Date=20260428T003007Z&HW-CC-Expire=86400&HW-CC-Sign=FBE5721B840A9EFCCF61459862F13135622526A20D1E5B8F7FEB64C2C9D68ACD "点击放大")

  如果热重载启动之前import语句处于置灰状态，此文件在编译过程中将不会被编译，属于未加载的模块。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/LOlcaS0ITHWoklYhQWUImw/zh-cn_image_0000002194318228.png?HW-CC-KV=V1&HW-CC-Date=20260428T003007Z&HW-CC-Expire=86400&HW-CC-Sign=5B8ED540800091F65475709E03F7EC5540FD45F7CEF3FA2CC0E9154484642677 "点击放大")
* 不支持顶层闭包变量的修改（但支持顶层闭包的新增、删除）。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/-SqAwRF4QIS6_umFywapvA/zh-cn_image_0000002229758481.png?HW-CC-KV=V1&HW-CC-Date=20260428T003007Z&HW-CC-Expire=86400&HW-CC-Sign=54430EC2CCBF3A8F5233B06A25E19B9BFADD3100B23EB8092CB400690D76A4B0 "点击放大")
* 支持class类继承，但class继承类和被继承类都不可以放在@Entry入口文件中，建议将class写在非@Entry入口文件中。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/-h55dON9TU67rOCfdPsmAw/zh-cn_image_0000002229604009.png?HW-CC-KV=V1&HW-CC-Date=20260428T003007Z&HW-CC-Expire=86400&HW-CC-Sign=97B5F09BE3F1563DD4E0EED17BB347EC0CAB93134E8E1161DBC0CE24616C2993 "点击放大")
* 不支持@Entry入口文件内大部分装饰器的修改。

  当前Hot Reload不支持大部分装饰器的修改。@Entry入口文件内支持@Styles装饰器的新增和修改，支持@Builder装饰器的修改，但不支持新增，不支持@State装饰器的新增和修改。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/EzoHNj5hQsufHCYAYf99eg/zh-cn_image_0000002229758473.png?HW-CC-KV=V1&HW-CC-Date=20260428T003007Z&HW-CC-Expire=86400&HW-CC-Sign=1A0FDB4F8FE6823372C358891D9ED65BC7C263F6DF271FCBE5976CEC4ED26C82 "点击放大")
* 不支持在@Entry文件内新增、修改其他struct自定义组件。建议以import方式引入。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/l-pgn6BpRoK2sa-wLOFW9A/zh-cn_image_0000002194318224.png?HW-CC-KV=V1&HW-CC-Date=20260428T003007Z&HW-CC-Expire=86400&HW-CC-Sign=F37DFDEA4B7FB91C13A9A366855F25EE1206CC624F431D5B38DEB74E1F8D9A8E "点击放大")
* 不支持在@Entry文件内新增、修改与@State变量重名的class或函数。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/xLN47Y-iSLK802d1L1N4Ag/zh-cn_image_0000002194318216.png?HW-CC-KV=V1&HW-CC-Date=20260428T003007Z&HW-CC-Expire=86400&HW-CC-Sign=CF4628820105965E60F6326DD02079A2363DCC25F54766FFAEF9A3DE48E7DD52 "点击放大")
* 不支持修改非ets/ts代码文件。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/ngnkzVArRJaT27Y2cvUsJw/zh-cn_image_0000002229758489.png?HW-CC-KV=V1&HW-CC-Date=20260428T003007Z&HW-CC-Expire=86400&HW-CC-Sign=FCC7144C603AAF291D4B307B0F203CB1D685E332DB4057465057FFBDD1D22218 "点击放大")
* 不支持修改worker线程文件。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/SDmH0CDXSeGzUNZkMmml4A/zh-cn_image_0000002194158612.png?HW-CC-KV=V1&HW-CC-Date=20260428T003007Z&HW-CC-Expire=86400&HW-CC-Sign=BDC7251D0CA7D81F67208E75329E8C2F804130D343FCCEB7AC040BB3FD24E120 "点击放大")
