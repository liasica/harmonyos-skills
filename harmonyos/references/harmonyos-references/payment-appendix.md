---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-appendix
title: 附录
breadcrumb: API参考 > 应用服务 > Payment Kit（鸿蒙支付服务） > 附录
category: harmonyos-references
scraped_at: 2026-04-28T08:18:18+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:24f5d795f274f5c5c5f3b8a4f5b041d2db94e1bf6e53d6b0a5df5121f9074da3
---

## 获取对应的UTC过期时间示例

```
1. /**
2. * 获取UTC格式的过期时间
3. * @param expectedExpiredTime 交易过期时间，请换算为分钟
4. * @return UTC时间
5. */
6. private static String getTradeExpireTime(int expectedExpiredTime) {
7. SimpleDateFormat formater = new SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ss.SSSZ");
8. formater.setTimeZone(TimeZone.getTimeZone("UTC"));
9. Calendar calendar = Calendar.getInstance();
10. calendar.set(Calendar.MINUTE, calendar.get(Calendar.MINUTE) + expectedExpiredTime);
11. return formater.format(calendar.getTime());
12. }
```
