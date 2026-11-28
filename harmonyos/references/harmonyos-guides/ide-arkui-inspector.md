---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-arkui-inspector
title: 布局分析
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 布局分析
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:39+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:d86366f95ec88485d32cd1c230eede2f9437f3877ebb64cb394ef1dcae1f3f9c
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/L-9T5guAS7ikS5ME06CWrQ/zh-cn_image_0000002808886255.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=C8B066279D34875BFD682A341ECBB22F05FE37250D8945785959477B80E32C9B)
2. 点击RUN![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/RSKsh8PkTay46szm19NLNw/zh-cn_image_0000002808766167.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=23BDF5C553989C1E4D02B36C0C76120C8859E03CFF284C18E47822F84C69651B)或者DEBUG![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/i-bxXDWUTQKxH6aG2UiC4g/zh-cn_image_0000002779566542.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=4F9F44E1E4E27B905AA4A17784BB9458C23A251F1FC38557FC4123EF2BC5224C)按钮，将应用推送安装到设备上，在设备的应用列表中选择当前显示在前台的UI进程。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/5M4cw36pTNiC205NyBqGAg/zh-cn_image_0000002779566596.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=A19430B9BB3E15EE034711FD5AA79DA75B47463BF2ED93B50654EF281A57196A)
3. ArkUI Inspector左侧为当前的组件树结构，中间栏显示当前设备的UI界面，右侧在选中组件的情况下为当前组件的属性信息。可以在左侧组件树上或在中间UI界面点击选择组件。当设备上UI发生变化时，可点击中间栏右上角![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/QXYNuc2kR1K5ZCo2f-5Hpw/zh-cn_image_0000002779406624.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=4F101A4B95F72322A6CDB3A3FD4E615336E1DBA6A5119944478AAB2F605BB4AE)按钮同步设备上的UI效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/dwTaVdvgT4eXLAqELrAf1A/zh-cn_image_0000002779566608.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=712428023B5636F1810698FEA894A111E75A112F3F4B7FF18C11E6DAB7132B86)
4. 在设备框，点击设备列表的最后一项**Stop inspector**，可断开与设备的连接。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/NhlhXoJkT4SmzE8cy6N6Hg/zh-cn_image_0000002779406582.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=2753641F7F5110F80C81A913212F938A0B9E7C289F1A68E3C576E4FB70E09E47)

## 显示组件信息

* 点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/JLXG_aVdRcqBIaxga46nTQ/zh-cn_image_0000002779566624.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=5D5F0CD281AEA6D5D92A9F83BDF8D64308208C1F3B332BED4D0BE8E43B3AD6D2 "点击放大")，勾选**Show Tree Statistics**，可显示组件树组件信息。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/c93R5A5rR_CjFpKh5RARBg/zh-cn_image_0000002808766153.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=B694E1AF01AB45E00DA14CC3F0167DFFC9D7204CD760E069B5AC3F3F20F904E6)
* 点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/3lYv--HjT5ipOKZIkaXYyw/zh-cn_image_0000002779406602.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=4344D4EFF153A8CB207B199D492A9DB5C0ADC3EFC4A472CE4FE8A70F1098D397 "点击放大")，勾选**Show Hidden Components**，可显示隐藏的组件。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/_9UnwYI5QG6nqi7mpkxQHw/zh-cn_image_0000002808886211.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=D0386146FE05FB96690E4A1A81EF605C8C6B52C08918E1C1A1E1AA59D50588E1)
* 点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/hzM8_KCZQoSp1Kl6WNdAmA/zh-cn_image_0000002808886225.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=345C6F4188C3781DC5104C3D12A51C4DA798D2889DDC7479857CCCF3B8D4245B "点击放大")，勾选**Show Custom Components**，可过滤自定义组件。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/vZeHVYTQSyqLdF85T3JrAg/zh-cn_image_0000002808886269.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=3C3461D5D7993F46D4A15C82C55D3C64961E7A618D4FDC12F24F05345C03B7E0)
* 点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/y5c9zY2JTeCtNIdoxoHEMg/zh-cn_image_0000002808886213.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=39D27D63225AFE00CB9FE37ECC4FC5F5789FCBB0EC064B508F074B91C02BEBE2 "点击放大")，勾选**Show System Components**，可过滤系统组件。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/TtevSBjWSmi2ubYOFCWCcg/zh-cn_image_0000002779566564.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=017D36BFA8D9E82940F92309A78E45BBC0109C0470B5F7051B16D4DFC56ABAA2)

## 导入/导出UI界面快照

ArkUI Inspector支持导出及导入应用UI界面快照，脱离设备查看应用UI界面显示效果。

* 在中间栏点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/5I4b4emNTueGwYuaOq8DYw/zh-cn_image_0000002779406634.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=AD7FCC4DBC31690C0C28F9EA616B753E87A32BBEC81B2CC2259F9C5562B8FC61)可以导入本地的应用UI界面快照。导入成功后将在DevEco Studio中打开该快照。
* 在中间栏点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/-fybeiEkSYG_LzDc8xo1Cg/zh-cn_image_0000002808886281.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=0387AA34E6D2BD2E765B48B9B559A229F7A0BB56D2C8946C2D7B25B117AC12A0)可以将应用UI界面快照导出到本地。导出成功后将默认在DevEco Studio中打开该快照。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/Mdyx97BRTZ2CrGpSnAWHKA/zh-cn_image_0000002779566558.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=5D5F0DD5751FF8FE919295FB0BB21FAF63DA0D0723192994427763B31B7B45B0)

## UI组件源码跳转

1. 单击**Run > Edit Configurations**，勾选“**Enable DebugLine**”，点击**OK**保存后，重新运行工程，表示开启源码跳转功能。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/1j8ymEfXSSSjVWwz16mx5A/zh-cn_image_0000002808886275.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=7B36E7C1E1503D792B0E8E01154B8185752E7AE9381927364480839A25AB3E3D)
2. 在ArkUI Inspector中，选中要进行源码跳转的UI组件，点击右侧的源码跳转，即可跳转到UI组件源码位置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/H2mOfKX3R7G1aAQMoyWmEw/zh-cn_image_0000002779566574.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=FC50CB71FDC7EBBD1B96A99484EB427AAF300D30223A8769C3D0C48F1DE6D805)

## 显示布局边框

在UI显示设置上，勾选“**Show Component Border**”，可显示当前页面所有组件的布局信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/SsR6gtcIQAesGd0q7F_W5Q/zh-cn_image_0000002808766141.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=FB85D8804A33A4F33B5120263A2403E522066E88FCBC6CEB17C8E0249476C336)

## 查看UI组件的状态变量

点击自定义组件，可以查看自定义组件的状态变量，以及状态变量影响的下一层组件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/_Uwx-GlAR8-BqdKJm0zRxg/zh-cn_image_0000002808766195.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=BAB88B315168ABD01F783CF855F4FD0403F8BEF6E16E0FD68CE1B34C38F32A60)

## 查看窗口交互事件

从DevEco Studio 6.1.0 Beta1版本开始，支持查看[窗口交互事件](arkts-interaction-capability-overview.md)，包括触屏、鼠标、按键、滚轮、窗口焦点变化事件，帮助开发者定位窗口发生失焦、获焦、重绘等问题。

选择**WindowEvents**页签，点击Start按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/hWZ_0YyZQAGHwC_W66ylUw/zh-cn_image_0000002779406598.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=679C4189152A02CD6B84B2FCEC4B6363FC927E1D6D0D88C9A1616B4EAC74EE63)，开始上报事件消息，包括事件时间戳、窗口ID、事件类型、坐标等，支持按事件类型过滤。点击Stop按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/KQ4BW1ObQJem1wz6Oc3QWQ/zh-cn_image_0000002808886247.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=F7740101693E526C75B1F6DB075FF1DEA707606AA4F3BD76D80A2079DF9034E1)，即可停止上报事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/dKd7PXLJT8uBK_xoTSuUjg/zh-cn_image_0000002808766197.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=52D4975F8C8291FB62993A80532CC8784A572FD1F19A8BEA8E31D7A6AC884E55)

## 3D展开应用

ArkUI Inspector支持将应用按照组件粒度进行3D展开，即UI界面能够在Z轴展开，方便查看组件之间的嵌套、遮挡关系。

该功能从DevEco Studio 6.0.0 Beta1版本开始支持，同时设备系统版本需要升级到API 20。

### 使用场景

* 点击图层可以精准选中和查看被遮挡的组件，可用于定位组件是否被遮挡等问题。
* 3D视图展示的图层均是组件树上参与渲染的组件，可帮助开发者判断组件是否需要进行渲染，例如过长的列表、不可见区域是否需要渲染，帮助开发者优化渲染性能。
* 对于页面复杂、小组件较多的场景，在组件树或者2D视图中难以选中，通过3D视图增加图层之间的距离，能够有效地突出小组件，使其更易于选中。

### 进入3D视图

点击3D View按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/4teIUGWbSqingfD0-0WJfw/zh-cn_image_0000002779406592.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=7656C0A290BA6DFC704141B4BF5B896534A4C9FAABBFC039195B0D039A60DD82)，进入3D视图。首次进入3D视图会加载3D数据，请等待数据加载完成。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/2lNfMKcDTnOxXQnC2miENA/zh-cn_image_0000002808766191.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=D4A4316540CF5F38DFE84B159D33DDD63641C28302982A4AE46239274A317591)

### 基础操作

* 旋转视图：按住鼠标左键移动。
* 平移视图：按住鼠标右键移动。
* 放大/缩小视图：滚动鼠标滚轮。

### 隐藏前方图层

选中图层后，图层会显示蓝色边框，点击Hide Views in Front按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/6dVj3ImIQqeJNHid3b8HIA/zh-cn_image_0000002779406566.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=EA40D23240F43D2E4CE8052CD6236E52090ADFCF034AC8EF652A85A62814F28C)，能够隐藏当前选中图层前方（朝向用户）的所有图层，避免不必要图层的干扰。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/GpLEs38oQ9WNM2sPSV6hhA/zh-cn_image_0000002779406588.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=2842737516CA2C174D5ED89C78B2E7FD9E7C1D9F4590249B30A31C297BD1AE5C)

### 隐藏后方图层

和隐藏前方图层类似，选中图层后，点击Hide Views Behind按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/-hZrieOBTqeh6Hc1dpa7mg/zh-cn_image_0000002779406576.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=59AB1B3C331F15456F4B3BB1CE226E9A879B6E58EA73E8345808669029844728)，能够隐藏当前选中图层后方的所有图层。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/igiuyrU-TX6kpKIXplcK7g/zh-cn_image_0000002808766133.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=4FC0D0FE4C78CA6769712D96E2CA35C574B7E1D38EECF5AE55DA7EBCDF84FD69)

### 恢复隐藏图层

点击Restore Hidden Views按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/cKBlIhnLQ-GP4GXVdMBgDg/zh-cn_image_0000002779566602.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=90410F5D5CD214BA5B836E7F496D66F9869C4F7F040575D0EA97497848264CF8)，能够恢复所有隐藏的前方图层和后方图层。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/9nYtT4s8Slygtf6sC0mjTA/zh-cn_image_0000002779566566.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=CF39811C055778606B2468553B7DA8F904FCE54E8A03929AC7726A1C8C96B0B4)

### 切换图层排列顺序

图层有两种排列顺序，id顺序和层级顺序。

* id顺序：默认顺序，即渲染的顺序，也是组件真实显示的顺序，图层的遮挡关系和实际应用一致，每个图层显示在一个Z轴平面上，但如果图层数量较多，会导致Z轴过长，操作不方便。
* 层级顺序：组件树上同一层级的组件，在3D视图中会显示在相同Z轴平面上，能够有效减少3D视图下Z轴长度。

切换方式：点击Switch to Layer Order/Switch to Id Order按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/awJ7iG87QGCggfbGZkIxqw/zh-cn_image_0000002808886251.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=8A73E8BD0D08588268A361A3429719100A5A15E2A3652A8EC383F1C77A4028CC)，可以将图层的排列顺序分别切换至层级顺序/id顺序。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/Pvdo438WQnKbt4lxuWD8Dw/zh-cn_image_0000002808886219.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=96C52DB309091763CFA3B0562FED7EE8D8CC1AC9506FBDD7207118D9FA23F1EA)

### 调节图层间距

鼠标悬浮在Adjust the Gap of Layers按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/PlyZaw6-RU2ymwE2L8iqNw/zh-cn_image_0000002808766129.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=EA4D63FB5E721FD5FF8027A3A7D99C821B5E7C0DEE89300B0FEAF83AC3008455)上，出现一个拖动条，拖动后可调节图层间的距离，范围是0~100px。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/lE0e_KYoRIa5vonqEe0JFA/zh-cn_image_0000002808886277.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=D9D65BEEAC9B463F5E76CECED918076727B96612A3FCB4BABC26E20ED73E1EFE)

### 显示/隐藏图层边框

DevEco Studio默认给图层加了边框，此边框并非应用自身边框，便于查看透明图层。点击Hide Border按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/xoMdhBOpQjGtj3i8QzIm5A/zh-cn_image_0000002808886285.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=C97F07BA1CBDDC24FC1B18A4C38CB286AB350F1AA115AF26732F07DC11E7C59B)或Show Border![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/UXX4DQqdSl6553DPZ4vAtQ/zh-cn_image_0000002779566614.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=67D47D9B0809283846F8CE031698676118815259B4C9EDFB23D7C6E6D1768669)可以隐藏或显示图层边框。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/g3EP4EoYQQyt1d6Rf-wYcA/zh-cn_image_0000002779406590.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=E810BDE341AADC21AE97790C78873B11763DB1B2C784561CD2EDDABE441013FC)

### 放大/缩小视图

点击Zoom In按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/-ZraStfkS8q0er0FJLhWQA/zh-cn_image_0000002779566546.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=09C8C48F21524280B40E6E983B873C429355160A272F8460E36A5FA7CCE8FE8C)或Zoom Out按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/SbwPjkbsRumR8kArddHvig/zh-cn_image_0000002779406600.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=5C044C3230F98051116BB97D343B894E8D3E98E1B14ADADD16AC856A4C265ACB)，能够放大或缩小3D视图。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/4mZEK0_CQAmaAGiGqqqtTw/zh-cn_image_0000002779566548.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=B663D2826483CF8FBB79AC19DEB809870B52A45D7E5A3C23991A28A960A30AA4)

### 自适应窗口

点击Zoom to Fit Screen按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/V_T-Bq7GTP-W268snQfMcQ/zh-cn_image_0000002779406626.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=E50D07CC4099C91A53AB8EB33F6DA06723AAF67084603735865EFC7C8BA2C80D)，能够自动根据窗口大小，调整3D图层的缩放比例，并使3D视图回到区域中间。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/dNEgYiZLQm2j2cvZdNA7kQ/zh-cn_image_0000002808886261.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=493E183F2E512F0D67DCFEDD7E0042B5A349ED606FD42DC01A83404F5D0EAB3B)

### 切换正面/侧面视图

DevEco Studio默认展示侧面视图，经过复杂的旋转后，可点击Switch to Front View按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/ZpzjimLoT5mrk_khpuUDzw/zh-cn_image_0000002779406570.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=C4436F25A79338FAC91E1EECDEBBCC0BB4F643281C4A95D34FE6BE517D632E25)或Switch to Side View按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/jKvynWrBS7esmWLlwDRtjw/zh-cn_image_0000002808766201.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=E082F67C18008F4CE1F112F22D32216C88FF246C84586329B75EEA1C6F180071)，将3D视图自动调整到预设的正面或侧面视角。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/8G1NQaboTrW5Ara371O7jg/zh-cn_image_0000002779406616.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=426938810AC8125E6A3CA107F1628094876FEA2D04996CB8C27D328D8B6984B0)

### 返回2D视图

点击2D View按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/BCS88GvUQLakoIN3_IQC0A/zh-cn_image_0000002808766171.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=C2FB23310D4AC744506E5529EDCEB18D85F381CAC452AD9FD7A1DF3B8AC428DB)，可切换至2D视图。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/MqNIKFrmQm2qtujP84HGjw/zh-cn_image_0000002808766177.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=DD91A04968CB69E6A93BC990EACAB0693E55949277C1522118CB9AD0FA4E1668)
