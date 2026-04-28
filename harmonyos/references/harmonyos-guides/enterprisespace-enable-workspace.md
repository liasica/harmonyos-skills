---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisespace-enable-workspace
title: 使能工作空间
breadcrumb: 指南 > 应用服务 > Enterprise Space Kit（企业数字空间服务） > 空间管理 > 使能工作空间
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:55+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0a000ed7b4f78464743900ea0a42a86fbc6bb4e1e597cd2117a26ac974d9944d
---

## 场景介绍

Enterprise Space Kit为应用提供使能双空间的能力。需要先使能工作空间才可以创建个人空间。

## 接口说明

详细接口说明可参考[接口文档](../harmonyos-references/enterprisespace-spacemanager.md#enableworkspace)。

| 接口名 | 描述 |
| --- | --- |
| [enableWorkspace](../harmonyos-references/enterprisespace-spacemanager.md#enableworkspace)(enable: boolean): Promise<void> | 使能工作空间。使用Promise异步回调。 |

## 开发步骤

1. 导入Enterprise Space Kit模块。

   ```
   1. import { spaceManager } from '@kit.EnterpriseSpaceKit';
   ```
2. 调用[enableWorkspace](../harmonyos-references/enterprisespace-spacemanager.md#enableworkspace)接口，使能工作空间，并且查看打印信息。

   ```
   1. const enable: boolean = true;
   2. try {
   3. await spaceManager.enableWorkspace(enable);
   4. console.info('Succeeded in enabling workspace');
   5. } catch (err) {
   6. console.error(`Failed to enable workspace. Code: ${err.code}, message: ${err.message}`);
   7. }
   ```
