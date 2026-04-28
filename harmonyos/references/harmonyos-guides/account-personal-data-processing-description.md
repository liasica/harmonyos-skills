---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-personal-data-processing-description
title: 个人数据处理说明
breadcrumb: 指南 > 应用服务 > Account Kit（华为账号服务） > 个人数据处理说明
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:08+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:50215cb28a985ec0af8b814c84315ecee857d13bbf7f0b420964546c11d2e25d
---

此文档针对华为作为最终用户数据处理者，开发者作为最终用户数据控制者的数据处理进行说明，包括：

* 华为处理的个人数据清单
* 指导开发者如何帮助最终用户实现对数据的控制

## 华为处理的个人数据清单

最后修改时间：2025/12/18

| 个人数据清单 | 使用目的 | 存留期 |
| --- | --- | --- |
| 账号信息 | 当用户在第三方应用使用华为账号授权登录功能时，用户授权后，应用开发者可以从账号获取到账号信息（包含头像、昵称、华为账号信息以及年龄段） | 该信息会在用户注销华为账号时删除 |
| 联系方式 | 当用户在第三方应用使用华为账号授权登录功能时，用户授权后，应用开发者可以从账号获取到联系方式（手机号、邮箱） | 该信息会在用户注销华为账号时删除 |
| 发票抬头信息 | 当用户在第三方应用使用华为账号获取发票抬头功能时，用户授权后，应用开发者可以从账号获取到发票抬头信息 | 该信息会在用户注销华为账号时删除 |
| 地址信息 | 当用户在第三方应用使用华为账号获取地址信息功能时，用户授权后，应用开发者可以从账号获取到地址信息 | 该信息会在用户注销华为账号时删除 |

## 指导开发者如何帮助最终用户实现对数据的控制

开发者通过Account Kit API获取的用户数据，需要开发者自行提供对应的数据主体权利。Account Kit存储的用户个人数据请参考《[关于华为账号与隐私的声明](https://legal.cloud.huawei.com/terms/scope/huawei/id-hmos/privacy-statement.htm?code=CN&language=zh-CN)》
