---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-160
title: 异步接口如何以同步的方式进行调用
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 异步接口如何以同步的方式进行调用
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:53+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:81c31f1bfafdf8aa5aaa9b62a3d4120c6f2d9873b7d993fa94c3072af06dda72
---

## 问题现象

在API文档中，setSpecificSystemBarEnabled接口只有Promise异步回调的方法，如何以同步的方式进行调用？

## 背景知识

* [setSpecificSystemBarEnabled](../harmonyos-references/arkts-apis-window-window.md#setspecificsystembarenabled11)可以设置主窗口三键导航栏、状态栏、底部导航条的显示和隐藏，使用Promise异步回调。
* [async/await](../harmonyos-guides/async-concurrency-overview.md#asyncawait)是JavaScript中处理异步操作的语法糖，基于Promise实现，可以让异步代码的编写和阅读更接近同步方式。

## 解决方案

目前HarmonyOS未提供setSpecificSystemBarEnabled的同步设置方法，可以使用async/await让异步代码的写法更接近同步逻辑。

```screen
import { window } from '@kit.ArkUI';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct SpecificSystemBarEnabledSample {
  context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  @State flag: boolean = true;

  /**
   * setSpecificSystemBarEnabled的同步设置方法
   */
  set() {
    window.getLastWindow(this.context, async (err: BusinessError, topWindow) => {
      const errCode: number = err.code;
      if (errCode) {
        console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
        return;
      }
      try {
        await topWindow.setSpecificSystemBarEnabled('status', this.flag);
      } catch (exception) {
        console.error(`Failed to set the system bar to be invisible. Cause code: ${exception.code}, message: ${exception.message}`);
      }
    });
  }

  build() {
    RelativeContainer() {
      Text('点击测试')
        .id('SpecificSystemBarEnabledSample')
        .fontSize($r('app.float.page_text_font_size'))
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          this.set();
          this.flag = !this.flag;
        })
    }
    .height('100%')
    .width('100%')
  }
}
```
