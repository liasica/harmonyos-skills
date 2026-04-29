---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-radio-button
title: 单选框 (Radio)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 按钮与选择 > 单选框 (Radio)
category: harmonyos-guides
scraped_at: 2026-04-29T13:27:51+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:14c6a90d1830a6e1a021c9f57c1c755de8f7ed731adcaef94a2525126511dd7f
---

Radio是单选框组件，通常用于提供相应的用户交互选择项，同一组的Radio中只有一个可以被选中。具体用法请参考[Radio](../harmonyos-references/ts-basic-components-radio.md)。

## 创建单选框

Radio通过调用[RadioOptions](../harmonyos-references/ts-basic-components-radio.md#radiooptions对象说明)来创建，以RadioOptions中的value和group为例：

```
1. Radio(options: {value: string, group: string})
```

其中，value是单选框的名称，group是单选框的所属群组名称。checked属性可以设置单选框的状态，状态分别为false和true，设置为true时表示单选框被选中。

Radio支持设置选中状态和非选中状态的样式。

```
1. Radio({ value: 'Radio1', group: 'radioGroup' })
2. .checked(false)
3. Radio({ value: 'Radio2', group: 'radioGroup' })
4. .checked(true)
```

[RadioButton.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ChooseComponent/entry/src/main/ets/pages/radio/RadioButton.ets#L34-L39)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/GchjfInxSkS6eFFFhPD7Lg/zh-cn_image_0000002558604718.png?HW-CC-KV=V1&HW-CC-Date=20260429T052750Z&HW-CC-Expire=86400&HW-CC-Sign=944787ABC751860325450047696BB86D04B3C7F69F2E8F05DC26A7D8DA53D8BF)

## 添加事件

除支持[通用事件](../harmonyos-references/ts-component-general-events.md)外，Radio还用于选中后触发某些操作，可以绑定onChange事件来响应选中操作后的自定义行为。

```
1. Radio({ value: 'Radio1', group: 'radioGroup' })
2. .onChange((isChecked: boolean) => {
3. if(isChecked) {
4. //需要执行的操作
5. // ···
6. }
7. })
8. Radio({ value: 'Radio2', group: 'radioGroup' })
9. .onChange((isChecked: boolean) => {
10. if(isChecked) {
11. //需要执行的操作
12. // ···
13. }
14. })
```

[RadioButton.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ChooseComponent/entry/src/main/ets/pages/radio/RadioButton.ets#L47-L66)

## 场景示例

通过点击Radio切换声音模式。

```
1. // xxx.ets
2. import { promptAction } from '@kit.ArkUI';

4. @Entry
5. @Component
6. export struct RadioExample {
7. @State rst: promptAction.ShowToastOptions = { 'message': 'Ringing mode.' };
8. @State vst: promptAction.ShowToastOptions = { 'message': 'Vibration mode.' };
9. @State sst: promptAction.ShowToastOptions = { 'message': 'Silent mode.' };

11. build() {
12. // ···
13. Row() {
14. Column() {
15. Radio({ value: 'Ringing', group: 'radioGroup' }).checked(true)
16. .height(50)
17. .width(50)
18. .onChange((isChecked: boolean) => {
19. if (isChecked) {
20. // 切换为响铃模式
21. this.getUIContext().getPromptAction().openToast(this.rst);
22. }
23. })
24. Text('Ringing')
25. }

27. Column() {
28. Radio({ value: 'Vibration', group: 'radioGroup' })
29. .height(50)
30. .width(50)
31. .onChange((isChecked: boolean) => {
32. if (isChecked) {
33. // 切换为振动模式
34. this.getUIContext().getPromptAction().openToast(this.vst);
35. }
36. })
37. Text('Vibration')
38. }

40. Column() {
41. Radio({ value: 'Silent', group: 'radioGroup' })
42. .height(50)
43. .width(50)
44. .onChange((isChecked: boolean) => {
45. if (isChecked) {
46. // 切换为静音模式
47. this.getUIContext().getPromptAction().openToast(this.sst);
48. }
49. })
50. Text('Silent')
51. }
52. }.height('100%').width('100%').justifyContent(FlexAlign.Center)
53. // ···
54. }
55. }
```

[RadioSample.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ChooseComponent/entry/src/main/ets/pages/radio/RadioSample.ets#L16-L76)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/-d591WanSLOise_uAzwEvA/zh-cn_image_0000002589324243.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052750Z&HW-CC-Expire=86400&HW-CC-Sign=50C33DDFBDD1122BF80920D97F933A1DA344A4C9F337EF8AAE53721A37FD5456)
