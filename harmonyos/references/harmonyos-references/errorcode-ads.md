---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-ads
title: 广告服务框架错误码
breadcrumb: API参考 > 应用服务 > Ads Kit（广告服务） > 错误码 > 广告服务框架错误码
category: harmonyos-references
scraped_at: 2026-04-28T08:16:18+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9f190850023d3489c56e556a89240e2568cb0df74d319b5ecfdcfe8619f4ad9f
---

说明

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## 21800001 系统内部错误

PhonePC/2in1Tablet

**错误信息**

System internal error.

**错误描述**

系统内部错误（例如：注册或删除Web组件JavaScript对象失败）。

**可能原因**

连接服务失败。

**处理步骤**

1. 重启设备后重试。
2. 若您的问题仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/add/101704353566310877?level2=101704353626565886&level3=101704354358694993&keyWord=Ads Kit)提交问题，华为支持人员会及时处理。

## 21800003 广告请求加载失败

PhonePC/2in1Tablet

**错误信息**

Failed to load the ad request.

**错误描述**

广告请求加载失败。

**可能原因**

1. 网络连接异常。
2. 广告请求参数错误。
3. 服务器无合适广告填充。

**处理步骤**

1. 请检查网络状态。
2. 请根据API参考检查广告请求参数是否符合要求。
3. 若您的问题仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/add/101704353566310877?level2=101704353626565886&level3=101704354358694993&keyWord=Ads Kit)提交问题，华为支持人员会及时处理。

## 21800004 广告展示失败

PhonePC/2in1Tablet

**错误信息**

Failed to display the ad.

**错误描述**

广告展示失败。

**可能原因**

网络连接异常。

**处理步骤**

请检查网络状态。

## 21800005 广告数据解析失败

PhonePC/2in1Tablet

**错误信息**

Failed to parse the ad response.

**错误描述**

广告数据解析失败。

**可能原因**

广告响应数据缺失关键属性或存在结构错误。

**处理步骤**

请检查广告响应数据。
