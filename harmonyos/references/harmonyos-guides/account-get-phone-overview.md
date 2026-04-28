---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-get-phone-overview
title: 概述
breadcrumb: 指南 > 应用服务 > Account Kit（华为账号服务） > 获取华为账号用户信息 > 获取手机号 > 概述
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:00+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:edd64359e1ff20a2043e79ecdcbe95f21e7074a845f1d0e64fade7ba068e8d4c
---

当应用需要获取用户手机号时，可使用Account Kit提供的手机号授权能力，引导用户完成手机号授权。

注意

在应用账号已登录并绑定用户华为账号UnionID的情况下，应用可以在获取手机号等用户信息时根据实际业务场景判断是否需要提前校验当前应用账号绑定的UnionID与系统账号当前的UnionID是否一致。

Account Kit提供了快速验证方式：

| 场景 | 说明 |
| --- | --- |
| [快速验证](account-get-phonenumber.md) | 对用户选择的华为账号绑定的手机号或者新增的手机号进行验证，**不保证是实时验证**，**仅首次需要用户授权**。 |

## 约束与限制

1. 应用满足《[常见类型移动互联网应用程序必要个人信息范围规定](http://www.cac.gov.cn/2021-03/22/c_1617990997054277.htm)》（对第三方网站的内容，华为不承担任何责任）中使用手机号的必要业务场景。
2. 儿童账号无法通过快速验证获取到手机号。
3. 获取手机号能力支持Phone、Tablet、PC/2in1设备。并且从5.1.0(18)版本开始，新增支持Wearable设备；从5.1.1(19)版本开始，新增支持TV设备。
