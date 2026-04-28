---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-immersive-effect-check
title: @cross-device-app-dev/immersive-effect-check
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 一次开发多端部署规则@cross-device-app-dev > @cross-device-app-dev/immersive-effect-check
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:24+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:986cb49637ed227165abd44b5a11d992806185135211b4f899be03dcf6364036
---

若应用通过[setWindowLayoutFullScreen()](../harmonyos-references/arkts-apis-window-window.md#setwindowlayoutfullscreen9)接口设置窗口布局，建议调用[getWindowAvoidArea()](../harmonyos-references/arkts-apis-window-window.md#getwindowavoidarea9)和[on('avoidAreaChange')](../harmonyos-references/arkts-apis-window-window.md#onavoidareachange9)获取和动态监听避让区域的变更信息，使页面布局根据避让区域信息进行动态调整。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@cross-device-app-dev/immersive-effect-check": "suggestion"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. // EntryAbility.ets
2. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
3. import { window } from '@kit.ArkUI';
4. import { BusinessError } from '@kit.BasicServicesKit';
5. export default class EntryAbility extends UIAbility {
6. // ...
7. onWindowStageCreate(windowStage: window.WindowStage): void {
8. windowStage.loadContent('pages/Index', (err, data) => {
9. if (err.code) {
10. return;
11. }
12. let windowClass: window.Window = windowStage.getMainWindowSync(); // Obtain the main window of the application.
13. // 1. 设置窗口全屏.
14. let isLayoutFullScreen = true;
15. windowClass.setWindowLayoutFullScreen(isLayoutFullScreen).then(() => {
16. console.info('Succeeded in setting the window layout to full-screen mode.');
17. }).catch((err: BusinessError) => {
18. console.error('Failed to set the window layout to full-screen mode. Cause:' + JSON.stringify(err));
19. });

21. // 2. 获取避让区域.
22. let type = window.AvoidAreaType.TYPE_NAVIGATION_INDICATOR; // Here a navigation bar is used as an example.
23. let avoidArea = windowClass.getWindowAvoidArea(type);
24. let bottomRectHeight = avoidArea.bottomRect.height; // Obtain the height of the navigation area.
25. AppStorage.setOrCreate('bottomRectHeight', bottomRectHeight);
26. type = window.AvoidAreaType.TYPE_SYSTEM; // The status bar is used as an example.
27. avoidArea = windowClass.getWindowAvoidArea(type);
28. let topRectHeight = avoidArea.topRect.height; // Obtain the height of the status bar area.
29. AppStorage.setOrCreate('topRectHeight', topRectHeight);
30. // 3. Register a listening function to dynamically obtain the data of the avoid area.
31. windowClass.on('avoidAreaChange', (data) => {
32. if (data.type === window.AvoidAreaType.TYPE_SYSTEM) {
33. let topRectHeight = data.area.topRect.height;
34. AppStorage.setOrCreate('topRectHeight', topRectHeight);
35. } else if (data.type == window.AvoidAreaType.TYPE_NAVIGATION_INDICATOR) {
36. let bottomRectHeight = data.area.bottomRect.height;
37. AppStorage.setOrCreate('bottomRectHeight', bottomRectHeight);
38. }
39. });
40. });
41. }
42. }
```

## 反例

```
1. // EntryAbility.ets
2. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
3. import { window } from '@kit.ArkUI';
4. import { BusinessError } from '@kit.BasicServicesKit';
5. export default class EntryAbility extends UIAbility {
6. // ...
7. onWindowStageCreate(windowStage: window.WindowStage): void {
8. windowStage.loadContent('pages/Index', (err, data) => {
9. if (err.code) {
10. return;
11. }
12. let windowClass: window.Window = windowStage.getMainWindowSync(); // Obtain the main window of the application.
13. // 只设置窗口全屏.
14. let isLayoutFullScreen = true;
15. windowClass.setWindowLayoutFullScreen(isLayoutFullScreen).then(() => {
16. console.info('Succeeded in setting the window layout to full-screen mode.');
17. }).catch((err: BusinessError) => {
18. console.error('Failed to set the window layout to full-screen mode. Cause:' + JSON.stringify(err));
19. });
20. });
21. }
22. }
```

## 规则集

```
1. plugin:@cross-device-app-dev/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
