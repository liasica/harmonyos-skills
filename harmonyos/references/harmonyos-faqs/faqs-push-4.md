---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-push-4
title: 收到推送但是没有铃声和震动提醒
breadcrumb: FAQ > 应用服务开发 > 消息推送服务（Push Kit） > 收到推送但是没有铃声和震动提醒
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:50+08:00
doc_updated_at: 2026-08-12
content_hash: sha256:d729f3ff725811ce5c702673132c069689aae404c9615951ba34919eccffed93
---

## 问题现象

使用消息推送服务，收到消息时，没有铃声和震动提醒。

推送代码如下：

```json
{
    "payload": {
      "notification": {
        "category": "MARKETING",
        "title": "普通通知标题",
        "body": "普通通知内容",
        "clickAction": {
          "actionType": 1,
          "action": "****",
          "uri": "****",
          "data": {
            "securityData": "{
                "data": {
                    "batchNo": "",
                    "msgId": "****",
                    "userId": "****"
                },
                "click_action": "****"
            }"
          }
        }
      }
    },
    "target": {
      "token": ["*******"]
    },
    "pushOptions": {
      "testMessage": true
    }
  }
```

## 背景知识

[Push Kit（推送服务）](../harmonyos-guides/push-kit-introduction.md)是华为提供的消息推送平台，建立了从云端到终端的消息推送通道。所有HarmonyOS应用可通过集成Push Kit，实现向应用实时推送消息，使消息易见，构筑良好的用户关系，提升用户的感知度和活跃度。

## 问题定位

1. category是MARKETING，该消息分类为资讯营销类，消息提醒方式为静默通知，仅在通知栏展示。当category =IM （非MARKETING）时，按照[通知消息分类标准和提醒方式](../harmonyos-guides/push-apply-right.md#通知消息分类标准与提醒方式)，是有震动和铃声的，但是依然没有。
2. 确认是否申请了自分类权益。登录AppGallery Connect网站，点击"我的项目"。在项目列表中找到您的项目，通过"推送服务>配置"，在"配置"页签下选择需要申请自分类权益的应用，查看自分类权益是否已申请。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/Ad-p1DOBSAm0pVIfsg7hkQ/zh-cn_image_0000002655996468.png "点击放大")

## 分析结论

根本原因是应用未申请推送场景化消息权益。未开通通知消息自分类权益的应用，通知消息类型将会默认归为资讯营销类消息，静默通知，仅在通知中心展示消息。

## 修改建议

1. [申请通知消息自分类权益](../harmonyos-guides/push-apply-right.md#申请通知消息自分类权益)。
2. 适配云端category字段，使用对应的服务与通讯类取值，参考如下请求示例：

   ```json
   // POST https://push-api.cloud.huawei.com/v3/3158882***52863/messages:send
   // Authorization:Bearer xxx
   // ****
   // push-type:0
   {
     "payload": {
       "notification": {
         "category": "IM",
         "title": "普通标题",
         "body": "普通内容",
         "clickAction": {
           "actionType": 0
         },
         "style": 0,
         "image": "https://lf*******246.png"
       }
     },
     "target": {
       "token": [
         "MAAALgE4G98BAAAAst*******jg"
       ]
     }
   }
   ```

## 常见FAQ

Q：推送消息是否支持自定义通知铃声，实现收到消息时播报指定铃声？

A：可以通过场景化消息推送中notification的[sound](../harmonyos-references/push-scenariozed-api-request-param.md#notification)字段自定义消息通知铃声，满足收到通知消息后播放指定铃声的需求。
