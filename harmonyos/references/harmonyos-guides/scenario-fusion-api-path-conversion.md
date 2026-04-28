---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-fusion-api-path-conversion
title: 文件路径转换API
breadcrumb: 指南 > 应用服务 > Scenario Fusion Kit（融合场景服务） > 文件路径转换API
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:45+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:45a510656d986ed4c2c72c55ec6cd1ad786ad67d80503193644a9acb2c80d121
---

## 场景介绍

Scenario Fusion Kit提供文件路径转换的API，在HarmonyOS 4及以下到HarmonyOS 5及以上的升级场景和克隆场景，调用该接口可以将源文件路径转换为目标文件路径。

## 接口说明

以下是获取转换文件uri信息的接口说明，更多接口及使用方法请参见[fileUriService（文件路径转换API）](../harmonyos-references/scenario-fusion-fileuriresult.md)。

| 接口名 | 描述 |
| --- | --- |
| [convertFileUris](../harmonyos-references/scenario-fusion-fileuriresult.md#convertfileuris)(sourceFileUris: Array<string>): Promise<Array<[FileUriResult](../harmonyos-references/scenario-fusion-fileuriresult.md#fileuriresult)>> | 获取转换文件uri信息的请求对象。 |

## 开发步骤

1. 导入Scenario Fusion Kit模块以及相关公共模块。

   ```
   1. import { fileUriService } from '@kit.ScenarioFusionKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 传入待转换的文件路径参数列表，调用接口获取转换后的文件路径列表，代码如下：

   ```
   1. try {
   2. // '/storage/emulated/0/Pictures/test.gif'表示test.gif的文件路径。
   3. let sourceFileUris: Array<string> =
   4. ['100','content://media/external/files/10', '/storage/emulated/0/Pictures/test.gif',
   5. '/storage/emulated/0/media/com.test/test.mp4'];
   6. fileUriService.convertFileUris(sourceFileUris).then(result => {
   7. hilog.info(0x0000, 'testTag', 'succeeded in converting file uris');
   8. result.forEach(data => {
   9. switch (data.targetType) {
   10. case fileUriService.TargetType.UNKNOWN:
   11. hilog.info(0x0000, 'testTag', 'input uri or path is not exist');
   12. break;
   13. case fileUriService.TargetType.MEDIA:
   14. hilog.info(0x0000, 'testTag', 'converted media uri: %{public}s', data.targetUri);
   15. break;
   16. case fileUriService.TargetType.FILE:
   17. // 如果输入路径存在，结果中的targetUri将是转换后的URI。
   18. // 否则，targetUri 将与输入路径相同，targetType 将为 UNKNOWN。
   19. hilog.info(0x0000, 'testTag', 'converted file path: %{public}s', data.targetUri);
   20. break;
   21. }
   22. })
   23. }).catch((error: BusinessError) => {
   24. hilog.error(0x0000, 'testTag', 'Promise error: %{public}d %{public}s', error.code, error.message);
   25. });
   26. } catch (error) {
   27. hilog.error(0x0000, 'testTag', 'failReason: %{public}d %{public}s', error.code, error.message);
   28. }
   ```
