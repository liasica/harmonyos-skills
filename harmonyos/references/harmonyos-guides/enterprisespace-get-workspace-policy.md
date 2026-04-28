---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisespace-get-workspace-policy
title: 查询工作空间策略
breadcrumb: 指南 > 应用服务 > Enterprise Space Kit（企业数字空间服务） > 空间管理 > 查询工作空间策略
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:57+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:025966257a2738355ebb2dc000b291e9d49662ab27bd8e3ad6dc4b61e13ca76e
---

## 场景介绍

从6.0.2(22)开始，支持查询工作空间策略的能力。

Enterprise Space Kit为应用提供查询工作空间策略的能力。从6.0.2(22)版本开始支持深度冻结策略“lockdown”，从6.1.0(23)版本开始支持个人空间创建引导页展示策略“spaceguide”。

## 接口说明

详细接口说明可参考[接口文档](../harmonyos-references/enterprisespace-spacemanager.md#getworkspacepolicy)。

| 接口名 | 描述 |
| --- | --- |
| [getWorkspacePolicy](../harmonyos-references/enterprisespace-spacemanager.md#getworkspacepolicy)(key: string, workspaceId?: number): Promise<number> | 查询工作空间策略并返回结果。使用Promise异步回调。 |

## 开发步骤

1. 导入Enterprise Space Kit模块和相关依赖模块。

   ```
   1. import { spaceManager } from '@kit.EnterpriseSpaceKit';
   ```
2. 调用接口[getWorkspacePolicy](../harmonyos-references/enterprisespace-spacemanager.md#getworkspacepolicy)，查询空间策略，并且查看打印信息。

   ```
   1. const key: string = 'lockdown';
   2. const workspaceId: number = 100;
   3. try {
   4. const value: number = await spaceManager.getWorkspacePolicy(key, workspaceId);
   5. console.info(`Succeeded in getting workspace policy. value: ${value}`);
   6. } catch (err) {
   7. console.error(`Failed to get workspace policy. Code: ${err.code}, message: ${err.message}`);
   8. }
   ```
