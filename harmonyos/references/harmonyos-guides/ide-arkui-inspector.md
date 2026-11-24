---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-arkui-inspector
title: 布局分析
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 布局分析
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:30+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:e1682060a22f6af6163b32f6be2bc0b7913e27979478f890bed7cd7c9c37c197
---

开发者可以使用ArkUI Inspector，在DevEco Studio上查看应用在真机上的UI显示效果，并通过查看多次操作后的界面状态，快速分析定位UI界面存在的问题。

ArkUI Inspector支持的功能包括：

* [查看设备上应用的UI显示效果](ide-arkui-inspector.md#section1645813371383)。
* [导出及导入应用UI界面快照](ide-arkui-inspector.md#section0442629153111)，脱离设备查看UI显示效果。
* 在组件树上选择组件，UI界面自动框选对应组件，属性列表显示当前组件的属性信息。
* 在UI界面点击选择组件，组件树对应组件变化为选中状态，属性列表显示当前组件的属性信息。
* [UI组件源码跳转](ide-arkui-inspector.md#section1226015494335)，选中UI组件后点击源码跳转按钮即可跳转至源码位置。
* [查看当前页面上所有组件显示区域](ide-arkui-inspector.md#section1137025915336)。
* 在组件树上选择自定义组件，属性列表显示当前组件配置的[状态变量信息以及影响组件](ide-arkui-inspector.md#section19923158103412)。
* [查看窗口交互事件](ide-arkui-inspector.md#section516993011576)，包括触屏、鼠标、按键、滚轮、窗口焦点变化事件。
* 按照组件粒度[3D展开应用](ide-arkui-inspector.md#section138812162416)，方便查看组件之间的嵌套、遮挡关系。

## 使用场景

针对界面较复杂的应用：

* 通过组件树查看组件的父子关系，检查是否存在冗余组件。
* 针对应用在真机或模拟器上运行出现UI界面显示异常，尤其经过多次界面复杂操作后产生的界面错误以及后台逻辑错误，进行问题分析定位。

## 使用约束

* 已通过USB或WLAN连接设备。
* 仅支持Stage工程。
* 仅支持运行在前台的应用。
* 仅支持全屏应用。
* 不支持应用市场上架的发布签名应用。

## 操作步骤

1. 在菜单栏点击**View > Tool Windows > ArkUI Inspector**，或者在DevEco Studio下方点击**ArkUI Inspector**，打开ArkUI Inspector。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/zUKubBkORQiR9fi0Mo_hFw/zh-cn_image_0000002808886255.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=2CF689E91410742A37841D5FF2244B307F5EC8A093459C79EDC83240F44C8D44)
2. 点击RUN![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/zs0yP4spTyyjM2u0bWiudg/zh-cn_image_0000002808766167.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=F39D2DB5AAF1104C4A80AF57F9556AB7CF81CDE559283B416106E166BD92925B)或者DEBUG![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/5YWgXVIWSFO6Q8Z7dNMpUw/zh-cn_image_0000002779566542.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=06C6C85347A76C67BA58DC22C68C3E9A4E55937E2BAC7EE76BBDC39BECC67F75)按钮，将应用推送安装到设备上，在设备的应用列表中选择当前显示在前台的UI进程。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/0d4nMLqeRNK4sw8DowvaAg/zh-cn_image_0000002779566596.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=C487EE1297CB1DC3386E67F82153A06C89ADD084619A752CD10633D06F767D8A)
3. ArkUI Inspector左侧为当前的组件树结构，中间栏显示当前设备的UI界面，右侧在选中组件的情况下为当前组件的属性信息。可以在左侧组件树上或在中间UI界面点击选择组件。当设备上UI发生变化时，可点击中间栏右上角![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/7LQRrdMTSmCdUQzyu20RQA/zh-cn_image_0000002779406624.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=DA0C5B7D580AC824C242ED423E773CD72DDF2794D605569B04E74C3B46062DB4)按钮同步设备上的UI效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/UpvRiw9iSQarVsSQnL-6Iw/zh-cn_image_0000002779566608.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=7C5333332901EAB2596005398009DEAB963A17D219FA3B77E6266B7621216AC9)
4. 在设备框，点击设备列表的最后一项**Stop inspector**，可断开与设备的连接。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/_T7Pe475T0W69GsdGy7SjA/zh-cn_image_0000002779406582.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=8AE695EFC23CE17498C154BE081CADF129D93C56E3ABFDB62A76D1A8D658BD1E)

## 显示组件信息

* 点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/I0c2P2TGRu2en_vxWtMP2g/zh-cn_image_0000002779566624.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=05159A7C2C721603D0BA2AA44578EBD49AAAB7F047F7B872DB003659B9F5ACF5 "点击放大")，勾选**Show Tree Statistics**，可显示组件树组件信息。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/Do9Q1hBZQrmHJjlTgqtFBg/zh-cn_image_0000002808766153.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=188DD04915ABD7A2B0B1BCFD0B2BCA4B36315150A22AA7C1C79645268240B3E4)
* 点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/Qf1fHFpsQeOGHpVCY7Xa_Q/zh-cn_image_0000002779406602.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=73681323A028622A37EE30B949E139CF8ED5675D1FDA947E9671F453160C3A25 "点击放大")，勾选**Show Hidden Components**，可显示隐藏的组件。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/cG3J9I_1R3Ky5Je9BPNo9Q/zh-cn_image_0000002808886211.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=458DE8CF0B77F023965052834021F6A125184CDC050D56EC2B57DB9B80F4D98C)
* 点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/GsOqlCT1TcyBghxT2_fyWQ/zh-cn_image_0000002808886225.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=60C2C08FF2F1DECD4DDD10C0F856EEFE651EFED634C8FEB84114230AF61DE3BB "点击放大")，勾选**Show Custom Components**，可过滤自定义组件。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/aDg_tcqOQ8ScYl6Xjvh6QA/zh-cn_image_0000002808886269.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=228A1236441BDD68C8AFDD83BC1093A4A43BC82F864C0EF533B18D75369C52F0)
* 点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/DhfWtCSKS7aXu_aApYQhLQ/zh-cn_image_0000002808886213.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=3E6FD2503C43DF3AFC836E7B8E282C131823311EEBD66DE592F91A0789B92591 "点击放大")，勾选**Show System Components**，可过滤系统组件。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/6P2nEVJCSayRxs7HLWlHtA/zh-cn_image_0000002779566564.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=78784410FAFDF5A1A47703A333CF40EB056A4006E5B0AF714B95C5B1FFAA1626)

## 导入/导出UI界面快照

ArkUI Inspector支持导出及导入应用UI界面快照，脱离设备查看应用UI界面显示效果。

* 在中间栏点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/2O1tbHrjS0Getc8irhQsdA/zh-cn_image_0000002779406634.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=9BE3B8BDDF231714A06414671A625D6195C9CB6D4347C9E1026F3C7B01BCEFB6)可以导入本地的应用UI界面快照。导入成功后将在DevEco Studio中打开该快照。
* 在中间栏点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/oo5_RKXUS4S5_2fmkN_aqw/zh-cn_image_0000002808886281.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=6289B1A5486952C745C0262B0BBA5CFA513ADED5E24B651F69AE948A62808FF9)可以将应用UI界面快照导出到本地。导出成功后将默认在DevEco Studio中打开该快照。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/Ejq5KUOiQ8210NkNkg9aqQ/zh-cn_image_0000002779566558.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=6187F24C7042C17245E633A925028B7E5011C82F476826F622B03CCCBD911EF9)

## UI组件源码跳转

1. 单击**Run > Edit Configurations**，勾选“**Enable DebugLine**”，点击**OK**保存后，重新运行工程，表示开启源码跳转功能。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/eb09HZPNSXev7WthcS5wHw/zh-cn_image_0000002808886275.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=B6B063100A97F5313FAEA008151D08A15EFCBB3215933BFC26597B34D3DD40C3)
2. 在ArkUI Inspector中，选中要进行源码跳转的UI组件，点击右侧的源码跳转，即可跳转到UI组件源码位置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/zoe5q8vfRYCnHXhyKd-jmA/zh-cn_image_0000002779566574.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=EEB06C9C44AABD014596C6AD0D2450F94A766D1EF34ED302076C67F5AC0370F7)

## 显示布局边框

在UI显示设置上，勾选“**Show Component Border**”，可显示当前页面所有组件的布局信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/wkTUgoNXQ7SeT-Q3Istmjw/zh-cn_image_0000002808766141.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=1BB10A60A42D43A74B2EF8B23BCAB3E87F76D2ED162C8B065E33FC516DBD9C0F)

## 查看UI组件的状态变量

点击自定义组件，可以查看自定义组件的状态变量，以及状态变量影响的下一层组件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/ML8mt85WQOuF5E2KC2y9bQ/zh-cn_image_0000002808766195.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=44D36ADD3E5060C0E889BBFD584F4B1574FC7D22C0C89A8A2B9E05FC53BB2E0C)

## 查看窗口交互事件

从DevEco Studio 6.1.0 Beta1版本开始，支持查看[窗口交互事件](arkts-interaction-capability-overview.md)，包括触屏、鼠标、按键、滚轮、窗口焦点变化事件，帮助开发者定位窗口发生失焦、获焦、重绘等问题。

选择**WindowEvents**页签，点击Start按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/Lkrkaj6OQxKiArzsfb0i4g/zh-cn_image_0000002779406598.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=629C9FD6EC82F531780315D5C4DF9461D5E261B14DFE0C712B2C0DE5D02BBCD1)，开始上报事件消息，包括事件时间戳、窗口ID、事件类型、坐标等，支持按事件类型过滤。点击Stop按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/8axYDoBFSBeaeVExew25jA/zh-cn_image_0000002808886247.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=8754E47DB845E9FDE282BD3C77DB5A135F633390614C7DBF12B580EA60AD581F)，即可停止上报事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/MMZlJm4jTHmi2Dr6sWM_WA/zh-cn_image_0000002808766197.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=CC8924E4834194889A235A5A5E41F217446F88DD0B176AA5D03F9AC96A939172)

## 3D展开应用

ArkUI Inspector支持将应用按照组件粒度进行3D展开，即UI界面能够在Z轴展开，方便查看组件之间的嵌套、遮挡关系。

该功能从DevEco Studio 6.0.0 Beta1版本开始支持，同时设备系统版本需要升级到API 20。

### 使用场景

* 点击图层可以精准选中和查看被遮挡的组件，可用于定位组件是否被遮挡等问题。
* 3D视图展示的图层均是组件树上参与渲染的组件，可帮助开发者判断组件是否需要进行渲染，例如过长的列表、不可见区域是否需要渲染，帮助开发者优化渲染性能。
* 对于页面复杂、小组件较多的场景，在组件树或者2D视图中难以选中，通过3D视图增加图层之间的距离，能够有效地突出小组件，使其更易于选中。

### 进入3D视图

点击3D View按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/RccXaaeRRgG-EtiUDzPysg/zh-cn_image_0000002779406592.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=FD67A6504EC67F4F913288F0ABCD353CE1FC0D9BC79AFF3F20A3E6A0CDB225FE)，进入3D视图。首次进入3D视图会加载3D数据，请等待数据加载完成。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/6wkjhOJwQsuKC3SpF06p4w/zh-cn_image_0000002808766191.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=ABB1D6769A50874AC00161D877EAE4FCFC06BA0012AC0ACB26A3276AC2FD7C69)

### 基础操作

* 旋转视图：按住鼠标左键移动。
* 平移视图：按住鼠标右键移动。
* 放大/缩小视图：滚动鼠标滚轮。

### 隐藏前方图层

选中图层后，图层会显示蓝色边框，点击Hide Views in Front按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/PLUxz7ddQ1S6F4SQNl3nZQ/zh-cn_image_0000002779406566.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=2EDB0F4DFD37BA355B86F44B0450FBC261531D0574610B35E2DCE0E83AEC5527)，能够隐藏当前选中图层前方（朝向用户）的所有图层，避免不必要图层的干扰。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/X8gKnDeCThmdGYwx2_4Uug/zh-cn_image_0000002779406588.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=33A4BDC1FC98B346F4CCC960236BD787D5EBFE96664C97151A6E6AC68EDA465F)

### 隐藏后方图层

和隐藏前方图层类似，选中图层后，点击Hide Views Behind按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/iQ9Gt8I0QJGSnXq_afG0dw/zh-cn_image_0000002779406576.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=9724B22EDF770B9DF3B08F41D59C157FD08D19931FEF05993BFF6C8C41D5CBFF)，能够隐藏当前选中图层后方的所有图层。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/NkpZGPdNTpiJsjd508AuJg/zh-cn_image_0000002808766133.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=0E6E9B493669A14F9FEE3C5214BCEB8970969A39544CD3BBBB63BC32CE665B5B)

### 恢复隐藏图层

点击Restore Hidden Views按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/AsU4faBPQpyTxWHWO673lw/zh-cn_image_0000002779566602.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=B587595A920E8976235E61368ECCDC181D293BA8A26CED94B38DA83CDA6D1DEE)，能够恢复所有隐藏的前方图层和后方图层。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/nKOnin6-Q62a5NRvWChaLA/zh-cn_image_0000002779566566.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=DFEB441AD6C60BC519B3705FC0481ACDE0EDCBFCE011E72C6757AC6F4455CCBA)

### 切换图层排列顺序

图层有两种排列顺序，id顺序和层级顺序。

* id顺序：默认顺序，即渲染的顺序，也是组件真实显示的顺序，图层的遮挡关系和实际应用一致，每个图层显示在一个Z轴平面上，但如果图层数量较多，会导致Z轴过长，操作不方便。
* 层级顺序：组件树上同一层级的组件，在3D视图中会显示在相同Z轴平面上，能够有效减少3D视图下Z轴长度。

切换方式：点击Switch to Layer Order/Switch to Id Order按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/VgPdjo_jQNmyX0GxVaRZtQ/zh-cn_image_0000002808886251.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=0BE19DB0BB2CDFF7AAD4286E238D06819185BD38BEB5AFF8AE7148A79EE2B783)，可以将图层的排列顺序分别切换至层级顺序/id顺序。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/gBTUG10kQ1mb6Jcqmk2xBQ/zh-cn_image_0000002808886219.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=E5697DC1FB3EF64DF4421AF7B772FB7BD35CA54DEBEF9DDF44946959DC041697)

### 调节图层间距

鼠标悬浮在Adjust the Gap of Layers按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/Hb82MumTQTGf3HdaJh8m3Q/zh-cn_image_0000002808766129.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=A650FE43E1F0C618062D24AC87110A4F357BE2FF26BFCF0408EAF062FC41F444)上，出现一个拖动条，拖动后可调节图层间的距离，范围是0~100px。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/ohA6_kU5Swe9fZgRfbs5OA/zh-cn_image_0000002808886277.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=D11FD6380CC23B37A67CC935FFD5CE263098101DB7FB79E8AA7843FEA5DABB5E)

### 显示/隐藏图层边框

DevEco Studio默认给图层加了边框，此边框并非应用自身边框，便于查看透明图层。点击Hide Border按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/AgGA2zu9T-S1Hmo-2oC6Lg/zh-cn_image_0000002808886285.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=450745F4459BDED89FF628150574A480E6CABB85461CEE91C24F14267B031DE2)或Show Border![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/IvXVL-eTQT-82lF_uUlRfA/zh-cn_image_0000002779566614.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=18D41BC09FF35169FD57D30AE4F752D1BF3D2D48746867628B00C556A3FB772E)可以隐藏或显示图层边框。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/IrKBcFPoQRGdcPJ47Ukpcw/zh-cn_image_0000002779406590.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=1F9C86E57E23327F8D6301B941A455E8AA2FE3BACF8BB1D68292AF0DF58FC538)

### 放大/缩小视图

点击Zoom In按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/7kq0iAcGTqSKCuuKGMn3xg/zh-cn_image_0000002779566546.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=A4542053FF75ED1ABE4F3D4452A2321EDAA877C4BC437D994AA83A785DE416B2)或Zoom Out按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/Vkz9hii3QDiho19xOaadGg/zh-cn_image_0000002779406600.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=DD063632518744C1C6673BBB40CD673FFA8EC8255E0B856B67B76D63176786F2)，能够放大或缩小3D视图。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/-wrHDYzTT7KPnGs31QQ2bQ/zh-cn_image_0000002779566548.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=CB3BABDD24BBA71EBCA62EC47B392CB48296A7FFD481AF441338B2237BEF3B55)

### 自适应窗口

点击Zoom to Fit Screen按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/Gize6ZBOQHyECKyz0VRk6g/zh-cn_image_0000002779406626.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=692DD2B2A435C9644015051118478C47255BC7F8338A2A9DA6C894952F243650)，能够自动根据窗口大小，调整3D图层的缩放比例，并使3D视图回到区域中间。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/C8h06j34TraUFRZfGr7A4w/zh-cn_image_0000002808886261.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=02F54913419E68DB316F8621F146612AA8A9165C58B8A8CAE4881F932DEBDE82)

### 切换正面/侧面视图

DevEco Studio默认展示侧面视图，经过复杂的旋转后，可点击Switch to Front View按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/BtKuSTj4SbmCF2GxmqH4TQ/zh-cn_image_0000002779406570.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=6106A041E9592CEBB8122834D237C1A6C4B2B620D0510CDE65D5B80106E4F76D)或Switch to Side View按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/CYCQvrsrRVqwC0cfoMltqA/zh-cn_image_0000002808766201.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=C0FA7D6E13C2A6EC58FEAA5E7C485A284DFDF820EE68794420D0A2636D780B86)，将3D视图自动调整到预设的正面或侧面视角。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/hT-fxMtzQW2edre7_MGNdA/zh-cn_image_0000002779406616.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=DE396B3ABFBF45F54A2C1274BF2EB8DFE4B4A6DF4CD26D45343C1D568DAF6385)

### 返回2D视图

点击2D View按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/Nt7PkntGQkKW2D9SQ8YfhA/zh-cn_image_0000002808766171.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=A89C2B0DE8F6A93DBBFC64B29D196E1B45B990A55E91C59A83B3805790AEEB31)，可切换至2D视图。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/_NV58zmTRASEB6GOtkvASw/zh-cn_image_0000002808766177.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=CEDCA34961EEF74B73E50F44199E7CF524792C25C2C6C6F667D267E1D3171A55)
