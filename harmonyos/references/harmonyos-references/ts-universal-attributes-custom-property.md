---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-custom-property
title: 自定义属性设置
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 动态属性与自定义 > 自定义属性设置
category: harmonyos-references
scraped_at: 2026-04-28T08:01:17+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:e00e495ace91f03980707dcd404a1e4eeb68b5f2c7faa374de6b5eee21175fe1
---

当开发者希望在组件上设置自定义的属性时，可以使用自定义属性设置功能。这些自定义属性可以在其对应的FrameNode上获取，从而实现更自由的组件管理。

说明

从API version 12开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## customProperty

PhonePC/2in1TabletTVWearable

customProperty(name: string, value: Optional<Object>): T

设置组件的自定义属性。[自定义组件](../harmonyos-guides/arkts-create-custom-components.md)不支持设置自定义属性。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 自定义属性的名称。 |
| value | [Optional](ts-universal-attributes-custom-property.md#optionalt)<Object> | 是 | 自定义属性的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## Optional<T>

PhonePC/2in1TabletTVWearable

type Optional<T> = T | undefined

定义可选类型，其值可以是undefined。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

| 类型 | 说明 |
| --- | --- |
| T | 表示该类型声明的对象是自定义类型。 |
| undefined | 表示该类型声明的对象是undefined。 |

## 示例

PhonePC/2in1TabletTVWearable

在[Column](ts-container-column.md)组件上设置自定义属性，并在其对应的[FrameNode](js-apis-arkui-framenode.md#framenode-1)上获取所设置的自定义属性。

```
1. // xxx.ets
2. import { FrameNode, UIContext } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct CustomPropertyExample {
7. build() {
8. Column() {
9. Text('text')
10. Button('print').onClick(() => {
11. // 获取Column对应的frameNode节点并查询设置的自定义属性
12. const uiContext: UIContext = this.getUIContext();
13. if (uiContext) {
14. const node: FrameNode | null = uiContext.getFrameNodeById("Test_Column") || null;
15. if (node) {
16. for (let i = 1; i < 4; i++) {
17. const key = 'customProperty' + i;
18. const property = node.getCustomProperty(key);
19. console.info(key, JSON.stringify(property));
20. }
21. }
22. }
23. })
24. }
25. .id('Test_Column')
26. // 设置Column组件的自定义属性
27. .customProperty('customProperty1', {
28. 'number': 10,
29. 'string': 'this is a string',
30. 'bool': true,
31. 'object': {
32. 'name': 'name',
33. 'value': 100
34. }
35. })
36. .customProperty('customProperty2', {})
37. .customProperty('customProperty3', undefined)
38. .width('100%')
39. .height('100%')
40. }
41. }
```
