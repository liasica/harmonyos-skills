---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web_full_screen
title: Web组件支持视频沉浸式全屏播放
breadcrumb: 指南 > 应用框架 > ArkWeb（方舟Web） > 使用网页多媒体 > Web组件支持视频沉浸式全屏播放
category: harmonyos-guides
scraped_at: 2026-04-29T13:29:27+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:b93f5deece4c379ccaf9e98299de7765982e959a590e1639b3262d13fee72287
---

Web组件提供了视频进入全屏和退出全屏的事件功能，应用可通过监听这些事件实现进入和退出沉浸式全屏模式。

Web组件引用第三方H5页面加载的视频，当单击视频全屏时，视频仅扩展至整个Web组件区域，无法实现系统全屏显示（如图2所示）。若要达到系统全屏的沉浸式视频播放效果（如图3所示），则需应用监听进入全屏的事件并调整界面其他组件的属性。

| 图1 退出全屏模式 | 图2 非沉浸式全屏模式 | 图3 沉浸式全屏模式 |
| --- | --- | --- |
|  |  |  |

Web组件可通过[onFullScreenEnter](../harmonyos-references/arkts-basic-components-web-events.md#onfullscreenenter9)和[onFullScreenExit](../harmonyos-references/arkts-basic-components-web-events.md#onfullscreenexit9)回调监听全屏按键的单击事件。其中，onFullScreenEnter表示Web组件进入全屏模式，onFullScreenExit表示Web组件退出全屏模式。在这两个监听事件中，可根据具体业务场景调整某些全局变量，例如组件的显隐状态、组件的margin属性等，以实现退出和进入沉浸式全屏模式的界面效果，如图1和图3所示。

可见性[visibility](../harmonyos-references/ts-universal-attributes-visibility.md#visibility)是ArkUI提供的组件通用属性。开发者可通过设置组件属性visibility的不同值，控制组件的显隐状态。

```
1. import { webview } from '@kit.ArkWeb';

3. @Entry
4. @Component
5. struct ShortWebPage {
6. controller: webview.WebviewController = new webview.WebviewController();
7. CONSTANT_HEIGHT = 100;
8. @State marginTop: number = this.CONSTANT_HEIGHT;
9. @State isVisible: boolean = true; // 自定义标志位isVisible，来控制是否需要显示组件

11. build() {
12. Column() {
13. Text('TextTextTextText')
14. .width('100%')
15. .height(this.CONSTANT_HEIGHT)
16. .backgroundColor('#e1dede') // 当isVisible标志位为true的时候，组件状态为可见，否则组件状态为不可见，不参与布局、不进行占位
17. .visibility(this.isVisible ? Visibility.Visible :
18. Visibility.None)
19. Web({
20. src: $rawfile('FullScreen.html'), // 示例网址
21. controller: this.controller
22. })
23. .onFullScreenEnter((event) => {
24. console.info('onFullScreenEnter...');
25. // 当全屏的时候，isVisible标志位为false，组件状态为不可见，不参与布局、不进行占位
26. this.isVisible = false;
27. })
28. .onFullScreenExit(() => {
29. console.info('onFullScreenExit...');
30. // 当退出全屏的时候，isVisible标志位为true，组件状态为可见
31. this.isVisible = true;
32. })
33. .width('100%')
34. .height('100%')
35. .zIndex(10)
36. .zoomAccess(true)
37. }.width('100%').height('100%')
38. }
39. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ArkWebPictureInPicture/entry1/src/main/ets/pages/Index.ets#L16-L56)
