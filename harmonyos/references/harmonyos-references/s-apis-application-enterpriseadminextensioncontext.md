---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/s-apis-application-enterpriseadminextensioncontext
title: EnterpriseAdminExtensionContext
breadcrumb: API参考 > 系统 > 基础功能 > MDM Kit（企业设备管理服务） > ArkTS API > application > EnterpriseAdminExtensionContext
category: harmonyos-references
scraped_at: 2026-04-29T14:01:15+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:14510b6ec5ad696f7b31a6aa03678bc5b7877132b3d413ceefbb7fe63de2b1c3
---

EnterpriseAdminExtensionContext是[EnterpriseAdminExtensionAbility](js-apis-enterpriseadminextensionability.md)的上下文环境，继承自[ExtensionContext](js-apis-inner-application-extensioncontext.md)。

每个EnterpriseAdminExtensionAbility组件实例化时，系统都会自动创建对应的EnterpriseAdminExtensionContext。开发者可以通过EnterpriseAdminExtensionContext获取应用的沙箱路径、启动其他的组件。该上下文环境只能在当前EnterpriseAdminExtensionAbility中使用，不能传递到其他组件中使用。

说明

本模块首批接口从API version 23 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

本模块接口仅对设备管理应用开放，且调用接口前需激活设备管理应用，具体请参考[MDM Kit开发指南](../harmonyos-guides/mdm-kit-guide.md)。

## 导入模块

PhonePC/2in1Tablet

```
1. import { common } from '@kit.MDMKit';
```

## EnterpriseAdminExtensionContext

PhonePC/2in1Tablet

[EnterpriseAdminExtensionAbility](js-apis-enterpriseadminextensionability.md)的上下文，继承自[ExtensionContext](js-apis-inner-application-extensioncontext.md)。

### startAbilityByAdmin

PhonePC/2in1Tablet

startAbilityByAdmin(admin: Want, want: Want): Promise<void>

在[EnterpriseAdminExtensionAbility](js-apis-enterpriseadminextensionability.md)组件中直接启动另外一个组件（页面没有弹窗提醒），目前支持[UIAbility](js-apis-app-ability-uiability.md)，[AppServiceExtensionAbility](js-apis-app-ability-appserviceextensionability.md)。使用Promise异步回调。

说明

仅支持启动三方应用组件，不支持系统应用组件。

被启动的组件需要对外可见，即module.json5中的exported字段需要为true。

不支持[隐式Want启动](../harmonyos-guides/ability-terminology.md#隐式want启动)。

如果被启动的UIAbility有权限保护，需要额外申请对应的权限。

**需要权限**：ohos.permission.ENTERPRISE\_START\_ABILITIES

**系统能力**：SystemCapability.Customization.EnterpriseDeviceManager

**模型约束**：此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| want | [Want](js-apis-app-ability-want.md) | 是 | 启动组件的必要信息，Want中必须包含被启动组件的abilityName和所在应用的bundleName。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。当启动组件失败时，会抛出错误对象。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200014 | Failed to start the ability. |
| 9200015 | The ability does not exist. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

需要在module.json5中配置被启动组件的信息。permissions为可选字段，需根据实际情况进行替换或者不填。

```
1. "abilities": [
2. {
3. "name": "MainAbility",
4. "srcEntry": "./ets/MainAbility/MainAbility.ts",
5. "description": "$string:MainAbility_desc",
6. "icon": "$media:icon",
7. "label": "$string:MainAbility_label",
8. "startWindowIcon": "$media:icon",
9. "startWindowBackground": "$color:white",
10. "exported": true,
11. "permissions": [
12. "ohos.permission.START_UI_Ability"
13. ]
14. }
15. ]
```

调用方应用需要在module.json5中申请对应的权限。启动其他应用中的组件时，调用方应用必须获取该组件所要求的权限。

```
1. "requestPermissions": [
2. {
3. "name": "ohos.permission.START_UI_ABILITY"
4. },
5. {
6. "name": "ohos.permission.ENTERPRISE_START_ABILITIES"
7. }
8. ]
```

```
1. import { EnterpriseAdminExtensionAbility } from '@kit.MDMKit';
2. import { preferences } from '@kit.ArkData';
3. import { Want } from '@kit.AbilityKit';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. /**
7. * 企业设备管理扩展能力组件
8. */
9. export default class EnterpriseAdminAbility extends EnterpriseAdminExtensionAbility {
10. onAdminEnabled() {
11. // 需根据实际情况进行替换
12. let admin: Want = {
13. bundleName: 'com.example.myapplication',
14. abilityName: 'EnterpriseAdminAbility',
15. };
16. // 需根据实际情况进行替换
17. let want: Want = {
18. bundleName: 'com.example.myotherapplication',
19. abilityName: 'MainAbility'
20. };
21. this.context.startAbilityByAdmin(admin, want).catch((err: BusinessError) => {
22. console.error(`Failed to start an ability. Code: ${err.code}, message: ${err.message}`);
23. });

25. // 通过context获取到应用文件路径
26. let preferencesDir = this.context.preferencesDir;
27. console.info(`preferencesDir: ` + preferencesDir);

29. // 通过context获取到preferences数据
30. let options: preferences.Options = {
31. // 需根据实际情况进行替换
32. name: "key",
33. };
34. try {
35. let preference = preferences.getPreferencesSync(this.context, options);
36. // 需根据实际情况进行替换
37. preference.putSync("key", "value");
38. preference.flushSync();

40. // 需根据实际情况进行替换
41. let value: string = preference.getSync('key', 'default') as string;
42. console.info(`get preferences value: ${value}`);
43. } catch (error) {
44. console.error('get preference fail');
45. }
46. }
47. }
```
