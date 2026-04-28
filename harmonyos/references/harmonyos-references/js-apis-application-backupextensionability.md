---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-application-backupextensionability
title: @ohos.application.BackupExtensionAbility (备份恢复扩展能力)
breadcrumb: API参考 > 应用框架 > Core File Kit（文件基础服务） > ArkTS API > @ohos.application.BackupExtensionAbility (备份恢复扩展能力)
category: harmonyos-references
scraped_at: 2026-04-28T08:05:41+08:00
doc_updated_at: 2026-03-19
content_hash: sha256:312ab2daac2d14f402331072ee105e94f29285290db7f0bb560a071397c3c555
---

BackupExtensionAbility模块提供备份恢复服务相关扩展能力，为应用提供扩展的备份恢复能力。

说明

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块接口仅可在Stage模型下使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { BackupExtensionAbility, BundleVersion } from '@kit.CoreFileKit';
```

## BundleVersion

PhonePC/2in1TabletTVWearable

恢复时所需要的版本信息，开发者可根据配置的版本号来判断本次恢复时的应用版本数据。

**系统能力**：SystemCapability.FileManagement.StorageService.Backup

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| code | number | 否 | 否 | 应用的版本号。 |
| name | string | 否 | 否 | 应用的版本名称。 |

## BackupExtensionAbility

PhonePC/2in1TabletTVWearable

应用接入数据备份恢复需要通过BackupExtensionAbility实现，开发者可以通过[onBackup](js-apis-application-backupextensionability.md#onbackup)，[onRestore](js-apis-application-backupextensionability.md#onrestore)来实现自定义的备份恢复操作。

### 属性

PhonePC/2in1TabletTVWearable

**系统能力**：SystemCapability.FileManagement.StorageService.Backup

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| context11+ | [BackupExtensionContext](js-apis-file-backupextensioncontext.md) | 否 | 否 | BackupExtensionAbility的上下文环境，继承自[ExtensionContext](js-apis-inner-application-extensioncontext.md)。 |

### onBackup

PhonePC/2in1TabletTVWearable

onBackup(): void

Extension生命周期回调，在执行备份数据时回调，由开发者提供扩展的备份数据的操作。

**系统能力**：SystemCapability.FileManagement.StorageService.Backup

**示例：**

```
1. class BackupExt extends BackupExtensionAbility {
2. async onBackup() {
3. console.info('onBackup');
4. }
5. }
```

### onBackupEx12+

PhonePC/2in1TabletTVWearable

onBackupEx(backupInfo: string): string | Promise<string>

备份恢复框架增加扩展参数，允许应用备份、恢复时传递参数给应用。支持异步操作，使用Promise异步回调。

onBackupEx与onBackup互斥，如果重写onBackupEx，则优先调用onBackupEx。

onBackupEx返回值不能为空字符串，若onBackupEx返回值为空字符串，则会尝试调用onBackup。

**系统能力**：SystemCapability.FileManagement.StorageService.Backup

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| backupInfo | string | 是 | 扩展恢复数据的特殊处理接口中三方应用需要传递的包信息。  backupInfo可能为空字符串，需要开发者针对空字符串场景做判断处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | Promise<string> | 返回应用执行自定义备份操作的信息，包含备份结果和报错信息，返回值为Json格式。  异步返回Promise对象。  同步返回string。 |

说明

同步处理业务场景中，推荐使用示例如下。

**示例：**

```
1. import { BackupExtensionAbility, BundleVersion } from '@kit.CoreFileKit';

3. interface ErrorInfo {
4. type: string,
5. errorCode: number,
6. errorInfo: string
7. }
8. class BackupExt extends BackupExtensionAbility {
9. onBackupEx(backupInfo: string): string {
10. try {
11. if (backupInfo == "") {
12. // 当backupInfo为空时，应用根据业务自行做处理。
13. console.info("backupInfo is empty");
14. }
15. console.info(`onBackupEx ok`);
16. let errorInfo: ErrorInfo = {
17. type: "ErrorInfo",
18. errorCode: 0,
19. errorInfo: "app customized error info"
20. }
21. return JSON.stringify(errorInfo);
22. } catch (err) {
23. console.error(`BackupExt error. Code:${err.code}, message:${err.message}`);
24. }
25. return "";
26. }
27. }
```

说明

异步处理业务场景中，推荐使用示例如下。

**示例：**

```
1. import { BackupExtensionAbility, BundleVersion } from '@kit.CoreFileKit';

3. interface ErrorInfo {
4. type: string,
5. errorCode: number,
6. errorInfo: string
7. }
8. class BackupExt extends BackupExtensionAbility {
9. // 异步实现
10. async onBackupEx(backupInfo: string): Promise<string> {
11. try {
12. if (backupInfo == "") {
13. // 当backupInfo为空时，应用根据业务自行做处理。
14. console.info("backupInfo is empty");
15. }
16. console.info(`onBackupEx ok`);
17. let errorInfo: ErrorInfo = {
18. type: "ErrorInfo",
19. errorCode: 0,
20. errorInfo: "app customized error info"
21. }
22. return JSON.stringify(errorInfo);
23. } catch (err) {
24. console.error(`BackupExt error. Code:${err.code}, message:${err.message}`);
25. }
26. return "";
27. }
28. }
```

### onRestore

PhonePC/2in1TabletTVWearable

onRestore(bundleVersion: BundleVersion): void

Extension生命周期回调，在执行恢复数据时回调，由开发者提供扩展的恢复数据的操作。

**系统能力**：SystemCapability.FileManagement.StorageService.Backup

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bundleVersion | [BundleVersion](js-apis-application-backupextensionability.md#bundleversion) | 是 | 恢复时应用数据所在的版本信息。 |

**示例：**

```
1. import { BackupExtensionAbility, BundleVersion } from '@kit.CoreFileKit';

3. class BackupExt extends BackupExtensionAbility {
4. async onRestore(bundleVersion : BundleVersion) {
5. console.info(`onRestore ok ${JSON.stringify(bundleVersion)}`);
6. }
7. }
```

### onRestoreEx12+

PhonePC/2in1TabletTVWearable

onRestoreEx(bundleVersion: BundleVersion, restoreInfo: string): string | Promise<string>

Extension生命周期回调，在执行恢复数据时回调，由开发者提供扩展的恢复数据的操作，支持异步操作，使用Promise异步回调。

onRestoreEx与onRestore互斥，如果重写onRestoreEx，则优先调用onRestoreEx。

onRestoreEx返回值不能为空字符串，若onRestoreEx返回值为空字符串，则会尝试调用onRestore。

onRestoreEx的返回值为Json格式，使用方法见示例代码。

**系统能力**：SystemCapability.FileManagement.StorageService.Backup

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bundleVersion | [BundleVersion](js-apis-application-backupextensionability.md#bundleversion) | 是 | 恢复时应用数据所在的版本信息。 |
| restoreInfo | string | 是 | 预留字段，应用恢复过程中需要的扩展参数。  restoreInfo可能为空字符串，需要开发者针对空字符串场景做判断处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | Promise<string> | 返回应用执行自定义恢复操作的信息，包含恢复结果和报错信息，返回值为Json格式。  异步返回Promise对象。  同步返回string。 |

说明

异步处理业务场景中，推荐使用示例如下。

**示例：**

```
1. import { BackupExtensionAbility, BundleVersion } from '@kit.CoreFileKit';
2. interface ErrorInfo {
3. type: string,
4. errorCode: number,
5. errorInfo: string
6. }
7. class BackupExt extends BackupExtensionAbility {
8. // 异步实现
9. async onRestoreEx(bundleVersion : BundleVersion, restoreInfo: string): Promise<string> {
10. try {
11. if (restoreInfo == "") {
12. // 当restoreInfo为空时，应用根据业务自行做处理。
13. console.info("restoreInfo is empty");
14. }
15. console.info(`onRestoreEx ok ${JSON.stringify(bundleVersion)}`);
16. let errorInfo: ErrorInfo = {
17. type: "ErrorInfo",
18. errorCode: 0,
19. errorInfo: "app customized error info"
20. }
21. return JSON.stringify(errorInfo);
22. } catch (err) {
23. console.error(`onRestoreEx error. Code:${err.code}, message:${err.message}`);
24. }
25. return "";
26. }
27. }
```

说明

同步处理业务场景中，推荐使用示例如下。

**示例：**

```
1. import { BackupExtensionAbility, BundleVersion } from '@kit.CoreFileKit';
2. interface ErrorInfo {
3. type: string,
4. errorCode: number,
5. errorInfo: string
6. }

8. class BackupExt extends BackupExtensionAbility {
9. // 同步实现
10. onRestoreEx(bundleVersion : BundleVersion, restoreInfo: string): string {
11. try {
12. if (restoreInfo == "") {
13. // 当restoreInfo为空时，应用根据业务自行做处理。
14. console.info("restoreInfo is empty");
15. }
16. console.info(`onRestoreEx ok ${JSON.stringify(bundleVersion)}`);
17. let errorInfo: ErrorInfo = {
18. type: "ErrorInfo",
19. errorCode: 0,
20. errorInfo: "app customized error info"
21. }
22. return JSON.stringify(errorInfo);
23. } catch (err) {
24. console.error(`onRestoreEx error. Code:${err.code}, message:${err.message}`);
25. }
26. return "";
27. }
28. }
```

### onProcess12+

PhonePC/2in1TabletTVWearable

onProcess(): string

备份恢复框架增加进度返回接口。该接口为同步接口，由应用在执行onBackup(onBackupEx)/onRestore(onRestoreEx)期间进行实现。返回应用自身处理业务的进度，返回值为json结构，使用方法见示例代码。

**系统能力**：SystemCapability.FileManagement.StorageService.Backup

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回应用onBackup或者onRestore执行过程中处理数据的进度信息（返回值为Json格式）。 |

说明

* onProcess可以不实现，系统有默认处理机制；若要实现，返回值结构严格按照示例代码返回。
* onProcess具有超时机制，执行不可超过1秒，系统每5秒调用一次onProcess，累计3次超时后，直接结束应用当前备份或恢复任务。
* 实现onProcess时，业务需要将onBackup(onBackupEx)/onRestore(onRestoreEx)做异步实现，且需要单独开辟子线程，否则onProcess相关功能无法正常运行。具体使用方式见示例代码。
* onProcess()推荐使用示例如下。

**示例：**

```
1. import { BackupExtensionAbility } from '@kit.CoreFileKit';
2. import { taskpool } from '@kit.ArkTS';

4. @Sendable
5. class MigrateProgressInfo {
6. private migrateProgress: string = '';
7. private name: string = "test"; // appName
8. private processed: number = 0; // 已处理的数据
9. private total: number = 100; // 总数
10. private isPercentage: boolean = true // 可选字段，true表示需要按百分比的格式化展示进度，false或者不实现该字段表示按具体项数展示进度

12. getMigrateProgress(): string {
13. this.migrateProgress = `{"progressInfo": [{"name": ${this.name}, "processed": ${this.processed}, "total": ${
14. this.total}, "isPercentage": ${this.isPercentage}}]}`;
15. return this.migrateProgress;
16. }

18. updateProcessed(processed: number) {
19. this.processed = processed;
20. }
21. }

23. class BackupExt extends BackupExtensionAbility {
24. private progressInfo: MigrateProgressInfo = new MigrateProgressInfo();

26. // 如下代码中，appJob方法为模拟的实际业务代码，args为appJob方法的参数，用于提交到taskpool中，开启子线程进行工作
27. async onBackup() {
28. console.info(`onBackup begin`);
29. let args = 100; // args为appJob方法的参数
30. let jobTask: taskpool.Task = new taskpool.LongTask(appJob, this.progressInfo, args);
31. try {
32. await taskpool.execute(jobTask, taskpool.Priority.LOW);
33. } catch (error) {
34. console.error("onBackup error." + error.message);
35. }
36. taskpool.terminateTask(jobTask); // 需要手动销毁
37. console.info(`onBackup end`);
38. }

40. async onRestore() {
41. console.info(`onRestore begin`);
42. let args = 100; // args为appJob方法的参数
43. let jobTask: taskpool.Task = new taskpool.LongTask(appJob, this.progressInfo, args);
44. try {
45. await taskpool.execute(jobTask, taskpool.Priority.LOW);
46. } catch (error) {
47. console.error("onRestore error." + error.message);
48. }
49. taskpool.terminateTask(jobTask); // 需要手动销毁
50. console.info(`onRestore end`);
51. }

54. onProcess(): string {
55. console.info(`onProcess begin`);
56. return this.progressInfo.getMigrateProgress();
57. }
58. }

60. @Concurrent
61. function appJob(progressInfo: MigrateProgressInfo, args: number) : string {
62. console.info(`appJob begin, args is: ` + args);
63. // 在业务执行时刷新已处理进度
64. let currentProcessed: number = 0;
65. // 模拟业务实际逻辑
66. for (let i = 0; i < args; i++) {
67. currentProcessed = i;
68. progressInfo.updateProcessed(currentProcessed);
69. }
70. return "ok";
71. }
```

### onRelease20+

PhonePC/2in1TabletTVWearable

onRelease(scenario: number): Promise<void>

备份恢复框架安全退出接口。应用备份或恢复完成时回调，应用可实现备份恢复完成后的一些特殊处理，例如清理备份或恢复产生的临时文件。使用Promise异步回调。

onRelease具有超时机制，应用若在5秒内未完成onRelease操作，将触发备份恢复结束时的应用进程退出流程。

**系统能力**：SystemCapability.FileManagement.StorageService.Backup

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scenario | number | 是 | 表示处于备份或恢复场景。  scenario = 1表示当前为备份场景。  scenario = 2表示当前为恢复场景。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**示例：**

```
1. // 以清理文件为例
2. import { BackupExtensionAbility, fileIo } from '@kit.CoreFileKit';

4. const SCENARIO_BACKUP: number = 1;
5. const SCENARIO_RESTORE: number = 2;
6. // 需要清理的临时目录
7. let filePath: string = '/data/storage/el2/base/.temp/';

9. class BackupExt extends BackupExtensionAbility {
10. async onRelease(scenario: number): Promise<void> {
11. try {
12. if (scenario == SCENARIO_BACKUP) {
13. // 备份场景，应用自行实现处理，以清理备份产生的临时文件为例
14. console.info(`onRelease begin`);
15. await fileIo.rmdir(filePath);
16. console.info(`onRelease end, rmdir succeed`);
17. }
18. if (scenario == SCENARIO_RESTORE) {
19. // 恢复场景，应用自行实现处理，以清理恢复产生的临时文件为例
20. console.info(`onRelease begin`);
21. await fileIo.rmdir(filePath);
22. console.info(`onRelease end, rmdir succeed`);
23. }
24. } catch (error) {
25. console.error(`onRelease failed with error. Code: ${error.code}, message: ${error.message}`);
26. }
27. }
28. }
```
