---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisespace-set-lockdown-exemption-apps
title: 设置深度冻结豁免名单
breadcrumb: 指南 > 应用服务 > Enterprise Space Kit（企业数字空间服务） > 空间管理 > 设置深度冻结豁免名单
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:57+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:51d3610cd1c5b96e031cd9cff7cb5d7e3c4af4088d935d8f10ce2a43ea43ccf6
---

## 场景介绍

从6.0.2(22)开始，支持设置深度冻结豁免名单的能力。

Enterprise Space Kit为企业应用提供设置深度冻结豁免名单的能力。设置豁免的应用在后台空间可正常运行，不会被冻结。

## 接口说明

详细接口说明可参考[接口文档](../harmonyos-references/enterprisespace-spacemanager.md#setlockdownexemptionapps)。

| 接口名 | 描述 |
| --- | --- |
| [setLockdownExemptionApps](../harmonyos-references/enterprisespace-spacemanager.md#setlockdownexemptionapps)(appIds: string[], workspaceId?: number): Promise<void> | 设置深度冻结豁免名单。使用Promise异步回调。 |

## 开发步骤

1. 导入Enterprise Space Kit模块和相关依赖模块。

   ```
   1. import { spaceManager } from '@kit.EnterpriseSpaceKit';
   ```
2. 调用接口[setLockdownExemptionApps](../harmonyos-references/enterprisespace-spacemanager.md#setlockdownexemptionapps)，设置深度冻结豁免名单，并且查看打印信息。

   ```
   1. const workspaceId: number = 100;
   2. const appIds = [
   3. 'com.example.enterprisespacekit_samplecode_clientdemo_arkts1',
   4. 'com.example.enterprisespacekit_samplecode_clientdemo_arkts2'
   5. ];
   6. try {
   7. await spaceManager.setLockdownExemptionApps(appIds, workspaceId);
   8. console.info(`Succeeded in setting lockdown exemption apps.`);
   9. } catch (err) {
   10. console.error(`Failed to set lockdown exemption apps. Code: ${err.code}, message: ${err.message}`);
   11. }
   ```
