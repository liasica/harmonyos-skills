---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-20
title: 修改代码后使用Hot Reload不支持情况说明
breadcrumb: FAQ > DevEco Studio > 应用调试 > 修改代码后使用Hot Reload不支持情况说明
category: harmonyos-faqs
scraped_at: 2026-04-29T14:21:24+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:30abe56c5de41591a52584fa6dd3c087313253d4df98cb81821af2e505cf25ac
---

**问题现象**

执行热重载过程中，如果当前修改不支持热重载，控制台会打印蓝色重启链接，提示重新安装并重启。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/7kESpiYRSxmIEMXHcnuZDw/zh-cn_image_0000002194318220.png?HW-CC-KV=V1&HW-CC-Date=20260429T062123Z&HW-CC-Expire=86400&HW-CC-Sign=92EA48D590B6B8CA2F7ECB6BC628A4AB052C72F82553787885CDD3F37A8A29EA "点击放大")

**解决措施**

DevEco Studio的热重载功能支持特定的代码场景。如果修改的代码超出支持范围，系统将提示“当前修改不支持”，并要求重启。具体支持的代码范围，请参阅[Hot Reload使用约束](../harmonyos-guides/ide-hot-reload.md#section995453874915)。

**常见不支持代码场景**

* 不支持@Entry装饰器的struct Index内成员变量和成员函数的新增或修改。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/iJkLFtL6SMCrXwgRTVVw3g/zh-cn_image_0000002229604013.png?HW-CC-KV=V1&HW-CC-Date=20260429T062123Z&HW-CC-Expire=86400&HW-CC-Sign=9FB8973CF1AEC369232A5AA24FD2D46A5636ACD0172C3252890EC1480138689D "点击放大")
* 不支持@Entry入口文件内class成员函数的新增。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/SK87gg-9TciwBsHcBZthWQ/zh-cn_image_0000002194158608.png?HW-CC-KV=V1&HW-CC-Date=20260429T062123Z&HW-CC-Expire=86400&HW-CC-Sign=CB0D378CA17DED07FB33E132795DA403E0192BD2547A742043615AB1EB84E941 "点击放大")
* 不支持@Entry入口文件内枚举的修改。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/FNEeBzthTg-f_EpZPELyvQ/zh-cn_image_0000002194158604.png?HW-CC-KV=V1&HW-CC-Date=20260429T062123Z&HW-CC-Expire=86400&HW-CC-Sign=21D5C9D481D2CDF04E5E31C571B2C47F2D60F5DB72F4A628DFADA563C82BDC51 "点击放大")
* 不支持import未加载的模块的新增、修改。

  若一个代码文件在热重载启动时未被当前文件导入，则不支持在热重载过程中新增对该代码文件的导入。如下图所示，TestC.ets在热重载启动时未在Index.ets中导入，则在热重载过程中不支持在Index.ets中新增导入TestC.ets的语句。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/GCESsr7YQ4WOjb5Ht89McA/zh-cn_image_0000002229604005.png?HW-CC-KV=V1&HW-CC-Date=20260429T062123Z&HW-CC-Expire=86400&HW-CC-Sign=8A0AC098EB23EC9034D9620A77423DFCEB137C9923E1BBBDE4E7516013E4770D "点击放大")

  如果热重载启动之前import语句处于置灰状态，此文件在编译过程中将不会被编译，属于未加载的模块。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/LOlcaS0ITHWoklYhQWUImw/zh-cn_image_0000002194318228.png?HW-CC-KV=V1&HW-CC-Date=20260429T062123Z&HW-CC-Expire=86400&HW-CC-Sign=2675C641431B3B50A826EA16D8BDDCFD04773A9F2EE47E67F76EF3A2D34A684F "点击放大")
* 不支持顶层闭包变量的修改（但支持顶层闭包的新增、删除）。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/-SqAwRF4QIS6_umFywapvA/zh-cn_image_0000002229758481.png?HW-CC-KV=V1&HW-CC-Date=20260429T062123Z&HW-CC-Expire=86400&HW-CC-Sign=66D70A504FA635F37D58CFBF80CBF47BF36C16AEB3CFB7FD7F64AA3593392EF6 "点击放大")
* 支持class类继承，但class继承类和被继承类都不可以放在@Entry入口文件中，建议将class写在非@Entry入口文件中。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/-h55dON9TU67rOCfdPsmAw/zh-cn_image_0000002229604009.png?HW-CC-KV=V1&HW-CC-Date=20260429T062123Z&HW-CC-Expire=86400&HW-CC-Sign=B1E965667C0B5502F6496C967CC83ABDD28CEC7643FCDCCAFEBD7116B9593D3F "点击放大")
* 不支持@Entry入口文件内大部分装饰器的修改。

  当前Hot Reload不支持大部分装饰器的修改。@Entry入口文件内支持@Styles装饰器的新增和修改，支持@Builder装饰器的修改，但不支持新增，不支持@State装饰器的新增和修改。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/EzoHNj5hQsufHCYAYf99eg/zh-cn_image_0000002229758473.png?HW-CC-KV=V1&HW-CC-Date=20260429T062123Z&HW-CC-Expire=86400&HW-CC-Sign=DB4F348BB7F27359055A7152E88D0114A5FFD7251B225DF81549AD5430681829 "点击放大")
* 不支持在@Entry文件内新增、修改其他struct自定义组件。建议以import方式引入。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/l-pgn6BpRoK2sa-wLOFW9A/zh-cn_image_0000002194318224.png?HW-CC-KV=V1&HW-CC-Date=20260429T062123Z&HW-CC-Expire=86400&HW-CC-Sign=6DB9630E1857857B5B585423A4363A09A0DCF58220B2C73B735852167FBA9D6F "点击放大")
* 不支持在@Entry文件内新增、修改与@State变量重名的class或函数。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/xLN47Y-iSLK802d1L1N4Ag/zh-cn_image_0000002194318216.png?HW-CC-KV=V1&HW-CC-Date=20260429T062123Z&HW-CC-Expire=86400&HW-CC-Sign=08DB13FCD4341F61A7C74C3B1F7D2045F3D2AC0C7D1B59AF060832E285C2DC12 "点击放大")
* 不支持修改非ets/ts代码文件。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/ngnkzVArRJaT27Y2cvUsJw/zh-cn_image_0000002229758489.png?HW-CC-KV=V1&HW-CC-Date=20260429T062123Z&HW-CC-Expire=86400&HW-CC-Sign=A80206A7B7F27FE8E0B70FD348AD33BCA84A41848D7733601AA64A33FD595523 "点击放大")
* 不支持修改worker线程文件。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/SDmH0CDXSeGzUNZkMmml4A/zh-cn_image_0000002194158612.png?HW-CC-KV=V1&HW-CC-Date=20260429T062123Z&HW-CC-Expire=86400&HW-CC-Sign=2EFFCFA0FCC543436E7B68F18773FD6A3917E456B542FA7928A50403FCBFE1E3 "点击放大")
