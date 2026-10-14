---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/reader-flip-page
title: 手动触发翻页
breadcrumb: 指南 > 应用服务 > Reader Kit（阅读服务） > 书籍内容交互 > 手动触发翻页
category: harmonyos-guides
scraped_at: 2026-10-15T07:05:40+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:40797a1dd40c54f705a7a9169189c1781285b0c7ff4ee8c25f8be08f58d0e224
---

Reader Kit的交互能力已经集成了手指点击和触摸滑动翻页，如果开发者需要增加其它翻页场景时（如：耳机播控翻页），可使用手动翻页接口实现自定义翻页场景。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/ntS9egxzR2KFK8g11C8bHg/zh-cn_image_0000002762501178.png)

## 接口说明

手动触发场景只涉及1个翻页接口，具体介绍如下表所示。

| 接口名 | 描述 |
| --- | --- |
| [flipPage](../harmonyos-references/reader-read-core.md#flippage)(isNext: boolean): void | 触发ReadPageComponent组件进行翻页。 |

## 开发准备

在进行手动触发翻页之前，请先确保已经“[构建阅读器](reader-read-page.md)”。

## 开发步骤

1. 在调用翻页接口之前，需要应用先构建需要手动触发翻页的场景，如耳机播控场景等。
2. 当自定义翻页场景调用触发翻页时，调用flipPage接口即可实现翻页能力。

   ```typescript
   let isNext: boolean = true; // true为下一页, false为上一页
   this.readerComponentController.flipPage(isNext);
   ```
