---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-marqueedynamicsyncscene
title: Class (MarqueeDynamicSyncScene)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > @ohos.arkui.UIContext (UIContext) > Class (MarqueeDynamicSyncScene)
category: harmonyos-references
scraped_at: 2026-04-28T08:00:25+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:1179c1d69aceff0ccda5f04b2980817a5ff7d485437454f10349f884c6eb9eca
---

提供Marquee组件相关帧率的配置。

说明

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Class首批接口从API version 14开始支持。
* MarqueeDynamicSyncScene继承自[DynamicSyncScene](arkts-apis-uicontext-dynamicsyncscene.md)，对应[Marquee](ts-basic-components-marquee.md)的动态帧率场景。

## 属性

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [MarqueeDynamicSyncSceneType](arkts-apis-uicontext-e.md#marqueedynamicsyncscenetype14) | 是 | 否 | Marquee的动态帧率场景。 |

**示例：**

```
1. import { MarqueeDynamicSyncSceneType, MarqueeDynamicSyncScene } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct MarqueeExample {
6. @State start: boolean = false;
7. @State src: string = '';
8. @State marqueeText: string = 'Running Marquee';
9. private fromStart: boolean = true;
10. private step: number = 10;
11. private loop: number = Number.POSITIVE_INFINITY;
12. controller: TextClockController = new TextClockController();
13. convert2time(value: number): string {
14. let date = new Date(Number(value+'000'));
15. let hours = date.getHours().toString().padStart(2, '0');
16. let minutes = date.getMinutes().toString().padStart(2, '0');
17. let seconds = date.getSeconds().toString().padStart(2, '0');
18. return hours+ ":" + minutes + ":" + seconds;
19. }
20. @State ANIMATION: ExpectedFrameRateRange = { min: 0, max: 120, expected: 30 };
21. private scenes: MarqueeDynamicSyncScene[] = [];

23. build() {
24. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
25. Marquee({
26. start: this.start,
27. step: this.step,
28. loop: this.loop,
29. fromStart: this.fromStart,
30. src: this.marqueeText + this.src
31. })
32. .marqueeUpdateStrategy(MarqueeUpdateStrategy.PRESERVE_POSITION)
33. .width(300)
34. .height(80)
35. .fontColor('#FFFFFF')
36. .fontSize(48)
37. .fontWeight(700)
38. .backgroundColor('#182431')
39. .margin({ bottom: 40 })
40. .id('dynamicMarquee')
41. .onAppear(()=>{
42. this.scenes = this.getUIContext().requireDynamicSyncScene('dynamicMarquee') as MarqueeDynamicSyncScene[];
43. })
44. Button('Start')
45. .onClick(() => {
46. this.start = true;
47. this.controller.start();
48. this.scenes.forEach((scenes: MarqueeDynamicSyncScene) => {
49. if (scenes.type == MarqueeDynamicSyncSceneType.ANIMATION) {
50. scenes.setFrameRateRange(this.ANIMATION);
51. }
52. });
53. })
54. .width(120)
55. .height(40)
56. .fontSize(16)
57. .fontWeight(500)
58. .backgroundColor('#007DFF')
59. TextClock({ timeZoneOffset: -8, controller: this.controller })
60. .format('hms')
61. .onDateChange((value: number) => {
62. this.src = this.convert2time(value);
63. })
64. .margin(20)
65. .fontSize(30)
66. }
67. .width('100%')
68. .height('100%')
69. }
70. }
```
