---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-remote-communication-1
title: rcp模块发起请求时如何设置超时时间
breadcrumb: FAQ > 系统开发 > 网络 > 远场通信（Remote Communication） > rcp模块发起请求时如何设置超时时间
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:17+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:8e9c090a072d48d6266fd2a1e9904b2643fc2470febea346fedf3ffa4a06bf91
---

rcp模块发起请求如需要设置超时时间，可在建立session会话前设置SessionConfiguration内有关参数。

相关示例如下：

```
1. import { rcp } from '@kit.RemoteCommunicationKit';

3. const sessionConfig: rcp.SessionConfiguration = {
4. // Used to specify the configuration of HTTP requests associated with the session
5. requestConfiguration: {
6. transfer: {
7. // Timeout parameter setting
8. timeout: {
9. // The connection has timed out. The default value is 60,000
10. connectMs: 5000,
11. // Transmission timeout, with the default value being 60,000
12. transferMs: 10000,
13. },
14. }
15. }
16. };
17. const session = rcp.createSession(sessionConfig);

19. @Entry
20. @Component
21. export struct SetTimeout {
22. build() {
23. Row() {
24. Column() {
25. Button($r('app.string.timeout_parameter_setting'))
26. .onClick(() => {
27. if (session) {
28. console.log('Created session successful!')
29. console.log('Connection timeout parameter settings:',
30. sessionConfig.requestConfiguration?.transfer?.timeout?.connectMs);
31. console.log('Transmission timeout parameters settings:',
32. sessionConfig.requestConfiguration?.transfer?.timeout?.transferMs);
33. } else {
34. console.log('Created session failure!');
35. }
36. })
37. }
38. .width('100%')
39. }
40. .height('100%')
41. }
42. }
```

[RcpConfig.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/RemoteCommunication/entry/src/main/ets/pages/RcpConfig.ets#L21-L64)
