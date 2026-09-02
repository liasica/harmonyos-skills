---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-healthservice-8
title: 运动健康测试权限相关问题
breadcrumb: FAQ > 应用服务开发 > 运动健康数据服务（Health Service Kit） > 运动健康测试权限相关问题
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:30+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:d0f9a0f39dd6a7f0ef6bed832d381dc1e6e13dc602379a4d18e86df29d6f2b90
---

## 问题现象

1. 开发者联盟网站上申请了Health Service Kit服务，待审核状态可以测试Health Service Kit能力吗？
2. 运动健康服务已经开通，怎么添加测试用户？
3. 调用用户获取锻炼记录的接口[healthStore.readData](../harmonyos-references/health-api-healthstore.md#healthstorereaddata-1)，返回异常The number of beta users exceeds the maximum。

## 背景知识

[申请运动健康服务](../harmonyos-guides/health-apply.md)，如果审批通过，即可进入“已开通测试权限”阶段，应用可调用相应的接口获取运动健康服务数据进行测试开发。

**说明** 

* 首次申请开通测试权限后权限将及时生效，若业务范围发生变动，修改权限并重新提交申请，请等待测试权限修改生效1小时后再进行测试验证。
* 当前审核通过仅以开发测试为目的，测试阶段有用户数量的限制，仅限前100位用户使用您所申请应用中的华为运动健康服务。为解除用户数量的限制，请在应用完成开发测试验证后提交验证申请，具体请参见[申请验证获取正式权限](../harmonyos-guides/health-verification.md)提交验证申请。
* 测试权限开通后，请于半年内完成[申请验证获取正式权限](../harmonyos-guides/health-verification.md)操作，否则平台将关闭您已开通测试权限。

## 解决方案

1. 需要运动健康服务权限申请通过后，状态由“待审核”改为“已开通测试”后才可验证，“待审核”状态无法测试。具体参考[申请运动健康服务](../harmonyos-guides/health-apply.md)第六点，审核周期约为15个工作日。
2. 当前测试阶段有用户数量的限制，仅限前100位用户使用您申请应用中的华为运动健康服务。为解除用户数的限制，请在应用完成开发测试验证后，参考[申请验证获取正式权限](../harmonyos-guides/health-verification.md)，提交验证申请。
3. 登录[管理中心](https://developer.huawei.com/consumer/cn/console/overview)，点击左侧菜单栏中应用服务，选择Health Service Kit，查看测试人数是否已达上限，若上限已满会返回异常。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/aeFGbhGiQDWDWS_jUxg40A/zh-cn_image_0000002658913951.png "点击放大")
