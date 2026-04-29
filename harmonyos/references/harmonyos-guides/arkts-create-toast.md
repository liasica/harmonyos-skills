---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-create-toast
title: 即时反馈（Toast）
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用弹窗 > 即时反馈（Toast）
category: harmonyos-guides
scraped_at: 2026-04-29T13:27:59+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:730b64bb441f000c3e7813518d1efdbf70c776a261fd5c475940e739c605fc8c
---

即时反馈（Toast）是一种临时性的消息提示框，用于向用户显示简短的操作反馈或状态信息。​它通常在屏幕的底部或顶部短暂弹出，随后在一段时间后自动消失。即时反馈的主要目的是提供简洁、不打扰的信息反馈，避免干扰用户当前的操作流程。

可以通过使用[UIContext](../harmonyos-references/arkts-apis-uicontext-uicontext.md)中的[getPromptAction](../harmonyos-references/arkts-apis-uicontext-uicontext.md#getpromptaction)方法获取当前UI上下文关联的[PromptAction](../harmonyos-references/arkts-apis-uicontext-promptaction.md)对象，再通过该对象调用[showToast](../harmonyos-references/arkts-apis-uicontext-promptaction.md#showtoast)创建并显示文本提示框。

说明

为了安全考虑，例如Toast恶意遮挡其他页面，Toast只能显示在当前的UI实例中，应用退出后，不会单独显示在桌面上。

## 使用建议

* 合理使用弹出场景，避免过度提醒用户。

  可以针对以下常用场景使用即时反馈操作，例如，当用户执行某个操作时及时结果反馈，用来提示用户操作是否成功或失败；或是当应用程序的状态发生变化时提供状态更新等。
* 注意文本的信息密度，即时反馈展示时间有限，应当避免长文本的出现。

  Toast控件的文本应该清晰可读，字体大小和颜色应该与应用程序的主题相符。除此之外，即时反馈控件本身不应该包含任何可交互的元素，如按钮或链接。
* 杜绝强制占位和密集弹出的提示。

  即时反馈作为应用内的轻量通知，应当避免内容布局占用界面内的其他元素信息，如遮盖弹出框的展示内容，从而迷惑用户弹出的内容是否属于弹出框。再或者频繁性的弹出信息内容，且每次弹出之间无时间间隔，影响用户的正常使用。也不要在短时间内频繁弹出新的即时反馈替代上一个。即时反馈的单次显示时长不要超过 3 秒钟，避免影响用户正常的行为操作。
* 遵从系统默认弹出位置。

  即时反馈在系统中默认从界面底部弹出，距离底部有一定的安全间距，作为系统性的应用内提示反馈，请遵从系统默认效果，避免与其他弹出类组件内容重叠。特殊场景下可对内容布局进行规避。
* 弹框字体最大放大倍数限制。

  即时反馈中，字体的最大放大倍数为2。

## 即时反馈模式对比

即时反馈提供了两种显示模式，分别为DEFAULT（显示在应用内）、TOP\_MOST（显示在应用之上）。

在TOP\_MOST类型的Toast显示前，会创建一个全屏大小的子窗（手机上子窗大小和主窗大小一致），然后在该子窗上计算Toast的布局位置，最后显示在该子窗上。具体和DEFAULT模式Toast的差异如下：

| 差异点 | DEFAULT | TOP\_MOST |
| --- | --- | --- |
| 是否创建子窗 | 否 | 是 |
| 层级 | 显示在主窗内，层级和主窗一致，一般比较低 | 显示在子窗中，一般比主窗层级高，比其他弹窗类组件层级高，比软键盘和权限弹窗层级低 |
| 是否避让软键盘 | 软键盘抬起时，必定上移软键盘的高度 | 软键盘抬起时，只有toast被遮挡时，才会避让，且避让后toast底部距离软键盘高度为80vp |
| UIExtension内布局 | 以UIExtension为主窗中布局，对齐方式与UIExtension对齐 | 以宿主窗口为主窗中布局，对齐方式与宿主窗口对齐 |

```
1. import { promptAction } from '@kit.ArkUI';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const TAG: string = '[Sample_dialogproject]';
6. const DOMAIN: number = 0xFF00;

8. @Entry
9. @Component
10. export struct DefaultAndTopToastExample {
11. build() {
12. // ...
13. Column({ space: 10 }) {
14. TextInput()
15. Button('Toast of the DEFAULT type')
16. .fontSize(20)
17. .fontWeight(FontWeight.Bold)
18. .onClick(() => {
19. try {
20. this.getUIContext().getPromptAction().showToast({
21. message: 'ok, I am DEFAULT toast',
22. duration: 2000,
23. showMode: promptAction.ToastShowMode.DEFAULT,
24. bottom: 80
25. });
26. } catch (error) {
27. let message = (error as BusinessError).message;
28. let code = (error as BusinessError).code;
29. hilog.error(DOMAIN, TAG, '%{public}s', 'showToast args error code is $\{code}, message is $\{message}');
30. }
31. })

33. Button('Toast of the TOPMOST type')
34. .fontSize(20)
35. .fontWeight(FontWeight.Bold)
36. .onClick(() => {
37. try {
38. this.getUIContext().getPromptAction().showToast({
39. message: 'ok, I am TOP_MOST toast',
40. duration: 2000,
41. showMode: promptAction.ToastShowMode.TOP_MOST,
42. bottom: 85
43. });
44. }  catch (error) {
45. let message = (error as BusinessError).message;
46. let code = (error as BusinessError).code;
47. hilog.error(DOMAIN, TAG, '%{public}s', 'showToast args error code is $\{code}, message is $\{message}');
48. }
49. })
50. }
51. // ...
52. }
53. }
```

[DefaultAndTopToast.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/Toast/DefaultAndTopToast.ets#L16-L80)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/BUjjvks0SWmtNtKu0ukDVg/zh-cn_image_0000002589244223.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052625Z&HW-CC-Expire=86400&HW-CC-Sign=9C1CAA904A3EA08F34DDD89625512D8636754A27742408A901B71268C2016253)

## 创建即时反馈

适用于短时间内提示框自动消失的场景。

```
1. import { PromptAction } from '@kit.ArkUI';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const TAG: string = '[Sample_dialogproject]';
6. const DOMAIN: number = 0xFF00;

8. @Entry
9. @Component
10. export struct CreateToastExample {
11. private uiContext: UIContext = this.getUIContext();
12. private promptAction: PromptAction = this.uiContext.getPromptAction();
13. build() {
14. // ...
15. Column() {
16. Button('Show toast').fontSize(20)
17. .onClick(() => {
18. try {
19. this.promptAction.showToast({
20. message: 'Hello World',
21. duration: 2000
22. });
23. } catch (error) {
24. let message = (error as BusinessError).message;
25. let code = (error as BusinessError).code;
26. hilog.error(DOMAIN, TAG, '%{public}s', 'showToast args error code is $\{code}, message is $\{message}');
27. }
28. })
29. }.height('100%').width('100%').justifyContent(FlexAlign.Center)
30. // ...
31. }
32. }
```

[CreateToast.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/Toast/CreateToast.ets#L16-L56)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/psoES4_ZQpKYmadZpQOkBg/zh-cn_image_0000002558764416.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052625Z&HW-CC-Expire=86400&HW-CC-Sign=337442273E73A54851123E55415D3C554BDCF945730E159C93106635691C45C4)

## 显示和关闭即时反馈

适用于提示框停留时间较长，用户操作可以提前关闭提示框的场景。

```
1. import { PromptAction } from '@kit.ArkUI';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const TAG: string = '[Sample_dialogproject]';
6. const DOMAIN: number = 0xFF00;

8. @Entry
9. @Component
10. export struct OpenCloseToastExample {
11. @State toastId: number = 0;
12. private uiContext: UIContext = this.getUIContext();
13. private promptAction: PromptAction = this.uiContext.getPromptAction();

15. build() {
16. // ...
17. Column() {
18. Button('Open Toast')
19. .height(100)
20. .type(ButtonType.Capsule)
21. .onClick(() => {
22. try {
23. this.promptAction.openToast({
24. message: 'Toast Message',
25. duration: 10000,
26. }).then((toastId: number) => {
27. this.toastId = toastId;
28. });
29. } catch (error) {
30. let message = (error as BusinessError).message;
31. let code = (error as BusinessError).code;
32. hilog.error(DOMAIN, TAG, '%{public}s', 'OpenToast error code is $\{code}, message is $\{message}');
33. }
34. })
35. Blank().height(50);
36. Button('Close Toast')
37. .height(100)
38. .type(ButtonType.Capsule)
39. .onClick(() => {
40. try {
41. this.promptAction.closeToast(this.toastId);
42. } catch (error) {
43. let message = (error as BusinessError).message;
44. let code = (error as BusinessError).code;
45. hilog.error(DOMAIN, TAG, '%{public}s', 'CloseToast error code is $\{code}, message is $\{message}');
46. }
47. })
48. }.height('100%').width('100%').justifyContent(FlexAlign.Center)
49. // ...
50. }
51. }
```

[OpenCloseToast.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/Toast/OpenCloseToast.ets#L15-L74)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/hmKK-k-_TYCFo0RQSzcV-w/zh-cn_image_0000002558604760.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052625Z&HW-CC-Expire=86400&HW-CC-Sign=53804A9649AD019777FD281C808FCF3964A5500A7F808184FA2E24A9E3B44E98)
