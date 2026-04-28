---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/e2e-verification
title: 端到端验证
breadcrumb: 指南 > 应用框架 > Core File Kit（文件基础服务） > 应用文件 > 应用数据备份恢复 > 设备升级应用数据迁移适配指导 > 验证应用数据迁移 > 端到端验证
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:15+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a0b55f0c3387d861905b3ca119942633d5b71bdcae5d0fcc074279582c996b47
---

应用适配完成并[上架到华为应用市场](../app/agc-help-releaseharmony-0000001933963166.md)之后，开发者需要模拟终端用户将终端设备从HarmonyOS升级到HarmonyOS NEXT的场景，端到端验证应用数据迁移结果。

1. 在应用适配完成并上架到华为应用市场之后，开发者可以端到端验证应用数据迁移结果。当前开发者持有的终端设备为HarmonyOS NEXT。开发者在验证升级前，需要将设备从HarmonyOS NEXT回退到HarmonyOS。系统回退的入口为：**设置** > **系统** > **开发者选项** > **系统回退**。
2. 将终端设备回退到HarmonyOS后，需要预置APK应用的数据。在数据预置完成后，开发者需要将终端设备从HarmonyOS升级到HarmonyOS NEXT。系统更新的入口为：**设置** > **系统和更新** > **软件更新**。
3. 终端设备成功从HarmonyOS升级到HarmonyOS NEXT，走过开机向导界面后，开始执行应用数据迁移。开发者请在应用数据迁移结束后，验证应用数据迁移的结果。
