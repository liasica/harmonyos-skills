---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-linking-1
title: 如何解决AppLinking跳转与推送通知消息跳转配置冲突问题
breadcrumb: FAQ > 应用服务开发 > 应用链接跳转服务（App Linking Kit） > 如何解决AppLinking跳转与推送通知消息跳转配置冲突问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:50+08:00
doc_updated_at: 2026-08-12
content_hash: sha256:74c3a66dc59770a9306f41ddcfbc30456622dce40a828228faa654c1396cb88d
---

## 问题现象

AppLinking配置与推送通知配置存在冲突问题，如果在skill中配置了uris会导致消息推送失败，如果不配置uris会导致AppLinking跳转无法使用，module.json5配置如下:

```screen
{
  "name": "TestAbility",
  "srcEntry": "./ets/abilities/TestAbility.ets",
  "exported": false,
  "startWindowIcon": "$media:icon",
  "startWindowBackground": "$color:start_window_background",
  "skills": [
    {
      "actions": [
        "action.system.home",
        // 极光推送需要此字段
        "ohos.want.action.viewData"
        // 微博跳转配置
      ],
      // 目前推送和AppLinking配置存在互斥，如果在skill中配置了uris会导致接入的第三方库【极光推送】无法正常接收到通知，如果不配置uris会导致AppLinking配置失效
      "uris": [
        // appLink的配置
        {
          "scheme": "https",
          // scheme须配置为https
          "host": "xxx.xxx.com",
          // host须配置为关联的域名
          "path": "open"
          // path可选，为了避免匹配到多个应用，建议配置该字段【可选字段】
        }
      ]
    }
  ]
}
```

## 背景知识

* 使用[App Linking](../harmonyos-guides/app-linking-startup.md)进行跳转时，系统会根据接口传入的uri信息（HTTPS链接）将用户引导至目标应用中的特定内容，无论应用是否已安装，用户都可以访问到链接对应的内容，跳转体验相比Deep Linking方式更加顺畅。
* 使用推送服务[点击消息进入应用首页并传递数据](../harmonyos-guides/push-send-alert.md#点击消息进入应用首页)时，检查项目模块级别下的src/main/module.json5中的skills标签配置，其中用于标识应用首页的skill（即配置了"entity.system.home"和"action.system.home"的skill）中不要配置uris。

## 问题定位

AppLinking跳转需要配置uri，推送消息跳转用于标识应用首页的skill不能配置uris。

## 分析结论

开发者将推送消息跳转和AppLinking跳转配置在同一个skill对象中，导致冲突。

## 修改建议

可以在skills数组中创建不同的skill对象，分别映射对应的能力，参考[点击消息进入应用内页](../harmonyos-guides/push-send-alert.md#点击消息进入应用内页)步骤1中方式二的示例代码。

## 总结

如果需要同时设置推送消息跳转能力和其他跳转能力（如NFC跳转、浏览器跳转等），module.json5文件中的skills标签下可以同时配置多个skill对象，每个对象对应一种能力。
