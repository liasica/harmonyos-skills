---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-carkey-cloud
title: 云侧开发准备
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 数字车钥匙 > 云侧开发准备
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:09+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6c037375e5ffcc0a1edf1a3d66e30ea1b3d40efc607d6f634a721ca38d6a4a36
---

## Wallet Kit服务云侧接入基本信息配置

在[创建Wallet Kit服务](wallet-preparations.md)的配置参数里填写。

| Wallet Kit服务参数名称 | 参数值 |
| --- | --- |
| 服务类型 | 钥匙 |
| 服务项目 | ICCE车钥匙 |
| 服务名称 | xxx数字车钥匙服务（xxx可为公司名称/产品名称）。该字段仅用于方便开发者区分自己配置的多个服务，没有其他用途。 |
| 服务号 | ICCE车钥匙卡片的发卡机构，用于唯一表明某一发卡机构。hwpass.stdcarkey.xxx.xxx（xxx可为公司/产品名称，总长度不超过32个英文小写字符，请严格按照此规则定义）。钱包可根据此值进行发卡机构的管控；在预置模板、生成钥匙卡片以及开通激活过程的请求体中会携带该值。 |
| 接入方式 | 云端接入 |
| 回调地址 | 用于用户添加/删除卡券时回调通知发卡机构的地址，注意：地址必须使用https。示例：https://商户服务器地址/v1/passes/nfccallback。 |
| 用户公钥 | 按照[创建Wallet Kit服务](wallet-preparations.md)步骤5提供的生成方式，并将生成的公钥内容粘贴在此处。 |

| NFC参数名称 | 参数值 |
| --- | --- |
| 是否支持跨设备移动同步 | 是 |
| 是否开通NFC能力 | 是 |

说明

这里的“是否开通NFC能力”，只要支持蓝牙功能，就需要选择是。

## 配置车钥匙管理台地址至钱包服务器

在车钥匙的开通激活阶段，钱包需要向商户服务器请求数据；这整个的数据链路为：华为钱包APP->钱包云服务器->DK业务管理服务。

钱包云服务器向DK业务管理服务请求需要知道DK业务管理服务的地址，因此需要将DK业务管理服务的地址配置进钱包云服务器。

```
1. "registrationsUrl": "商户服务器地址/v1/passes/registrations",
2. "requestPersonalizeTokenUrl": "商户服务器地址/v1/passes/requestPersonalizeToken",
3. "requestPersonalizeUrl": "商户服务器地址/v1/passes/requestPersonalize",
4. "spNfcOperCallBackUrl"："商户服务器地址/v1/passes/nfccallback"
```

## UI设计

| 车钥匙列表元素 | 设计规范 |
| --- | --- |
| LOGO | 尺寸64dp×64dp，提供方图 |
| 名称 | 无 |

| 车钥匙详情元素 | 设计规范 |
| --- | --- |
| LOGO | 尺寸32dp×32dp |
| 名称 | 无 |
| 卡面图片 | 尺寸328dp×205dp，提供方图 |

说明

所有图片请直接提供直角，请勿切圆角；注意在深色模式下，图片的边框不要有白边。
