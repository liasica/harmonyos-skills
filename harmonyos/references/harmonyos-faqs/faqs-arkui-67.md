---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-67
title: 如何设置窗口旋转
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何设置窗口旋转
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:23+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:39202bb41e339db45116569687c810fe9bc6bc64a086092f9acbf7d75c4a6ba8
---

步骤一：通过[getLastWindow()](../harmonyos-references/arkts-apis-window-f.md#windowgetlastwindow9)、[createWindow()](../harmonyos-references/arkts-apis-window-f.md#windowcreatewindow9)、[findWindow()](../harmonyos-references/arkts-apis-window-f.md#windowfindwindow9)中的任一方法获取到Window实例。

步骤二：通过设置[setPreferredOrientation](../harmonyos-references/arkts-apis-window-window.md#setpreferredorientation9)属性来设置窗口的显示方向属性，使用callback异步回调。参数[Orientation](../harmonyos-references/js-apis-display.md#orientation10)提供了窗口显示方向类型枚举。

在EntryAbility.ets中的onWindowStageCreate方法中将WindowStage设置一个AppStorage。参考代码如下：

```
1. AppStorage.setOrCreate('windowStage',windowStage);
```

[EntryAbilityScreenRotation.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/entryability/EntryAbilityScreenRotation.ets#L40-L40)

通过setPreferredOrientation可以设置旋转模式。

```
1. import { display, window } from '@kit.ArkUI';

3. @Component
4. struct ScreenRotation {
5. windowStage: window.WindowStage = AppStorage.get('windowStage') as window.WindowStage;
6. // Method to get the main window
7. mainWin: window.Window = this.windowStage.getMainWindowSync();
8. context = this.getUIContext();

10. onPageShow() {
11. // Method to get the top window
12. window.getLastWindow(this.context.getHostContext());
13. this.mainWin.setPreferredOrientation(window.Orientation.LANDSCAPE);
14. // Use display interface to get current rotation direction, can be placed in listener for continuous updates
15. display.getDefaultDisplaySync().rotation;
16. }

18. build() {
19. Row() {
20. Column({ space: 10 }) {
21. Text('Screen rotation demo')
22. .fontSize(25)
23. .margin(20)
24. .fontColor(0x3399FF)
25. }.width('100%')
26. }.height('100%').backgroundColor(Color.White)
27. }
28. }
```

[ScreenRotation.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ScreenRotation.ets#L21-L48)
