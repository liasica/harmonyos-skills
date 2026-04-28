---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-arkui-inspector
title: 布局分析
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 布局分析
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:55+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:eb3858bacd70131fcaef79acdeb8d914a80dcd05e75bce3e0f3a5130e969835e
---

开发者可以使用ArkUI Inspector，在DevEco Studio上查看应用在真机上的UI显示效果，并通过查看多次操作后的界面状态，快速分析定位UI界面存在的问题。

ArkUI Inspector支持的功能包括：

* [查看设备上应用的UI显示效果](ide-arkui-inspector.md#section1645813371383)。
* [导出及导入应用UI界面快照](ide-arkui-inspector.md#section0442629153111)，脱离设备查看UI显示效果。
* 在组件树上选择组件，UI界面自动框选对应组件，属性列表显示当前组件的属性信息。
* 在UI界面点击选择组件，组件树对应组件变化为选中状态，属性列表显示当前组件的属性信息。
* [UI组件源码跳转](ide-arkui-inspector.md#section1226015494335)，选中UI组件后点击源码跳转按钮即可跳转至源码位置。
* 在UI界面上选择Show Component Border，可[查看当前页面上所有组件显示区域](ide-arkui-inspector.md#section1137025915336)。
* 在组件树上选择自定义组件，属性列表显示当前组件配置的[状态变量信息以及影响组件](ide-arkui-inspector.md#section19923158103412)。
* [查看窗口交互事件](ide-arkui-inspector.md#section516993011576)，包括触屏、鼠标、按键、滚轮、窗口焦点变化事件。
* 按照组件粒度[3D展开应用](ide-arkui-inspector.md#section138812162416)，方便查看组件之间的嵌套、遮挡关系。

## 使用场景

针对界面较复杂的应用：

* 通过组件树查看组件的父子关系，检查是否存在冗余组件。
* 针对应用在真机或模拟器上运行出现UI界面显示异常，尤其经过多次界面复杂操作后产生的界面错误以及后台逻辑错误，进行问题分析定位。

## 使用约束

* 仅运行在前台的应用支持通过Inspector查看。
* 已通过USB或WLAN连接设备。
* 仅支持Stage工程。
* 仅支持全屏应用或者焦点在前台的窗口。
* 不支持应用市场上架的商用签名应用。

## 操作步骤

1. 在DevEco Studio下方点击**ArkUI Inspector**，打开ArkUI Inspector。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/jKPbJ_97SXKvquWUtMyI8g/zh-cn_image_0000002561832709.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=273FB2D62D9C831BC37FDF9B49C8A4A544A0842D8EF1FDBB0613014DDC5370C6)
2. 点击RUN![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/9vBFwfC_Rw-U5B2x8Rs_HA/zh-cn_image_0000002530912780.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=F72AC1F4EFD7240BA6F5F8F1AA7317872FA2CE7011E0147C56CC0887751E714D)或者DEBUG![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/ISVPQqYoRVKfawBcqt6H2w/zh-cn_image_0000002561832651.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=AEFA7EB25E051FE5F7E53DEB884DD65BADAB325EF964C817E33FC03689CB8D32)按钮，将应用推送安装到设备上，在设备的应用列表中选择当前显示在前台的UI进程。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/gYi-EqtJQdSl7MuequR5KQ/zh-cn_image_0000002561832715.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=9268FC044B817DE25FF780A131C28C22FF4C1DBA04F437059913CDBE84EB239A)
3. ArkUI Inspector左侧为当前的组件树结构，中间栏显示当前设备的UI界面，右侧在选中组件的情况下为当前组件的属性信息。可以在左侧组件树上或在中间UI界面点击选择组件。当设备上UI发生变化时，可点击中间栏右上角![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/i3ScXMcaRuywRqrOSAHugw/zh-cn_image_0000002561832717.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=7A9844D9804878C0FFD00E963F82B182DBAF01CA7A2673B9A00EC005DE8D22A0)按钮同步设备上的UI效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/dxBI999MTKe9oG_VnWgLmg/zh-cn_image_0000002561832725.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=7B3A7B944D7AD48012E5F8E91FF00D7E349163F33B6A432D8C973454F75A83AF)
4. 在设备框，点击设备列表的最后一项**Stop inspector**，可断开与设备的连接。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/gWU51t1hS7eQxx2xUe3UxQ/zh-cn_image_0000002561832677.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=8D9F5BBF66F6BBF439ED722856DB2CA7B0507A72E236FB8A2A0450D92DFEE828)

## 显示组件信息

* 点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/GexaXrs-RDykveh2cBkHLA/zh-cn_image_0000002530752826.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=CCD23C0C947088F1A6F2D5AA47DACDDCC10941D55E856B04A9AD630EE47046CE)，勾选**Show Tree Statistics**，可显示组件树组件信息。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/0qKZqoS4RbSgwYE1jg9VMQ/zh-cn_image_0000002530912764.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=198EBCC3CCC383445B6DD44A931851451B2670776BF04242F10948E168EDD6AA)
* 点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/JCrUdHFbTRyypLBhh3hsVQ/zh-cn_image_0000002530752780.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=288D7911D6E1206A27C3BE83DB519F94029B254D4E04BD56573CD348E412E87B)，勾选**Show Hidden Components**，可显示隐藏的组件。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/yx3uMdkHSd2Kj0Oz1Hn5uQ/zh-cn_image_0000002561752679.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=8E02793AE7F982FB26B3E9D3D505C4BA8212B9BC45F97BB5393E4D498E361E0C)
* 点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/b9A2oBxCRsC7nAhVmXwINw/zh-cn_image_0000002530912754.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=23FBAB10F6C1A50C04286B16AFD8DE5E65DF9216E734B34C4A190388B834F512)，勾选**Show Custom Components**，可过滤自定义组件。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/gR5f-0p6TnqCXbm9KzddXw/zh-cn_image_0000002530752804.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=2AC03DCB27A52FDAC7F3E08BADF1713D3570CE9FF80B088F190BB50309916CFF)
* 点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/EB7hjsAlTE6PQMwCDYv1Xw/zh-cn_image_0000002561752685.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=21986C8CE89DC63EC9EFB408FA979EC1F34FB042179B1C076930BC8BF463AA32)，勾选**Show System Components**，可过滤系统组件。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/UfWZxno6S1eCLoYr0VY-Ag/zh-cn_image_0000002530752760.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=ECFDFAC870872FDF1B25698D55E7A931546774FC92993E17FB8E12B5082359BE)

## 导入/导出UI界面快照

ArkUI Inspector支持导出及导入应用UI界面快照，脱离设备查看应用UI界面显示效果。

* 在中间栏点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/64ewuJ2TQbelmoU7EXPS-Q/zh-cn_image_0000002561752749.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=88AEB1F315750CD11633EE2ED1426E30804A217E15B5B95C950E52BB5D736EE1)可以导入本地的应用UI界面快照。导入成功后将在DevEco Studio中打开该快照。
* 在中间栏点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/P2PGO5jMRzKKX83zrBHN7A/zh-cn_image_0000002561832741.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=AE0A9FDD098A93EA554AB9F8D796199143DD25110141EB0903611D039C52740E)可以将应用UI界面快照导出到本地。导出成功后将默认在DevEco Studio中打开该快照。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/bhmEAIMKSd-ZxAymw7faQQ/zh-cn_image_0000002561832675.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=46E09699502001AFEA413473F32873BD530773E4FF890C0C6FAC430F8FBFAE5C)

## UI组件源码跳转

1. 单击**Run > Edit Configurations**，勾选“**Enable DebugLine**”，点击**OK**保存后，重新运行工程，表示开启源码跳转功能。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/-wpCWAPXRLq_nVzacQ305g/zh-cn_image_0000002561752751.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=75D7934CA928BA8BC8CF3FEB33F3D2C22B9CDB44977CAC0B3C15DCCC68997418)
2. 在ArkUI Inspector中，选中要进行源码跳转的UI组件，点击右侧的源码跳转，即可跳转到UI组件源码位置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/VgXopSiYTCq0SbUoWS8DUA/zh-cn_image_0000002530752772.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=10BDE37B6B3923C6086C53870C800BBC31E87505BA4EE6C487BD44FDF4F65FAE)

## 显示布局边框

在UI显示设置上，勾选“**Show Component Border**”，可显示当前页面所有组件的布局信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/wR1RrQySTuWEZeiTtshbxw/zh-cn_image_0000002561752695.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=2B12391853B6BDB6317983C8BF830A5F8CDE3A0AEC5D9A58C9A9AF7223807C46)

## 查看UI组件的状态变量

点击自定义组件，可以查看自定义组件的状态变量，以及状态变量影响的下一层组件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/4BEgyhalTiy8dhgB6gxUjA/zh-cn_image_0000002530752816.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=DD23BBEC8E22446674E79D71C61A7DDBBE77E83871B08CB85B32FBD5A6C46288)

## 查看窗口交互事件

从DevEco Studio 6.1.0 Beta1版本开始，支持查看[窗口交互事件](arkts-interaction-capability-overview.md)，包括触屏、鼠标、按键、滚轮、窗口焦点变化事件，帮助开发者定位窗口发生失焦、获焦、重绘等问题。

选择**WindowEvents**页签，点击Start按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/6N0r1-j2SeSvr41rg_W-qQ/zh-cn_image_0000002561832693.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=5572612EBE0D2612385A2FDF262449C992D037FF0B67C82F79C7FB4C5305F638)，开始上报事件消息，包括事件时间戳、窗口ID、事件类型、坐标等，支持按事件类型过滤。点击Stop按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/MHJl3qVoQ_-Ir3P5wA0C9A/zh-cn_image_0000002561752721.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=47FCB126DD59CD8D5EB73DF6E1EEF0A0C0D8E65A47E9E8AE445A436EB2095666)，即可停止上报事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/O1ywH2heS62TxcdMzvCR7w/zh-cn_image_0000002561752757.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=0761E361D6B4F56FE7D8518494EBE1D97F90CE7DF394E0C9B492215B8F4092D2)

## 3D展开应用

ArkUI Inspector支持将应用按照组件粒度进行3D展开，即UI界面能够在Z轴展开，方便查看组件之间的嵌套、遮挡关系。

该功能从DevEco Studio 6.0.0 Beta1版本开始支持，同时设备系统版本需要升级到API 20。

### 使用场景

* 点击图层可以精准选中和查看被遮挡的组件，可用于定位组件是否被遮挡等问题。
* 3D视图展示的图层均是组件树上参与渲染的组件，可帮助开发者判断组件是否需要进行渲染，例如过长的列表、不可见区域是否需要渲染，帮助开发者优化渲染性能。
* 对于页面复杂、小组件较多的场景，在组件树或者2D视图中难以选中，通过3D视图增加图层之间的距离，能够有效地突出小组件，使其更易于选中。

### 进入3D视图

点击3D View按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/PjxF8GwNS8KIXpmpMF-cPA/zh-cn_image_0000002561752707.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=D11B0AAE6C1255E86E598A673DDB978E5253DDA2745E979552E50A1CAF471D69)，进入3D视图。首次进入3D视图会加载3D数据，请等待数据加载完成。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/EuVp7OgTQ-2nR0aqPogf4w/zh-cn_image_0000002561752747.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=300BF05B0A71F426610A7FD062691E18CFC942E3401CFDFF6AA108A2FADFECCA)

### 基础操作

* 旋转视图：按住鼠标左键移动。
* 平移视图：按住鼠标右键移动。
* 放大/缩小视图：滚动鼠标滚轮。

### 隐藏前方图层

选中图层后，图层会显示蓝色边框，点击Hide Views in Front按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/lwqxz5JLQqCeR86EJY2XrQ/zh-cn_image_0000002561832653.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=16D7C3348C09DE30F933B92D260BA49823171F0D6238767CC66DBF640A4899D1)，能够隐藏当前选中图层前方（朝向用户）的所有图层，避免不必要图层的干扰。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/TP1__1S1R9yAwpcxexrrUA/zh-cn_image_0000002561832683.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=E3E0D16DB822A9E5B8D1EF646FA621A66453B4B3C3B130B357FD034037893EB4)

### 隐藏后方图层

和隐藏前方图层类似，选中图层后，点击Hide Views Behind按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/dCHIuCvXTzeVr5yW-obz0Q/zh-cn_image_0000002530912744.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=BA7AB5BFAE84430C55844B29453DC8D23A6A3E38B2E802EF9761D3B513A45731)，能够隐藏当前选中图层后方的所有图层。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/BISxUIQUS4y4FiSj5RwxcQ/zh-cn_image_0000002530912742.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=047E52B8113508F96154220E8FE96EA15079B4C88AC11D0FAB24AC9C3EE381F2)

### 恢复隐藏图层

点击Restore Hidden Views按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/wUy3kD2vRDySB4ZHz3Hu6w/zh-cn_image_0000002530912794.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=BBB7C636655D8918774BFF4260228A78CE8E876CDD194F66EBC33B12BD73975E)，能够恢复所有隐藏的前方图层和后方图层。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/vvkRN6C3TVi9pR5KBb13vg/zh-cn_image_0000002530912760.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=E8C0B77166E8A45F5BC9908139C1F57BE92C19666E76E1E85B5FE66ED627C02B)

### 切换图层排列顺序

图层有两种排列顺序，id顺序和层级顺序。

* id顺序：默认顺序，即渲染的顺序，也是组件真实显示的顺序，图层的遮挡关系和实际应用一致，每个图层显示在一个Z轴平面上，但如果图层数量较多，会导致Z轴过长，操作不方便。
* 层级顺序：组件树上同一层级的组件，在3D视图中会显示在相同Z轴平面上，能够有效减少3D视图下Z轴长度。

切换方式：点击Switch to Layer Order/Switch to Id Order按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/T-6zXjSlTIu1aq1jH3j0Mw/zh-cn_image_0000002561832707.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=5CF714C1C3457FA5DC03DAC23FA35FE6DC90EB5BEE3BE9AF6F5BC9F0C65A1F65)，可以将图层的排列顺序分别切换至层级顺序/id顺序。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/N0Zwb0RqQk2Z2D3RY6N81g/zh-cn_image_0000002561832671.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=ED8AD9AA89B7724C8DEB8565E69BC95346D942A9DA894070E1CE3E38579582FB)

### 调节图层间距

鼠标悬浮在Adjust the Gap of Layers按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/f0u3FPINRCGqEDmQf-JIag/zh-cn_image_0000002530752744.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=913FF74882E411946B12BE225649C1CCB465BADC6B672C01F7583D5765A5FFF2)上，出现一个拖动条，拖动后可调节图层间的距离，范围是0~100px。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/9qOeitA6TFGIdrA-bZuG0w/zh-cn_image_0000002530912812.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=C47EC0EC40780C06BA25196838EC67B622DD2D5BA0D742873AD623A0EC8EF4D5)

### 显示/隐藏图层边框

DevEco Studio默认给图层加了边框，此边框并非应用自身边框，便于查看透明图层。点击Hide Border按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/1ZPm2-bzRzOvjcZf21o9pQ/zh-cn_image_0000002530912818.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=6524F9D5A609598EC3B316751375355437B85B255A04F9852A53BC4F9B43FD3D)或Show Border![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/PWZ02HaeSByvfxU5sEhsYg/zh-cn_image_0000002530912810.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=8DD372E89D9E20D874961C6BDF28D278999F7EF18D1245068FCFB3A2B30CE0B1)可以隐藏或显示图层边框。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/zgYMW6rmQ7Gq7s6axy2yYA/zh-cn_image_0000002530752766.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=1E1EF5EFB3BE12964E80BFDA343A658DF608026683A21BDEB3D8742EB5485138)

### 放大/缩小视图

点击Zoom In按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/Ln0VdckPQ9m5-vwmaje1mQ/zh-cn_image_0000002561832655.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=3CB38F0677788F85E61B581D221E7AFFBC97FF34DA10CE33DF5434755E61B5D6)或Zoom Out按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/2dA3TsRFTFqesu_CMwi-uw/zh-cn_image_0000002561832697.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=42ED29E5B5A748D5C2FF24EFCD36439B54EFA9C915DE9BE573E233F043775EFF)，能够放大或缩小3D视图。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/uxYSco3-R4qukU8mkadW3g/zh-cn_image_0000002530912736.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=1677D6A48720A603DE9E2B04A8513296825111E325376F49F530575C4E5AE48B)

### 自适应窗口

点击Zoom to Fit Screen按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/T1bmiQQFQuKLnR0lZe3lPw/zh-cn_image_0000002530752800.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=A6BE439DCB8397878E2C8EAE64C5DC151E9DD72BBD965994A755A02EB02C9785)，能够自动根据窗口大小，调整3D图层的缩放比例，并使3D视图回到区域中间。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/rvLLoHY2QlypTGuDtcR1ow/zh-cn_image_0000002530912790.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=1669C53BE8526CC9DB0CEB2D1B86D00267F3F322C86C2D092C9002901B0ADA75)

### 切换正面/侧面视图

DevEco Studio默认展示侧面视图，经过复杂的旋转后，可点击Switch to Front View按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/HkYU1srFTsyg1xzgzQZDrw/zh-cn_image_0000002561832657.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=06F6368D131B8F1E30D1CAF9E25E4AA930D78C025A20FB1A0EA37F46EBE398F2)或Switch to Side View按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/zZiBhj42Qk-zMwSzl6W1zQ/zh-cn_image_0000002561752761.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=9B873A4D1992D9967FF0D11E4045FD18065C4B53AB4C774F25E47AAE221CE6BA)，将3D视图自动调整到预设的正面或侧面视角。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/vAURWBsZTsivCBCMY8gKQQ/zh-cn_image_0000002530912786.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=A06FF472C11C0207487F0F80E5BC5665F4592E443C18270D94973DF35C210958)

### 返回2D视图

点击2D View按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/nsufb-UURbyGeCFpP3erkA/zh-cn_image_0000002530912782.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=05F4B154A84421E77C22181249ABB909965C4548CAC8F312ED8ED1EEC0ACEE60)，可切换至2D视图。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/NhM2LmmIS2yOU3hbl--Zow/zh-cn_image_0000002530752792.png?HW-CC-KV=V1&HW-CC-Date=20260427T235653Z&HW-CC-Expire=86400&HW-CC-Sign=BAEFDD0E7CCCF10936B3A1F09FD0D79060E47CE3296FF9D8555FEB4FE41E3390)
