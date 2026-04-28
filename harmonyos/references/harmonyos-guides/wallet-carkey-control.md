---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-carkey-control
title: 车控
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 数字车钥匙 > 车控
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:08+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c858dd594c6d4464c5e6b025e2d19f1a4fe08655b39f56b0b8b35ba7f9e84e95
---

数字车钥匙开通完成后，车主APP可以通过车控指令远程控制车辆的开门等操作。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/oMkKOKnPRfi-5G_6UPQKqw/zh-cn_image_0000002583439249.png?HW-CC-KV=V1&HW-CC-Date=20260427T235107Z&HW-CC-Expire=86400&HW-CC-Sign=218476E436793CA64094896B4186793B56CA5150B5B128985C63B538F67B9E7C)

典型的交互流程如下:

* 通过[queryICCEConnectionState](../harmonyos-references/wallet-walletpass.md#queryicceconnectionstate)接口检查车控蓝牙的连接状态，如果未连接则使用[startICCEConnection](../harmonyos-references/wallet-walletpass.md#starticceconnection)主动连接。
* 通过[registerICCEListener](../harmonyos-references/wallet-walletpass.md#registericcelistener)注册监听，接收华为钱包发送的消息。
* 车主APP可以通过[sendICCERKEMessage](../harmonyos-references/wallet-walletpass.md#sendiccerkemessage)接口发送车控指令。
* 用户退出数字钥匙车控页面，通过[unregisterICCEListener](../harmonyos-references/wallet-walletpass.md#unregistericcelistener)接口取消监听。

## 开发步骤

1. 车主APP使用[创建Wallet Kit服务](wallet-preparations.md)时注册的服务号和[申请钥匙卡片](../harmonyos-references/wallet-rest-api-carkey.md#申请钥匙卡片)时定义的卡券唯一标识，通过[queryICCEConnectionState](../harmonyos-references/wallet-walletpass.md#queryicceconnectionstate)判断车钥匙的蓝牙链路状态。

   ```
   1. import { common } from '@kit.AbilityKit';
   2. import { walletPass } from '@kit.WalletKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';

   5. @Entry
   6. @Component
   7. struct Index {
   8. private walletPassClient: walletPass.WalletPassClient = new walletPass.WalletPassClient(this.getUIContext().getHostContext() as common.UIAbilityContext);
   9. // 创建Wallet Kit服务时注册的服务号
   10. private passType: string = '';
   11. // 申请钥匙卡片时定义的卡券唯一标识
   12. private serialNumber: string = '';

   14. async queryICCEConnectionState() {
   15. let passStr = JSON.stringify({
   16. passType: this.passType,
   17. serialNumber: this.serialNumber
   18. });
   19. this.walletPassClient.queryICCEConnectionState(passStr).then((result: string) => {
   20. console.info(`Succeeded in querying ICCEConnectionState, result: ${result}`);
   21. }).catch((err: BusinessError) => {
   22. console.error(`Failed to query ICCEConnectionState, code:${err.code}, message:${err.message}`);
   23. })
   24. }

   26. build() {
   27. // your application UI
   28. }
   29. }
   ```
2. 如果[queryICCEConnectionState](../harmonyos-references/wallet-walletpass.md#queryicceconnectionstate)接口返回连接状态connectionState为未配对0时，需要调用[startICCEConnection](../harmonyos-references/wallet-walletpass.md#starticceconnection)主动创建蓝牙链接。

   ```
   1. import { common } from '@kit.AbilityKit';
   2. import { walletPass } from '@kit.WalletKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';

   5. @Entry
   6. @Component
   7. struct Index {
   8. private walletPassClient: walletPass.WalletPassClient = new walletPass.WalletPassClient(this.getUIContext().getHostContext() as common.UIAbilityContext);
   9. // 创建Wallet Kit服务时注册的服务号
   10. private passType: string = '';
   11. // 申请钥匙卡片时定义的卡券唯一标识
   12. private serialNumber: string = '';

   14. async startICCEConnection() {
   15. let passStr = JSON.stringify({
   16. passType: this.passType,
   17. serialNumber: this.serialNumber
   18. });
   19. this.walletPassClient.startICCEConnection(passStr).then((result: string) => {
   20. console.info(`Succeeded in starting ICCEConnection, result: ${result}`);
   21. }).catch((err: BusinessError) => {
   22. console.error(`Failed to start ICCEConnection, code:${err.code}, message:${err.message}`);
   23. })
   24. }

   26. build() {
   27. // your application UI
   28. }
   29. }
   ```
3. 车主APP通过[registerICCEListener](../harmonyos-references/wallet-walletpass.md#registericcelistener)注册监听华为钱包发送的消息。

   ```
   1. import { common } from '@kit.AbilityKit';
   2. import { walletPass } from '@kit.WalletKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   4. import { rpc } from '@kit.IPCKit';

   6. class ICCECallBack extends rpc.RemoteObject {
   7. constructor() {
   8. super('ICCECallBack');
   9. }

   11. async onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence, option: rpc.MessageOption): Promise<boolean> {
   12. // processing after receiving communication data
   13. let codeInt = data.readInt();
   14. return true;
   15. }
   16. }

   18. @Entry
   19. @Component
   20. struct Index {
   21. private walletPassClient: walletPass.WalletPassClient = new walletPass.WalletPassClient(this.getUIContext().getHostContext() as common.UIAbilityContext);
   22. private callback: rpc.RemoteObject | null = null;
   23. // 创建Wallet Kit服务时注册的服务号
   24. private passType: string = '';
   25. // 注册监听的应用名称，一般为包名
   26. private registerName: string = '';

   28. async registerICCEListener() {
   29. let passStr = JSON.stringify({
   30. passType: this.passType,
   31. registerName: this.registerName
   32. });
   33. this.callback = new ICCECallBack();
   34. this.walletPassClient.registerICCEListener(passStr, this.callback).then((result: string) => {
   35. console.info(`Succeeded in registering ICCEListener, result: ${result}`);
   36. }).catch((err: BusinessError) => {
   37. console.error(`Failed to register ICCEListener, code:${err.code}, message:${err.message}`);
   38. })
   39. }

   41. build() {
   42. // your application UI
   43. }
   44. }
   ```
4. 车主APP通过[sendICCERKEMessage](../harmonyos-references/wallet-walletpass.md#sendiccerkemessage)接口发送车控指令。

   ```
   1. import { common } from '@kit.AbilityKit';
   2. import { walletPass } from '@kit.WalletKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';

   5. @Entry
   6. @Component
   7. struct Index {
   8. private walletPassClient: walletPass.WalletPassClient = new walletPass.WalletPassClient(this.getUIContext().getHostContext() as common.UIAbilityContext);
   9. // 创建Wallet Kit服务时注册的服务号
   10. private passType: string = '';
   11. // 申请钥匙卡片时定义的卡券唯一标识
   12. private serialNumber: string = '';
   13. // 车控指令
   14. private rkeCommand: string = '';

   16. async sendICCERKEMessage() {
   17. let passStr = JSON.stringify({
   18. passType: this.passType,
   19. serialNumber: this.serialNumber,
   20. rkeCommand: this.rkeCommand,
   21. encryptFlag: '0',
   22. directionFlag: '1'
   23. });
   24. this.walletPassClient.sendICCERKEMessage(passStr).then((result: string) => {
   25. console.info(`Succeeded in sending ICCERKEMessage, result: ${result}`);
   26. }).catch((err: BusinessError) => {
   27. console.error(`Failed to send ICCERKEMessage, code:${err.code}, message:${err.message}`);
   28. })
   29. }

   31. build() {
   32. // your application UI
   33. }
   34. }
   ```
5. 用户退出数字钥匙车控页面，车主APP通过[unregisterICCEListener](../harmonyos-references/wallet-walletpass.md#unregistericcelistener)接口取消监听。

   ```
   1. import { common } from '@kit.AbilityKit';
   2. import { walletPass } from '@kit.WalletKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   4. import { rpc } from '@kit.IPCKit';

   6. @Entry
   7. @Component
   8. struct Index {
   9. private walletPassClient: walletPass.WalletPassClient = new walletPass.WalletPassClient(this.getUIContext().getHostContext() as common.UIAbilityContext);
   10. private callback: rpc.RemoteObject | null = null;
   11. // 创建Wallet Kit服务时注册的服务号
   12. private passType: string = '';
   13. // 注册监听的应用名称，一般为包名
   14. private registerName: string = '';

   16. async unregisterICCEListener() {
   17. let passStr = JSON.stringify({
   18. passType: this.passType,
   19. registerName: this.registerName
   20. });

   22. this.walletPassClient.unregisterICCEListener(passStr).then((result: string) => {
   23. console.info(`Succeeded in unregistering ICCEListener, result: ${result}`);
   24. this.callback = null;
   25. }).catch((err: BusinessError) => {
   26. console.error(`Failed to unregister ICCEListener, code:${err.code}, message:${err.message}`);
   27. })
   28. }

   30. build() {
   31. // your application UI
   32. }
   33. }
   ```
