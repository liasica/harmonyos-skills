---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-telephony-1
title: 如何判断蜂窝信号强度
breadcrumb: FAQ > 系统开发 > 网络 > 蜂窝通信（Telephony） > 如何判断蜂窝信号强度
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:38+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:c93ba893dbadd55c6b095e9dde046c4249295ea41a0f0dbdd318b3c6b6aaaf29
---

可以通过radio.getSignalInformation()接口获取蜂窝信号强度，具体步骤如下：

1. 导入相应的模块。
2. 调用getSignalInformation()方法，返回SignalInformation列表。
3. 遍历SignalInformation数组，根据不同的signalType获取相应制式的信号强度。
4. （可选）订阅蜂窝网络信号变化。

参考代码如下：

```typescript
import { radio, observer } from '@kit.TelephonyKit';

// Taking obtaining the signal strength of card 1 as an example
let slotId: number = 0;
radio.getSignalInformation(slotId, (err, data) => {
  if (!err) {
    console.log("get signal information success.");
    // Traverse the array and output the signal strength under different network standards
    for (let j = 0; j < data.length; j++) {
      console.log("type:" + data[j].signalType + ", level:" + data[j].signalLevel);
    }
  } else {
    console.error("get signal information fail, err is:" + JSON.stringify(err));
  }
});

// Subscription to cellular network signal changes (optional)
observer.on("signalInfoChange", (data) => {
  console.log("signal info change, data is:" + JSON.stringify(data));
});
```

**参考链接**

[getSignalInformation](../harmonyos-references/js-apis-radio.md#radiogetsignalinformation7)
