---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-autofillmanager
title: @ohos.app.ability.autoFillManager (自动填充框架)
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > Stage模型能力的接口 > @ohos.app.ability.autoFillManager (自动填充框架)
category: harmonyos-references
scraped_at: 2026-04-28T07:58:16+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:de5aca430b65a2f560b52c568285aa4600ff58fad4a131394043caa82ac9dc3d
---

autoFillManager模块为应用提供账号、密码、地址、电话号码等用户信息的自动填充能力。

不同于页面切换时触发的系统自动保存功能，该功能需要由用户手动触发。例如用户在网站上输入了账号密码，并点击“保存”按钮，才能触发相应的自动保存操作。

说明

本模块首批接口从API version 11 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { autoFillManager } from '@kit.AbilityKit';
```

## AutoSaveCallback

PhonePC/2in1TabletTVWearable

当保存请求完成时所触发的回调接口。

### onSuccess

PhonePC/2in1TabletTVWearable

onSuccess(): void

当保存请求成功时，该回调被调用。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**示例：**

参见[AutoSaveCallback.onFailure](js-apis-app-ability-autofillmanager.md#onfailure)。

### onFailure

PhonePC/2in1TabletTVWearable

onFailure(): void

当保存请求失败时，该回调被调用。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**示例：**

```
1. // Index.ets, 含有账号、密码框等组件的页面
2. import { autoFillManager } from '@kit.AbilityKit';
3. import { UIContext } from '@kit.ArkUI';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. let uiContext = AppStorage.get<UIContext>("uiContext");
7. let callback: autoFillManager.AutoSaveCallback = {
8. onSuccess: () => {
9. console.info(`save request on success.`);
10. },
11. onFailure: () => {
12. console.error(`save request on failure.`);
13. }
14. };

16. @Entry
17. @Component
18. struct Index {
19. build() {
20. Button('requestAutoSave')
21. .onClick(() => {
22. try {
23. // 发起保存请求
24. autoFillManager.requestAutoSave(uiContext, callback);
25. } catch (error) {
26. console.error(`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}`);
27. }
28. })
29. }
30. }
```

说明

示例中从AppStorage中取得的UiContext为预先在EntryAbility（拉起此页面的Ability）中OnWindowStageCreate生命周期获得，并存储到AppStorage中，具体可参考[requestAutoSave](js-apis-app-ability-autofillmanager.md#autofillmanagerrequestautosave)。

## autoFillManager.requestAutoSave

PhonePC/2in1TabletTVWearable

requestAutoSave(context: UIContext, callback?: AutoSaveCallback): void

请求保存表单数据。使用callback异步回调。

如果当前表单没有提供表单切换的功能，可以通过此接口保存历史表单输入数据，保存请求完成时会触发该回调。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [UIContext](arkts-apis-uicontext-uicontext.md) | 是 | 将在其中执行保存操作的UI上下文。 |
| callback | [AutoSaveCallback](js-apis-app-ability-autofillmanager.md#autosavecallback) | 否 | 当保存请求完成时所触发的回调接口。 |

**错误码：**

以下错误码的详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes: 1. Get instance id failed; 2. Parse instance id failed; 3. The second parameter is not of type callback. |
| 16000050 | Internal error. |

**示例：**

```
1. // EntryAbility.ets
2. import { UIAbility, common } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { window, UIContext } from '@kit.ArkUI';
5. import { hilog } from '@kit.PerformanceAnalysisKit';

7. export default class EntryAbility extends UIAbility {
8. onWindowStageCreate(windowStage: window.WindowStage): void {
9. // Main window is created, set main page for this ability
10. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
11. let localStorageData: Record<string, string | common.UIAbilityContext> = {
12. 'message': "AutoFill Page",
13. 'context': this.context,
14. };
15. let storage = new LocalStorage(localStorageData);
16. windowStage.loadContent('pages/Index', storage, (err, data) => {
17. if (err && err.code) {
18. hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
19. return;
20. }
21. // Obtain the main window.
22. windowStage.getMainWindow((err: BusinessError, data: window.Window) => {
23. let errCode: number = err?.code;
24. if (errCode) {
25. console.error('Failed to obtain the main window. Cause: ' + JSON.stringify(err));
26. return;
27. }
28. console.info('Succeeded in obtaining the main window. Data: ' + JSON.stringify(data));
29. // get UIContext instance.
30. let uiContext: UIContext = windowStage.getMainWindowSync().getUIContext();
31. PersistentStorage.persistProp("uiContext", uiContext);
32. })
33. hilog.info(0x0000, 'testTag', 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
34. });
35. }
36. }
```

```
1. // Index.ets
2. import { autoFillManager } from '@kit.AbilityKit';
3. import { UIContext } from '@kit.ArkUI';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. @Entry
7. @Component
8. struct Index {
9. build() {
10. Row() {
11. Column() {
12. Text('Hello World')
13. .fontSize(50)
14. .fontWeight(FontWeight.Bold)
15. }

17. Button('requestAutoSave')
18. .onClick(() => {
19. let uiContext = AppStorage.get<UIContext>("uiContext");
20. console.info("uiContext: ", JSON.stringify(uiContext));
21. try {
22. // 发起保存请求
23. autoFillManager.requestAutoSave(uiContext, {
24. onSuccess: () => {
25. console.info(`save request on success.`);
26. },
27. onFailure: () => {
28. console.error(`save request on failure.`);
29. }
30. });
31. } catch (error) {
32. console.error(`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}`);
33. }
34. })
35. .width('100%')
36. }
37. .height('100%')
38. }
39. }
```
