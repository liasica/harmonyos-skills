---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/asset-scenario2
title: 保护需要用户认证的密码类数据
breadcrumb: 指南 > 系统 > 安全 > Asset Store Kit（关键资产存储服务） > 常见场景 > 保护需要用户认证的密码类数据
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:10+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:3554f3cf3a3c1ddfc61e1341f78b7852d0c7ef9ea102ab932c3f6d09f41a00f0
---

说明

密码类数据可以是密码、登录令牌、信用卡号等用户敏感数据。

## 场景描述

用户在金融/银行类应用中查看银行卡号时，需要核实用户身份为持卡人本人。针对此种场景，应用可以将银行卡号存储到ASSET中，同时设置访问银行卡号需要用户身份认证。

用户查看银行卡号时，应用请求用户进行身份认证（例如通过验证锁屏密码或生物特征），身份校验通过后，应用查询并向用户展示银行卡号，极大地提升了用户安全体验。

## 关键流程

业务调用ASSET保护需要用户认证的关键资产，可以参照以下流程进行开发。

说明

由于统一用户认证（UserIAM）只提供ArkTS接口，故本场景只支持使用ArkTS语言开发。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/_jJOSZ6aRq6aT4x3mCC-sQ/zh-cn_image_0000002583438421.png?HW-CC-KV=V1&HW-CC-Date=20260427T234209Z&HW-CC-Expire=86400&HW-CC-Sign=48299F7A7A73D277CB287A0B19C0C2103B9AA4423DB29315BDB6D0B3BDB6F1D2)

1. 业务查询符合条件的关键资产属性，根据查询成功或失败，判断关键资产是否存在。

   * 开发步骤参考[查询关键资产](asset-js-query.md)，代码示例参考[查询单条关键资产属性](asset-js-query.md#查询单条关键资产属性)。
2. 如果关键资产不存在，业务可选择：

   * 新增关键资产，开发步骤参考[新增关键资产](asset-js-add.md)。
3. 如果关键资产存在，业务可选择：

   * 删除关键资产，开发步骤参考[删除关键资产](asset-js-remove.md)。
   * 更新关键资产，开发步骤参考[更新关键资产](asset-js-update.md)。
   * 查询关键资产明文，开发步骤包括预处理、用户认证、查询明文、后置处理，参考[查询需要用户认证的关键资产](asset-js-query-auth.md)。
