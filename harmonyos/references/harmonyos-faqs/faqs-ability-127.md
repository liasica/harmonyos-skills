---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-127
title: 应用启动闪屏
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 应用启动闪屏
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:55+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a7c263f5d00dec8b3ab72b34d707db4d086a7c4eb95cb2a30326388633acf6c7
---

## 问题现象

应用在冷启动时出现闪屏现象。

## 背景知识

* [syncLoad](../harmonyos-references/ts-basic-components-image.md#syncload8)：设置是否同步加载图片。

  | 参数名 | 类型 | 必填 | 说明 |
  | --- | --- | --- | --- |
  | value | boolean | 是 | 是否同步加载图片，默认是异步加载。同步加载时阻塞UI线程，不会显示占位图。默认值：false，false表示异步加载图片，true表示同步加载图片。 |
* [startWindow标签](../harmonyos-guides/module-configuration-file.md#startwindow标签)：该标签指向一个profile文件资源，用于指定UIAbility组件启动页面的配置文件。
* [startWindowBackground](../harmonyos-guides/launch-page-config.md#启动页的分类和实现方式)：标识当前UIAbility组件简易启动页面背景颜色资源文件的索引，取值为长度不超过255字节的字符串。

## 问题定位

* 排查应用resources/base/profile下，是否有start\_window.json文件。
  + 有start\_window.json文件：查看文件中startWindowBackgroundColor是否设置为透明背景。
  + 没有start\_window.json文件：查看module.json5配置文件中startWindowBackground是否设置为透明背景。
* 查看应用闪屏页面是否使用Image组件并启用syncLoad来同步加载图片。

## 分析结论

* 启动页背景色没有设置为透明色，导致应用启动闪屏。
* 闪屏页背景图片异步加载，导致应用启动闪屏。

## 修改建议

* 在module.json5中设置透明背景。

  ```ts
  "startWindowIcon": "$media:splash_icon",
  "startWindowBackground": "$color:transparent",
  ```
* 使用syncLoad同步加载图片。

  ```ts
  @Entry
  @Component
  struct SplashPage {
    build() {
      Column() {
        Image($r('app.media.splash_bg'))
          .width('100%')
          .height('100%')
          .syncLoad(true) // 同步加载避免闪屏
      }
    }
  }
  ```
