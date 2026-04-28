---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/speech-windowmanager
title: WindowManager（窗口管理）
breadcrumb: API参考 > AI > Speech Kit（场景化语音服务） > ArkTS API > WindowManager（窗口管理）
category: harmonyos-references
scraped_at: 2026-04-28T08:19:13+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:26c7df0e2ffe04c5a557863a4668a130ea21aaf1baf9a8ef4b616f4b035507a8
---

朗读控件的窗口管理类。

**起始版本：** 5.0.0(12)

## 导入模块

PhonePC/2in1Tablet

```
1. import { WindowManager } from '@kit.SpeechKit';
```

## setWindowStage

PhonePC/2in1Tablet

static setWindowStage(windowStage: window.WindowStage): void

设置窗口管理器，在EntryAbility的onWindowStageCreate方法中调用，否则调用[init](speech-textreader-api.md#init)初始化朗读控件将会失败。更多和设置EntryAbility相关的内容，请见[UIAbility组件生命周期](../harmonyos-guides/uiability-lifecycle.md)。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**设备行为差异：** 该接口在PC/2in1中可正常调用，在其他设备类型中无效果。

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| windowStage | [window.WindowStage](arkts-apis-window-windowstage.md) | 是 | 窗口管理器。管理各个基本窗口单元，即[Window](arkts-apis-window-window.md)实例。 |

**示例：**

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { window } from '@kit.ArkUI';
4. import { WindowManager } from '@kit.SpeechKit';

6. export default class EntryAbility extends UIAbility {
7. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
8. hilog.info(0x0000, 'testTag', 'Ability onCreate');
9. }

11. onDestroy(): void {
12. hilog.info(0x0000, 'testTag', 'Ability onDestroy');
13. }

15. onWindowStageCreate(windowStage: window.WindowStage): void {
16. hilog.info(0x0000, 'testTag', 'Ability onWindowStageCreate');
17. WindowManager.setWindowStage(windowStage);

19. windowStage.loadContent('pages/Index', (err, data) => {
20. if (err) {
21. hilog.error(0x0000, 'testTag', `Failed to load the content. Code: ${err.code}, message: ${err.message}.`);
22. return;
23. }
24. hilog.info(0x0000, 'testTag', `Succeeded in loading the content. Data: ${JSON.stringify(data)}.` );
25. });
26. }

28. onWindowStageDestroy(): void {
29. hilog.info(0x0000, 'testTag', 'Ability onWindowStageDestroy');
30. }

32. onForeground(): void {
33. hilog.info(0x0000, 'testTag', 'Ability onForeground');
34. }

36. onBackground(): void {
37. hilog.info(0x0000, 'testTag', 'Ability onBackground');
38. }
39. }
```

## getWindowStage

PhonePC/2in1Tablet

static getWindowStage(): window.WindowStage

获取窗口管理器。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [window.WindowStage](arkts-apis-window-windowstage.md) | 窗口管理器。管理各个基本窗口单元，即[Window](arkts-apis-window-window.md)实例。 |

**示例：**

```
1. import { WindowManager } from '@kit.SpeechKit';

3. try {
4. let windowManager = WindowManager.getWindowStage()
5. console.info(`TextReader succeeded in getting windowStage.`)
6. } catch (e) {
7. console.error(`TextReader failed to get windowStage. Code: ${e.code}, message: ${e.message}.`)
8. }
```
