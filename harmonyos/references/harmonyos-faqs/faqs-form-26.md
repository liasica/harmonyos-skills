---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-form-26
title: 服务卡片实现长期破窗效果
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 卡片开发（Form） > 服务卡片实现长期破窗效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:56+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:cfaa397d5db5888ebe8663f7c75b17e77ba1e9524284c493a0d12907bbf3a034
---

## 问题现象

在某些业务场景中，希望服务卡片能够长期呈现“破窗”效果（即视觉上突破卡片默认矩形边界），并实现自定义边框样式。如何在普通卡片上达成这一需求？

## 背景知识

* [互动卡片](../harmonyos-guides/arkts-ui-liveform-overview.md)提供卡片动效能力，例如卡片破框动效，丰富信息提醒、浅层交互功能，显著提升用户体验。
* 从API version 22开始，Form Kit提供卡片[背板元素透明](../harmonyos-guides/arkts-ui-transparent-backplate-form-development.md)显示的能力，满足更丰富的UI设计以及美观诉求。

## 解决方案

传统互动卡片的“破窗”效果是短时的——仅在用户点击触发动效时进入激活态，动效结束后自动恢复为非激活态。

若要实现长期破窗（如自定义边框、卡片边缘悬浮感），可借助背板透明卡片间接达成。具体步骤如下：

1. 参考[透明卡片开放能力申请](../harmonyos-guides/arkts-ui-transparent-backplate-form-development.md#透明卡片开放能力申请)，在AppGallery Connect中申请“背板透明卡片”权限，并重新生成应用Profile文件。
2. 参考[创建ArkTS卡片](../harmonyos-guides/arkts-ui-widget-creation.md)按标准流程创建ArkTS卡片。
3. 在卡片配置文件form\_config.json中，将transparencyEnabled字段设置为true（该字段为背板透明卡片的必配项）。

   ```json
   {
     "forms": [
       {
         "name": "widget",
         "displayName": "$string:widget_display_name",
         "description": "$string:widget_desc",
         "src": "./ets/widget/pages/WidgetCard.ets",
         "uiSyntax": "arkts",
         "window": {
           "designWidth": 720,
           "autoDesignWidth": true
         },
         "colorMode": "auto",
         "isDynamic": true,
         "isDefault": true,
         "updateEnabled": false,
         "scheduledUpdateTime": "10:30",
         "updateDuration": 1,
         "defaultDimension": "2*2",
         "transparencyEnabled": true,
         "supportDimensions": [
           "2*2"
         ]
       }
     ]
   }
   ```
4. 为实现“自定义边框”视觉效果，建议将卡片核心内容区域尺寸设计得小于卡片整体尺寸，使背景透明区域露出，形成边框或悬浮感。

   ```ts
   @Entry
   @Component
   struct WidgetCard {
     @Builder
     item() {
       Row()
         .backgroundColor(Color.Pink)
         .borderRadius(5)
         .width(10)
         .height(30);
     }

     build() {
       Stack({ alignContent: Alignment.Top }) {
         Column() {
           Row() {
           }
           .layoutWeight(1);

           Row() {
             Text('好好学习   天天向上')
               .fontSize(26);
           }
           .justifyContent(FlexAlign.Center)
           .padding(10)
           .borderRadius(16)
           .backgroundColor(Color.Brown)
           .width('100%')
           .height('90%');
         }.width('100%')
         .height('100%');

         Row({ space: 10 }) {
           this.item();
           this.item();
           this.item();
         }
         .justifyContent(FlexAlign.SpaceBetween)
         .padding(20)
         .width('100%')
         .height(30);
       };

     }
   }
   ```
5. 在调试或发布阶段，需进行[手动签名](../harmonyos-guides/ide-signing.md#section297715173233)，确保权限生效。

## 常见FAQ

Q：如何实现透明卡片？

A：从API version 22开始，Form Kit提供卡片[背板元素透明显示](../harmonyos-guides/arkts-ui-transparent-backplate-form-development.md)的能力，满足更丰富的UI设计以及美观诉求。
