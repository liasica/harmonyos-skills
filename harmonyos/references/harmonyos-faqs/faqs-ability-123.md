---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-123
title: 应用在设备上显示的图标，和应用市场上显示的图标不一致
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 应用在设备上显示的图标，和应用市场上显示的图标不一致
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:55+08:00
doc_updated_at: 2026-07-31
content_hash: sha256:3d9de1a91ab39629ab43211f0a5061106051707d32b6bd22fbf5c2db578416e0
---

## 问题现象

应用在桌面和设置中应用列表显示的图标，与应用市场中的图标不一致。

## 背景知识

* 在开发应用时，需要配置应用的一些标签，例如[配置应用图标和名称](../harmonyos-guides/layered-image.md)等。
* 在将应用上架至应用市场时，需要确保在上架流程中上传的应用图标与开发应用时配置的应用图标保持一致，避免造成误导。
* [应用图标和名称](../harmonyos-guides/application-component-configuration-stage.md#应用图标和名称配置)通常一起配置，对应app.json5配置文件和module.json5配置文件中的icon和label。
* 图标和标签主要有以下三个[使用场景](../harmonyos-guides/layered-image.md#使用场景)：
  + 用于在应用界面内展示当前应用。例如：在设置应用中展示应用列表，在设置的隐私管理中展示应用申请的权限。通常在配置文件中设置。
  + 用于在设备桌面上展示当前应用。例如：桌面或者最近任务列表中显示应用。通常在配置文件中设置。
  + 用于在通知栏中展示发出通知消息的应用或在应用实况窗中展示当前实况窗的来源应用。
    - 通知栏中的图标通常在通知栏开发的对应代码中设置，可以在[发送通知消息](../harmonyos-guides/push-send-alert.md)时携带image字段设置消息[通知大图标](../harmonyos-guides/push-send-alert.md#通知大图标)内容，提醒用户查看对应的应用消息。
    - 实况窗中的图标通常在实况窗开发的对应代码中设置，可参考Live View Kit（实况窗服务）[使用入门](../harmonyos-guides/liveview-introduction.md#使用入门)进行设计。

## 问题定位

排查应用使用的图标和[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/)中上传的图标是否一致。根据以下情况确认应用图标，检查对应配置文件中的icon标签是否引用的是期望的图标资源。若引用的图片资源与上架应用市场流程中上传的图片资源不一致，则会造成误导，不符合预期。

* 若HAP中包含UIAbility，查看是否在module.json5配置文件的abilities标签中配置了icon。
  + 若对应的ability中skills标签下面的entities中包含"entity.system.home"、actions中包含"ohos.want.action.home"或者"action.system.home"，则系统将优先返回module.json5中的icon。
  + 若存在多个满足条件的ability，优先返回module.json5中mainElement对应的ability配置的icon。
  + 若在module.json5配置文件的abilities标签中未设置icon，或者对应的skills标签下面的entities与actions没有做相关配置，那么系统将使用app.json5中的icon。
* 若HAP中不包含UIAbility，系统将使用app.json5中的icon。

* app.json5配置示例：

  ```ts
  {
    "app": {
      "icon": "$media:app_icon",
      "label": "$string:app_name"
      // ...
    }
  }
  ```
* module.json5配置示例：

  ```ts
  {
    "module": {
      // ...
      "abilities": [
        {
          // ...
          "icon": "$media:icon",
          "label": "$string:EntryAbility_label",
          "skills": [
            {
              "entities": [
                "entity.system.home"
              ],
              "actions": [
                "ohos.want.action.home"
              ]
            }
          ],
        }
      ]
    }
  }
  ```

## 分析结论

图标显示不一致的原因为配置文件中的icon标签引用的图标资源，与上架应用市场时上传的图标资源不一致，即配置文件中的icon字段未被正确设置。

## 修改建议

在相应的配置文件中的icon标签引用期望的图标资源，同时需确保引用的图片资源符合设计规范，详情可参考[图标资源规范](../design-guides/application-icon-0000001953444009.md#section634668113212)。

## 常见FAQ

A：AGC配置的图标和包名，会覆盖HAP包中配置的图标和包名吗？

Q：AGC的包名是强制校验项，HAP包必须主动匹配，而非被覆盖。AGC的图标配置仅影响应用市场展示和设置界面，桌面图标由HAP包的module.json5直接控制。参考以下覆盖规则：

* 包名覆盖规则：

  不会自动覆盖：AGC配置的包名不会直接覆盖HAP包中的bundleName。相反，HAP包的bundleName必须与AGC创建应用时填写的包名严格一致，否则上传软件包时会因包名冲突而失败。

  手动维护一致性：开发者需确保module.json5或app.json5中的bundleName字段与AGC应用配置的包名一致。
* 图标覆盖规则：

  桌面图标由HAP包决定：应用在设备桌面显示的图标由HAP包中module.json5的icon字段配置的图标资源决定。

  设置中的图标可能被覆盖：如果通过build-profile.json5的products配置了不同产物的icon字段，这些配置会覆盖app.json5中的默认设置，但仅影响设置界面中的应用信息显示，不影响桌面图标。
