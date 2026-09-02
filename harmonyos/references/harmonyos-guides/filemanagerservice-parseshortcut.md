---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/filemanagerservice-parseshortcut
title: 解析文件快捷方式
breadcrumb: 指南 > 应用服务 > File Manager Service Kit（文件管理服务） > 解析文件快捷方式
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:25+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:52429655c501dc2f357811d7ac2581b5727b301e185228eb763245ac5cdc4deb
---

从6.1.0(23)版本开始，新增支持解析文件快捷方式。

## 场景介绍

解析出指定快捷方式文件对应原文件的URI。常用在应用需要通过快捷方式文件打开原文件的场景。

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| [parseShortcut](../harmonyos-references/filemanagerservice-arkts-filemanagerservice.md#filemanagerserviceparseshortcut)(linkUri: string): Promise<string> | 根据快捷方式文件的URI解析出对应原文件的URI，并返回。使用Promise异步回调。 |

## 示例代码

1.导入文件管理服务模块及相关模块。

```typescript
import { fileManagerService } from '@kit.FileManagerServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';
```

2.根据指定快捷方式文件的URI解析出对应原文件的URI。

```typescript
private async getTargetUriByLinkUri(linkUri: string): Promise<string> {
  // 示例代码linkUri表示快捷方式文件的URI，快捷方式文件的后缀为“.hlink”
  // 例如，linkUri可以输入为: ”file://docs/storage/Users/currentUser/Documents/1.jpg.hlink“
  // 开发者应根据自己实际的URI进行开发，并确保对该文件有读写权限
  try {
    let targetUri: string = await fileManagerService.parseShortcut(linkUri);
    console.info('targetUri is: ' + targetUri);
    return targetUri;
  } catch (err) {
    let error: BusinessError = err as BusinessError;
    console.error('parse shortcut failed, errCode:' + error.code + ', errMessage:' + error.message);
  }
  return '';
}
```
