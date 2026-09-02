---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1569
title: 如何解决启动页背景和startWindowIcon属性设置为同一张图时出现的闪屏问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何解决启动页背景和startWindowIcon属性设置为同一张图时出现的闪屏问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:11+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:e1802894ebec0abf003dd23fcf23db3e73a26c8b62413adce928652e099a9c1b
---

## 问题现象

如果启动页背景和module.json中startWindowIcon属性设置为同一张图，APP启动时相当于需要加载两张图，不能平滑过渡，会有闪屏现象。

## 背景知识

[Image组件](../harmonyos-references/ts-basic-components-image.md)为图片组件，常用于在应用中显示图片，支持png、jpg、jpeg、bmp、svg、webp、gif和heif类型的图片格式。

## 解决方案

使用Image组件代替Column组件背景的方案，并设置图片加载方式为同步。

参考示例代码如下：

```ts
@Entry
@Component
struct WhitePage {
  aboutToAppear(): void {
    setTimeout(() => {
    }, 10 * 1000);
  }

  build() {
    Stack() {
      Image($r('app.media.startIcon')) // 此图片仅作示例参考
        .width('50%')
        .height('50%')
        .opacity(0.2)
        .syncLoad(true); // 设置图片为同步加载
      Text('Hello World');
    }
    .width('100%')
    .height('100%');
  }
}
```
