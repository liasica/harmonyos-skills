---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-multilingual
title: 朗读多语言内容
breadcrumb: 指南 > 应用框架 > Accessibility Kit（无障碍服务） > 提升应用的无障碍体验 > 提升屏幕朗读无障碍体验 > 朗读多语言内容
category: harmonyos-guides
scraped_at: 2026-09-02T14:49:44+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d08951c0d06ad2a67772be4be7cf7b16a0f27f0a569ddd5ad098d9ad34d460be
---

## 设计场景

当对朗读内容进行标注时，须对标注字符串进行多语种翻译，具体支持的语种和应用本身界面支持的语种保持一致。若采用多个字符串进行朗读内容的拼接，需考虑多语种的情况，避免拼接后朗读错误，例如阿拉伯语从右到左。

## 开发流程

```typescript
@Entry
@Component
export struct Rule_2_1_10 {
  title: string = 'Rule 2.1.10';
  private multilingual: string = 'It is convenient: 屏幕朗读已开启 and use';

  build() {
    NavDestination() {
      Column() {
        Flex({
          direction: FlexDirection.Column,
          alignItems: ItemAlign.Center,
          justifyContent: FlexAlign.Center,
        }) {
          Row() {
            Text(this.multilingual)
              .fontSize(30)
              .fontColor(Color.Blue)
          }
          .width('80%')
        }
        .width('100%')
        .height('100%')
        .backgroundColor(Color.White)
      }
    }.title(this.title)
  }
}
```
