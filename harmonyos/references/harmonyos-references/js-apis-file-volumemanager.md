---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-volumemanager
title: "@ohos.file.volumeManager (卷管理)"
breadcrumb: API参考 > 应用框架 > Core File Kit（文件基础服务） > ArkTS API > @ohos.file.volumeManager (卷管理)
category: harmonyos-references
scraped_at: 2026-11-12T09:55:04+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:48587490e149831c70af5645031bd9cb22264730c4c7f708a508adf4927eacea
---

该模块提供外置存储磁盘设备和卷设备信息查询的相关功能，包括获取外置存储物理磁盘信息和外置存储卷设备信息等。适用于外置存储设备管理、存储空间查询等场景，帮助开发者获取外置存储设备的磁盘和卷设备详情。

**起始版本**：9

## 导入模块

```ts
import { volumeManager } from '@kit.CoreFileKit';
```

## volumeManager.getExternalDiskInfos

getExternalDiskInfos(): Promise<Array<ExternalDiskInfo>>

获取所有外置存储物理磁盘信息。使用Promise异步回调。

**起始版本**：26.0.1

**需要权限**：ohos.permission.GET\_STORAGE\_VOLUME\_INFO

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.FileManagement.StorageService.Volume

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[ExternalDiskInfo](js-apis-file-volumemanager.md#externaldiskinfo)>> | Promise对象，返回外置存储物理磁盘信息列表。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. |
| 13600001 | IPC error. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

volumeManager.getExternalDiskInfos().then((disks: Array<volumeManager.ExternalDiskInfo>) => {
  console.info("getExternalDiskInfos successfully:" + JSON.stringify(disks));
}).catch((error: BusinessError) => {
  console.error(`Failed to getExternalDiskInfos. Code: ${error.code}, message: ${error.message}`);
});
```

## volumeManager.getExternalVolumeInfos

getExternalVolumeInfos(): Promise<Array<ExternalVolumeInfo>>

获取所有外置存储卷设备信息。使用Promise异步回调。

**起始版本**：26.0.1

**需要权限**：ohos.permission.GET\_STORAGE\_VOLUME\_INFO

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.FileManagement.StorageService.Volume

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[ExternalVolumeInfo](js-apis-file-volumemanager.md#externalvolumeinfo)>> | Promise对象，返回外置存储卷设备信息列表。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[文件管理错误码](errorcode-filemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. |
| 13600001 | IPC error. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

volumeManager.getExternalVolumeInfos().then((volumes: Array<volumeManager.ExternalVolumeInfo>) => {
  console.info("getExternalVolumeInfos successfully:" + JSON.stringify(volumes));
}).catch((error: BusinessError) => {
  console.error(`Failed to getExternalVolumeInfos. Code: ${error.code}, message: ${error.message}`);
});
```

## ExternalDiskInfo

外置磁盘信息。

**起始版本**：26.0.1

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.FileManagement.StorageService.Volume

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| diskId | string | 否 | 否 | 磁盘设备ID，格式为disk-{主设备号}-{次设备号}，如disk-8-0。 |
| diskType | number | 否 | 否 | 磁盘设备类型：  1：SD卡。  2：U盘。  3：光盘（CD/DVD/BD）。  值为整数。 |
| volumeIds | Array<string> | 否 | 否 | 磁盘上的卷设备ID列表。一个磁盘可以包含多个卷设备，如["vol-8-1", "vol-8-2"]。 |
| vendorId | number | 否 | 否 | USB设备的厂商ID，由USB-IF分配，用于标识设备制造商。值为整数。 |
| productId | number | 否 | 否 | USB设备的产品ID，由制造商分配，用于标识具体产品型号。值为整数。 |

## ExternalVolumeInfo

外置卷设备信息。

**起始版本**：26.0.1

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.FileManagement.StorageService.Volume

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| volumeId | string | 否 | 否 | 卷设备ID，格式为vol-{主设备号}-{次设备号}，如vol-8-1。 |
| uuid | string | 否 | 否 | 卷设备uuid，是卷设备的通用唯一识别码，不会随着插卡顺序变化而变化，但是卷设备的格式化会改变卷设备的uuid，如3C16-F61F。 |
| diskId | string | 否 | 否 | 卷设备所属的磁盘ID。一个磁盘可以有一个或多个卷设备。磁盘设备ID的格式为disk-{主设备号}-{次设备号}，如disk-8-0。 |
| description | string | 否 | 否 | 卷设备描述。卷设备的格式化会改变卷设备描述，如"MyUSB"。 |
| state | number | 否 | 否 | 卷设备状态：  0：卸载状态。  1：检查状态。  2：挂载状态。  3：正在弹出状态。  值为整数。 |
| totalSize | number | 否 | 否 | 卷设备总大小。单位：Byte。 |
| freeSize | number | 否 | 否 | 卷设备可用大小。单位：Byte。 |
| path | string | 否 | 否 | 卷设备的挂载地址，一般为/mnt/data/external/{uuid}。卷设备的格式化会改变挂载路径。 |
| fsType | string | 否 | 否 | 文件系统类型。常见的文件系统有fat32、ntfs、exfat、ext4、udf和iso9660。 |
