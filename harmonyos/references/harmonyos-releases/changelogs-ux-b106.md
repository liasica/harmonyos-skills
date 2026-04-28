---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/changelogs-ux-b106
title: UX样式或效果的变更
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.1(13) > OS平台能力 > OS平台行为变更说明 > HarmonyOS 5.0.1(13) Beta3引入的行为变更 > UX样式或效果的变更
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:58+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:c4d08d0d0a8cb0bb020a2fcc806773baadd0e9c8bc0f0b617fb4465526f8c929
---

## QRCode深浅色适配修改

**变更原因**

QRCode在深色模式下使用默认颜色生成的二维码无法被正常识别。

**变更影响**

此变更涉及应用适配。

变更前:在深色模式下，QRCode生成的二维码背景颜色为黑色，图案颜色为白色。

变更后:在深色模式下，QRCode生成的二维码背景颜色为白色，图案颜色为黑色，与浅色模式相同。

**起始API Level**

12

**变更的接口/组件**

QRcode组件

**适配指导**

默认效果变更，按需适配。若需反色二维码（背景颜色为黑色，图案颜色为白色），请自定义设置color、backgroundColor实现。

## 属性动画onFinish结束回调在UIAbility退后台时因有限循环动画被终止而提前触发

**变更原因**

属性动画在UIAbility退后台时不会停止而是继续步进，此时动画不显示但持续请求Vsync，造成了不必要的功耗浪费，故而需要变更动画行为。变更为，在UIAbility退后台时，其包含的有限循环动画会立即结束，无限循环动画依旧不结束。

**变更影响**

此变更涉及应用适配。

变更前：onFinish接口在相应属性动画结束时触发回调。动画不感知UIAbility的前后台状态，UIAbility退后台后，动画仍按照所设时长和循环次数步进至完成，并触发结束回调。

变更后：onFinish接口在相应属性动画结束时触发回调。动画感知UIAbility的前后台状态，UIAbility退后台时，如果此时有限循环动画还未结束，该动画会被停止至终点态并触发onFinish结束回调。无限循环动画不受退后台影响，不会停止。

**起始API Level**

7

**变更的接口/组件**

AnimateParam和KeyframeAnimateParam的onFinish接口。

**适配指导**

默认行为变更，应注意变更后的行为是否对整体应用逻辑产生影响。

## TextInput组件在非标准字体场景下showCounter接口布局变更

**变更原因**

在大字体时，showCounter所属的TextInput组件的下侧Margin空间不足。

**变更影响**

此变更涉及应用适配。

变更前：在设置showCounter后，TextInput组件的下侧Margin大小为固定的22vp，showCounter的垂直偏移量为字体高度。

变更后：在设置showCounter后，标准字体下，TextInput组件的下侧Margin以及垂直偏移量和变更前保持一致。非标准字体设置下，TextInput组件的下侧Margin大小为16vp加上showCounter的字体高度，垂直偏移量为8vp。

设置非标准字体时，变更前后对比效果如下图所示：

| 变更前 | 变更后 |
| --- | --- |
|  |  |

示例：

```
1. @Entry
2. @Component
3. struct Index {
4. @State message: string = 'Hello World';

6. build() {
7. Column() {
8. TextInput({text: "输入文字1"})
9. .showCounter(true)
10. .maxLength(10)
11. TextInput({text: "输入文字2"})
12. }
13. .height('100%')
14. .width('100%')
15. }
16. }
```

**起始API Level**

11

**变更的接口/组件**

TextInput组件showCounter接口。

**适配指导**

默认效果变更，无需适配，但应注意变更后的默认效果是否符合开发者预期，如不符合则应自定义修改效果控制变量以达到预期。

## MenuItem组件在非PC/2in1设备上超长文本布局由缩略显示变更为换行显示

**变更原因**

对于使用超长文本的MenuItem组件场景，默认布局效果优化，UX体验更佳。

**变更影响**

此变更不涉及应用适配。

说明

此变更已做版本隔离，变更仅在应用的targetSdkVersion设置为大于等于5.0.1(13)时生效。

变更前：MenuItem组件含有超长文本时，文本缩略显示。

变更后：API13开始，MenuItem组件含有超长文本时，在PC/2in1设备上不换行，其余设备无限换行。

| 变更前长文本缩略 | 变更后非PC/2in1设备长文本换行 |
| --- | --- |
|  |  |

**起始API Level**

11

**变更的接口/组件**

MenuItem组件。

**适配指导**

MenuItem UX默认布局效果变更，应用无需适配。

## Tabs组件barOverlap接口默认效果变更

**变更原因**

优化Tabs组件barOverlap属性设置为true时，TabBar的模糊效果和渲染性能。

**变更影响**

此变更涉及应用适配。

变更前：设置barOverlap属性为true时，TabBar默认背景色修改为'#F2F1F3F5'并添加模糊效果。

变更后：设置barOverlap属性为true时，TabBar默认模糊材质的BlurStyle值修改为'BlurStyle.COMPONENT\_THICK'。

| 变更前 | 变更后 |
| --- | --- |
|  |  |

**起始API Level**

10

**变更的接口/组件**

barOverlap接口

**适配指导**

当barOverlap设置为true时，开发者若期望无模糊效果，设置barBackgroundBlurStyle为BlurStyle.NONE。示例如下：

```
1. @Entry
2. @Component
3. struct barHeightTest {
4. @State arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
5. build() {
6. Column() {
7. Tabs({ barPosition: BarPosition.End }) {
8. TabContent() {
9. Column() {
10. List({ space: 10 }) {
11. ForEach(this.arr, (item: number) => {
12. ListItem() {
13. Text("item" + item).width('80%').height(200).fontSize(16).textAlign(TextAlign.Center).backgroundColor('#fff8b81e')
14. }
15. }, (item: string) => item)
16. }.width('100%').height('100%')
17. .lanes(2).alignListItem(ListItemAlign.Center)
18. }.width('100%').height('100%')
19. .backgroundColor(Color.Pink)
20. }
21. .tabBar(new BottomTabBarStyle($r('sys.media.ohos_icon_mask_svg'), "测试0"))

23. TabContent() {
24. Column() {
25. List({ space: 10 }) {
26. ForEach(this.arr, (item: number) => {
27. ListItem() {
28. Text("item" + item).width('80%').height(200).fontSize(16).textAlign(TextAlign.Center).backgroundColor('#fff8b81e')
29. }
30. }, (item: string) => item)
31. }.width('100%').height('100%')
32. .lanes(2).alignListItem(ListItemAlign.Center)
33. }.width('100%').height('100%')
34. .backgroundColor(Color.Blue)
35. }
36. .tabBar(new BottomTabBarStyle($r('sys.media.ohos_icon_mask_svg'), "测试1"))
37. }
38. .barOverlap(true)
39. .barBackgroundBlurStyle(BlurStyle.NONE) // 关闭TabBar模糊效果
40. }
41. }
42. }
```
