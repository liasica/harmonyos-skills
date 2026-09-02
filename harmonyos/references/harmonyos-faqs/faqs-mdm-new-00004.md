---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-mdm-new-00004
title: 通过应用管理接口隐藏桌面应用图标的实现方式
breadcrumb: FAQ > 系统开发 > 基础功能 > 企业设备管理（MDM） > 通过应用管理接口隐藏桌面应用图标的实现方式
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:40+08:00
doc_updated_at: 2026-07-22
content_hash: sha256:4ab254e057e0d450c089432423d7d0327a81d5d9bc9c130c2a2aa1d88a1de4d7
---

## 问题现象

应用黑白名单仅提供禁止使用的能力，应用图标仍在系统桌面展示，无法满足应用隔离要求。期望下发应用黑白名单后，应用图标在系统桌面上隐藏，无法被其他应用拉起；取消名单后，应用图标恢复展示。应用本身未被卸载，仅图标隐藏且无法被三方应用拉起和使用。

## 背景知识

应用管理接口[applicationManager.addHideLauncherIcon](../harmonyos-references/js-apis-enterprise-applicationmanager.md#applicationmanageraddhidelaunchericon)提供添加隐藏桌面应用图标名单的能力，可用于实现应用图标隐藏功能。

## 解决方案

升级设备至7.0（26.0.0）Beta版本后，调用[applicationManager.addHideLauncherIcon](../harmonyos-references/js-apis-enterprise-applicationmanager.md#applicationmanageraddhidelaunchericon)接口添加隐藏桌面应用图标名单。下发名单后，对应应用图标在系统桌面上隐藏，无法被其他应用拉起；取消名单后，应用图标恢复展示。应用本身未被卸载，仅图标隐藏且无法被三方应用拉起和使用。

**接口说明：**

* addHideLauncherIcon(admin: Want, appIconIdList: string[]): Promise<void>：添加隐藏桌面应用图标名单。
  + admin：企业设备管理应用信息，类型为Want，需指定企业设备管理应用的包名与能力名称。
  + appIconIdList：需要隐藏图标的应用包名列表，类型为string[]。
* removeHideLauncherIcon(admin: Want, appIconIdList: string[]): Promise<void>：移除隐藏桌面应用图标名单，取消隐藏后应用图标恢复展示。
  + admin：企业设备管理应用信息，类型为Want。
  + appIconIdList：需要取消隐藏图标的应用包名列表，类型为string[]。

**前置条件：**

* 调用方需为企业设备管理应用（EDM），且已获取企业设备管理权限。
* 需在module.json5中声明ohos.permission.MANAGE\_ENTERPRISE\_DEVICE\_ADMIN权限。

**代码示例：**

```ts
import { applicationManager } from '@kit.EnterpriseDeviceManager';
import { Want } from '@kit.AbilityKit';

// 企业设备管理应用信息
let admin: Want = {
  bundleName: 'com.example.edm',
  abilityName: 'EnterpriseAdminAbility'
};

// 需要隐藏图标的应用包名列表
let appIconIdList: string[] = ['com.example.target1', 'com.example.target2'];

// 添加隐藏桌面应用图标名单
applicationManager.addHideLauncherIcon(admin, appIconIdList).then(() => {
  console.info('Succeeded in adding hide launcher icon list.');
}).catch((err: BusinessError) => {
  console.error(`Failed to add hide launcher icon list. Code: ${err.code}, message: ${err.message}`);
});

// 取消隐藏桌面应用图标名单，恢复图标展示
applicationManager.removeHideLauncherIcon(admin, appIconIdList).then(() => {
  console.info('Succeeded in removing hide launcher icon list.');
}).catch((err: BusinessError) => {
  console.error(`Failed to remove hide launcher icon list. Code: ${err.code}, message: ${err.message}`);
});
```
