---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-file-backup-extension
title: 应用接入数据备份恢复
breadcrumb: 指南 > 应用框架 > Core File Kit（文件基础服务） > 应用文件 > 应用数据备份恢复 > 应用接入数据备份恢复
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:13+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e0b1cc756295d11cbedef0c9d2e45ae8ff4ff6d7b4d1857c909fe996437b8e6c
---

应用接入数据备份恢复需要通过BackupExtensionAbility实现。

BackupExtensionAbility是[Stage模型](stage-model-development-overview.md)中扩展组件[ExtensionAbility](extensionability-overview.md)的派生类。开发者可以通过修改配置文件定制备份恢复框架的行为，包括是否允许备份恢复，备份哪些文件等。

## 接口说明

备份恢复扩展能力关键接口如下表所示。API的接口使用指导请参见[BackupExtensionAbility API参考](../harmonyos-references/js-apis-application-backupextensionability.md#backupextensionability)和[BackupExtensionContext API参考](../harmonyos-references/js-apis-file-backupextensioncontext.md)。

| 接口名 | 描述 |
| --- | --- |
| onBackup(): void | 数据备份准备阶段，迁移备份数据前回调。 |
| onBackupEx(backupInfo: string): string | Promise<string> | 数据备份准备阶段，迁移备份数据前回调，支持传递备份信息和返回备份结果。 |
| onRestore(bundleVersion: BundleVersion): void | 数据恢复阶段，备份数据迁移完成后回调。 |
| onRestoreEx(bundleVersion: BundleVersion, restoreInfo: string): string | Promise<string> | 数据恢复阶段，备份数据迁移完成后回调，支持传递恢复信息和返回恢复结果。 |
| onRelease(scenario: number): Promise<void> | 备份或恢复完成时的特殊处理，备份或恢复完成时回调。  **说明**：从API version 20开始支持该接口。 |

## 约束与限制

* 当备份恢复时，所有待备份文件及目录的路径不得超过4095字节，否则将导致未定义行为。
* 当备份目录时，应用进程必须拥有读取该目录及其所有子目录的权限（DAC中的r），否则将导致备份失败。
* 当备份文件时，应用进程必须拥有搜索该文件所有祖父级目录的权限（DAC中的x），否则将导致备份失败。
* 当备份恢复时，所有待备份恢复的文件及目录不支持相对路径(../)和软链接。

## 开发步骤

1. 在应用配置文件module.json5中注册extensionAbilities相关配置

   新增"extensionAbilities"字段，其中注册类型"type"设置为"backup"，元数据信息["metadata"](../harmonyos-references/js-apis-bundlemanager-metadata.md)新增一个"name"为"ohos. extension. backup"的条目。

   BackupExtensionAbility配置文件示例：

   ```
   1. {
   2. "extensionAbilities": [
   3. {
   4. "description": "$string:ServiceExtAbility",
   5. "icon": "$media:icon",
   6. "name": "BackupExtensionAbility",
   7. "type": "backup",
   8. "exported": false,
   9. "metadata": [
   10. {
   11. "name": "ohos.extension.backup",
   12. "resource": "$profile:backup_config"
   13. }
   14. ],
   15. "srcEntry": "./ets/BackupExtension/BackupExtension.ets"
   16. }
   17. ]
   18. }
   ```
2. 新增元数据资源配置文件

   在元数据资源配置文件中，定义备份恢复时需要传输的文件。元数据资源配置文件名称需要与module.json5中"metadata.resource"例如"backup\_config.json"名称保持一致，其保存位置在工程的resources/base/profile文件夹下。

   元数据资源配置文件示例：

   ```
   1. {
   2. "allowToBackupRestore": true,
   3. "includes": [
   4. "/data/storage/el2/base/files/users/"
   5. ],
   6. "excludes": [
   7. "/data/storage/el2/base/files/users/hidden/"
   8. ],
   9. "fullBackupOnly": false,
   10. "restoreDeps": ""
   11. }
   ```
3. 开发者可以在BackupExtension.ets文件中自定义类继承的BackupExtensionAbility，通过重写其onBackup/onBackupEx和onRestore/onRestoreEx方法，使其达到在备份预加工应用数据或者在恢复阶段加工待恢复文件。

   如果没有特殊要求可以空实现，则备份恢复服务会按照统一的备份恢复数据规则进行备份恢复。

   下面的示例展示了一个空实现的BackupExtension.ets文件：

   ```
   1. // onBackup && onRestore
   2. import { BackupExtensionAbility, BundleVersion } from '@kit.CoreFileKit';
   3. import {hilog} from '@kit.PerformanceAnalysisKit';

   5. const TAG = `FileBackupExtensionAbility`;
   6. export default class BackupExtension extends  BackupExtensionAbility {
   7. // onBackup
   8. async onBackup ()   {
   9. hilog.info(0x0000, TAG, `onBackup ok`);
   10. }
   11. // onRestore
   12. async onRestore (bundleVersion : BundleVersion) {
   13. hilog.info(0x0000, TAG, `onRestore end`);
   14. }
   15. }
   ```

   ```
   1. import { BackupExtensionAbility } from '@kit.CoreFileKit';
   2. import { BundleVersion } from '@kit.CoreFileKit';
   3. // ...

   5. interface ErrorInfo {
   6. type: string,
   7. errorCode: number,
   8. errorInfo: string
   9. }

   11. // ...

   13. class BackupExt extends BackupExtensionAbility {
   14. // onBackupEx
   15. async onBackupEx(backupInfo: string): Promise<string> {
   16. console.info('onBackupEx ok');
   17. let errorInfo: ErrorInfo = {
   18. type: 'ErrorInfo',
   19. errorCode: 0,
   20. errorInfo: 'app diy error info'
   21. }
   22. return JSON.stringify(errorInfo);
   23. }

   25. // onRestoreEx
   26. async onRestoreEx(bundleVersion : BundleVersion, restoreInfo: string): Promise<string> {
   27. console.info(`onRestoreEx begin`);
   28. let errorInfo: ErrorInfo = {
   29. type: 'ErrorInfo',
   30. errorCode: 0,
   31. errorInfo: 'app diy error info'
   32. }
   33. return JSON.stringify(errorInfo);
   34. }
   35. // ...
   36. }
   ```

   [BackupExtension.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/CoreFile/FileBackupExtension/entry/src/main/ets/common/BackupExtension.ets#L16-L87)
4. 从API 20开始，开发者如需在应用备份恢复完成后执行一些特殊操作，例如清理备份或恢复时应用创建的临时文件，可以在BackupExtension.ets文件中自定义类继承的BackupExtensionAbility，通过重写其onRelease方法，当备份或恢复完成时，会执行onRelease方法以执行开发者自定义的行为。

   onRelease具有超时机制，应用若在5秒内未完成onRelease操作，将触发备份恢复结束时的应用进程退出流程。

   下面的示例展示了需要清理临时文件目录时onRelease的实现：

   ```
   1. import { BackupExtensionAbility } from '@kit.CoreFileKit';
   2. // ...
   3. import { fileIo } from '@kit.CoreFileKit';

   5. // ...

   7. const SCENARIO_BACKUP: number = 1;
   8. const SCENARIO_RESTORE: number = 2;
   9. // 需要清理的临时目录
   10. let filePath: string = '/data/storage/el2/base/.temp/';

   12. class BackupExt extends BackupExtensionAbility {
   13. // ...
   14. // onRelease
   15. async onRelease(scenario: number): Promise<void> {
   16. try {
   17. if (scenario == SCENARIO_BACKUP) {
   18. // 备份场景，应用自行实现处理，以清理备份产生的临时文件为例
   19. console.info(`onRelease begin`);
   20. await fileIo.rmdir(filePath);
   21. console.info(`onRelease end, rmdir succeed`);
   22. }
   23. if (scenario == SCENARIO_RESTORE) {
   24. // 恢复场景，应用自行实现处理，以清理恢复产生的临时文件为例
   25. console.info(`onRelease begin`);
   26. await fileIo.rmdir(filePath);
   27. console.info(`onRelease end, rmdir succeed`);
   28. }
   29. } catch (error) {
   30. console.error(`onRelease failed with error. Code: ${error.code}, message: ${error.message}`);
   31. }
   32. }
   33. }
   ```

   [BackupExtension.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/CoreFile/FileBackupExtension/entry/src/main/ets/common/BackupExtension.ets#L17-L88)

### 元数据资源配置文件说明

| 属性名称 | 数据类型 | 必填 | 含义 |
| --- | --- | --- | --- |
| allowToBackupRestore | 布尔值 | 是 | 是否允许备份恢复，默认为false。true为允许备份恢复，false为不允许备份恢复。 |
| includes | 字符串数组 | 否 | 应用沙箱中需要备份的文件和目录。  当模式串以非/开始时，表示一个相对于根路径的相对路径。  includes支持的路径清单列表如下述代码段内容所示，当配置includes时请确保配置路径范围包含在其中，**不支持备份el3、el4路径**。  当includes已配置时，备份恢复框架会采用开发者配置的模式串，否则将会采用下述代码段内容作为默认值。 |
| excludes | 字符串数组 | 否 | includes中无需备份的例外项。格式同includes。  在配置excludes时，请确保其范围在includes的子集中。  当excludes已配置时，备份恢复框架会采用开发者配置的模式串，否则将会采用**空数组**作为默认值。 |
| fullBackupOnly | 布尔值 | 否 | 是否使用应用默认恢复目录，默认值为false。当值为true时，恢复数据时会通过临时路径进行缓存，临时路径可通过[backupDir](../harmonyos-references/js-apis-file-backupextensioncontext.md#属性)获取。当值为false或者不配置该字段时，恢复数据会以'/'为根目录解压数据。 |
| restoreDeps | 字符串 | 否 | **不推荐使用**，应用恢复时依赖其他应用数据，默认值为""，需要配置依赖应用名称。当前仅支持最多一个依赖项。配置的依赖仅在一次恢复任务上下文生效，如果一次恢复任务中没有检测到依赖应用，则忽略该依赖描述继续执行恢复任务。**依赖应用未恢复或者恢复失败都会导致本应用恢复失败**。 |
| extraInfo | json串 | 否 | 额外信息可通过该字段传递。 |

**字段说明：**

1. **有关fullBackupOnly字段的说明**

   * 当fullBackupOnly为false时，恢复数据会以 **/** 为根目录解压数据，同路径下的同名文件会被覆盖。
   * 当fullBackupOnly为true时，恢复数据会以临时目录为根目录解压数据，开发者需要在OnRestore/OnRestoreEx内自行实现恢复数据的逻辑，进行最终的恢复。

   开发者可根据自身的业务场景，选择对应的恢复数据方式。

   **示例：**

   假设应用的数据备份路径为：**data/storage/el2/base/files/A/** 。那么在恢复时：

   * 如果配置了fullBackupOnly为false，数据会被直接解压到：**/data/storage/el2/base/files/A/** 目录下；
   * 如果配置了fullBackupOnly为true，数据则会被解压到：**临时路径backupDir + /restore/data/storage/el2/base/files/A/** 目录下。
2. **includes支持的路径清单列表如下：**

   ```
   1. {
   2. "includes": [
   3. "data/storage/el1/database/",
   4. "data/storage/el1/base/files/",
   5. "data/storage/el1/base/preferences/",
   6. "data/storage/el1/base/haps/*/files/",
   7. "data/storage/el1/base/haps/*/preferences/",
   8. "data/storage/el2/database/",
   9. "data/storage/el2/base/files/",
   10. "data/storage/el2/base/preferences/",
   11. "data/storage/el2/base/haps/*/files/",
   12. "data/storage/el2/base/haps/*/preferences/",
   13. "data/storage/el2/distributedfiles/",
   14. "data/storage/el5/database/",
   15. "data/storage/el5/base/files/",
   16. "data/storage/el5/base/preferences/",
   17. "data/storage/el5/base/haps/*/files/",
   18. "data/storage/el5/base/haps/*/preferences/"
   19. ]
   20. }
   ```
