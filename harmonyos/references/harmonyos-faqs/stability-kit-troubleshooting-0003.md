---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/stability-kit-troubleshooting-0003
title: NFC提示弹窗无法关闭
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > 故障排查 > NFC提示弹窗无法关闭
category: harmonyos-faqs
scraped_at: 2026-10-15T07:13:29+08:00
doc_updated_at: 2026-10-14
content_hash: sha256:449662d40bd077a3834534d555f4a64dd7154e3a2df0f8978a680668b21ab52c
---

## 问题现象

应用界面弹窗提示需要关闭NFC功能，点击按钮跳转到NFC设置页关闭NFC，返回后应用弹窗未消失，弹窗无法关闭。

## 定位过程

1. 查看hilog日志，搜索关键字Register event，从日志Register event: nfcStateChange可知，在15:25:47.021时应用已经注册了NFC开关状态事件，并且由nfc state: 3可知NFC是打开状态。

   ```txt
   07-07 15:25:47.019   52975-52975    I  [nfc_controller.cpp(InitNfcRemoteSA:83)]InitNfcRemoteSA:add remote death listener
   07-07 15:25:47.020   52975-52975    I  [nfc_basic_proxy.cpp(SendRequestExpectReplyInt:71)]SendRequestExpectReplyInt, cmd 101, ret 0, reply 3
   07-07 15:25:47.020   52975-52975    I  [nfc_controller.cpp(GetNfcState:155)]nfc state: 3.
   07-07 15:25:47.021   52975-52975    I  [nfc_napi_controller_event.cpp(Init:432)]SubscribeSystemAbility, systemAbilityId = 1140, ret = 0
   07-07 15:25:47.021   52975-52975    I  [nfc_napi_controller_event.cpp(Register:277)]Register event: nfcStateChange
   07-07 15:25:47.021   52975-52975    I  [nfc_controller.cpp(RegListener:176)]NfcController::RegListener
   ```
2. 搜索关键字Click accepted，在15:31:11.045点击了关闭按钮。

   ```txt
   07-07 15:31:11.045   52975-52975   I  [(1000000:1000000:scope)] Click try accept
   07-07 15:31:11.045   52975-52975   I  [(1000000:1000000:scope)] Click accepted, tag: Column
   ```
3. 搜索关键字Unregister event，从日志Unregister event: nfcStateChange可知，在点击按钮后，应用在15:31:11.100已经取消NFC状态的监听。

   ```txt
   07-07 15:31:11.100   52975-52975    I  当前页面index离开 0
   07-07 15:31:11.100   52975-52975    I  [nfc_napi_controller_event.cpp(Unregister:377)]Unregister event: nfcStateChange
   07-07 15:31:11.100   52975-52975    I  [nfc_napi_controller_event.cpp(Unregister:394)]All callback is unsubscribe for event: nfcStateChange
   07-07 15:31:11.100   52975-52975    I  [nfc_napi_controller_event.cpp(DeleteAllRegisterObj:363)]delete all ref, m_regEnv: <private>, m_regHanderRef: <private>, refCount: 0
   07-07 15:31:11.100   52975-52975    I  [nfc_controller.cpp(UnregListener:192)]NfcController::UnregListener
   ```
4. 由于在点击按钮后已经取消了NFC状态的监听，此时应用无法感知NFC状态的变化，导致关闭了NFC后，回到原来的页面NFC提示弹窗依旧没有消失。

## 分析结论

提前取消NFC状态监听，导致NFC提示弹窗无法关闭，页面卡死。

## 修改建议

取消NFC状态监听时，需确保当前页面后续不再使用nfcController接口，建议将[nfcController.off('nfcStateChange')](../harmonyos-references/js-apis-nfccontroller.md#nfccontrolleroffnfcstatechange)的执行移动到[aboutToDisappear](../harmonyos-references/ts-custom-component-lifecycle.md#abouttodisappear)生命周期回调函数中，并及时关闭NFC提示弹窗。
