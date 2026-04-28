---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-two-way-sync
title: $$语法：系统组件双向同步
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式状态管理 > 语法糖 > $$语法：系统组件双向同步
category: harmonyos-guides
scraped_at: 2026-04-28T07:39:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9ffc7d3645b271c85025ec1e82c936bb12b7de091cf737e7ff7146ad7e694831
---

$$运算符为系统组件提供TS变量的引用，使得TS变量和系统组件的内部状态保持同步。

内部状态的具体含义取决于组件。例如，[TextInput](../harmonyos-references/ts-basic-components-textinput.md)组件的text参数。

## 使用规则

* 当前$$支持基础类型变量，当该变量使用[@State](arkts-state.md)、[@Link](arkts-link.md)、[@Prop](arkts-prop.md)、[@Provide](arkts-provide-and-consume.md)等状态管理V1装饰器装饰，或者[@Local](arkts-new-local.md)等状态管理V2装饰器装饰时，变量值的变化会触发UI刷新。
* 当前$$支持的组件：

  | 组件 | 支持的参数/属性 | 起始API版本 |
  | --- | --- | --- |
  | [Checkbox](../harmonyos-references/ts-basic-components-checkbox.md) | select | 10 |
  | [CheckboxGroup](../harmonyos-references/ts-basic-components-checkboxgroup.md) | selectAll | 10 |
  | [DatePicker](../harmonyos-references/ts-basic-components-datepicker.md) | selected | 10 |
  | [TimePicker](../harmonyos-references/ts-basic-components-timepicker.md) | selected | 10 |
  | [MenuItem](../harmonyos-references/ts-basic-components-menuitem.md) | selected | 10 |
  | [Panel](../harmonyos-references/ts-container-panel.md) | mode | 10 |
  | [Radio](../harmonyos-references/ts-basic-components-radio.md) | checked | 10 |
  | [Rating](../harmonyos-references/ts-basic-components-rating.md) | rating | 10 |
  | [Search](../harmonyos-references/ts-basic-components-search.md) | value | 10 |
  | [SideBarContainer](../harmonyos-references/ts-container-sidebarcontainer.md) | showSideBar | 10 |
  | [Slider](../harmonyos-references/ts-basic-components-slider.md) | value | 10 |
  | [Stepper](../harmonyos-references/ts-basic-components-stepper.md) | index | 10 |
  | [Swiper](../harmonyos-references/ts-container-swiper.md) | index | 10 |
  | [Tabs](../harmonyos-references/ts-container-tabs.md) | index | 10 |
  | [TextArea](../harmonyos-references/ts-basic-components-textarea.md) | text | 10 |
  | [TextInput](../harmonyos-references/ts-basic-components-textinput.md) | text | 10 |
  | [TextPicker](../harmonyos-references/ts-basic-components-textpicker.md) | selected、value | 10 |
  | [Toggle](../harmonyos-references/ts-basic-components-toggle.md) | isOn | 10 |
  | [AlphabetIndexer](../harmonyos-references/ts-container-alphabet-indexer.md) | selected | 10 |
  | [Select](../harmonyos-references/ts-basic-components-select.md) | selected、value | 10 |
  | [BindSheet](../harmonyos-references/ts-universal-attributes-sheet-transition.md#bindsheet) | isShow | 10 |
  | [BindContentCover](../harmonyos-references/ts-universal-attributes-modal-transition.md#bindcontentcover) | isShow | 10 |
  | [Refresh](../harmonyos-references/ts-container-refresh.md) | refreshing | 8 |
  | [GridItem](../harmonyos-references/ts-container-griditem.md) | selected | 10 |
  | [ListItem](../harmonyos-references/ts-container-listitem.md) | selected | 10 |

## 使用示例

以[TextInput](../harmonyos-references/ts-basic-components-textinput.md)方法的text参数为例：

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TextInputExample {
5. @State text: string = '';
6. controller: TextInputController = new TextInputController();

8. build() {
9. Column({ space: 20 }) {
10. Text(this.text)
11. TextInput({ text: $$this.text, placeholder: 'input your word...', controller: this.controller })
12. .placeholderColor(Color.Grey)
13. .placeholderFont({ size: 14, weight: 400 })
14. .caretColor(Color.Blue)
15. .width(300)
16. }
17. .width('100%')
18. .height('100%')
19. .justifyContent(FlexAlign.Center)
20. }
21. }
```

[SyncUsageExample.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/syncStateManager/SyncUsageExample.ets#L30-L52)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/KQi7nbmxS7uMh5mdF0Ca3A/zh-cn_image_0000002552957622.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233912Z&HW-CC-Expire=86400&HW-CC-Sign=EF0BED17019385B584AE3D322B1437360DCDCBF9A6E5AFA559C8A25B3453A3B3)
