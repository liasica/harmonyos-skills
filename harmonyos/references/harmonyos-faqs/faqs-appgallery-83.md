---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-83
title: 调用Publishing API（HarmonyOS）的提交发布接口报错
breadcrumb: FAQ > 应用服务开发 > 应用市场服务（AppGallery Kit） > 调用Publishing API（HarmonyOS）的提交发布接口报错
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:902610282f85682ba6f79b91d9509cb0070a22eeb6875fa9f93267d298fd76b6
---

## 问题现象

调用Publishing API（HarmonyOS）的[提交发布接口](../app/agc-help-publish-api-app-submit-0000002271160585.md)，返回错误信息：

```txt
“[amis] update version information failed, additional msg is [[AppGalleryConnectAppMetaInfoService]there is no full release version on shelf!]”。
```

入参为：

```txt
"phasedReleaseEndTime":"2025-02-23T15:25:27+0800","phasedReleaseStartTime":"2025-02-21T15:25:25+0800","releaseType":3,"phasedReleasePercent":"70","emark":null,"phasedReleaseDescription":"测试"
```

## 解决方案

通过调用的入参"releaseType":3，可以看出应用为[分阶段发布](../app/agc-help-maintain-phased-release-0000002271493785.md)类型，提交分阶段发布的前提为已经有一个全网在架的版本了，否则返回“there is no full release version on shelf”的报错信息，先提交全网在架版本，再提交分阶段发布版本。
