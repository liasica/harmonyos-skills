---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-ide-previewer
title: UI预览
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发调试调优 > UI预览
category: harmonyos-guides
scraped_at: 2026-04-29T13:28:59+08:00
doc_updated_at: 2026-03-20
content_hash: sha256:d90c35cd0b7f9e8f1b4534997f8207a69968c0c06afdfcacdf6d4d57f500bdf3
---

DevEco Studio为开发者提供了UI预览功能，方便查看UI效果并随时调整页面布局。预览支持页面预览和组件预览。图1中左侧图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/DvvBIJGRR4SU0iRw9LBQ9g/zh-cn_image_0000002589324517.png?HW-CC-KV=V1&HW-CC-Date=20260429T052858Z&HW-CC-Expire=86400&HW-CC-Sign=F2E5A3B4EB8378DF238B7A07AC8AED9865A591B5EEEE85780DC08FC50D80241B)表示页面预览，右侧图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/sIvAfWGNQNG3T7CT5FlhKA/zh-cn_image_0000002589244455.png?HW-CC-KV=V1&HW-CC-Date=20260429T052858Z&HW-CC-Expire=86400&HW-CC-Sign=78569309D26BC5D055C53225DF4900C197C1F32080BFF0F040ACA30FD98E1551)表示组件预览。

说明

操作系统和真机设备的差异可能导致预览效果与真机效果不同。预览效果仅作参考，实际效果以真机为准。

**图1** 预览图标

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/7IyXOpLJRQG8_rHCEmcOrQ/zh-cn_image_0000002558764648.png?HW-CC-KV=V1&HW-CC-Date=20260429T052858Z&HW-CC-Expire=86400&HW-CC-Sign=1F84974FE7416CE405ED570CB454D4CED2B1D20419C7F8BE8F0F64D13904C81E)

## 页面预览

ArkTS应用/元服务均支持页面预览。页面预览通过在工程的ets文件中，给自定义组件添加[@Entry](arkts-create-custom-components.md#entry)装饰器，即可以查看当前UI页面效果。

* 启动方式：选中需要预览的ets页面，点击右侧侧边栏的Previewer按钮，启动页面预览。
* 热加载：在启动页面预览的前提下，添加、删除或修改UI组件后，通过Ctrl+S保存，预览器会同步刷新预览效果，无需重新启动预览。
* 路由能力：支持通过路由能力进行页面切换查看其它页面预览效果。

在页面预览的基础上，提供了极速预览和Inspector双向预览两种特性。下面将详细说明这两种特性。

### 极速预览

支持在修改组件的属性时，无需使用Ctrl+S进行保存，可以直接观察到修改后的预览效果。极速预览默认开启，若需关闭，点击预览器右上角按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/6Vd_9GqQTKKeEZVeQCVPKA/zh-cn_image_0000002558604992.png?HW-CC-KV=V1&HW-CC-Date=20260429T052858Z&HW-CC-Expire=86400&HW-CC-Sign=DFA2EAB3E921BB30B8382DA218983FC8862114381AF505BF612DBE833F583EA6)即可。

注意

部分应用场景不支持极速预览：

* 不显示的组件。
* 新增或删除组件。
* 包含private变量或无类型的controller的组件。
* 使用了[@Builder](arkts-builder.md)、[@Style](arkts-style.md)、[@Extend](arkts-extend.md)等装饰器的组件。
* 修改使用import导入外部组件/模块的组件。
* 修改状态变量。

效果如图2所示：

**图2** 极速预览演示图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/_s1zA7UcTpCl-1AGjw0E1Q/zh-cn_image_0000002589324519.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052858Z&HW-CC-Expire=86400&HW-CC-Sign=4FD52E77671C780D8AB7A65F0B18513A731433A7B293C5F38656C2D39263D1D6)

### inspector双向预览

支持ets文件与预览器的双向预览。使用时，点击预览器界面图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/-XXf4f_vSFmI291ztbRAdg/zh-cn_image_0000002589244457.png?HW-CC-KV=V1&HW-CC-Date=20260429T052858Z&HW-CC-Expire=86400&HW-CC-Sign=F0D5A27A1AE5458A9C8E20E6E1F8940F8A4A3BE36744E630FC9028B703FF76D8)开启双向预览功能。

开启双向预览功能后，支持代码编辑器、UI界面和组件树之间的联动：

1. 选中预览器界面中的组件，组件树上对应的组件将被选中，同时代码编辑器中的布局文件中对应的代码块高亮显示。
2. 选中布局文件中的代码块，预览器界面将高亮显示，组件树上的组件节点将呈现被选中的状态。
3. 选中组件树中的组件，对应的代码块和预览器界面将高亮显示。
4. 在预览界面，通过组件的属性面板修改可修改的属性或样式。预览界面的修改会自动同步到代码编辑器中，并实时刷新预览器界面。代码编辑器中的源码修改也会实时刷新预览器界面，并更新组件树信息及组件属性。

效果如图3所示：

**图3** inspector双向预览演示图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/RNUJJynDR8ek9MdZaoa1gQ/zh-cn_image_0000002558764650.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052858Z&HW-CC-Expire=86400&HW-CC-Sign=5AB7EC8DF41B3C9C7C51695657EFF24AEA6BF38EBFFE4A652E3CBD3B2BA17371)

## 组件预览

ArkTS应用/元服务支持组件预览功能。组件预览通过在自定义组件前添加[@Preview](../harmonyos-references/ts-universal-component-previewer.md#preview装饰器)装饰器实现。在单个源文件中，最多可以使用10个@Preview装饰自定义组件。启动方式：

* 当组件被@Entry和@Preview装饰时，点击右侧侧边栏的Previewer按钮，启动页面预览，页面加载成功后，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/M6VTqyU5RvKuJkVzOhgm4w/zh-cn_image_0000002589244455.png?HW-CC-KV=V1&HW-CC-Date=20260429T052858Z&HW-CC-Expire=86400&HW-CC-Sign=F5093E0E74B33E260DBE352ED9351BDA46331BEC394A2D8B714944AAF19B5853)，切换到组件预览。
* 当组件仅被@Preview装饰时，点击右侧侧边栏的Previewer按钮，则默认为组件预览。

组件预览时，使用@Preview装饰器的默认属性（请参考[PreviewParams](../harmonyos-references/ts-universal-component-previewer.md#previewparams9)）进行效果显示。可以通过设置@Preview的参数，指定预览设备的相关属性，包括设备类型、屏幕形状等。

@Preview的使用参考如下示例：

```
1. @Entry
2. @Preview
3. @Component
4. struct ComponentPreviewOne {
5. build() {
6. Column() {
7. Text('this is component previewer One')
8. .height(80)
9. .fontSize(30)
10. // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件
11. Image($r('app.media.startIcon'))
12. .height(300)
13. .width(300)
14. }
15. }
16. }

18. @Preview
19. @Component
20. struct ComponentPreviewTwo {
21. build() {
22. Column() {
23. Text('this is component previewer Two')
24. .height(80)
25. .fontSize(30)
26. .fontColor(Color.Pink)
27. // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件
28. Image($r('app.media.startIcon'))
29. .height(300)
30. .width(300)
31. }
32. }
33. }
```

效果如图4所示：

**图4** 组件预览效果图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/8YDR1rhcRoqRMD27SpM0tw/zh-cn_image_0000002558604994.png?HW-CC-KV=V1&HW-CC-Date=20260429T052858Z&HW-CC-Expire=86400&HW-CC-Sign=095AF779D740FB5932383903B4349526AFC870F0F46A7B1EDF71FA149FD8DFEA)

## 动态修改分辨率

同一个应用/元服务可以运行在多个设备上，因不同设备的屏幕分辨率、形状、大小等不同，开发者需要在不同的设备上查看应用/元服务的UI布局和交互效果。预览支持动态修改分辨率，方便开发者随时查看不同设备上的页面显示效果。启动方式：启动页面预览后，点击右上角![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/oW9LDtqbQwGKQr8KNxgzIg/zh-cn_image_0000002589324521.png?HW-CC-KV=V1&HW-CC-Date=20260429T052858Z&HW-CC-Expire=86400&HW-CC-Sign=FE3631328942D06CE2ADDE5789D300584DDF55D4366AA9D0B9D33E95158B37DB)，即可拖动页面选中框动态修改当前设备的屏幕大小。

效果如图5所示：

**图5** 动态修改分辨率效果图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/8hqCLoMFSGagPp409s1Lyg/zh-cn_image_0000002589244459.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052858Z&HW-CC-Expire=86400&HW-CC-Sign=383866CB5F3C994222F9D935C7BC232525C453C42E595F62AA4B0926692EFB72)
