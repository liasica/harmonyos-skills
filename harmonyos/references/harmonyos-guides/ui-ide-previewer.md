---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-ide-previewer
title: UI预览
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发调试调优 > UI预览
category: harmonyos-guides
scraped_at: 2026-11-19T09:47:49+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:bc457b474064f9769bd447890b34878cd8c30758970e6449fa731413eaf88842
---

DevEco Studio为开发者提供了UI预览功能，方便查看UI效果并随时调整页面布局。预览支持页面预览和组件预览。图1中左侧图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/1vuKrlXNR3aK1noaev8vNg/zh-cn_image_0000002791725394.png?HW-CC-KV=V1&HW-CC-Date=20261119T014749Z&HW-CC-Expire=31536000000&HW-CC-Sign=775CAD7269F4EF7D3E76A7B3FAFDEEF67743A2054F8FD5ABD684AE075758EB3F)表示页面预览，右侧图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/KlPbnFNVShaiBrpChqKi3Q/zh-cn_image_0000002791565422.png?HW-CC-KV=V1&HW-CC-Date=20261119T014749Z&HW-CC-Expire=31536000000&HW-CC-Sign=81ECEF1BB54D3F3E123C3DDC022DA1F1D3143FCCD3BD5A5F505E7A8ACBBEE744)表示组件预览。

**说明** 

操作系统和真机设备的差异可能导致预览效果与真机效果不同。预览效果仅作参考，实际效果以真机为准。

**图1** 预览图标

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/nKFGkoWvTIm7_XPiKW1P8w/zh-cn_image_0000002820525375.png?HW-CC-KV=V1&HW-CC-Date=20261119T014749Z&HW-CC-Expire=31536000000&HW-CC-Sign=DA42955F4683574788856235E79C3716F6A7673BAC2A385546BCA90028EA5377)

## 页面预览

ArkTS应用/元服务均支持页面预览。页面预览通过在工程的ets文件中，给自定义组件添加[@Entry](arkts-create-custom-components.md#entry)装饰器，即可以查看当前UI页面效果。

* 启动方式：选中需要预览的ets页面，点击右侧侧边栏的Previewer按钮，启动页面预览。
* 热加载：在启动页面预览的前提下，添加、删除或修改UI组件后，通过Ctrl+S保存，预览器会同步刷新预览效果，无需重新启动预览。
* 路由能力：支持通过路由能力进行页面切换查看其他页面预览效果。

在页面预览的基础上，提供了极速预览和Inspector双向预览两种特性。下面将详细说明这两种特性。

### 极速预览

支持在修改组件的属性时，无需使用Ctrl+S进行保存，可以直接观察到修改后的预览效果。极速预览默认开启，若需关闭，点击预览器右上角按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/FNUPWlkqT-mp89nUv_fX4A/zh-cn_image_0000002820405375.png?HW-CC-KV=V1&HW-CC-Date=20261119T014749Z&HW-CC-Expire=31536000000&HW-CC-Sign=1B20899C40C7BABA9B0FCACEEB9A385DFBD1FE2C2BCBCD2D68FFD75D7FFD6F2B)即可。

**注意** 

部分应用场景不支持极速预览：

* 不显示的组件。
* 新增或删除组件。
* 包含private变量或无类型的controller的组件。
* 使用了[@Builder](arkts-builder.md)、[@Style](arkts-style.md)、[@Extend](arkts-extend.md)等装饰器的组件。
* 修改使用import导入外部组件/模块的组件。
* 修改状态变量。

效果如图2所示：

**图2** 极速预览演示图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/qQQbe78rSyGS87GRKiCcQQ/zh-cn_image_0000002791725396.gif?HW-CC-KV=V1&HW-CC-Date=20261119T014749Z&HW-CC-Expire=31536000000&HW-CC-Sign=A28C9ED60E5725C2B2E4010098787F6A565E62D323C277294F4C0C48A8965DCE)

### Inspector双向预览

支持ets文件与预览器的双向预览。使用时，点击预览器界面图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/ytIKEi_9QzGblUqnq4asLw/zh-cn_image_0000002791565424.png?HW-CC-KV=V1&HW-CC-Date=20261119T014749Z&HW-CC-Expire=31536000000&HW-CC-Sign=D46FB6225BE10D5F595467BE352F9E190A9A332AE5458F6F33421635F3A95A9B)开启双向预览功能。

开启双向预览功能后，支持代码编辑器、UI界面和组件树之间的联动：

1. 选中预览器界面中的组件，组件树上对应的组件将被选中，同时代码编辑器中的布局文件中对应的代码块高亮显示。
2. 选中布局文件中的代码块，预览器界面将高亮显示，组件树上的组件节点将呈现被选中的状态。
3. 选中组件树中的组件，对应的代码块和预览器界面将高亮显示。
4. 在预览界面，通过组件的属性面板修改可修改的属性或样式。预览界面的修改会自动同步到代码编辑器中，并实时刷新预览器界面。代码编辑器中的源码修改也会实时刷新预览器界面，并更新组件树信息及组件属性。

效果如图3所示：

**图3** Inspector双向预览演示图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/dpzeU74sSVmO-Z6cVvikOw/zh-cn_image_0000002820525377.gif?HW-CC-KV=V1&HW-CC-Date=20261119T014749Z&HW-CC-Expire=31536000000&HW-CC-Sign=81CEA5C1FE6443487AF5D9693306D2C1C3ECA4F98210049A769A714EFE77BED7)

## 组件预览

ArkTS应用/元服务支持组件预览功能。组件预览通过在自定义组件前添加[@Preview装饰器](../harmonyos-references/ts-universal-component-previewer.md#preview装饰器)装饰器实现。在单个源文件中，最多可以使用10个@Preview装饰自定义组件。启动方式：

* 当组件被@Entry和@Preview装饰时，点击右侧侧边栏的Previewer按钮，启动页面预览，页面加载成功后，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/KBeo2rcrTCCVlaei2X-LyA/zh-cn_image_0000002791565422.png?HW-CC-KV=V1&HW-CC-Date=20261119T014749Z&HW-CC-Expire=31536000000&HW-CC-Sign=F07C03D8AF6DC0E42C1ABECB9DECDDDDDEA698FAB686389D86C4CB4CE487A601)，切换到组件预览。
* 当组件仅被@Preview装饰时，点击右侧侧边栏的Previewer按钮，则默认为组件预览。

组件预览时，使用@Preview装饰器的默认属性（请参考[PreviewParams](../harmonyos-references/ts-universal-component-previewer.md#previewparams9)）进行效果显示。可以通过设置@Preview的参数，指定预览设备的相关属性，包括设备类型、屏幕形状等。

@Preview的使用参考如下示例：

```ts
@Entry
@Preview
@Component
struct ComponentPreviewOne {
  build() {
    Column() {
      Text('this is component previewer One')
        .height(80)
        .fontSize(30)
      // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件
      Image($r('app.media.startIcon'))
        .height(300)
        .width(300)
    }
  }
}

@Preview
@Component
struct ComponentPreviewTwo {
  build() {
    Column() {
      Text('this is component previewer Two')
        .height(80)
        .fontSize(30)
        .fontColor(Color.Pink)
      // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件
      Image($r('app.media.startIcon'))
        .height(300)
        .width(300)
    }
  }
}
```

效果如图4所示：

**图4** 组件预览效果图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/SICFGs9cRI2xQDw-ygK-Eg/zh-cn_image_0000002820405377.png?HW-CC-KV=V1&HW-CC-Date=20261119T014749Z&HW-CC-Expire=31536000000&HW-CC-Sign=6E3AF09A01515F2FEB83208AAC40B7A55B3CA159715369F1A4DB9EDEBA643707)

## 动态修改分辨率

同一个应用/元服务可以运行在多个设备上，因不同设备的屏幕分辨率、形状、大小等不同，开发者需要在不同的设备上查看应用/元服务的UI布局和交互效果。预览支持动态修改分辨率，方便开发者随时查看不同设备上的页面显示效果。启动方式：启动页面预览后，点击右上角![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/i-Da41JoRSKBc8AL5jCw5w/zh-cn_image_0000002791725398.png?HW-CC-KV=V1&HW-CC-Date=20261119T014749Z&HW-CC-Expire=31536000000&HW-CC-Sign=3990BFB4F0E8DF86D2CAE768E74324FAEB4604111BABA42B553F5243D5F5EA62)，即可拖动页面选中框动态修改当前设备的屏幕大小。

效果如图5所示：

**图5** 动态修改分辨率效果图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/TIltTcXcQwibiofVLbvjRQ/zh-cn_image_0000002791565426.gif?HW-CC-KV=V1&HW-CC-Date=20261119T014749Z&HW-CC-Expire=31536000000&HW-CC-Sign=18EF95707837F67377CCE792E4C2DEF27293FE173E83E6BD6A67612C341D8F4D)
