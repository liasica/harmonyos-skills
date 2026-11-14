---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-ide-previewer
title: UI预览
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发调试调优 > UI预览
category: harmonyos-guides
scraped_at: 2026-11-14T08:47:12+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:02b727fe125c476e6e3969cb189d93fed86403d5e7481d93e219a30b9523b254
---

DevEco Studio为开发者提供了UI预览功能，方便查看UI效果并随时调整页面布局。预览支持页面预览和组件预览。图1中左侧图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/C9aOWfYmSH-28G5uaSKTWg/zh-cn_image_0000002817426457.png?HW-CC-KV=V1&HW-CC-Date=20261114T004533Z&HW-CC-Expire=31536000000&HW-CC-Sign=BE44FA1658A930230EE5E380D39BF30DE4D4434A3E784DE2D62C3C5D47ACFD65)表示页面预览，右侧图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/LhP9Tke_RLicPuPqCE-IhA/zh-cn_image_0000002788467038.png?HW-CC-KV=V1&HW-CC-Date=20261114T004533Z&HW-CC-Expire=31536000000&HW-CC-Sign=DFCAA132B30E2BE336BCDAE0B40B55A6D9CFD43E6D56AE12C4D37FEC7C40C8A3)表示组件预览。

**说明** 

操作系统和真机设备的差异可能导致预览效果与真机效果不同。预览效果仅作参考，实际效果以真机为准。

**图1** 预览图标

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/R6XEYgL4QrCDg2ajfdo-JA/zh-cn_image_0000002817506525.png?HW-CC-KV=V1&HW-CC-Date=20261114T004533Z&HW-CC-Expire=31536000000&HW-CC-Sign=765932E466F3F14D2E466C1376E1F4FC691B9B37883198B5EB06A79E7A02828F)

## 页面预览

ArkTS应用/元服务均支持页面预览。页面预览通过在工程的ets文件中，给自定义组件添加[@Entry](arkts-create-custom-components.md#entry)装饰器，即可以查看当前UI页面效果。

* 启动方式：选中需要预览的ets页面，点击右侧侧边栏的Previewer按钮，启动页面预览。
* 热加载：在启动页面预览的前提下，添加、删除或修改UI组件后，通过Ctrl+S保存，预览器会同步刷新预览效果，无需重新启动预览。
* 路由能力：支持通过路由能力进行页面切换查看其他页面预览效果。

在页面预览的基础上，提供了极速预览和Inspector双向预览两种特性。下面将详细说明这两种特性。

### 极速预览

支持在修改组件的属性时，无需使用Ctrl+S进行保存，可以直接观察到修改后的预览效果。极速预览默认开启，若需关闭，点击预览器右上角按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/zOg7zgs4RPCszEIx2nAUiQ/zh-cn_image_0000002788307096.png?HW-CC-KV=V1&HW-CC-Date=20261114T004533Z&HW-CC-Expire=31536000000&HW-CC-Sign=948476C5186C7AC2DD2BEC7F17478283BD12ECC8C0D4FE2B2BA83C7C14777332)即可。

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/6DtTM3VgTUuOAreXPLGdcA/zh-cn_image_0000002817426459.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004533Z&HW-CC-Expire=31536000000&HW-CC-Sign=B50D3904B6589F8A3CDA86E59D2852C3D61AECDE2B13C196F647FCBD554A0D4F)

### Inspector双向预览

支持ets文件与预览器的双向预览。使用时，点击预览器界面图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/6UAX6ChDQDKmfZp4KO43_Q/zh-cn_image_0000002788467040.png?HW-CC-KV=V1&HW-CC-Date=20261114T004533Z&HW-CC-Expire=31536000000&HW-CC-Sign=E839D396D12F49E0D9CE986528299BDCC25E98F3332FA2A7972D409B813A70CC)开启双向预览功能。

开启双向预览功能后，支持代码编辑器、UI界面和组件树之间的联动：

1. 选中预览器界面中的组件，组件树上对应的组件将被选中，同时代码编辑器中的布局文件中对应的代码块高亮显示。
2. 选中布局文件中的代码块，预览器界面将高亮显示，组件树上的组件节点将呈现被选中的状态。
3. 选中组件树中的组件，对应的代码块和预览器界面将高亮显示。
4. 在预览界面，通过组件的属性面板修改可修改的属性或样式。预览界面的修改会自动同步到代码编辑器中，并实时刷新预览器界面。代码编辑器中的源码修改也会实时刷新预览器界面，并更新组件树信息及组件属性。

效果如图3所示：

**图3** Inspector双向预览演示图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/iIirkcniRuqxC6rSHIGyZQ/zh-cn_image_0000002817506527.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004533Z&HW-CC-Expire=31536000000&HW-CC-Sign=ABF520BFB5BA8A0BD42513C948D8F41B6B0EFF3A6EDEE61DEB07641625661704)

## 组件预览

ArkTS应用/元服务支持组件预览功能。组件预览通过在自定义组件前添加[@Preview装饰器](../harmonyos-references/ts-universal-component-previewer.md#preview装饰器)装饰器实现。在单个源文件中，最多可以使用10个@Preview装饰自定义组件。启动方式：

* 当组件被@Entry和@Preview装饰时，点击右侧侧边栏的Previewer按钮，启动页面预览，页面加载成功后，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/jAooYUmaQtWsZbzIP0Oecg/zh-cn_image_0000002788467038.png?HW-CC-KV=V1&HW-CC-Date=20261114T004533Z&HW-CC-Expire=31536000000&HW-CC-Sign=3BF1767D610AA4DAB60400EAC78D5E9B248E00C8FCB8DCD806064C58CE1D88ED)，切换到组件预览。
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/TdpmbnRdRaqCD5CNXdJlWw/zh-cn_image_0000002788307098.png?HW-CC-KV=V1&HW-CC-Date=20261114T004533Z&HW-CC-Expire=31536000000&HW-CC-Sign=4C9F8C35D42B242EAC39EBCA44946DCB24A59E80A7426D3B5E61DA1F06EC55CE)

## 动态修改分辨率

同一个应用/元服务可以运行在多个设备上，因不同设备的屏幕分辨率、形状、大小等不同，开发者需要在不同的设备上查看应用/元服务的UI布局和交互效果。预览支持动态修改分辨率，方便开发者随时查看不同设备上的页面显示效果。启动方式：启动页面预览后，点击右上角![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/tgczOsneSIGoeh3OMtjXOQ/zh-cn_image_0000002817426461.png?HW-CC-KV=V1&HW-CC-Date=20261114T004533Z&HW-CC-Expire=31536000000&HW-CC-Sign=E2604B8B165E6ACB352FFF5E86E0685DF7D36C2273AD341C2F10613A9C9A444F)，即可拖动页面选中框动态修改当前设备的屏幕大小。

效果如图5所示：

**图5** 动态修改分辨率效果图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/UNmwHzvOREKXM2LziicHTA/zh-cn_image_0000002788467042.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004533Z&HW-CC-Expire=31536000000&HW-CC-Sign=0B0CF358D2316F2AF121CEB9601C1F1E3616D87486E2B018333F56408E74F6F6)
