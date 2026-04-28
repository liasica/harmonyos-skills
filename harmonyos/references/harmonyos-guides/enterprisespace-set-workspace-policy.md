---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisespace-set-workspace-policy
title: 设置工作空间策略
breadcrumb: 指南 > 应用服务 > Enterprise Space Kit（企业数字空间服务） > 空间管理 > 设置工作空间策略
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:57+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ecf4e7dcd3ef18bdefff633dc486dca08460c169cf4e7f59365d4d55d155b600
---

## 场景介绍

从6.0.2(22)开始，支持设置工作空间策略的能力。

Enterprise Space Kit为应用提供设置工作空间策略的能力。从6.0.2(22)版本开始支持深度冻结策略“lockdown”，从6.1.0(23)版本开始支持个人空间创建引导页展示策略“spaceguide”。

## 接口说明

详细接口说明可参考[接口文档](../harmonyos-references/enterprisespace-spacemanager.md#setworkspacepolicy)。

| 接口名 | 描述 |
| --- | --- |
| [setWorkspacePolicy](../harmonyos-references/enterprisespace-spacemanager.md#setworkspacepolicy)(key: string, value: number, workspaceId?: number): Promise<void> | 设置工作空间策略。使用Promise异步回调。 |

## 开发步骤

1. 导入Enterprise Space Kit模块和相关依赖模块。

   ```
   1. import { spaceManager } from '@kit.EnterpriseSpaceKit';
   ```
2. 调用接口[setWorkspacePolicy](../harmonyos-references/enterprisespace-spacemanager.md#setworkspacepolicy)，设置空间策略，并且查看打印信息。

   ```
   1. const key: string = 'lockdown';
   2. const value: spaceManager.LockdownModePolicy = spaceManager.LockdownModePolicy.OFF;
   3. const workspaceId: number = 100;
   4. try {
   5. await spaceManager.setWorkspacePolicy(key, value, workspaceId);
   6. console.info(`Succeeded in setting workspace policy.`);
   7. } catch (err) {
   8. console.error(`Failed to set workspace policy. Code: ${err.code}, message: ${err.message}`);
   9. }
   ```
