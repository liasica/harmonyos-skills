---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkui-support-for-aging-adaptation
title: 支持适老化
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 无障碍与适老化 > 支持适老化
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:07+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:f96a0f5a39bbca74663bb7ff5890f563a95f6aebbde68d22a83cd86c2e5bda99
---

系统字体被放大后，应用应确保整体布局不出现错乱，组件不出现重叠。可以根据业务需要限制跟随的字体最大档位、改变布局来更好的适配更大字体等。本文旨在指导应用如何跟随系统字体大小和跟随到的最大倍数。

## 应用适配规则

* 在系统使用1.75倍及以上的大字体时，页面布局不得错乱，组件不得叠加，文字不得截断。
* 图标及图片不会随着字体的变大而变化。
* 页面中不重要的内容字体，可采用不跟随系统字体变化或限制字体最大尺寸的方法进行布局。
* 若应用跟随系统字体增大后导致页面内容位置挤压或截断等问题，可采取将X轴扩展至Y轴的措施，例如将左右布局调整为上下布局。
* [系统组件](arkui-support-for-aging-adaptation.md#适配适老化的系统组件及触发方式)已针对适老化大字体进行了单独适配，尽可能在开发过程中使用系统组件。

## 应用适配适老化大字体

1. 开启路径

   在“设置-辅助功能-关怀模式-放大显示”中开启。

   各档位对应参数：

   | 档位 | 字体大小 | 字体粗细 |
   | --- | --- | --- |
   | 标准 | 1倍 | 1倍 |
   | 大1档 | 1.15倍 | 1倍 |
   | 大2档 | 1.3倍 | 1.1倍 |
   | 大3档 | 1.45倍 | 1.1倍 |
   | 大4档 | 1.75倍 | 1.25倍 |
   | 大5档 | 2.0倍 | 1.25倍 |
   | 大6档 | 3.2倍 | 1.25倍 |
2. 适配方法

   当前默认应用不跟随系统字体的变化。如需跟随系统字体变化，并设置最大跟随变化的倍数，请按以下步骤操作：

   * [app.json5配置文件](app-configuration-file.md)适配。

     通过配置"configuration": "$profile:configuration"，指向base/profile/configuration.json文件；

     ```
     1. {
     2. "app": {
     3. "bundleName": "com.example.myapplication",
     4. "vendor": "example",
     5. "versionCode": 1000000,
     6. "versionName": "1.0.0",
     7. "icon": "$media:app_icon",
     8. "label": "$string:app_name",
     9. "configuration": "$profile:configuration"
     10. }
     11. }
     ```
   * 在base文件目录下新增profile文件夹，并在此目录下新增 configuration.json 文件。

     配置"fontSizeScale": "followSystem"表示该应用的字体大小将根据系统设置进行缩放，"fontSizeMaxScale": "1.3"表示应用字体大小随系统变化的最大缩放比例为1.3倍。

     ```
     1. {
     2. "configuration": {
     3. "fontSizeScale": "followSystem",
     4. "fontSizeMaxScale": "1.3"
     5. }
     6. }
     ```
   * 若应用需适应系统字体大小的变化，最大应调整至1.75倍，但部分组件可调整至2倍。

     首先需要按照上述步骤配置"fontSizeMaxScale"为1.75。

     ```
     1. {
     2. "configuration": {
     3. "fontSizeScale": "followSystem",
     4. "fontSizeMaxScale": "1.75"
     5. }
     6. }
     ```

     然后，为Text添加maxFontScale属性，传递参数为2，表示该Text组件跟随系统字体大小变化的最大倍数为2倍。

     ```
     1. Text('hello world!')
     2. .fontSize($r('sys.float.Body_M'))
     3. .maxFontScale(2)
     4. .fontColor($r('sys.color.font_secondary'))
     ```

     当Text组件配置了maxFontScale属性时，将采用组件设置的最大放大倍数，而非系统默认的最大放大倍数。
   * 若应用不需要跟随系统字体大小变化，无需配置。
3. 获取字体大小和粗细。

   * 生命周期回调方法[onConfigurationUpdated](../harmonyos-references/js-apis-app-ability-environmentcallback.md#onconfigurationupdated)的config参数可接收字体大小（[fontSizeScale](../harmonyos-references/js-apis-app-ability-configuration.md#configuration)）与字体粗细（[fontWeightScale](../harmonyos-references/js-apis-app-ability-configuration.md#configuration)）。

     注册系统环境变化的监听后，在系统环境变化时可触发回调。
   * 应用冷启动查询系统字体大小档位。

     ```
     1. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
     2. let fontSizeScale: number = context.config?.fontSizeScale ?? 1;
     ```

## 适配适老化的系统组件及触发方式

适老化提供了一种通过鼠标或手指长按的方法来放大所选区域或组件，即如果系统字体大小大于1倍，当用户使用鼠标或手指长按装配了适老化方法的组件，需要从所选区域的组件中提取数据，并放入另一个弹窗组件中展示。该方法的目的在于使组件和组件内部数据（子组件）放大，同时将整体组件在屏幕中央显示，让用户能够更好的观察该组件。

* 适老化规则

  由于在系统字体大于1倍时，组件并没有默认放大，需要通过配置[configuration标签](app-configuration-file.md#configuration标签)，实现组件放大的适老化功能。
* 如何开启适老化

  进入手机设置，点击辅助功能，开启关怀模式。
* 适老化操作

  在已经支持适老化能力的组件上长按组件，能够触发弹窗，当用户释放时，适老化操作结束。当设置系统字体大于1倍时，组件自动放大，当系统字体恢复至1倍时组件恢复正常状态。
* 适老化对象

  触发适老化操作并提供数据的组件。
* 适老化弹窗目标

  可接收并处理适老化数据的组件。
* 弹窗限制

  当用户将系统字体设置为2倍以上时，弹窗内容包括icon和文字的放大倍数固定为2倍。
* 联合其他能力

  适老化能力可以适配其他能力（如：滑动拖拽）。底部页签（tabBar）组件在触发适老化时，如果用户滑动手指或鼠标可以触发底部页签其他子组件的适老化功能。

| 触发方式 | 组件名称 |
| --- | --- |
| 长按系统组件触发 | [SideBarContainer](../harmonyos-references/ts-container-sidebarcontainer.md)， [底部页签（tabBar）](../harmonyos-references/ts-container-tabcontent.md#tabbar9)，[Navigation](../harmonyos-references/ts-basic-components-navigation.md)，[NavDestination](../harmonyos-references/ts-basic-components-navigation.md#navdestination10)， [Tabs](../harmonyos-references/ts-container-tabs.md) |
| 设置系统字体默认放大 | [PickerDialog](../harmonyos-references/ts-methods-calendarpicker-dialog.md)， [Button](../harmonyos-references/ts-basic-components-button.md)， [Menu](../harmonyos-references/ts-basic-components-menu.md)， [Stepper](../harmonyos-references/ts-basic-components-stepper.md)， [BindSheet](../harmonyos-references/ts-universal-attributes-sheet-transition.md#bindsheet)，[TextInput](../harmonyos-references/ts-basic-components-textinput.md)，[TextArea](../harmonyos-references/ts-basic-components-textarea.md)，[Search](../harmonyos-references/ts-basic-components-search.md)，[SelectionMenu](../harmonyos-references/ohos-arkui-advanced-selectionmenu.md)，[Chip](../harmonyos-references/ohos-arkui-advanced-chip.md)，[Dialog](../harmonyos-references/ohos-arkui-advanced-dialog.md)，[Slider](../harmonyos-references/ts-basic-components-slider.md)， [Progress](../harmonyos-references/ts-basic-components-progress.md)， [Badge](../harmonyos-references/ts-container-badge.md) |

SideBarContainer组件通过长按控制按钮触发适老化弹窗。在系统字体为1倍的情况下，长按控制按钮不能弹窗。在系统字体大于1倍的情况下，长按控制按钮可以弹窗。

```
1. @Entry
2. @Component
3. struct SideBarContainerExample {
4. @State currentFontSizeScale: number = 1
5. normalIcon: Resource = $r("app.media.icon")
6. selectedIcon: Resource = $r("app.media.icon")
7. @State arr: number[] = [1, 2, 3]
8. @State current: number = 1
9. @State title: string = 'Index01';

11. build() {
12. SideBarContainer(SideBarContainerType.Embed) {
13. Column() {
14. ForEach(this.arr, (item: number) => {
15. Column({ space: 5 }) {
16. Image(this.current === item ? this.selectedIcon : this.normalIcon).width(64).height(64)
17. Text("0" + item)
18. .fontSize(25)
19. .fontColor(this.current === item ? '#0A59F7' : '#999')
20. .fontFamily('source-sans-pro,cursive,sans-serif')
21. }
22. .onClick(() => {
23. this.current = item;
24. this.title = "Index0" + item;
25. })
26. }, (item: string) => item)
27. }.width('100%')
28. .justifyContent(FlexAlign.SpaceEvenly)
29. .backgroundColor($r('sys.color.mask_fifth'))
30. }
31. .controlButton({
32. icons: {
33. hidden: $r('sys.media.ohos_ic_public_drawer_open_filled'),
34. shown: $r('sys.media.ohos_ic_public_drawer_close')
35. }
36. })
37. .sideBarWidth(150)
38. .minSideBarWidth(50)
39. .maxSideBarWidth(300)
40. .minContentWidth(0)
41. .onChange((value: boolean) => {
42. console.info('status:' + value)
43. })
44. .divider({ strokeWidth: '1vp', color: Color.Gray, startMargin: '4vp', endMargin: '4vp' })
45. }
46. }
```

切换系统字体前后长按已经支持适老化能力的组件，有如下效果：

| 系统字体为一倍（适老化能力开启前） | 系统字体为1.75倍（适老化能力开启后） |
| --- | --- |
|  |  |

[TextPickerDialog](../harmonyos-references/ts-methods-textpicker-dialog.md)组件通过设置系统字体大小触发适老化弹窗。在系统字体为1倍的情况下，适老化不触发；在系统字体大于1倍的情况下，适老化触发。

```
1. @Entry
2. @Component
3. struct TextPickerExample {
4. private select: number | number[] = 0;
5. private cascade: TextCascadePickerRangeContent[] = [
6. {
7. text: '辽宁省',
8. children: [{ text: '沈阳市', children: [{ text: '沈河区' }, { text: '和平区' }, { text: '浑南区' }] },
9. { text: '大连市', children: [{ text: '中山区' }, { text: '金州区' }, { text: '长海县' }] }]
10. },
11. {
12. text: '吉林省',
13. children: [{ text: '长春市', children: [{ text: '南关区' }, { text: '宽城区' }, { text: '朝阳区' }] },
14. { text: '四平市', children: [{ text: '铁西区' }, { text: '铁东区' }, { text: '梨树县' }] }]
15. },
16. {
17. text: '黑龙江省',
18. children: [{ text: '哈尔滨市', children: [{ text: '道里区' }, { text: '道外区' }, { text: '南岗区' }] },
19. { text: '牡丹江市', children: [{ text: '东安区' }, { text: '西安区' }, { text: '爱民区' }] }]
20. }
21. ]
22. @State v: string = '';
23. @State showTriggered: string = '';
24. private triggered: string = '';
25. private maxLines: number = 3;

27. linesNum(max: number): void {
28. let items: string[] = this.triggered.split('').filter(item => item != '');
29. if (items.length > max) {
30. this.showTriggered = items.slice(-this.maxLines).join('');
31. } else {
32. this.showTriggered = this.triggered;
33. }
34. }

36. build() {
37. Column() {
38. Button("TextPickerDialog.show:" + this.v)
39. .onClick(() => {
40. TextPickerDialog.show({
41. range: this.cascade,
42. selected: this.select,
43. onAccept: (value: TextPickerResult) => {
44. this.select = value.index
45. console.log(this.select + '')
46. this.v = value.value as string
47. console.info("TextPickerDialog:onAccept()" + JSON.stringify(value))
48. if (this.triggered != '') {
49. this.triggered += `onAccept(${JSON.stringify(value)})`;
50. } else {
51. this.triggered = `onAccept(${JSON.stringify(value)})`;
52. }
53. this.linesNum(this.maxLines);
54. },
55. onCancel: () => {
56. console.info("TextPickerDialog:onCancel()")
57. if (this.triggered != '') {
58. this.triggered += `onCancel()`;
59. } else {
60. this.triggered = `onCancel()`;
61. }
62. this.linesNum(this.maxLines);
63. },
64. onChange: (value: TextPickerResult) => {
65. console.info("TextPickerDialog:onChange()" + JSON.stringify(value))
66. if (this.triggered != '') {
67. this.triggered += `onChange(${JSON.stringify(value)})`;
68. } else {
69. this.triggered = `onChange(${JSON.stringify(value)})`;
70. }
71. this.linesNum(this.maxLines);
72. },
73. })
74. })
75. .margin({ top: 60 })
76. }
77. }
78. }
```

| 系统字体为一倍（适老化能力开启前） | 系统字体为1.75倍（适老化能力开启后） |
| --- | --- |
|  |  |
