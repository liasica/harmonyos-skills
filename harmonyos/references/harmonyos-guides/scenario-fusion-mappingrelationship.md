---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-fusion-mappingrelationship
title: H5/三方框架和HarmonyOS配置项映射关系
breadcrumb: 指南 > 应用服务 > Scenario Fusion Kit（融合场景服务） > 智能填充服务 > 三方框架+H5接入智能填充 > H5/三方框架和HarmonyOS配置项映射关系
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:49+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ca902eb6ac79949d2638e4e18f96a90e62dd61e17503d1ec81bfd3c04e0409a0
---

## H5 autocomplete和HarmonyOS的ContentType的映射关系

| 输入场景 | 【H5】autocomplete | 【ArkUI】ContentType | 说明 |
| --- | --- | --- | --- |
| 昵称 | nickname | NICKNAME | 昵称，如“Vivian”。 |
| 姓名 | name | PERSON\_FULL\_NAME | 姓名，如“张三”。 |
| 姓氏 | family-name | PERSON\_LAST\_NAME | 姓氏，如“张”。 |
| 名字 | given-name | PERSON\_FIRST\_NAME | 名字，如“三”。 |
| 手机号 | tel-national | PHONE\_NUMBER | 手机号，如“188\*\*\*\*\*\*88”。 |
| 邮件地址 | email | EMAIL\_ADDRESS | 邮箱地址，如“a\*\*\*\*t@huawei.com”。 |
| 身份证号 | id-card-number | ID\_CARD\_NUMBER | 身份证号，如“3201\*\*\*\*\*\*\*\*\*\*\*123”。 |
| 地址 | street-address | FULL\_STREET\_ADDRESS | 带街道详细地址，如“雨花街道玉兰路98号”。 |
| 国籍 | country | COUNTRY\_ADDRESS | 国籍，如“中国”。 |
| 护照号 | passport-number | PASSPORT\_NUMBER | 护照号，如“G\*\*\*\*\*\*\*1”。 |
| 有效期至 | validity | VALIDITY | 有效期至，如“2025-1-1”。 |
| 签发地 | issue-at | ISSUE\_AT | 签发地，如“广东”。 |
| 车牌号 | license-plate | LICENSE\_PLATE | 车牌号，如“粤A\*\*\*\*\*1”。 |
| 名称 | organization | ORGANIZATION | 名称，如“深圳市xx公司”。 |
| 税号 | tax-id | TAX\_ID | 税号，如“2020\*\*\*\*\*\*\*\*\*\*\*000”。 |

说明

autocomplete配置项name和（family-name，given-name）不能同时在同一个表单中使用（在护照信息场景中可以同时使用）。

## React Native textContentType和HarmonyOS的ContentType的映射关系

| 输入场景 | 【React Native】textContentType | 【ArkUI】ContentType | 说明 |
| --- | --- | --- | --- |
| 昵称 | nickname | NICKNAME | 昵称，如“Vivian”。 |
| 姓名 | name | PERSON\_FULL\_NAME | 姓名，如“张三”。 |
| 姓氏 | familyName | PERSON\_LAST\_NAME | 姓氏，如“张”。 |
| 名字 | givenName | PERSON\_FIRST\_NAME | 名字，如“三”。 |
| 手机号 | telephoneNumber | PHONE\_NUMBER | 手机号，如“188\*\*\*\*\*\*88”。 |
| 邮件地址 | emailAddress | EMAIL\_ADDRESS | 邮箱地址，如“a\*\*\*\*t@huawei.com”。 |
| 身份证号 | idCardNumber | ID\_CARD\_NUMBER | 身份证号，如“3201\*\*\*\*\*\*\*\*\*\*\*123”。 |
| 全量地址 | formatAddress | FORMAT\_ADDRESS | 全量地址，如“中国江苏省南京市雨花台区雨花街道玉兰路98号”。 |
| 街道详细地址 | fullStreetAddress | FULL\_STREET\_ADDRESS | 带街道详细地址，如“雨花街道玉兰路98号”。 |
| 详细地址 | detailInfoWithoutStreet | DETAIL\_INFO\_WITHOUT\_STREET | 不带街道详细地址，如“玉兰路98号”。 |
| 国籍 | countryName | COUNTRY\_ADDRESS | 国籍，如“中国”。 |
| 护照号 | passportNumber | PASSPORT\_NUMBER | 护照号，如“G\*\*\*\*\*\*\*1”。 |
| 有效期至 | validity | VALIDITY | 有效期至，如“2025-1-1”。 |
| 签发地 | issueAt | ISSUE\_AT | 签发地，如“广东”。 |
| 车牌号 | licensePlate | LICENSE\_PLATE | 车牌号，如“粤A\*\*\*\*\*1”。 |
| 名称 | organization | ORGANIZATION | 名称，如“深圳市xx公司”。 |
| 税号 | taxId | TAX\_ID | 税号，如“2020\*\*\*\*\*\*\*\*\*\*\*000”。 |

说明

textContentType配置项name和（familyName，givenName）不能同时在同一个表单中使用（在护照信息场景中可以同时使用）。
