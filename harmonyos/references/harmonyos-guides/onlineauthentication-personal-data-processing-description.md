---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/onlineauthentication-personal-data-processing-description
title: 个人数据处理说明
breadcrumb: 指南 > 系统 > 安全 > Online Authentication Kit（在线认证服务） > 个人数据处理说明
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:03+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:00b6131735fd4a960fe7d5dc628fd97127576bc033ca4b06328eda48c16a6818
---

此文档针对华为作为最终用户数据处理者，开发者作为最终用户数据控制者的数据处理进行说明，包括：

* 华为处理的个人数据清单
* 指导开发者如何帮助最终用户实现对数据的控制

## 华为处理的个人数据清单

最后修改时间：2026/05/11

| 个人数据清单 | 使用目的 | 存留期 |
| --- | --- | --- |
| 指纹ID | FIDO、SOTER、IFAA服务和数字身份服务会将匿名化的指纹ID返回至应用，以提供绑定具体生物特征的免密认证能力 | 用户注销FIDO、SOTER和IFAA服务功能删除或者用户删除数字身份标识DID时删除 |
| 面容ID | FIDO、SOTER、IFAA服务和数字身份服务会将匿名化的面容ID返回至应用，以提供绑定具体生物特征的免密认证能力 | 用户注销FIDO、SOTER和IFAA服务功能删除或者用户删除数字身份标识DID时删除 |
| 数字身份凭证信息 | 数字身份服务会将凭证信息返回至应用，以提供数字身份管理、可验证凭证管理等能力 | 用户删除数字凭证时删除 |
| 应用的用户昵称 | 通行密钥服务需要将应用中的用户昵称上传至网络中继服务器，用于跨设备扫码认证场景，以便实现两台设备的认证数据通信 | 不存储 |
| 应用的用户标识符 | 通行密钥服务需要将应用中的用户标识符信息上传至网络中继服务器，用于跨设备扫码认证场景，以便实现两台设备的认证数据通信 | 不存储 |

## 指导开发者如何帮助最终用户实现对数据的控制

开发者通过Online Authentication Kit API获取的用户数据，需要开发者自行提供对应的数据主体权利。
