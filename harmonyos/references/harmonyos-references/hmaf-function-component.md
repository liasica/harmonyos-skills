---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/hmaf-function-component
title: FunctionComponent（功能组件）
breadcrumb: API参考 > AI > Agent Framework Kit（智能体框架服务） > ArkTS组件 > FunctionComponent（功能组件）
category: harmonyos-references
scraped_at: 2026-04-28T08:18:47+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1a2b89845a170a968bed9f107fba7dc1fc05e7e1f8a80050e987a79d561e24c1
---

Agent Framework Kit（智能体框架服务）提供了拉起指定智能体的能力。

应用在[小艺开放平台](https://developer.huawei.com/consumer/cn/hag/hagindex.html?isInFrame=true&lang=zh_CN#/)上线智能体后，向用户提供应用+智能体组合的服务，让用户可以在适当的场景下通过Agent Framework Kit的UI控件能力主动拉起智能体。配置智能体请参考[快速创建智能体](../service/quick-start-0000002469548009.md)。

**起始版本：** 6.0.0(20)

## 导入模块

PhoneTablet

```
1. import { AgentController, BaseOptions, FunctionController, FunctionOptions, ButtonType, FunctionComponent } from '@kit.AgentFrameworkKit';
```

## FunctionComponent

PhoneTablet

Agent功能组件，可以实现拉起智能体功能。

**装饰器类型：** @Component

**元服务API：** 从版本6.0.1(21)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Agent.AgentKit

**起始版本：** 6.0.0(20)

**参数：**

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| agentId | string | 是 | - | Agent ID，Agent的唯一标识，[创建智能体](../service/quick-start-0000002469548009.md)时获取。智能体创建成功后，可在智能体配置页面的网址链接中获取。  长度限制1~64位字符。 |
| onError | [ErrorCallback](js-apis-base.md#errorcallback) | 是 | - | 错误回调函数。 |
| options | [FunctionOptions](hmaf-function-component.md#functionoptions) | 否 | - | Function组件初始化可选参数。 |
| controller | [FunctionController](hmaf-function-component.md#functioncontroller) | 否 | - | Function组件控制器。默认为undefined。 |

说明

该组件的所有参数均为初始化配置项，仅在组件实例化时生效，运行过程中修改参数值无法实现动态更新，若需调整参数请重新初始化组件。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](hmaf-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1022400010 | Parameter error. |
| 1022400014 | Internal error. |

**示例：**

```
1. import { BusinessError } from "@kit.BasicServicesKit";
2. import { hilog } from "@kit.PerformanceAnalysisKit";
3. import { FunctionComponent } from '@kit.AgentFrameworkKit';

5. @Entry
6. @Component
7. struct FunctionExample {
8. private agentId: string = 'agentproxy65481da1fa2293a8482d45'; // 智能体对应的agentid，由小艺智能体平台在创建智能体时指定

10. build() {
11. Column() {
12. FunctionComponent({
13. agentId: this.agentId,
14. onError: (err: BusinessError) => {
15. hilog.error(0x0001, 'FunctionExample', `err code: ${err.code}, message: ${err.message}`)
16. },
17. options: {
18. title: '智能创建',
19. queryText: '创建一个新的模式',
20. isShowShadow: true
21. }
22. })
23. }
24. }
25. }
```

## AgentController

PhoneTablet

Agent Framework Kit控件通用控制器。

**元服务API：** 从版本6.0.1(21)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Agent.AgentKit

**起始版本：** 6.0.0(20)

### isAgentSupport

PhoneTablet

isAgentSupport(context: common.UIAbilityContext, agentId: string): Promise<boolean>

查询Agent是否可用。若可用，返回Agent信息。使用Promise异步回调。

**元服务API：** 从版本6.0.1(21)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Agent.AgentKit

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.UIAbilityContext](js-apis-app-ability-common.md#uiabilitycontext) | 是 | 当前上下文环境。 |
| agentId | string | 是 | Agent ID，Agent的唯一标识，[创建智能体](../service/quick-start-0000002469548009.md)时获取。  长度限制1~64位字符。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，agentId是否有效，Agent功能是否正常。  true：agentId有效且Agent功能支持。  false：agentId无效或者Agent功能不支持。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](hmaf-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1022400010 | Parameter error. |
| 1022400011 | Privacy agreement not accepted. |
| 1022400012 | HUAWEI ID not signed in. |
| 1022400013 | Internet error. |
| 1022400014 | Internal error. |

**示例：**

```
1. import { BusinessError } from "@kit.BasicServicesKit";
2. import { hilog } from "@kit.PerformanceAnalysisKit";
3. import { common } from "@kit.AbilityKit";
4. import { FunctionComponent, FunctionController } from '@kit.AgentFrameworkKit';

6. @Entry
7. @Component
8. struct AgentDemo {
9. private functionController: FunctionController = new FunctionController()
10. private agentId: string = 'agentproxy65481da1fa2293a8482d45'; // 智能体对应的agentid，由小艺智能体平台在创建智能体时指定

12. @State isAgentSupport: boolean = false;

14. aboutToAppear() {
15. void this.checkAgentSupport()
16. }

18. async checkAgentSupport() {
19. try {
20. let context = this.getUIContext()?.getHostContext() as common.UIAbilityContext;
21. this.isAgentSupport = await this.functionController.isAgentSupport(context, this.agentId)
22. } catch (err) {
23. hilog.error(0x0001, 'AgentExample', `err code: ${err.code}, message: ${err.message}`)
24. }
25. }
26. build() {
27. Column() {
28. // 若使用该方法判断是否加载，请确保agentId可用
29. if (this.isAgentSupport) {
30. FunctionComponent({
31. agentId: this.agentId,
32. onError: (err: BusinessError) => {
33. hilog.error(0x0001, 'AgentExample', `err: ${JSON.stringify(err)}, message: ${err.message}`)
34. },
35. options: {
36. title: '智能创建',
37. queryText: '创建一个新的模式',
38. isShowShadow: true
39. }
40. })
41. }
42. }
43. }
44. }
```

### on('agentDialogOpened')

PhoneTablet

on(type: 'agentDialogOpened', callback: Callback<void>): void

监听智能体对话框打开事件。

**元服务API：** 从版本6.0.1(21)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Agent.AgentKit

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 值为'agentDialogOpened'，监听智能体对话框打开事件。 |
| callback | Callback<void> | 是 | callback回调函数。 |

**示例：**

```
1. import { BusinessError } from "@kit.BasicServicesKit";
2. import { hilog } from "@kit.PerformanceAnalysisKit";
3. import { FunctionComponent, FunctionController } from '@kit.AgentFrameworkKit';

5. @Entry
6. @Component
7. struct AgentDemo{
8. private controller: FunctionController = new FunctionController();
9. private agentId: string = 'agentproxy65481da1fa2293a8482d45'; // 智能体对应的agentid，由小艺智能体平台在创建智能体时指定

11. aboutToAppear() {
12. this.controller?.on('agentDialogOpened', this.onAgentOpenedCallback)
13. this.controller?.on('agentDialogClosed', this.onAgentClosedCallback)
14. }
15. onAgentOpenedCallback = () => {
16. hilog.info(0x0001, 'AgentExample', 'agent dialog opened callback')
17. }
18. onAgentClosedCallback = () => {
19. hilog.info(0x0001, 'AgentExample', 'agent dialog closed callback')
20. }
21. aboutToDisappear() {
22. this.controller?.off('agentDialogOpened')
23. this.controller?.off('agentDialogClosed')
24. }
25. build() {
26. Column() {
27. FunctionComponent({
28. agentId: this.agentId,
29. onError: (err: BusinessError) => {
30. hilog.error(0x0001, 'AgentExample', `err: ${JSON.stringify(err)}, message: ${err.message}`)
31. },
32. options: {
33. title: '智能创建',
34. queryText: '创建一个新的模式',
35. isShowShadow: true
36. },
37. controller: this.controller
38. })
39. }
40. }
41. }
```

### off('agentDialogOpened')

PhoneTablet

off(type: 'agentDialogOpened', callback?: Callback<void>): void

取消智能体对话框打开事件的监听。

**元服务API：** 从版本6.0.1(21)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Agent.AgentKit

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 值为 'agentDialogOpened'，取消智能体对话框打开事件的监听。 |
| callback | Callback<void> | 否 | 需要取消注册的回调函数，需与订阅时传入的回调函数是同一个。若无此参数，则取消注册所有的回调函数。 |

**示例：**

```
1. import { BusinessError } from "@kit.BasicServicesKit";
2. import { hilog } from "@kit.PerformanceAnalysisKit";
3. import { FunctionComponent, FunctionController } from '@kit.AgentFrameworkKit';

5. @Entry
6. @Component
7. struct AgentDemo{
8. private controller: FunctionController = new FunctionController();
9. private agentId: string = 'agentproxy65481da1fa2293a8482d45'; // 智能体对应的agentid，由小艺智能体平台在创建智能体时指定

11. aboutToAppear() {
12. this.controller?.on('agentDialogOpened', this.onAgentOpenedCallback)
13. this.controller?.on('agentDialogClosed', this.onAgentClosedCallback)
14. }
15. onAgentOpenedCallback = () => {
16. hilog.info(0x0001, 'AgentExample', 'agent dialog opened callback')
17. }
18. onAgentClosedCallback = () => {
19. hilog.info(0x0001, 'AgentExample', 'agent dialog closed callback')
20. }
21. aboutToDisappear() {
22. this.controller?.off('agentDialogOpened')
23. this.controller?.off('agentDialogClosed')
24. }
25. build() {
26. Column() {
27. FunctionComponent({
28. agentId: this.agentId,
29. onError: (err: BusinessError) => {
30. hilog.error(0x0001, 'AgentExample', `err: ${JSON.stringify(err)}, message: ${err.message}`)
31. },
32. options: {
33. title: '智能创建',
34. queryText: '创建一个新的模式',
35. isShowShadow: true
36. },
37. controller: this.controller
38. })
39. }
40. }
41. }
```

### on('agentDialogClosed')

PhoneTablet

on(type: 'agentDialogClosed', callback: Callback<void>): void

监听智能体对话框关闭事件。

**元服务API：** 从版本6.0.1(21)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Agent.AgentKit

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 值为'agentDialogClosed'，监听智能体对话框关闭事件。 |
| callback | Callback<void> | 是 | callback回调函数。 |

**示例：**

```
1. import { BusinessError } from "@kit.BasicServicesKit";
2. import { hilog } from "@kit.PerformanceAnalysisKit";
3. import { FunctionComponent, FunctionController } from '@kit.AgentFrameworkKit';

5. @Entry
6. @Component
7. struct AgentDemo{
8. private controller: FunctionController = new FunctionController();
9. private agentId: string = 'agentproxy65481da1fa2293a8482d45'; // 智能体对应的agentid，由小艺智能体平台在创建智能体时指定

11. aboutToAppear() {
12. this.controller?.on('agentDialogOpened', this.onAgentOpenedCallback)
13. this.controller?.on('agentDialogClosed', this.onAgentClosedCallback)
14. }
15. onAgentOpenedCallback = () => {
16. hilog.info(0x0001, 'AgentExample', 'agent dialog opened callback')
17. }
18. onAgentClosedCallback = () => {
19. hilog.info(0x0001, 'AgentExample', 'agent dialog closed callback')
20. }
21. aboutToDisappear() {
22. this.controller?.off('agentDialogOpened')
23. this.controller?.off('agentDialogClosed')
24. }
25. build() {
26. Column() {
27. FunctionComponent({
28. agentId: this.agentId,
29. onError: (err: BusinessError) => {
30. hilog.error(0x0001, 'AgentExample', `err: ${JSON.stringify(err)}, message: ${err.message}`)
31. },
32. options: {
33. title: '智能创建',
34. queryText: '创建一个新的模式',
35. isShowShadow: true
36. },
37. controller: this.controller
38. })
39. }
40. }
41. }
```

### off('agentDialogClosed')

PhoneTablet

off(type: 'agentDialogClosed', callback?: Callback<void>): void

取消智能体对话框关闭事件的监听。

**元服务API：** 从版本6.0.1(21)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Agent.AgentKit

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 值为 'agentDialogClosed'，取消智能体对话框关闭事件的监听。 |
| callback | Callback<void> | 否 | 需要取消注册的回调函数，需与订阅时传入的回调函数是同一个。若不传入此参数，则取消注册所有的回调函数。 |

**示例：**

```
1. import { BusinessError } from "@kit.BasicServicesKit";
2. import { hilog } from "@kit.PerformanceAnalysisKit";
3. import { FunctionComponent, FunctionController } from '@kit.AgentFrameworkKit';

5. @Entry
6. @Component
7. struct AgentDemo{
8. private controller: FunctionController = new FunctionController();
9. private agentId: string = 'agentproxy65481da1fa2293a8482d45'; // 智能体对应的agentid，由小艺智能体平台在创建智能体时指定

11. aboutToAppear() {
12. this.controller?.on('agentDialogOpened', this.onAgentOpenedCallback)
13. this.controller?.on('agentDialogClosed', this.onAgentClosedCallback)
14. }
15. onAgentOpenedCallback = () => {
16. hilog.info(0x0001, 'AgentExample', 'agent dialog opened callback')
17. }
18. onAgentClosedCallback = () => {
19. hilog.info(0x0001, 'AgentExample', 'agent dialog closed callback')
20. }
21. aboutToDisappear() {
22. this.controller?.off('agentDialogOpened')
23. this.controller?.off('agentDialogClosed')
24. }
25. build() {
26. Column() {
27. FunctionComponent({
28. agentId: this.agentId,
29. onError: (err: BusinessError) => {
30. hilog.error(0x0001, 'AgentExample', `err: ${JSON.stringify(err)}, message: ${err.message}`)
31. },
32. options: {
33. title: '智能创建',
34. queryText: '创建一个新的模式',
35. isShowShadow: true
36. },
37. controller: this.controller
38. })
39. }
40. }
41. }
```

## FunctionController

PhoneTablet

Function组件控制器，用于与Function组件控制交互。预留接口，当前版本完全继承[AgentController](hmaf-function-component.md#agentcontroller)的方法，无额外的实现。

**元服务API：** 从版本6.0.1(21)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Agent.AgentKit

**起始版本：** 6.0.0(20)

## BaseOptions

PhoneTablet

组件可选参数的基础对象。

**元服务API：** 从版本6.0.1(21)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Agent.AgentKit

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| title | string | 否 | 是 | 表示AgentFramework组件的标题。默认值为空。  [FunctionOptions](hmaf-function-component.md#functionoptions).buttonType按钮类型为ButtonType.CIRCLE时不体现。  当前只显示指定大小，宽度超过8个中文字符会进行省略。  字体大于1.75倍时默认最大显示两行。 |
| titleFontSize | number | 否 | 是 | 表示AgentFramework组件标题的字体大小。取值范围为[14, 16]，默认值为16。取值在范围外取默认值。 |
| iconSize | number | 否 | 是 | 表示AgentFramework组件图标的大小。取值范围为[16, 24]。  - 按钮类型为CIRCLE时，默认值为24。  - 按钮类型为CAPSULE时，默认值为20。  取值在范围外取默认值。 |
| iconColors | [ResourceColor[]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcecolor) | 否 | 是 | 表示图标颜色，当前仅支持设置一种颜色，不设置时，为默认渐变色图标。 |

## FunctionOptions

PhoneTablet

功能组件选项的定义。继承自[BaseOptions](hmaf-function-component.md#baseoptions)。

**元服务API：** 从版本6.0.1(21)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Agent.AgentKit

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| queryText | string | 否 | 是 | 使用功能组件的初始查询文本，默认值为空。 |
| controlSize | [ControlSize](ts-basic-components-button.md#controlsize11枚举说明) | 否 | 是 | 功能组件按钮的大小，默认值为ControlSize.NORMAL。 |
| buttonType | [ButtonType](hmaf-function-component.md#buttontype) | 否 | 是 | 功能组件的按钮类型。title属性为空或不传时默认值为ButtonType.CIRCLE，title属性不为空时默认值为ButtonType.CAPSULE。 |
| isShowShadow | boolean | 否 | 是 | 如果显示按钮的阴影，仅在 ButtonType.CAPSULE 胶囊类型时有效。默认值为false。  true：显示阴影。  false：不显示阴影。 |
| backgroundColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 显示背景板时，组件的背景颜色。  默认值为sys.color.comp\_background\_tertiary背景色。 |
| titleColors | [ResourceColor[]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcecolor) | 否 | 是 | 功能组件带文本时，文本的颜色，当前最多仅支持设置两种颜色。  - 设置两种颜色时为渐变色。  - 设置一种颜色时为设置颜色。  - 不设置时为默认渐变色文本。 |

## ButtonType

PhoneTablet

按钮类型的枚举值。

**元服务API：** 从版本6.0.1(21)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Agent.AgentKit

**起始版本：** 6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CIRCLE | 0 | 圆形按钮。 |
| CAPSULE | 1 | 胶囊按钮（圆角默认高度为一半）。  **说明：**  字体倍数小于1.75倍时，显示为胶囊按钮，大于或等于1.75倍时，显示为矩形倒角按钮。 |
| ICON\_ABOVE\_TITLE | 2 | 图标与标题为上下结构的胶囊按钮。  **起始版本：** 6.0.1(21) |
