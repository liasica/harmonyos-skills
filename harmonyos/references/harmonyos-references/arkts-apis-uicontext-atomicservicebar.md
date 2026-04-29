---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-atomicservicebar
title: Interface (AtomicServiceBar)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > @ohos.arkui.UIContext (UIContext) > Interface (AtomicServiceBar)
category: harmonyos-references
scraped_at: 2026-04-29T13:50:40+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:f4597a43cf24311798f658bdfb0affeaac4df691392419a6432b933389046c97
---

提供设置元服务menuBar的属性。

说明

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Interface首批接口从API version 11开始支持。
* 以下接口需要先使用UIContext中的[getAtomicServiceBar](arkts-apis-uicontext-uicontext.md#getatomicservicebar11)方法获取到AtomicServiceBar对象，再通过该对象调用对应方法。
* 从API version 12开始元服务menuBar样式变更，以下接口将失效。

## setVisible11+

PhonePC/2in1TabletTVWearable

setVisible(visible: boolean): void

通过该方法设置元服务menuBar是否可见。

说明

从API version 12开始，元服务menuBar默认隐藏并以悬浮按钮替代。**在元服务中调用setVisible()时，visible参数将被忽略，无法实现menuBar的显示或隐藏。**

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| visible | boolean | 是 | 元服务menuBar是否可见。true表示设置menuBar可见，false表示设置menuBar不可见。 |

**示例：**

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { UIContext, AtomicServiceBar, window } from '@kit.ArkUI';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. export default class EntryAbility extends UIAbility {
6. onWindowStageCreate(windowStage: window.WindowStage) {
7. // Main window is created, set main page for this ability
8. hilog.info(0x0000, 'testTag', 'Ability onWindowStageCreate');
9. windowStage.loadContent('pages/Index', (err, data) => {
10. let uiContext: UIContext = windowStage.getMainWindowSync().getUIContext();
11. let atomicServiceBar: Nullable<AtomicServiceBar> = uiContext.getAtomicServiceBar();
12. if (atomicServiceBar != undefined) {
13. hilog.info(0x0000, 'testTag', 'Get AtomicServiceBar Successfully.');
14. atomicServiceBar.setVisible(false);
15. } else {
16. hilog.info(0x0000, 'testTag', 'Get AtomicServiceBar failed.');
17. }
18. });
19. }
20. }
```

## setBackgroundColor11+

PhonePC/2in1TabletTVWearable

setBackgroundColor(color:Nullable<Color | number | string>): void

通过该方法设置元服务menuBar的背景颜色。

说明

从API version 12开始，元服务menuBar背景默认隐藏。**在元服务中调用setBackgroundColor()时，color参数将被忽略，无法设置menuBar的背景颜色。**

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | Nullable<[Color](ts-appendix-enums.md#color) | number | string> | 是 | 通过该方法设置元服务menuBar的背景颜色，undefined代表使用默认颜色。number为HEX格式颜色，支持rgb或者argb，示例：0xffffff。string为rgb或者argb格式颜色，示例：'#ffffff'。 |

**示例：**

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { UIContext, AtomicServiceBar, window } from '@kit.ArkUI';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. export default class EntryAbility extends UIAbility {
6. onWindowStageCreate(windowStage: window.WindowStage) {
7. // Main window is created, set main page for this ability
8. hilog.info(0x0000, 'testTag', 'Ability onWindowStageCreate');
9. windowStage.loadContent('pages/Index', (err, data) => {
10. let uiContext: UIContext = windowStage.getMainWindowSync().getUIContext();
11. let atomicServiceBar: Nullable<AtomicServiceBar> = uiContext.getAtomicServiceBar();
12. if (atomicServiceBar != undefined) {
13. hilog.info(0x0000, 'testTag', 'Get AtomicServiceBar Successfully.');
14. atomicServiceBar.setBackgroundColor(0x88888888);
15. } else {
16. hilog.info(0x0000, 'testTag', 'Get AtomicServiceBar failed.');
17. }
18. });
19. }
20. }
```

## setTitleContent11+

PhonePC/2in1TabletTVWearable

setTitleContent(content:string): void

通过该方法设置元服务menuBar的标题内容。

说明

从API version 12开始，元服务menuBar标题默认隐藏。**在元服务中调用setTitleContent()时，content参数将被忽略，无法设置menuBar的标题内容。**

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| content | string | 是 | 元服务menuBar中的标题内容。 |

**示例：**

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { UIContext, AtomicServiceBar, window } from '@kit.ArkUI';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. export default class EntryAbility extends UIAbility {
6. onWindowStageCreate(windowStage: window.WindowStage) {
7. // Main window is created, set main page for this ability
8. hilog.info(0x0000, 'testTag', 'Ability onWindowStageCreate');
9. windowStage.loadContent('pages/Index', (err, data) => {
10. let uiContext: UIContext = windowStage.getMainWindowSync().getUIContext();
11. let atomicServiceBar: Nullable<AtomicServiceBar> = uiContext.getAtomicServiceBar();
12. if (atomicServiceBar != undefined) {
13. hilog.info(0x0000, 'testTag', 'Get AtomicServiceBar Successfully.');
14. atomicServiceBar.setTitleContent('text2');
15. } else {
16. hilog.info(0x0000, 'testTag', 'Get AtomicServiceBar failed.');
17. }
18. });
19. }
20. }
```

## setTitleFontStyle11+

PhonePC/2in1TabletTVWearable

setTitleFontStyle(font:FontStyle):void

通过该方法设置元服务menuBar的字体样式。

说明

从API version 12开始，元服务menuBar标题默认隐藏。**在元服务中调用setTitleFontStyle()时，font参数将被忽略，无法设置menuBar标题的字体样式，例如斜体显示。**

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| font | [FontStyle](ts-appendix-enums.md#fontstyle) | 是 | 元服务menuBar中的字体样式。 |

**示例：**

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { UIContext, AtomicServiceBar, window } from '@kit.ArkUI';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. export default class EntryAbility extends UIAbility {
6. onWindowStageCreate(windowStage: window.WindowStage) {
7. // Main window is created, set main page for this ability
8. hilog.info(0x0000, 'testTag', 'Ability onWindowStageCreate');
9. windowStage.loadContent('pages/Index', (err, data) => {
10. let uiContext: UIContext = windowStage.getMainWindowSync().getUIContext();
11. let atomicServiceBar: Nullable<AtomicServiceBar> = uiContext.getAtomicServiceBar();
12. if (atomicServiceBar != undefined) {
13. hilog.info(0x0000, 'testTag', 'Get AtomicServiceBar Successfully.');
14. atomicServiceBar.setTitleFontStyle(FontStyle.Normal);
15. } else {
16. hilog.info(0x0000, 'testTag', 'Get AtomicServiceBar failed.');
17. }
18. });
19. }
20. }
```

## setIconColor11+

PhonePC/2in1TabletTVWearable

setIconColor(color:Nullable<Color | number | string>): void

通过该方法设置元服务图标的颜色。

说明

从API version 12开始，元服务menuBar默认隐藏并以悬浮按钮替代。**在元服务中调用setIconColor()时，color参数将被忽略，无法设置menuBar图标颜色。**

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | Nullable<[Color](ts-appendix-enums.md#color) | number | string> | 是 | 元服务图标的颜色，undefined代表使用默认颜色。number为HEX格式颜色，支持rgb或者argb，示例：0xffffff。string为rgb或者argb格式颜色，示例：'#ffffff'。 |

**示例：**

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { UIContext, AtomicServiceBar, window } from '@kit.ArkUI';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. export default class EntryAbility extends UIAbility {
6. onWindowStageCreate(windowStage: window.WindowStage) {
7. // Main window is created, set main page for this ability
8. hilog.info(0x0000, 'testTag', 'Ability onWindowStageCreate');
9. windowStage.loadContent('pages/Index', (err, data) => {
10. let uiContext: UIContext = windowStage.getMainWindowSync().getUIContext();
11. let atomicServiceBar: Nullable<AtomicServiceBar> = uiContext.getAtomicServiceBar();
12. if (atomicServiceBar != undefined) {
13. hilog.info(0x0000, 'testTag', 'Get AtomicServiceBar Successfully.');
14. atomicServiceBar.setIconColor(0x12345678);
15. } else {
16. hilog.info(0x0000, 'testTag', 'Get AtomicServiceBar failed.');
17. }
18. });
19. }
20. }
```

## getBarRect15+

PhonePC/2in1TabletTVWearable

getBarRect(): Frame

获取元服务menuBar相对窗口的布局信息。

说明

布局信息包含了元服务menuBar的左右margin。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Frame](js-apis-arkui-graphics.md#frame) | 元服务menuBar的大小和位置。 |

**示例：**

```
1. import { AtomicServiceBar } from '@kit.ArkUI';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. @Entry
5. @Component
6. struct Index {
7. build() {
8. Button("getBarRect")
9. .onClick(() => {
10. let uiContext: UIContext = this.getUIContext();
11. let currentBar: Nullable<AtomicServiceBar> = uiContext.getAtomicServiceBar();
12. if (currentBar != undefined) {
13. let rect = currentBar.getBarRect();
14. hilog.info(0x0000, 'testTag', 'Get AtomicServiceBar Successfully. x:'
15. + rect.x + ' y:' + rect.y + ' width:' + rect.width + ' height:' + rect.height);
16. } else {
17. hilog.info(0x0000, 'testTag', 'Get AtomicServiceBar failed.');
18. }
19. })
20. }
21. }
```
