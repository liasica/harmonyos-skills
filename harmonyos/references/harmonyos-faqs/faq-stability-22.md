---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-22
title: NFC提示弹窗无法关闭
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > NFC提示弹窗无法关闭
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:49+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:d272f9b4b5ec0a7e917637aecf7e97002b69c4f59893e8ec7f116e94fba8fcdb
---

## 问题现象

应用界面弹窗提示需要关闭NFC功能，点击按钮跳转到NFC设置页关闭NFC，返回后应用弹窗未消失，弹窗无法关闭。

## 背景知识

* 近场通信(Near Field Communication，[NFC](../harmonyos-guides/nfc.md))：一种短距高频的无线电技术，在13.56MHz频率运行，通信距离一般在10厘米距离内。电子设备可以通过NFC通信技术和NFC标签通信，从标签中读取数据，或写入数据到标签。
* [@ohos.nfc.controller (标准NFC)](../harmonyos-references/js-apis-nfccontroller.md)：主要用于管理NFC状态，包括打开和关闭NFC，读取NFC的状态等。
* [nfcController.on('nfcStateChange')](../harmonyos-references/js-apis-nfccontroller.md#nfccontrolleronnfcstatechange)：注册NFC开关状态事件，通过Callback方式获取NFC状态的变化通知。
* [nfcController.off('nfcStateChange')](../harmonyos-references/js-apis-nfccontroller.md#nfccontrolleroffnfcstatechange)：取消NFC开关状态事件的注册，取消后NFC状态变化时，就不会再收到Callback的通知。

## 问题定位

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
