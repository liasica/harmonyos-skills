---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-localization-14
title: 在多模块工程中，如何获取har/hsp中的rawfile资源
breadcrumb: FAQ > 应用框架开发 > 无障碍和本地化 > 本地化开发（Localization） > 在多模块工程中，如何获取har/hsp中的rawfile资源
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:31+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:6d71e3f88bdf617cc91c13c9f47195543b2fdc6c89aeb1e038ba3d805661b90f
---

har模块中的资源可以通过[@ohos.resourceManager (资源管理)](../harmonyos-references/js-apis-resource-manager.md)获取，hsp中的资源可以通过application的[application.createModuleContext](../harmonyos-references/js-apis-app-ability-application.md#applicationcreatemodulecontext)接口创建相应模块的context，再通过resourceManager获取。

示例如下：

```typescript
import { application, common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { buffer } from '@kit.ArkTS';

@Entry
@Component
struct Index {
  private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

  build() {
    Column() {
      Button('get rawFile content')
        .onClick(() => {
          application.createModuleContext(this.context, 'hsp')
            .then((data) => {
              let rawFileData = data.resourceManager.getRawFileContentSync('hsp.txt');
              let hspContent: string = buffer.from(rawFileData.buffer).toString();
            })
            .catch((error: BusinessError) => {
              console.error(`createModuleContext failed, error.code: ${error.code}, error.message: ${error.message}`);
            })
        })
    }
    .height('100%')
    .width('100%')
    .justifyContent(FlexAlign.Center)
  }
}
```
