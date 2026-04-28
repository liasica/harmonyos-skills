---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-199
title: 如何设置沉浸式窗口
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何设置沉浸式窗口
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:52+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:e407abe6887fc700173e0ccdeaca58658faa3b88db04403e48466940e0947e47
---

在EntryAbility的onWindowStageCreate方法中通过windowStage获取window，然后分别调用setWindowLayoutFullScreen和setWindowSystemBarEnable方法。参考代码如下：

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. export default class EntryAbility extends UIAbility {
6. onWindowStageCreate(windowStage: window.WindowStage) {
7. // 1.Get the main window of the application.
8. let windowClass: window.Window | null = null;
9. windowStage.getMainWindow((err: BusinessError, data) => {
10. let errCode: number = err.code;
11. if (errCode) {
12. console.error('Failed to obtain the main window. Cause: ' + JSON.stringify(err));
13. return;
14. }
15. windowClass = data;
16. console.info('Succeeded in obtaining the main window. Data: ' + JSON.stringify(data));

18. // 2.Realize immersive effects. Method 1: Set the navigation bar and status bar to not display.
19. let names: Array<'status' | 'navigation'> = [];
20. windowClass.setWindowSystemBarEnable(names).then(() => {
21. console.info('Succeeded in setting the system bar to be visible.');
22. });
23. // 2.Realize immersive effects. Method 2: Set the window to a full screen layout, and coordinate with the transparency, background/text color, and highlighted icons of the navigation bar and status bar to maintain consistency with the main window display.
24. let isLayoutFullScreen = true;
25. windowClass.setWindowLayoutFullScreen(isLayoutFullScreen).then(() => {
26. console.info('Succeeded in setting the window layout to full-screen mode.');
27. });
28. let sysBarProps: window.SystemBarProperties = {
29. statusBarColor: '#ff00ff',
30. navigationBarColor: '#00ff00',
31. statusBarContentColor: '#ffffff',
32. navigationBarContentColor: '#ffffff'
33. };
34. windowClass.setWindowSystemBarProperties(sysBarProps).then(() => {
35. console.info('Succeeded in setting the system bar properties.');
36. });
37. })
38. // 3.Load the corresponding target page for the immersive window.
39. windowStage.loadContent("pages/page2", (err: BusinessError) => {
40. let errCode: number = err.code;
41. if (errCode) {
42. console.error('Failed to load the content. Cause:' + JSON.stringify(err));
43. return;
44. }
45. console.info('Succeeded in loading the content.');
46. });
47. }
48. };
```

[EntryAbilityImmersiveWindow.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/entryability/EntryAbilityImmersiveWindow.ets#L21-L68)

**参考链接**

[体验窗口沉浸式能力](../harmonyos-guides/application-window-stage.md#体验窗口沉浸式能力)
