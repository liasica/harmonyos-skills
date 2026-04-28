---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mdm-kit-admin
title: EnterpriseAdminExtensionAbility开发指南
breadcrumb: 指南 > 系统 > 基础功能 > MDM Kit（企业设备管理服务） > EnterpriseAdminExtensionAbility开发指南
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:33+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:cd2567245b609590065ca6291a98d940ac6291c687a4396598a84069f03ecaaf
---

## 概述

企业设备管理扩展能力组件，是设备管理应用必备组件。当开发者为企业开发设备管理应用时，需继承EnterpriseAdminExtensionAbility，在EnterpriseAdminExtensionAbility实例中实现MDM业务逻辑，EnterpriseAdminExtensionAbility实现了系统管理状态变化通知功能，并定义了管理应用激活、去激活、应用安装、卸载事件等回调接口。

## 接口说明

以下为本次开发示例所使用的接口，更多接口及使用方式请见[企业设备管理扩展能力接口文档](../harmonyos-references/js-apis-enterpriseadminextensionability.md)。

| 接口名称 | 描述 |
| --- | --- |
| [onAdminEnabled(): void](../harmonyos-references/js-apis-enterpriseadminextensionability.md#onadminenabled) | 设备管理应用被激活回调方法。 |
| [onAdminDisabled(): void](../harmonyos-references/js-apis-enterpriseadminextensionability.md#onadmindisabled) | 设备管理应用被解除激活回调方法。 |
| [onBundleAdded(bundleName: string): void](../harmonyos-references/js-apis-enterpriseadminextensionability.md#onbundleadded) | 应用安装回调方法。 |
| [onBundleRemoved(bundleName: string): void](../harmonyos-references/js-apis-enterpriseadminextensionability.md#onbundleremoved) | 应用卸载回调方法。 |
| [onDeviceAdminEnabled(bundleName: string): void](../harmonyos-references/js-apis-enterpriseadminextensionability.md#ondeviceadminenabled23) | 普通设备管理应用被激活回调方法。 |
| [onDeviceAdminDisabled(bundleName: string): void](../harmonyos-references/js-apis-enterpriseadminextensionability.md#ondeviceadmindisabled23) | 普通设备管理应用被解除激活回调方法。 |

## 开发步骤

新建一个工程后，结构如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/_PMoQww5TtiRQmWbmjz9Rw/zh-cn_image_0000002583438509.png?HW-CC-KV=V1&HW-CC-Date=20260427T234432Z&HW-CC-Expire=86400&HW-CC-Sign=07AE69751193D185C159FD07C1444D377E0E0071C9AE2661DC7AE7AAFF10DA0A)

首先，创建一个EnterpriseAdmin类型的ExtensionAbility（也就是EnterpriseAdminExtensionAbility）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/oMRUgV5dRJWvp-PG1TV-Dw/zh-cn_image_0000002552958464.png?HW-CC-KV=V1&HW-CC-Date=20260427T234432Z&HW-CC-Expire=86400&HW-CC-Sign=581804DD47F187FA659509001AB8E650A67B193A934178A504A2E82EB1CE2FA9)

其次，打开新建的EnterpriseAdminAbility文件，导入EnterpriseAdminExtensionAbility模块，使其继承EnterpriseAdminExtensionAbility并加上需要的应用通知回调方法，如onAdminEnabled()、onAdminDisabled()等回调方法。当设备管理应用激活或者解除激活时，可以在对应回调方法中接收系统发送通知。

```
1. import { EnterpriseAdminExtensionAbility } from '@kit.MDMKit';
2. // ···

4. export default class EnterpriseAdminAbility extends EnterpriseAdminExtensionAbility {
5. // ···

7. // 设备管理器应用激活回调方法，应用可在此回调函数中进行初始化策略设置。
8. onAdminEnabled() {
9. console.info('onAdminEnabled');
10. // ···
11. }

13. // 设备管理器应用去激活回调方法，应用可在此回调函数中通知企业管理员设备已脱管。
14. onAdminDisabled() {
15. console.info('onAdminDisabled');
16. // ···
17. }

19. // 应用安装回调方法，应用可在此回调函数中进行事件上报，通知企业管理员。
20. onBundleAdded(bundleName: string) {
21. console.info('EnterpriseAdminAbility onBundleAdded bundleName:' + bundleName);
22. }

24. // 应用卸载回调方法，应用可在此回调函数中进行事件上报，通知企业管理员。
25. onBundleRemoved(bundleName: string) {
26. console.info('EnterpriseAdminAbility onBundleRemoved bundleName' + bundleName);
27. }

29. // 普通设备管理应用激活回调方法，应用可在此回调函数中进行初始化策略设置
30. onDeviceAdminEnabled(bundleName: string) {
31. console.info("EnterpriseAdminAbility onDeviceAdminEnabled bundleName:" + bundleName);
32. }

34. // 普通设备管理应用解除激活回调方法，应用可在此回调函数中通知企业管理员设备已脱管
35. onDeviceAdminDisabled(bundleName: string) {
36. console.info("EnterpriseAdminAbility onDeviceAdminDisabled bundleName" + bundleName);
37. }
38. };
```

[EnterpriseAdminAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/EnterpriseAdminExtensionAbility/EnterpriseAdminExtensionAbility/entry/src/main/ets/enterpriseadminability/EnterpriseAdminAbility.ets#L27-L195)

最后，在工程Module对应的[module.json5](module-configuration-file.md)配置文件中将EnterpriseAdminAbility注册为ExtensionAbility，type标签需要设置为“enterpriseAdmin”，srcEntry标签表示当前ExtensionAbility组件所对应的代码路径。

```
1. "extensionAbilities": [
2. {
3. "name": "EnterpriseAdminAbility",
4. "type": "enterpriseAdmin",
5. "exported": true,
6. "srcEntry": "./ets/enterpriseadminability/EnterpriseAdminAbility.ets"
7. }
8. ],
```

[module.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/EnterpriseAdminExtensionAbility/EnterpriseAdminExtensionAbility/entry/src/main/module.json5#L51-L60)
