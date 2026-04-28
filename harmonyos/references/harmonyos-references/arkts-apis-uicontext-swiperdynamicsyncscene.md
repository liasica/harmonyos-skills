---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-swiperdynamicsyncscene
title: Class (SwiperDynamicSyncScene)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > @ohos.arkui.UIContext (UIContext) > Class (SwiperDynamicSyncScene)
category: harmonyos-references
scraped_at: 2026-04-28T08:00:26+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:fa0427144d5cb7d4525f7765e3f3f6d315c458357a5d4ddc992ef1efdc0084b3
---

提供Swiper组件相关帧率的配置。

说明

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Class首批接口从API version 12开始支持。
* SwiperDynamicSyncScene继承自[DynamicSyncScene](arkts-apis-uicontext-dynamicsyncscene.md)，对应Swiper的动态帧率场景。

## 属性

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type12+ | [SwiperDynamicSyncSceneType](arkts-apis-uicontext-e.md#swiperdynamicsyncscenetype12) | 是 | 否 | Swiper的动态帧率场景。 |

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
26. let scenes = this.getUIContext().requireDynamicSyncScene("dynamicSwiper") as SwiperDynamicSyncScene[];
27. if (scenes) {
28. this.scenes = scenes;
29. }
30. })
31. }

33. Button("set frame")
34. .onClick(() => {
35. this.scenes.forEach((scenes: SwiperDynamicSyncScene) => {

37. if (scenes.type == SwiperDynamicSyncSceneType.ANIMATION) {
38. scenes.setFrameRateRange(this.ANIMATION);
39. }

41. if (scenes.type == SwiperDynamicSyncSceneType.GESTURE) {
42. scenes.setFrameRateRange(this.GESTURE);
43. }
44. });
45. })
46. }
47. }
48. }
```
