---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-appendix
title: 附录
breadcrumb: API参考 > 应用服务 > Payment Kit（鸿蒙支付服务） > 附录
category: harmonyos-references
scraped_at: 2026-09-02T14:53:29+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:fbc662eb8acc788cd930bb15b88c0079863629bec0b58d97131fd5ed9f5bb6e1
---

## 获取对应的UTC过期时间示例

```java
/**
* 获取UTC格式的过期时间
* @param expectedExpiredTime 交易过期时间，请换算为分钟
* @return UTC时间
*/
private static String getTradeExpireTime(int expectedExpiredTime) {
     SimpleDateFormat formater = new SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ss.SSSZ");
     formater.setTimeZone(TimeZone.getTimeZone("UTC"));
     Calendar calendar = Calendar.getInstance();
     calendar.set(Calendar.MINUTE, calendar.get(Calendar.MINUTE) + expectedExpiredTime);
     return formater.format(calendar.getTime());
 }
```
