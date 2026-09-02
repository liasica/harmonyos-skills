---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-159
title: 启动应用时，启动页图标缩放
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 启动应用时，启动页图标缩放
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:55+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:13f98de0029fce13d96c2fb35685fd39750fdd1d3fa719a3fd18532d4bf64ac0
---

## 问题现象

启动应用时，启动页展示的图标视觉上会有缩放效果，影响视觉体验。

## 背景知识

当前Image Asset功能支持为Phone、Tablet、2in1应用，[生成单层图标](../harmonyos-guides/ide-apply-generated-icon.md)支持生成以下两种类型图标：

* icon：应用图标（手机或其他设备桌面及设置的图标会比应用中出现的应用图标大）。
* startWindowIcon：启动页图标。

## 问题定位

* 排查module.json5配置文件中配置的启动页图标startWindowIcon是否是发生缩放的图标资源。同时，进一步排查是否存在闪屏页。

  ```json
  // entry模块的module.json5配置文件
  {
    "module": {
      // ...
      "abilities": [
        {
          // ...
          "name": "EntryAbility",
          "startWindowIcon": "$media:ic_eshop",  // 启动页图标配置
          "startWindowBackground": "$color:start_window_background",
        }
      ],
    }
  }
  ```
* 若应用同时配置了启动页图标和开发了闪屏页，查看二者配置的图标资源是否一致，若闪屏页的图标和启动图标是同一个图标资源，但是开发的闪屏页无法与启动页图标的大小位置保持完全一致，就会导致启动应用的时候，视觉上启动图标缩放。

## 分析结论

开屏图标缩放的原因为启动页面重复出现，用户除配置启动页图标外还额外开发了闪屏页，启动页图标与闪屏页图标是同一个图标资源，但位置尺寸不一致，导致打开应用时，两个页面上的图标接连显示，启动页图标出现视觉上的缩放效果。

## 修改建议

建议根据应用的设计理念，取消闪屏页或配置启动页为透明图标。

* 取消闪屏页开发，EntryAbility中windowStage.loadContent直接加载首页。
* 配置启动页为透明图标：将配置的startWindowIcon替换为透明SVG图片，startWindowBackground配置为白色（深色模式的资源文件配置为黑色）。
