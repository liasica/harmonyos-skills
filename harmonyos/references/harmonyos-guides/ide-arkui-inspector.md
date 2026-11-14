---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-arkui-inspector
title: 布局分析
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 布局分析
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:00+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:9ad1218d49fd275a41f6cf9835020e7873eff38545f1a0bc086e9be9d4498576
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/UaFy5Q5PQBW9sABa_fPDdg/zh-cn_image_0000002808886255.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=F1B49093E034BBAAFC283CC8DEE080EB3566C8421D3120C92BF15B6AA921B992)
2. 点击RUN![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/DjpNgH8PSr-j3CtbhgYUuQ/zh-cn_image_0000002808766167.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=DDF30333515E233A8887627C87300306934AE235A62C6CF9D4C75BCE56CB3364)或者DEBUG![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/NcV-6ELPRSuYK5DAld46GA/zh-cn_image_0000002779566542.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=90BCF45679A6EEC2B7923081CB875E58A060F159EDA448B2F05B1BDDF8192E18)按钮，将应用推送安装到设备上，在设备的应用列表中选择当前显示在前台的UI进程。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/fSX6q6RUTkCA4g3aJ6CUMQ/zh-cn_image_0000002779566596.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=0780C76529FEA018B7B14FD99B15CFE88F979891FD9D729553A50F0A6BB83409)
3. ArkUI Inspector左侧为当前的组件树结构，中间栏显示当前设备的UI界面，右侧在选中组件的情况下为当前组件的属性信息。可以在左侧组件树上或在中间UI界面点击选择组件。当设备上UI发生变化时，可点击中间栏右上角![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/t3kFgPlYRq-2Q3MrkuFnMQ/zh-cn_image_0000002779406624.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=F033D1E6F78E68BD0CAB56ADEE976B14FBF6B5E0262974AA4CC8AF8E8030B0E8)按钮同步设备上的UI效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/kgAIwbZbSxWUyHoyEvSoAg/zh-cn_image_0000002779566608.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=3F579296978C784C5908E720B561E87B1C48F44A402BCC0B99E09EBB757C2139)
4. 在设备框，点击设备列表的最后一项**Stop inspector**，可断开与设备的连接。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/dv7dg56dTbOt0kNFNnVrRw/zh-cn_image_0000002779406582.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=C27E04F0AA9656A81CD9DCA145E97E54809EAEE59C76BEE71059BA6A5D421D41)

## 显示组件信息

* 点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/BeJRh0y6TxCbKi0qMTUPcw/zh-cn_image_0000002779566624.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=AAE2BC785EE117FAC9974D442CF2463E39F4B0546B670C29009BF50051340D02 "点击放大")，勾选**Show Tree Statistics**，可显示组件树组件信息。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/QwSQBKgJT_GO_BnLUzZyWg/zh-cn_image_0000002808766153.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=0E2BA7D1235AF0AD4AAC7B2166C1B8238BAB91E856872EDCA80EB4A0584E8637)
* 点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/0BAkfVd4SrqTR0uMZpo2ng/zh-cn_image_0000002779406602.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=620CB4F3AFE6CE969BC4AA75054A4BD61B1CFD13305BFC0AD74D66140C026647 "点击放大")，勾选**Show Hidden Components**，可显示隐藏的组件。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/udODHXPISHaDtntRUACnSA/zh-cn_image_0000002808886211.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=28D5DDDE5CDD905F263E33B8997CD7FE89AE0E2BCC37EB095313B60FBA0C4A18)
* 点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/uddAmNQ6QhaeFCBtu2DCVw/zh-cn_image_0000002808886225.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=E2475A72845062950CB488A98ADA466A7858512AC8A3D18198E48D5260314211 "点击放大")，勾选**Show Custom Components**，可过滤自定义组件。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/hm_ytEsgRcC0HqX67zUXUA/zh-cn_image_0000002808886269.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=1BEDDA9E6372E170E6A7C21B0861186441A270BE38BA7F19803BAADDB391AED7)
* 点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/V8TkhhKARVmaCyS4WsWspQ/zh-cn_image_0000002808886213.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=A68C4DA5DD67B0D1797BF60CABDAE9AFA2B99B8FE36DE6845C985C4033686DB4 "点击放大")，勾选**Show System Components**，可过滤系统组件。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/1rd78xRCQ6OnthuSPnui4Q/zh-cn_image_0000002779566564.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=A6178EA31185A8E65238DF85760BBAA6EF318E3FF47413785E52EFDDBCC78D0E)

## 导入/导出UI界面快照

ArkUI Inspector支持导出及导入应用UI界面快照，脱离设备查看应用UI界面显示效果。

* 在中间栏点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/rO1QgfTxQlaQLWB93UsLgA/zh-cn_image_0000002779406634.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=796C8B801B872A3745ECB4FA8155FDED7C95FC353B63EC86A099BCD0CBA9BA54)可以导入本地的应用UI界面快照。导入成功后将在DevEco Studio中打开该快照。
* 在中间栏点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/qzO4gUxMT_KajO2GBaBPow/zh-cn_image_0000002808886281.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=472ADE6F61E45D626796962BAFEEA7E462A6DBCB3E4C6B52374AACDF68ADE6C9)可以将应用UI界面快照导出到本地。导出成功后将默认在DevEco Studio中打开该快照。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/Yy1XcvxKSpOESZNrNVH6aQ/zh-cn_image_0000002779566558.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=AD92C93AE3789B662A16626B9438D2FCC5A1567ED34E067DCF59422443F7F47A)

## UI组件源码跳转

1. 单击**Run > Edit Configurations**，勾选“**Enable DebugLine**”，点击**OK**保存后，重新运行工程，表示开启源码跳转功能。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/h_xGAtcETVa7_rSXNoF9kA/zh-cn_image_0000002808886275.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=ECA946339496BA139F33AFCF3E84D527B97EE72FB8FA6084E763B900301A734D)
2. 在ArkUI Inspector中，选中要进行源码跳转的UI组件，点击右侧的源码跳转，即可跳转到UI组件源码位置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/FKAes4jZTOGfGD3CWZsbSg/zh-cn_image_0000002779566574.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=79D31DB51E977261765DCA0E58A5175BC53B747BD2B2B68D5D28DD64E8A2601D)

## 显示布局边框

在UI显示设置上，勾选“**Show Component Border**”，可显示当前页面所有组件的布局信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/TJjBruU1QLmzsbWNk9SM2Q/zh-cn_image_0000002808766141.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=C0570ED7E886D594DBF43CCECE6B639EFFBC8BCBAF6A417C7218FFDB1AF9D252)

## 查看UI组件的状态变量

点击自定义组件，可以查看自定义组件的状态变量，以及状态变量影响的下一层组件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/R46kL0qrStK6YXNk_7pZGA/zh-cn_image_0000002808766195.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=304C3E241F59E4BC4743C2C47DBADBE87ADA4413E70F35C46AB600EC7E555197)

## 查看窗口交互事件

从DevEco Studio 6.1.0 Beta1版本开始，支持查看[窗口交互事件](arkts-interaction-capability-overview.md)，包括触屏、鼠标、按键、滚轮、窗口焦点变化事件，帮助开发者定位窗口发生失焦、获焦、重绘等问题。

选择**WindowEvents**页签，点击Start按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/D7QOeQ_FRFS8j3EU3xcv-Q/zh-cn_image_0000002779406598.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=5ECF013C82BBB1CF2944C6294D61FE44F616F721CD4EBB199ADA06F22523932D)，开始上报事件消息，包括事件时间戳、窗口ID、事件类型、坐标等，支持按事件类型过滤。点击Stop按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/9o52v34qQeWiWJ6KNvltsg/zh-cn_image_0000002808886247.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=0C208669D70BFB1910B9163F85C06D16DBB06929B2F932BBB4F9E7C4B82DF405)，即可停止上报事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/gOFW_Tq5RxC-y3srKpLNOg/zh-cn_image_0000002808766197.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=FF8AAA23574896C86B6A8D6B5574990175B803E4803F97D61BFF1BCF223B50FA)

## 3D展开应用

ArkUI Inspector支持将应用按照组件粒度进行3D展开，即UI界面能够在Z轴展开，方便查看组件之间的嵌套、遮挡关系。

该功能从DevEco Studio 6.0.0 Beta1版本开始支持，同时设备系统版本需要升级到API 20。

### 使用场景

* 点击图层可以精准选中和查看被遮挡的组件，可用于定位组件是否被遮挡等问题。
* 3D视图展示的图层均是组件树上参与渲染的组件，可帮助开发者判断组件是否需要进行渲染，例如过长的列表、不可见区域是否需要渲染，帮助开发者优化渲染性能。
* 对于页面复杂、小组件较多的场景，在组件树或者2D视图中难以选中，通过3D视图增加图层之间的距离，能够有效地突出小组件，使其更易于选中。

### 进入3D视图

点击3D View按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/WoQrrzKpREiUAi25MsdHuQ/zh-cn_image_0000002779406592.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=2F4685D944775BE59652F63757159A458AE7FBB53035BA0870758F41D5B0DC5F)，进入3D视图。首次进入3D视图会加载3D数据，请等待数据加载完成。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/cpAlGc1SSH6iGX3k1S8VoA/zh-cn_image_0000002808766191.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=9B1B48FC5C1584BEDC63A93639C1F52DD033F12659C7F33EA2E32B224744682B)

### 基础操作

* 旋转视图：按住鼠标左键移动。
* 平移视图：按住鼠标右键移动。
* 放大/缩小视图：滚动鼠标滚轮。

### 隐藏前方图层

选中图层后，图层会显示蓝色边框，点击Hide Views in Front按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/dhGrHT5xTNiP7d0Mdonyug/zh-cn_image_0000002779406566.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=2DCEA1EC126F55C49578AC146FAF9EF3373024B82C3EA928D95C56D97AD40251)，能够隐藏当前选中图层前方（朝向用户）的所有图层，避免不必要图层的干扰。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/e5-oqauLRCqVrenaj73-rQ/zh-cn_image_0000002779406588.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=9E658D67C74CAE8D044409DC62EE109B97739CF4727D6635F11BF377468CFE8C)

### 隐藏后方图层

和隐藏前方图层类似，选中图层后，点击Hide Views Behind按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/CDVodSCjSZOiuTZHehShww/zh-cn_image_0000002779406576.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=3FF3AA31B318AC9844E8A5505A4C66A03991E48E92F7F18D2A7554F2A03A736B)，能够隐藏当前选中图层后方的所有图层。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/PGxnewmxQvKeXhDxSygF-A/zh-cn_image_0000002808766133.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=19C106D9FC79AD590C35C84CE567B850757365366CC2ADDADE2A90703C13B7B5)

### 恢复隐藏图层

点击Restore Hidden Views按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/fQgCk6oXQ4K5zWUU75gvXA/zh-cn_image_0000002779566602.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=BA1ED0E02B1A5BB09223406DC6093A0D4416918E14CBE7080EDAD20430887062)，能够恢复所有隐藏的前方图层和后方图层。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/OrUDQePMRfqL8RjjzpOikg/zh-cn_image_0000002779566566.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=97B7CED1DC24B6E4907788884713590EBC6DB5D7958A64BE100709323ED11B6A)

### 切换图层排列顺序

图层有两种排列顺序，id顺序和层级顺序。

* id顺序：默认顺序，即渲染的顺序，也是组件真实显示的顺序，图层的遮挡关系和实际应用一致，每个图层显示在一个Z轴平面上，但如果图层数量较多，会导致Z轴过长，操作不方便。
* 层级顺序：组件树上同一层级的组件，在3D视图中会显示在相同Z轴平面上，能够有效减少3D视图下Z轴长度。

切换方式：点击Switch to Layer Order/Switch to Id Order按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/ESzGTAt4TPqLZAYs6WjrYQ/zh-cn_image_0000002808886251.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=2E2B37AA17E8FEACBBB8FD0278DBD5E52F3AFECC98F63F408527BE8BC4F291CB)，可以将图层的排列顺序分别切换至层级顺序/id顺序。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/5EgKMkARRJqMtH-6QsWYsQ/zh-cn_image_0000002808886219.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=978B0DFC98696C98DD5948CF6CF5BC1FD59D5B2EF294DAC8BAD90A69BE3B44E0)

### 调节图层间距

鼠标悬浮在Adjust the Gap of Layers按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/5NGVDzVxTgO6aHoyPjwjRQ/zh-cn_image_0000002808766129.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=A7817D29CEBB4B25BAB813ED3C00D0FCB2253806B9A12CA02F8BB265C79D6220)上，出现一个拖动条，拖动后可调节图层间的距离，范围是0~100px。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/6PdqzG74RiaqiLPcRHZ-zA/zh-cn_image_0000002808886277.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=452EB917819C84FA15FA1FE21E80B365FC10DBD3DA83C931F06EDCC4AE39E94E)

### 显示/隐藏图层边框

DevEco Studio默认给图层加了边框，此边框并非应用自身边框，便于查看透明图层。点击Hide Border按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/aBRgTEN_QJeBVwGm0XVqzA/zh-cn_image_0000002808886285.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=9A0EBBA7C48FB6BDC4053DB812273F86270AD139D3B11958DF895DAC325623C9)或Show Border![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/rdikbiboSniLuOLj3lQyYA/zh-cn_image_0000002779566614.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=4A0B0C7FA5B99D67F6EDC163A3618999E3F78CF02BE5D79EC57E407754E20A0A)可以隐藏或显示图层边框。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/FfdXdV9GQcS0eVjXfnI0MA/zh-cn_image_0000002779406590.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=769884A2D351E8423BBD3616ACD44224FFCC06E55C0367C26819408C30B745F3)

### 放大/缩小视图

点击Zoom In按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/0Ti8Q52RRvS3g-nT0BaLCw/zh-cn_image_0000002779566546.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=F6C6005F5E70F87BE2BCEBCE7B2636364803E1BFB845A2E2A17FA550B9ACE180)或Zoom Out按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/mMZWm2qyQu-LyVVwjzG9yg/zh-cn_image_0000002779406600.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=CC24D2B4A16C4822B6C691A702DDFCCD159D4360965747A054C01D8BE4283B62)，能够放大或缩小3D视图。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/Nqxe5D7PQrCZPi6PoQIhbg/zh-cn_image_0000002779566548.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=9B1EBFC0CD3D5089FD30B405E5270B9A88E75B1B0AB52A368046A2D6EE2659DD)

### 自适应窗口

点击Zoom to Fit Screen按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/C3KJm4pGRly9BcoI_3bR_g/zh-cn_image_0000002779406626.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=DBCA1FDBE11C229051A28A00DDB785CA1E1E8901261574A3AEB0A3EC84456ECC)，能够自动根据窗口大小，调整3D图层的缩放比例，并使3D视图回到区域中间。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/c2koDXMiRLSy0A3dWUis3g/zh-cn_image_0000002808886261.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=865CD8E8CF9E8BB72C77FC1C72A7F138A5FCD036FA1F665C26CE22E38B05B1BF)

### 切换正面/侧面视图

DevEco Studio默认展示侧面视图，经过复杂的旋转后，可点击Switch to Front View按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/e-hZ5eP8T1i7e9pmpxvtNA/zh-cn_image_0000002779406570.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=804A405F8700C3EDA0B8D3CF956D508EBC99D41D4FDA58C5F5E088997BF0F459)或Switch to Side View按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/vyJI-jf3R-Gvdm69RwJrbA/zh-cn_image_0000002808766201.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=F7ECC46AC19928B9FCF10DAFD8AB9D5A7033E8FBACE99A2415A63259F3CD072A)，将3D视图自动调整到预设的正面或侧面视角。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/Z7CVxKf-QTeqN5l2tzVPAg/zh-cn_image_0000002779406616.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=AD98B2EFCD998E05AAD4B8D208EF2FEAC080DF6D963321C093168373358AA025)

### 返回2D视图

点击2D View按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/snFZiMR2RnKo74yjQN4CRg/zh-cn_image_0000002808766171.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=7177AFCBB79C25C131B1F8B500E286935947EA2CA2E6E34FDC948DD367D47A59)，可切换至2D视图。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/ViN9PBO0QQiyda5wYve7AA/zh-cn_image_0000002808766177.png?HW-CC-KV=V1&HW-CC-Date=20261114T004900Z&HW-CC-Expire=31536000000&HW-CC-Sign=B2FB634C82DA23256FB2BAC04A87BBE3FFB87E751DBA9E0882B3991E0EA6BB7A)
