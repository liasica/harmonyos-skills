---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-arkui-inspector
title: 布局分析
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 布局分析
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:1aa650873c976fb804c42dd4183d820850f36755fe3c3c082c8b1f01395f6b97
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/Novaq4b6SDue9Wnb8sp0zA/zh-cn_image_0000002808886255.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=D2C93C7EF4BF6890050DDFCF0099B43C78C14F9CFA0DC656DF022B30E7453D21)
2. 点击RUN![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/Tw8nihloTguWwTMkpnmSVw/zh-cn_image_0000002808766167.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=470B23216C19C501242D1B8C6C6D5297C5F32ECF4056055E1C391FD954D39739)或者DEBUG![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/FqW7KuiDRTuJUv5or-FdCg/zh-cn_image_0000002779566542.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=19D0B1D1DFB0CCC73320B3B7BBA60FCE85D82F6AC4A54C3CE244147CC67DF4DA)按钮，将应用推送安装到设备上，在设备的应用列表中选择当前显示在前台的UI进程。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/4aKsgCMnRA6UCq-Q74JInw/zh-cn_image_0000002779566596.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=3B233E2D5C610EB74CD3E49BE8368AE99C650BDBAD867BAD4B33AA7E22E29B8F)
3. ArkUI Inspector左侧为当前的组件树结构，中间栏显示当前设备的UI界面，右侧在选中组件的情况下为当前组件的属性信息。可以在左侧组件树上或在中间UI界面点击选择组件。当设备上UI发生变化时，可点击中间栏右上角![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/MshGhXWdSu62NaGsaUS8TQ/zh-cn_image_0000002779406624.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=30C4E4712FC9B08AD756E380563BFDDD17D56ACC2FA6D83E31C8D67BA52B31A1)按钮同步设备上的UI效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/Yg1ekRCzTIq61mim7c0z0Q/zh-cn_image_0000002779566608.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=39B424E6D919E80DC35C3F9404B1E0528005F57C311F5E5D23FFBDF811998F18)
4. 在设备框，点击设备列表的最后一项**Stop inspector**，可断开与设备的连接。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/BFEJ41oETfOansu0FKMzFA/zh-cn_image_0000002779406582.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=8353D5913A0BB608A8D466D97D11BB80A8E0961B72F25276AB8FD7C74FBD9AD4)

## 显示组件信息

* 点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/ue-2BprAQoSkfyBoBdVhNg/zh-cn_image_0000002779566624.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=9DF65224987496166CE3AC2AF12287543F688026E6025BFCBB5CD0F6AE26F388 "点击放大")，勾选**Show Tree Statistics**，可显示组件树组件信息。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/IdYMSgTAQ_S596MUPXaBwQ/zh-cn_image_0000002808766153.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=922C3303C96F72950EBE65A1F55EDC31F3F0C62B9396BAE4DE2F28C8B53E1D0C)
* 点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/xq5YGmKBRgK4Qgg2MQJAIg/zh-cn_image_0000002779406602.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=4F3D5C1F90EE51148D54F5B25E975618967A0429CE39631E1F7772A79D75F827 "点击放大")，勾选**Show Hidden Components**，可显示隐藏的组件。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/bktgeCv4S4y-XCnfnshAUg/zh-cn_image_0000002808886211.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=15AAFF07F675B5B03BCFD735E7AFCB16A4BE8A52D56BE532465B3D89F6127FB9)
* 点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/cN65PvF7QFWcWNMDiXhTxg/zh-cn_image_0000002808886225.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=CE935E3EFDF6749353492A20C5AA4348FAB9218D9C15242CE1D149D29EC92C4B "点击放大")，勾选**Show Custom Components**，可过滤自定义组件。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/nvQwypP9SG6G1n-4Rn83lw/zh-cn_image_0000002808886269.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=63B89D376C2C9E257367187B104FF59CCA4CDC656274666FDDB36382351D6EAD)
* 点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/uSeIP018SSW-uii7q79IoA/zh-cn_image_0000002808886213.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=7321BDFFA0F4E361576730F5E47F77BBD6FAE7C2051CC47CBAF220C2FD98B562 "点击放大")，勾选**Show System Components**，可过滤系统组件。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/MpdRZ_LWSlq9jC-kvPY6hQ/zh-cn_image_0000002779566564.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=8788FE2D82847EB558ECBE04B29B673C3FF5C3A5BB9CEAE9ECFB070D8032B9EE)

## 导入/导出UI界面快照

ArkUI Inspector支持导出及导入应用UI界面快照，脱离设备查看应用UI界面显示效果。

* 在中间栏点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/KoqmYjQKSkeVuxZop8Qy9A/zh-cn_image_0000002779406634.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=8B21087CFCF4B4FB703E0E6015EE8D2C1804768D04FA1F435B93F9849589DA6A)可以导入本地的应用UI界面快照。导入成功后将在DevEco Studio中打开该快照。
* 在中间栏点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/Fx-C4HuvQTOQZkUTqKDluA/zh-cn_image_0000002808886281.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=9129C676246A4C57F5CD1921FD1549F4B144C115C3251C9EF56CC6B27A50920A)可以将应用UI界面快照导出到本地。导出成功后将默认在DevEco Studio中打开该快照。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/9dFhZorPQzOXjP6Il1ilkw/zh-cn_image_0000002779566558.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=E3C2DDF54C23761A776A987F6B97EBACE4039AD69F11A49F6D91CA89DE80FF59)

## UI组件源码跳转

1. 单击**Run > Edit Configurations**，勾选“**Enable DebugLine**”，点击**OK**保存后，重新运行工程，表示开启源码跳转功能。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/a17nVNCBQSKc63FwV9K35A/zh-cn_image_0000002808886275.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=A24A3B840410958EF69254E04EE2B018AE22015AA8C324A1C6617760FFC11DBF)
2. 在ArkUI Inspector中，选中要进行源码跳转的UI组件，点击右侧的源码跳转，即可跳转到UI组件源码位置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/CUBUCqlcSDGXKarDX7kGfQ/zh-cn_image_0000002779566574.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=511C748879D049F44876C2DF937C7DBA1F2E7014B6F974A5FA9A784E848412BC)

## 显示布局边框

在UI显示设置上，勾选“**Show Component Border**”，可显示当前页面所有组件的布局信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/Yn74fEmaTv-b2WIgUJdGdg/zh-cn_image_0000002808766141.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=25198C28205054F5122FFCBF1C474326576C14EF53B918665B016E3EED6F8048)

## 查看UI组件的状态变量

点击自定义组件，可以查看自定义组件的状态变量，以及状态变量影响的下一层组件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/T09mby8aSPy4HocenQeTcA/zh-cn_image_0000002808766195.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=2B8508026827EEDFE4B7163ED7E0E79FD1075A8589D6CE04E81551A762CD30CA)

## 查看窗口交互事件

从DevEco Studio 6.1.0 Beta1版本开始，支持查看[窗口交互事件](arkts-interaction-capability-overview.md)，包括触屏、鼠标、按键、滚轮、窗口焦点变化事件，帮助开发者定位窗口发生失焦、获焦、重绘等问题。

选择**WindowEvents**页签，点击Start按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/B_tw-Wa3RH-bMoDecsodGQ/zh-cn_image_0000002779406598.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=FEE0FB08EBEC678E4B75FE31CD9F6A694924EB7576E026F051EF55A69E232879)，开始上报事件消息，包括事件时间戳、窗口ID、事件类型、坐标等，支持按事件类型过滤。点击Stop按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/zYZisKS6Qj2PF2E3lQ_Rag/zh-cn_image_0000002808886247.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=17B0E97F7FC897043947B03F5BF89CC2F90D4B3BCCAB6840EA2DFFFB6B4D7D2E)，即可停止上报事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/9IBwUILtRjihLOigYJrSHg/zh-cn_image_0000002808766197.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=EAC3C6FF8DD763B0CE467BDBFB2F4EC80A0299172EA09067C2F92B5D1854AC8C)

## 3D展开应用

ArkUI Inspector支持将应用按照组件粒度进行3D展开，即UI界面能够在Z轴展开，方便查看组件之间的嵌套、遮挡关系。

该功能从DevEco Studio 6.0.0 Beta1版本开始支持，同时设备系统版本需要升级到API 20。

### 使用场景

* 点击图层可以精准选中和查看被遮挡的组件，可用于定位组件是否被遮挡等问题。
* 3D视图展示的图层均是组件树上参与渲染的组件，可帮助开发者判断组件是否需要进行渲染，例如过长的列表、不可见区域是否需要渲染，帮助开发者优化渲染性能。
* 对于页面复杂、小组件较多的场景，在组件树或者2D视图中难以选中，通过3D视图增加图层之间的距离，能够有效地突出小组件，使其更易于选中。

### 进入3D视图

点击3D View按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/iVZ5A3jyQ76tfkME0IvRZQ/zh-cn_image_0000002779406592.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=DEAC47DD50054CAB5D267A5C3FE305A3358B36BDBDB549D9DD48F588DFD517C3)，进入3D视图。首次进入3D视图会加载3D数据，请等待数据加载完成。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/FwKNIyOJRgibhWCLvcWp0w/zh-cn_image_0000002808766191.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=FB13F23222186543603B7ED1B51FC2DE766A5C9B1359D8616F4C01FD24660B29)

### 基础操作

* 旋转视图：按住鼠标左键移动。
* 平移视图：按住鼠标右键移动。
* 放大/缩小视图：滚动鼠标滚轮。

### 隐藏前方图层

选中图层后，图层会显示蓝色边框，点击Hide Views in Front按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/bChvGc3nSIC6Q0rLqyltNA/zh-cn_image_0000002779406566.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=1A4834DA96B4904EED74F1650AD6061F770DBD4EC8855A7438996C954219692A)，能够隐藏当前选中图层前方（朝向用户）的所有图层，避免不必要图层的干扰。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/11JXfNLpR-KTxs2kx2Hcpg/zh-cn_image_0000002779406588.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=A45345B5717F1D21F7E4C9200CED810D31451445DB59E99E59E7277E3471C33C)

### 隐藏后方图层

和隐藏前方图层类似，选中图层后，点击Hide Views Behind按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/XD9z7-mdQu6xmRq2OjxwRA/zh-cn_image_0000002779406576.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=7DEA76C56FFD5A804BC5495A1BBE2E84A2BD0F46E086821CB4981ECCFBB46121)，能够隐藏当前选中图层后方的所有图层。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/F_ee6jr7R76SyJJ0Me7JCQ/zh-cn_image_0000002808766133.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=C70D9D506D873CD44F579A19CC4623B49BC62D3689CA75620BD5283AD5D6A089)

### 恢复隐藏图层

点击Restore Hidden Views按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/Bg8WJngfREy740A7LkJqbg/zh-cn_image_0000002779566602.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=1959FFED6D828B485812505370C8EF681BE95B3A00A52C000B407384456C5CFA)，能够恢复所有隐藏的前方图层和后方图层。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/RcNB0eBsQk64pJf_Edafdw/zh-cn_image_0000002779566566.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=5DC5BCED4CA80B630EE6CAC4B8D5708E9C42A8F4DA9144FF75081EA87371B37B)

### 切换图层排列顺序

图层有两种排列顺序，id顺序和层级顺序。

* id顺序：默认顺序，即渲染的顺序，也是组件真实显示的顺序，图层的遮挡关系和实际应用一致，每个图层显示在一个Z轴平面上，但如果图层数量较多，会导致Z轴过长，操作不方便。
* 层级顺序：组件树上同一层级的组件，在3D视图中会显示在相同Z轴平面上，能够有效减少3D视图下Z轴长度。

切换方式：点击Switch to Layer Order/Switch to Id Order按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/VjQ9PmXESa-NyxLUPUAQNw/zh-cn_image_0000002808886251.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=1A47940830F326ACD438D6251A36CCF19463ADD002DF8363490CF0B313555CA0)，可以将图层的排列顺序分别切换至层级顺序/id顺序。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/AHT-aaLXRs6l9B8jHIN35Q/zh-cn_image_0000002808886219.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=150D8DB860F90591AE7947BB885CC18FB36154F3123AA584EF66D4825C159078)

### 调节图层间距

鼠标悬浮在Adjust the Gap of Layers按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/koITZQWCT9Cqijn-1D6Cxw/zh-cn_image_0000002808766129.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=388067A2B9588B8596BEAB36C8FE16F4F29E2776BCDCB25096D8AE1532A71B8F)上，出现一个拖动条，拖动后可调节图层间的距离，范围是0~100px。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/flk1G053QU2KBcy8htixgQ/zh-cn_image_0000002808886277.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=57FD564ACA462E510C340503CCA63343EC643A938D7E7E705974EB87065DB3EC)

### 显示/隐藏图层边框

DevEco Studio默认给图层加了边框，此边框并非应用自身边框，便于查看透明图层。点击Hide Border按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/KdYTlaDMQLq-Kuw3SAN4Ow/zh-cn_image_0000002808886285.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=740A01F88338E5F0967730D765581961B0C4D66DC738ABFB432FEAD84493BA01)或Show Border![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/BsXjb3nqTr-QGklskrXJKQ/zh-cn_image_0000002779566614.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=662910AAE5B84AA2B02FEBB345F64456AE3E187A94CDBC083850123D9911D256)可以隐藏或显示图层边框。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/RUj8cDtvQCukK1qNSBNY-Q/zh-cn_image_0000002779406590.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=FFB5E76AB320E64EE86E9B28EC9F6599DEADCBAB63F48F0357A5E6A9A9FA5F57)

### 放大/缩小视图

点击Zoom In按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/VIQujcIHRJyRK7vdj9Stdw/zh-cn_image_0000002779566546.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=155E358F1CE8D6DAD033ED1AFF2FEFE3C5A3A3D022F2B7AD181FD9CB1AF4E4A8)或Zoom Out按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/gVId3hJLR5OU_WICn1u25g/zh-cn_image_0000002779406600.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=29755CDD0F3B27A45469F39E5FE66ECA399A8BB7F64D26E811EE6ABE3A89ED4F)，能够放大或缩小3D视图。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/mDWDbyh1Rju_cIopjsBkBw/zh-cn_image_0000002779566548.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=56C4F8C2B614FB3D325AA22013E63BEF655DBF2654FD5078A740D4AE686D9974)

### 自适应窗口

点击Zoom to Fit Screen按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/5kdsgLxCRSK1RWPcoXF2mA/zh-cn_image_0000002779406626.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=B68112B563A37275946877539C016DC37EA08BE92B6E436176ACC6F74D7081B8)，能够自动根据窗口大小，调整3D图层的缩放比例，并使3D视图回到区域中间。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/tjSDMZ19QbKQLINq-zZ-tQ/zh-cn_image_0000002808886261.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=79DFA6CB0CC7373F03685952D608334EA0416C897B5DA47659CA50398BC4CDF4)

### 切换正面/侧面视图

DevEco Studio默认展示侧面视图，经过复杂的旋转后，可点击Switch to Front View按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/QfT1sXpQQfqIideXelHbGA/zh-cn_image_0000002779406570.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=5221294D8EBE0A02E926CFC4EA929BE7961CC206412F84AB294C40BA2AC21315)或Switch to Side View按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/CbUcDZYhQLe3jUz7LqL6UQ/zh-cn_image_0000002808766201.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=5EFA36E60920E12120A073812BCAEE0FD7461242726555E4ADF8E45D7E4A7602)，将3D视图自动调整到预设的正面或侧面视角。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/MJ97VhNkQXGWEBqtuODOZw/zh-cn_image_0000002779406616.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=64D9D9411042789B2B6034AE8CBDABD3C5238FFD35DA1F6CEB0E307E33E19DB9)

### 返回2D视图

点击2D View按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/LxkW0HzyRymRRa5-Y-sQXw/zh-cn_image_0000002808766171.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=D1E584605410FC0B8EC62249D67A6BA144D5FB3C808FECACEC2D12604F80DEAE)，可切换至2D视图。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/X1indfcMTlu8YD9q_EfTGA/zh-cn_image_0000002808766177.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=D6C41B31126F9E153C5738DC873C53CB3C99CC8AFE6BB278BCAFC87944AE26AE)
