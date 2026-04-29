---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-explicit-animatetoimmediately
title: 显式动画立即下发 (animateToImmediately)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 动画 > 显式动画立即下发 (animateToImmediately)
category: harmonyos-references
scraped_at: 2026-04-29T13:52:43+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d320204711449abc723759f5a3346af4ded58616f170a2e5d9f56ae44458ec69
---

animateToImmediately接口用来提供[显式动画](ts-explicit-animation.md)立即下发功能。同时加载多个属性动画的情况下，使用该接口可以立即执行闭包代码中状态变化导致的过渡动效。

与[animateTo](arkts-apis-uicontext-uicontext.md#animateto)相比，animateToImmediately能即时将生成的动画指令发送至渲染层执行，无需等待vsync信号，从而在视觉效果上实现部分动画的优先呈现。当应用的主线程存在耗时操作，且需提前更新部分用户界面时，此接口可有效缩短应用的响应延迟。需要注意的是，animateToImmediately仅支持渲染层上的属性动画提前执行，无法用于UI侧的逐帧动画。

此外，该接口会将调用前的状态和新生成的动画一并发送至渲染层，因此渲染结果可能会基于调用时的状态进行。务必确保调用时的状态完整，否则前几帧可能出现渲染异常。

因此，建议开发者优先使用[animateTo](arkts-apis-uicontext-uicontext.md#animateto)，以防止干扰框架的显示时序，避免在动画启动时因状态设置不完整而导致的显示错误。

说明

从API version 12开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 接口

PhonePC/2in1TabletTVWearable

## animateToImmediately

PhonePC/2in1TabletTVWearable

animateToImmediately(value: AnimateParam , event: () => void): void

提供显式动画立即下发功能。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [AnimateParam](ts-explicit-animation.md#animateparam对象说明) | 是 | 设置动画效果相关参数。 |
| event | () => void | 是 | 指定显示动效的闭包函数，在闭包函数中导致的状态变化系统会自动插入过渡动画。 |

## 示例

PhonePC/2in1TabletTVWearable

该示例主要演示通过[animateToImmediately](ts-explicit-animatetoimmediately.md#animatetoimmediately)接口来实现显式动画立即下发。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct AnimateToImmediatelyExample {
5. @State widthSize: number = 250;
6. @State heightSize: number = 100;
7. @State opacitySize: number = 0;
8. private flag: boolean = true;

10. build() {
11. Column() {
12. Column()
13. .width(this.widthSize)
14. .height(this.heightSize)
15. .backgroundColor(Color.Green)
16. .opacity(this.opacitySize)
17. Button('change size')
18. .margin(30)
19. .onClick(() => {
20. if (this.flag) {
21. animateToImmediately({
22. delay: 0,
23. duration: 1000
24. }, () => {
25. this.opacitySize = 1;
26. })
27. this.getUIContext()?.animateTo({
28. delay: 1000,
29. duration: 1000
30. }, () => {
31. this.widthSize = 150;
32. this.heightSize = 60;
33. })
34. } else {
35. animateToImmediately({
36. delay: 0,
37. duration: 1000
38. }, () => {
39. this.widthSize = 250;
40. this.heightSize = 100;
41. })
42. this.getUIContext()?.animateTo({
43. delay: 1000,
44. duration: 1000
45. }, () => {
46. this.opacitySize = 0;
47. })
48. }
49. this.flag = !this.flag;
50. })
51. }.width('100%').margin({ top: 5 })
52. }
53. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/P5oJcbaCSTCpjazGg9g5ng/zh-cn_image_0000002589246367.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055242Z&HW-CC-Expire=86400&HW-CC-Sign=93996069FE057E2E60BB3ABD8DC9C45397DF720A8F2AB796CEA0A0E31BE2B50C)
