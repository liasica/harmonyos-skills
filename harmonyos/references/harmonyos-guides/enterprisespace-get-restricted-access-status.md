---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisespace-get-restricted-access-status
title: 获取系统服务进程不可访问的后台用户数据状态
breadcrumb: 指南 > 应用服务 > Enterprise Space Kit（企业数字空间服务） > 空间管理 > 获取系统服务进程不可访问的后台用户数据状态
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:56+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7fa5e43b4f97a18babb7b1a5bd46ded4e86716948c744faaea041d655139c76f
---

## 场景介绍

从6.0.1(21)开始，支持获取系统服务进程不可访问的后台用户数据状态的能力。

Enterprise Space Kit为应用提供获取系统服务进程管控不可访问后台用户数据的状态，用于确认系统服务进程是否被管控访问后台用户数据。

## 接口说明

详细接口说明可参考[接口文档](../harmonyos-references/enterprisespace-spacemanager.md#getrestrictedaccessbackgrounduserdatastatus)。

| 接口名 | 描述 |
| --- | --- |
| [getRestrictedAccessBackgroundUserdataStatus](../harmonyos-references/enterprisespace-spacemanager.md#getrestrictedaccessbackgrounduserdatastatus)(userData: [UserDataEnum](../harmonyos-references/enterprisespace-spacemanager.md#userdataenum)): Promise<boolean> | 获取系统服务进程管控不可访问后台用户数据的状态。使用Promise异步回调。 |

## 开发步骤

1. 导入Enterprise Space Kit模块。

   ```
   1. import { spaceManager } from '@kit.EnterpriseSpaceKit';
   ```
2. 调用接口[getRestrictedAccessBackgroundUserdataStatus](../harmonyos-references/enterprisespace-spacemanager.md#getrestrictedaccessbackgrounduserdatastatus)，提供获取系统服务进程管控不可访问后台用户数据的状态，并且查看打印信息。

   ```
   1. const userData: spaceManager.UserDataEnum = spaceManager.UserDataEnum.ENTERPRISE;
   2. try {
   3. const status: boolean = await spaceManager.getRestrictedAccessBackgroundUserdataStatus(userData);
   4. console.info(`Succeeded in getting restricted access background user data status. status: ${status}`);
   5. } catch (err) {
   6. console.error(`Failed to get restricted access background user data status. Code: ${err.code}, message: ${err.message}`);
   7. }
   ```
