---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-ads
title: 广告服务框架错误码
breadcrumb: API参考 > 应用服务 > Ads Kit（广告服务） > 错误码 > 广告服务框架错误码
category: harmonyos-references
scraped_at: 2026-09-02T15:02:51+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b9ce6d209e7b037ae0ed8b9dbba76b2fbe56a2feeb547634b021036c6d188af2
---

**说明** 

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## 21800001 系统内部错误

**错误信息**

System internal error.

**错误描述**

系统内部错误（例如：注册或删除Web组件JavaScript对象失败）。

**可能原因**

连接服务失败。

**处理步骤**

1. 重启设备后重试。
2. 若您的问题仍无法解决，请优先通过企点QQ：800183590、[转人工链接](https://webpage.qidian.qq.com/qidian/chatv3/pc.html?linkType=1&env=ol&kfuin=2885820057&fid=365&key=646c4489e237ea477e85483a1791dfaa&cate=1&type=16&ftype=1&_type=wpa&qidian=true&waitTime=10005&clickid=ad71nq.wg8a2n.l1fu39si&callImType=1&delayTime=10&roleValue=1&roleData=474&translateSwitch=0&source=0&isLBS=0&isSsc=0&isCustomEntry=0&im_jump_from=v2_1)联系技术人员排查处理，若以上方式未能有效解决问题，可通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/add/101704353566310877?level2=101704353626565886&level3=101704354358694993&keyWord=Ads Kit)提交问题。

## 21800003 广告请求加载失败

**错误信息**

Failed to load the ad request.

**错误描述**

广告请求加载失败。

**可能原因**

1. 服务器无合适广告填充。设备是否返回广告，取决于广告底价设置、用户负反馈屏蔽或算法决策等因素，因此无法保证每次请求都有填充。

**处理步骤**

1. 请检查网络状态。
2. 请根据API参考检查广告请求参数是否符合要求。
3. 单台设备多次请求仍无法请求到广告时，建议使用多台设备进行测试。若您的问题仍无法解决，请优先通过企点QQ：800183590、[转人工链接](https://webpage.qidian.qq.com/qidian/chatv3/pc.html?linkType=1&env=ol&kfuin=2885820057&fid=365&key=646c4489e237ea477e85483a1791dfaa&cate=1&type=16&ftype=1&_type=wpa&qidian=true&waitTime=10005&clickid=ad71nq.wg8a2n.l1fu39si&callImType=1&delayTime=10&roleValue=1&roleData=474&translateSwitch=0&source=0&isLBS=0&isSsc=0&isCustomEntry=0&im_jump_from=v2_1)联系技术人员排查处理，若以上方式未能有效解决问题，可通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/add/101704353566310877?level2=101704353626565886&level3=101704354358694993&keyWord=Ads Kit)提交问题。

## 21800004 广告展示失败

**错误信息**

Failed to display the ad.

**错误描述**

广告展示失败。

**可能原因**

网络连接异常。

**处理步骤**

请检查网络状态。

## 21800005 广告数据解析失败

**错误信息**

Failed to parse the ad response.

**错误描述**

广告数据解析失败。

**可能原因**

广告响应数据缺失关键属性或存在结构错误。

**处理步骤**

请检查广告响应数据。
