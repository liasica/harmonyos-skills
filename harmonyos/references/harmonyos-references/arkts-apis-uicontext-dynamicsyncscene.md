---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-dynamicsyncscene
title: Class (DynamicSyncScene)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > @ohos.arkui.UIContext (UIContext) > Class (DynamicSyncScene)
category: harmonyos-references
scraped_at: 2026-04-28T08:00:21+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:90b1c4cb4515888b64a7fdf6ef779a5c639b6b208c3fedbedefe5a0f4895cd76
---

提供组件自定义场景下相关帧率的配置。

说明

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Class首批接口从API version 12开始支持。
* 以下接口需先使用UIContext中的[requireDynamicSyncScene](arkts-apis-uicontext-uicontext.md#requiredynamicsyncscene12)方法获取DynamicSyncScene对象，再通过此实例调用对应方法。

## setFrameRateRange12+

PhonePC/2in1TabletTVWearable

setFrameRateRange(range: ExpectedFrameRateRange): void

设置期望帧率范围。

最终结果不一定是设置的帧率，会由系统能力做综合决策，尽量满足开发者的设置帧率。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| range | [ExpectedFrameRateRange](ts-explicit-animation.md#expectedframeraterange11) | 是 | 设置期望的帧率范围。  默认值：{min:0, max:120, expected: 120} |

**示例：**

```
1. import { SwiperDynamicSyncSceneType, SwiperDynamicSyncScene } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Frame {
6. @State ANIMATION: ExpectedFrameRateRange = { min: 0, max: 120, expected: 90 };
7. @State GESTURE: ExpectedFrameRateRange = { min: 0, max: 120, expected: 30};
8. private scenes: SwiperDynamicSyncScene[] = [];

10. build() {
11. Column() {
12. Text("动画"+ JSON.stringify(this.ANIMATION))
13. Text("跟手"+ JSON.stringify(this.GESTURE))
14. Row(){
15. Swiper() {
16. Text("one")
17. Text("two")
18. Text("three")
19. }
20. .width('100%')
21. .height('300vp')
22. .id("dynamicSwiper")
23. .backgroundColor(Color.Blue)
24. .autoPlay(true)
25. .onAppear(()=>{
26. this.scenes = this.getUIContext().requireDynamicSyncScene("dynamicSwiper") as SwiperDynamicSyncScene[];
27. })
28. }

30. Button("set frame")
31. .onClick(() => {
32. this.scenes.forEach((scenes: SwiperDynamicSyncScene) => {

34. if (scenes.type == SwiperDynamicSyncSceneType.ANIMATION) {
35. scenes.setFrameRateRange(this.ANIMATION);
36. }

38. if (scenes.type == SwiperDynamicSyncSceneType.GESTURE) {
39. scenes.setFrameRateRange(this.GESTURE);
40. }
41. });
42. })
43. }
44. }
45. }
```

## getFrameRateRange12+

PhonePC/2in1TabletTVWearable

getFrameRateRange(): ExpectedFrameRateRange

获取期望帧率范围。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ExpectedFrameRateRange](ts-explicit-animation.md#expectedframeraterange11) | 期望帧率范围。 |

**示例：**

```
1. import { SwiperDynamicSyncSceneType, SwiperDynamicSyncScene } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Frame {
6. @State ANIMATION: ExpectedFrameRateRange = { min: 0, max: 120, expected: 90 };
7. @State GESTURE: ExpectedFrameRateRange = { min: 0, max: 120, expected: 30 };
8. private scenes: SwiperDynamicSyncScene[] = [];

10. build() {
11. Column() {
12. Text("动画"+ JSON.stringify(this.ANIMATION))
13. Text("跟手"+ JSON.stringify(this.GESTURE))
14. Row(){
15. Swiper() {
16. Text("one")
17. Text("two")
18. Text("three")
19. }
20. .width('100%')
21. .height('300vp')
22. .id("dynamicSwiper")
23. .backgroundColor(Color.Blue)
24. .autoPlay(true)
25. .onAppear(() => {
26. this.scenes = this.getUIContext().requireDynamicSyncScene("dynamicSwiper") as SwiperDynamicSyncScene[];
27. })
28. }

30. Button("set frame")
31. .onClick(() => {
32. this.scenes.forEach((scenes: SwiperDynamicSyncScene) => {

34. if (scenes.type == SwiperDynamicSyncSceneType.ANIMATION) {
35. scenes.setFrameRateRange(this.ANIMATION);
36. scenes.getFrameRateRange();
37. }

39. if (scenes.type == SwiperDynamicSyncSceneType.GESTURE) {
40. scenes.setFrameRateRange(this.GESTURE);
41. scenes.getFrameRateRange();
42. }
43. });
44. })
45. }
46. }
47. }
```
