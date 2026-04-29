---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-arkui-inspector
title: 布局分析
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 布局分析
category: harmonyos-guides
scraped_at: 2026-04-29T13:46:53+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2ee68a89c1b1910217becbc02766a080bd65e5407e0c1b8c589632aa8f48946a
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/DkG9bNpUS3uu_1MeyvBvXg/zh-cn_image_0000002561832709.png?HW-CC-KV=V1&HW-CC-Date=20260429T054648Z&HW-CC-Expire=86400&HW-CC-Sign=AB7D40AA4DF2E7C8A14B071EDD14BDE263398343FFE0E264672B0F08702ADF68)
2. 点击RUN![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/Qs-a48mBS-WxdDPHIEJp_Q/zh-cn_image_0000002530912780.png?HW-CC-KV=V1&HW-CC-Date=20260429T054648Z&HW-CC-Expire=86400&HW-CC-Sign=A95A164769C0C095D8D54914D6B3EB4D1254962610C5BF904A995757934230EE)或者DEBUG![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/EhKKrtTzQA6RS1yE2I5vUw/zh-cn_image_0000002561832651.png?HW-CC-KV=V1&HW-CC-Date=20260429T054648Z&HW-CC-Expire=86400&HW-CC-Sign=2E6ED072FDE4102CA750371586CF7B86B18429EB6B7AB9B14ACB1281AE1C47D6)按钮，将应用推送安装到设备上，在设备的应用列表中选择当前显示在前台的UI进程。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/VxAHKiU0SIKCS7YILjX7mg/zh-cn_image_0000002561832715.png?HW-CC-KV=V1&HW-CC-Date=20260429T054648Z&HW-CC-Expire=86400&HW-CC-Sign=EB189D21C9ACEFF90DE93631AFD65B5B9D7CE92ED8DF2373BB99A70FA5F504B0)
3. ArkUI Inspector左侧为当前的组件树结构，中间栏显示当前设备的UI界面，右侧在选中组件的情况下为当前组件的属性信息。可以在左侧组件树上或在中间UI界面点击选择组件。当设备上UI发生变化时，可点击中间栏右上角![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/h0t31GAtS8KWHdXVH8R4gQ/zh-cn_image_0000002561832717.png?HW-CC-KV=V1&HW-CC-Date=20260429T054648Z&HW-CC-Expire=86400&HW-CC-Sign=EBBF32E64A90E706AC0FC45183EBBB4617311980FC02B67B9E897DC92D002F2C)按钮同步设备上的UI效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/TWOEOPSlSFG5z3jKfr2ruA/zh-cn_image_0000002561832725.png?HW-CC-KV=V1&HW-CC-Date=20260429T054648Z&HW-CC-Expire=86400&HW-CC-Sign=E989CCA5E6C7573150C483E8C9528E1D717B650875B77F847FA7D94BD03D1720)
4. 在设备框，点击设备列表的最后一项**Stop inspector**，可断开与设备的连接。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/t7v3fSXgQfqIV23768GAzw/zh-cn_image_0000002561832677.png?HW-CC-KV=V1&HW-CC-Date=20260429T054648Z&HW-CC-Expire=86400&HW-CC-Sign=A08E1135A3526CE693F3E99074D76D2D02A485B959F93B171D6354ABEA493925)

## 显示组件信息

* 点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/fWauICbLTHS81wmzEw6mVQ/zh-cn_image_0000002530752826.png?HW-CC-KV=V1&HW-CC-Date=20260429T054648Z&HW-CC-Expire=86400&HW-CC-Sign=FD8E789A2CF3B1D9A914F1DFC541F5427A18B245A6250858B23C3992D84C289F)，勾选**Show Tree Statistics**，可显示组件树组件信息。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/8MOhIz-ZQY24n_n1_IeJEA/zh-cn_image_0000002530912764.png?HW-CC-KV=V1&HW-CC-Date=20260429T054648Z&HW-CC-Expire=86400&HW-CC-Sign=9031ECE80359DDF2EDEC12A9A05B39FD2AA4E4096FE8F324A57B892CF94AF1D2)
* 点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/zBhRzowITX2F2Nr9Nw5Vvg/zh-cn_image_0000002530752780.png?HW-CC-KV=V1&HW-CC-Date=20260429T054648Z&HW-CC-Expire=86400&HW-CC-Sign=34217F204764A20C3AE9A6343D57BB040E3EB3BD61B98DFFD67C6D0A64A31D63)，勾选**Show Hidden Components**，可显示隐藏的组件。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/NoeIvf-ISQyOOpk2tH__ag/zh-cn_image_0000002561752679.png?HW-CC-KV=V1&HW-CC-Date=20260429T054648Z&HW-CC-Expire=86400&HW-CC-Sign=21836402477087057705CA2B431883C4D3D46B5C7B2D3BFCC7569A304B99CAED)
* 点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/SI0LLAapR7eh-dfOFqoI0A/zh-cn_image_0000002530912754.png?HW-CC-KV=V1&HW-CC-Date=20260429T054648Z&HW-CC-Expire=86400&HW-CC-Sign=85C7E6434ADAB65A9B93BA5CBBFDD066166FFEFD3E93406F1C1973A28790E88C)，勾选**Show Custom Components**，可过滤自定义组件。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/QksAVATaTuu-EqCwAR-EfQ/zh-cn_image_0000002530752804.png?HW-CC-KV=V1&HW-CC-Date=20260429T054648Z&HW-CC-Expire=86400&HW-CC-Sign=018A436F8964B189271183DF572C4233B2A7A1F7CC06600AB98A5EC3A971B206)
* 点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/SftHHB1FT_uOL6yl1FYw_A/zh-cn_image_0000002561752685.png?HW-CC-KV=V1&HW-CC-Date=20260429T054648Z&HW-CC-Expire=86400&HW-CC-Sign=9541699022BD9BC474769A337D987F60D5917CB49E1C92604C1B888B68D1351D)，勾选**Show System Components**，可过滤系统组件。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/LXwChF66RAa_PbIS6j830w/zh-cn_image_0000002530752760.png?HW-CC-KV=V1&HW-CC-Date=20260429T054648Z&HW-CC-Expire=86400&HW-CC-Sign=AE7107FDCE2639656E568E5010B8DCD8B75121CC930B1FE835F85B4A02AFAE42)

## 导入/导出UI界面快照

ArkUI Inspector支持导出及导入应用UI界面快照，脱离设备查看应用UI界面显示效果。

* 在中间栏点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/90IhpFTeSkux9j44yt_sOQ/zh-cn_image_0000002561752749.png?HW-CC-KV=V1&HW-CC-Date=20260429T054648Z&HW-CC-Expire=86400&HW-CC-Sign=F22E8FF2E91B7F39CBAD3C5D29056D8D6A692DE733F0CE1F65BE77B1C24F1985)可以导入本地的应用UI界面快照。导入成功后将在DevEco Studio中打开该快照。
* 在中间栏点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/lNVOtrLVS52_uPMHnD9B9A/zh-cn_image_0000002561832741.png?HW-CC-KV=V1&HW-CC-Date=20260429T054648Z&HW-CC-Expire=86400&HW-CC-Sign=82232D19677381D914D01F7A7C1253D5DE4CF558C48B9FEE449027CB3051B9C0)可以将应用UI界面快照导出到本地。导出成功后将默认在DevEco Studio中打开该快照。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/Vsv474wwSdSn54iqlpY30A/zh-cn_image_0000002561832675.png?HW-CC-KV=V1&HW-CC-Date=20260429T054648Z&HW-CC-Expire=86400&HW-CC-Sign=05066672C8ECD230E02BC67EF6BC56FA78FA57F5FFE21A50621FACE827277531)

## UI组件源码跳转

1. 单击**Run > Edit Configurations**，勾选“**Enable DebugLine**”，点击**OK**保存后，重新运行工程，表示开启源码跳转功能。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/aSRsL9AkTo-4L2yMfYaNHw/zh-cn_image_0000002561752751.png?HW-CC-KV=V1&HW-CC-Date=20260429T054648Z&HW-CC-Expire=86400&HW-CC-Sign=9531E70EAF2FEF7DA7B9DF1AC4B406A810774686E2D3D8701DBB97834407F307)
2. 在ArkUI Inspector中，选中要进行源码跳转的UI组件，点击右侧的源码跳转，即可跳转到UI组件源码位置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/zU-SN8ZBTh-NO_y233-mOQ/zh-cn_image_0000002530752772.png?HW-CC-KV=V1&HW-CC-Date=20260429T054648Z&HW-CC-Expire=86400&HW-CC-Sign=DB41CF06E6D72E3D350C3442B451F8E731E0A88E45B72E9A195FB2F6EC710D87)

## 显示布局边框

在UI显示设置上，勾选“**Show Component Border**”，可显示当前页面所有组件的布局信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/B7wPQPspSGq22-8v9Vv-jA/zh-cn_image_0000002561752695.png?HW-CC-KV=V1&HW-CC-Date=20260429T054648Z&HW-CC-Expire=86400&HW-CC-Sign=051984635AC229C53FFD31FB19DA7D84A3199488267AF64A06728D323E2CB540)

## 查看UI组件的状态变量

点击自定义组件，可以查看自定义组件的状态变量，以及状态变量影响的下一层组件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/50ah4Vm-SwGSkOLeW_B4PA/zh-cn_image_0000002530752816.png?HW-CC-KV=V1&HW-CC-Date=20260429T054648Z&HW-CC-Expire=86400&HW-CC-Sign=086CDA9E59639F65AD6156C71002B86F60B527A584D25B033D87FEE615649511)

## 查看窗口交互事件

从DevEco Studio 6.1.0 Beta1版本开始，支持查看[窗口交互事件](arkts-interaction-capability-overview.md)，包括触屏、鼠标、按键、滚轮、窗口焦点变化事件，帮助开发者定位窗口发生失焦、获焦、重绘等问题。

选择**WindowEvents**页签，点击Start按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/CQvdCihnQtOQQgCrd4OORQ/zh-cn_image_0000002561832693.png?HW-CC-KV=V1&HW-CC-Date=20260429T054648Z&HW-CC-Expire=86400&HW-CC-Sign=039FB1BDBDF6B5615E5022B8C226AF4FEDA9E985398077C985C921CC1363841E)，开始上报事件消息，包括事件时间戳、窗口ID、事件类型、坐标等，支持按事件类型过滤。点击Stop按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/PcLPEY-6QEmqXfw90-5rwA/zh-cn_image_0000002561752721.png?HW-CC-KV=V1&HW-CC-Date=20260429T054648Z&HW-CC-Expire=86400&HW-CC-Sign=70CCD799ACB9A9E3B60313A9C8D0999CEF41CC32B880CE20C9C35781B1C5D6AB)，即可停止上报事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/p4Bjk2zgQnaKqBV8sZRgwA/zh-cn_image_0000002561752757.png?HW-CC-KV=V1&HW-CC-Date=20260429T054648Z&HW-CC-Expire=86400&HW-CC-Sign=5935A26D96B4C83F3E0A018E36D590B30795732C209F1FA869F8C1DB0FDFDCE1)

## 3D展开应用

ArkUI Inspector支持将应用按照组件粒度进行3D展开，即UI界面能够在Z轴展开，方便查看组件之间的嵌套、遮挡关系。

该功能从DevEco Studio 6.0.0 Beta1版本开始支持，同时设备系统版本需要升级到API 20。

### 使用场景

* 点击图层可以精准选中和查看被遮挡的组件，可用于定位组件是否被遮挡等问题。
* 3D视图展示的图层均是组件树上参与渲染的组件，可帮助开发者判断组件是否需要进行渲染，例如过长的列表、不可见区域是否需要渲染，帮助开发者优化渲染性能。
* 对于页面复杂、小组件较多的场景，在组件树或者2D视图中难以选中，通过3D视图增加图层之间的距离，能够有效地突出小组件，使其更易于选中。

### 进入3D视图

点击3D View按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/V4rBG13JRrurcoY3GImHLQ/zh-cn_image_0000002561752707.png?HW-CC-KV=V1&HW-CC-Date=20260429T054648Z&HW-CC-Expire=86400&HW-CC-Sign=9F7B8C6CC39CD2F74C8E3497B0AF0A6A03474B716339CD9377771DD02613EFE0)，进入3D视图。首次进入3D视图会加载3D数据，请等待数据加载完成。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/GNHwS1n0QFS0um6NxhTzwA/zh-cn_image_0000002561752747.png?HW-CC-KV=V1&HW-CC-Date=20260429T054648Z&HW-CC-Expire=86400&HW-CC-Sign=6370697EEF41B870D0B37A8B27F7D258D56680DA53BEA7FBDB890078ECB93A5E)

### 基础操作

* 旋转视图：按住鼠标左键移动。
* 平移视图：按住鼠标右键移动。
* 放大/缩小视图：滚动鼠标滚轮。

### 隐藏前方图层

选中图层后，图层会显示蓝色边框，点击Hide Views in Front按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/BrlnGVi-RLe1yN6EFvR_Yg/zh-cn_image_0000002561832653.png?HW-CC-KV=V1&HW-CC-Date=20260429T054648Z&HW-CC-Expire=86400&HW-CC-Sign=7FD813A12BB3C28D6982D17A6AE8FAA01D0F39A4C325717DB9536432EFE00548)，能够隐藏当前选中图层前方（朝向用户）的所有图层，避免不必要图层的干扰。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/PVSDtjVKT9aDZ56jDZLWjg/zh-cn_image_0000002561832683.png?HW-CC-KV=V1&HW-CC-Date=20260429T054648Z&HW-CC-Expire=86400&HW-CC-Sign=7A9A498230465216DA4AD7B58CE6F71816BFCC1DAE30BE5C1399691B90040A69)

### 隐藏后方图层

和隐藏前方图层类似，选中图层后，点击Hide Views Behind按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/EqZdgYhjQgmLxLabr-G4LA/zh-cn_image_0000002530912744.png?HW-CC-KV=V1&HW-CC-Date=20260429T054648Z&HW-CC-Expire=86400&HW-CC-Sign=0C7375000308170B83A8B117609210A8938FD62310024A065F6AC844BE00DC7E)，能够隐藏当前选中图层后方的所有图层。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/jyaAfxVjRtuzwX6WecPMAQ/zh-cn_image_0000002530912742.png?HW-CC-KV=V1&HW-CC-Date=20260429T054648Z&HW-CC-Expire=86400&HW-CC-Sign=648FE00356871CC7F004847023705ABE97DF11B925D405F93F2500FE8B6EEA13)

### 恢复隐藏图层

点击Restore Hidden Views按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/B46axJvOTf29p-wRG29YbQ/zh-cn_image_0000002530912794.png?HW-CC-KV=V1&HW-CC-Date=20260429T054648Z&HW-CC-Expire=86400&HW-CC-Sign=A199292B387A302CEF6DE7AC109848A222B5838B2C68059726023FC278907570)，能够恢复所有隐藏的前方图层和后方图层。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/OvljrGNMRSOXHaEhH24Z5Q/zh-cn_image_0000002530912760.png?HW-CC-KV=V1&HW-CC-Date=20260429T054648Z&HW-CC-Expire=86400&HW-CC-Sign=9D03285B6A6AAB26A29732406AEAC1CF8111724C4C4C8BB017BD5A266A969B05)

### 切换图层排列顺序

图层有两种排列顺序，id顺序和层级顺序。

* id顺序：默认顺序，即渲染的顺序，也是组件真实显示的顺序，图层的遮挡关系和实际应用一致，每个图层显示在一个Z轴平面上，但如果图层数量较多，会导致Z轴过长，操作不方便。
* 层级顺序：组件树上同一层级的组件，在3D视图中会显示在相同Z轴平面上，能够有效减少3D视图下Z轴长度。

切换方式：点击Switch to Layer Order/Switch to Id Order按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/hPHvIY2KQcqdgyMBZxqgEA/zh-cn_image_0000002561832707.png?HW-CC-KV=V1&HW-CC-Date=20260429T054648Z&HW-CC-Expire=86400&HW-CC-Sign=AFFB28C54DB84F29A685F0B4F9E317D9CAE0724EB87E465B9DBF7B7FE8EE4D51)，可以将图层的排列顺序分别切换至层级顺序/id顺序。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/0WOuyvJKRly6dPVJlwbWpQ/zh-cn_image_0000002561832671.png?HW-CC-KV=V1&HW-CC-Date=20260429T054648Z&HW-CC-Expire=86400&HW-CC-Sign=157B2AEDA71710FBC62FA53D789FFC2227B80DFFCCF7F63DC60622E3A3152D40)

### 调节图层间距

鼠标悬浮在Adjust the Gap of Layers按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/Gw1nlhxFTAihB9T6E4lBaQ/zh-cn_image_0000002530752744.png?HW-CC-KV=V1&HW-CC-Date=20260429T054648Z&HW-CC-Expire=86400&HW-CC-Sign=CEA38B01C4952E6E9AD5B1E9BF6E341FA627F49808650B7ACFD485F5053B766B)上，出现一个拖动条，拖动后可调节图层间的距离，范围是0~100px。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/vvbRXJRuTDSUdX5c8KhcZw/zh-cn_image_0000002530912812.png?HW-CC-KV=V1&HW-CC-Date=20260429T054648Z&HW-CC-Expire=86400&HW-CC-Sign=53DB503BD1DCA20A20BA2DFD632F0F516FDCCD62BC59219059474ABF1B98BA65)

### 显示/隐藏图层边框

DevEco Studio默认给图层加了边框，此边框并非应用自身边框，便于查看透明图层。点击Hide Border按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/NUo8i5yuQAm8z4uunKZ58Q/zh-cn_image_0000002530912818.png?HW-CC-KV=V1&HW-CC-Date=20260429T054648Z&HW-CC-Expire=86400&HW-CC-Sign=2FAB60978A8DCBC6E89FFF8360964C7F906D6F254D38A5CF9708EE988A0A6465)或Show Border![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/ARUUiqUARWCl8VurItHPrg/zh-cn_image_0000002530912810.png?HW-CC-KV=V1&HW-CC-Date=20260429T054648Z&HW-CC-Expire=86400&HW-CC-Sign=D6DA3B442B31E06D1C3D9407AC63D144793665C23419BBA970C6F07536E0625F)可以隐藏或显示图层边框。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/jyZ3Eb0KSviJG1KnbGmblA/zh-cn_image_0000002530752766.png?HW-CC-KV=V1&HW-CC-Date=20260429T054648Z&HW-CC-Expire=86400&HW-CC-Sign=00A57AB96DC0F06BEFBB8D3362B8953EE5FD0F448E3CFA0CE04E7A0492286783)

### 放大/缩小视图

点击Zoom In按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/Dfv8mmWoRrCdEcXcxmYAAA/zh-cn_image_0000002561832655.png?HW-CC-KV=V1&HW-CC-Date=20260429T054648Z&HW-CC-Expire=86400&HW-CC-Sign=8AB4ECBBCA75B88413E147C9D1343F19C631024C3F206F78353C5A46DFF21CE5)或Zoom Out按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/Zvfl1-6WQB-rDCT44GzZgg/zh-cn_image_0000002561832697.png?HW-CC-KV=V1&HW-CC-Date=20260429T054648Z&HW-CC-Expire=86400&HW-CC-Sign=7C3D2B11AB59546C6C3F9B8FEF1A90469D820ACC40C5FD2ABAC017FCC5222C18)，能够放大或缩小3D视图。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/pbYa4OOtTkmE3RROaQsUOA/zh-cn_image_0000002530912736.png?HW-CC-KV=V1&HW-CC-Date=20260429T054648Z&HW-CC-Expire=86400&HW-CC-Sign=78B7100F2A63ECBF0CD4AA952E6EB6A8730FB8178283E9FDE823A71CD76FDE65)

### 自适应窗口

点击Zoom to Fit Screen按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/q9N0bPL0QW-bZnipUFpQMQ/zh-cn_image_0000002530752800.png?HW-CC-KV=V1&HW-CC-Date=20260429T054648Z&HW-CC-Expire=86400&HW-CC-Sign=DF28175B2953F36019B027304DC01769F5526B53BCF608C14A413F6B53048881)，能够自动根据窗口大小，调整3D图层的缩放比例，并使3D视图回到区域中间。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/6MU0MafKQmq6qOUcOixVYg/zh-cn_image_0000002530912790.png?HW-CC-KV=V1&HW-CC-Date=20260429T054648Z&HW-CC-Expire=86400&HW-CC-Sign=B30589152EFC218484E25D67A0922096CD571DAAF7C9A20415965B8FF06F7360)

### 切换正面/侧面视图

DevEco Studio默认展示侧面视图，经过复杂的旋转后，可点击Switch to Front View按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/1IEkHnJsSO6oYatOooD6VA/zh-cn_image_0000002561832657.png?HW-CC-KV=V1&HW-CC-Date=20260429T054648Z&HW-CC-Expire=86400&HW-CC-Sign=41BE4420468E06EA2E6432754D1225A43CE068E3402D9FE5445E1A7953974858)或Switch to Side View按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/w_MSwGVWROyRBvsOxcvxCQ/zh-cn_image_0000002561752761.png?HW-CC-KV=V1&HW-CC-Date=20260429T054648Z&HW-CC-Expire=86400&HW-CC-Sign=C712CC0294D732A9F82DD51E41CCEAEFE41F9F0B74EAF80BE782B1E377F9FAD9)，将3D视图自动调整到预设的正面或侧面视角。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/CjU_EC8kQ8KR1bVwIH48eg/zh-cn_image_0000002530912786.png?HW-CC-KV=V1&HW-CC-Date=20260429T054648Z&HW-CC-Expire=86400&HW-CC-Sign=F7D7B1B7E528871DA89CE1D1570DCE459E37C73BB57F6E012F23995F29489AEB)

### 返回2D视图

点击2D View按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/J_Y6OF5RS02F2cnkoCnLwg/zh-cn_image_0000002530912782.png?HW-CC-KV=V1&HW-CC-Date=20260429T054648Z&HW-CC-Expire=86400&HW-CC-Sign=46D1EA6027EC293306B319C795CA7A729FFDC6B06BB06BD0B323F7E113E5F04B)，可切换至2D视图。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/j2KpGskpSBCaT3RyIHXG1Q/zh-cn_image_0000002530752792.png?HW-CC-KV=V1&HW-CC-Date=20260429T054648Z&HW-CC-Expire=86400&HW-CC-Sign=C3A1A3E3D09E9131563BC590801D1B4F4AE3B2E7DDED2A0E8481005ACBFF60E8)
