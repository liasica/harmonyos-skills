---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rotation-transition-animation
title: 旋转屏动画
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用动画 > 转场动画 > 旋转屏动画
category: harmonyos-guides
scraped_at: 2026-04-29T13:28:11+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7c21a574b5d3de06c97c286332a291dc1997446cfd00f5bbe5377f71cbd35d43
---

旋转屏动画主要分为两类：[布局切换的旋转屏动画](arkts-rotation-transition-animation.md#布局切换的旋转屏动画)和[透明度变化的旋转屏动画](arkts-rotation-transition-animation.md#透明度变化的旋转屏动画)，旨在实现屏幕显示方向变化时的自然过渡。布局切换的旋转屏动画实现较为简便，例如在module.json5中配置自动旋转（或设置窗口显示方向）即可实现。而透明度变化的旋转屏动画则需在module.json5配置的基础上，预备两套视图，在屏幕旋转时，通过视图切换，使消失的视图呈现渐隐效果，新出现的视图则渐显，从而营造流畅的视觉体验。

## 布局切换的旋转屏动画

布局切换时的旋转屏动画，是在屏幕显示方向改变时，为窗口与应用视图同步旋转而设计的大小和位置过渡动画。这种布局切换的旋转屏动画是系统默认的，便于开发者实现。当屏幕显示方向变化时，系统会生成窗口旋转动画，并自动调整窗口大小以匹配旋转后的尺寸。在此过程中，窗口会通知对应的应用，要求其根据新的窗口大小重新布局，产生与窗口旋转动画参数相同的布局动画。

切换屏幕方向即可实现布局切换的旋转屏动画效果。

```
1. @Entry
2. @Component
3. struct rotation {
4. build() {
5. Stack() {
6. // 请将$r('app.media.tree')替换为实际资源文件
7. Image($r('app.media.tree'))
8. .position({ x: 0, y: 0 })
9. .size({ width: 100, height: 100 })
10. .id('image1')
11. }
12. .backgroundColor(Color.White)
13. .size({ width: '100%', height: '100%' })
14. }
15. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Animation/entry/src/main/ets/pages/rotation/template1/Index.ets#L17-L34)

需要在项目的module.json5文件中的abilities列表里添加"orientation"，指定为"auto\_rotation"。

```
1. "orientation": "auto_rotation",
```

布局切换的旋转屏动画，会对同步旋转的窗口与应用视图做大小和位置的过渡。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/kWoUzLNPQdSK61V-RJUolg/zh-cn_image_0000002589244289.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052810Z&HW-CC-Expire=86400&HW-CC-Sign=F93BBD79EEA8BD77DAB4920498439E2429FADFC77C4412F08C6BB92087FC3F92)

## 透明度变化的旋转屏动画

透明度变化的旋转屏动画在屏幕显示方向变化时启用，当窗口进行旋转动画时，为旋转过程中新增或删除的组件添加默认透明度转场，以实现组件的优雅出现和消失。此功能通过监听窗口旋转事件，在事件中切换组件的视图效果，如果消失视图的根节点和新出现视图的根节点未设置转场效果，会为其自动添加默认透明度转场（即[TransitionEffect](../harmonyos-references/ts-transition-animation-component.md#transitioneffect10对象说明).OPACITY），展现出透明度的渐隐和渐显效果。

```
1. import { display } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct rotation {

7. // 获取通过监听窗口的windowsSizeChange事件得到的屏幕显示方向
8. @StorageLink('orientation') myOrientation: display.Orientation = display.Orientation.PORTRAIT;

10. build() {
11. Stack() {

13. // 当屏幕显示方向变化时，切换组件的视图效果
14. if (this.myOrientation == display.Orientation.PORTRAIT || this.myOrientation == display.Orientation.PORTRAIT_INVERTED) {
15. // 请将$r('app.media.sky')替换为实际资源文件
16. Image($r('app.media.sky'))
17. .size({ width: 100, height: 100 })
18. .id('image1')

20. // 开发者也可以通过自行设置transition的TransitionEffect.OPACITY转场效果来实现旋转屏动画的透明度变化
21. // .transition(TransitionEffect.OPACITY)
22. } else {
23. // 请将$r('app.media.tree')替换为实际资源文件
24. Image($r('app.media.tree'))
25. .position({ x: 0, y: 0 })
26. .size({ width: 200, height: 200 })
27. .id('image2')

29. // 开发者也可以通过自行设置transition的TransitionEffect.OPACITY来实现旋转屏动画的透明度变化
30. // .transition(TransitionEffect.OPACITY)
31. }
32. }
33. .backgroundColor(Color.White)
34. .size({ width: '100%', height: '100%' })
35. }
36. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Animation/entry/src/main/ets/pages/rotation/template2/Index.ets#L15-L53)

监听窗口旋转的同步事件windowSizeChange来实现视图的切换。例如可在EntryAbility.ets文件的[onWindowStageCreate](../harmonyos-references/js-apis-app-ability-uiability.md#onwindowstagecreate)方法中添加处理逻辑以获取屏幕的显示方向。

```
1. import { display, window } from '@kit.ArkUI';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. const DOMAIN = 0x0000;
5. const TAG: string = 'EntryAbility';
6. // ...
7. onWindowStageCreate(windowStage: window.WindowStage): void {
8. // ...
9. hilog.info(DOMAIN, TAG, '%{public}s', 'Ability onWindowStageCreate');
10. let mainWindow: window.Window;
11. try {
12. mainWindow = windowStage.getMainWindowSync();
13. let displayClass: display.Display = display.getDefaultDisplaySync();
14. AppStorage.setOrCreate('orientation', displayClass.orientation);
15. // 监听窗口的windowsSizeChange事件，旋转屏时会触发该事件
16. mainWindow.on('windowSizeChange', (data) => {
17. hilog.info(DOMAIN, TAG, 'Succeeded in enabling the listener for window size changes. Data: ' + data);
18. let displayClass: display.Display | null = null;
19. try {
20. displayClass = display.getDefaultDisplaySync();
21. hilog.info(DOMAIN, TAG, 'display orientation is ' + displayClass.orientation);
22. // 获取屏幕的显示方向
23. AppStorage.set('orientation', displayClass.orientation);
24. } catch {
25. return;
26. }
27. })
28. } catch {
29. hilog.error(DOMAIN, TAG, '%{public}s', 'error');
30. return;
31. }
32. // ...

34. windowStage.loadContent('pages/Index', (err) => {
35. if (err.code) {
36. hilog.error(DOMAIN, TAG, 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
37. return;
38. }
39. hilog.info(DOMAIN, TAG, 'Succeeded in loading the content.');
40. });
41. }

43. // ...
```

[EntryAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Animation/entry/src/main/ets/entryability/EntryAbility.ets#L21-L144)

需要在项目的module.json5文件中的abilities列表里添加"orientation"，指定为"auto\_rotation"。

```
1. "orientation": "auto_rotation",
```

透明度变化的旋转屏动画，会对窗口做大小和位置的过渡，并同时对应用视图做切换过渡，且为消失隐藏的应用视图做渐隐效果，对新出现的视图做渐显的效果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/4tD2PalpR0iz5N5sYwkr7g/zh-cn_image_0000002558764482.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052810Z&HW-CC-Expire=86400&HW-CC-Sign=69B2ECB2AD60C4B93E10EC9190014EACC885C1BB4E9975DC51EFA809097446F6)
