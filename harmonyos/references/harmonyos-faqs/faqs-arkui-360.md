---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-360
title: 进入全屏模式后隐藏状态栏，退出全屏模式如何显示状态栏
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 进入全屏模式后隐藏状态栏，退出全屏模式如何显示状态栏
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:32+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:720acdaaa0a63297ef68c80b25f95ac22c9b0d12f891ce8b7f644c9e929255d4
---

**问题描述**

当应用进入全屏模式时调用[setWindowLayoutFullscreen](../harmonyos-references/arkts-apis-window-window.md#setwindowlayoutfullscreen9)接口会导致状态栏隐藏，返回非全屏页面时需要重新显示状态栏。

**解决措施**

退出页面时，需要调用[setSpecificSystemBarEnabled](../harmonyos-references/arkts-apis-window-window.md#setspecificsystembarenabled11)启用状态栏,再调用[setWindowLayoutFullscreen](../harmonyos-references/arkts-apis-window-window.md#setwindowlayoutfullscreen9)接口刷新布局使设置生效。

参考代码

首先获取窗口对象，可参考：[Interface (Window)](../harmonyos-references/arkts-apis-window-window.md)。

```
1. // EntryAbility.ets

4. onWindowStageCreate(windowStage: window.WindowStage): void {
5. // Main window is created, set main page for this ability
6. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

9. windowStage.loadContent('pages/GridImage', (err) => {
10. if (err.code) {
11. hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
12. return;
13. }
14. hilog.info(0x0000, 'testTag', 'Succeeded in loading the content.');

17. let windowClass: window.Window = windowStage.getMainWindowSync(); // 获取应用主窗口
18. // 1. 设置窗口全屏
19. let isLayoutFullScreen = true;
20. windowClass.setWindowLayoutFullScreen(isLayoutFullScreen);
21. // 2. 缓存window窗口对象
22. AppStorage.setOrCreate('windowClass', windowClass);
23. });
24. }
```

[EntryAbilityFullScreenStatus.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/entryability/EntryAbilityFullScreenStatus.ets#L28-L51)

```
1. import { window } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct GridImage {
7. @State message: string = 'Hello World';
8. @State isVisible: boolean = true;
9. @State isVisibleButton: boolean = true;
10. data: number[] = [];
11. windowClass = AppStorage.get<window.Window>('windowClass') as window.Window;

14. aboutToAppear(): void {
15. for (let i = 0; i < 40; i++) {
16. this.data.push(i);
17. }
18. }

21. build() {
22. Stack() {
23. Grid() {
24. ForEach(this.data, (item: number, index: number) => {
25. GridItem() {
26. Image($r('app.media.startIcon'))
27. .width('100%')
28. .objectFit(ImageFit.Cover)
29. .onClick(() => {
30. let isLayoutFullScreen = true;
31. this.windowClass.setWindowLayoutFullScreen(isLayoutFullScreen);
32. this.windowClass.setSpecificSystemBarEnabled('status', false);
33. this.windowClass.setSpecificSystemBarEnabled('navigationIndicator', false);
34. this.isVisible = !this.isVisible;
35. })
36. }
37. .aspectRatio(1)
38. }, (item: number, index: number) => JSON.stringify(item) + index)
39. }
40. .visibility(this.isVisible ? Visibility.Visible : Visibility.None)
41. .columnsTemplate('1fr 1fr 1fr 1fr')
42. .rowsGap(2)
43. .columnsGap(2)
44. .height('100%')
45. .width('100%')

48. Image($r('app.media.startIcon'))
49. .objectFit(ImageFit.Contain)
50. .width('100%')
51. .visibility(this.isVisible ? Visibility.None : Visibility.Visible)
52. .onClick(() => {
53. let isLayoutFullScreen = false;
54. this.windowClass.setSpecificSystemBarEnabled('status', true);
55. this.windowClass.setSpecificSystemBarEnabled('navigationIndicator', true);
56. this.windowClass.setWindowLayoutFullScreen(isLayoutFullScreen);
57. this.isVisible = !this.isVisible;
58. })
59. }
60. }
61. }
```

[FullScreenStatusBar.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/FullScreenStatusBar.ets#L21-L81)
