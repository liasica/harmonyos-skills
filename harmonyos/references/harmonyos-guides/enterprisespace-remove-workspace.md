---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisespace-remove-workspace
title: 移除工作空间
breadcrumb: 指南 > 应用服务 > Enterprise Space Kit（企业数字空间服务） > 空间管理 > 移除工作空间
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:55+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2559987fb57dc79f831833ee6ef4fee2f7a7c2208be0908448688a0c4053601e
---

## 场景介绍

Enterprise Space Kit为企业用户提供移除工作空间的能力。

## 接口说明

详细接口说明可参考[接口文档](../harmonyos-references/enterprisespace-spacemanager.md#removeworkspace)。

| 接口名 | 描述 |
| --- | --- |
| [removeWorkspace](../harmonyos-references/enterprisespace-spacemanager.md#removeworkspace)(localId: number): Promise<void> | 移除工作空间。使用Promise异步回调。 |

## 开发步骤

1. 导入Enterprise Space Kit模块。

   ```
   1. import { spaceManager } from '@kit.EnterpriseSpaceKit';
   ```
2. 调用[removeWorkspace](../harmonyos-references/enterprisespace-spacemanager.md#removeworkspace)接口，移除工作空间，并且查看打印信息。

   ```
   1. const workspaceId: number = 100;
   2. try {
   3. await spaceManager.removeWorkspace(workspaceId);
   4. console.info('Succeeded in removing workspace');
   5. } catch (err) {
   6. console.error(`Failed to remove workspace. Code: ${err.code}, message: ${err.message}`);
   7. }
   ```
