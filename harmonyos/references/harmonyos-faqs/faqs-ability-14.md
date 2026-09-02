---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-14
title: 如何获取当前应用程序缓存目录
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 如何获取当前应用程序缓存目录
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:55+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:d77a09a5de0cf804fbc2e71e1a39f1fa8855dbbf624125268606cf5a73597ee1
---

使用Context.cacheDir获取应用程序的缓存目录。代码示例如下：

```typescript
import { common } from '@kit.AbilityKit';

@Entry
@Component
export struct GetCacheDirectoryView {
  private context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  @State cachePath: string = '';

  build() {
    Column() {
      Text(this.cachePath)
        .margin({ bottom: 24 })
      Button() {
        Text('Get the application cache directory address')
      }
      .onClick(() => {
        const applicationContext = this.context.getApplicationContext();
        // Get the application file path
        const cacheDir = applicationContext.cacheDir;
        this.cachePath = cacheDir + '/test.txt';
      })
      .width(300)
      .height(50)
    }
    .justifyContent(FlexAlign.Center)
    .width('100%')
    .height('100%')
  }
}
```

**参考链接**

[获取应用文件路径](../harmonyos-guides/application-context-stage.md#获取应用文件路径)
