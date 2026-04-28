---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-266
title: 如何获取屏幕顶部状态栏、底部导航栏和导航条的高度
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何获取屏幕顶部状态栏、底部导航栏和导航条的高度
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:09+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:190c3da173c854e7cf34aee6fc3f87f6c4f02f2309ae7cbeaea1e935ba2c86b4
---

可以使用window的[getWindowAvoidArea](../harmonyos-references/js-apis-arkui-uiextension.md#getwindowavoidarea)方法获取，示例代码如下：

```
1. import { window } from '@kit.ArkUI';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct GetAvoidAreaHeight {
7. context = this.getUIContext();

9. build() {
10. Column() {
11. Button('GetAvoidAreaHeight')
12. .onClick(() => {
13. let systemAvoidAreaType = window.AvoidAreaType.TYPE_SYSTEM; // system
14. let navigationIndicatorType = window.AvoidAreaType.TYPE_NAVIGATION_INDICATOR; // navigation
15. if (this.context) {
16. window.getLastWindow(this.context.getHostContext()).then((data) => {
17. // Get the system default area, usually including the status bar and navigation bar
18. let avoidArea1 = data.getWindowAvoidArea(systemAvoidAreaType);
19. // Top status bar height
20. let statusBarHeight = avoidArea1.topRect.height;
21. // Bottom navigation bar height
22. let bottomNavHeight = avoidArea1.bottomRect.height;
23. // Get the navigation bar area
24. let avoidArea2 = data.getWindowAvoidArea(navigationIndicatorType);
25. // Get the height of the navigation bar area
26. let indicatorHeight = avoidArea2.bottomRect.height;
27. console.info(`statusBarHeight is ${statusBarHeight}`);
28. console.info(`bottomNavHeight is ${bottomNavHeight}`);
29. console.info(`indicatorHeight is ${indicatorHeight}`);
30. }).catch((err: BusinessError) => {
31. console.error(`Failed to obtain the window. Cause: ${JSON.stringify(err)}`);
32. });
33. }
34. })
35. }
36. }
37. }
```

[AvoidAreaHeight.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/AvoidAreaHeight.ets#L21-L58)
