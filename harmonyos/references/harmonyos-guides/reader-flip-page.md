---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/reader-flip-page
title: 手动触发翻页
breadcrumb: 指南 > 应用服务 > Reader Kit（阅读服务） > 书籍内容交互 > 手动触发翻页
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:046262919e965a1fad88cf1f71cf62705cd65a6bed95e35b3093f029ecdfa7bc
---

Reader Kit的交互能力已经集成了手指点击和触摸滑动翻页，如果开发者需要增加其它翻页场景时（如：耳机播控翻页），可使用手动翻页接口实现自定义翻页场景。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/ltGMHQ5eQ0CyJQ8pYoGyqQ/zh-cn_image_0000002583479145.png?HW-CC-KV=V1&HW-CC-Date=20260427T235039Z&HW-CC-Expire=86400&HW-CC-Sign=CA02B8B4EDE0AD2DFA5B277ADE7EADD26DDBAF66F248D807EA9D385AA25FA038)

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

   ```
   1. let isNext: boolean = true; // true为下一页, false为上一页
   2. this.readerComponentController.flipPage(isNext);
   ```
