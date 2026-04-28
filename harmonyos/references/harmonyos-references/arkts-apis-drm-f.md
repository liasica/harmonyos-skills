---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-drm-f
title: Functions
breadcrumb: API参考 > 媒体 > DRM Kit（数字版权保护服务） > ArkTS API > @ohos.multimedia.drm (数字版权保护) > Functions
category: harmonyos-references
scraped_at: 2026-04-28T08:12:59+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:690560f622fa4d2746055334aaa2207f2704f19e81a1edbcb92ac189a254ec54
---

说明

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { drm } from '@kit.DrmKit';
```

## drm.createMediaKeySystem

PhonePC/2in1TabletTVWearable

createMediaKeySystem(name: string): MediaKeySystem

创建MediaKeySystem实例。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | DRM解决方案名称，如"com.wiseplay.drm"。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [MediaKeySystem](arkts-apis-drm-mediakeysystem.md) | MediaKeySystem实例。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[DRM错误码](errorcode-drm.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 24700101 | All unknown errors |
| 24700103 | Meet max MediaKeySystem num limit |
| 24700201 | Fatal service error, for example, service died |

**示例：**

```
1. import { drm } from '@kit.DrmKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. try {
4. let mediaKeySystem: drm.MediaKeySystem = drm.createMediaKeySystem("com.wiseplay.drm");
5. } catch (err) {
6. let error = err as BusinessError;
7. console.error(`createMediaKeySystem ERROR: ${error}`);
8. }
```

## drm.isMediaKeySystemSupported

PhonePC/2in1TabletTVWearable

isMediaKeySystemSupported(name: string): boolean

判断设备是否支持指定的DRM解决方案。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | DRM解决方案名称，如"com.wiseplay.drm"。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回是否支持。true表示支持指定的DRM解决方案，false表示不支持指定的DRM解决方案。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[DRM错误码](errorcode-drm.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified. 2.Parameter verification failed, the param name's length is zero or too big(exceeds 4096 Bytes). |
| 24700101 | All unknown errors |
| 24700201 | Fatal service error, for example, service died |

**示例：**

```
1. import { drm } from '@kit.DrmKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. let supported: boolean = drm.isMediaKeySystemSupported("com.wiseplay.drm");
6. console.info("isMediaKeySystemSupported: ", supported);
7. } catch (err) {
8. let error = err as BusinessError;
9. console.error(`isMediaKeySystemSupported ERROR: ${error}`);
10. }
```

## drm.isMediaKeySystemSupported

PhonePC/2in1TabletTVWearable

isMediaKeySystemSupported(name: string, mimeType: string): boolean

判断设备是否支持指定DRM解决方案及媒体类型。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | DRM解决方案名称。建议先调用[isMediaKeySystemSupported](arkts-apis-drm-f.md#drmismediakeysystemsupported)判断是否是支持的解决方案名称。 |
| mimeType | string | 是 | 媒体类型，支持的媒体类型取决于DRM解决方案，如：video/avc、video/hevc。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回是否支持。true表示支持指定DRM解决方案及媒体类型，false表示不支持指定DRM解决方案及媒体类型。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[DRM错误码](errorcode-drm.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 24700101 | All unknown errors |
| 24700201 | Fatal service error, for example, service died |

**示例：**

```
1. import { drm } from '@kit.DrmKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. let supported: boolean = drm.isMediaKeySystemSupported("com.wiseplay.drm", "video/avc");
6. console.info("isMediaKeySystemSupported: ", supported);
7. } catch (err) {
8. let error = err as BusinessError;
9. console.error(`isMediaKeySystemSupported ERROR: ${error}`);
10. }
```

## drm.isMediaKeySystemSupported

PhonePC/2in1TabletTVWearable

isMediaKeySystemSupported(name: string, mimeType: string, level: ContentProtectionLevel): boolean

判断设备是否支持指定DRM解决方案、媒体类型以及内容保护级别。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | DRM解决方案名称。建议先调用[isMediaKeySystemSupported](arkts-apis-drm-f.md#drmismediakeysystemsupported)判断是否是支持的解决方案名称。 |
| mimeType | string | 是 | 媒体类型，支持的媒体类型取决于DRM解决方案。建议先调用[isMediaKeySystemSupported](arkts-apis-drm-f.md#drmismediakeysystemsupported-1)判断是否是DRM解决方案支持的类型。 |
| level | [ContentProtectionLevel](arkts-apis-drm-e.md#contentprotectionlevel) | 是 | 内容保护级别。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回是否支持。true表示支持指定DRM解决方案、媒体类型以及内容保护级别，false表示不支持指定DRM解决方案、媒体类型以及内容保护级别。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[DRM错误码](errorcode-drm.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 24700101 | All unknown errors |
| 24700201 | Fatal service error, for example, service died |

**示例：**

```
1. import { drm } from '@kit.DrmKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. let supported: boolean = drm.isMediaKeySystemSupported("com.wiseplay.drm", "video/avc", drm.ContentProtectionLevel.CONTENT_PROTECTION_LEVEL_SW_CRYPTO);
6. console.info("isMediaKeySystemSupported: ", supported);
7. } catch (err) {
8. let error = err as BusinessError;
9. console.error(`isMediaKeySystemSupported ERROR: ${error}`);
10. }
```

## drm.getMediaKeySystemUuid12+

PhonePC/2in1TabletTVWearable

getMediaKeySystemUuid(name: string): string;

获取DRM解决方案支持的DRM内容保护系统唯一标识。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | DRM解决方案名称，支持的解决方案名称可通过[isMediaKeySystemSupported](arkts-apis-drm-f.md#drmismediakeysystemsupported)判断。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | DRM内容保护系统的唯一标识。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[DRM错误码](errorcode-drm.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed.Possibly because: 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 24700101 | All unknown errors |
| 24700201 | Fatal service error, for example, service died |

**示例：**

```
1. import { drm } from '@kit.DrmKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. try {
4. let uuid: string = drm.getMediaKeySystemUuid("com.wiseplay.drm");
5. console.info("getMediaKeySystemUuid: ", uuid);
6. } catch (err) {
7. let error = err as BusinessError;
8. console.error(`getMediaKeySystemUuid ERROR: ${error}`);
9. }
```

## drm.getMediaKeySystems12+

PhonePC/2in1TabletTVWearable

getMediaKeySystems(): MediaKeySystemDescription[]

获取设备支持的插件信息列表。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [MediaKeySystemDescription[]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-drm-i#mediakeysystemdescription12) | 设备支持的插件信息列表。 |

**错误码：**

以下错误码的详细介绍请参见[DRM错误码](errorcode-drm.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 24700101 | All unknown errors |
| 24700201 | Fatal service error, for example, service died |

**示例：**

```
1. import { drm } from '@kit.DrmKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. try {
4. let description: drm.MediaKeySystemDescription[] = drm.getMediaKeySystems();
5. } catch (err) {
6. let error = err as BusinessError;
7. console.error(`getMediaKeySystems ERROR: ${error}`);
8. }
```
