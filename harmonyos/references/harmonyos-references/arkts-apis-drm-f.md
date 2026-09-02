---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-drm-f
title: Functions
breadcrumb: API参考 > 媒体 > DRM Kit（数字版权保护服务） > ArkTS API > @ohos.multimedia.drm (数字版权保护) > Functions
category: harmonyos-references
scraped_at: 2026-09-02T15:02:29+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:cb50370a1632757b06ac0dd7da95af6cf2b1dc49e346d5fc66a4599b324e6db5
---

**说明** 

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```ts
import { drm } from '@kit.DrmKit';
```

## drm.createMediaKeySystem

createMediaKeySystem(name: string): MediaKeySystem

创建MediaKeySystem实例。最多可以创建64个MediaKeySystem实例。超过上限时，会抛出错误码24700103。建议及时调用[destroy](arkts-apis-drm-mediakeysystem.md#destroy)接口释放不再使用的MediaKeySystem实例。

**元服务API：** 从API版本14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | DRM解决方案名称。可通过[drm.getMediaKeySystems](arkts-apis-drm-f.md#drmgetmediakeysystems12)接口获取设备支持的DRM解决方案名称，如"com.wiseplay.drm"。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [MediaKeySystem](arkts-apis-drm-mediakeysystem.md) | MediaKeySystem实例。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[DRM错误码](errorcode-drm.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 24700101 | All unknown errors. |
| 24700103 | Meet max MediaKeySystem num limit. |
| 24700201 | Fatal service error, for example, service died. |

**示例：**

```ts
import { drm } from '@kit.DrmKit';
// name为DRM解决方案名称，可通过drm.getMediaKeySystems接口获取设备支持的DRM解决方案名称，如"com.wiseplay.drm"。
let name = 'com.wiseplay.drm';
let mediaKeySystem: drm.MediaKeySystem = drm.createMediaKeySystem(name);
console.info(`createMediaKeySystem success, name: ${name}`);
```

## drm.isMediaKeySystemSupported

isMediaKeySystemSupported(name: string): boolean

判断设备是否支持指定的DRM解决方案。

**元服务API：** 从API版本14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | DRM解决方案名称，长度不超过4096字节。可通过[drm.getMediaKeySystems](arkts-apis-drm-f.md#drmgetmediakeysystems12)接口获取设备支持的DRM解决方案名称，如"com.wiseplay.drm"。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回是否支持指定的DRM解决方案。true表示支持，false表示不支持。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[DRM错误码](errorcode-drm.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified. 2.Parameter verification failed, the param name's length is zero or too big(exceeds 4096 Bytes). |
| 24700101 | All unknown errors. |
| 24700201 | Fatal service error, for example, service died. |

**示例：**

```ts
import { drm } from '@kit.DrmKit';

let supported: boolean = drm.isMediaKeySystemSupported('com.wiseplay.drm');
console.info("isMediaKeySystemSupported: ", supported);
```

## drm.isMediaKeySystemSupported

isMediaKeySystemSupported(name: string, mimeType: string): boolean

判断设备是否支持指定的DRM解决方案及媒体类型。

**元服务API：** 从API版本14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | DRM解决方案名称。从API版本12开始，可通过[drm.getMediaKeySystems](arkts-apis-drm-f.md#drmgetmediakeysystems12)接口获取设备支持的DRM解决方案名称，如"com.wiseplay.drm"。 |
| mimeType | string | 是 | 媒体类型，支持的媒体类型取决于DRM解决方案，如：video/avc、video/hevc。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回是否支持指定的DRM解决方案及媒体类型。当name和mimeType都支持时返回true，否则返回false。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[DRM错误码](errorcode-drm.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 24700101 | All unknown errors. |
| 24700201 | Fatal service error, for example, service died. |

**示例：**

```ts
import { drm } from '@kit.DrmKit';

let supported: boolean = drm.isMediaKeySystemSupported('com.wiseplay.drm', 'video/avc');
console.info("isMediaKeySystemSupported: ", supported);
```

## drm.isMediaKeySystemSupported

isMediaKeySystemSupported(name: string, mimeType: string, level: ContentProtectionLevel): boolean

判断设备是否支持指定的DRM解决方案、媒体类型及内容保护级别。

**元服务API：** 从API版本14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | DRM解决方案名称。可通过[drm.getMediaKeySystems](arkts-apis-drm-f.md#drmgetmediakeysystems12)接口获取设备支持的DRM解决方案名称，如"com.wiseplay.drm"。 |
| mimeType | string | 是 | 媒体类型，支持的媒体类型取决于DRM解决方案。 |
| level | [ContentProtectionLevel](arkts-apis-drm-e.md#contentprotectionlevel) | 是 | 内容保护级别，用于指定DRM内容的安全保护程度，不同级别对应不同的解密能力和安全要求。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回是否支持指定的DRM解决方案、媒体类型以及内容保护级别。当name、mimeType和level都支持时返回true，否则返回false。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[DRM错误码](errorcode-drm.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 24700101 | All unknown errors. |
| 24700201 | Fatal service error, for example, service died. |

**示例：**

```ts
import { drm } from '@kit.DrmKit';

let supported: boolean = drm.isMediaKeySystemSupported('com.wiseplay.drm', 'video/avc', drm.ContentProtectionLevel.CONTENT_PROTECTION_LEVEL_SW_CRYPTO);
console.info("isMediaKeySystemSupported: ", supported);
```

## drm.getMediaKeySystemUuid12+

getMediaKeySystemUuid(name: string): string

获取DRM解决方案支持的DRM内容保护系统唯一标识。

**元服务API：** 从API版本14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | DRM解决方案名称。可通过[drm.getMediaKeySystems](arkts-apis-drm-f.md#drmgetmediakeysystems12)接口获取设备支持的DRM解决方案名称，如"com.wiseplay.drm"。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | DRM内容保护系统的唯一标识。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[DRM错误码](errorcode-drm.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed.Possibly because: 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 24700101 | All unknown errors. |
| 24700201 | Fatal service error, for example, service died. |

**示例：**

```ts
import { drm } from '@kit.DrmKit';

let uuid: string = drm.getMediaKeySystemUuid('com.wiseplay.drm');
console.info("getMediaKeySystemUuid: ", uuid);
```

## drm.getMediaKeySystems12+

getMediaKeySystems(): MediaKeySystemDescription[]

获取设备支持的插件信息列表。

**元服务API：** 从API版本14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [MediaKeySystemDescription](arkts-apis-drm-i.md#mediakeysystemdescription12)[] | 设备支持的插件信息列表。 |

**错误码：**

以下错误码的详细介绍请参见[DRM错误码](errorcode-drm.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 24700101 | All unknown errors. |
| 24700201 | Fatal service error, for example, service died. |

**示例：**

```ts
import { drm } from '@kit.DrmKit';

let description: drm.MediaKeySystemDescription[] = drm.getMediaKeySystems();
// 验证返回结果，description为插件信息列表，包含插件名称和唯一标识。
if (description.length > 0) {
  console.info(`getMediaKeySystems success, count: ${description.length}`);
  for (let i = 0; i < description.length; i++) {
    console.info(`name: ${description[i].name}, uuid: ${description[i].uuid}`);
  }
} else {
  console.info('No DRM system available');
}
```
