---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inputmethodlist
title: @ohos.inputMethodList (输入法切换列表控件)
breadcrumb: API参考 > 应用框架 > IME Kit（输入法开发服务） > ArkTS API > @ohos.inputMethodList (输入法切换列表控件)
category: harmonyos-references
scraped_at: 2026-04-28T08:06:09+08:00
doc_updated_at: 2026-04-10
content_hash: sha256:f3b1c22c596377d206c95e9a091a54c7b5f1eb41257fcfc0c023b18fe76af229
---

本模块主要面向系统应用和输入法应用，提供输入法切换列表控件，控件中显示默认输入法子类型和三方输入法应用列表，对于默认输入法应用，提供模式切换入口。

说明

该组件从API version 11开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { InputMethodListDialog } from '@kit.IMEKit';
```

## 子组件

PhonePC/2in1TabletTVWearable

无

## 属性

PhonePC/2in1TabletTVWearable

不支持[通用属性](ts-component-general-attributes.md)

## InputMethodListDialog

PhonePC/2in1TabletTVWearable

InputMethodListDialog({controller: CustomDialogController, patternOptions?: PatternOptions})

输入法切换列表弹窗。

**装饰器类型：**@CustomDialog

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| controller | [CustomDialogController](ts-methods-custom-dialog-box.md#customdialogcontroller) | 是 | - | 输入法切换列表弹窗控制器。 |
| patternOptions | [PatternOptions](js-apis-inputmethodlist.md#patternoptions) | 否 | - | 输入法模式选项（仅系统预置输入法支持）。 |

## PatternOptions

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| defaultSelected | number | 否 | 是 | 非必填。默认选择的模式。 |
| patterns | Array<[Pattern](js-apis-inputmethodlist.md#pattern)> | 否 | 否 | 必填。模式选项的资源。 |
| action | (index: number) => void | 否 | 否 | 必填。模式选项改变时的回调。 |

## Pattern

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| icon | [Resource](ts-types.md#resource) | 否 | 否 | 必填。默认图片资源。 |
| selectedIcon | [Resource](ts-types.md#resource) | 否 | 否 | 必填。选中时的图片资源。 |

## 事件

PhonePC/2in1TabletTVWearable

不支持[通用事件](ts-component-general-events.md)

## 示例

PhonePC/2in1TabletTVWearable

```
1. import { Pattern, PatternOptions } from '@kit.IMEKit';

3. @Entry
4. // 设置组件
5. @Component
6. struct SettingsItem {
7. @State defaultPattern: number = 1;
8. private oneHandAction: PatternOptions = {
9. defaultSelected: this.defaultPattern,
10. patterns: [ // patterns中的图标需要在工程的resource中添加对应图标资源后使用
11. {
12. icon: $r('app.media.hand_icon'), // 此处为输入法模式选项的图标资源，例如单手模式图标
13. selectedIcon: $r('app.media.hand_icon_selected') // 此处为输入法模式选项的图标资源选中状态，例如单手模式选中状态的图标
14. },
15. {
16. icon: $r('app.media.hand_icon1'),
17. selectedIcon: $r('app.media.hand_icon_selected1')
18. },
19. {
20. icon: $r('app.media.hand_icon2'),
21. selectedIcon: $r('app.media.hand_icon_selected2'),
22. }],
23. action:(index: number)=>{
24. console.info(`pattern is changed, current is ${index}`);
25. this.defaultPattern = index;
26. }
27. };
28. private listController: CustomDialogController = new CustomDialogController({
29. builder: InputMethodListDialog({ patternOptions: this.oneHandAction }),
30. customStyle: true,
31. maskColor: '#00000000'
32. });

34. build() {
35. Column() {
36. Flex({ direction: FlexDirection.Column,
37. alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
38. Text("输入法切换列表").fontSize(20)
39. }
40. }
41. .width("13%")
42. .id('bindInputMethod')
43. .onClick((event?: ClickEvent) => {
44. this.listController.open();
45. })
46. }
47. }
```

示例效果图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/iXakntR6RfqgNHqTec6GHg/zh-cn_image_0000002583480517.png?HW-CC-KV=V1&HW-CC-Date=20260428T000606Z&HW-CC-Expire=86400&HW-CC-Sign=95A16AF213649238EFC107D5E605F1F998FA8646F9AB170B30A571E2771C14CC)
