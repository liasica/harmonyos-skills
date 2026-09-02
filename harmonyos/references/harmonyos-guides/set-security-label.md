---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/set-security-label
title: 设置分布式文件数据等级
breadcrumb: 指南 > 应用框架 > Core File Kit（文件基础服务） > 分布式文件系统 > 设置分布式文件数据等级
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:24+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d50cd2dd27f8ccf0f6a62e2a36bd1f9b79c6bec7289932300d3e7b1fef970ceb
---

不同设备本身的安全能力差异较大，一些小的嵌入式设备安全能力远弱于平板等设备类型。用户或者应用不同的文件数据有不同安全诉求，例如个人的健康信息和银行卡信息等不期望被弱设备读取。因此，HarmonyOS提供一套完整的数据分级、设备分级标准，并针对不同设备制定不同的数据流转策略，具体规则请参见[数据、设备安全分级](access-control-by-device-and-data-level.md)。

## 接口说明

API详细介绍请参见[ohos.file.securityLabel](../harmonyos-references/js-apis-file-securitylabel.md)。

**表1** 设置文件数据等级，其中“√”表示支持。

| 接口名 | 功能 | 接口类型 | 支持同步 | 支持异步 |
| --- | --- | --- | --- | --- |
| setSecurityLabel | 设置文件安全标签。 | 方法 | √ | √ |
| getSecurityLabel | 获取文件安全标签。 | 方法 | √ | √ |

**须知** 

1. 对于不满足安全等级的文件，跨设备仍然可以看到该文件，但是无权限打开访问该文件。
2. 分布式文件系统的数据等级默认为S3，应用可以主动设置文件的安全等级。

## 开发示例

获取通用文件沙箱路径，并设置数据等级标签。示例中的context的获取方式请参见[获取UIAbility的上下文信息](uiability-usage.md#获取uiability的上下文信息)。

```ts
import { securityLabel } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import { fileIo } from '@kit.CoreFileKit';
```

```typescript
// 获取需要设备数据等级的文件沙箱路径，请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let pathDir = context.filesDir;
let filePath = pathDir + '/test.txt';

// 打开文件
let file: fileIo.File | null = null;
try {
  file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
  // 设置文件的数据等级为s0
  securityLabel.setSecurityLabel(filePath, 's0').then(() => {
    console.info('Succeeded in setting security label.');
    fileIo.closeSync(file);
  }).catch((err: BusinessError) => {
    console.error(`Failed to set security label. Code: ${err.code}, message: ${err.message}`);
    if (file) {
      try {
        fileIo.closeSync(file);
      } catch (closeErr) {
        console.error(`Failed to close file`);
      }
    }
  });
} catch (err) {
  console.error(`Failed to open file. Code: ${err.code}, message: ${err.message}`);
  if (file) {
    try {
      fileIo.closeSync(file);
    } catch (closeErr) {
      console.error(`Failed to close file`);
    }
  }
}
```
