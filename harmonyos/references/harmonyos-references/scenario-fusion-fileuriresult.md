---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/scenario-fusion-fileuriresult
title: fileUriService（文件路径转换API）
breadcrumb: API参考 > 应用服务 > Scenario Fusion Kit（融合场景服务） > ArkTS API > fileUriService（文件路径转换API）
category: harmonyos-references
scraped_at: 2026-09-02T14:53:31+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:3af0846727666282fd5d888ff3de99d40dcaee646d6a75e5934593b7e1013185
---

本模块为开发者在HarmonyOS 4及以下到HarmonyOS 5及以上的升级场景和克隆场景，调用该接口可以将源文件路径转换为目标文件路径。

**起始版本：** 5.0.2(14)

## 导入模块

```typescript
import { fileUriService } from '@kit.ScenarioFusionKit';
```

## FileUriResult

该类提供融合场景文件路径转换的对象。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ScenarioFusionComponent.FileUriService

**起始版本：** 5.0.2(14)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| sourceUri | string | 否 | 否 | 源文件路径。 |
| targetUri | string | 否 | 否 | 目标文件路径。 |
| targetType | [TargetType](scenario-fusion-fileuriresult.md#targettype) | 否 | 否 | 文件类型枚举。 |

## TargetType

该枚举定义了对象URI的类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ScenarioFusionComponent.FileUriService

**起始版本：** 5.0.2(14)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNKNOWN | 0 | 不确定文件类型。 |
| MEDIA | 1 | 媒体文件。 |
| FILE | 2 | 文管文件。 |

## convertFileUris

convertFileUris(sourceFileUris: Array<string>): Promise<Array<FileUriResult>>

调用该方法获取转换文件uri信息，使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ScenarioFusionComponent.FileUriService

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，从API版本26.0.0开始在Car、TV中可正常调用，在其他设备类型中返回801错误码。

**起始版本：** 5.0.2(14)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sourceFileUris | Array<string> | 是 | 待转换文件uri信息列表。列表数量范围：[1,100]，范围越界错误码：401 parameter error。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[FileUriResult](scenario-fusion-fileuriresult.md#fileuriresult)>> | Promise对象，返回[FileUriResult](scenario-fusion-fileuriresult.md#fileuriresult)对象数组。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](errorcode-universal.md#section401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```typescript
import { fileUriService } from '@kit.ScenarioFusionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // '/storage/emulated/0/Pictures/test.gif'表示test.gif的文件路径。
  let sourceFileUris: Array<string> =
    ['100', 'content://media/external/files/10', '/storage/emulated/0/Pictures/test.gif',
      '/storage/emulated/0/media/com.test/test.mp4'];
  fileUriService.convertFileUris(sourceFileUris).then(result => {
    hilog.info(0x0000, 'testTag', 'succeeded in converting file uris');
    result.forEach(data => {
      switch (data.targetType) {
        case fileUriService.TargetType.UNKNOWN:
          hilog.info(0x0000, 'testTag', 'input uri or path is not exist');
          break;
        case fileUriService.TargetType.MEDIA:
          hilog.info(0x0000, 'testTag', 'converted media uri: %{public}s', data.targetUri);
          break;
        case fileUriService.TargetType.FILE:
          // 如果输入路径存在，结果中的targetUri将是转换后的URI。
          // 否则，targetUri 将与输入路径相同，targetType 将为 UNKNOWN。
          hilog.info(0x0000, 'testTag', 'converted file path: %{public}s', data.targetUri);
          break;
      }
    });
  }).catch((error: BusinessError) => {
    hilog.error(0x0000, 'testTag', 'Promise error: %{public}d %{public}s', error.code, error.message);
  });
} catch (error) {
  hilog.error(0x0000, 'testTag', 'Failed to convert file uris, failReason: %{public}d %{public}s', error.code, error.message);
}
```
