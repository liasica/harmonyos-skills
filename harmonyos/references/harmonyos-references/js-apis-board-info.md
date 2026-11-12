---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-board-info
title: "@ohos.boardInfo (板级硬件信息)"
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > ArkTS API > 设备管理 > @ohos.boardInfo (板级硬件信息)
category: harmonyos-references
scraped_at: 2026-11-12T09:55:51+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:75c9001fec91aa5ce26e8a24cd2242eb068f2a998db5c38a9dde2ab702896187
---

本模块提供板级硬件信息查询能力，支持获取CPU、主板、BIOS等硬件信息，适用于设备识别、资产管理、兼容性判断等场景。开发者不可配置这些信息。

**说明** 

本模块首批接口从API version 26.0.1开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口在执行期间会拉起临时进程，当系统负载较高时，可能引发阻塞风险。为确保应用主线程的响应性能，建议避免在主线程中调用。硬件信息因设备而异且固定不变，可在首次获取后缓存在本地，避免每次使用时重复获取，以提升性能。

本模块接口仅可在Stage模型下使用。

## 导入模块

```ts
import { boardInfo } from '@kit.BasicServicesKit';
```

## 常量

**系统能力**：SystemCapability.Startup.BoardInfo

**模型约束**：本模块接口仅可在Stage模型下使用。

**权限**：以下各项所需要的权限有所不同，详见下表。

**起始版本**：26.0.1

| 名称 | 类型 | 只读 | 说明 |
| --- | --- | --- | --- |
| cpuId | string | 是 | CPU ID。  示例：AA AA AA AA 00 00 00 00（十六进制字符串） |
| cpuArch | string | 是 | CPU架构。  示例：aarch64 |
| cpuVendor | string | 是 | CPU厂商信息。  示例：HISILICON |
| boardSn | string | 是 | 主板序列号。  **需要权限**：ohos.permission.ACCESS\_BOARD\_INFO  示例：0123456789ABCDEF |
| boardVendor | string | 是 | 主板厂商。  示例：HUAWEI |
| boardName | string | 是 | 主板产品名称。  示例：HAD-PCB |
| biosVendor | string | 是 | BIOS厂商。  示例：HUAWEI |
| biosVersion | string | 是 | BIOS版本。  示例：1.00 |
| biosDate | string | 是 | BIOS发布日期。  示例：2026/01/01 08:00:00 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例**

```ts
import { boardInfo } from '@kit.BasicServicesKit';

let cpuId: string = boardInfo.cpuId;
// 输出结果：the value of boardInfo cpuId is :AA AA AA AA 00 00 00 00
console.info('the value of boardInfo cpuId is :' + cpuId);

let cpuArch: string = boardInfo.cpuArch;
// 输出结果：the value of boardInfo cpuArch is :aarch64
console.info('the value of boardInfo cpuArch is :' + cpuArch);

let cpuVendor: string = boardInfo.cpuVendor;
// 输出结果：the value of boardInfo cpuVendor is :HISILICON
console.info('the value of boardInfo cpuVendor is :' + cpuVendor);

let boardSn: string = boardInfo.boardSn;
// 输出结果：the value of boardInfo boardSn is :0123456789ABCDEF
console.info('the value of boardInfo boardSn is :' + boardSn);

let boardVendor: string = boardInfo.boardVendor;
// 输出结果：the value of boardInfo boardVendor is :HUAWEI
console.info('the value of boardInfo boardVendor is :' + boardVendor);

let boardName: string = boardInfo.boardName;
// 输出结果：the value of boardInfo boardName is :HAD-PCB
console.info('the value of boardInfo boardName is :' + boardName);

let biosVendor: string = boardInfo.biosVendor;
// 输出结果：the value of boardInfo biosVendor is :HUAWEI
console.info('the value of boardInfo biosVendor is :' + biosVendor);

let biosVersion: string = boardInfo.biosVersion;
// 输出结果：the value of boardInfo biosVersion is :1.00
console.info('the value of boardInfo biosVersion is :' + biosVersion);

let biosDate: string = boardInfo.biosDate;
// 输出结果：the value of boardInfo biosDate is :2026/01/01 08:00:00
console.info('the value of boardInfo biosDate is :' + biosDate);
```
