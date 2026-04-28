---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisespace-get-restricted-access-process-list
title: 获取不可访问后台用户数据的系统服务进程列表
breadcrumb: 指南 > 应用服务 > Enterprise Space Kit（企业数字空间服务） > 空间管理 > 获取不可访问后台用户数据的系统服务进程列表
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:57+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9afebbbf78bd022d1821698b75ae3f0b914aa583c4a757fc0e3e79a5168fc54f
---

## 场景介绍

从6.0.1(21)开始，支持获取不可访问后台用户数据的系统服务进程列表的能力。

Enterprise Space Kit为应用提供获取通过接口[addRestrictedAccessBackgroundUserdataProcessList](../harmonyos-references/enterprisespace-spacemanager.md#addrestrictedaccessbackgrounduserdataprocesslist)添加管控的系统服务进程列表的功能。

## 接口说明

详细接口说明可参考[接口文档](../harmonyos-references/enterprisespace-spacemanager.md#getrestrictedaccessbackgrounduserdataprocesslist)。

| 接口名 | 描述 |
| --- | --- |
| [getRestrictedAccessBackgroundUserdataProcessList](../harmonyos-references/enterprisespace-spacemanager.md#getrestrictedaccessbackgrounduserdataprocesslist)(userData: [UserDataEnum](../harmonyos-references/enterprisespace-spacemanager.md#userdataenum)): Promise<ProcessConfigInfo[]> | 获取不可访问后台用户数据的系统服务进程列表。使用Promise异步回调。 |

## 开发步骤

1. 导入Enterprise Space Kit模块。

   ```
   1. import { spaceManager } from '@kit.EnterpriseSpaceKit';
   ```
2. 调用接口[getRestrictedAccessBackgroundUserdataProcessList](../harmonyos-references/enterprisespace-spacemanager.md#getrestrictedaccessbackgrounduserdataprocesslist)，获取不可访问后台用户数据的系统服务进程列表，并且查看打印信息。

   ```
   1. const userData: spaceManager.UserDataEnum = spaceManager.UserDataEnum.ENTERPRISE;
   2. try {
   3. const processConfigInfos: spaceManager.ProcessConfigInfo[] = await spaceManager.getRestrictedAccessBackgroundUserdataProcessList(userData);
   4. console.info(`Succeeded in getting restricted access background user data process list. process config infos: ${JSON.stringify(processConfigInfos)}`);
   5. } catch (err) {
   6. console.error(`Failed to get restricted access background user data process list. Code: ${err.code}, message: ${err.message}`);
   7. }
   ```
