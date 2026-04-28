---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-66
title: 无网络环境下使用同步方法获取网络状态报错
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > 无网络环境下使用同步方法获取网络状态报错
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:15+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:c67d8447b0a84b01c59f4fb3061119c40b326e88c919c7ef7b9678b66ba529b2
---

在无网环境中调用同步方法请求时，无法解析nethandle对应的内容，方法执行时会报错。可以使用try-catch语句捕获并处理报错信息。参考代码如下：

```
1. import { connection } from '@kit.NetworkKit'
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct GetErrInfo {
7. getErrInfo() {
8. try {
9. let netHandle = connection.getDefaultNetSync();
10. let connectionproperties = connection.getConnectionPropertiesSync(netHandle);
11. } catch (err) {
12. let error: BusinessError = err as BusinessError;
13. console.log('error: ' + JSON.stringify(error));
14. }
15. }

17. build() {
18. Row() {
19. Column() {
20. Button('获取网络类型')
21. .onClick(() => {
22. this.getErrInfo();

24. })
25. }
26. .width('100%')
27. }
28. .height('100%')
29. }
30. }
```

[GetNetErr.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/NetworkKit/entry/src/main/ets/pages/GetNetErr.ets#L21-L50)
