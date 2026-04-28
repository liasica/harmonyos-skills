---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-on-touch-intercept
title: 自定义事件拦截
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用事件 > 交互事件分发控制 > 自定义事件拦截
category: harmonyos-references
scraped_at: 2026-04-28T08:00:56+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:9e1ad789075279e5d7c0841ec6e3b3010ac6d966a970f051cc4c9c39d2841c29
---

为组件提供自定义的事件拦截能力，开发者可根据事件在控件上按下时的位置，输入源等事件信息决定控件上的HitTestMode属性。

说明

从API version 12开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## onTouchIntercept

PhonePC/2in1TabletTVWearable

onTouchIntercept(callback: Callback<TouchEvent, HitTestMode>): T

给组件绑定自定义事件拦截回调。

说明

从API version 20开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[TouchEvent](ts-universal-events-touch.md#touchevent对象说明), [HitTestMode](ts-appendix-enums.md#hittestmode9)> | 是 | 自定义事件拦截回调。在做[触摸测试](../harmonyos-guides/arkts-interaction-basic-principles.md#触摸测试)时回调此函数。通过返回值设置组件的[触摸测试类型](ts-universal-attributes-hit-test-behavior.md)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## 示例

PhonePC/2in1TabletTVWearable

该示例通过onTouchIntercept修改组件的HitTestMode属性。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Index {
5. isPolygon(event: TouchEvent) {
6. return true;
7. }

9. build() {
10. Row() {
11. Column() {
12. Text("hello world")
13. .backgroundColor(Color.Blue)
14. .fontSize(50)
15. .fontWeight(FontWeight.Bold)
16. .onClick(() => {
17. console.info("Text click");
18. })
19. }
20. .width(400)
21. .height(300)
22. .backgroundColor(Color.Pink)
23. .onClick(() => {
24. console.info("Column click");
25. })
26. // 调用onTouchIntercept修改该组件的HitTestMode属性
27. .onTouchIntercept((event: TouchEvent) => {
28. console.info("OnTouchIntercept + " + JSON.stringify(event));
29. // 使用touches时需要先校验是否为空
30. if (event && event.touches) {
31. let touches = event.touches;
32. for (let i = 0; touches[i] != null; i++) {
33. console.info('onTouchIntercept touches:', JSON.stringify(touches[i]));
34. }
35. }
36. if (this.isPolygon(event)) {
37. return HitTestMode.None;
38. }
39. return HitTestMode.Default;
40. })
41. }
42. .width('100%')
43. }
44. }
```
