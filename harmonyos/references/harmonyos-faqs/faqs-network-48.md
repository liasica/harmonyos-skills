---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-48
title: 如何实现http长连接
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > 如何实现http长连接
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:12+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:59a868a03abf094a4755cf6aa39d18da858d2c3a5c48b6f81aea29690742dca8
---

可使用定时HTTP请求模拟长连接。参考代码如下：

```
1. import { http } from '@kit.NetworkKit';

3. let httpRequest = http.createHttp();
4. // 设置5秒轮询一次
5. setTimeout(() => {
6. httpRequest.request("EXAMPLE_URL", {
7. method: http.RequestMethod.GET,
8. connectTimeout: 60000,
9. readTimeout: 60000
10. }, (err, data) => {
11. if (!err) {
12. console.info('Received data:', JSON.stringify(data.result));
13. } else {
14. console.info('Polling error:', JSON.stringify(err));
15. }
16. })
17. }, 5000)
```

[SetLongConnect.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/NetworkKit/entry/src/main/ets/pages/SetLongConnect.ets#L21-L37)
