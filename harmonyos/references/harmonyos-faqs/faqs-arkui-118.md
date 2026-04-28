---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-118
title: 如何修改状态栏字体颜色
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何修改状态栏字体颜色
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:32+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:4879ff59168c9898ffc32a34e26078b8a5c35b4f5817b5539b830e4f0391dd42
---

[setWindowSystemBarProperties](../harmonyos-references/arkts-apis-window-window.md#setwindowsystembarproperties9)可以用于设置窗口内导航栏和状态栏的属性，包括状态栏背景颜色和状态栏文字颜色等。

在EntryAbility.ets的onWindowStageCreate方法中设置WindowStage的AppStorage。参考代码如下：

```
1. AppStorage.setOrCreate('windowStage',windowStage);
```

[EntryAbilityStatusBar.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/entryability/EntryAbilityStatusBar.ets#L41-L41)

通过setWindowSystemBarProperties可以设置状态栏样式。

```
1. import { window } from '@kit.ArkUI';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Component
5. struct ChangeStatusBar {
6. windowStage: window.WindowStage = AppStorage.get("windowStage") as window.WindowStage;
7. // How to get the main window
8. mainWin: window.Window = this.windowStage.getMainWindowSync();

10. aboutToAppear(): void {
11. let sysBarProps: window.SystemBarProperties = {
12. statusBarColor: '#000000',
13. statusBarContentColor: '#ffffff'
14. };
15. this.mainWin.setWindowSystemBarProperties(sysBarProps).then(() => {
16. console.info('[StaticUtils] Succeeded in setting the system bar properties.');
17. }).catch((err: BusinessError) => {
18. console.error(`setting system bar properties failed, code is ${err.code}, message is ${err.message}`);
19. });
20. }

22. build() {
23. Row() {
24. Column({ space: 10 }) {
25. Text('Demo of modifying the status bar')
26. .fontSize(25)
27. .margin(20)
28. .fontColor(0x3399FF)
29. }.width('100%')
30. }.height('100%').backgroundColor(Color.White)
31. }
32. }
```

[ChangeTheFontColorOfTheStatusBar.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ChangeTheFontColorOfTheStatusBar.ets#L21-L52)
