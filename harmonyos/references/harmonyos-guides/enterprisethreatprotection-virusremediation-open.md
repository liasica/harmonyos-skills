---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisethreatprotection-virusremediation-open
title: 打开文件
breadcrumb: 指南 > 系统 > 安全 > Enterprise Threat Protection Kit（企业威胁防护服务） > 病毒检测与处置 > 打开文件
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:03+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:db26ccf12ce8e10c7678ef60608961231b40968995ee1d7eec5a91bedbd07baf
---

## 基本概念

打开文件功能为安全防护类应用提供专用接口以获取文件描述符（fd）。

## 场景介绍

当安全防护类应用（如病毒扫描、恶意软件检测等）需要对设备上的文件进行安全扫描时，可能会遇到目标文件位于应用沙箱外且应用没有直接读取权限的情况。此时，可通过文件打开接口获取目标文件的文件描述符（fd），使安全防护应用能够正常访问和扫描这些文件，确保设备整体安全性。

## 接口说明

详细接口说明可参考[接口文档](../harmonyos-references/enterprisethreatprotection-virusremediation-interface.md#openfile)。

| 接口 | 描述 |
| --- | --- |
| openFile(path: string): Promise<number> | 获取指定路径文件的文件描述符fd。 |

## 开发步骤

1. 导入模块。

   ```typescript
    // 导入企业威胁防护能力模块和文件IO模块
    import { virusRemediation } from '@kit.EnterpriseThreatProtectionKit';
    import { fileIo } from '@kit.CoreFileKit';
   ```
2. 通过调用接口[openFile](../harmonyos-references/enterprisethreatprotection-virusremediation-interface.md#openfile)，获取目标文件的文件描述符（fd）。path参数为目标文件的绝对路径。使用完fd后应记得关闭。

   ```typescript
   import { BusinessError } from '@kit.BasicServicesKit';

   // 获取文件fd，查看打印结果
   function openFilePromise() {
     // 目标文件路径，此处为示例路径，实际使用时需替换为用户指定的真实路径或通过参数传入
     let targetFilePath: string = '/example/path/to/file.txt';
     virusRemediation.openFile(targetFilePath).then((fd: number) => {
       console.info(`Succeeded in opening file. Path: ${targetFilePath}, FD: ${fd}.`);
       // 使用完fd后应记得关闭
       fileIo.closeSync(fd);
     }).catch((err: BusinessError) => {
       // 根据错误码进行不同的业务处理
       if (err.code === 1023803001) {
         console.error('Access denied, please check if the file belongs to current user.');
       } else {
         console.error(`Failed to open file. Code: ${err.code}, message: ${err.message}.`);
       }
     });
   }
   ```
