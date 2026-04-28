---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisespace-set-workspace-local-name
title: 设置空间本地名称
breadcrumb: 指南 > 应用服务 > Enterprise Space Kit（企业数字空间服务） > 空间管理 > 设置空间本地名称
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:58+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:318d0adc086e15d676b039ce61953f6453959b2e5e8a8015fd57cb6efaaafccc
---

## 场景介绍

从6.1.0(23)开始，支持设置工作空间本地名称的能力。

Enterprise Space Kit为应用提供设置工作空间本地名称（即工作空间的账号名称），企业工作空间和个人工作空间都可设置本地名称。

## 接口说明

详细接口说明可参考[接口文档](../harmonyos-references/enterprisespace-spacemanager.md#setworkspacelocalname)。

| 接口名 | 描述 |
| --- | --- |
| [setWorkspaceLocalName](../harmonyos-references/enterprisespace-spacemanager.md#setworkspacelocalname)(localName: string, workspaceId?: number): Promise<void> | 设置工作空间本地名称。使用Promise异步回调。 |

## 开发步骤

1. 导入Enterprise Space Kit模块。

   ```
   1. import { spaceManager } from '@kit.EnterpriseSpaceKit';
   ```
2. 调用[setWorkspaceLocalName](../harmonyos-references/enterprisespace-spacemanager.md#setworkspacelocalname)接口，设置工作空间本地名称，并且查看打印信息。

   ```
   1. const localName: string = 'localName'; // 设置的工作空间的本地名称。
   2. const workspaceId: number = 100; // 工作空间ID。
   3. try {
   4. await spaceManager.setWorkspaceLocalName(localName, workspaceId);
   5. console.info('Succeeded in setting workspace local name');
   6. } catch (err) {
   7. console.error(`Failed to set workspace local name. Code: ${err.code}, message: ${err.message}`);
   8. }
   ```
