---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/telephony-call
title: 拨打电话
breadcrumb: 指南 > 系统 > 网络 > Telephony Kit（蜂窝通信服务） > 拨打电话
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:13+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:118ee4296673b26275c5ef502d54d2eb73664b8d2552929c7441f8e52f229bd6
---

## 场景介绍

开发者可以通过以下方式实现拨打电话的功能：

* 对于三方应用，开发者可以使用makeCall接口，拉起系统电话应用，用户可以自行呼出通话。

## 基本概念

* 通话状态码

  将当前的通话状态上报给app，可以根据当前的通话状态去做一些逻辑处理。例如在当前没有正在进行呼叫的时候，可以正常拨打新的一通电话。

  | 名称 | 值 | 说明 |
  | --- | --- | --- |
  | CALL\_STATE\_UNKNOWN | -1 | 无效状态，当获取呼叫状态失败时返回。 |
  | CALL\_STATE\_IDLE | 0 | 表示没有正在进行的呼叫。 |
  | CALL\_STATE\_RINGING | 1 | 表示来电正在振铃或等待。 |
  | CALL\_STATE\_OFFHOOK | 2 | 表示至少有一个呼叫处于拨号、通话中或呼叫保持状态，并且没有新的来电振铃或等待。 |

## 约束与限制

1. 仅支持在标准系统上运行。
2. 设备需插入可用的SIM卡。

## 接口说明

说明

为了保证应用的运行效率，大部分API调用都是异步的，对于异步调用的API均提供了callback和Promise两种方式，以下示例均采用callback函数，更多方式可以查阅[API参考](../harmonyos-references/js-apis-call.md)。

| 接口名 | 描述 |
| --- | --- |
| hasVoiceCapability(): boolean; | 判断是否具有语音功能，默认false。  -true：是  -false：否 |
| makeCall(phoneNumber: string, callback: AsyncCallback<void>): void; | 转到拨号屏幕，显示被叫号码。 |

observer模块为开发者提供订阅和取消订阅通话业务状态的功能。具体API说明详见[接口文档](../harmonyos-references/js-apis-observer.md)。

| 接口名 | 描述 |
| --- | --- |
| on(type: 'callStateChange', options: { slotId: number }, callback: Callback<{ state: CallState, number: string }>): void; | 监听通话状态变化。 |

## 开发步骤

### 使用makeCall拨打电话

1. 导入call和observer模块。
2. 调用hasVoiceCapability，确认当前设备是否支持拨号。
3. 调用makeCall接口，跳转到拨号界面并显示待拨号的号码。
4. （可选）订阅通话业务状态变化。

   ```
   1. // import需要的模块
   2. import { call, observer } from '@kit.TelephonyKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';

   5. // 调用查询能力接口
   6. let isSupport = call.hasVoiceCapability();
   7. if (isSupport) {
   8. // 如果设备支持呼叫能力，则继续跳转到拨号界面，并显示拨号的号码
   9. // 从API15开始支持tel格式电话号码，如："tel:13xxxx"
   10. call.makeCall("13xxxx", (err: BusinessError) => {
   11. if (!err) {
   12. console.info("make call success.");
   13. } else {
   14. console.error("make call fail, err is:" + JSON.stringify(err));
   15. }
   16. });
   17. // 订阅通话业务状态变化（可选）
   18. class SlotId {slotId: number = 0}
   19. class CallStateCallback {
   20. state: call.CallState = call.CallState.CALL_STATE_UNKNOWN;
   21. number: string = "";
   22. }
   23. let slotId: SlotId = {slotId: 0}
   24. observer.on("callStateChange", slotId, (data: CallStateCallback) => {
   25. console.info("call state change, data is:" + JSON.stringify(data));
   26. });
   27. }
   ```
