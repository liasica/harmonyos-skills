---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-animatorproperty
title: 属性动画 (animation)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 动画 > 属性动画 (animation)
category: harmonyos-references
scraped_at: 2026-04-29T13:52:41+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:7a08d7f3bc4d7a6b0b198cf1087c00903883f5c468c5fdb2bf3e169080314a4d
---

组件的某些通用属性变化时，可以通过属性动画实现渐变过渡效果，提升用户体验。支持的属性包括[width](ts-universal-attributes-size.md#width)、[height](ts-universal-attributes-size.md#height)、[backgroundColor](ts-universal-attributes-background.md#backgroundcolor)、[opacity](ts-universal-attributes-opacity.md#opacity)、[scale](ts-universal-attributes-transformation.md#scale)、[rotate](ts-universal-attributes-transformation.md#rotate)、[translate](ts-universal-attributes-transformation.md#translate)等。对于改变布局类属性（如宽高）的动画，内容通常会直接跳转到最终状态，例如文字或[Canvas](ts-components-canvas-canvas.md)中的内容。如果希望内容跟随宽高变化，可以使用[renderFit](ts-universal-attributes-renderfit.md#renderfit)属性进行配置。

说明

从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## animation

PhonePC/2in1TabletTVWearable

animation(value:AnimateParam): T

设置组件的属性动画。

说明

* 在单一页面上存在大量应用动效的组件时，可以使用[renderGroup](ts-universal-attributes-image-effect.md#rendergroup10)方法来解决卡顿问题，从而提升动画性能。最佳实践请参考[动画使用指导-使用renderGroup](../best-practices/bpta-fair-use-animation.md#section1223162922415)。
* 该接口不支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [AnimateParam](ts-explicit-animation.md#animateparam对象说明) | 是 | 设置动画效果相关参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

属性动画只对写在animation前面的属性生效，且对组件构造器的属性不生效。

```
1. @Entry
2. @Component
3. struct AnimationExample {
4. @State widthSize: number = 250;
5. @State heightSize: number = 100;
6. @State rotateAngle: number = 0;
7. @State flag: boolean = true;
8. @State space: number = 10;

10. build() {
11. Column() {
12. Column({ space: this.space }) // 改变Column构造器中的space动画不生效
13. .onClick(() => {
14. if (this.flag) {
15. this.widthSize = 150;
16. this.heightSize = 60;
17. this.space = 20; // 改变this.space动画不生效
18. } else {
19. this.widthSize = 250;
20. this.heightSize = 100;
21. this.space = 10; // 改变this.space动画不生效
22. }
23. this.flag = !this.flag;
24. })
25. .backgroundColor(Color.Black)
26. .margin(30)
27. .width(this.widthSize) // 只有写在animation前面才生效
28. .height(this.heightSize) // 只有写在animation前面才生效
29. .animation({
30. duration: 2000,
31. curve: Curve.EaseOut,
32. iterations: 3,
33. playMode: PlayMode.Normal
34. })
35. // .width(this.widthSize) // 动画不生效
36. // .height(this.heightSize) // 动画不生效
37. }
38. }
39. }
```

## 示例

PhonePC/2in1TabletTVWearable

该示例通过animation实现了组件的属性动画。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct AttrAnimationExample {
5. @State widthSize: number = 250
6. @State heightSize: number = 100
7. @State rotateAngle: number = 0
8. @State flag: boolean = true

10. build() {
11. Column() {
12. Button('change size')
13. .onClick(() => {
14. if (this.flag) {
15. this.widthSize = 150
16. this.heightSize = 60
17. } else {
18. this.widthSize = 250
19. this.heightSize = 100
20. }
21. this.flag = !this.flag
22. })
23. .margin(30)
24. .width(this.widthSize)
25. .height(this.heightSize)
26. .animation({
27. duration: 2000,
28. curve: Curve.EaseOut,
29. iterations: 3,
30. playMode: PlayMode.Normal
31. })
32. Button('change rotate angle')
33. .onClick(() => {
34. this.rotateAngle = 90
35. })
36. .margin(50)
37. .rotate({ angle: this.rotateAngle })
38. .animation({
39. duration: 1200,
40. curve: Curve.Friction,
41. delay: 500,
42. iterations: -1, // 设置-1表示动画无限循环
43. playMode: PlayMode.Alternate,
44. expectedFrameRateRange: {
45. min: 20,
46. max: 120,
47. expected: 90,
48. }
49. })
50. }.width('100%').margin({ top: 20 })
51. }
52. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/uEifmZSFRganTCPHnHmhmQ/zh-cn_image_0000002558606888.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055240Z&HW-CC-Expire=86400&HW-CC-Sign=48A6EBF9E06FCC167304CAD55A6922606E858994C11EA8ECD894C4D9B377AE55)
