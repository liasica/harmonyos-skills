---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisespace-query-workspace
title: 查询工作空间
breadcrumb: 指南 > 应用服务 > Enterprise Space Kit（企业数字空间服务） > 空间管理 > 查询工作空间
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:55+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:673b758bce8bf42ce249c9eeed1bf7a3f279eeb361577134b2de539608bed7ac
---

## 场景介绍

Enterprise Space Kit为应用提供查询工作空间信息的能力。

## 接口说明

详细接口说明可参考[接口文档](../harmonyos-references/enterprisespace-spacemanager.md#queryworkspace)。

| 接口名 | 描述 |
| --- | --- |
| [queryWorkspace](../harmonyos-references/enterprisespace-spacemanager.md#queryworkspace)(queryFlag: [QueryType](../harmonyos-references/enterprisespace-spacemanager.md#querytype)): Promise<WorkspaceInfo[]> | 查询工作空间信息并返回结果。使用Promise异步回调。 |

## 开发步骤

1. 导入Enterprise Space Kit模块。

   ```
   1. import { spaceManager } from '@kit.EnterpriseSpaceKit';
   ```
2. 调用[queryWorkspace](../harmonyos-references/enterprisespace-spacemanager.md#queryworkspace)接口，查询工作空间，并且查看打印信息。

   ```
   1. const queryFlag: spaceManager.QueryType = spaceManager.QueryType.ALL;
   2. try {
   3. const spaces: spaceManager.WorkspaceInfo[] = await spaceManager.queryWorkspace(queryFlag);
   4. console.info(`Succeeded in querying workspace` + JSON.stringify(spaces));
   5. } catch (err) {
   6. console.error(`Failed to query workspace. Code: ${err.code}, message: ${err.message}`);
   7. }
   ```
