---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-healthservice-9
title: 企业开发者同步运动健康数据指导
breadcrumb: FAQ > 应用服务开发 > 运动健康数据服务（Health Service Kit） > 企业开发者同步运动健康数据指导
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:52+08:00
doc_updated_at: 2026-08-26
content_hash: sha256:83a0917f956d519ae7c24c815541621438d93195e9f58c163a6ae835e91561e9
---

## 问题现象

1. 管理中心申请运动健康服务，产品类型很多，具体如何选择？
2. 申请运动健康数据权限上传材料有哪些注意事项？
3. 申请成功后企业开发者如何同步运动健康数据？
4. 海外穿戴应用服务开发可以获取健康云的数据吗？

## 背景知识

* 运动健康服务：参考[Health Service Kit简介](../harmonyos-guides/health-service-kit-ability.md)。

  华为运动健康开放平台提供了多种形式的开放能力，支持应用生态开放能力和设备接入开放能力。提供丰富的运动健康类的API，支持多种运动类型和健康数据的数据开放，如步数、心率等。
* 企业资质：参考[企业、事业单位/政府机构、社会团体开发者接入资质审核要求](../harmonyos-guides/health-application-qualifications.md#企业事业单位政府机构社会团体开发者接入资质审核要求)。

  企业以实缴注册资本为准，申请访问开放等级为基础的用户数据，企业实缴注册资本不低于50万元；申请访问开放等级为高阶的用户数据，企业实缴注册资本不低于500万元。申请主体存续且成立时间需1年以上。

## 解决方案

1. 运动健康服务是为华为生态应用打造的基于华为账号和用户授权的运动健康数据开放平台。在获取用户授权后，开发者可以使用Health Service Kit提供的开放能力获取运动健康数据。
   * HarmonyOS Next应用详情请参考：[接入流程](../harmonyos-guides/health-application-access.md)、[数据开放总览](../harmonyos-guides/health-data-overview.md)，[应用开发者申请资质说明](../harmonyos-guides/health-application-qualifications.md)。
   * HarmonyOS 3.x/4.x应用请参考：[面向应用开放服务](../HMSCore-Guides/application_description-0000001418052318.md)。
2. 产品类型选择HarmonyOS应用，并填写申请信息，勾选产品必需申请的数据权限。需注意：
   * 添加运动健康服务时，遵循权限最小化原则。数据访问权限应与业务相符，不可申请超出业务范围或者暂不使用的权限。
   * 在应用或服务发布后，华为会对权限使用情况进行不定期抽查，抽查形式包括但不限于对已发布的应用进行抽样检查、对API调用情况进行监控、派遣专员核查等。您可以通过在申请运动健康服务前签署的合作协议，了解核查标准以及核查后的处理方式。
   * 数据类型对应的OAuth权限请参见[权限说明](../harmonyos-guides/health-permission-description.md)。

     申请材料注意事项可以参考[申请被驳回的常见问题](../harmonyos-guides/health-apply.md#申请被驳回的常见问题)。
3. 企业开发者可申请数据权限具体参考[数据开放总览](../harmonyos-guides/health-data-overview.md)，开放等级中，上锁图标表示该数据权限为高阶数据，暂不对个人开发者开放。如需使用，请使用企业账号重新注册并申请权限；开锁图标表示该数据权限为基础数据，个人及企业开发者均可申请查询/使用。

   申请运动健康服务通过后需[配置Client ID](../harmonyos-guides/health-configuration-client-id.md)。

   具体开发指导参考：[Phone/Tablet应用开发](../harmonyos-guides/health-app-dev.md)、[Wearable应用开发](../harmonyos-guides/health-wearable-app-dev.md)。
4. Health Service Kit[支持的国家/地区](../harmonyos-guides/health-service-kit-ability.md#支持的国家地区)仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。

   海外开发者可以选择[云侧数据开放服务](../HMSCore-Guides/cloud_dateservice-0000001418212814.md)：HUAWEI Health Service Kit允许三方生态应用通过REST API接口访问数据库，对用户数据进行增、删、改、查等操作，为用户提供运动健康类数据服务。

   具体支持的国家/地区参考：[基础能力支持的国家/地区](../HMSCore-Guides/countries_and_regions-0000001470884353.md)、[扩展能力支持的国家/地区](../HMSCore-Guides/extended_countries_and_regions-0000001461157870.md)。

   海外接入文档可以参考[Introduction to Health Service Kit](https://developer.huawei.com/consumer/en/doc/HMSCore-Guides/description-0000001558389985)。

## 常见FAQ

Q：申请运动健康服务时，数据使用场景说明中的“应用模拟截图”是否必须提供？可以仅描述数据使用说明而不提交截图吗？

A：可以不提供应用模拟截图，但数据使用说明不能过于简略单一，需将数据使用场景描述清楚，并遵循最小数据权限原则。

Q：提升数据开放实时性与订阅数据两个服务的时效性分别是怎样的？

A：运动健康App属于近实时数据开放，云端订阅属于小时级数据开放。如需提升数据开放实时性，可参考[实时数据开放](../HMSCore-Guides/real-time-data-openness-0000001504559665.md)。

Q：已申请其他运动健康数据权限后，再申请心脏健康数据或肺功能数据是否需要满足额外条件？

A：不需要满足额外条件。已通过其他健康数据申请的企业开发者，可以直接提交心脏健康数据和肺功能数据的申请。
