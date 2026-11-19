---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/asset-scenario1
title: 保护密码类数据
breadcrumb: 指南 > 系统 > 安全 > Asset Store Kit（关键资产存储服务） > 常见场景 > 保护密码类数据
category: harmonyos-guides
scraped_at: 2026-11-19T09:48:01+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:fd28951dd62e9903323086a1a76799330b00b5f097ce05404f5887854ae816c0
---

**说明** 

密码类数据可以是密码、登录令牌、信用卡号等用户敏感数据。

## 场景描述

用户在应用/浏览器中登录账号时，可以选择“记住密码”（如图）。针对此种场景，应用/浏览器可以将用户密码存储在ASSET中，由ASSET保证用户密码的安全性。

用户再次打开登录界面时，应用/浏览器可以从ASSET中查询用户密码，并将其自动填充到密码输入框，用户只需点击“登录”按钮即可完成账号登录，极大地提升了用户体验。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/_-T5m7DARPqkvOn-jzyt3g/zh-cn_image_0000002820525659.png?HW-CC-KV=V1&HW-CC-Date=20261119T014710Z&HW-CC-Expire=31536000000&HW-CC-Sign=35AD525BAF64B8D9E29E63B87925A64BA8E65D00BE594E1597FA1C5FA4321441)

## 关键流程

业务调用ASSET保护密码类数据（后文统称为“关键资产”），可以参照以下流程进行开发。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/6G6bXKBySI2-W6-kEm1CLA/zh-cn_image_0000002820405659.png?HW-CC-KV=V1&HW-CC-Date=20261119T014710Z&HW-CC-Expire=31536000000&HW-CC-Sign=E644CF1BAA8DC9985AD2E42A543C8A3179C4D2A8B5C24EB50EA8BD926D253626)

1. 业务查询符合条件的关键资产属性，根据查询成功/失败，判断关键资产是否存在。

   * 开发步骤参考[查询关键资产(ArkTS)](asset-js-query.md) / [查询关键资产(C/C++)](asset-native-query.md)，代码示例参考[查询单条关键资产属性(ArkTS)](asset-js-query.md#查询单条关键资产属性) / [查询单条关键资产属性(C/C++)](asset-native-query.md#查询单条关键资产属性)。
2. 如果关键资产不存在，业务可选择：

   * 新增关键资产，开发步骤参考[新增关键资产(ArkTS)](asset-js-add.md) / [新增关键资产(C/C++)](asset-native-add.md)。
3. 如果关键资产存在，业务可选择：

   * 删除关键资产，开发步骤参考[删除关键资产(ArkTS)](asset-js-remove.md) / [删除关键资产(C/C++)](asset-native-remove.md)。
   * 更新关键资产，开发步骤参考[更新关键资产(ArkTS)](asset-js-update.md) / [更新关键资产(C/C++)](asset-native-update.md)。
   * 查询关键资产明文，开发步骤参考[查询关键资产(ArkTS)](asset-js-query.md) / [查询关键资产(C/C++)](asset-native-query.md)，代码示例参考[查询单条关键资产明文(ArkTS)](asset-js-query.md#查询单条关键资产明文) / [查询单条关键资产明文(C/C++)](asset-native-query.md#查询单条关键资产明文)。
