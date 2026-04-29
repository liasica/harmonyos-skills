---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-previewer-arkts-js
title: 查看ArkTS/JS预览效果
breadcrumb: 指南 > 编写与调试应用 > 界面预览 > 查看ArkTS/JS预览效果
category: harmonyos-guides
scraped_at: 2026-04-29T13:46:32+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7f71cec8f4758a3f5f7637675c83278edc5267db60b4da511482613d8e7979f1
---

预览器支持ArkTS/JS应用/元服务“实时预览”和“动态预览”。

说明

* 预览支持Phone、Tablet、2in1、Car、Wearable、TV设备的ArkTS工程，支持LiteWearable和Wearable设备的JS工程。
* 预览器功能依赖于电脑显卡的OpenGL版本，OpenGL版本要求为3.2及以上。
* 预览时将不会运行Ability生命周期。
* 从DevEco Studio 6.0.0 Beta3版本开始，HAP/HSP引用HSP时支持预览，HAR模块引用HSP不支持预览，请直接在HSP内预览或为该HSP[设置Mock实现](ide-previewer-mock.md)。
* 预览场景下，不支持通过相对路径及绝对路径的方式访问resources目录下的文件。
* 预览不支持组件拖拽。
* 部分API不支持预览，如Ability、App、MultiMedia等模块。
* Richtext、Web、Video、XComponent组件不支持预览。
* 不支持调用C++库的预览。
* HAR在被应用/元服务使用时真机效果有区别，真机上实际效果应用不显示menubar，元服务显示menubar，但预览器都以不显示menubar为准。若开发HAR模块，请注意被元服务使用时预览器效果与真机效果的不同。

* **实时预览**：在开发界面UI代码过程中，如果添加或删除了UI组件，您只需**Ctrl+S**进行保存，然后预览器就会立即刷新预览结果。如果修改了组件的属性，则预览器会实时（亚秒级）刷新预览结果，达到极速预览的效果（当前版本极速预览仅支持ArkTS组件。支持部分数据绑定场景，如@State装饰的变量）。实时预览默认开启，如果不需要实时预览，请单击预览器右上角![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/AdlMQry1QsKerIWnwMPZfQ/zh-cn_image_0000002530912978.png?HW-CC-KV=V1&HW-CC-Date=20260429T054631Z&HW-CC-Expire=86400&HW-CC-Sign=663AF729BDAE1EDD70A638DA38758DDAF0E42B11F490A14F900EE92957C307E8)按钮，关闭实时预览功能。

  说明

  开发者修改resources/base/profile目录下的配置文件（如main\_pages.json/form\_config.json），不支持触发实时预览，开发者需要点击重新加载![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/V1z1cPncR5KVD8U8eT3FNw/zh-cn_image_0000002561752919.png?HW-CC-KV=V1&HW-CC-Date=20260429T054631Z&HW-CC-Expire=86400&HW-CC-Sign=125C0CCDFD2D1FB332E35678B0F349FA6E009A1D4F96DB36807DCDE8C49F283F)。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/knqQf5ccSFmxOJMcXiQBaA/zh-cn_image_0000002561832907.gif?HW-CC-KV=V1&HW-CC-Date=20260429T054631Z&HW-CC-Expire=86400&HW-CC-Sign=C52CE429FCD6D49A19CE96AEA0E2D54CD2A4519A6C6BF7B07849CD24910F8F34 "点击放大")
* **动态预览**：在预览器界面，可以在预览器中操作应用/元服务的界面交互动作，如单击、跳转、滑动等，与应用/元服务运行在真机设备上的界面交互体验一致。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/J0CLk9KDQOuUcWesSR0eWQ/zh-cn_image_0000002561752927.gif?HW-CC-KV=V1&HW-CC-Date=20260429T054631Z&HW-CC-Expire=86400&HW-CC-Sign=71423CE38176EB8B74B6E177AD4A24EA14D0212A06857B68D80E444F28BDEB9A "点击放大")

以ArkTS为例，使用预览器的方法如下：

1. 创建或打开一个ArkTS应用/元服务工程。本示例以打开一个本地ArkTS Demo工程为例。
2. 在工程目录下，打开任意一个.ets文件（JS工程请打开.hml/.css/.js页面）。
3. 可以通过如下任意一种方式打开预览器，启动预览。
   * 通过菜单栏，单击**View > Tool Windows > Previewer**打开预览器。
   * 在编辑窗口右上角的侧边工具栏，单击**Previewer**，打开预览器。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/En_Ap89pQXeIjVxmkrPylQ/zh-cn_image_0000002561832905.png?HW-CC-KV=V1&HW-CC-Date=20260429T054631Z&HW-CC-Expire=86400&HW-CC-Sign=DCF4282416B8F115825F2401D604F1482D297100CC9CF217431066B6417D5861 "点击放大")
4. 点击按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/SAndFm4EQJarOEehZY2HPw/zh-cn_image_0000002561752929.png?HW-CC-KV=V1&HW-CC-Date=20260429T054631Z&HW-CC-Expire=86400&HW-CC-Sign=51872FB55CFCDF4D8FF8BAB7BEBC348DFB275D0BBEF1C35F180C49A5E26772D0)，停止预览。
