---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-ide-previewer
title: UI预览
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发调试调优 > UI预览
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:38+08:00
doc_updated_at: 2026-03-20
content_hash: sha256:b1553832c077031f0a898336dde40da8cbf5471936dd3747960b54ab7278dbd4
---

DevEco Studio为开发者提供了UI预览功能，方便查看UI效果并随时调整页面布局。预览支持页面预览和组件预览。图1中左侧图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/Jmo3ZwnXRR-boDxIYgrwWA/zh-cn_image_0000002552958156.png?HW-CC-KV=V1&HW-CC-Date=20260427T234036Z&HW-CC-Expire=86400&HW-CC-Sign=354D1D3A3DC00A7592055FFDCB4AF03C6916B46D3EF5E7FD8E6E852505228D64)表示页面预览，右侧图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/nyF0ql3tScWvbjBI1Dx2fg/zh-cn_image_0000002583478157.png?HW-CC-KV=V1&HW-CC-Date=20260427T234036Z&HW-CC-Expire=86400&HW-CC-Sign=38D86873CB859A25A6FBB6C41CE06458B9B7967435FA864E2D5914F260AEDE76)表示组件预览。

说明

操作系统和真机设备的差异可能导致预览效果与真机效果不同。预览效果仅作参考，实际效果以真机为准。

**图1** 预览图标

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/M2Iv9fdaQfO9_wykcLiNGQ/zh-cn_image_0000002552798508.png?HW-CC-KV=V1&HW-CC-Date=20260427T234036Z&HW-CC-Expire=86400&HW-CC-Sign=1A85DC1F19010508132807FB603DB810A215DFAF329D003E43FB8F13A5A5552D)

## 页面预览

ArkTS应用/元服务均支持页面预览。页面预览通过在工程的ets文件中，给自定义组件添加[@Entry](arkts-create-custom-components.md#entry)装饰器，即可以查看当前UI页面效果。

* 启动方式：选中需要预览的ets页面，点击右侧侧边栏的Previewer按钮，启动页面预览。
* 热加载：在启动页面预览的前提下，添加、删除或修改UI组件后，通过Ctrl+S保存，预览器会同步刷新预览效果，无需重新启动预览。
* 路由能力：支持通过路由能力进行页面切换查看其它页面预览效果。

在页面预览的基础上，提供了极速预览和Inspector双向预览两种特性。下面将详细说明这两种特性。

### 极速预览

支持在修改组件的属性时，无需使用Ctrl+S进行保存，可以直接观察到修改后的预览效果。极速预览默认开启，若需关闭，点击预览器右上角按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/M8w2BzbERrC79v4x__2NEQ/zh-cn_image_0000002583438203.png?HW-CC-KV=V1&HW-CC-Date=20260427T234036Z&HW-CC-Expire=86400&HW-CC-Sign=AC2AEAE82546AD0BC1D45BC46D0E91CFB4DC363FF2E13671837F9DC04440B4D0)即可。

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/g7jHtzzTTSKZYEg186dopw/zh-cn_image_0000002552958158.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234036Z&HW-CC-Expire=86400&HW-CC-Sign=844EF524736EF1D36A28A100EEA1C0DD4A9984BE55F9DFDB378EB407B658DC15)

### inspector双向预览

支持ets文件与预览器的双向预览。使用时，点击预览器界面图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/nj6Qy9jOSAGWA85jKYoIxQ/zh-cn_image_0000002583478159.png?HW-CC-KV=V1&HW-CC-Date=20260427T234036Z&HW-CC-Expire=86400&HW-CC-Sign=527333F389715E6E9C1362117E424D7945B1BD71C829E48F7993A6A4A4BBABCA)开启双向预览功能。

开启双向预览功能后，支持代码编辑器、UI界面和组件树之间的联动：

1. 选中预览器界面中的组件，组件树上对应的组件将被选中，同时代码编辑器中的布局文件中对应的代码块高亮显示。
2. 选中布局文件中的代码块，预览器界面将高亮显示，组件树上的组件节点将呈现被选中的状态。
3. 选中组件树中的组件，对应的代码块和预览器界面将高亮显示。
4. 在预览界面，通过组件的属性面板修改可修改的属性或样式。预览界面的修改会自动同步到代码编辑器中，并实时刷新预览器界面。代码编辑器中的源码修改也会实时刷新预览器界面，并更新组件树信息及组件属性。

效果如图3所示：

**图3** inspector双向预览演示图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/xa8AVVnfTw-DQZJjJLSNgg/zh-cn_image_0000002552798510.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234036Z&HW-CC-Expire=86400&HW-CC-Sign=4E0A4D58229078D473D446293D5F6C8766C3EB696E640E392886211CF1C8051D)

## 组件预览

ArkTS应用/元服务支持组件预览功能。组件预览通过在自定义组件前添加[@Preview](../harmonyos-references/ts-universal-component-previewer.md#preview装饰器)装饰器实现。在单个源文件中，最多可以使用10个@Preview装饰自定义组件。启动方式：

* 当组件被@Entry和@Preview装饰时，点击右侧侧边栏的Previewer按钮，启动页面预览，页面加载成功后，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/KSDkc4QuQiqDaCMSqbY-7g/zh-cn_image_0000002583478157.png?HW-CC-KV=V1&HW-CC-Date=20260427T234036Z&HW-CC-Expire=86400&HW-CC-Sign=754B64CF46CFD8C02457A35CADDAE527059C0C771828C452A804766836F100B4)，切换到组件预览。
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/h5Xy59gGT3e-ChjXX9ETSQ/zh-cn_image_0000002583438205.png?HW-CC-KV=V1&HW-CC-Date=20260427T234036Z&HW-CC-Expire=86400&HW-CC-Sign=2D249C76E7B39FE26DF6DA533DD32A566BE32E901FA86DC298E7686BF72CE764)

## 动态修改分辨率

同一个应用/元服务可以运行在多个设备上，因不同设备的屏幕分辨率、形状、大小等不同，开发者需要在不同的设备上查看应用/元服务的UI布局和交互效果。预览支持动态修改分辨率，方便开发者随时查看不同设备上的页面显示效果。启动方式：启动页面预览后，点击右上角![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/qHLVrVE_S3CWsLAyySjuzQ/zh-cn_image_0000002552958160.png?HW-CC-KV=V1&HW-CC-Date=20260427T234036Z&HW-CC-Expire=86400&HW-CC-Sign=453BCD1FA7735CD75ED58441EF1D5397CE676E85BD301A97761068B6884C4A6D)，即可拖动页面选中框动态修改当前设备的屏幕大小。

效果如图5所示：

**图5** 动态修改分辨率效果图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/6ro6d2rHRK-GwZdLchx0LQ/zh-cn_image_0000002583478161.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234036Z&HW-CC-Expire=86400&HW-CC-Sign=3526234CA0EA6A4B5D85B081AFF507C10139A907F61382A17394B1938F13A6FB)
