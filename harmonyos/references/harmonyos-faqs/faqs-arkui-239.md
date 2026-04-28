---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-239
title: 如何获取设备屏幕横竖屏状态
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何获取设备屏幕横竖屏状态
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:01+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:eead2f9dff428c3cc7724b2f093226d1c7b90fb6a84512f4515b95e8de4e6397
---

方法一：利用媒体查询

```
1. import { mediaquery, UIContext } from '@kit.ArkUI';

3. // Store context in EntryAbility
4. const context = AppStorage.get("context") as UIContext;
5. let listener = context.getMediaQuery().matchMediaSync('(orientation: landscape)'); // Listen to landscape events
6. function onPortrait(mediaQueryResult: mediaquery.MediaQueryResult) {
7. console.info('mediaQueryResult.matches:' + mediaQueryResult.matches)
8. if (mediaQueryResult.matches) {
9. // do something here
10. } else {
11. // do something here
12. }
13. }
14. listener.on('change', onPortrait) // Register callback
15. listener.off('change', onPortrait) // Unregister callback

17. @Entry
18. @Component
19. struct Index {
20. build() {
21. Column() {
22. Column() {
23. Text('test')
24. }
25. .width('100%')
26. }
27. .height('100%')
28. .width('100%')
29. .justifyContent(FlexAlign.End)
30. }
31. }
```

[GetHorizontalAndVerticalScreenStatus.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/GetHorizontalAndVerticalScreenStatus.ets#L21-L51)

方法二：

可通过[display.getDefaultDisplaySync](../harmonyos-references/js-apis-display.md#displaygetdefaultdisplaysync9)方法获取到[Display](../harmonyos-references/js-apis-display.md#display)实例，再通过此实例获取其rotation属性即可获取屏幕横竖屏状态。

```
1. import { display, window } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct WindowRotation {
6. build() {
7. Text("Scroll Area")
8. .width("100%")
9. .height("100%")
10. .backgroundColor(0X330000FF)
11. .fontSize(16)
12. .textAlign(TextAlign.Center)
13. .onClick(() => {
14. window.getLastWindow(this.getUIContext().getHostContext(), (err, win) => {
15. let cutOutInfo = win.getWindowAvoidArea(window.AvoidAreaType.TYPE_SYSTEM_GESTURE)
16. console.log(JSON.stringify(cutOutInfo))
17. if (window.Orientation.AUTO_ROTATION) {
18. let rotation: number = display.getDefaultDisplaySync().orientation // Get current screen orientation enum value
19. console.log('' + rotation);
20. if (rotation == 0) {
21. console.log("CutOutInfo Portrait data: " + JSON.stringify(cutOutInfo));
22. } else if (rotation == 1) {
23. console.log("CutOutInfo Landscape data: " + JSON.stringify(cutOutInfo));
24. } else if (rotation == 2) {
25. console.log("CutOutInfo Reverse portrait data: " + JSON.stringify(cutOutInfo));
26. } else {
27. console.log("CutOutInfo Reverse landscape data: " + JSON.stringify(cutOutInfo));
28. }
29. }
30. })
31. })
32. }
33. }
```

[GetHorizontalAndVerticalScreenStatusWindowRotation.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/GetHorizontalAndVerticalScreenStatusWindowRotation.ets#L21-L53)
