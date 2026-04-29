---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-backupextensioncontext
title: @ohos.file.BackupExtensionContext (备份恢复扩展能力)
breadcrumb: API参考 > 应用框架 > Core File Kit（文件基础服务） > ArkTS API > @ohos.file.BackupExtensionContext (备份恢复扩展能力)
category: harmonyos-references
scraped_at: 2026-04-29T13:56:15+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:e96ade74b12b76f83c990570821ccf1e4fbc22fa2c3cab1126ce3167da19b8d1
---

BackupExtensionContext是BackupExtension的上下文环境，继承自ExtensionContext。

BackupExtensionContext模块提供访问特定BackupExtension的资源的能力。对于扩展的BackupExtension，可直接将BackupExtensionContext作为上下文环境，或者定义一个继承自BackupExtensionContext的类型作为上下文环境。

说明

* 本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块接口仅可在Stage模型下使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import  { BackupExtensionContext } from '@kit.CoreFileKit';
```

## BackupExtensionContext

PhonePC/2in1TabletTVWearable

### 属性

PhonePC/2in1TabletTVWearable

**系统能力**：SystemCapability.FileManagement.StorageService.Backup

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| backupDir | string | 是 | 否 | 获取备份恢复时的临时路径，该路径只允许在备份恢复过程中作为临时路径使用，不允许应用将该路径作为其他用途来使用。目前只支持el1, el2路径，使用其他路径会返回空值。 |

### 使用场景

BackupExtensionContext主要用于获取备份恢复过程中的临时路径。

**示例：**

```
1. import { BackupExtensionAbility } from '@kit.CoreFileKit';
2. import { contextConstant } from '@kit.AbilityKit';

4. export default class MyBackupExtAbility extends BackupExtensionAbility {
5. async onBackup() {
6. console.info("onBackup begin");
7. // 使用者可通过改变 this.context.area 来进行切换el1，el2对应的沙箱路径
8. this.context.area = contextConstant.AreaMode.EL1;
9. // 使用者可通过 this.context.backupDir 对沙箱路径进行获取
10. let dir = this.context.backupDir;
11. console.info(`onBackup el1 dir: ${dir}`);
12. this.context.area = contextConstant.AreaMode.EL2;
13. dir = this.context.backupDir;
14. console.info(`onBackup el2 dir: ${dir}`);
15. console.info("onBackup end");
16. }

18. async onRestore() {
19. console.info("onRestore begin");
20. this.context.area = contextConstant.AreaMode.EL1;
21. let dir = this.context.backupDir;
22. console.info(`onRestore el1 dir: ${dir}`);
23. this.context.area = contextConstant.AreaMode.EL2;
24. dir = this.context.backupDir;
25. console.info(`onRestore el2 dir: ${dir}`);
26. console.info("onRestore end");
27. }
28. }
```
