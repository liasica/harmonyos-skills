---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-third-party-faq
title: 三方支付问题处理
breadcrumb: 指南 > 应用服务 > Payment Kit（鸿蒙支付服务） > 通用收银台接入 > 拉起三方支付收银台 > 三方支付问题处理
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:10+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:80de0c01fedd4be5f806a50845138254d5ade3f50f1f01e530a873ccd15a7948
---

## 接入微信H5 支付，支付完成后会停留在微信里面，没有自动返回应用，需要用户手动返回？

支付完成需回调页面可参见[这里](https://pay.weixin.qq.com/doc/v2/merchant/4011936869)。

目前deeplink拉起微信支付，微信支付现状支付成功后停留在微信支付界面，无法返回应用，当前无解决方案。可通过[基于接口拉起方式](payment-launch-third-party-payment-sdk.md)拉起三方支付收银台，可以支持微信支付支付成功后自动关闭。
