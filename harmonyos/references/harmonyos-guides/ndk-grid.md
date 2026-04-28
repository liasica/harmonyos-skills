---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-grid
title: 使用网格
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (基于NDK构建UI) > 构建布局 > 使用网格
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:16+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b4e6d8f2d397723fcea4d1d3242b4c3d92d250a1b93175ea743527fe00c494c9
---

## 概述

ArkUI开发框架从API version 12开始在NDK接口提供了网格组件，使用网格可以将页面按行列分割成单元格，并指定子组件所在单元格和占用的行列数，从而实现不同的布局需求。例如页面上大小不同的卡片和应用图标、按日期分组显示图片等。

[创建网格](ndk-grid.md#创建网格)后，可以[设置子组件所占行列数](ndk-grid.md#设置子组件所占行列数)，滚动场景还可以[处理滚动事件](ndk-grid.md#处理滚动事件)。

使用NDK接口构建UI界面以及NDK基本使用，可以参考[接入ArkTS页面](ndk-access-the-arkts-page.md)。

## 创建网格

通过[ArkUI\_NativeNodeAPI\_1](../harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1.md)调用[createNode(ARKUI\_NODE\_GRID)](../harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#createnode)得到组件对象指针，并设置[ArkUI\_NodeAttributeType](../harmonyos-references/capi-native-node-h.md#arkui_nodeattributetype)中的列数NODE\_GRID\_COLUMN\_TEMPLATE、行数NODE\_GRID\_ROW\_TEMPLATE、列间距NODE\_GRID\_COLUMN\_GAP和行间距NODE\_GRID\_ROW\_GAP等属性，可以创建一个网格组件。

参考[示例](ndk-access-the-arkts-page.md#示例)中列表组件的实现方式，将网格组件常用的属性设置封装到自定义的ArkUIGridNode类中方便后续使用。

```
1. #ifndef MYAPPLICATION_ARKUIGRIDNODE_H
2. #define MYAPPLICATION_ARKUIGRIDNODE_H

4. #include "ArkUINode.h"
5. #include "ArkUINodeAdapter.h"

7. namespace NativeModule {
8. class ArkUIGridNode : public ArkUINode {
9. public:
10. ArkUIGridNode() : ArkUINode((NativeModuleInstance::GetInstance()->GetNativeNodeAPI())->createNode(ARKUI_NODE_GRID))
11. {
12. }

14. ~ArkUIGridNode() override {}

16. void SetColumnsTemplate(const std::string &str)
17. {
18. ArkUI_AttributeItem item = {.string = str.c_str()};
19. nativeModule_->setAttribute(handle_, NODE_GRID_COLUMN_TEMPLATE, &item);
20. }

22. void SetRowsTemplate(const std::string &str)
23. {
24. ArkUI_AttributeItem item = {.string = str.c_str()};
25. nativeModule_->setAttribute(handle_, NODE_GRID_ROW_TEMPLATE, &item);
26. }

28. void SetColumnsGap(float val)
29. {
30. ArkUI_NumberValue value[] = {{.f32 = val}};
31. ArkUI_AttributeItem item = {value, 1};
32. nativeModule_->setAttribute(handle_, NODE_GRID_COLUMN_GAP, &item);
33. }

35. void SetRowsGap(float val)
36. {
37. ArkUI_NumberValue value[] = {{.f32 = val}};
38. ArkUI_AttributeItem item = {value, 1};
39. nativeModule_->setAttribute(handle_, NODE_GRID_ROW_GAP, &item);
40. }

42. void SetLayoutOptions(ArkUI_GridLayoutOptions *option)
43. {
44. if (option == nullptr) {
45. return;
46. }
47. ArkUI_AttributeItem item = {.object = option};
48. nativeModule_->setAttribute(handle_, NODE_GRID_LAYOUT_OPTIONS, &item);
49. }

51. void SetScrollBar(int32_t barState)
52. {
53. ArkUI_NumberValue value[] = {{.i32 = barState}};
54. ArkUI_AttributeItem item = {value, 1};
55. nativeModule_->setAttribute(handle_, NODE_SCROLL_BAR_DISPLAY_MODE, &item);
56. }

58. void SetLazyAdapter(const std::shared_ptr<ArkUINodeAdapter> &adapter)
59. {
60. if (!IsNotNull(adapter)) {
61. return;
62. }
63. ArkUI_AttributeItem item{nullptr, 0, nullptr, adapter->GetAdapter()};
64. nativeModule_->setAttribute(handle_, NODE_GRID_NODE_ADAPTER, &item);
65. _adapter = adapter;
66. }

68. void ReleaseAdapter() { return _adapter.reset(); }

70. private:
71. std::shared_ptr<ArkUINodeAdapter> _adapter;
72. };
73. } // namespace NativeModule

75. #endif // MYAPPLICATION_ARKUIGRIDNODE_H
```

[ArkUIGridNode.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NDKGridSample/entry/src/main/cpp/ArkUIGridNode.h#L16-L93)

使用ArkUIGridNode创建一个6行4列的网格组件并设置行列间距的代码如下。

```
1. auto grid = std::make_shared<ArkUIGridNode>();
2. grid->SetPercentWidth(0.9f);
3. grid->SetHeight(SIX_ROWS * ITEM_HEIGHT + (SIX_ROWS - 1) * ROWS_GAP);
4. grid->SetColumnsTemplate("1fr 1fr 1fr 1fr");
5. grid->SetRowsTemplate("1fr 1fr 1fr 1fr 1fr 1fr");
6. grid->SetColumnsGap(10.0f);
7. grid->SetRowsGap(ROWS_GAP);
```

[GridRectByIndexExample.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NDKGridSample/entry/src/main/cpp/GridRectByIndexExample.cpp#L64-L72)

其中NODE\_GRID\_COLUMN\_TEMPLATE和NODE\_GRID\_ROW\_TEMPLATE支持多种形式定义列数和行数，以列数设置为例：

```
1. // 使用fr单位（fraction，比例）
2. grid->SetColumnsTemplate("1fr 2fr 1fr");  // 第二列宽度是第一、三列的2倍

4. // 使用repeat函数
5. grid->SetColumnsTemplate("repeat(auto-fill, 100vp)");  // 自动填充100vp宽的列
```

更多形式可以参考[columnsTemplate](../harmonyos-references/ts-container-grid.md#columnstemplate)。

## 设置子组件所占行列数

网格组件默认所有子组件都占1行1列，这类场景通过列表组件设置[ArkUI\_NodeAttributeType](../harmonyos-references/capi-native-node-h.md#arkui_nodeattributetype)中的NODE\_LIST\_LANES也可以实现。网格布局更适合用于部分子组件占用多行或多列的场景，如页面上大小不同的卡片和图标、按日期分组显示图片等。从API version 22开始，这类场景可以通过创建网格时传入合适的[ArkUI\_GridLayoutOptions](../harmonyos-references/capi-arkui-nativemodule-arkui-gridlayoutoptions.md)实现。

### 布局选项对比

| 需求场景 | 推荐方法 | 说明 |
| --- | --- | --- |
| 固定行列网格，部分项占多行多列 | [OH\_ArkUI\_GridLayoutOptions\_RegisterGetRectByIndexCallback](../harmonyos-references/capi-native-type-h.md#oh_arkui_gridlayoutoptions_registergetirregularsizebyindexcallback) | 灵活控制每个项的位置和大小。 |
| 可滚动网格，分组标题占整行 | [OH\_ArkUI\_GridLayoutOptions\_SetIrregularIndexes](../harmonyos-references/capi-native-type-h.md#oh_arkui_gridlayoutoptions_setirregularindexes) | 指定索引占整行。 |

### 设置固定行列场景下子组件的位置和大小

如下图在前面创建的6行\*4列的网格布局中放置了一些子组件，其中“0”占据2行4列，“1”占据2行2列，“2”占据1行2列，0和1之间有一行空行，模拟页面放置不同大小卡片和图标的场景。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/h1XJ9UELRAmos5llblj9fA/zh-cn_image_0000002552798416.png?HW-CC-KV=V1&HW-CC-Date=20260427T234015Z&HW-CC-Expire=86400&HW-CC-Sign=D285B6A14F513D03F8203C478311D7179A5C86B823EC2A1D31F8BC21158D6FD1)

通过[OH\_ArkUI\_GridLayoutOptions\_RegisterGetRectByIndexCallback](../harmonyos-references/capi-native-type-h.md#oh_arkui_gridlayoutoptions_registergetirregularsizebyindexcallback)给网格组件设置用于获取每一个子组件位置的回调函数，开发者可以在该回调中指定每一个子组件所在的起始行号、起始列号、占用行数和占用列数，即[ArkUI\_GridItemRect](../harmonyos-references/capi-arkui-nativemodule-arkui-griditemrect.md)。上图布局可以通过如下代码实现。

“0”从网格左上角开始占据2行4列，需要将其对应的ArkUI\_GridItemRect设置为{0, 0, 2, 4}。其他子组件的位置和大小设置以此类推。

```
1. auto option = std::make_shared<ArkuiGridLayoutOptions>();
2. auto layoutOptions = option->GetLayoutOptions();
3. OH_ArkUI_GridLayoutOptions_RegisterGetRectByIndexCallback(
4. option->GetLayoutOptions(), nullptr, [](int32_t itemIndex, void *userData) -> ArkUI_GridItemRect {
5. switch (itemIndex) {
6. case 0:
7. return ArkUI_GridItemRect{0, 0, 2, 4};
8. case 1:
9. return ArkUI_GridItemRect{3, 0, 2, 2};
10. case ITEM_INDEX_2:
11. return ArkUI_GridItemRect{3, 2, 1, 2};
12. case ITEM_INDEX_3:
13. return ArkUI_GridItemRect{4, 2, 1, 1};
14. case ITEM_INDEX_4:
15. return ArkUI_GridItemRect{4, 3, 1, 1};
16. case ITEM_INDEX_5:
17. return ArkUI_GridItemRect{5, 0, 1, 1};
18. case ITEM_INDEX_6:
19. return ArkUI_GridItemRect{5, 1, 1, 1};
20. case ITEM_INDEX_7:
21. return ArkUI_GridItemRect{5, 2, 1, 1};
22. default:
23. return ArkUI_GridItemRect{5, 3, 1, 1};
24. }
25. });
26. grid->SetLayoutOptions(layoutOptions);
```

[GridRectByIndexExample.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NDKGridSample/entry/src/main/cpp/GridRectByIndexExample.cpp#L78-L105)

### 设置滚动场景下数据分组显示

如下图模拟了分组展示图片或文件的场景，其中作为分组名称的子组件占据一整行，其他子组件占据1行1列。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/qPct5IqLQd62Fb4P9CfIOg/zh-cn_image_0000002583438111.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234015Z&HW-CC-Expire=86400&HW-CC-Sign=C489F89E9D16A77221EFFC14938E5EABD35DF950895E821006F190D542088B5E)

纵向滚动的网格布局，只需要设置列数，无需设置行数。

```
1. grid->SetColumnsTemplate("1fr 1fr 1fr");
2. grid->SetColumnsGap(10.0f);
3. grid->SetRowsGap(10.0f);
4. grid->SetScrollBar(ARKUI_SCROLL_BAR_DISPLAY_MODE_OFF);
```

[GridIrregularIndexesExample.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NDKGridSample/entry/src/main/cpp/GridIrregularIndexesExample.cpp#L42-L47)

分组显示数据，可以通过[OH\_ArkUI\_GridLayoutOptions\_SetIrregularIndexes](../harmonyos-references/capi-native-type-h.md#oh_arkui_gridlayoutoptions_setirregularindexes)设置分组节点对应的index，这些index对应的子组件将占据一整行，其他子组件将占据1行1列。

```
1. auto layoutOptions = std::make_shared<ArkuiGridLayoutOptions>();
2. uint32_t irregularIndexes[] = {0, 6, 8, 15};
3. OH_ArkUI_GridLayoutOptions_SetIrregularIndexes(layoutOptions->GetLayoutOptions(), irregularIndexes,
4. sizeof(irregularIndexes) / sizeof(irregularIndexes[0]));
5. grid->SetLayoutOptions(layoutOptions->GetLayoutOptions());
```

[GridIrregularIndexesExample.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NDKGridSample/entry/src/main/cpp/GridIrregularIndexesExample.cpp#L124-L130)

网格组件支持使用[NodeAdapter](../harmonyos-references/capi-arkui-nativemodule-arkui-nodeadapter8h.md)按需生成子组件以提升性能。详情请参阅[NodeAdapter介绍](ndk-loading-long-list.md#nodeadapter介绍)和[分组显示数据完整示例](https://gitcode.com/openharmony/applications_app_samples/blob/master/code/DocsSample/ArkUISample/NDKGridSample/entry/src/main/cpp/GridIrregularIndexesExample.cpp)。

## 处理滚动事件

### 监听滚动事件监听

参考[监听组件事件](ndk-listen-to-component-events.md)中列表组件[ArkUI\_NodeEventType](../harmonyos-references/capi-native-node-h.md#arkui_nodeeventtype)中的NODE\_LIST\_ON\_SCROLL\_INDEX事件监听示例代码，可以实现网格滚动事件监听。

网格组件支持以下滚动事件：

| 事件枚举 | 事件说明 | API起始版本 |
| --- | --- | --- |
| NODE\_SCROLL\_EVENT\_ON\_SCROLL\_FRAME\_BEGIN | 网格组件开始时回调当前帧将要滑动的偏移量、当前滑动状态。 | 12 |
| NODE\_SCROLL\_EVENT\_ON\_SCROLL\_START | 网格组件滑动开始回调。 | 22 |
| NODE\_SCROLL\_EVENT\_ON\_SCROLL\_STOP | 网格组件滑动停止回调。 | 22 |
| NODE\_SCROLL\_EVENT\_ON\_REACH\_START | 网格组件到达起始位置回调。 | 12 |
| NODE\_SCROLL\_EVENT\_ON\_REACH\_END | 网格组件到达末尾位置回调。 | 12 |
| NODE\_SCROLL\_EVENT\_ON\_WILL\_STOP\_DRAGGING | 网格组件拖划即将离手回调。 | 20 |
| NODE\_SCROLL\_EVENT\_ON\_WILL\_START\_DRAGGING | 网格组件拖划结束回调。 | 21 |
| NODE\_SCROLL\_EVENT\_ON\_DID\_STOP\_DRAGGING | 网格组件拖划结束回调。 | 21 |
| NODE\_SCROLL\_EVENT\_ON\_WILL\_START\_FLING | 网格组件滑动动画即将开始回调。 | 21 |
| NODE\_SCROLL\_EVENT\_ON\_DID\_STOP\_FLING | 网格组件滑动动画结束回调。 | 21 |
| NODE\_GRID\_ON\_SCROLL\_INDEX | 有子组件滑入或滑出网格显示区域时回调显示区域起始和终止位置子组件的索引值。 | 22 |
| NODE\_GRID\_ON\_WILL\_SCROLL | 网格组件滑动前回调当前帧将要滑动的偏移量、当前滑动状态、滑动操作来源。 | 22 |
| NODE\_GRID\_ON\_DID\_SCROLL | 网格组件滑动后回调当前帧滑动的偏移量和当前滑动状态。 | 22 |
| NODE\_GRID\_ON\_SCROLL\_BAR\_UPDATE | 每帧布局结束时设置滚动条的位置及长度。 | 22 |

### 控制滚动位置

参考[控制列表滚动位置](ndk-loading-long-list.md#控制列表滚动位置)设置[ArkUI\_NodeAttributeType](../harmonyos-references/capi-native-node-h.md#arkui_nodeattributetype)中的NODE\_SCROLL\_OFFSET、NODE\_GRID\_SCROLL\_TO\_INDEX可以控制网格组件滚动位置。

从API version 23开始，新增支持NODE\_GRID\_SCROLL\_TO\_INDEX。

## 完整示例

[使用网格](https://gitcode.com/openharmony/applications_app_samples/blob/master/code/DocsSample/ArkUISample/NDKGridSample)
