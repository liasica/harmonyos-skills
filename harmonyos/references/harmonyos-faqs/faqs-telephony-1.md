---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-telephony-1
title: 如何判断蜂窝信号强度
breadcrumb: FAQ > 系统开发 > 网络 > 蜂窝通信（Telephony） > 如何判断蜂窝信号强度
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:19+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:46aa039c93259349d1fd688fb1691f96f3267277d89e36af7b2d1ff648c9614f
---

可以通过radio.getSignalInformation()接口获取蜂窝信号强度，具体步骤如下：

1. 导入相应的模块。
2. 调用getSignalInformation()方法，返回SignalInformation列表。
3. 遍历SignalInformation数组，根据不同的signalType获取相应制式的信号强度。
4. （可选）订阅蜂窝网络信号变化。

参考代码如下：

```
1. import { radio, observer } from '@kit.TelephonyKit';

3. // Taking obtaining the signal strength of card 1 as an example
4. let slotId: number = 0;
5. radio.getSignalInformation(slotId, (err, data) => {
6. if (!err) {
7. console.log("get signal information success.");
8. // Traverse the array and output the signal strength under different network standards
9. for (let j = 0; j < data.length; j++) {
10. console.log("type:" + data[j].signalType + ", level:" + data[j].signalLevel);
11. }
12. } else {
13. console.error("get signal information fail, err is:" + JSON.stringify(err));
14. }
15. });

17. // Subscription to cellular network signal changes (optional)
18. observer.on("signalInfoChange", (data) => {
19. console.log("signal info change, data is:" + JSON.stringify(data));
20. });
```

[GetSignal.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/TelephonyKit/entry/src/main/ets/pages/GetSignal.ets#L21-L41)

**参考链接**

[getSignalInformation](../harmonyos-references/js-apis-radio.md#radiogetsignalinformation7)
