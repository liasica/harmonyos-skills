---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-framecallback
title: Class (FrameCallback)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > @ohos.arkui.UIContext (UIContext) > Class (FrameCallback)
category: harmonyos-references
scraped_at: 2026-04-28T08:00:22+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:9e2ddb2bde83e7a21b8a77848eae02454bf2469ab18ac5f7eff93952585e08ea
---

用于设置下一帧渲染时需要执行的任务。

说明

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Class首批接口从API version 12开始支持。
* 以下API需要配合[UIContext](arkts-apis-uicontext-uicontext.md)中的[postFrameCallback](arkts-apis-uicontext-uicontext.md#postframecallback12)和[postDelayedFrameCallback](arkts-apis-uicontext-uicontext.md#postdelayedframecallback12)使用。开发者需要继承该类并重写[onFrame](arkts-apis-uicontext-framecallback.md#onframe12)或[onIdle](arkts-apis-uicontext-framecallback.md#onidle12)方法，实现具体的业务逻辑。

## onFrame12+

PhonePC/2in1TabletTVWearable

onFrame(frameTimeInNano: number): void

在下一帧进行渲染时，该方法将被执行。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| frameTimeInNano | number | 是 | 下一帧渲染开始执行的时间，以纳秒为单位。  取值范围：[0, +∞) |

**示例：**

```
1. import { FrameCallback } from '@kit.ArkUI';

3. class MyFrameCallback extends FrameCallback {
4. private tag: string;

6. constructor(tag: string) {
7. super();
8. this.tag = tag;
9. }

11. onFrame(frameTimeNanos: number) {
12. console.info('MyFrameCallback ' + this.tag + ' ' + frameTimeNanos.toString());
13. }
14. }

16. @Entry
17. @Component
18. struct Index {
19. build() {
20. Row() {
21. Column() {
22. Button('点击触发postFrameCallback')
23. .onClick(() => {
24. this.getUIContext().postFrameCallback(new MyFrameCallback("normTask"));
25. })
26. Button('点击触发postDelayedFrameCallback')
27. .onClick(() => {
28. this.getUIContext().postDelayedFrameCallback(new MyFrameCallback("delayTask"), 5);
29. })
30. }
31. .width('100%')
32. }
33. .height('100%')
34. }
35. }
```

## onIdle12+

PhonePC/2in1TabletTVWearable

onIdle(timeLeftInNano: number): void

在下一帧渲染结束时，如果距离下一个Vsync信号到来还有1ms以上的剩余时间，该方法将被执行，否则将顺延至后面的帧。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| timeLeftInNano | number | 是 | 这一帧剩余的空闲时间，以纳秒为单位。  取值范围：[0, +∞) |

**示例：**

```
1. import { FrameCallback } from '@kit.ArkUI';

3. class MyIdleCallback extends FrameCallback {
4. private tag: string;

6. constructor(tag: string) {
7. super();
8. this.tag = tag;
9. }

11. onIdle(timeLeftInNano: number) {
12. console.info('MyIdleCallback ' + this.tag + ' ' + timeLeftInNano.toString());
13. }
14. }

16. @Entry
17. @Component
18. struct Index {
19. build() {
20. Row() {
21. Column() {
22. Button('点击触发postFrameCallback')
23. .onClick(() => {
24. this.getUIContext().postFrameCallback(new MyIdleCallback("normTask"));
25. })
26. Button('点击触发postDelayedFrameCallback')
27. .onClick(() => {
28. this.getUIContext().postDelayedFrameCallback(new MyIdleCallback("delayTask"), 5);
29. })
30. }
31. .width('100%')
32. }
33. .height('100%')
34. }
35. }
```
