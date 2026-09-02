---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-liveview-2
title: 实况窗有哪些支持对接的场景以及消息推送机制
breadcrumb: FAQ > 应用服务开发 > 实况视图服务（Live View Kit） > 实况窗有哪些支持对接的场景以及消息推送机制
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:49+08:00
doc_updated_at: 2026-08-19
content_hash: sha256:a0b28bbe176c62ceece8a848e274d8b2b46acc3e15e5d869494b6ec07c0908f8
---

## 问题现象

* 问题一：实况窗有哪些支持对接的场景？以及如何申请？
* 问题二：官方给出的实况窗参考demo图片改为网络加载，实况窗不弹出来是什么原因？实况窗消息服务器下发下来后，端上能够先拦截处理后再显示吗？实况窗在通知栏未展示出来，并且进入设置->应用和元服务->详情->实况窗开关也看不到这是为什么？推送实况窗需要企业账号吗？
* 问题三：如何实现小组件常驻通知栏且不随一键清除通知而消失？
* 问题四：沉浸式实况窗锁屏不显示地图是什么原因？如何申请沉浸态权限？
* 问题五：实况窗是否支持家居设备类场景的申请？
* 问题六：实况窗是否支持车机设备？

## 解决方案

* 问题一：
  1. [Live View Kit（实况窗服务）](../harmonyos-guides/liveview-introduction.md)支持应用将订单或者服务的实时状态信息变化在设备的关键界面展示，并对展示信息的生命周期、用户界面UI效果等进行管理。实况窗目前为Beta阶段，优先对满足场景准入原则和适用范围的应用开放申请。[实况窗支持对接的场景](../harmonyos-guides/liveview-introduction.md#实况窗支持对接的场景)主要有出行打车、即时配送、运动锻炼、导航等。
  2. 实况窗权益需要开发者根据业务场景，同时满足[实况窗设计规范](../harmonyos-guides/liveview-design-formula.md)，在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)申请，具体申请方法参考[申请实况窗正式权限](../harmonyos-guides/liveview-formal-authority.md)。
* 问题二：
  1. 实况窗需要本地序列化，整体有大小限制，所以对使用的素材也有大小限制，建议下载到本地使用本地图片，且可能是图片超过大小限制了，image.PixelMap大小不能大于30KB，可使用[ImagePacker](../harmonyos-references/arkts-apis-image-imagepacker.md)压缩图片。
  2. 通过Push Kit更新实况窗内容的过程是自动更新的。客户端在创建本地实况窗后，使用Push Kit获取Push Token并调用相关API接口时，Push Kit会自动推送更新消息。因此无法进行拦截。
  3. 在开通实况窗权益前，需要首先为项目开通“[推送服务](../harmonyos-guides/push-config-setting.md)”权益然后才能正常使用实况窗。
  4. 推送实况窗需要企业账号，详情参考[实况窗权益说明](../harmonyos-guides/liveview-rights.md)。
* 问题三：

  支持该能力。建议使用[Live View Kit（实况窗服务）](../harmonyos-guides/liveview-introduction.md)实现。实况窗支持应用将订单或者服务的实时状态信息变化在设备的关键界面展示，并对展示信息的生命周期、用户界面UI效果等进行管理，包含胶囊和卡片两种形式。
* 问题四：
  1. 沉浸式实况窗的支持场景基于有导航功能的场景（如户外跑步），沉浸态需要开通正式权限后才能评审申请，因此已开通普通实况窗权益但未开通沉浸态权限时，锁屏沉浸式实况窗上的地图不会显示。
  2. 实况窗沉浸态没有调测过程，需要参考[实况窗设计规范](../harmonyos-guides/liveview-design-formula.md)设计UX图进行评审，开通权限后应用可以调测并上线。
  3. 实况窗沉浸态权限可以同正式权限同步申请，需在设计方案和功能实现中包含实况窗沉浸态，后续审核人员会同步评审，通过后在开通正式权限后会提交申请开通应用的沉浸态权限，具体申请方法参考[申请实况窗正式权限](../harmonyos-guides/liveview-formal-authority.md)。
* 问题五：

  目前实况窗不支持家居设备类场景的申请。家居场景的厂家设备需接入智慧生活生态，由智慧生活统一来弹实况窗。
* 问题六：

  实况窗当前支持的设备类型包括Phone、PC/2in1、Tablet、TV、Wearable，暂不支持车机设备。
