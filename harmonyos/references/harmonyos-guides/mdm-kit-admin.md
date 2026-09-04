---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mdm-kit-admin
title: EnterpriseAdminExtensionAbility开发指南
breadcrumb: 指南 > 系统 > 基础功能 > MDM Kit（企业设备管理服务） > EnterpriseAdminExtensionAbility开发指南
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:34+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:89d11793319c3700245f1f749253b91b15f2be7cdf46c8e308b0c7f8610c0939
---

## 概述

企业设备管理扩展能力组件，是设备管理应用必备组件。当开发者为企业开发设备管理应用时，需继承EnterpriseAdminExtensionAbility，在EnterpriseAdminExtensionAbility实例中实现MDM业务逻辑，EnterpriseAdminExtensionAbility实现了系统管理状态变化通知功能，并定义了管理应用激活、去激活、应用安装、卸载事件等回调接口。

## 接口说明

以下为本次开发示例所使用的接口，更多接口及使用方式请见企业设备管理扩展能力接口文档[EnterpriseAdminExtensionAbility](../harmonyos-references/js-apis-enterpriseadminextensionability.md)。

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/4qmtNkbkRk6fnHcvYOJY-w/zh-cn_image_0000002712244630.png)

首先，创建一个EnterpriseAdmin类型的ExtensionAbility（也就是EnterpriseAdminExtensionAbility）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/9En4C8RQQwWY6INakOcSeg/zh-cn_image_0000002742003583.png)

其次，打开新建的EnterpriseAdminAbility文件，导入EnterpriseAdminExtensionAbility模块，使其继承EnterpriseAdminExtensionAbility并加上需要的应用通知回调方法，如onAdminEnabled()、onAdminDisabled()等回调方法。当设备管理应用激活或者解除激活时，可以在对应回调方法中接收系统发送通知。

```typescript
import { EnterpriseAdminExtensionAbility } from '@kit.MDMKit';
// ...

export default class EnterpriseAdminAbility extends EnterpriseAdminExtensionAbility {
  // ...

  // 设备管理器应用激活回调方法，应用可在此回调函数中进行初始化策略设置。
  onAdminEnabled() {
    console.info('onAdminEnabled');
    // ...
  }

  // 设备管理器应用去激活回调方法，应用可在此回调函数中通知企业管理员设备已脱管。
  onAdminDisabled() {
    console.info('onAdminDisabled');
    // ...
  }

  // 应用安装回调方法，应用可在此回调函数中进行事件上报，通知企业管理员。
  onBundleAdded(bundleName: string) {
    console.info('EnterpriseAdminAbility onBundleAdded bundleName:' + bundleName);
  }

  // 应用卸载回调方法，应用可在此回调函数中进行事件上报，通知企业管理员。
  onBundleRemoved(bundleName: string) {
    console.info('EnterpriseAdminAbility onBundleRemoved bundleName:' + bundleName);
  }

  // 普通设备管理应用激活回调方法，应用可在此回调函数中进行初始化策略设置。
  onDeviceAdminEnabled(bundleName: string) {
    console.info('EnterpriseAdminAbility onDeviceAdminEnabled bundleName:' + bundleName);
  }

  // 普通设备管理应用解除激活回调方法，应用可在此回调函数中通知企业管理员设备已脱管。
  onDeviceAdminDisabled(bundleName: string) {
    console.info('EnterpriseAdminAbility onDeviceAdminDisabled bundleName:' + bundleName);
  }
};
```

最后，在工程Module对应的[module.json5](module-configuration-file.md)配置文件中将EnterpriseAdminAbility注册为ExtensionAbility，type标签需要设置为“enterpriseAdmin”，srcEntry标签表示当前ExtensionAbility组件所对应的代码路径。

```json5
"extensionAbilities": [
  {
    "name": "EnterpriseAdminAbility",
    "type": "enterpriseAdmin",
    "exported": true,
    "srcEntry": "./ets/enterpriseadminability/EnterpriseAdminAbility.ets"
  }
],
```
