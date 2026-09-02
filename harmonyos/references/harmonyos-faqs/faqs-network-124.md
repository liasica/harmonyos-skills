---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-124
title: 解决调用mdns.removeLocalService移除mdns服务报错401问题
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > 解决调用mdns.removeLocalService移除mdns服务报错401问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:37+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:1a307ae1ab705729af8a769f643863d37ddb32f729b42972a6cfbecf8f59560a
---

## 问题现象

应用中添加mdns服务之后，退出后台重新运行App，此时期望删除上次发布的serviceName时，抛出异常:code:401, name:undefined, message:Parameter error，如何解决？

## 背景知识

[mdns管理](../harmonyos-references/js-apis-net-mdns.md)：通过对本地服务的创建，删除和解析等管理本地服务，并对指定类型的本地服务状态变化进行监听。

## 问题定位

1. 使用[mdns.addLocalService](../harmonyos-references/js-apis-net-mdns.md#mdnsaddlocalservice)成功添加一条mdns服务，然后应用退出后台。重新打开应用，启动搜索mdns服务后，在'serviceFound'回调中可以发现此前添加的服务。
2. 再调用[mdns.removeLocalService](../harmonyos-references/js-apis-net-mdns.md#mdnsremovelocalservice)移除该服务时报错code:401, message:Parameter error。
3. 添加服务后如果不杀掉进程，直接移除是可以的。

## 分析结论

mdns.removeLocalService只能移除注册过的服务，不能移除搜索到的服务。强行杀掉应用后不是之前注册的服务，因此移除会报错。

## 修改建议

调用mdns.removeLocalService接口移除服务需要保持注册的应用始终存在，即要保持应用存活，不能强行销毁应用。可以在UIAbility销毁时或者在组件销毁时，调用removeLocalService主动注销服务。
