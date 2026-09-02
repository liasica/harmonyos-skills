---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-healthservice-6
title: 如何获取运动健康全量数据副本
breadcrumb: FAQ > 应用服务开发 > 运动健康数据服务（Health Service Kit） > 如何获取运动健康全量数据副本
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:52+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:9c63a2948915572f0f87ce7d88fa5a93e41cd46291732abdb45f6ba5fd00c737
---

## 问题现象

基于HarmonyOS设备已经采集到的运动健康数据，如何获取到全量数据副本并导出为CSV或JSON格式？

## 背景知识

[Health Service Kit（运动健康服务）](../harmonyos-guides/health-service-kit-guide.md)是为华为生态应用打造的基于华为账号和用户授权的运动健康数据开放平台。在获取用户授权后，开发者可以使用Health Service Kit提供的开放能力获取运动健康数据，基于多种类型数据构建运动健康领域应用与服务，为用户打造丰富、便捷、专业的运动健康场景体验。

[隐私中心](https://privacy.consumer.huawei.com/tool?lang=zh-cn&themeName=blue)可以管理您的隐私，详情可访问[隐私声明](https://legal.cloud.huawei.asia/website/privacy/index.htm?language=zh-cn&code=SG)查看所有功能。

## 解决方案

* 参考官网[指导开发者如何帮助最终用户实现对数据的控制](../harmonyos-guides/health-personal-data-processing.md#指导开发者如何帮助最终用户实现对数据的控制)：开发者通过华为运动健康服务API，可以通过数据访问接口获取用户数据，为用户提供数据导出服务，具体方法见[healthStore.readData](../harmonyos-references/health-api-healthstore.md#healthstorereaddata)，详细使用请参见[运动健康采样数据](../harmonyos-guides/health-samplepoint-manage.md)开发指导。
* 部分运动数据可以在华为运动健康APP中直接导出，更完整的数据需要前往[隐私中心](https://privacy.consumer.huawei.com/tool?lang=zh-cn&themeName=blue)申请获取，通过隐私中心申请运动健康数据副本获取步骤如下：
  1. 登录网站隐私中心，扫码或登录华为运动健康账号；
  2. 选择“获取您的隐私副本”并输入验证码进行身份验证；
  3. 待审核通过后会收到短信/邮件通知，再次登录页面，选择“运动健康”下载数据副本。
