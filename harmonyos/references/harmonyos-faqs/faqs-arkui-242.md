---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-242
title: 如何获取手机屏幕信息
breadcrumb: FAQ > 应用框架开发 > UI框架 > 屏幕管理 > 如何获取手机屏幕信息
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:13+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:cedf2bf5aaa49480a0bcba1943b246b78c588d475576b5404acb47d4ff450f08
---

可参考如下代码，获取了屏幕的宽和高，Display实例的所有属性见文档：[@ohos.display (屏幕属性)](../harmonyos-references/js-apis-display.md)。

```typescript
import { display } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';
  private screenWidth: number = 0;
  private screenHeight: number = 0;

  aboutToAppear() {
    try {
      this.screenWidth = display.getDefaultDisplaySync().width;
      this.screenHeight = display.getDefaultDisplaySync().height;
    } catch (e) {
      console.error('Fail with code: ' + JSON.stringify(e));
    }
  }

  build() {
    Row() {
      Column() {
        Text('---->width: ' + this.screenWidth)
        Text('---->height: ' + this.screenHeight)
      }
      .width('100%')
    }
    .height('100%')
  }
}
```
