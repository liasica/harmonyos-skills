---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiextensioncontentsession
title: @ohos.app.ability.UIExtensionContentSession (UIExtensionAbility界面操作类)
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > Stage模型能力的接口 > @ohos.app.ability.UIExtensionContentSession (UIExtensionAbility界面操作类)
category: harmonyos-references
scraped_at: 2026-04-28T07:58:22+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:956a902cfbb6f468a922794974dceff3bda7679a4948fc4764dd60b46c8f1652
---

UIExtensionContentSession是[UIExtensionAbility](js-apis-app-ability-uiextensionability.md)组件的界面操作类，提供页面加载、设置宿主应用（UIExtensionAbility组件的拉起方）窗口隐私模式等功能。当宿主应用拉起指定的UIExtensionAbility组件时，系统创建UIExtensionContentSession对象，并通过[onSessionCreate](js-apis-app-ability-uiextensionability.md#onsessioncreate)回调传递给开发者。一个UIExtensionAbility组件对应一个UIExtensionContentSession对象，每个UIExtensionAbility组件的UIExtensionContentSession对象之间互不影响。

说明

本模块首批接口从API version 10 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { UIExtensionContentSession } from '@kit.AbilityKit';
```

## UIExtensionContentSession

PhonePC/2in1TabletTVWearable

UIExtensionAbility组件的界面操作类，提供页面加载、设置宿主应用窗口隐私模式等功能。

### loadContent

PhonePC/2in1TabletTVWearable

loadContent(path: string, storage?: LocalStorage): void

为[UIExtensionAbility](js-apis-app-ability-uiextensionability.md)组件加载页面，支持通过[LocalStorage](../harmonyos-guides/arkts-localstorage.md)传递状态属性给被加载的页面。该接口用于开发者在UIExtensionAbility组件的[onSessionCreate](js-apis-app-ability-uiextensionability.md#onsessioncreate)生命周期中加载页面。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 要加载的页面所在的路径，该路径通过[module.json5配置文件](../harmonyos-guides/module-configuration-file.md)中的[pages标签](../harmonyos-guides/module-configuration-file.md#pages标签)配置。 |
| storage | [LocalStorage](../harmonyos-guides/arkts-localstorage.md) | 否 | 页面级UI状态存储单元，开发者可通过该参数为加载的页面传递状态属性。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 16000050 | Internal error. |

**示例：**

```
1. // UIExtensionAbility组件不支持三方应用直接继承，故以派生类ShareExtensionAbility举例说明。
2. import { UIExtensionContentSession, ShareExtensionAbility, Want } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. export default class ShareExtAbility extends ShareExtensionAbility {
6. // ...

8. onSessionCreate(want: Want, session: UIExtensionContentSession): void {
9. try {
10. let storage: LocalStorage = new LocalStorage();
11. storage.setOrCreate('session', session);
12. session.loadContent('pages/Extension', storage);
13. } catch (error) {
14. let code = (error as BusinessError).code;
15. let message = (error as BusinessError).message;
16. console.error(`Failed to load content, code: ${code}, msg: ${message}`);
17. }
18. }

20. // ...
21. }
```

### loadContentByName18+

PhonePC/2in1TabletTVWearable

loadContentByName(name: string, storage?: LocalStorage): void

为[UIExtensionAbility](js-apis-app-ability-uiextensionability.md)组件加载[命名路由](../harmonyos-guides/arkts-routing.md#命名路由)页面，支持通过[LocalStorage](../harmonyos-guides/arkts-localstorage.md)传递状态属性给被加载的页面。该接口用于开发者在UIExtensionAbility组件的[onSessionCreate](js-apis-app-ability-uiextensionability.md#onsessioncreate)生命周期中加载命名路由页面。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 命名路由页面的名称。 |
| storage | [LocalStorage](../harmonyos-guides/arkts-localstorage.md) | 否 | 页面级UI状态存储单元，开发者可通过该参数为加载的页面传递状态属性。 |

**错误码：**

以下错误码详细介绍请参考[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 16000050 | Internal error. |

**示例：**

UIExtensionAbility组件的实现：

```
1. // UIExtensionAbility组件不支持三方应用直接继承，故以派生类ShareExtensionAbility举例说明。
2. import { UIExtensionContentSession, ShareExtensionAbility, Want } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import './pages/UIExtensionPage'; // 导入命名路由页面，示例代码以“./pages/UIExtensionPage.ets”文件为例，在实际代码开发过程中修改为真实路径和文件名称。

6. export default class ShareExtAbility extends ShareExtensionAbility {
7. // 其他生命周期和实现

9. onSessionCreate(want: Want, session: UIExtensionContentSession): void {
10. let storage: LocalStorage = new LocalStorage();
11. storage.setOrCreate('session', session);

13. let name: string = 'UIExtPage'; // 命名路由页面的名字。
14. try {
15. session.loadContentByName(name, storage);
16. } catch (error) {
17. let code = (error as BusinessError).code;
18. let message = (error as BusinessError).message;
19. console.error(`Failed to load content by name ${name}, code: ${code}, msg: ${message}`);
20. }
21. }

23. // 其他生命周期和实现
24. }
```

UIExtensionAbility组件加载的命名路由页面的实现：

```
1. // “./pages/UIExtensionPage.ets”文件的实现。
2. import { UIExtensionContentSession } from '@kit.AbilityKit';

4. @Entry({ routeName: 'UIExtPage' }) // 通过“routeName”定义命名路由页面的名字。
5. @Component
6. struct UIExtensionPage {
7. @State message: string = 'Hello world';
8. storage: LocalStorage | undefined = this.getUIContext().getSharedLocalStorage();
9. private session: UIExtensionContentSession | undefined = this.storage?.get<UIExtensionContentSession>('session');

11. build() {
12. Row() {
13. Column() {
14. Text(this.message)
15. .fontSize(20)
16. .fontWeight(FontWeight.Bold)
17. }
18. .width('100%')
19. }
20. .height('100%')
21. }
22. }
```

### terminateSelf

PhonePC/2in1TabletTVWearable

terminateSelf(callback: AsyncCallback<void>): void

销毁UIExtensionAbility组件自身，同时关闭对应的宿主应用窗口界面。使用callback异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当接口调用成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. import { UIExtensionContentSession } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry()
5. @Component
6. struct Index {
7. storage: LocalStorage | undefined = this.getUIContext().getSharedLocalStorage();
8. private session: UIExtensionContentSession | undefined =
9. this.storage?.get<UIExtensionContentSession>('session');

11. build() {
12. RelativeContainer() {
13. Button('TerminateSelf')
14. .onClick(() => {
15. this.session?.terminateSelf((err: BusinessError) => {
16. if (err) {
17. console.error(`Failed to terminate self, code: ${err.code}, msg: ${err.message}`);
18. return;
19. }
20. console.info(`Succeeded in terminating self.`);
21. });

23. this.storage?.clear();
24. })
25. }
26. .height('100%')
27. .width('100%')
28. }
29. }
```

### terminateSelf

PhonePC/2in1TabletTVWearable

terminateSelf(): Promise<void>

销毁UIExtensionAbility组件自身，同时关闭对应的宿主应用窗口界面。使用Promise异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**示例：**

```
1. import { UIExtensionContentSession } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry()
5. @Component
6. struct Index {
7. storage: LocalStorage | undefined = this.getUIContext().getSharedLocalStorage();
8. private session: UIExtensionContentSession | undefined =
9. this.storage?.get<UIExtensionContentSession>('session');

11. build() {
12. RelativeContainer() {
13. Button('TerminateSelf')
14. .onClick(() => {
15. this.session?.terminateSelf()
16. .then(() => {
17. console.info(`Succeeded in terminating self.`);
18. })
19. .catch((err: BusinessError) => {
20. console.error(`Failed to terminate self, code: ${err.code}, msg: ${err.message}`);
21. });

23. this.storage?.clear();
24. })
25. }
26. .height('100%')
27. .width('100%')
28. }
29. }
```

### terminateSelfWithResult

PhonePC/2in1TabletTVWearable

terminateSelfWithResult(parameter: AbilityResult, callback: AsyncCallback<void>): void

销毁UIExtensionAbility组件自身，关闭对应的宿主应用窗口界面，并将结果返回给宿主应用。使用callback异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| parameter | [AbilityResult](js-apis-inner-ability-abilityresult.md) | 是 | 返回给宿主应用的信息。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当接口调用成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. import { UIExtensionContentSession, common } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry()
5. @Component
6. struct Index {
7. storage: LocalStorage | undefined = this.getUIContext().getSharedLocalStorage();
8. private session: UIExtensionContentSession | undefined =
9. this.storage?.get<UIExtensionContentSession>('session');

11. build() {
12. RelativeContainer() {
13. Button('TerminateSelfWithResult')
14. .onClick(() => {
15. let abilityResult: common.AbilityResult = {
16. resultCode: 0,
17. want: {
18. bundleName: 'com.ohos.uiextensioncontentsession',
19. parameters: {
20. 'result': 123456
21. }
22. }
23. };

25. this.session?.terminateSelfWithResult(abilityResult, (err: BusinessError) => {
26. if (err) {
27. console.error(`Failed to terminate self with result, code: ${err.code}, msg: ${err.message}`);
28. return;
29. }
30. console.info(`Succeeded in terminating self with result.`);
31. });

33. this.storage?.clear();
34. })
35. }
36. .height('100%')
37. .width('100%')
38. }
39. }
```

### terminateSelfWithResult

PhonePC/2in1TabletTVWearable

terminateSelfWithResult(parameter: AbilityResult): Promise<void>

销毁UIExtensionAbility组件自身，关闭对应的宿主应用窗口界面，并将结果返回给宿主应用。使用Promise异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| parameter | [AbilityResult](js-apis-inner-ability-abilityresult.md) | 是 | 返回给宿主应用的信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. import { UIExtensionContentSession, common } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry()
5. @Component
6. struct Index {
7. storage: LocalStorage | undefined = this.getUIContext().getSharedLocalStorage();
8. private session: UIExtensionContentSession | undefined =
9. this.storage?.get<UIExtensionContentSession>('session');

11. build() {
12. RelativeContainer() {
13. Button('TerminateSelfWithResult')
14. .onClick(() => {
15. let abilityResult: common.AbilityResult = {
16. resultCode: 0,
17. want: {
18. bundleName: 'com.ohos.uiextensioncontentsession',
19. parameters: {
20. 'result': 123456
21. }
22. }
23. };

25. this.session?.terminateSelfWithResult(abilityResult)
26. .then(() => {
27. console.info(`Succeeded in terminating self with result.`);
28. })
29. .catch((err: BusinessError) => {
30. console.error(`Failed to terminate self with result, code: ${err.code}, msg: ${err.message}`);
31. });

33. this.storage?.clear();
34. })
35. }
36. .height('100%')
37. .width('100%')
38. }
39. }
```

### setWindowPrivacyMode

PhonePC/2in1TabletTVWearable

setWindowPrivacyMode(isPrivacyMode: boolean): Promise<void>

设置宿主应用窗口的隐私模式开启或关闭。设置为隐私模式的窗口，窗口内容将无法被截屏或录屏。使用Promise异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**需要权限**：ohos.permission.PRIVACY\_WINDOW

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isPrivacyMode | boolean | 是 | 表示是否开启隐私模式。true表示开启；false表示关闭。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call the interface. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. // UIExtensionAbility组件不支持三方应用直接继承，故以派生类ShareExtensionAbility举例说明。
2. import { UIExtensionContentSession, ShareExtensionAbility, Want } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. export default class ShareExtAbility extends ShareExtensionAbility {
6. // ...

8. onSessionCreate(want: Want, session: UIExtensionContentSession): void {
9. let isPrivacyMode: boolean = true;
10. try {
11. session.setWindowPrivacyMode(isPrivacyMode)
12. .then(() => {
13. console.info(`Succeeded in setting window to privacy mode.`);
14. })
15. .catch((err: BusinessError) => {
16. console.error(`Failed to set window to privacy mode, code: ${err.code}, msg: ${err.message}`);
17. });
18. } catch (e) {
19. let code = (e as BusinessError).code;
20. let msg = (e as BusinessError).message;
21. console.error(`Failed to set window to privacy mode, code: ${code}, msg: ${msg}`);
22. }
23. }

25. // ...
26. }
```

### setWindowPrivacyMode

PhonePC/2in1TabletTVWearable

setWindowPrivacyMode(isPrivacyMode: boolean, callback: AsyncCallback<void>): void

设置宿主应用窗口的隐私模式开启或关闭。设置为隐私模式的窗口，窗口内容将无法被截屏或录屏。使用callback异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**需要权限**：ohos.permission.PRIVACY\_WINDOW

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isPrivacyMode | boolean | 是 | 表示是否开启隐私模式。true表示开启；false表示关闭。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当设置成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call the interface. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. // UIExtensionAbility组件不支持三方应用直接继承，故以派生类ShareExtensionAbility举例说明。
2. import { UIExtensionContentSession, ShareExtensionAbility, Want } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. export default class ShareExtAbility extends ShareExtensionAbility {
6. // ...

8. onSessionCreate(want: Want, session: UIExtensionContentSession): void {
9. let isPrivacyMode: boolean = true;
10. try {
11. session.setWindowPrivacyMode(isPrivacyMode, (err: BusinessError) => {
12. if (err) {
13. console.error(`Failed to set window to privacy mode, code: ${err.code}, msg: ${err.message}`);
14. return;
15. }
16. console.info(`Succeeded in setting window to privacy mode.`);
17. });
18. } catch (e) {
19. let code = (e as BusinessError).code;
20. let msg = (e as BusinessError).message;
21. console.error(`Failed to set window to privacy mode, code: ${code}, msg: ${msg}`);
22. }
23. }

25. // ...
26. }
```

### startAbilityByType11+

PhonePC/2in1TabletTVWearable

startAbilityByType(type: string, wantParam: Record<string, Object>, abilityStartCallback: AbilityStartCallback, callback: AsyncCallback<void>): void

通过type隐式启动UIExtensionAbility。使用callback异步回调。仅支持处于前台的应用调用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | UIExtensionAbility组件类型，取值详见[通过startAbilityByType接口拉起垂类面板](../harmonyos-guides/start-intent-panel.md#匹配规则)。 |
| wantParam | Record<string, Object> | 是 | 表示启动UIExtensionAbility组件时传递的参数。 |
| abilityStartCallback | [AbilityStartCallback](js-apis-inner-application-abilitystartcallback.md) | 是 | 表示启动UIExtensionAbility组件的执行结果。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当接口调用成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 16000050 | Internal error. |

**示例：**

```
1. // UIExtensionAbility组件不支持三方应用直接继承，故以派生类ShareExtensionAbility举例说明。
2. import { UIExtensionContentSession, ShareExtensionAbility, Want, common } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. export default class ShareExtAbility extends ShareExtensionAbility {
6. // ...

8. onSessionCreate(want: Want, session: UIExtensionContentSession): void {
9. let wantParams: Record<string, Object> = {
10. 'sceneType': 1
11. };
12. let abilityStartCallback: common.AbilityStartCallback = {
13. onError: (code: number, name: string, message: string) => {
14. console.error(`onError, code: ${code}, name: ${name}, msg: ${message}`);
15. },
16. onResult: (result: common.AbilityResult) => {
17. console.info(`onResult, result: ${JSON.stringify(result)}`);
18. }
19. };

21. session.startAbilityByType('navigation', wantParams, abilityStartCallback, (err: BusinessError) => {
22. if (err) {
23. console.error(`Failed to startAbilityByType, code: ${err.code}, msg: ${err.message}`);
24. return;
25. }
26. console.info(`Succeeded in startAbilityByType`);
27. });
28. }

30. // ...
31. }
```

### startAbilityByType11+

PhonePC/2in1TabletTVWearable

startAbilityByType(type: string, wantParam: Record<string, Object>, abilityStartCallback: AbilityStartCallback): Promise<void>

通过type隐式启动UIExtensionAbility组件。使用Promise异步回调。仅支持处于前台的应用调用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | UIExtensionAbility组件类型，取值详见[通过startAbilityByType接口拉起垂类面板](../harmonyos-guides/start-intent-panel.md#匹配规则)。 |
| wantParam | Record<string, Object> | 是 | 表示启动UIExtensionAbility组件时传递的参数。 |
| abilityStartCallback | [AbilityStartCallback](js-apis-inner-application-abilitystartcallback.md) | 是 | 表示启动UIExtensionAbility组件的执行结果。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 16000050 | Internal error. |

**示例：**

```
1. // UIExtensionAbility组件不支持三方应用直接继承，故以派生类ShareExtensionAbility举例说明。
2. import { UIExtensionContentSession, ShareExtensionAbility, Want, common } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. export default class ShareExtAbility extends ShareExtensionAbility {
6. // ...

8. onSessionCreate(want: Want, session: UIExtensionContentSession): void {
9. let wantParams: Record<string, Object> = {
10. 'sceneType': 1
11. };
12. let abilityStartCallback: common.AbilityStartCallback = {
13. onError: (code: number, name: string, message: string) => {
14. console.error(`onError, code: ${code}, name: ${name}, msg: ${message}`);
15. },
16. onResult: (result: common.AbilityResult) => {
17. console.info(`onResult, result: ${JSON.stringify(result)}`);
18. }
19. };

21. session.startAbilityByType('test', wantParams, abilityStartCallback)
22. .then(() => {
23. console.info(`Succeeded in startAbilityByType`);
24. })
25. .catch((err: BusinessError) => {
26. console.error(`Failed to startAbilityByType, code: ${err.code}, msg: ${err.message}`);
27. });
28. }

30. // ...
31. }
```

### getUIExtensionWindowProxy12+

PhonePC/2in1TabletTVWearable

getUIExtensionWindowProxy(): uiExtension.WindowProxy

获取UIExtension窗口代理。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [uiExtension.WindowProxy](js-apis-arkui-uiextension.md#windowproxy) | UIExtensionAbility组件的宿主应用窗口代理。 |

**错误码：**

以下错误码详细介绍请参考[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 16000050 | Internal error. |

**示例：**

```
1. // Index.ets
2. import { UIExtensionContentSession } from '@kit.AbilityKit';
3. import { uiExtension } from '@kit.ArkUI';

5. @Entry()
6. @Component
7. struct Extension {
8. storage: LocalStorage | undefined = this.getUIContext().getSharedLocalStorage();
9. @State message: string = 'EmbeddedUIExtensionAbility Index';
10. private session: UIExtensionContentSession | undefined = this.storage?.get<UIExtensionContentSession>('session');
11. private extensionWindow: uiExtension.WindowProxy | undefined = this.session?.getUIExtensionWindowProxy();

13. aboutToAppear(): void {
14. this.extensionWindow?.on('windowSizeChange', (size) => {
15. console.info(`size = ${JSON.stringify(size)}`);
16. });
17. this.extensionWindow?.on('avoidAreaChange', (info) => {
18. console.info(`type = ${JSON.stringify(info.type)}, area = ${JSON.stringify(info.area)}`);
19. });
20. }

22. aboutToDisappear(): void {
23. this.extensionWindow?.off('windowSizeChange');
24. this.extensionWindow?.off('avoidAreaChange');
25. }

27. build() {
28. Column() {
29. Text(this.message)
30. .fontSize(20)
31. .fontWeight(FontWeight.Bold)
32. }
33. .width('100%')
34. }
35. }
```
