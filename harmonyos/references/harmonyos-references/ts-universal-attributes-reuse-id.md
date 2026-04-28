---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-reuse-id
title: 复用标识
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 其他 > 复用标识
category: harmonyos-references
scraped_at: 2026-04-28T08:01:19+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:078b9f9fd2f164d5c193ec54b0eac38cb69b4ef9f3f5c8ddc81d2c1face558ae
---

reuseId用于标记自定义组件复用组，当组件回收复用时，复用框架将根据组件的reuseId来划分组件的复用组。

说明

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## reuseId

PhonePC/2in1TabletTVWearable

reuseId(id: string): T

复用标识，用于划分自定义组件的复用组。

说明

* 根据不同场景灵活设置reuseId，实现最佳复用效果。最佳实践请参考[组件复用-使用reuseId标记布局发生变化的组件](../best-practices/bpta-component-reuse.md#section1239555818211)。
* 该接口不支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 | 复用标识，用于划分自定义组件的复用组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## 示例

PhonePC/2in1TabletTVWearable

该示例通过reuseId标识自定义组件的复用组。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct MyComponent {
5. @State switch: boolean = true;
6. private type: string = "type1";

8. build() {
9. Column() {
10. Button("ChangeType")
11. .onClick(() => {
12. this.type = "type2"
13. })
14. Button("Switch")
15. .onClick(() => {
16. this.switch = !this.switch
17. })
18. if (this.switch) {
19. ReusableChildComponent({ type: this.type })
20. .reuseId(this.type)
21. }
22. }
23. .width('100%')
24. .height('100%')
25. }
26. }

28. @Reusable
29. @Component
30. struct ReusableChildComponent {
31. @State type: string = ''

33. aboutToAppear() {
34. console.info(`ReusableChildComponent Appear ${this.type}`)
35. }

37. aboutToReuse(params: ESObject) {
38. console.info(`ReusableChildComponent Reuse ${this.type}`)
39. this.type = params.type;
40. }

42. build() {
43. Row() {
44. Text(this.type)
45. .fontSize(20)
46. .margin({ left: 10 })
47. }.margin({ left: 10, right: 10 })
48. }
49. }
```
