---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1438
title: 判断Text组件中的内容是否换行
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 判断Text组件中的内容是否换行
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:21+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:400070e234c6876b5e415ce68785907de9fb3ade4c1fe94fb48e65e2a22b5765
---

## 问题现象

如何获取Text组件每行显示的内容，并判断是否使用了换行符？

## 背景知识

在Text组件中，可以通过调用[getLayoutManager](../harmonyos-references/ts-basic-components-text.md#getlayoutmanager12)接口来获取布局管理器对象[LayoutManager](../harmonyos-references/ts-text-common.md#layoutmanager12)，进而获得最新的布局信息。

## 解决方案

通过调用getLayoutManager接口可以获取Text组件中每行显示的内容。将第i行文本的结束索引endIndex与第i+1行文本的起始索引startIndex进行对比，如果两者不相等，则表明该文本是通过换行符实现换行的。

```screen
import { util } from '@kit.ArkTS';

@Entry
@Component
struct TextPage3 {
  private controller: TextController = new TextController();
  textStr: string = '你好，开发者\n欢迎使用HarmonyOS';

  build() {
    Scroll() {
      Column() {
        Text(this.textStr, { controller: this.controller })
          .fontSize(20)
          .onClick(() => {
            let layoutManager: LayoutManager = this.controller.getLayoutManager();
            let lineCount = layoutManager.getLineCount();
            for (let i = 0; i < lineCount - 1; i++) {
              if (layoutManager.getLineMetrics(i + 1).startIndex !==
              layoutManager.getLineMetrics(i).endIndex) {
                // 获取第i行的endIndex与第i+1行的startIndex相比较，如果不相同，则说明此文本存在换行行为
                console.info(util.format("第%s行存在使用换行符进行换行的行为", i + 1));
              } else {
                console.info(util.format("第%s行不存在使用换行符进行换行的行为", i + 1));
              }
            }
          })
          .margin({ bottom: 20, top: 10 })
      }
      .margin({ top: 100, left: 8, right: 8 })
    }
  }
}
```
