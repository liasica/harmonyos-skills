---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-fusion-intelligentfilling-appendix
title: ContentType使用场景说明
breadcrumb: 指南 > 应用服务 > Scenario Fusion Kit（融合场景服务） > 智能填充服务 > ContentType使用场景说明
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:47+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:58369086c6d9be3828fc5cb9235c050aa20dc0e55ac0a40aa63fd8210691492f
---

华为账号昵称

| 名称 | 说明 |
| --- | --- |
| NICKNAME | 昵称，如“Vivian”。 |

用户姓名

| 名称 | 说明 |
| --- | --- |
| PERSON\_FULL\_NAME | 姓名，如“张三”。 |
| PERSON\_LAST\_NAME | 姓氏，如“张”。 |
| PERSON\_FIRST\_NAME | 名字，如“三”。 |

说明

* PERSON\_FULL\_NAME和（PERSON\_LAST\_NAME，PERSON\_FIRST\_NAME）不能同时在同一个表单中使用（在护照信息场景中可以同时使用）。
* 请在收集使用用户敏感个人信息的表单界面告知目的以及必要性。

联系方式

| 名称 | 说明 |
| --- | --- |
| PHONE\_NUMBER | 手机号，如“188\*\*\*\*\*\*88”。 |
| EMAIL\_ADDRESS | 邮箱地址，如“a\*\*\*\*t@huawei.com”。 |

身份信息

| 名称 | 说明 |
| --- | --- |
| ID\_CARD\_NUMBER | 身份证号，如“3201\*\*\*\*\*\*\*\*\*\*\*123”。 |

说明

* ID\_CARD\_NUMBER目前只支持身份证号的推荐、填充，不支持其他类型的证件，可参考[动态修改ContentType值](scenario-fusion-intelligentfilling-amend.md)动态配置输入框的ContentType。
* 请在收集使用用户敏感个人信息的表单界面告知目的以及必要性。

护照信息

| 名称 | 说明 |
| --- | --- |
| COUNTRY\_ADDRESS | 国籍，如“中国”。 |
| PASSPORT\_NUMBER | 护照号，如“G\*\*\*\*\*\*\*1”。 |
| VALIDITY | 有效期至，如“2025-1-1”。 |
| ISSUE\_AT | 签发地，如“广东”。 |

说明

请在收集使用用户敏感个人信息的表单界面告知目的以及必要性。

车牌信息

| 名称 | 说明 |
| --- | --- |
| LICENSE\_PLATE | 车牌号，如“粤A\*\*\*\*\*1”。 |

地址信息

| 名称 | 说明 |
| --- | --- |
| FULL\_STREET\_ADDRESS | 带街道详细地址，如“雨花街道玉兰路98号”。 |
| FORMAT\_ADDRESS | 全量地址，如“中国江苏省南京市雨花台区雨花街道玉兰路98号”。 |
| DETAIL\_INFO\_WITHOUT\_STREET | 不带街道详细地址，如“玉兰路98号”。 |
| ADDRESS\_CITY\_AND\_STATE | 所在地区，如“中国广东省深圳市龙岗区”。 |

发票抬头信息

| 名称 | 说明 |
| --- | --- |
| ORGANIZATION | 名称，如“深圳市xx公司”。 |
| TAX\_ID | 税号，如“2020\*\*\*\*\*\*\*\*\*\*\*000”。 |
