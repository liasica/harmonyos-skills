---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/net-eap
title: 扩展认证
breadcrumb: 指南 > 系统 > 网络 > Network Kit（网络服务） > 管理网络 > 扩展认证
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:54+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f97645864120a555ee2fd1f98ab593dda860a80336e4a01f041a15936a029886
---

## 简介

部分企业用户的PC网络接入认证使用802.1X认证方式，认证客户端由第三方厂商提供。

说明

扩展认证能力从API version 20开始支持。

认证客户端有以下定制行为：

1. 在EAP协议报文内封装私有数据，该私有数据遵循客户端与认证服务器约定的数据结构。
2. 在认证过程中，客户端在本地进行安检扫描等定制动作，定制动作结束后，客户端向接入设备回复认证消息。

   在这种机制下，需要操作系统提供三方客户端介入802.1X认证流程的机制，支撑客户端的定制认证。

为满足以上需求场景，定制化802.1X认证提供如下功能：

1. 定制化监听与修改802.1X报文交互流程的能力。
2. 对eth网口发起802.1X认证和去认证的能力。

## 场景介绍

定制化802.1X认证流程的典型场景如下：

1. 企业网管应用，需要在企业Wi-Fi的802.1X认证流程中加入自定义的安全校验，来接入企业内网。

   * 支持指定要进行定制化处理的报文类型和EAP类型。
   * 支持根据自定义的安全校验结果来指定标准认证流程的结果。
2. 企业网管应用，需要支持使用eth网口进行802.1X安全认证流程来接入企业内网。

   * 支持标准802.1X认证流程。
   * 支持定制化802.1X认证流程。

具体开发方式介绍如下。

## 802.1X认证流程中加入自定义的安全校验

1. 从@kit.NetworkKit中导入eap命名空间。

   ```
   1. import { eap } from '@kit.NetworkKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```

   [AccreditationProcess.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_NetManager/NetEap_case/entry/src/main/ets/pages/AccreditationProcess.ets#L15-L18)
2. 调用[regCustomEapHandler](../harmonyos-references/js-apis-net-eap.md#eapregcustomeaphandler)方法，注册所需监听的EAP报文类型。

   在802.1X认证过程中，系统会将符合条件的EAP报文传递至callback函数（如示例代码中的eapData函数）中，供企业应用获取。报文传递至callback函数后，802.1X认证流程会阻塞等待，用户能够获取到完整的报文内容。

   （1）若注册的是由服务器发送给客户端的报文类型（即eapCode=1），则此时可以从报文中看到由服务器加入的自定义内容。应用根据自定义内容，判断认证是否应该继续往后续步骤进行，并调用[replyCustomEapData](../harmonyos-references/js-apis-net-eap.md#eapreplycustomeapdata)方法通知系统。

   （2）若注册的报文类型是由客户端发给服务器的（即eapCode=2），则此时获取到的是原始的802.1X认证报文，应用需要在原始报文内容中加入自己的自定义内容，并将加入自定义内容后的报文内容调用[replyCustomEapData](../harmonyos-references/js-apis-net-eap.md#eapreplycustomeapdata)方法通知系统。

   （3）若注册的报文类型是服务器返回的成功（即eapCode=3）或失败（即eapCode=4）的结果，客户端可在接收到此结果之后做定制处理。

   以下注册服务器发送给客户端的报文类型（即eapCode=1，eapType=25）为例，若需注册其他类型，修改eapCode值后再调用[regCustomEapHandler](../harmonyos-references/js-apis-net-eap.md#eapregcustomeaphandler)方法即可。

   ```
   1. let netType = 1;
   2. let eapCode= 1; // eap request
   3. let eapType= 25; // EAP_PEAP
   4. let result = 1;

   6. let eapData = (eapData:eap.EapData):void => {
   7. hilog.info(0x0000, 'testTag', 'rsp result',JSON.stringify(eapData));
   8. const newBuffer = new Uint8Array(eapData.bufferLen);
   9. newBuffer.set(eapData.eapBuffer, 0);
   10. let eapData2: eap.EapData = {
   11. msgId: eapData.msgId,
   12. eapBuffer: newBuffer,
   13. bufferLen: newBuffer.length
   14. }
   15. try{
   16. eap.replyCustomEapData(result, eapData2);
   17. hilog.info(0x0000, 'testTag', 'replyCustomEapData success');
   18. } catch (err) {
   19. hilog.error(0x0000, 'testTag', 'errCode: ' + err.code + ' , errMessage: ' + err.message);
   20. }
   21. }
   22. function serverReplyCustomEapData() {
   23. try{
   24. eap.regCustomEapHandler(netType, eapCode, eapType, eapData);
   25. hilog.info(0x0000, 'testTag', 'regCustomEapHandler success');
   26. // ...
   27. } catch (err) {
   28. hilog.error(0x0000, 'testTag', 'errCode: ' + err.code + 'errMessage: ' + err.message);
   29. // ...
   30. }
   31. }
   ```

   [AccreditationProcess.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_NetManager/NetEap_case/entry/src/main/ets/pages/AccreditationProcess.ets#L26-L74)
3. 若需取消定制化，可调用[unregCustomEapHandler](../harmonyos-references/js-apis-net-eap.md#eapunregcustomeaphandler)方法。

   ```
   1. let netType = 1;
   2. let eapCode= 1; // eap request
   3. let eapType= 25; // EAP_PEAP
   4. let result = 1;

   6. let eapData = (eapData:eap.EapData):void => {
   7. hilog.info(0x0000, 'testTag', 'rsp result',JSON.stringify(eapData));
   8. const newBuffer = new Uint8Array(eapData.bufferLen);
   9. newBuffer.set(eapData.eapBuffer, 0);
   10. let eapData2: eap.EapData = {
   11. msgId: eapData.msgId,
   12. eapBuffer: newBuffer,
   13. bufferLen: newBuffer.length
   14. }
   15. // ...
   16. }
   17. // ...
   18. try {
   19. eap.unregCustomEapHandler(netType, eapCode, eapType, eapData);
   20. hilog.info(0x0000, 'testTag', 'unregCustomEapHandler success');
   21. // ...
   22. } catch (err) {
   23. hilog.error(0x0000, 'testTag', 'errCode: ' + err.code + ', errMessage: ' + err.message);
   24. // ...
   25. }
   ```

   [AccreditationProcess.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_NetManager/NetEap_case/entry/src/main/ets/pages/AccreditationProcess.ets#L27-L98)

## 使用eth接口发起802.1X认证流程

1. 设备通过硬件接口，插入网线。
2. 从@kit.NetworkKit中导入eap命名空间。

   ```
   1. import { eap } from '@kit.NetworkKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```

   [EthInterface.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_NetManager/NetEap_case/entry/src/main/ets/pages/EthInterface.ets#L15-L18)
3. 当企业管理软件需要进行认证，调用[startEthEap](../harmonyos-references/js-apis-net-eap.md#eapstartetheap)方法时，会发起802.1X认证流程。

   ```
   1. const netId: number = 100;
   2. // ...
   3. let profile: eap.EthEapProfile = {
   4. eapMethod: eap.EapMethod.EAP_TTLS,
   5. phase2Method: eap.Phase2Method.PHASE2_AKA_PRIME,
   6. identity: 'identity',
   7. anonymousIdentity: 'anonymousIdentity',
   8. password: 'password',
   9. caCertAliases: 'caCertAliases',
   10. caPath: 'caPath',
   11. clientCertAliases: 'clientCertAliases',
   12. certEntry: new Uint8Array([5,6,7,8,9,10]),
   13. certPassword: 'certPassword',
   14. altSubjectMatch: 'altSubjectMatch',
   15. domainSuffixMatch: 'domainSuffixMatch',
   16. realm: 'realm',
   17. plmn: 'plmn',
   18. eapSubId: 1
   19. };

   21. try {
   22. eap.startEthEap(netId, profile);
   23. hilog.info(0x0000, 'testTag', 'startEthEap success');
   24. // ...
   25. } catch (err) {
   26. // ...
   27. hilog.error(0x0000, 'testTag', 'errCode: ' + err.code + ', errMessage: ' + err.message);
   28. }
   ```

   [EthInterface.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_NetManager/NetEap_case/entry/src/main/ets/pages/EthInterface.ets#L27-L71)
4. 当企业管理软件需要退出认证状态，调用[logOffEthEap](../harmonyos-references/js-apis-net-eap.md#eaplogoffetheap)方法，即会发起802.1X取消认证流程。

   ```
   1. const netId: number = 100;
   2. // ...
   3. try{
   4. eap.logOffEthEap(netId);
   5. hilog.error(0x0000, 'testTag', 'logOffEthEap success');
   6. // ...
   7. } catch (err) {
   8. // ...
   9. hilog.error(0x0000, 'testTag', 'errCode: ' + err.code + ', errMessage: ' + err.message);
   10. }
   ```

   [EthInterface.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_NetManager/NetEap_case/entry/src/main/ets/pages/EthInterface.ets#L26-L96)
