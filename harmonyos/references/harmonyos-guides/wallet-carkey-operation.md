---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-carkey-operation
title: 钥匙开通
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 数字车钥匙 > 钥匙开通
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:09+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b94c2e4021bc8f85346b2148382f2fda0303c589a75f0e92d56341345c1ce6cd
---

钥匙开通分为添加钥匙和激活钥匙两步，整体交互流程图如下。相关接口定义请参照[钱包服务API](../harmonyos-references/wallet-walletpass.md)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/EndADaG3QP2qmvD0pl-Oeg/zh-cn_image_0000002583479199.png?HW-CC-KV=V1&HW-CC-Date=20260427T235107Z&HW-CC-Expire=86400&HW-CC-Sign=58D329FC6FC95660785FCFBEAD41CBA5D1BDFFEA3F2124A3F863901872FD3C7A)

1. 车主APP调用[queryPass](../harmonyos-references/wallet-walletpass.md#querypass)接口检查当前设备车钥匙的开通情况。
2. 如果[queryPass](../harmonyos-references/wallet-walletpass.md#querypass)接口返回[1010220501 查询卡券不存在](../harmonyos-references/wallet-error-code.md#section1010220501-查询卡券不存在)，则调用[canAddPass](../harmonyos-references/wallet-walletpass.md#canaddpass)接口检查当前设备是否支持添加车钥匙。
3. 如果[queryPass](../harmonyos-references/wallet-walletpass.md#querypass)接口或是[canAddPass](../harmonyos-references/wallet-walletpass.md#canaddpass)接口返回[1010200003 访问钱包的前置环境没有准备好](../harmonyos-references/wallet-error-code.md#section1010200003-访问钱包的前置环境没有准备好)，则调用[initWalletEnvironment](../harmonyos-references/wallet-walletpass.md#initwalletenvironment)接口初始化钱包开通车钥匙的同意协议或是登录账号等必要条件，引导用户跳转钱包App完成应用初始化。
4. 车主APP调用[queryPassDeviceInfo](../harmonyos-references/wallet-walletpass.md#querypassdeviceinfo)接口查询设备类型，指定目标设备标识，提升安全性。
5. 车主服务器预置模板后申请钥匙卡片以及JWE数据，参考[车主服务器开发](wallet-carkey-operation.md#车主服务器开发)。
6. 用户主动发起开卡时，车主APP跳转钱包应用，调用[addPass](../harmonyos-references/wallet-walletpass.md#addpass)接口携带上述流程中生成的编码后的JWE数据，开通车钥匙到钱包。
7. 卡片激活的过程中钱包服务器需要和DK业务管理服务进行交互的包括：设备的认证（和车钥匙管理台交换证书信息）、获取请求个人化数据时的token（用于向车钥匙管理台请求Applet个人化数据）、以及最后的请求Applet个人化数据，最后写入安全芯片，参考[车主服务器激活卡片](wallet-carkey-operation.md#车主服务器激活卡片)。
8. 车主APP可通过[viewPass](../harmonyos-references/wallet-walletpass.md#viewpass)接口跳转钱包查看已开通的车钥匙详情页。

## 开发步骤

1. 车主APP使用[创建Wallet Kit服务](wallet-preparations.md)时注册的服务号和[申请钥匙卡片](../harmonyos-references/wallet-rest-api-carkey.md#申请钥匙卡片)时定义的卡券唯一标识，车主APP调用[queryPass](../harmonyos-references/wallet-walletpass.md#querypass)接口检查当前设备车钥匙的开通情况。

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

   14. async queryPass() {
   15. let passStr = JSON.stringify({
   16. passType: this.passType,
   17. serialNumber: this.serialNumber
   18. });
   19. this.walletPassClient.queryPass(passStr).then((result: string) => {
   20. console.info(`Succeeded in querying pass, result: ${result}`);
   21. }).catch((err: BusinessError) => {
   22. console.error(`Failed to query pass, code:${err.code}, message:${err.message}`);
   23. })
   24. }

   26. build() {
   27. // your application UI
   28. }
   29. }
   ```
2. 如果[queryPass](../harmonyos-references/wallet-walletpass.md#querypass)接口返回[1010220501 查询卡券不存在](../harmonyos-references/wallet-error-code.md#section1010220501-查询卡券不存在)，则调用[canAddPass](../harmonyos-references/wallet-walletpass.md#canaddpass)接口检查当前设备是否支持添加车钥匙。

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
   11. // 目标设备类型 phone: 手机
   12. private targetDeviceType: string = '';

   14. async canAddPass() {
   15. let passStr = JSON.stringify({
   16. passType: this.passType,
   17. targetDeviceType: this.targetDeviceType
   18. });
   19. this.walletPassClient.canAddPass(passStr).then((result: string) => {
   20. console.info(`Succeeded in checking addPass, result:${result}`);
   21. }).catch((err: BusinessError) => {
   22. console.error(`Failed to check addPass, code:${err.code}, message:${err.message}`);
   23. })
   24. }

   26. build() {
   27. // your application UI
   28. }
   29. }
   ```
3. 如果[queryPass](../harmonyos-references/wallet-walletpass.md#querypass)接口或是[canAddPass](../harmonyos-references/wallet-walletpass.md#canaddpass)接口返回[1010200003 访问钱包的前置环境没有准备好](../harmonyos-references/wallet-error-code.md#section1010200003-访问钱包的前置环境没有准备好)，则调用[initWalletEnvironment](../harmonyos-references/wallet-walletpass.md#initwalletenvironment)接口初始化钱包开通车钥匙的同意协议或是登录账号等必要条件，引导用户跳转钱包App完成应用初始化。

   ```
   1. import { common } from '@kit.AbilityKit';
   2. import { walletPass } from '@kit.WalletKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';

   5. @Entry
   6. @Component
   7. struct Index {
   8. private walletPassClient: walletPass.WalletPassClient = new walletPass.WalletPassClient(this.getUIContext().getHostContext() as common.UIAbilityContext);
   9. // 目标设备类型 phone: 手机
   10. private targetDeviceType: string = '';

   12. async initWalletEnvironment() {
   13. let passStr = JSON.stringify({
   14. targetDeviceType: this.targetDeviceType
   15. });
   16. this.walletPassClient.initWalletEnvironment(passStr).then(() => {
   17. console.info(`Succeeded in initiating walletEnvironment`);
   18. }).catch((err: BusinessError) => {
   19. console.error(`Failed to initiate walletEnvironment, code:${err.code}, message:${err.message}`);
   20. })
   21. }

   23. build() {
   24. // your application UI
   25. }
   26. }
   ```
4. 车主APP调用[queryPassDeviceInfo](../harmonyos-references/wallet-walletpass.md#querypassdeviceinfo)接口查询设备类型，指定目标设备标识。

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
   11. // 目标设备类型 phone: 手机
   12. private targetDeviceType: string = '';

   14. async queryPassDeviceInfo() {
   15. let passStr = JSON.stringify({
   16. passType: this.passType,
   17. targetDeviceType: this.targetDeviceType
   18. });
   19. this.walletPassClient.queryPassDeviceInfo(passStr).then((result: string) => {
   20. console.info(`Succeeded in querying passDeviceInfo, result:${result}`);
   21. }).catch((err: BusinessError) => {
   22. console.error(`Failed to query passDeviceInfo, code:${err.code}, message:${err.message}`);
   23. })
   24. }

   26. build() {
   27. // your application UI
   28. }
   29. }
   ```
5. 车主服务器预置模板后申请钥匙卡片以及JWE数据，参考[车主服务器开发](wallet-carkey-operation.md#车主服务器开发)。
6. 用户主动发起开卡时，车主APP跳转钱包应用，调用[addPass](../harmonyos-references/wallet-walletpass.md#addpass)接口携带上述流程中生成的编码后的JWE数据，开通车钥匙到钱包。

   ```
   1. import { common } from '@kit.AbilityKit';
   2. import { walletPass } from '@kit.WalletKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';

   5. @Entry
   6. @Component
   7. struct Index {
   8. private walletPassClient: walletPass.WalletPassClient = new walletPass.WalletPassClient(this.getUIContext().getHostContext() as common.UIAbilityContext);
   9. // 参考车主服务器开发生成的JWE数据
   10. private jweContent: string = '';

   12. async addPass() {
   13. let passStr = JSON.stringify({
   14. jweContent: this.jweContent
   15. });
   16. this.walletPassClient.addPass(passStr).then((result: string) => {
   17. console.info(`Succeeded in adding pass, result:${result}`);
   18. }).catch((err: BusinessError) => {
   19. console.error(`Failed to add pass, code:${err.code}, message:${err.message}`);
   20. })
   21. }

   23. build() {
   24. // your application UI
   25. }
   26. }
   ```
7. 卡片激活的过程中钱包服务器需要和DK业务管理服务进行交互的包括：设备的认证（和车钥匙管理台交换证书信息）、获取请求个人化数据时的token（用于向车钥匙管理台请求Applet个人化数据）、以及最后的请求Applet个人化数据，最后写入安全芯片，参考[车主服务器激活卡片](wallet-carkey-operation.md#车主服务器激活卡片)。
8. 车主APP可通过[viewPass](../harmonyos-references/wallet-walletpass.md#viewpass)接口跳转钱包查看已开通的车钥匙详情页。

   ```
   1. import { common } from '@kit.AbilityKit';
   2. import { walletPass } from '@kit.WalletKit';

   4. @Entry
   5. @Component
   6. struct Index {
   7. private walletPassClient: walletPass.WalletPassClient = new walletPass.WalletPassClient(this.getUIContext().getHostContext() as common.UIAbilityContext);
   8. // 创建Wallet Kit服务时注册的服务号
   9. private passType: string = '';
   10. // 申请钥匙卡片时定义的卡券唯一标识
   11. private serialNumber: string = '';

   13. async viewPass() {
   14. let passStr = JSON.stringify({
   15. passType: this.passType,
   16. serialNumber: this.serialNumber
   17. });
   18. try {
   19. await this.walletPassClient.viewPass(passStr);
   20. console.info(`Succeeded in viewing pass`);
   21. } catch (err) {
   22. console.error(`Failed to view pass, code:${err.code}, message:${err.message}`);
   23. }
   24. }

   26. build() {
   27. // your application UI
   28. }
   29. }
   ```

## 车主服务器开发

1. 使用Intellij IDEA打开[钱包服务-服务端卡片开通](https://gitcode.com/harmonyos_samples/wallet-kit-sample-code-severdemo-java)的示例代码，没有请先下载Intellij IDEA的当前最新版本。示例代码和工具下载完成后，目录结构如下，我们需要关注下图框出来几个文件：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/oLBMe6Y3TGmMTb3cNmEHaA/zh-cn_image_0000002552799550.png?HW-CC-KV=V1&HW-CC-Date=20260427T235107Z&HW-CC-Expire=86400&HW-CC-Sign=3F228A52DB0F4DB0E422B0750847577D8BDC1EAEEF371F91FE8382DF1173C4A3)
2. 打开resources/release.config.properties文件，替换真实的应用数据。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/mnptBUtsRBqfgo0C9wGinA/zh-cn_image_0000002583439245.png?HW-CC-KV=V1&HW-CC-Date=20260427T235107Z&HW-CC-Expire=86400&HW-CC-Sign=48DC3413D3BC1C823566301A4B9677C911FCC9A4D67E0E5CC37A3010CF281067)

   | 需替换的参数 | 参数说明 |
   | --- | --- |
   | gw.appid |  |
   | gw.appid.secret | [AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)平台申请的Client ID和Client Secret分别填入gw.appid和gw.appid.secret |
   | walletServerBaseUrl | 固定填入服务器基地址：https://wallet-passentrust-drcn.cloud.huawei.com.cn/hmspass |
   | servicePrivateKey | [创建Wallet Kit服务](wallet-preparations.md)步骤5生成的私钥 |
3. 打开resources/data/StdCarKeyModel.json文件，替换真实的应用数据，详细见[预置模板](../harmonyos-references/wallet-rest-api-carkey.md#预置模板)的请求参数。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/ouotbqdCQWG0DLGWXzAj3g/zh-cn_image_0000002583479201.png?HW-CC-KV=V1&HW-CC-Date=20260427T235107Z&HW-CC-Expire=86400&HW-CC-Sign=4A42432548B1F291C595C46619FCC9E500F29377C8CFE38E8FDBEEB4986024E1)
4. 打开stdcarkey/StdCarKeyModelTest.java文件，运行createStdCarKeyModel方法，可看到控制台如下输出，详细见[预置模板](../harmonyos-references/wallet-rest-api-carkey.md#预置模板)的响应参数。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/cXsgm5P5QEyGIvoieTHssg/zh-cn_image_0000002552799552.png?HW-CC-KV=V1&HW-CC-Date=20260427T235107Z&HW-CC-Expire=86400&HW-CC-Sign=9368B3048D3ED219D9ED780100174DBE87CD7AD4241DCC98CF33A68543DD7BCF)
5. 打开resources/data/StdCarKeyInstance.json文件，替换真实的应用数据，详细见[申请钥匙卡片](../harmonyos-references/wallet-rest-api-carkey.md#申请钥匙卡片)的请求参数。
6. 打开stdcarkey/StdCarKeyInstanceTest.java文件，运行addStdCarKeyInstance方法，可看到控制台如下输出，详细见[申请钥匙卡片](../harmonyos-references/wallet-rest-api-carkey.md#申请钥匙卡片)的响应参数。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/4fVAk2uJTfWKChsWdBCXug/zh-cn_image_0000002583439247.png?HW-CC-KV=V1&HW-CC-Date=20260427T235107Z&HW-CC-Expire=86400&HW-CC-Sign=ECF34993FDBF8DE912722C999D1FD62470A0B828E00D011424F212AD32C56823)

## 车主服务器激活卡片

1. 使用 Intellij IDEA打开[钱包服务-服务端卡片激活](https://gitcode.com/harmonyos_samples/wallet-kit-sample-code-severdemo-nfc-java)的示例代码。示例代码和工具下载完成后，解决工程配置等问题后，Constants类中替换SERVER\_PUBLIC\_KEY和SERVER\_SECRET\_KEY为您在[创建Wallet Kit服务](wallet-preparations.md)步骤5生成的公钥和私钥，直接打开PassesController这个类。
2. [设备认证](../harmonyos-references/wallet-rest-api-public.md#设备认证)对应类中的register方法，通过此方法进行设备认证。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/e7U_ZyeqRd6AloZSLbv6Og/zh-cn_image_0000002552959202.png?HW-CC-KV=V1&HW-CC-Date=20260427T235107Z&HW-CC-Expire=86400&HW-CC-Sign=C5FF140AAEF32D56C080A1BBB52764F54DE4CF8EA9CBC20EB99BF135C5E98FDD)
3. [获取个人化数据Token](../harmonyos-references/wallet-rest-api-public.md#获取个人化数据token)对应类中的requestToken方法，通过此方法获取个人化数据Token。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/BKbfXLLITjCrAclx1nhJMA/zh-cn_image_0000002583479203.png?HW-CC-KV=V1&HW-CC-Date=20260427T235107Z&HW-CC-Expire=86400&HW-CC-Sign=CB968AAC9F81BE32C9B3FE14BD25A6C580EC4D78161AE3AFBB8A021AB874EA3D)
4. [获取个人化数据](../harmonyos-references/wallet-rest-api-public.md#获取个人化数据)对应类中的getPersonalInfo方法，重点看dealWithPersonalizeDataRequest中的getDevicePassData这个方法，查看ICCECarKeyDevicePassUnit的generatePassData方法，通过这些方法获取个人化数据。再深入打开里面的getPersonalizeData方法，根据此接口的说明进行生成。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/_1ZvVOqAQA2MYAsrQdB1Pw/zh-cn_image_0000002552799554.png?HW-CC-KV=V1&HW-CC-Date=20260427T235107Z&HW-CC-Expire=86400&HW-CC-Sign=099225663808A8AF7058CFD68403C627A1051BCA672E3FF3041D1D01F184D2F0)
