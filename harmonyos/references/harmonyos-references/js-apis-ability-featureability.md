---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-ability-featureability
title: @ohos.ability.featureAbility (FeatureAbility模块)
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > FA模型能力的接口 > @ohos.ability.featureAbility (FeatureAbility模块)
category: harmonyos-references
scraped_at: 2026-04-28T07:58:26+08:00
doc_updated_at: 2026-04-13
content_hash: sha256:3650950ac308c26e6d3150fa9afd2465c9d66043db81d49bdea5abebf2f8eaa6
---

FeatureAbility模块提供与用户进行交互的Ability的能力，包括启动新的Ability、停止Ability、获取dataAbilityHelper对象、获取当前Ability对应的窗口，连接断连Service等。

说明

本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在FA模型下使用。

## 使用限制

PhonePC/2in1TabletTVWearable

FeatureAbility模块的接口只能在Page类型的Ability中调用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { featureAbility } from '@kit.AbilityKit';
```

## featureAbility.startAbility

PhonePC/2in1TabletTVWearable

startAbility(parameter: StartAbilityParameter, callback: AsyncCallback<number>): void

启动新的Ability。使用callback异步回调。

说明

组件启动规则详见：[组件启动规则（FA模型）](../harmonyos-guides/component-startup-rules-fa.md)。

**模型约束**：此接口仅可在FA模型下使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| parameter | [StartAbilityParameter](js-apis-inner-ability-startabilityparameter.md) | 是 | 表示被启动的Ability。 |
| callback | AsyncCallback<number> | 是 | 回调函数。当启动Ability成功，err为undefined，data为0表示启动成功，data为其他表示启动失败；否则为错误对象。 |

**示例：**

```
1. import { featureAbility, wantConstant } from '@kit.AbilityKit';

3. featureAbility.startAbility(
4. {
5. want:
6. {
7. action: '',
8. entities: [''],
9. type: '',
10. flags: wantConstant.Flags.FLAG_AUTH_READ_URI_PERMISSION,
11. deviceId: '',
12. bundleName: 'com.example.myapplication',
13. /* FA模型中abilityName由package + Ability name组成 */
14. abilityName: 'com.example.myapplication.secondAbility',
15. uri: ''
16. },
17. },
18. (error, data) => {
19. if (error && error.code !== 0) {
20. console.error(`startAbility fail, error: ${JSON.stringify(error)}`);
21. } else {
22. console.info(`startAbility success, data: ${JSON.stringify(data)}`);
23. }
24. }
25. );
```

## featureAbility.startAbility

PhonePC/2in1TabletTVWearable

startAbility(parameter: StartAbilityParameter): Promise<number>

启动新的Ability。使用Promise异步回调。

说明

组件启动规则详见：[组件启动规则（FA模型）](../harmonyos-guides/component-startup-rules-fa.md)。

**模型约束**：此接口仅可在FA模型下使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| parameter | [StartAbilityParameter](js-apis-inner-ability-startabilityparameter.md) | 是 | 表示被启动的Ability。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。返回0表示启动成功，返回其他表示启动失败。 |

**示例：**

```
1. import { featureAbility, wantConstant } from '@kit.AbilityKit';

3. featureAbility.startAbility(
4. {
5. want:
6. {
7. action: 'ohos.want.action.home',
8. entities: ['entity.system.home'],
9. type: 'MIMETYPE',
10. flags: wantConstant.Flags.FLAG_AUTH_READ_URI_PERMISSION,
11. deviceId: '',
12. bundleName: 'com.example.myapplication',
13. /* FA模型中abilityName由package + Ability name组成 */
14. abilityName: 'com.example.myapplication.secondAbility',
15. uri: ''
16. },
17. }
18. ).then((data) => {
19. console.info(`startAbility data: ${JSON.stringify(data)}`);
20. });
```

## featureAbility.acquireDataAbilityHelper7+

PhonePC/2in1TabletTVWearable

acquireDataAbilityHelper(uri: string): DataAbilityHelper

获取dataAbilityHelper对象。

说明

组件启动规则详见：[组件启动规则（FA模型）](../harmonyos-guides/component-startup-rules-fa.md)。

跨应用访问dataAbility，对端应用需配置关联启动。

**模型约束**：此接口仅可在FA模型下使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 表示要打开的文件的路径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DataAbilityHelper](js-apis-inner-ability-dataabilityhelper.md) | 用来协助其他Ability访问DataAbility的工具类。 |

**示例：**

```
1. import { featureAbility } from '@kit.AbilityKit';

3. let dataAbilityHelper = featureAbility.acquireDataAbilityHelper(
4. 'dataability:///com.example.DataAbility'
5. );
```

## featureAbility.startAbilityForResult7+

PhonePC/2in1TabletTVWearable

startAbilityForResult(parameter: StartAbilityParameter, callback: AsyncCallback<AbilityResult>): void

启动一个Ability。使用callback异步回调。启动Ability后，存在如下几种情况：

* 正常情况下可通过调用[terminateSelfWithResult](js-apis-ability-featureability.md#featureabilityterminateselfwithresult7)接口使之终止并且返回结果给调用方。
* 异常情况下比如杀死Ability会返回异常信息给调用方, 异常信息中resultCode为-1。
* 如果被启动的Ability模式是单实例模式, 不同应用多次调用该接口启动这个Ability，当这个Ability调用[terminateSelfWithResult](js-apis-ability-featureability.md#featureabilityterminateselfwithresult7)接口使之终止时，只将正常结果返回给最后一个调用方, 其它调用方返回异常信息, 异常信息中resultCode为-1。

说明

组件启动规则详见：[组件启动规则（FA模型）](../harmonyos-guides/component-startup-rules-fa.md)。

**模型约束**：此接口仅可在FA模型下使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| parameter | [StartAbilityParameter](js-apis-inner-ability-startabilityparameter.md) | 是 | 表示被启动的Ability。 |
| callback | AsyncCallback<[AbilityResult](js-apis-inner-ability-abilityresult.md)> | 是 | 回调函数。当启动Ability成功，err为undefined，data为ability的启动结果；否则为错误对象。 |

**示例：**

```
1. import { featureAbility, wantConstant } from '@kit.AbilityKit';

3. featureAbility.startAbilityForResult(
4. {
5. want:
6. {
7. action: 'ohos.want.action.home',
8. entities: ['entity.system.home'],
9. type: 'MIMETYPE',
10. flags: wantConstant.Flags.FLAG_AUTH_READ_URI_PERMISSION,
11. deviceId: '',
12. bundleName: 'com.example.myapplication',
13. /* FA模型中abilityName由package + Ability name组成 */
14. abilityName: 'com.example.myapplication.secondAbility',
15. uri: ''
16. },
17. },
18. (error, data) => {
19. if (error && error.code !== 0) {
20. console.error(`startAbilityForResult fail, error: ${JSON.stringify(error)}`);
21. } else {
22. console.info(`startAbilityForResult success, data: ${JSON.stringify(data)}`);
23. }
24. }
25. );
```

## featureAbility.startAbilityForResult7+

PhonePC/2in1TabletTVWearable

startAbilityForResult(parameter: StartAbilityParameter): Promise<AbilityResult>

启动一个Ability。使用Promise异步回调。启动Ability后，存在如下几种情况：

* 正常情况下可通过调用[terminateSelfWithResult](js-apis-ability-featureability.md#featureabilityterminateselfwithresult7)接口使之终止并且返回结果给调用方。
* 异常情况下比如杀死Ability会返回异常信息给调用方, 异常信息中resultCode为-1。
* 如果被启动的Ability模式是单实例模式, 不同应用多次调用该接口启动这个Ability，当这个Ability调用[terminateSelfWithResult](js-apis-ability-featureability.md#featureabilityterminateselfwithresult7)接口使之终止时，只将正常结果返回给最后一个调用方, 其它调用方返回异常信息, 异常信息中resultCode为-1。

说明

组件启动规则详见：[组件启动规则（FA模型）](../harmonyos-guides/component-startup-rules-fa.md)。

**模型约束**：此接口仅可在FA模型下使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| parameter | [StartAbilityParameter](js-apis-inner-ability-startabilityparameter.md) | 是 | 表示被启动的Ability。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AbilityResult](js-apis-inner-ability-abilityresult.md)> | Promise对象，返回启动Ability的结果。 |

**示例：**

```
1. import { featureAbility, wantConstant } from '@kit.AbilityKit';

3. featureAbility.startAbilityForResult(
4. {
5. want:
6. {
7. action: 'ohos.want.action.home',
8. entities: ['entity.system.home'],
9. type: 'MIMETYPE',
10. flags: wantConstant.Flags.FLAG_AUTH_READ_URI_PERMISSION,
11. deviceId: '',
12. bundleName: 'com.example.myapplication',
13. /* FA模型中abilityName由package + Ability name组成 */
14. abilityName: 'com.example.myapplication.secondAbility',
15. uri: '',
16. parameters:
17. {
18. mykey0: 1111,
19. mykey1: [1, 2, 3],
20. mykey2: '[1, 2, 3]',
21. mykey3: 'xxxxxxxxxxxxxxxxxxxxxx',
22. mykey4: [1, 15],
23. mykey5: [false, true, false],
24. mykey6: ['aaaaaa', 'bbbbb', 'ccccccccccc'],
25. mykey7: true,
26. },
27. },
28. },
29. ).then((data) => {
30. console.info(`startAbilityForResult data: ${JSON.stringify(data)}`);
31. });
```

## featureAbility.terminateSelfWithResult7+

PhonePC/2in1TabletTVWearable

terminateSelfWithResult(parameter: AbilityResult, callback: AsyncCallback<void>): void

停止当前的Ability。使用callback异步回调。如果该Ability是通过调用[startAbilityForResult](js-apis-ability-featureability.md#featureabilitystartabilityforresult7)接口被拉起的，调用terminateSelfWithResult接口时会将结果返回给调用者，如果该Ability不是通过调用[startAbilityForResult](js-apis-ability-featureability.md#featureabilitystartabilityforresult7)接口被拉起的，调用terminateSelfWithResult接口时不会有结果返回给调用者。

**模型约束**：此接口仅可在FA模型下使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| parameter | [AbilityResult](js-apis-inner-ability-abilityresult.md) | 是 | 表示停止Ability之后返回的结果。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当停止当前Ability成功，err为undefined，否则为错误对象。 |

**示例：**

```
1. import { featureAbility, wantConstant } from '@kit.AbilityKit';

3. featureAbility.terminateSelfWithResult(
4. {
5. resultCode: 1,
6. want:
7. {
8. action: 'ohos.want.action.home',
9. entities: ['entity.system.home'],
10. type: 'MIMETYPE',
11. flags: wantConstant.Flags.FLAG_AUTH_READ_URI_PERMISSION,
12. deviceId: '',
13. bundleName: 'com.example.myapplication',
14. /* FA模型中abilityName由package + Ability name组成 */
15. abilityName: 'com.example.myapplication.secondAbility',
16. uri: '',
17. parameters: {
18. mykey0: 2222,
19. mykey1: [1, 2, 3],
20. mykey2: '[1, 2, 3]',
21. mykey3: 'ssssssssssssssssssssssssss',
22. mykey4: [1, 15],
23. mykey5: [false, true, false],
24. mykey6: ['qqqqq', 'wwwwww', 'aaaaaaaaaaaaaaaaa'],
25. mykey7: true,
26. }
27. },
28. },
29. (error) => {
30. console.error(`error: ${JSON.stringify(error)}`);
31. }
32. );
```

## featureAbility.terminateSelfWithResult7+

PhonePC/2in1TabletTVWearable

terminateSelfWithResult(parameter: AbilityResult): Promise<void>

停止当前的Ability。使用Promise异步回调。如果该Ability是通过调用[startAbilityForResult](js-apis-ability-featureability.md#featureabilitystartabilityforresult7)接口被拉起的，调用terminateSelfWithResult接口时会将结果返回给调用者，如果该Ability不是通过调用[startAbilityForResult](js-apis-ability-featureability.md#featureabilitystartabilityforresult7)接口被拉起的，调用terminateSelfWithResult接口时不会有结果返回给调用者。

**模型约束**：此接口仅可在FA模型下使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| parameter | [AbilityResult](js-apis-inner-ability-abilityresult.md) | 是 | 表示停止Ability之后返回的结果。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```
1. import { featureAbility, wantConstant } from '@kit.AbilityKit';

3. featureAbility.terminateSelfWithResult(
4. {
5. resultCode: 1,
6. want:
7. {
8. action: 'ohos.want.action.home',
9. entities: ['entity.system.home'],
10. type: 'MIMETYPE',
11. flags: wantConstant.Flags.FLAG_AUTH_READ_URI_PERMISSION,
12. deviceId: '',
13. bundleName: 'com.example.myapplication',
14. /* FA模型中abilityName由package + Ability name组成 */
15. abilityName: 'com.example.myapplication.secondAbility',
16. uri:'',
17. parameters: {
18. mykey0: 2222,
19. mykey1: [1, 2, 3],
20. mykey2: '[1, 2, 3]',
21. mykey3: 'ssssssssssssssssssssssssss',
22. mykey4: [1, 15],
23. mykey5: [false, true, false],
24. mykey6: ['qqqqq', 'wwwwww', 'aaaaaaaaaaaaaaaaa'],
25. mykey7: true,
26. }
27. },
28. }
29. ).then(() => {
30. console.info('==========================>terminateSelfWithResult=======================>');
31. });
```

## featureAbility.hasWindowFocus7+

PhonePC/2in1TabletTVWearable

hasWindowFocus(callback: AsyncCallback<boolean>): void

检查Ability的主窗口是否具有窗口焦点。使用callback异步回调。

**模型约束**：此接口仅可在FA模型下使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 回调函数。  如果此Ability当前具有视窗焦点，则返回true；否则返回false。 |

**示例：**

```
1. import { featureAbility } from '@kit.AbilityKit';

3. featureAbility.hasWindowFocus((error, data) => {
4. if (error && error.code !== 0) {
5. console.error(`hasWindowFocus fail, error: ${JSON.stringify(error)}`);
6. } else {
7. console.info(`hasWindowFocus success, data: ${JSON.stringify(data)}`);
8. }
9. });
```

## featureAbility.hasWindowFocus7+

PhonePC/2in1TabletTVWearable

hasWindowFocus(): Promise<boolean>

检查Ability的主窗口是否具有窗口焦点。使用Promise异步回调。

**模型约束**：此接口仅可在FA模型下使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。如果此Ability当前具有视窗焦点，则返回true；否则返回false。 |

**示例：**

```
1. import { featureAbility } from '@kit.AbilityKit';

3. featureAbility.hasWindowFocus().then((data) => {
4. console.info(`hasWindowFocus data: ${JSON.stringify(data)}`);
5. });
```

## featureAbility.getWant

PhonePC/2in1TabletTVWearable

getWant(callback: AsyncCallback<Want>): void

获取要拉起的Ability对应的Want。使用callback异步回调。

**模型约束**：此接口仅可在FA模型下使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[Want](js-apis-application-want.md)> | 是 | 回调函数，当获取要拉起的Ability对应的Want成功，err为undefined，data为当前Ability对应的Want；否则为错误对象。 |

**示例：**

```
1. import { featureAbility } from '@kit.AbilityKit';

3. featureAbility.getWant((error, data) => {
4. if (error && error.code !== 0) {
5. console.error(`getWant fail, error: ${JSON.stringify(error)}`);
6. } else {
7. console.info(`getWant success, data: ${JSON.stringify(data)}`);
8. }
9. });
```

## featureAbility.getWant

PhonePC/2in1TabletTVWearable

getWant(): Promise<Want>

获取要拉起的Ability对应的Want。使用Promise异步回调。

**模型约束**：此接口仅可在FA模型下使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Want](js-apis-application-want.md)> | Promise对象，返回want信息。 |

**示例：**

```
1. import { featureAbility } from '@kit.AbilityKit';

3. featureAbility.getWant().then((data) => {
4. console.info(`getWant data: ${JSON.stringify(data)}`);
5. });
```

## featureAbility.getContext

PhonePC/2in1TabletTVWearable

getContext(): Context

获取应用上下文。

**模型约束**：此接口仅可在FA模型下使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Context | 返回应用程序上下文。 |

**示例：**

```
1. import { featureAbility } from '@kit.AbilityKit';

3. let context = featureAbility.getContext();
4. context.getBundleName((error, data) => {
5. if (error && error.code !== 0) {
6. console.error(`getBundleName fail, error: ${JSON.stringify(error)}`);
7. } else {
8. console.info(`getBundleName success, data: ${JSON.stringify(data)}`);
9. }
10. });
```

## featureAbility.terminateSelf7+

PhonePC/2in1TabletTVWearable

terminateSelf(callback: AsyncCallback<void>): void

停止当前的Ability。使用callback异步回调。

**模型约束**：此接口仅可在FA模型下使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当停止当前的Ability成功，err为undefined，否则为错误对象。 |

**示例：**

```
1. import { featureAbility } from '@kit.AbilityKit';

3. featureAbility.terminateSelf(
4. (error) => {
5. console.error(`error: ${JSON.stringify(error)}`);
6. }
7. )
```

## featureAbility.terminateSelf7+

PhonePC/2in1TabletTVWearable

terminateSelf(): Promise<void>

停止当前的Ability。使用Promise异步回调。

**模型约束**：此接口仅可在FA模型下使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```
1. import { featureAbility } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. featureAbility.terminateSelf().then(() => {
5. console.info('==========================>terminateSelf=======================>');
6. }).catch((error: BusinessError) => {
7. console.error(`terminateSelf failed, error.code: ${error.code}, error.message: ${error.message}`);
8. });
```

## featureAbility.connectAbility7+

PhonePC/2in1TabletTVWearable

connectAbility(request: Want, options:ConnectOptions): number

将当前Ability与指定的ServiceAbility进行连接。

说明

组件启动规则详见：[组件启动规则（FA模型）](../harmonyos-guides/component-startup-rules-fa.md)。

跨应用连接serviceAbility，对端应用需配置关联启动。

**模型约束**：此接口仅可在FA模型下使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | [Want](js-apis-application-want.md) | 是 | 表示被连接的ServiceAbility。 |
| options | [ConnectOptions](js-apis-inner-ability-connectoptions.md) | 是 | 表示连接回调函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 连接的ServiceAbility的ID(ID从0开始自增，每连接成功一次ID加1)。 |

**示例：**

```
1. import { featureAbility } from '@kit.AbilityKit';
2. import { rpc } from '@kit.IPCKit';

4. let connectId = featureAbility.connectAbility(
5. {
6. deviceId: '',
7. bundleName: 'com.ix.ServiceAbility',
8. abilityName: 'com.ix.ServiceAbility.ServiceAbilityA',
9. },
10. {
11. onConnect: (element, remote) => {
12. console.info(`ConnectAbility onConnect remote is proxy: ${(remote instanceof rpc.RemoteProxy)}`);
13. },
14. onDisconnect: (element) => {
15. console.info(`ConnectAbility onDisconnect element.deviceId : ${element.deviceId}`);
16. },
17. onFailed: (code) => {
18. console.error(`featureAbilityTest ConnectAbility onFailed errCode : ${code}`);
19. },
20. },
21. );
```

## featureAbility.disconnectAbility7+

PhonePC/2in1TabletTVWearable

disconnectAbility(connection: number, callback:AsyncCallback<void>): void

断开与指定ServiceAbility的连接。使用callback异步回调。

**模型约束**：此接口仅可在FA模型下使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| connection | number | 是 | 表示断开连接的ServiceAbility的ID。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当断开与指定ServiceAbility的连接成功，err为undefined，否则为错误对象。 |

**示例：**

```
1. import { featureAbility } from '@kit.AbilityKit';
2. import { rpc } from '@kit.IPCKit';

4. let connectId = featureAbility.connectAbility(
5. {
6. bundleName: 'com.ix.ServiceAbility',
7. abilityName: 'com.ix.ServiceAbility.ServiceAbilityA',
8. },
9. {
10. onConnect: (element, remote) => {
11. console.info(`ConnectAbility onConnect remote is proxy: ${(remote instanceof rpc.RemoteProxy)}`);
12. },
13. onDisconnect: (element) => {
14. console.info(`ConnectAbility onDisconnect element.deviceId : ${element.deviceId}`);
15. },
16. onFailed: (code) => {
17. console.error(`featureAbilityTest ConnectAbility onFailed errCode : ${code}`);
18. },
19. },
20. );

22. featureAbility.disconnectAbility(connectId, (error) => {
23. if (error && error.code !== 0) {
24. console.error(`disconnectAbility fail, connectId: ${connectId}, error: ${JSON.stringify(error)}`);
25. } else {
26. console.info(`disconnectAbility success， connectId: ${connectId}`);
27. }
28. });
```

## featureAbility.disconnectAbility7+

PhonePC/2in1TabletTVWearable

disconnectAbility(connection: number): Promise<void>

断开与指定ServiceAbility的连接。使用Promise异步回调。

**模型约束**：此接口仅可在FA模型下使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| connection | number | 是 | 表示断开连接的ServiceAbility的ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```
1. import { featureAbility } from '@kit.AbilityKit';
2. import { rpc } from '@kit.IPCKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. let connectId = featureAbility.connectAbility(
6. {
7. bundleName: 'com.ix.ServiceAbility',
8. abilityName: 'com.ix.ServiceAbility.ServiceAbilityA',
9. },
10. {
11. onConnect: (element, remote) => {
12. console.info(`ConnectAbility onConnect remote is proxy: ${(remote instanceof rpc.RemoteProxy)}`);
13. },
14. onDisconnect: (element) => {
15. console.info(`ConnectAbility onDisconnect element.deviceId : ${element.deviceId}`);
16. },
17. onFailed: (code) => {
18. console.error(`featureAbilityTest ConnectAbility onFailed errCode : ${code}`);
19. },
20. },
21. );

23. featureAbility.disconnectAbility(connectId).then(() => {
24. console.info('disconnectAbility success');
25. }).catch((error: BusinessError)=>{
26. console.error(`featureAbilityTest result errCode : ${error.code}`);
27. });
```

## featureAbility.getWindow7+

PhonePC/2in1TabletTVWearable

getWindow(callback: AsyncCallback<window.Window>): void

获取当前Ability对应的窗口。使用callback异步回调。

**模型约束**：此接口仅可在FA模型下使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[window.Window](arkts-apis-window-window.md)> | 是 | 回调函数。当获取窗口成功，err为undefined，data为当前Ability对应的窗口；否则为错误对象。 |

**示例：**

```
1. import { featureAbility } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. featureAbility.getWindow((error: BusinessError, data: window.Window) => {
6. if (error && error.code !== 0) {
7. console.error(`getWindow fail, error: ${JSON.stringify(error)}`);
8. } else {
9. console.info(`getWindow success, data: ${typeof(data)}`);
10. }
11. });
```

## featureAbility.getWindow7+

PhonePC/2in1TabletTVWearable

getWindow(): Promise<window.Window>

获取当前Ability对应的窗口。使用Promise异步回调。

**模型约束**：此接口仅可在FA模型下使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[window.Window](arkts-apis-window-window.md)> | Promise对象，返回当前Ability对应的窗口。 |

**示例：**

```
1. import { featureAbility } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. featureAbility.getWindow().then((data: window.Window) => {
6. console.info(`getWindow success, data: ${typeof(data)}`);
7. }).catch((error: BusinessError)=>{
8. console.error(`getWindow fail, error: ${JSON.stringify(error)}`);
9. });
```

## AbilityWindowConfiguration7+

PhonePC/2in1TabletTVWearable

表示当前Ability对应的窗口配置项，使用时通过featureAbility.AbilityWindowConfiguration获取。

**模型约束**：此接口仅可在FA模型下使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

| 名称 | 值 | 说明 |
| --- | --- | --- |
| WINDOW\_MODE\_UNDEFINED | 0 | 未定义。 |
| WINDOW\_MODE\_FULLSCREEN | 1 | 全屏。 |
| WINDOW\_MODE\_SPLIT\_PRIMARY | 100 | 屏幕如果是水平方向表示左分屏，屏幕如果是竖直方向表示上分屏。 |
| WINDOW\_MODE\_SPLIT\_SECONDARY | 101 | 屏幕如果是水平方向表示右分屏，屏幕如果是竖直方向表示下分屏。 |
| WINDOW\_MODE\_FLOATING | 102 | 悬浮窗。 |

**示例：**

```
1. import { featureAbility } from '@kit.AbilityKit';

3. featureAbility.AbilityWindowConfiguration.WINDOW_MODE_UNDEFINED
```

## AbilityStartSetting7+

PhonePC/2in1TabletTVWearable

表示当前Ability对应的窗口属性，abilityStartSetting属性是一个定义为[key: string]: any的对象，key对应设定类型为：AbilityStartSetting枚举类型，value对应设定类型为：AbilityWindowConfiguration枚举类型。

使用时通过featureAbility.AbilityStartSetting获取。

**模型约束**：此接口仅可在FA模型下使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

| 名称 | 值 | 说明 |
| --- | --- | --- |
| BOUNDS\_KEY | 'abilityBounds' | 窗口显示大小属性的参数名。 |
| WINDOW\_MODE\_KEY | 'windowMode' | 窗口显示模式属性的参数名。 |
| DISPLAY\_ID\_KEY | 'displayId' | 窗口显示设备ID属性的参数名。 |

**示例：**

```
1. import { featureAbility } from '@kit.AbilityKit';

3. featureAbility.AbilityStartSetting.BOUNDS_KEY
```

## ErrorCode7+

PhonePC/2in1TabletTVWearable

定义启动Ability时返回的错误码。

**模型约束**：此接口仅可在FA模型下使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NO\_ERROR | 0 | 没有异常。 |
| INVALID\_PARAMETER | -1 | 无效的参数。 |
| ABILITY\_NOT\_FOUND | -2 | 找不到ABILITY。 |
| PERMISSION\_DENY | -3 | 权限拒绝。 |

## DataAbilityOperationType7+

PhonePC/2in1TabletTVWearable

表示数据的操作类型。DataAbility批量操作数据时可以通过该枚举值指定操作类型。

**模型约束**：此接口仅可在FA模型下使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

| 名称 | 值 | 说明 |
| --- | --- | --- |
| TYPE\_INSERT | 1 | 插入类型。 |
| TYPE\_UPDATE | 2 | 修改类型。 |
| TYPE\_DELETE | 3 | 删除类型。 |
| TYPE\_ASSERT | 4 | 声明类型。 |

## Context9+

PhonePC/2in1TabletTVWearable

type Context = \_Context

Context模块。

**模型约束**：此接口仅可在FA模型下使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 类型 | 说明 |
| --- | --- |
| [\_Context](js-apis-inner-app-context.md) | Context模块。 |

## AppVersionInfo9+

PhonePC/2in1TabletTVWearable

type AppVersionInfo = \_AppVersionInfo

应用版本信息。

**模型约束**：此接口仅可在FA模型下使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 类型 | 说明 |
| --- | --- |
| [\_AppVersionInfo](js-apis-inner-app-appversioninfo.md) | 应用版本信息。 |

## ProcessInfo9+

PhonePC/2in1TabletTVWearable

type ProcessInfo = \_ProcessInfo

进程信息。

**模型约束**：此接口仅可在FA模型下使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 类型 | 说明 |
| --- | --- |
| [\_ProcessInfo](js-apis-inner-app-processinfo.md) | 进程信息。 |
