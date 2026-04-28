---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-switch
title: 切换按钮 (Toggle)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 按钮与选择 > 切换按钮 (Toggle)
category: harmonyos-guides
scraped_at: 2026-04-28T07:39:41+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:65214c829e8830aea4a8f50c63204dbc402c865ea0d146ba818c19a25a1808bd
---

Toggle组件提供状态按钮样式、勾选框样式和开关样式，一般用于两种状态之间的切换。具体用法请参考[Toggle](../harmonyos-references/ts-basic-components-toggle.md)。

## 创建切换按钮

Toggle通过调用[ToggleOptions](../harmonyos-references/ts-basic-components-toggle.md#toggleoptions18对象说明)来创建，具体调用形式如下：

```
1. Toggle(options: { type: ToggleType, isOn?: boolean })
```

其中，ToggleType为开关类型，包括Button、Checkbox和Switch，isOn为切换按钮的状态。

API version 11开始，Checkbox默认样式由圆角方形变为圆形。

接口调用有以下两种形式：

* 创建不包含子组件的Toggle。

  当ToggleType为Checkbox或者Switch时，用于创建不包含子组件的Toggle：

  ```
  1. Toggle({ type: ToggleType.Checkbox, isOn: false }).id('toggle1') // 请开发者替换为实际的id
  2. Toggle({ type: ToggleType.Checkbox, isOn: true }).id('toggle2') // 请开发者替换为实际的id
  ```

  [CreateToggle.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ChooseComponent/entry/src/main/ets/pages/toggle/CreateToggle.ets#L30-L33)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/N8guUNkXR56jCv8S4bfkgA/zh-cn_image_0000002583477885.png?HW-CC-KV=V1&HW-CC-Date=20260427T233939Z&HW-CC-Expire=86400&HW-CC-Sign=6F4537BA8CADEB67C12E50BF5AFE543F29EDAE102BBE38D942FE3AE21950D342)

  ```
  1. Toggle({ type: ToggleType.Switch, isOn: false }).id('toggle3') // 请开发者替换为实际的id
  2. Toggle({ type: ToggleType.Switch, isOn: true }).id('toggle4') // 请开发者替换为实际的id
  ```

  [CreateToggle.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ChooseComponent/entry/src/main/ets/pages/toggle/CreateToggle.ets#L39-L42)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/C5CoHyeaTJWQRkXMYMxK2A/zh-cn_image_0000002552798236.png?HW-CC-KV=V1&HW-CC-Date=20260427T233939Z&HW-CC-Expire=86400&HW-CC-Sign=DE0B58800001BAC3E8E5CAC64C57C9D1834C9EC11A9A905B64D07A91AD3943F3)
* 创建包含子组件的Toggle。

  当ToggleType为Button时，只能包含一个子组件，如果子组件有文本设置，则相应的文本内容会显示在按钮上。

  ```
  1. Toggle({ type: ToggleType.Button, isOn: false }) {
  2. Text('status button')
  3. .fontColor('#182431')
  4. .fontSize(12)
  5. }.width(100).id('toggle5') // 请开发者替换为实际的id

  7. Toggle({ type: ToggleType.Button, isOn: true }) {
  8. Text('status button')
  9. .fontColor('#182431')
  10. .fontSize(12)
  11. }.width(100).id('toggle6') // 请开发者替换为实际的id
  ```

  [CreateToggle.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ChooseComponent/entry/src/main/ets/pages/toggle/CreateToggle.ets#L61-L73)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/p8sOMMG_T7WUm7b0ektbYQ/zh-cn_image_0000002583437931.png?HW-CC-KV=V1&HW-CC-Date=20260427T233939Z&HW-CC-Expire=86400&HW-CC-Sign=FA658B546D9FE7621B3EE68D56EEB2459CF9635BEB6E2BA9DB5B128068EAA016)

## 自定义样式

* 通过selectedColor属性设置Toggle打开选中后的背景颜色。

  ```
  1. Toggle({ type: ToggleType.Button, isOn: true }) {
  2. Text('status button')
  3. .fontColor('#182431')
  4. .fontSize(12)
  5. }.width(100)
  6. .selectedColor(Color.Pink)
  7. // ···

  9. Toggle({ type: ToggleType.Checkbox, isOn: true })
  10. .selectedColor(Color.Pink)
  11. // ···
  12. Toggle({ type: ToggleType.Switch, isOn: true })
  13. .selectedColor(Color.Pink)
  14. // ···
  ```

  [ToggleCustomStyle.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ChooseComponent/entry/src/main/ets/pages/toggle/ToggleCustomStyle.ets#L31-L52)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/wbxVMqgtThqFW20g3qylZQ/zh-cn_image_0000002552957886.png?HW-CC-KV=V1&HW-CC-Date=20260427T233939Z&HW-CC-Expire=86400&HW-CC-Sign=710FFA7F20D5A813CDB593DACBD6460B17F51D753C83317994EAFA1397536FC0)
* 通过switchPointColor属性设置Switch类型的圆形滑块颜色，仅对type为ToggleType.Switch生效。

  ```
  1. Toggle({ type: ToggleType.Switch, isOn: false })
  2. .switchPointColor(Color.Pink)
  3. // ···
  4. Toggle({ type: ToggleType.Switch, isOn: true })
  5. .switchPointColor(Color.Pink)
  6. // ···
  ```

  [ToggleCustomStyle.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ChooseComponent/entry/src/main/ets/pages/toggle/ToggleCustomStyle.ets#L60-L71)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/2jKL_Ji_QKevQQCSZK5Lfw/zh-cn_image_0000002583477887.png?HW-CC-KV=V1&HW-CC-Date=20260427T233939Z&HW-CC-Expire=86400&HW-CC-Sign=7289DEFEAB78D94BBA4CB1BA9C60D16AFB74F5D1C627D9A70B214859762E50F7)

## 添加事件

除支持[通用事件](../harmonyos-references/ts-component-general-events.md)外，Toggle还用于选中和取消选中后触发某些操作，可以绑定onChange事件来响应操作后的自定义行为。

```
1. Toggle({ type: ToggleType.Switch, isOn: false })
2. .onChange((isOn: boolean) => {
3. if(isOn) {
4. // 需要执行的操作
5. // ···
6. }
7. })
```

[CreateToggle.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ChooseComponent/entry/src/main/ets/pages/toggle/CreateToggle.ets#L44-L54)

## 场景示例

Toggle用于切换蓝牙开关状态。

```
1. // xxx.ets
2. import { promptAction } from '@kit.ArkUI';

4. @Entry
5. @Component
6. export struct ToggleSample {
7. @State message: string = 'off';
8. pathStack: NavPathStack = new NavPathStack();

10. build() {
11. NavDestination() {
12. Column({ space: 8 }) {
13. Column({ space: 8 }) {
14. Text('Bluetooth Mode: ' + this.message)
15. .id('message')
16. Row() {
17. Text('Bluetooth')
18. Blank()
19. Toggle({ type: ToggleType.Switch })
20. .id('toggle') // 请开发者替换为实际的id
21. .onChange((isOn: boolean) => {
22. if (isOn) {
23. this.message = 'on';
24. promptAction.openToast({ 'message': 'Bluetooth is on.' });
25. } else {
26. this.message = 'off';
27. promptAction.openToast({ 'message': 'Bluetooth is off.' });
28. }
29. })
30. }.width('100%')
31. }
32. .alignItems(HorizontalAlign.Start)
33. .backgroundColor('#fff')
34. .borderRadius(12)
35. .padding(12)
36. .width('100%')
37. }
38. .width('100%')
39. .height('100%')
40. .padding({ left: 12, right: 12 })
41. }
42. .backgroundColor('#f1f2f3')
43. // 请将$r('app.string.ToggleCaseExample_title')替换为实际资源文件，在本示例中该资源文件的value值为"toggle蓝牙示例"
44. .title($r('app.string.ToggleCaseExample_title'))
45. }
46. }
```

[ToggleCaseExample.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ChooseComponent/entry/src/main/ets/pages/toggle/ToggleCaseExample.ets#L16-L69)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/-MMz484KTxKeaj-rXO3D1A/zh-cn_image_0000002552798238.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233939Z&HW-CC-Expire=86400&HW-CC-Sign=12C57D008CDB948F2E44DDABBBD2844B81CC97C9062759FB82E97A17F753DF50)
