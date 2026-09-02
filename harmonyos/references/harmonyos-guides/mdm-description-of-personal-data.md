---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mdm-description-of-personal-data
title: 个人数据处理说明
breadcrumb: 指南 > 系统 > 基础功能 > MDM Kit（企业设备管理服务） > 个人数据处理说明
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:08+08:00
doc_updated_at: 2026-06-12
content_hash: sha256:3de2bd8ef725062f3578b485788604c28ff358a0097220831fa9802a8de6acf4
---

此文档针对华为作为最终用户数据处理者，开发者作为最终用户数据控制者的数据处理进行说明，包括：

* MDM Kit处理的个人数据清单
* 指导用户行使数据主体权利

## MDM Kit处理的个人数据清单

| 个人数据清单 | 使用目的 | 存留期 |
| --- | --- | --- |
| MAC地址 | 开发者可以通过MDM API获取设备MAC地址。 | 不留存。 |
| 联系电话 | 开发者可以通过MDM API获取设备联系电话。 | 不留存。 |
| 已安装应用列表 | 开发者可以通过MDM API获取已安装应用列表。 | 不留存。 |
| SN | 开发者可以通过MDM API获取设备SN。 | 不留存。 |
| 系统属性 | 开发者可以通过MDM API获取系统属性。 | 不留存。 |
| IP地址 | 开发者可以通过MDM API获取设备IP地址。 | 不留存。 |
| 蓝牙列表 | 开发者可以通过MDM API获取设备蓝牙列表。 | 不留存。 |
| 系统日志 | 开发者可以通过MDM API获取设备系统日志。 | 不留存。 |
| ICCID | 开发者可以通过MDM API获取设备ICCID。 | 不留存。 |
| IMEI | 开发者可以通过MDM API获取设备IMEI。 | 不留存。 |
| MEID | 开发者可以通过MDM API获取设备MEID。 | 不留存。 |
| IMSI | 开发者可以通过MDM API获取设备IMSI。 | 不留存。 |
| 应用使用记录 | 开发者可以通过MDM API获取设备应用使用记录(应用使用时长)。 | 不留存。 |

## 指导用户行使数据主体权利

开发者通过MDM Kit API获取的用户数据，需要开发者自行提供对应的数据主体权利。
