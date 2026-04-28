---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-filter
title: Filter
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 系统预置UI组件库 > Filter
category: harmonyos-references
scraped_at: 2026-04-28T08:02:37+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:acced73f4daf70a60bdc78157388f5f78e89a358e4aa0006e382a2cd03820703
---

多条件筛选，帮助用户在大量信息中找到所需内容，应结合具体场景选择合适筛选方式。多条件筛选控件由筛选器与悬浮条构成，悬浮条可下拉展示悬浮筛选器。筛选器样式可分为多行可折叠类型与多行列表类型，并可以在筛选器最后一行附加快捷筛选器。

说明

* 该组件从API version 10开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 该组件仅可在Stage模型下使用。
* 如果Filter设置[通用属性](ts-component-general-attributes.md)和[通用事件](ts-component-general-events.md)，编译工具链会额外生成节点\_\_Common\_\_，并将通用属性或通用事件挂载在\_\_Common\_\_上，而不是直接应用到Filter本身。这可能导致开发者设置的通用属性或通用事件不生效或不符合预期，因此，不建议Filter设置通用属性和通用事件。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { Filter } from '@kit.ArkUI';
```

## 子组件

PhonePC/2in1TabletTVWearable

无

## Filter

PhonePC/2in1TabletTVWearable

Filter({ multiFilters: Array<FilterParams>, additionFilters?: FilterParams, filterType?: FilterType, onFilterChanged: (filterResults: Array<FilterResult>) => void, container: ()=> void })

**装饰器类型：**@Component

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| multiFilters | Array<[FilterParams](ohos-arkui-advanced-filter.md#filterparams)> | 是 | @Prop | 多条件筛选列表。 |
| additionFilters | [FilterParams](ohos-arkui-advanced-filter.md#filterparams) | 否 | @Prop | 附加快捷筛选项。如果不设置，则不显示附加快捷筛选项。 |
| filterType | [FilterType](ohos-arkui-advanced-filter.md#filtertype) | 否 | @Prop | 筛选器的样式类型。  默认值：FilterType.LIST\_FILTER |
| onFilterChanged | (filterResults: Array<[FilterResult](ohos-arkui-advanced-filter.md#filterresult)>) => void | 是 | - | 用户点击后的回调事件。回调函数的参数为选中的筛选项结果列表。 |
| container | ()=>void | 是 | @BuilderParam | 筛选结果展示区域自定义内容，通过尾随闭包形式传入。 |

## FilterParams

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | [ResourceStr](ts-types.md#resourcestr) | 否 | 否 | 筛选项维度名称。  默认值：空字符串。  **说明**：如果文本大于列宽时，文本被截断。 |
| options | Array<[ResourceStr](ts-types.md#resourcestr)> | 否 | 否 | 筛选项维度可选项列表。  默认值：空数组。  **说明**：文本超长显示省略号。 |

## FilterType

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| MULTI\_LINE\_FILTER | 0 | 多行可折叠类型筛选器。 |
| LIST\_FILTER | 1 | 多行列表类型筛选器。 |

## FilterResult

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | [ResourceStr](ts-types.md#resourcestr) | 否 | 否 | 筛选项维度名称。  默认值：空字符串。  **说明**：如果文本大于列宽时，文本被截断。 |
| index | number | 否 | 否 | 该维度筛选项选中项目的索引值。  取值范围：大于等于-1的整数。  默认值：-1，没有选中项。若设置数值小于-1，按没有选中项处理。 |
| value | [ResourceStr](ts-types.md#resourcestr) | 否 | 否 | 该维度筛选项选中项目的值。  默认值：空字符串。  **说明**：如果文本大于列宽时，文本被截断。 |

## 事件

PhonePC/2in1TabletTVWearable

不支持[通用事件](ts-component-general-events.md)。

## 示例

PhonePC/2in1TabletTVWearable

该示例设置FilterType属性为MULTI\_LINE\_FILTER，实现多行可折叠类型筛选器。

```
1. import { Filter, FilterParams, FilterResult, FilterType } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. private filterParam: Array<FilterParams> = [{
7. name: '月份',
8. options: ['全部', '1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月'],
9. },
10. {
11. name: '年份',
12. options: ['全部', '2023', '2022', '2021', '2020', '2019', '2018', '2017', '2016', '2015', '2014', '2013', '2012',
13. '2011', '2010', '2009', '2008'],
14. },
15. {
16. name: '节气',
17. options: ['全部', '立春', '雨水', '惊蛰', '春分', '清明', '谷雨', '立夏', '小满', '芒种', '夏至', '小暑', '大暑',
18. '立秋', '处暑', '白露', '秋分', '寒露', '霜降', '立冬', '小雪', '大雪', '冬至', '小寒', '大寒'],
19. }];
20. // additionFilters筛选行name必传，不可为空，否则整行不显示
21. private additionParam: FilterParams =
22. { name: '您还可以搜', options: ['运营栏目1', '运营栏目2', '运营栏目3', '运营栏目4', '运营栏目5', '运营栏目6'] };
23. private arr: number[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

25. build() {
26. Column() {
27. Filter({
28. multiFilters: this.filterParam,
29. additionFilters: this.additionParam,
30. filterType: FilterType.MULTI_LINE_FILTER,
31. onFilterChanged: (select: Array<FilterResult>) => {
32. console.info('rec filter change');
33. for (let filter of select) {
34. console.info('name:' + filter.name + ',index:' + filter.index + ',value:' + filter.value);
35. }
36. }
37. }) {
38. List({ initialIndex: 0 }) {
39. ForEach(this.arr, (item: string, index: number) => {
40. ListItem() {
41. Text(item.toString())
42. .width('100%')
43. .height(100)
44. .fontSize(16)
45. .textAlign(TextAlign.Center)
46. .borderRadius(10)
47. .backgroundColor(Color.White)
48. .margin({ top: 10, bottom: 10 })
49. }
50. })
51. }.backgroundColor(Color.Gray)
52. .padding({ left: 20, right: 20 })
53. }
54. }
55. .height('100%')
56. .width('100%')
57. }
58. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/g77vxk1eSsOzjVnK06l3zg/zh-cn_image_0000002583480109.png?HW-CC-KV=V1&HW-CC-Date=20260428T000236Z&HW-CC-Expire=86400&HW-CC-Sign=D056E1D8B91FFFCD2E81694AE8721B73D3AB2EF73C167CEF9E9656F010683E16)
