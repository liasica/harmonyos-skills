---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-extension-ability-support-dev
title: CryptoExtensionAbility适配开发指导
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:35+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:270b6814768ea56a835d6b8f7471f90194d5e320352e348a4cc38be0f0f67e2f
---

## 适配指导

本文档旨在指导驱动厂商如何继承实现[CryptoExtensionAbility](../harmonyos-references/js-apis-cryptoextensionability.md)需要的接口能力，此处给出实现参考，其他实现依照业务需要依次调用driver封装的底层驱动函数。

在DevEco Studio工程中手动新建一个CryptoExtensionAbility组件，具体步骤如下：

1. 在工程Module对应的ets目录下，右键选择“New > Directory”，新建一个目录，名称可以自己定义，例如cryptoability。
2. 在cryptoability目录，右键选择“New > ArkTS File”，新建一个文件，名称可以自己定义，例如CryptoAbility.ets。

   其目录结构如下所示：

   ```
   1. ├── ets
   2. │   └── cryptoability
   3. │       └── CryptoAbility.ets
   ```
3. 开发CryptoExtensionAbility需要配置[ohos.permission.CRYPTO\_EXTENSION\_REGISTER](restricted-permissions.md#ohospermissioncrypto_extension_register)权限，该权限属于[受限开放权限](restricted-permissions.md)，请按照[申请受限权限](declare-permissions-in-acl.md)指引为应用进行申请。

   ```
   1. // entry/src/main/module.json5
   2. {
   3. "module": {
   4. // ...
   5. "requestPermissions": [
   6. {
   7. "name": "ohos.permission.CRYPTO_EXTENSION_REGISTER"
   8. }
   9. ],
   10. }
   11. }
   ```
4. 在工程Module对应的module.json5配置文件中注册AppServiceExtensionAbility组件，name标签表示ability名称，长度最大为127字节，srcEntry标签表示当前CryptoExtensionAbility组件所对应的代码路径，type标签需要设置为“crypto”，exported标签设置为false表示不允许三方应用调用，配置多个ability时要求每个name标签必须是唯一的。

   ```
   1. // entry/src/main/module.json5
   2. {
   3. "module": {
   4. // ...
   5. "extensionAbilities": [
   6. {
   7. "name": "CryptoExtension",
   8. "srcEntry": "./ets/cryptoability/CryptoAbility.ets",
   9. "type": "crypto",
   10. "exported": false
   11. }
   12. ],
   13. }
   14. }
   ```
5. 在CryptoAbility.ets文件中，增加导入CryptoExtensionAbility的依赖包，自定义类继承CryptoExtensionAbility组件并实现其中的接口函数。导入CryptoExtensionAbility需要实现在[CryptoExtensionAbility](../harmonyos-references/js-apis-cryptoextensionability.md)中给出的所有函数，此处给出实现参考，与底层驱动的调用对应关系见下文。

   注意

   1. 句柄资源和PIN认证状态需要做基于UID的隔离，在onOpenResource、onCloseResource、onAuthUkeyPin、onGetUkeyPinAuthState和onClearUkeyPinAuthState接口的入参params中会包含业务的UID信息（通过[HUKS\_EXT\_CRYPTO\_TAG\_UID](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalcryptotag)可获取业务身份），可基于此做句柄资源和PIN认证状态的隔离。
   2. 接口函数的错误不支持自定义返回，不按接口定义方式返回会导致异常。

   ```
   1. import { huks, huksExternalCrypto, CryptoExtensionAbility, HuksCryptoExtensionCertInfo, HuksCryptoExtensionResult } from '@kit.UniversalKeystoreKit';
   2. import { util } from '@kit.ArkTS'
   3. import { cryptoFramework } from '@kit.CryptoArchitectureKit'

   5. class CryptoExtension extends CryptoExtensionAbility {
   6. // 本步骤内的接口函数实现均需在class内，为方便开发者理解及使用，每个接口函数在下文详细解释。
   7. }
   ```

   **接口介绍：**

   （1）onOpenResource在Ukey签名验签操作中用于打开指定资源（如建立会话或连接）。resourceId表示要打开的资源标识，应用身份可以在params中由[HUKS\_EXT\_CRYPTO\_TAG\_UID](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalcryptotag)参数携带。当调用成功时，返回值中的resultCode成员设置为0，handle成员非空；调用失败时，resultCode携带错误码信息。

   ```
   1. onOpenResource(resourceId: string, params: Array<huksExternalCrypto.HuksExternalCryptoParam>): Promise<HuksCryptoExtensionResult> {
   2. // 构造结果对象，默认返回操作失败，返回值为HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL
   3. let result: HuksCryptoExtensionResult = {
   4. resultCode: HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL,
   5. };

   7. // 获取 appId
   8. let appId: string | undefined = params.find((param =>
   9. param.tag === huksExternalCrypto.HuksExternalCryptoTag.HUKS_EXT_CRYPTO_TAG_UID))?.value.toString();
   10. if (appId === undefined) {
   11. return Promise.resolve(result);
   12. }

   14. // 解析 resource index
   15. let index: string = JSON.parse(resourceId)['index'];

   17. // ...
   18. let res: HuksCryptoExtensionResult = {
   19. resultCode: HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL,
   20. }
   21. try {
   22. let driver: YourUKeyDriver = YourDriverInstance;
   23. res = driver.YourDriver_onOpenResource(index, ...);
   24. // 场景：打开资源成功
   25. result.resultCode = res.resultCode
   26. result.handle = res.handle
   27. } catch (error) {
   28. // 场景：打开资源失败
   29. result.resultCode = res.resultCode
   30. console.error(`promise: onOpenResource failed`);
   31. }
   32. return Promise.resolve(result);
   33. }
   ```

   （2）onCloseResource在Ukey签名验签操作中用于关闭指定资源（如释放会话或连接）。handle为待关闭资源的句柄，应用身份可以在params中由[HUKS\_EXT\_CRYPTO\_TAG\_UID](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalcryptotag)参数携带。当调用成功时，返回值中的resultCode成员设置为0；调用失败时，resultCode携带错误码信息。

   ```
   1. onCloseResource(handle: string, params: Array<huksExternalCrypto.HuksExternalCryptoParam>): Promise<HuksCryptoExtensionResult> {
   2. // ...
   3. let result: HuksCryptoExtensionResult = {
   4. resultCode: HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL,
   5. };

   7. let res: HuksCryptoExtensionResult = {
   8. resultCode: HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL,
   9. }
   10. try {
   11. let driver: YourUKeyDriver = YourDriverInstance;
   12. res = driver.YourDriver_closeOpenResource(handle, ...);
   13. // 场景：关闭资源成功
   14. result.resultCode = res.resultCode
   15. } catch (error) {
   16. // 场景：关闭资源失败
   17. result.resultCode = res.resultCode
   18. console.error(`promise: onCloseResource failed`);
   19. }
   20. return Promise.resolve(result);
   21. }
   ```

   （3）onGetProperty在Ukey签名验签操作中用于获取指定资源的属性信息。handle为资源句柄，propertyId为待获取的属性标识，应用身份可以在params中由[HUKS\_EXT\_CRYPTO\_TAG\_UID](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalcryptotag)参数携带。当调用成功时，返回值中的resultCode成员设置为0，返回值中的property成员包含属性信息。调用失败时，resultCode携带错误码信息。

   在onGetProperty中须实现导出公钥功能，以便上游业务使用PIN加密传输并完成PIN码认证。加密算法支持RSA、SM2等。当入参propertyId为SKF\_ExportPublicKey时，返回的公钥信息采用JSON格式，包含以下4个必选字段，分别是publicKey（公钥数据）、algo（算法类型及密钥长度）、transformation（密码学操作参数，如填充模式）、size（公钥数据长度）。具体实现可参考下方示例代码中onGetProperty接口的相关部分。

   ```
   1. onGetProperty(handle: string, propertyId: string, params: Array<huksExternalCrypto.HuksExternalCryptoParam>): Promise<HuksCryptoExtensionResult> {
   2. // ...
   3. let emptyArray: Array<huksExternalCrypto.HuksExternalCryptoParam> = [];
   4. let result: HuksCryptoExtensionResult = {
   5. resultCode: HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL,
   6. property: emptyArray
   7. };

   9. // 导出公钥
   10. if (propertyId == 'SKF_ExportPublicKey') {
   11. result.resultCode = 0
   12. let encryptionAlgo: string = 'RSA1024'
   13. let padding: string = 'PRIMES_2';
   14. // 1. 创建一个AsyKeyGenerator实例。
   15. let rsaGenerator = cryptoFramework.createAsyKeyGenerator(`${encryptionAlgo}|${padding}`);
   16. // 2. 使用密钥生成器随机生成非对称密钥对。
   17. let keyPair = rsaGenerator.generateKeyPairSync();
   18. // 3. 将公钥导出，并转换为Json字符串
   19. const pkData = Array.from(keyPair.pubKey.getEncoded().data);
   20. let transformation: string = 'RSA1024|PKCS1'
   21. const encoder = new util.TextEncoder();
   22. let info = encoder.encodeInto(JSON.stringify({
   23. publicKey: pkData,
   24. algo: encryptionAlgo,
   25. transformation: transformation,
   26. size: pkData.length
   27. }));
   28. // 4. 保存私钥，后续用于解密加密的数据
   29. let privKey = keyPair.priKey
   30. // 返回用来加密传pin的公钥和加密算法信息，详见导出公钥文档
   31. result.property = [
   32. { tag: huksExternalCrypto.HuksExternalCryptoTag.HUKS_EXT_CRYPTO_TAG_EXTRA_DATA, value: info }
   33. ]
   34. return Promise.resolve(result);
   35. }

   37. let res: HuksCryptoExtensionResult = {
   38. resultCode: HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL,
   39. }
   40. try {
   41. // 场景：获取属性成功
   42. let driver: YourUKeyDriver = YourDriverInstance;
   43. res = driver.YourDriver_onGetProperty(...);
   44. result.resultCode = res.resultCode
   45. result.property = res.property
   46. } catch (error) {
   47. // 场景：获取属性失败
   48. result.resultCode = res.resultCode
   49. console.error(`promise: onGetProperty failed`);
   50. }
   51. return Promise.resolve(result);
   52. }
   ```

   （4）onAuthUkeyPin用于在Ukey签名之前验证PIN码。加密后的PIN码通过param中传入[HUKS\_EXT\_CRYPTO\_TAG\_UKEY\_PIN](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalcryptotag)参数携带，需使用onGetProperty中保存的私钥进行解密。

   当PIN码校验成功时，返回值中的resultCode成员设置为0，返回值中的authState设置为[HUKS\_EXT\_CRYPTO\_PIN\_AUTH\_SUCCEEDED](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalpinauthstate)。当PIN码不正确时，resultCode携带错误码信息，返回值中的retryCount设置为剩余重试次数，每次认证失败重试次数减1，当重试次数为0时，resultCode设置为[HUKS\_CRYPTO\_EXTENSION\_ERR\_PIN\_LOCKED](../harmonyos-references/js-apis-cryptoextensionability.md#hukscryptoextensionresultcode)，authState设置为[HUKS\_EXT\_CRYPTO\_PIN\_LOCKED](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalpinauthstate)。

   ```
   1. onAuthUkeyPin(handle: string, params: Array<huksExternalCrypto.HuksExternalCryptoParam>): Promise<HuksCryptoExtensionResult> {
   2. let pin: string | undefined = undefined;
   3. for (let param of params) {
   4. if (param.tag == huksExternalCrypto.HuksExternalCryptoTag.HUKS_EXT_CRYPTO_TAG_UKEY_PIN) {
   5. let originPinData = param.value as Uint8Array;
   6. // 根据导出公钥所传出的加密算法和填充方式进行解密originPinData获取pin
   7. // ...
   8. }
   9. }
   10. // ...
   11. let result: HuksCryptoExtensionResult = {
   12. resultCode: HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL,
   13. authState: huksExternalCrypto.HuksExternalPinAuthState.HUKS_EXT_CRYPTO_PIN_NO_AUTH,
   14. retryCount: 0
   15. };

   17. let res: HuksCryptoExtensionResult = {
   18. resultCode: HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL,
   19. }
   20. try {
   21. // 场景：PIN码认证成功
   22. let driver: YourUKeyDriver = YourDriverInstance;
   23. res = driver.YourDriver_onAuthUkeyPin(pin, ...);
   24. result.resultCode = res.resultCode
   25. result.authState = res.authState
   26. } catch (error) {
   27. // 场景：PIN码认证失败
   28. result.resultCode = res.resultCode
   29. result.retryCount = res.retryCount
   30. console.error(`promise: onAuthUkeyPin failed`);
   31. }
   32. return Promise.resolve(result);
   33. }
   ```

   （5）onGetUkeyPinAuthState用于应用查询PIN码的认证状态。当调用成功时，返回值中的resultCode成员设置为0，返回值中的authState设置为对应的认证状态。调用失败时，resultCode携带错误码信息。

   ```
   1. onGetUkeyPinAuthState(handle: string, params: Array<huksExternalCrypto.HuksExternalCryptoParam>): Promise<HuksCryptoExtensionResult> {
   2. // ...
   3. let result: HuksCryptoExtensionResult = {
   4. resultCode: HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL,
   5. authState: 0
   6. };

   8. let res: HuksCryptoExtensionResult = {
   9. resultCode: HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL,
   10. }
   11. try {
   12. // 场景：获取PIN码认证状态成功
   13. let driver: YourUKeyDriver = YourDriverInstance;
   14. res = driver.YourDriver_onAuthUkeyPin(...);
   15. result.resultCode = res.resultCode
   16. result.authState = res.authState
   17. if (result.authState != 0) {
   18. // 场景： PIN码已认证
   19. // ...
   20. } else {
   21. // 场景： PIN码未认证
   22. // ...
   23. }
   24. } catch (error) {
   25. // 场景：获取PIN码认证状态失败
   26. result.resultCode = res.resultCode
   27. console.error(`promise: onGetUkeyPinAuthState failed`);
   28. }
   29. return Promise.resolve(result);
   30. }
   ```

   （6）onClearUkeyPinAuthState用于重置PIN码的认证状态。当调用成功时，返回值中的resultCode成员设置为0。调用失败时，resultCode携带错误码信息。

   ```
   1. onClearUkeyPinAuthState(handle: string, params: Array<huksExternalCrypto.HuksExternalCryptoParam>): Promise<HuksCryptoExtensionResult> {
   2. // ...
   3. let result: HuksCryptoExtensionResult = {
   4. resultCode: HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL,
   5. };

   7. let res: HuksCryptoExtensionResult = {
   8. resultCode: HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL,
   9. }
   10. try {
   11. // 场景：清除PIN码认证状态成功
   12. let driver: YourUKeyDriver = YourDriverInstance;
   13. res = driver.YourDriver_onClearUkeyPinAuthState(...);
   14. result.resultCode = res.resultCode
   15. } catch (error) {
   16. // 场景：清除PIN码认证状态失败
   17. result.resultCode = res.resultCode
   18. console.error(`promise: onClearUkeyPinAuthState failed`);
   19. }
   20. return Promise.resolve(result);
   21. }
   ```

   （7）onInitSession在Ukey签名验签操作中用于初始化密钥会话。应用身份可以在param中由[HUKS\_EXT\_CRYPTO\_TAG\_UID](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalcryptotag)参数携带。当调用成功时，返回值中的resultCode成员设置为0，handle成员非空。调用失败时，resultCode携带错误码信息。

   ```
   1. onInitSession(handle: string, params: huks.HuksOptions): Promise<HuksCryptoExtensionResult> {
   2. // ...
   3. let result: HuksCryptoExtensionResult = {
   4. resultCode: HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL,
   5. handle: ""
   6. };

   8. let res: HuksCryptoExtensionResult = {
   9. resultCode: HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL,
   10. }
   11. try {
   12. // 场景：三段式init阶段成功
   13. let driver: YourUKeyDriver = YourDriverInstance;
   14. res = driver.YourDriver_onInitSession(...);
   15. result.resultCode = res.resultCode
   16. result.handle = res.handle
   17. } catch (error) {
   18. // 场景：三段式init阶段失败
   19. result.resultCode = res.resultCode
   20. console.error(`promise: onInitSession failed`);
   21. }
   22. return Promise.resolve(result);
   23. }
   ```

   （8）onUpdateSession在Ukey签名验签操作中用于分段传输大批量数据。应用身份可以在param中由[HUKS\_EXT\_CRYPTO\_TAG\_UID](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalcryptotag)参数携带。当调用成功时，返回值中的resultCode成员设置为0。调用失败时，resultCode携带错误码信息。

   ```
   1. onUpdateSession(handle: string, params: huks.HuksOptions): Promise<HuksCryptoExtensionResult> {
   2. // ...
   3. let certs: Uint8Array = new Uint8Array();
   4. let result: HuksCryptoExtensionResult = {
   5. resultCode: HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL,
   6. outData: certs
   7. };

   9. let res: HuksCryptoExtensionResult = {
   10. resultCode: HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL,
   11. }
   12. try {
   13. // 场景：三段式update阶段成功
   14. let driver: YourUKeyDriver = YourDriverInstance;
   15. res = driver.YourDriver_onUpdateSession(...);
   16. result.resultCode = res.resultCode
   17. result.outData = res.outData
   18. } catch (error) {
   19. // 场景：三段式update阶段失败
   20. result.resultCode = res.resultCode
   21. console.error(`promise: onUpdateSession failed`);
   22. }
   23. return Promise.resolve(result);
   24. }
   ```

   （9）onFinishSession在Ukey签名操作中用于传输最后一段明文，在验签操作中用于传输签名。应用身份可以在param中由[HUKS\_EXT\_CRYPTO\_TAG\_UID](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalcryptotag)参数携带。当调用成功时，返回值中的resultCode成员设置为0。调用失败时，resultCode携带错误码信息。

   ```
   1. onFinishSession(handle: string, params: huks.HuksOptions): Promise<HuksCryptoExtensionResult> {
   2. // ...
   3. let certs: Uint8Array = new Uint8Array();
   4. let result: HuksCryptoExtensionResult = {
   5. resultCode: HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL,
   6. outData: certs
   7. };

   9. let res: HuksCryptoExtensionResult = {
   10. resultCode: HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL,
   11. };
   12. try {
   13. // 场景：三段式finish阶段成功
   14. let driver: YourUKeyDriver = YourDriverInstance;
   15. res = driver.YourDriver_onFinishSession(...);
   16. result.resultCode = res.resultCode
   17. result.outData = res.outData
   18. } catch (error) {
   19. // 场景：三段式finish阶段失败
   20. result.resultCode = res.resultCode
   21. console.error(`promise: onFinishSession failed`);
   22. }
   23. return Promise.resolve(result);
   24. }
   ```

   （10）onExportCertificate用于查询某个resourceId下的证书。可以通过解析参数[HUKS\_EXT\_CRYPTO\_TAG\_PURPOSE](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalcryptotag)获取业务希望的证书类型。如未指定，默认获取的证书类型是签名证书。

   其值含义如下：

   0：默认用途。

   1：用于查询所有凭据。

   2：用于凭据签名。

   3：用于凭据加密。

   ```
   1. onExportCertificate(resourceId: string, params: Array<huksExternalCrypto.HuksExternalCryptoParam>): Promise<HuksCryptoExtensionResult> {
   2. // ...
   3. let certInfoSetArray: Array<HuksCryptoExtensionCertInfo> = []
   4. let result: HuksCryptoExtensionResult = {
   5. resultCode: HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL,
   6. certs: certInfoSetArray
   7. };

   9. let res: HuksCryptoExtensionResult = {
   10. resultCode: HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL,
   11. }
   12. try {
   13. // 场景：导出证书成功
   14. let driver: YourUKeyDriver = YourDriverInstance;
   15. res = driver.YourDriver_onExportCertificate(...);
   16. result.resultCode = res.resultCode
   17. result.certs = res.certs
   18. } catch (error) {
   19. // 场景：导出证书失败
   20. result.resultCode = res.resultCode
   21. console.error(`promise: onExportCertificate failed`);
   22. }
   23. return Promise.resolve(result);
   24. }
   ```

   （11）onEnumCertificates在Ukey签名验签操作中用于枚举证书列表。应用身份可以在params中由[HUKS\_EXT\_CRYPTO\_TAG\_UID](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalcryptotag)参数携带。当调用成功时，返回值中的resultCode成员设置为0，返回值中的certs成员包含证书列表（类型为Array<[HuksCryptoExtensionCertInfo](../harmonyos-references/js-apis-cryptoextensionability.md#hukscryptoextensioncertinfo)>）。调用失败时，resultCode携带错误码信息。

   ```
   1. onEnumCertificates(params: Array<huksExternalCrypto.HuksExternalCryptoParam>): Promise<HuksCryptoExtensionResult> {
   2. // ...
   3. let certInfoSetArray: Array<HuksCryptoExtensionCertInfo> = []
   4. let result: HuksCryptoExtensionResult = {
   5. resultCode: HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL,
   6. certs: certInfoSetArray
   7. };

   9. let res: HuksCryptoExtensionResult = {
   10. resultCode: HuksCryptoExtensionResultCode.HUKS_CRYPTO_EXTENSION_ERR_EXTENSION_FAIL,
   11. }
   12. try {
   13. // 场景：导出所有证书成功
   14. let driver: YourUKeyDriver = YourDriverInstance;
   15. res = driver.YourDriver_onEnumCertificates(...);
   16. result.resultCode = res.resultCode
   17. result.certs = res.certs
   18. } catch (error) {
   19. // 场景：导出所有证书失败
   20. result.resultCode = res.resultCode
   21. console.error(`promise: onEnumCertificates failed`);
   22. }
   23. return Promise.resolve(result);
   24. }
   ```

## 驱动应用注册、解注册CryptoExtensionAbility适配

### 注册CryptoExtensionAbility

驱动HAP检测到Ukey存在时，向系统注册CryptoExtensionAbility。例如：Ukey插入等。

**示例：**

```
1. // ./ets/cryptoability/CryptoAbility.ts

3. import { huksExternalCrypto } from '@kit.UniversalKeystoreKit';

5. let ExtPropertiesTemp: Array<huksExternalCrypto.HuksExternalCryptoParam> = [
6. {
7. tag: huksExternalCrypto.HuksExternalCryptoTag.HUKS_EXT_CRYPTO_TAG_ABILITY_NAME,
8. value: stringToUint8Array("YourCryptoExtensionName")
9. }
10. ]

12. // provider名称，为保证全局唯一，建议包含厂商信息。
13. let provider = "testProvider"
14. huksExternalCrypto.registerProvider(provider, ExtPropertiesTemp);
```

### 解注册CryptoExtensionAbility

驱动HAP检测到Ukey不存在时，向系统解注册CryptoExtensionAbility。例如：Ukey拔出等。

**示例：**

```
1. huksExternalCrypto.unregisterProvider(provider, ExtPropertiesTemp);
```
