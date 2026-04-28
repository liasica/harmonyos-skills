---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-previewer-arkts-js
title: 查看ArkTS/JS预览效果
breadcrumb: 指南 > 编写与调试应用 > 界面预览 > 查看ArkTS/JS预览效果
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:36+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:af3721f5c0cfbc84e9256f6898304af971fa59503eb9ea10e448a5390a0aa96c
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

* **实时预览**：在开发界面UI代码过程中，如果添加或删除了UI组件，您只需**Ctrl+S**进行保存，然后预览器就会立即刷新预览结果。如果修改了组件的属性，则预览器会实时（亚秒级）刷新预览结果，达到极速预览的效果（当前版本极速预览仅支持ArkTS组件。支持部分数据绑定场景，如@State装饰的变量）。实时预览默认开启，如果不需要实时预览，请单击预览器右上角![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/U2JyyEr3S4GA_tMeNYqymQ/zh-cn_image_0000002530912978.png?HW-CC-KV=V1&HW-CC-Date=20260427T235635Z&HW-CC-Expire=86400&HW-CC-Sign=49788BE9620E7748D30E1FD4AF913F94DD8F46885B71D5BFBEEAE0F8F1229E43)按钮，关闭实时预览功能。

  说明

  开发者修改resources/base/profile目录下的配置文件（如main\_pages.json/form\_config.json），不支持触发实时预览，开发者需要点击重新加载![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/b1VtWO1ATu-9I0yV5SaWyQ/zh-cn_image_0000002561752919.png?HW-CC-KV=V1&HW-CC-Date=20260427T235635Z&HW-CC-Expire=86400&HW-CC-Sign=D677874072501FDCFA680123F62BC2431A1BDFF676346A49BF368B41A2B7FD40)。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/qnsWnWKlTcyixkNPaC_pCA/zh-cn_image_0000002561832907.gif?HW-CC-KV=V1&HW-CC-Date=20260427T235635Z&HW-CC-Expire=86400&HW-CC-Sign=EE1C1E48BC1F8F634D2856DC7E82BF0953C893E407424FB15E1EBCA9917A7E17 "点击放大")
* **动态预览**：在预览器界面，可以在预览器中操作应用/元服务的界面交互动作，如单击、跳转、滑动等，与应用/元服务运行在真机设备上的界面交互体验一致。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/oMfe55EwTpKdSnYpRyIE4A/zh-cn_image_0000002561752927.gif?HW-CC-KV=V1&HW-CC-Date=20260427T235635Z&HW-CC-Expire=86400&HW-CC-Sign=FBEE4E44ECE5888EDAB9153E3613D11C6698E7E3BD752EF15E91C94C48B97FE3 "点击放大")

以ArkTS为例，使用预览器的方法如下：

1. 创建或打开一个ArkTS应用/元服务工程。本示例以打开一个本地ArkTS Demo工程为例。
2. 在工程目录下，打开任意一个.ets文件（JS工程请打开.hml/.css/.js页面）。
3. 可以通过如下任意一种方式打开预览器，启动预览。
   * 通过菜单栏，单击**View > Tool Windows > Previewer**打开预览器。
   * 在编辑窗口右上角的侧边工具栏，单击**Previewer**，打开预览器。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/TekBLo5kT_G6au-4qxisnw/zh-cn_image_0000002561832905.png?HW-CC-KV=V1&HW-CC-Date=20260427T235635Z&HW-CC-Expire=86400&HW-CC-Sign=708F1AFC3F5E9122FE22E109F79F3125B921F0A07BA8B9BA49362F4C92DDCAF5 "点击放大")
4. 点击按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/1UliCHvYQ1OTFXk856h9Kg/zh-cn_image_0000002561752929.png?HW-CC-KV=V1&HW-CC-Date=20260427T235635Z&HW-CC-Expire=86400&HW-CC-Sign=9BCCF5A92FD1E5BB1716F59B1547C65932165D844BD48DDAC460ACB4BAE52DF7)，停止预览。
