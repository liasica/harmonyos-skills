---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inputmethod-extension-context
title: @ohos.InputMethodExtensionContext (InputMethodExtensionContext)
breadcrumb: API参考 > 应用框架 > IME Kit（输入法开发服务） > ArkTS API > @ohos.InputMethodExtensionContext (InputMethodExtensionContext)
category: harmonyos-references
scraped_at: 2026-04-28T08:06:06+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c4356ee562db40c46999d7d242c334989a47e1a54817ee50578edd1a3e47cef5
---

InputMethodExtensionContext模块是InputMethodExtensionAbility的上下文环境，继承于ExtensionContext，提供InputMethodExtensionAbility具有的能力和接口，包括启动、停止、绑定、解绑Ability。

说明

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { InputMethodExtensionContext } from '@kit.IMEKit';
```

## 使用说明

PhonePC/2in1TabletTVWearable

在使用InputMethodExtensionContext的功能前，需要通过InputMethodExtensionAbility子类实例获取。

```
1. import { InputMethodExtensionAbility, InputMethodExtensionContext } from '@kit.IMEKit';
2. import { Want } from '@kit.AbilityKit';

4. class InputMethodExtAbility extends InputMethodExtensionAbility {
5. onCreate(want: Want): void {
6. console.info('onCreate, want:' + want.abilityName);
7. }
8. }
```

## InputMethodExtensionContext.destroy

PhonePC/2in1TabletTVWearable

destroy(callback: AsyncCallback<void>): void;

销毁输入法应用。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当销毁输入法应用成功时，err为undefined；否则为错误对象。 |

**示例：**

```
1. import { InputMethodExtensionAbility, InputMethodExtensionContext } from '@kit.IMEKit';
2. import { Want } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. class InputMethodExtAbility extends InputMethodExtensionAbility {
6. onCreate(want: Want): void {
7. console.info('onCreate, want:' + want.abilityName);
8. }

10. onDestroy() {
11. this.context.destroy((err: BusinessError) => {
12. if (err) {
13. console.error(`Failed to destroy context, err code = ${err.code}`);
14. return;
15. }
16. console.info('Succeeded in destroying context.');
17. });
18. }
19. }
```

## InputMethodExtensionContext.destroy

PhonePC/2in1TabletTVWearable

destroy(): Promise<void>;

销毁输入法应用。使用Promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```
1. import { InputMethodExtensionAbility, InputMethodExtensionContext } from '@kit.IMEKit';
2. import { Want } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. class InputMethodExtAbility extends InputMethodExtensionAbility {
6. onCreate(want: Want): void {
7. console.info('onCreate, want:' + want.abilityName);
8. }

10. onDestroy() {
11. this.context.destroy().then(() => {
12. console.info('Succeed in destroying context.');
13. }).catch((err: BusinessError)=>{
14. console.error(`Failed to destroy context, err code = ${err.code}`);
15. });
16. }
17. }
```

## InputMethodExtensionContext.startAbility12+

PhonePC/2in1TabletTVWearable

startAbility(want: Want): Promise<void>;

拉起目标应用。使用Promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-app-ability-want.md) | 是 | 用于指定目标应用的Want类型信息，包括ability名称、bundle名称等。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[元能力子系统错误码](errorcode-ability.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16000004 | Cannot start an invisible component. |
| 16000005 | The specified process does not have the permission. |
| 16000006 | Cross-user operations are not allowed. |
| 16000008 | The crowdtesting application expires. |
| 16000009 | An ability cannot be started or stopped in Wukong mode. |
| 16000010 | The call with the continuation and prepare continuation flag is forbidden. |
| 16000011 | The context does not exist. |
| 16000012 | The application is controlled. |
| 16000013 | The application is controlled by EDM. |
| 16000019 | No matching ability is found. |
| 16000050 | Internal error. |
| 16000053 | The ability is not on the top of the UI. |
| 16000055 | Installation-free timed out. |
| 16000061 | Operation not supported. |
| 16200001 | The caller has been released. |
| 16000069 | The extension cannot start the third party application. |
| 16000070 | The extension cannot start the service. |

**示例：**

```
1. import { InputMethodExtensionAbility, InputMethodExtensionContext } from '@kit.IMEKit';
2. import { Want } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. class InputMethodExtAbility extends InputMethodExtensionAbility {
6. onCreate(want: Want): void {
7. const context: InputMethodExtensionContext = this.context;
8. const targetWant: Want = {
9. bundleName: "com.example.aafwk.test",
10. abilityName: "com.example.aafwk.test.TwoAbility"
11. };

13. context.startAbility(targetWant)
14. .then(() => console.info('startAbility success'))
15. .catch((err: BusinessError) => {
16. console.error(`StartAbility failed. Code: ${err.code}, Message: ${err.message}`);
17. });
18. }

20. onDestroy() {
21. this.context.destroy().then(() => {
22. console.info('Succeed in destroying context.');
23. }).catch((err: BusinessError) => {
24. console.error(`Failed to destroy context, err code = ${err.code}`);
25. });
26. }
27. }
```
