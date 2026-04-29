---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-popup-and-menu-components-menu
title: 菜单控制（Menu）
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用弹窗 > 菜单 > 菜单控制（Menu）
category: harmonyos-guides
scraped_at: 2026-04-29T13:27:56+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9e5439b4e5ea3dd0f4cbc613b187ecb718c3f2f8b1d947c3982972efafef0a7e
---

Menu是菜单接口，一般用于鼠标右键弹窗、点击弹窗等。具体用法请参考[菜单控制](../harmonyos-references/ts-universal-attributes-menu.md)。

使用[bindContextMenu](../harmonyos-references/ts-universal-attributes-menu.md#bindcontextmenu12)并设置预览图，菜单弹出时有蒙层，此时为模态。

使用[bindMenu](../harmonyos-references/ts-universal-attributes-menu.md#bindmenu11)或bindContextMenu未设置预览图时，菜单弹出无蒙层，此时为非模态。

## 创建默认样式的菜单

菜单需要调用[bindMenu](../harmonyos-references/ts-universal-attributes-menu.md#bindmenu)接口来实现。bindMenu响应绑定组件的点击事件，绑定组件后手势点击对应组件后即可弹出。

```
1. Button('click for Menu')
2. .bindMenu([
3. {
4. value: 'Menu1',
5. action: () => {
6. hilog.info(0xFF00, 'DialogProject', 'handle Menu1 select');
7. }
8. }
9. ])
```

[CreateDefaultMenu.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/Menu/CreateDefaultMenu.ets#L25-L35)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/YTH5PsDPSGuFy6l1-qak7g/zh-cn_image_0000002589324273.png?HW-CC-KV=V1&HW-CC-Date=20260429T052755Z&HW-CC-Expire=86400&HW-CC-Sign=2D61A13DB72FA4E06BEF3A8044CE90F277BB7028D1F60D73D0925D6EF54B597B)

## 创建自定义样式的菜单

当默认样式不满足开发需求时，可使用[@Builder](arkts-builder.md)自定义菜单内容，通过bindMenu接口进行菜单的自定义。

### 使用@Builder自定义菜单内容

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. class Tmp {
4. // 请将$r('app.media.view_list_filled')替换为实际资源文件
5. public iconStr2: ResourceStr = $r('app.media.view_list_filled');

7. set(val: Resource) {
8. this.iconStr2 = val;
9. }
10. }

12. @Entry
13. @Component
14. export struct BuilderCustomMenuExample {
15. @State select: boolean = true;
16. // 请将$r('app.media.view_list_filled')替换为实际资源文件
17. private iconStr: ResourceStr = $r('app.media.view_list_filled');
18. private iconStr2: ResourceStr = $r('app.media.view_list_filled');
19. // 请将$r('app.string.copy')替换为实际资源文件，在本示例中该资源文件的value值为"复制"
20. private copy: ResourceStr = $r('app.string.copy');
21. // 请将$r('app.string.paste')替换为实际资源文件，在本示例中该资源文件的value值为"粘贴"
22. private paste: ResourceStr = $r('app.string.paste');

24. @Builder
25. SubMenu() {
26. Menu() {
27. MenuItem({ content: this.copy, labelInfo: 'Ctrl+C' })
28. MenuItem({ content: this.paste, labelInfo: 'Ctrl+V' })
29. }
30. }

32. @Builder
33. MyMenu() {
34. Menu() {
35. // 请将$r('app.string.menu_selection')替换为实际资源文件，在本示例中该资源文件的value值为"菜单选项"
36. // 请将$r('app.media.icon')替换为实际资源文件
37. // 请将$r('app.media.arrow_right_filled')替换为实际资源文件
38. MenuItem({ startIcon: $r('app.media.icon'), content: $r('app.string.menu_selection') })
39. MenuItem({ startIcon: $r('app.media.icon'), content: $r('app.string.menu_selection') }).enabled(false)
40. MenuItem({
41. startIcon: this.iconStr,
42. content: $r('app.string.menu_selection'),
43. endIcon: $r('app.media.arrow_right_filled'),
44. // 当builder参数进行配置时，表示与menuItem项绑定了子菜单。鼠标hover在该菜单项时，会显示子菜单。
45. builder: this.SubMenu
46. })
47. // 请将$r('app.string.menu_subtitle')替换为实际资源文件，在本示例中该资源文件的value值为"小标题"
48. MenuItemGroup({ header: $r('app.string.menu_subtitle') }) {
49. // 请将$r('app.string.menu_selection')替换为实际资源文件，在本示例中该资源文件的value值为"菜单选项"
50. MenuItem({ content: $r('app.string.menu_selection') })
51. .selectIcon(true)
52. .selected(this.select)
53. .onChange((selected) => {
54. hilog.info(0xFF00, 'DialogProject', 'menuItem select' + selected);
55. let str: Tmp = new Tmp();
56. str.set($r('app.media.icon'));
57. })
58. // 请将$r('app.string.menu_selection')替换为实际资源文件，在本示例中该资源文件的value值为"菜单选项"
59. // 请将$r('app.media.view_list_filled')替换为实际资源文件
60. // 请将$r('app.media.arrow_right_filled')替换为实际资源文件
61. MenuItem({
62. startIcon: $r('app.media.view_list_filled'),
63. content: $r('app.string.menu_selection'),
64. endIcon: $r('app.media.arrow_right_filled'),
65. builder: this.SubMenu
66. })
67. }

69. // 请将$r('app.string.menu_selection')替换为实际资源文件，在本示例中该资源文件的value值为"菜单选项"
70. // 请将$r('app.media.arrow_right_filled')替换为实际资源文件
71. MenuItem({
72. startIcon: this.iconStr2,
73. content: $r('app.string.menu_selection'),
74. endIcon: $r('app.media.arrow_right_filled')
75. })
76. }
77. }

79. build() {
80. // ...
81. }
82. }
```

[BuilderCustomMenu.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/Menu/BuilderCustomMenu.ets#L16-L114)

### 使用bindMenu属性绑定组件

```
1. Button('click for Menu')
2. .bindMenu(this.MyMenu)
```

[BuilderCustomMenu.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/Menu/BuilderCustomMenu.ets#L99-L102)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/WhOLLrr-Ro-0Dqg9aUNWdA/zh-cn_image_0000002589244213.png?HW-CC-KV=V1&HW-CC-Date=20260429T052755Z&HW-CC-Expire=86400&HW-CC-Sign=60D08ADE25BE6B6DBFA39EBF044A7F94759B6A32D6FDB138774CFE1AB216D6CB)

## 创建支持右键或长按的菜单

通过[bindContextMenu](../harmonyos-references/ts-universal-attributes-menu.md#bindcontextmenu8)接口自定义菜单，设置菜单弹出的触发方式，触发方式为右键或长按。使用bindContextMenu弹出的菜单项是在独立子窗口内的，可显示在应用窗口外部。

* 使用@Builder自定义菜单内容，与上文写法相同。
* 确认菜单的弹出方式，并使用bindContextMenu属性绑定组件。示例中为右键弹出菜单。

  ```
  1. Button('Right-click for Menu')
  2. .bindContextMenu(this.MyMenu, ResponseType.RightClick)
  ```

  [CreateMenu.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/Menu/CreateMenu.ets#L122-L125)

## 菜单弹出时振动效果

菜单从API version 18开始支持振动效果。菜单弹出时，默认不振动。若希望菜单弹出时有振动效果，可以通过[ContextMenuOptions](../harmonyos-references/ts-universal-attributes-menu.md#contextmenuoptions10)的hapticFeedbackMode属性，设置菜单弹出时的振动模式。

* 只有一级菜单可配置弹出时振动效果。
* 仅当应用具备ohos.permission.VIBRATE权限，且用户启用了触感反馈时才会生效。开启触控反馈时，需要在工程的module.json5中配置[声明权限](declare-permissions.md)的requestPermissions字段开启振动权限，配置如下：

  ```
  1. "requestPermissions": [
  2. {
  3. "name": "ohos.permission.VIBRATE",
  4. }
  5. ],
  ```

  [module.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/module.json5#L64-L70)

```
1. Button('click for Menu')
2. .id('click for Menu')
3. .bindMenu(this.MyMenu, { hapticFeedbackMode: HapticFeedbackMode.ENABLED})
```

[PopVibrateMenu.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/Menu/PopVibrateMenu.ets#L96-L100)

## 菜单支持避让中轴

从API version 18起，菜单支持中轴避让功能。从API version 20开始，在2in1设备上默认启用（仅在窗口处于瀑布模式时产生避让）。开发者可通过[ContextMenuOptions](../harmonyos-references/ts-universal-attributes-menu.md#contextmenuoptions10)中的enableHoverMode属性，控制菜单是否启用中轴避让。

说明

* 如果菜单的点击位置在中轴区域，则菜单不会避让。
* 2in1设备上需同时满足窗口处于瀑布模式才会产生避让。

```
1. @Entry
2. @Component
3. export struct SupportAvoidCentralAxisMenuExample {
4. @State message: string = 'Hello World';
5. // 请在resources\base\element\string.json文件中配置name为'xxx'，value为非空字符串的资源
6. @State upScreen: string =
7. this.getUIContext().getHostContext()?.resourceManager.getStringByNameSync('Upper_half_screen') as string;
8. @State middleAxle: string =
9. this.getUIContext().getHostContext()?.resourceManager.getStringByNameSync('Middle_axle') as string;
10. @State lowerScreen: string =
11. this.getUIContext().getHostContext()?.resourceManager.getStringByNameSync('Lower_half_screen') as string;
12. @State zone: string =
13. this.getUIContext().getHostContext()?.resourceManager.getStringByNameSync('zone') as string;
14. @State hoverModeStart: string =
15. this.getUIContext().getHostContext()?.resourceManager.getStringByNameSync('hoverMode_start') as string;
16. // 请将$r('app.media.startIcon')替换为实际资源文件
17. private iconStr: Resource = $r('app.media.startIcon');
18. @State index: number = 0;
19. @State arrayStr: Array<string> = [this.upScreen, this.middleAxle, this.lowerScreen];
20. @State enableHoverMode: boolean | undefined = true;
21. @State showInSubwindow: boolean = false;

23. @Builder
24. MyMenu1() {
25. Menu() {
26. // 请将$r('app.string.menu_selection')替换为实际资源文件，在本示例中该资源文件的value值为"菜单选项"
27. MenuItem({ startIcon: this.iconStr, content: $r('app.string.menu_selection') })
28. MenuItem({ startIcon: this.iconStr, content: $r('app.string.menu_selection') })
29. MenuItem({ startIcon: this.iconStr, content: $r('app.string.menu_selection') })
30. MenuItem({ startIcon: this.iconStr, content: $r('app.string.menu_selection') })
31. }
32. }

34. @State isShow: boolean = false;

36. build() {
37. NavDestination() {
38. Column({ space: 5 }) {
39. Button(this.zone + this.arrayStr[this.index])
40. .onClick(() => {
41. if (this.index < 2) {
42. this.index++
43. } else {
44. this.index = 0
45. }
46. })

48. Button(this.hoverModeStart + this.enableHoverMode)
49. .id('hoverMode_start')
50. .onClick(() => {
51. if (this.enableHoverMode === undefined) {
52. this.enableHoverMode = true
53. } else if (this.enableHoverMode === true) {
54. this.enableHoverMode = false
55. } else {
56. this.enableHoverMode = undefined
57. }
58. })
59. Button('Menu')
60. .fontWeight(FontWeight.Bold)
61. .bindMenu(this.MyMenu1(), {
62. enableHoverMode: this.enableHoverMode,
63. showInSubWindow: this.showInSubwindow
64. })
65. }
66. .height('100%')
67. .width('100%')
68. }
69. // ...
70. }
71. }
```

[SupportAvoidCentralAxisMenu.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/Menu/SupportAvoidCentralAxisMenu.ets#L16-L93)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/fF-3Ax1zQw-1jjgqfvLCfA/zh-cn_image_0000002558764406.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052755Z&HW-CC-Expire=86400&HW-CC-Sign=49EF7207D6119465629209605919AE10A40A242C5CBEDE3C2804365D234A7A04)

## 控制子窗菜单的事件透传

当菜单在子窗口中弹出时，默认情况下，菜单周围的事件会传递至所在窗口。从API version 20开始，开发者可通过[ContextMenuOptions](../harmonyos-references/ts-universal-attributes-menu.md#contextmenuoptions10)的modalMode属性设置子菜单弹出时的模态模式，以控制菜单周围事件是否传递。将modalMode设置为ModalMode.TARGET\_WINDOW时，菜单周围的事件将不再传递，菜单下方的控件也不会响应事件。

```
1. @Entry
2. @Component
3. export struct EventTransSubWindowMenuExample {
4. build() {
5. NavDestination() {
6. Column() {
7. }
8. .id('click')
9. .bindContextMenu(this.contextMenuBuilder, ResponseType.RightClick, {
10. modalMode: ModalMode.TARGET_WINDOW
11. })
12. .onClick(() => {
13. this.getUIContext().getPromptAction().showToast({
14. message: 'Clicked!'
15. })
16. })
17. .width('100%')
18. .height('100%')
19. }
20. // ...
21. }

23. @Builder
24. bindMenuBuilder() {
25. Menu() {
26. MenuItem({ content: 'bindMenu item' }) {

28. }
29. }
30. }

32. @Builder
33. contextMenuBuilder() {
34. Menu() {
35. MenuItem({ content: 'contextMenu item' }) {

37. }
38. }
39. }
40. }
```

[EventTransSubWindowMenu.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/Menu/EventTransSubWindowMenu.ets#L15-L59)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/jo567o9fQaOEfVH65cREyA/zh-cn_image_0000002558604750.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052755Z&HW-CC-Expire=86400&HW-CC-Sign=79E76EE8A468B9609B46C51720F74347D55C696FC98BC71AFF540243C6C6E941)

## 基于绑定组件指定位置弹出菜单

菜单从API version 20开始支持基于绑定组件在指定位置弹出。通过设置水平与垂直偏移量，控制菜单相对于绑定组件左上角的弹出位置。与单独使用offset接口不同，此方法可使菜单覆盖显示在绑定组件上。需要指定弹出位置时，可使用[ContextMenuOptions](../harmonyos-references/ts-universal-attributes-menu.md#contextmenuoptions10)的anchorPosition属性进行设置。

说明

* 当菜单处于预览状态时，设定的定位偏移量将无法生效。
* 预设的[placement](../harmonyos-references/ts-universal-attributes-menu.md#contextmenuoptions10)对齐参数将不再生效。
* 叠加[offset](../harmonyos-references/ts-universal-attributes-menu.md#contextmenuoptions10)参数的偏移量，最终确定菜单的精确显示位置。
* 当水平与垂直偏移量均设为负值时，菜单以绑定组件左下角为基准点进行显示。
* 当水平或垂直偏移量存在负值时，组件将以绑定组件的左上角为定位基准点，通过叠加偏移量参数实现反向偏移。

```
1. @Entry
2. @Component
3. export struct BindComponentMenuExample {
4. @Builder
5. MenuBuilder() {
6. Column() {
7. Menu() {
8. MenuItemGroup() {
9. // 请将$r('app.media.app_icon')替换为实际资源文件
10. MenuItem({ startIcon: $r('app.media.app_icon'), content: 'Select Mixed Menu 1', labelInfo: '' })
11. MenuItem({ startIcon: $r('app.media.app_icon'), content: 'Select Mixed Menu 2', labelInfo: '' })
12. MenuItem({ startIcon: $r('app.media.app_icon'), content: 'Select Mixed Menu 3', labelInfo: '' })
13. }
14. }
15. }
16. }

18. build() {
19. NavDestination() {
20. Column() {
21. Text()
22. .borderRadius(10)
23. .width(200)
24. .height(150)
25. .borderWidth(1)
26. .backgroundColor(Color.White)
27. .borderColor(Color.Red)
28. .margin({ top: 200, left: 125 })
29. .bindContextMenu(this.MenuBuilder, ResponseType.RightClick, {
30. anchorPosition: { x: 45, y: 50 },
31. })
32. }
33. .alignItems(HorizontalAlign.Start)
34. .width('100%')
35. .height('100%')
36. .backgroundColor('#F5F5F5')
37. }
38. // ...
39. }
40. }
```

[BindComponentMenu.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/Menu/BindComponentMenu.ets#L15-L59)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/W4jAcmFHQoqmFpYBNjQ6vw/zh-cn_image_0000002589324275.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052755Z&HW-CC-Expire=86400&HW-CC-Sign=48888F860DBC307717735ED53759ED95445A8AF68DF5D29AB75EF46EAF84497D)
