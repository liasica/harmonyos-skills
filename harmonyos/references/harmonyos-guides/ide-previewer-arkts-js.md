---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-previewer-arkts-js
title: 查看ArkTS/JS预览效果
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 界面预览 > 查看ArkTS/JS预览效果
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:28+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:e8847165a577b364e04ea29d1696553b7eefe4eb65b4ee8ac770fd17f81132fa
---

预览器支持ArkTS/JS应用/元服务“实时预览”和“动态预览”。

**说明** 

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

* **实时预览**：在开发界面UI代码过程中，如果添加或删除了UI组件，您只需**Ctrl+S**进行保存，然后预览器就会立即刷新预览结果。如果修改了组件的属性，则预览器会实时（亚秒级）刷新预览结果，达到极速预览的效果（当前版本极速预览仅支持ArkTS组件。支持部分数据绑定场景，如@State装饰的变量）。实时预览默认开启，如果不需要实时预览，请单击预览器右上角![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/CmYlMSG8RpOsYhB8iRbXqw/zh-cn_image_0000002779406840.png?HW-CC-KV=V1&HW-CC-Date=20261124T044228Z&HW-CC-Expire=31536000000&HW-CC-Sign=79B6CD8F2C1222CDF9848AE20D400C873FB31C462FE1F8EE6EEF7DAB4D126D1A)按钮，关闭实时预览功能。

  **说明** 

  开发者修改resources/base/profile目录下的配置文件（如main\_pages.json/form\_config.json），不支持触发实时预览，开发者需要点击重新加载![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/edJr4AXTQQaIjKzHyFveIA/zh-cn_image_0000002779566816.png?HW-CC-KV=V1&HW-CC-Date=20261124T044228Z&HW-CC-Expire=31536000000&HW-CC-Sign=DA3A529AA3C9AF6C6F6F21CC5FCBAAA54371868501BF42FE2117EA57DCC02ECC)。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/PbbbHMokT8KKudL3molGkw/zh-cn_image_0000002779566818.gif?HW-CC-KV=V1&HW-CC-Date=20261124T044228Z&HW-CC-Expire=31536000000&HW-CC-Sign=8BD1ABF667089AFEF50604A7D428CBC9F2C331FF9F013E05E5C1CD5A91FFE499 "点击放大")
* **动态预览**：在预览器界面，可以在预览器中操作应用/元服务的界面交互动作，如单击、跳转、滑动等，与应用/元服务运行在真机设备上的界面交互体验一致。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/jeYc_Iv6QUW_rUR4nVWiow/zh-cn_image_0000002808766401.gif?HW-CC-KV=V1&HW-CC-Date=20261124T044228Z&HW-CC-Expire=31536000000&HW-CC-Sign=96AAAFA8ED2BC3FC93693919DC8E58B9568BC4D38163A3FCA7475E7C53B5C13D "点击放大")

以ArkTS为例，使用预览器的方法如下：

1. 创建或打开一个ArkTS应用/元服务工程。本示例以打开一个本地ArkTS Demo工程为例。
2. 在工程目录下，打开任意一个.ets文件（JS工程请打开.hml/.css/.js页面）。
3. 可以通过如下任意一种方式打开预览器，启动预览。
   * 通过菜单栏，单击**View > Tool Windows > Previewer**打开预览器。
   * 在编辑窗口右上角的侧边工具栏，单击**Previewer**，打开预览器。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/XcpRuCAlTYSWRpDIiInTcQ/zh-cn_image_0000002808886481.png?HW-CC-KV=V1&HW-CC-Date=20261124T044228Z&HW-CC-Expire=31536000000&HW-CC-Sign=CA82F9EEF0CE36E2A8AB110B945EF27440C758DFC5111D63B188C85D71555AE5 "点击放大")
4. 点击按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/P14IuQd1TJymg1E8JinDDA/zh-cn_image_0000002779406842.png?HW-CC-KV=V1&HW-CC-Date=20261124T044228Z&HW-CC-Expire=31536000000&HW-CC-Sign=37ECBDA4FBE8013D8B3270DEAD57AB4D1AA007E0F9FAA52A1659E8A1E885B178)，停止预览。
