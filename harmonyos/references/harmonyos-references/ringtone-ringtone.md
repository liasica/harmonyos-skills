---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ringtone-ringtone
title: ringtone（铃声服务）
breadcrumb: API参考 > 媒体 > Ringtone Kit（铃声服务） > ArkTS API > ringtone（铃声服务）
category: harmonyos-references
scraped_at: 2026-09-02T14:53:03+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ab98045a5804cd3a753e66aedb7203c3faeff61d1f2e12aa6673da39db711f58
---

ringtone提供铃声设置的功能。

**起始版本：** 5.0.0(12)

## 导入模块

```typescript
import { ringtone } from '@kit.RingtoneKit';
```

## RingtoneType

描述铃声的类型枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ringtone.Core

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CALL | 0 | 来电铃声。 |
| MESSAGE | 1 | 信息铃声。 |
| NOTIFICATION | 2 | 通知铃声。 |
| ALARM | 3 | 闹钟铃声。 |

## RingtoneErrors

该枚举为设置铃声，获取铃声支持类型和获取铃声支持文件类型等接口的错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ringtone.Core

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ERROR\_INVALID\_PARAM | 401 | 参数非法。 |
| ERROR\_USER\_CANCELED | 1011600001 | 用户取消。 |
| ERROR\_FILE\_NOT\_FOUND | 1011600002 | 文件不存在。 |
| ERROR\_SHOW\_FAILED | 1011600003 | 铃声弹框失败。 |
| ERROR\_CALL\_SYSTEM\_API\_FAILED | 1011600004 | 调用系统接口失败。 |
| ERROR\_DATA\_TYPE\_NOT\_MATCHED | 1011600005 | 文件类型不匹配。**起始版本：** 26.0.0 |
| ERROR\_SYSTEM | 1011699999 | 系统内部错误。 |

## ringtone.getSupportedRingtoneTypes

getSupportedRingtoneTypes(): Array<RingtoneType>

查询当前系统支持自定义的铃声类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ringtone.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[RingtoneType](ringtone-ringtone.md#ringtonetype)> | 当前系统支持自定义的铃声类型。 |

**示例：**

```typescript
import { ringtone } from '@kit.RingtoneKit';
import { JSON } from '@kit.ArkTS';
import { hilog } from '@kit.PerformanceAnalysisKit';

const APP_TAG = 'Msc_Demo'
const DOMAIN = 0x0001

@Entry
@Component
struct Index {
  build() {
    Stack() {
      Column() {
        Button('查询当前系统支持自定义的铃声类型')
          .width(200)
          .height(50)
          .onClick(() => {
            let typeList: ringtone.RingtoneType[] = ringtone.getSupportedRingtoneTypes()
            hilog.info(DOMAIN, APP_TAG, `getSupportedRingtoneTypes: ${JSON.stringify(typeList)}`);
          })
      }
      .width('100%')
      .height('100%')
      .backgroundColor(Color.Pink)
    }
    .height('100%')
    .width('100%')
  }
}
```

## ringtone.getSupportedRingtoneTypes

getSupportedRingtoneTypes(mediaType: uniformTypeDescriptor.UniformDataType): Array<RingtoneType>

查询当前系统支持自定义的铃声类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ringtone.Core

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mediaType | [uniformTypeDescriptor.UniformDataType](js-apis-data-uniformtypedescriptor.md#uniformdatatype) | 是 | 待查询的文件类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[RingtoneType](ringtone-ringtone.md#ringtonetype)> | 当前系统支持自定义的铃声类型。 |

**示例：**

```typescript
import { ringtone } from '@kit.RingtoneKit';
import { JSON } from '@kit.ArkTS';
import { uniformTypeDescriptor } from '@kit.ArkData';
import { hilog } from '@kit.PerformanceAnalysisKit';

const APP_TAG = 'Msc_Demo'
const DOMAIN = 0x0001

@Entry
@Component
struct Index {
  build() {
    Stack() {
      Column() {
        Button('查询当前系统支持自定义的铃声类型')
          .width(200)
          .height(50)
          .onClick(() => {
            let typeList: ringtone.RingtoneType[] = ringtone.getSupportedRingtoneTypes(uniformTypeDescriptor.UniformDataType.AUDIO)
            hilog.info(DOMAIN, APP_TAG, `getSupportedRingtoneTypes: ${JSON.stringify(typeList)}`);
          })
      }
      .width('100%')
      .height('100%')
      .backgroundColor(Color.Pink)
    }
    .height('100%')
    .width('100%')
  }
}
```

## ringtone.getSupportedDataTypes

getSupportedDataTypes(ringtoneType: RingtoneType): Array<uniformTypeDescriptor.UniformDataType>

查询对应铃声类型支持的文件类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ringtone.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ringtoneType | [RingtoneType](ringtone-ringtone.md#ringtonetype) | 是 | 待查询的铃声类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[uniformTypeDescriptor.UniformDataType](js-apis-data-uniformtypedescriptor.md#uniformdatatype)> | 返回对应铃声类型支持的文件类型。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:ringtoneType is invalid. |

**示例：**

```typescript
import { ringtone } from '@kit.RingtoneKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { uniformTypeDescriptor } from '@kit.ArkData';
import { JSON } from '@kit.ArkTS';
import { hilog } from '@kit.PerformanceAnalysisKit';

const APP_TAG = 'Msc_Demo'
const DOMAIN = 0x0001

@Entry
@Component
struct Index {
  build() {
    Stack() {
      Column() {
        Button('查询支持的文件类型')
          .width(200)
          .height(50)
          .onClick(() => {
            try {
              let typeList: uniformTypeDescriptor.UniformDataType[] =
                ringtone.getSupportedDataTypes(ringtone.RingtoneType.NOTIFICATION)
              hilog.info(DOMAIN, APP_TAG, `getSupportedDataType: ${JSON.stringify(typeList)}`);
            } catch (error) {
              let err: BusinessError = error as BusinessError;
              hilog.error(DOMAIN, APP_TAG,
                `getSupportedDataType error message: ${err.message}, error code: ${err.code}`);
            }
          })
      }
      .width('100%')
      .height('100%')
      .backgroundColor(Color.Pink)
    }
    .height('100%')
    .width('100%')
  }
}
```

## ringtone.getSupportedMaxDuration

getSupportedMaxDuration(ringtoneType: RingtoneType, dataType: uniformTypeDescriptor.UniformDataType): number

查询不同铃声类型和文件类型对应的文件时长上限。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ringtone.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ringtoneType | [RingtoneType](ringtone-ringtone.md#ringtonetype) | 是 | 待查询的铃声类型。 |
| dataType | [uniformTypeDescriptor.UniformDataType](js-apis-data-uniformtypedescriptor.md#uniformdatatype) | 是 | 待查询的文件类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回对应类型的铃声和文件支持的最大时长（单位：s），其中闹钟铃声时长为300s，短信铃声和通知铃声时长为7s，来电铃声时长为60s。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:data type does not match the ringtone type. |

**示例：**

```typescript
import { ringtone } from '@kit.RingtoneKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { uniformTypeDescriptor } from '@kit.ArkData';
import { hilog } from '@kit.PerformanceAnalysisKit';

const APP_TAG = 'Msc_Demo'
const DOMAIN = 0x0001

@Entry
@Component
struct Index {
  build() {
    Stack() {
      Column() {
        Button('查询最大时长')
          .width(200)
          .height(50)
          .onClick(() => {
            try {
              let maxDuration: number =
                ringtone.getSupportedMaxDuration(ringtone.RingtoneType.MESSAGE,
                  uniformTypeDescriptor.UniformDataType.MP3)
              hilog.info(DOMAIN, APP_TAG, `getSupportedMaxDuration: ${maxDuration}`);
            } catch (error) {
              let err: BusinessError = error as BusinessError;
              hilog.error(DOMAIN, APP_TAG,
                `getSupportedMaxDuration error message: ${err.message}, error code: ${err.code}`);
            }
          })
      }
      .width('100%')
      .height('100%')
      .backgroundColor(Color.Pink)
    }
    .height('100%')
    .width('100%')
  }
}
```

## ringtone.getSupportedMaxSize

getSupportedMaxSize(ringtoneType: RingtoneType, dataType: uniformTypeDescriptor.UniformDataType): number

查询不同铃声类型和文件类型对应的文件大小上限。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ringtone.Core

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ringtoneType | [RingtoneType](ringtone-ringtone.md#ringtonetype) | 是 | 待查询的铃声类型。 |
| dataType | [uniformTypeDescriptor.UniformDataType](js-apis-data-uniformtypedescriptor.md#uniformdatatype) | 是 | 待查询的文件类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回对应类型的铃声和文件支持的最大文件大小（单位：kb），其中视频大小限制200MB及以下，音频大小无限制返回-1。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-ringtone.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1011600005 | The data type does not match the ringtone type. |

**示例：**

```typescript
import { ringtone } from '@kit.RingtoneKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { uniformTypeDescriptor } from '@kit.ArkData';
import { hilog } from '@kit.PerformanceAnalysisKit';

const APP_TAG = 'Msc_Demo'
const DOMAIN = 0x0001

@Entry
@Component
struct Index {
  build() {
    Stack() {
      Column() {
        Button('查询文件大小限制')
          .width(200)
          .height(50)
          .onClick(() => {
            try {
              let maxSize: number =
                ringtone.getSupportedMaxSize(ringtone.RingtoneType.CALL,
                  uniformTypeDescriptor.UniformDataType.MP3)
              hilog.info(DOMAIN, APP_TAG, `getSupportedMaxSize: ${maxSize}`);
            } catch (error) {
              let err: BusinessError = error as BusinessError;
              hilog.error(DOMAIN, APP_TAG,
                `getSupportedMaxSize error message: ${err.message}, error code: ${err.code}`);
            }
          })
      }
      .width('100%')
      .height('100%')
      .backgroundColor(Color.Pink)
    }
    .height('100%')
    .width('100%')
  }
}
```

## ringtone.startRingtoneSetting

startRingtoneSetting(context: common.UIAbilityContext, path: string, name: string, callback: AsyncCallback<RingtoneType>): void

拉起设置铃声弹窗，并返回点击的铃声类型，使用Callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ringtone.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | common.[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 是 | UIAbility上下文。 |
| path | string | 是 | 具有访问权限的文件路径。 |
| name | string | 是 | 文件名，限制长度1000字符。 |
| callback | AsyncCallback<[RingtoneType](ringtone-ringtone.md#ringtonetype)> | 是 | 回调函数。返回用户选择设置的铃声类型。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-ringtone.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: context is invalid. |
| 1011600001 | User canceled. |
| 1011600002 | The media file is not found. |
| 1011600003 | Failed to show the dialog box. |
| 1011600004 | Failed to call the system API. |
| 1011699999 | System exception. |

**示例：**

```typescript
import { common } from '@kit.AbilityKit';
import { ringtone } from '@kit.RingtoneKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { JSON } from '@kit.ArkTS';
import { hilog } from '@kit.PerformanceAnalysisKit';

const APP_TAG = 'Msc_Demo'
const DOMAIN = 0x0001

@Entry
@Component
struct Index {
  private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

  build() {
    Stack() {
      Column() {
        Button('设为铃声OGG格式')
          .width(200)
          .height(50)
          .onClick(() => {
            let audioPath: string = this.context.filesDir + '/test.ogg'
            let splitList = audioPath.split('/')
            let fileName = splitList[splitList.length - 1]
            hilog.info(DOMAIN, APP_TAG, `audioPath: ${audioPath}`)
            hilog.info(DOMAIN, APP_TAG, `fileName: ${fileName}`)

            try {
              ringtone.startRingtoneSetting(this.context, audioPath, fileName, (err, res) => {
                hilog.info(DOMAIN, APP_TAG, `返回值：${JSON.stringify(res)}`)
              })
            } catch (error) {
              let err: BusinessError = error as BusinessError;
              hilog.error(DOMAIN, APP_TAG,
                `accessSync failed with error message: ${err.message}, error code: ${err.code}`);
            }
          })
      }
      .width('100%')
      .height('100%')
      .backgroundColor(Color.Pink)
    }
    .height('100%')
    .width('100%')
  }
}
```

## ringtone.startRingtoneSetting

startRingtoneSetting(context: common.UIAbilityContext, path: string, name: string): Promise<RingtoneType>

拉起设置铃声弹窗，并返回点击的铃声类型，使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ringtone.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | common.[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 是 | UIAbility上下文。 |
| path | string | 是 | 具有访问权限的文件路径。 |
| name | string | 是 | 文件名，限制长度1000字符。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[RingtoneType](ringtone-ringtone.md#ringtonetype)> | Promise对象。返回用户选择设置的铃声类型。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-ringtone.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: context is invalid. |
| 1011600001 | User canceled. |
| 1011600002 | The media file is not found. |
| 1011600003 | Failed to show the dialog box. |
| 1011600004 | Failed to call the system API. |
| 1011699999 | System exception. |

**示例：**

```typescript
import { common } from '@kit.AbilityKit';
import { ringtone } from '@kit.RingtoneKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { JSON } from '@kit.ArkTS';
import { hilog } from '@kit.PerformanceAnalysisKit';

const APP_TAG = 'Msc_Demo'
const DOMAIN = 0x0001

@Entry
@Component
struct Index {
  private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

  build() {
    Stack() {
      Column() {
        Button('设为铃声OGG格式')
          .width(200)
          .height(50)
          .onClick(() => {
            let audioPath: string = this.context.filesDir + '/test.ogg'
            let splitList = audioPath.split('/')
            let fileName = splitList[splitList.length - 1]
            hilog.info(DOMAIN, APP_TAG, `audioPath: ${audioPath}`)
            hilog.info(DOMAIN, APP_TAG, `fileName: ${fileName}`)

            try {
              ringtone.startRingtoneSetting(this.context, audioPath, fileName).then(res => {
                hilog.info(DOMAIN, APP_TAG, `返回值：${JSON.stringify(res)}`)
              })
            } catch (error) {
              let err: BusinessError = error as BusinessError;
              hilog.error(DOMAIN, APP_TAG,
                `accessSync failed with error message: ${err.message}, error code: ${err.code}`);
            }
          })
      }
      .width('100%')
      .height('100%')
      .backgroundColor(Color.Pink)
    }
    .height('100%')
    .width('100%')
  }
}
```
