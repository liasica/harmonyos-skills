---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-switch
title: 切换按钮 (Toggle)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 按钮与选择 > 切换按钮 (Toggle)
category: harmonyos-guides
scraped_at: 2026-04-29T13:27:51+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:309f9f0d48479de6869974e16d9a8ae028c9050fc3855975dbaac7391405a99f
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/yPBszsovQxOhX2UftGTg3w/zh-cn_image_0000002589244183.png?HW-CC-KV=V1&HW-CC-Date=20260429T052750Z&HW-CC-Expire=86400&HW-CC-Sign=FD653784113B301E8D503CB3934AC01E207DD6DF24121EA0A2AC0BA2A47DC90C)

  ```
  1. Toggle({ type: ToggleType.Switch, isOn: false }).id('toggle3') // 请开发者替换为实际的id
  2. Toggle({ type: ToggleType.Switch, isOn: true }).id('toggle4') // 请开发者替换为实际的id
  ```

  [CreateToggle.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ChooseComponent/entry/src/main/ets/pages/toggle/CreateToggle.ets#L39-L42)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/LhL7s_eJTvurJsiEE6MdUg/zh-cn_image_0000002558764376.png?HW-CC-KV=V1&HW-CC-Date=20260429T052750Z&HW-CC-Expire=86400&HW-CC-Sign=705D23270DE413E05DACD8835296647714976C417C896E424D6261FAE7D84727)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/l0269XtpRh2g_tgjtcvzvg/zh-cn_image_0000002558604720.png?HW-CC-KV=V1&HW-CC-Date=20260429T052750Z&HW-CC-Expire=86400&HW-CC-Sign=6477D8E8DF1F2586AAE5D45B3E3B6EC0A216817CD4BB8B59A2868C132989745A)

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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/1qJjudpcT7uGIbuIlAyxjg/zh-cn_image_0000002589324245.png?HW-CC-KV=V1&HW-CC-Date=20260429T052750Z&HW-CC-Expire=86400&HW-CC-Sign=3A763FA7C570AB015B98EB36FEEA8789DEA08CE9DC1964FA12D9C138C900290B)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/FQgqcDnzTEmZ0O5zcScJaQ/zh-cn_image_0000002589244185.png?HW-CC-KV=V1&HW-CC-Date=20260429T052750Z&HW-CC-Expire=86400&HW-CC-Sign=7B9F8383E025C05F02F11910114E62791B3D3B10AD1F223D8AB8D22E3E017B59)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/CMJ5cdRrSguuWHz1rUeB7g/zh-cn_image_0000002558764378.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052750Z&HW-CC-Expire=86400&HW-CC-Sign=74D7EF1A6905E74000068D7D2D70576EEA4195A36A660505CFC350D18DE94AB3)
