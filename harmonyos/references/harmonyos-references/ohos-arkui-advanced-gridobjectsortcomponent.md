---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-gridobjectsortcomponent
title: GridObjectSortComponent
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 系统预置UI组件库 > GridObjectSortComponent
category: harmonyos-references
scraped_at: 2026-04-29T13:53:01+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:417e9157b4adcb64f8e6ffdcd0a90cdbe0df654bb338e6ec4117610852c5e150
---

网格对象排序组件，用于网格对象的编辑、拖动排序、新增和删除。

说明

* 该组件从API version 11开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 该组件仅可在Stage模型下使用。
* 如果GridObjectSortComponent设置[通用属性](ts-component-general-attributes.md)和[通用事件](ts-component-general-events.md)，编译工具链会额外生成节点\_\_Common\_\_，并将通用属性或通用事件挂载在\_\_Common\_\_上，而不是直接应用到GridObjectSortComponent本身。这可能导致开发者设置的通用属性或通用事件不生效或不符合预期，因此，不建议GridObjectSortComponent设置通用属性和通用事件。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { GridObjectSortComponent, GridObjectSortComponentItem, GridObjectSortComponentOptions, GridObjectSortComponentType , SymbolGlyphModifier } from '@kit.ArkUI';
```

## 子组件

PhonePC/2in1TabletTVWearable

无

## GridObjectSortComponent

PhonePC/2in1TabletTVWearable

GridObjectSortComponent({options: GridObjectSortComponentOptions, dataList: Array<GridObjectSortComponentItem>, onSave: (select: Array<GridObjectSortComponentItem>, unselect: Array<GridObjectSortComponentItem>) => void, onCancel: () => void })

网格对象排序组件。

**装饰器类型：**@Component

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| options | [GridObjectSortComponentOptions](ohos-arkui-advanced-gridobjectsortcomponent.md#gridobjectsortcomponentoptions) | 是 | @Prop | 组件配置信息。 |
| dataList | Array<[GridObjectSortComponentItem](ohos-arkui-advanced-gridobjectsortcomponent.md#gridobjectsortcomponentitem)> | 是 | - | 传入的数据，最大长度为50，数据长度超过50，只会取前50的数据。 |
| onSave | (select: Array<[GridObjectSortComponentItem](ohos-arkui-advanced-gridobjectsortcomponent.md#gridobjectsortcomponentitem)>, unselect: Array<[GridObjectSortComponentItem](ohos-arkui-advanced-gridobjectsortcomponent.md#gridobjectsortcomponentitem)>) => void | 是 | - | 保存编辑排序的回调函数，返回编辑后的数据。 |
| onCancel | () => void | 是 | - | 取消保存数据的回调。 |

## GridObjectSortComponentOptions

PhonePC/2in1TabletTVWearable

网格对象排序组件的组件配置信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [GridObjectSortComponentType](ohos-arkui-advanced-gridobjectsortcomponent.md#gridobjectsortcomponenttype) | 否 | 是 | 组件展示形态：文字|图片+文字。  默认值：GridObjectSortComponentType.TEXT |
| imageSize | number | [Resource](ts-types.md#resource) | 否 | 是 | 图片的尺寸，单位vp。  取值范围：大于等于0。  默认值：56vp |
| normalTitle | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 未编辑状态下显示的标题。  默认值：频道。 |
| showAreaTitle | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 展示区域标题，第一个子标题。  默认值：长按拖动排序。 |
| addAreaTitle | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 添加区域标题，第二个子标题。  默认值：点击添加。 |
| editTitle | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 编辑状态下头部标题显示。  默认值：编辑。 |

## GridObjectSortComponentType

PhonePC/2in1TabletTVWearable

配置网格对象排序组件节点的类型，配置名称 IMAGE\_TEXT 为图片文字类型，TEXT 为文字类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| IMAGE\_TEXT | "image\_text" | 图片文字类型。 |
| TEXT | "text" | 文字类型。 |

## GridObjectSortComponentItem

PhonePC/2in1TabletTVWearable

网格对象排序组件的组件数据配置信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | number | string | 否 | 否 | 数据id序号，不可重复。  默认值：空字符串。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| text | [ResourceStr](ts-types.md#resourcestr) | 否 | 否 | 显示文本信息。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| selected | boolean | 否 | 否 | 是否已经被添加，已添加：true，未添加：false。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| url | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | GridObjectSortComponentType类型为IMAGE\_TEXT时，需要传入图片地址。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| symbolStyle18+ | [SymbolGlyphModifier](universal-attributes-attribute-symbolglyphmodifier.md#symbolglyphmodifier) | 否 | 是 | GridObjectSortComponentType类型为IMAGE\_TEXT时，需要传入Symbol图标资源。配置优先级高于url。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| order | number | 否 | 否 | 顺序序号。  取值范围：大于等于0。  默认值：0  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

## 事件

PhonePC/2in1TabletTVWearable

不支持[通用事件](ts-component-general-events.md)。

## 示例

PhonePC/2in1TabletTVWearable

网格对象的编辑排序组件基础用法，涉及对组件配置信息初始化，数据初始化，保存、取消方法的使用。

```
1. import { GridObjectSortComponent, GridObjectSortComponentItem, GridObjectSortComponentOptions, GridObjectSortComponentType, SymbolGlyphModifier } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. // 组件数据初始化。
7. @State dataList: GridObjectSortComponentItem[] = [
8. {
9. id: 0,
10. url: $r('sys.media.ohos_save_button_filled'),
11. text: '下载',
12. selected: true,
13. order: 3
14. },
15. {
16. id: 1,
17. url: $r('sys.media.ohos_ic_public_web'),
18. text: '网络',
19. selected: true,
20. order: 9
21. },
22. {
23. id: 2,
24. url: $r('sys.media.ohos_ic_public_video'),
25. text: '视频',
26. selected: false,
27. order: 1
28. },
29. {
30. id: 3,
31. symbolStyle: new SymbolGlyphModifier($r('sys.symbol.record_circle')),
32. text: '录制',
33. selected: false,
34. order: 4
35. }
36. ]

38. // 组件配置信息初始化。
39. @State option: GridObjectSortComponentOptions = {
40. type: GridObjectSortComponentType.IMAGE_TEXT,
41. imageSize: 45,
42. normalTitle: '菜单',
43. editTitle: '编辑',
44. showAreaTitle: '长按拖动排序',
45. addAreaTitle: '点击添加'
46. }

48. build() {
49. Column() {
50. GridObjectSortComponent({
51. options: this.option,
52. dataList: this.dataList,
53. // 保存编辑排序的回调函数，返回编辑后的数据。
54. onSave: (
55. select: Array<GridObjectSortComponentItem>,
56. unselect: Array<GridObjectSortComponentItem>
57. ) => {
58. // save ToDo
59. },
60. // 取消保存数据的回调。
61. onCancel: () =>{
62. // cancel ToDo
63. }
64. })
65. }
66. }
67. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/wjk1hlYWR7q11Vmb4jj3SQ/zh-cn_image_0000002589326511.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055300Z&HW-CC-Expire=86400&HW-CC-Sign=59569EAD9DBAD76C33823302F81721EBC5D250A66E609CBAE6FCBE63E3005BF8)
