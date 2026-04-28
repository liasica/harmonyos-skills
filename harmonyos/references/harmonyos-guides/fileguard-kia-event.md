---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fileguard-kia-event
title: 订阅或取消订阅KIA文件拷贝、重命名和压缩事件
breadcrumb: 指南 > 系统 > 安全 > Enterprise Data Guard Kit（企业数据保护服务） > 文件分级管控 > 订阅或取消订阅KIA文件拷贝、重命名和压缩事件
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:07+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:23dfb8c7b5fd8df685fd9ab3549ed273132c81684980c2ed0a5c43ccb7cb635c
---

## 场景介绍

为应用提供监听或取消监听KIA文件拷贝、重命名和压缩事件的能力，当KIA文件发生变种时，通过回调函数，返回KIA变种信息。

## 接口说明

详细接口说明可参考[接口文档](../harmonyos-references/dataguard-fileguard.md)。

| 接口名 | 描述 |
| --- | --- |
| [on](../harmonyos-references/dataguard-fileguard.md#onkiacopy)(type: 'kiaCopy', callback: Callback<string>): void | 订阅KIA拷贝事件，需在业务初始化时注册。当用户拷贝KIA文件时会触发回调。 |
| [off](../harmonyos-references/dataguard-fileguard.md#offkiacopy)(type: 'kiaCopy', callback?: Callback<string>): void | 取消订阅KIA拷贝事件。 |
| [on](../harmonyos-references/dataguard-fileguard.md#onkiarename)(type: 'kiaRename', callback: Callback<string>): void | 订阅KIA重命名事件，需在业务初始化时注册。当用户重命名KIA文件时会触发回调。 |
| [off](../harmonyos-references/dataguard-fileguard.md#offkiarename)(type: 'kiaRename', callback?: Callback<string>): void | 取消订阅KIA重命名事件。 |
| [on](../harmonyos-references/dataguard-fileguard.md#onkiacompress)(type: 'kiaCompress', callback: Callback<string>): void | 订阅KIA压缩事件，需在业务初始化时注册。当用户压缩KIA文件时会触发回调。 |
| [off](../harmonyos-references/dataguard-fileguard.md#offkiacompress)(type: 'kiaCompress', callback?: Callback<string>): void | 取消订阅KIA压缩事件。 |

## 开发步骤

1. 导入模块。

   ```
   1. import { fileGuard } from '@kit.EnterpriseDataGuardKit';
   ```
2. 初始化[FileGuard](../harmonyos-references/dataguard-fileguard.md#fileguard)对象guard，调用接口on或off，订阅或取消订阅KIA文件拷贝、重命名和压缩事件。

   ```
   1. function onKiaCopyCallback(eventData: string) {
   2. console.info(`Succeeded in receiving kia copy eventData: ${eventData}.`);
   3. }
   4. function onKiaRenameCallback(eventData: string) {
   5. console.info(`Succeeded in receiving kia rename eventData: ${eventData}.`);
   6. }
   7. function onKiaCompressCallback(eventData: string) {
   8. console.info(`Succeeded in receiving kia compress eventData: ${eventData}.`);
   9. }

   11. function listenKIAEvent() {
   12. let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
   13. try {
   14. guard.on('kiaCopy', onKiaCopyCallback);
   15. guard.on('kiaRename', onKiaRenameCallback);
   16. guard.on('kiaCompress', onKiaCompressCallback);
   17. } catch (e) {
   18. console.error(`Failed to monitor the kia event. Code: ${e.code}, message: ${e.message}.`);
   19. }
   20. try {
   21. guard.off('kiaCopy');
   22. guard.off('kiaRename');
   23. guard.off('kiaCompress');
   24. } catch (e) {
   25. console.error(`Failed to cancel monitoring the kia event. Code: ${e.code}, message: ${e.message}.`);
   26. }
   27. }
   ```
