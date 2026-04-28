---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/code-precautions
title: 应用升级过程代码开发注意事项
breadcrumb: 指南 > 应用框架 > Core File Kit（文件基础服务） > 应用文件 > 应用数据备份恢复 > 设备升级应用数据迁移适配指导 > 应用升级过程代码开发注意事项
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:17+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a0617c1e44c30a2769d57668f37ee2085d28a0db47dd6884a8b14c8bbc191f1f
---

## 区分升级场景和克隆场景

开发者需要区分升级场景和克隆场景时，可以重写BackupExtensionAbility中的onRestoreEx方法，通过restoreInfo预留字段进行场景区分。onRestoreEx方法详细使用指导请参考：[BackupExtensionAbility API参考](../harmonyos-references/js-apis-application-backupextensionability.md#backupextensionability)。

示例代码如下所示：

```
1. import { BackupExtensionAbility, BundleVersion } from '@kit.CoreFileKit';

3. const TAG = `BackupExtensionAbility`;

5. interface ErrorInfo {
6. type: string,
7. errorCode: number,
8. errorInfo: string
9. }

11. interface DetailInfo {
12. type: string,
13. detail: string
14. }

16. export default class EntryBackupAbility extends BackupExtensionAbility {
17. async onBackup() {
18. console.info(TAG, 'onBackup ok');
19. }

21. async onRestoreEx(bundleVersion: BundleVersion, restoreInfo: string): Promise<string> {
22. console.info(TAG, `onRestoreEx ok ${JSON.stringify(bundleVersion)}`);
23. let errorInfo: ErrorInfo = {
24. type: "ErrorInfo",
25. errorCode: 0,
26. errorInfo: "app diy error info"
27. }
28. if (bundleVersion.name.startsWith("0.0.0.0")){
29. // 在此处实现终端设备从HarmonyOS 4.x到HarmonyOS NEXT的应用数据处理。
30. // 涉及异步操作请进行同步等待
31. console.info(TAG, `HarmonyOS to HarmonyOS NEXT scenario`);

33. // 如果升级场景与克隆场景没有差异化数据处理诉求，此处可以忽略。
34. if (this.IsOtaScenario(restoreInfo)) {
35. // 在此处实现终端设备从HarmonyOS 4.x到HarmonyOS NEXT升级场景的特有数据处理。无特殊要求，此处可以忽略。
36. console.info(TAG, `Ota Scenario`)
37. } else {
38. // 在此处实现终端设备从HarmonyOS 4.x到HarmonyOS NEXT克隆场景的特有数据处理。无特殊要求，此处可以忽略。
39. console.info(TAG, `Clone Scenario`)
40. }
41. } else {
42. // 在此处实现从HarmonyOS NEXT设备迁移到HarmonyOS NEXT设备后，应用数据的处理。无特殊要求，可以空实现。
43. // 涉及异步操作请进行同步等待
44. console.info(TAG, `Other scenario`);
45. }
46. return JSON.stringify(errorInfo);
47. }

49. /**
50. * 判断是否是升级场景
51. * @param restoreInfo 预留字段，应用恢复过程中需要的扩展参数
52. * @returns 升级场景返回true，否则返回false
53. */
54. IsOtaScenario(restoreInfo: string): boolean {
55. let details:Array<DetailInfo> = JSON.parse(restoreInfo);
56. return details.some((detailInfo) => {
57. //设备从HarmonyOS 4.x升级到HarmonyOS NEXT/5.0.x场景判断条件
58. return detailInfo.type == 'isSameDevice' && detailInfo.detail == 'true';
59. });
60. }
61. }
```

## 公共目录文件URI继承

### 场景说明

应用在HarmonyOS 3.1 Release API 9及更低版本运行时，开发者可通过记录公共媒体库中文件的URI或者路径，用于后续的文件访问。 当终端设备从HarmonyOS升级到HarmonyOS NEXT后，公共媒体库中的文件会由系统整体搬迁至新位置，直接继承。导致应用记录的旧有URI或者路径不可使用。

为解决该问题，系统提供数据迁移公共目录文件继承方案，支持应用将记录的HarmonyOS公共媒体库文件URI或者路径转换为对应的HarmonyOS NEXT公共媒体库文件URI或者路径，并且返回对应文件类型。当应用需要在HarmonyOS NEXT中访问公共媒体库中的文件时，可以使用转换后的HarmonyOS NEXT公共媒体库文件URI或者路径，通过HarmonyOS NEXT提供的公共媒体库API进行授权访问。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/CBTlGAQKRoC4ImlYJFSn0Q/zh-cn_image_0000002583478279.png?HW-CC-KV=V1&HW-CC-Date=20260427T234115Z&HW-CC-Expire=86400&HW-CC-Sign=8FE2D7F47AC9FA56DDF331BE9EFD58FD33B8E4503A0049AF4EE913B594B82053)

### 代码实现

应用可以调用Scenario Fusion Kit的接口[convertFileUris()](../harmonyos-references/scenario-fusion-fileuriresult.md#section1272664195920)，将记录的HarmonyOS公共媒体库文件URI或者路径转换为HarmonyOS NEXT可访问的URI或者路径，并获取到对应文件类型。其中媒体文件类型请参考[继承媒体文件访问权限](medialibrary-request-photouris-permission.md)，其他类型文件可通过[基础文件接口](app-file-access.md)进行操作。convertFileUris()接口详细使用指导请参考：[基于融合场景服务实现文件路径转换参考指导](scenario-fusion-api-path-conversion.md)。

说明

开发者可以在数据迁移的过程中，通过该接口将HarmonyOS公共媒体库文件URI或者路径转换为对应的HarmonyOS NEXT公共媒体库文件URI或者路径，并重新保存，便于后续使用。
