---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/connectivity-kit-troubleshooting-0003
title: NFC服务执行Tag业务逻辑报错
breadcrumb: FAQ > 系统开发 > 网络 > 短距通信（Connectivity） > 故障排查 > NFC服务执行Tag业务逻辑报错
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:17+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:3bb919a47d2f2c9ceec15502780740a29c626104d4c31353c08fb628faec174f
---

## 问题现象

NFC服务在获取IsoDep类型的NFC Tag对象并与标签建立连接时报错。

报错信息如下：

```txt
Tag running state is abnormal in service
```

## 定位过程

该报错信息与该[错误码文档](../harmonyos-references/errorcode-nfc.md#section3100201-nfc服务读写tag错误)中的错误信息一致。因此可按照文档中给出的可能原因及处理步骤进行排查。

可能原因：

* Tag参数值和实际调用函数要求不匹配。
* Tag操作时，NFC状态是关闭的。
* Tag操作前，已经处在断开状态。
* Tag芯片返回错误状态或响应超时。
* 和NFC服务没有建立绑定关系，无法调用接口。

首先检查NFC参数是否和所调用接口匹配。在NFC服务读取到标签后，通过打印[TagInfo](../harmonyos-references/js-apis-nfctag.md#taginfo)中支持的[技术类型](../harmonyos-references/js-apis-nfctag.md#常量)，可判断当前标签支持的技术类型中没有ISO\_DEP。

## 分析结论

读取到的标签不支持IsoDep类型，由于Tag参数值和实际调用函数要求不匹配，所以当使用getIsoDep()方法并连接时会导致报错。

## 修改建议

1.当读取到NFC标签卡片后，通过该标签的TagInfo对象判断该标签是否支持IsoDep技术类型，以防止Tag参数值和后续实际调用的getIsoDep()函数要求不匹配，从而导致报错。具体判断逻辑代码可参考[NFC标签读写开发指南](../harmonyos-guides/nfc-tag-access-guide.md#开发步骤)中的示例代码。

2.更换为支持IsoDep技术类型的NFC标签卡片。
