---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-set-listitem-style
title: 设置列表卡片样式
breadcrumb: 指南 > 应用框架 > UI Design Kit（UI设计套件） > 列表 > 设置列表卡片样式
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:16+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:53b9d6f2b1807bb315b883c5a81c804b470b5e19c64f3f7c4092cc607262c1ce
---

## 场景介绍

从6.0.0(20)版本开始，新增支持设置列表卡片样式。

应用使用[HdsListItemCard (列表卡片)](../harmonyos-references/ui-design-hdslistitemcard.md)组件实现多设备上的系统列表样式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/4cgeVH7mTdSIVox8tluTPw/zh-cn_image_0000002712404448.jpg)

## 开发步骤

1. 导入相关模块。

   ```typescript
   import { HdsListItemCard, PrefixImage, SuffixSwitch} from '@kit.UIDesignKit';
   import { promptAction } from '@kit.ArkUI';
   ```
2. 创建HdsListItemCard组件，设置左边为Image，中间为Text，右边为Switch的场景。

   ```typescript
   @Entry
   @Component
   struct Index {
     private scroller: ListScroller = new ListScroller();

     build() {
       Column() {
         List({ space: 10, scroller: this.scroller }) {
           ListItem() {
             HdsListItemCard({
               // A区图片
               prefixItem: new PrefixImage({
                 image: $r('app.media.background'),
                 onClick: () => {
                   promptAction.openToast({ message: 'left image' });
                 }
               }),
               // B区文本
               textItem: {
                 primaryText: {
                   text: 'Primary Text'
                 },
                 secondaryText: {
                   text: 'Secondary Text'
                 },
                 description: {
                   text: 'Description Text'
                 }
               },
               // C区Switch
               suffixItem: new SuffixSwitch({
                 isCheck: false,
                 onChange: (num: boolean) => {
                   if (num) {
                     promptAction.openToast({ message: 'switch is true' });
                   } else {
                     promptAction.openToast({ message: 'switch is false' });
                   }
                 }
               }),
               onClick: () => {
                 promptAction.openToast({ message: 'hdslistitem' });
               }
             })
           }
         }
         .width('100%')
         .height('100%')
         .margin(10)
       }.backgroundColor(0x1a0a59f7).height('100%')
     }
   }
   ```
