---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-ukey-best-dev
title: Ukey流程示例指导
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 外部密钥管理扩展 > Ukey流程示例指导
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:35+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b62453985933e502aa64eeef22bc01172fc5645f50752d872c7b79f116fc94aa
---

## 开发模式选择

当前针对双向SSL认证场景，通常有以下两种开发模式。

### 浏览器使用系统ArkWeb能力并自定义客户端

1. 端侧应用调用证书管理能力，拉起证书选择弹框，等待用户选择证书，获得[keyUri](../harmonyos-references/js-apis-certmanagerdialog.md#certreference22)作为resourceId。
2. 端侧应用监听PIN认证回调，处理事件，调用证书管理能力拉起PIN认证弹窗。
3. 此时证书管理会返回认证结果给端侧应用，端侧应用将结果返回给ArkWeb组件。

### 浏览器使用自定义Web组件并自定义客户端

1. 端侧应用调用证书管理能力，拉起证书选择弹框，等待用户选择证书，将[keyUri](../harmonyos-references/js-apis-certmanagerdialog.md#certreference22)作为resourceId，透传到Web组件。
2. Web组件通过证书管理获取对应证书的数据，并且通过[keyUri](../harmonyos-references/js-apis-certmanagerdialog.md#certreference22)作为resourceId调用HUKS的打开资源接口，并查询PIN认证状态。
3. 根据认证结果，进行处理：

   * 如果未认证，需要让端侧应用拉起PIN认证，此时端侧应用收到认证请求并处理事件，调用证书管理能力拉起PIN认证弹窗，获得认证结果后返回给Web组件，接着执行已认证的流程。
   * 如果已认证，Web组件可以直接调用HUKS的三段式接口[initSession](../harmonyos-references/js-apis-huks.md#huksinitsession9)/[updateSession](../harmonyos-references/js-apis-huks.md#huksupdatesession9)/[finishSession](../harmonyos-references/js-apis-huks.md#huksfinishsession9)进行签名。

注意

如果要调用底层Extension的三段式能力，需要传入参数中必须包含[OH\_HUKS\_TAG\_KEY\_CLASS](../harmonyos-references/capi-native-huks-type-h.md#oh_huks_tag)，且值为[OH\_HUKS\_KEY\_CLASS\_EXTENSION](../harmonyos-references/capi-native-huks-type-h.md#oh_huks_keyclasstype)。

## 实践举例

以下是浏览器使用系统能力进行双向SSL认证开发举例。

1. 端侧应用调用证书管理的能力，拉起证书选择弹框[certificateManagerDialog.openAuthorizeDialog](../harmonyos-references/js-apis-certmanagerdialog.md#certificatemanagerdialogopenauthorizedialog22)，等待用户选择证书。

   ```
   1. import { certificateManagerDialog, certificateManager } from '@kit.DeviceCertificateKit';
   2. import { BusinessError } from '@kit.BasicservicesKit';
   3. import { common } from '@kit.AbilityKit';
   4. import { UIContext } from '@kit.ArkUI';

   6. /* context为应用的上下文信息，调用方自行获取，此处仅为示例 */
   7. let context: common.Context = new UIContext().getHostContext() as common.Context;
   8. let certTypes: Array<certificateManagerDialog.CertificateType> = [
   9. certificateManagerDialog.CertificateType.CREDENTIAL_USER,
   10. certificateManagerDialog.CertificateType.CREDENTIAL_APP,
   11. certificateManagerDialog.CertificateType.CREDENTIAL_UKEY
   12. ];
   13. let certPurpose: certificateManager.CertificatePurpose = certificateManager.CertificatePurpose.PURPOSE_DEFAULT;
   14. let authorizeRequest: certificateManagerDialog.AuthorizeRequest = { certTypes: certTypes, certPurpose: certPurpose };
   15. try {
   16. certificateManagerDialog.openAuthorizeDialog(context, authorizeRequest).then((certReference: certificateManagerDialog.CertReference) => {
   17. /* 需要记录选择证书弹窗中获取到的keyUri，方便后续使用 */
   18. let keyUri = certReference.keyUri;
   19. console.info(`Succeeded in opening authorize dialog.`);
   20. }).catch((err: BusinessError) => {
   21. console.error(`Failed to open authorize dialog. Code: ${err.code}, message: ${err.message}`);
   22. });
   23. } catch (err) {
   24. let error = err as BusinessError;
   25. console.error(`Failed to open authorize dialog. Code: ${error.code}, message: ${error.message}`);
   26. }
   ```
2. Web组件解析证书，调用HUKS打开资源，并查询PIN认证状态。

   首先调用证书管理的NDK接口解析用户选择的证书[OH\_CertManager\_GetUkeyCertificate](../harmonyos-references/capi-cm-native-api-h.md#oh_certmanager_getukeycertificate)，获取对应的证书数据。

   其次，根据用户选中的keyUri作为resourceId调用HUKS的NDK接口打开资源[OH\_Huks\_OpenResource](../harmonyos-references/capi-native-huks-external-crypto-api-h.md#oh_huks_openresource)。

   最后，调用HUKS的NDK接口查询PIN认证状态[OH\_Huks\_GetUkeyPinAuthState](../harmonyos-references/capi-native-huks-external-crypto-api-h.md#oh_huks_getukeypinauthstate)。

   ```
   1. #include "huks/native_huks_external_crypto_api.h"
   2. #include "huks/native_huks_param.h"
   3. #include <device_certificate/certmanager/cm_native_api.h>
   4. #include <device_certificate/certmanager/cm_native_type.h>
   5. #include "napi/native_api.h"
   6. #include <string.h>

   8. /* 1. 调用证书管理的NDK接口解析用户选择的证书，获取对应的证书数据 */
   9. static napi_value GetUkeyCert(napi_env env, napi_callback_info info)
   10. {
   11. size_t argc = 1;
   12. napi_value argv[1] = { nullptr };
   13. napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);
   14. if (argc != 1) {
   15. return nullptr;
   16. }
   17. /* 获取keyUri长度 */
   18. size_t length = 0;
   19. napi_get_value_string_utf8(env, argv[0], nullptr, 0, &length);
   20. /* 获取keyUri值 */
   21. char *keyUriBuffer = static_cast<char*>(malloc(length + 1));
   22. size_t result = 0;
   23. napi_get_value_string_utf8(env, argv[0], keyUriBuffer, length + 1, &result);
   24. OH_CM_Blob keyUri = { static_cast<uint32_t>(length + 1), (uint8_t*)keyUriBuffer };

   26. /* 定义UkeyInfo入参 */
   27. OH_CM_UkeyInfo ukeyInfo = { OH_CM_CERT_PURPOSE_SIGN }; /* USB凭据的属性信息，此处省略 */

   29. /* 获取keyUri对应的Ukey证书详情 */
   30. OH_CM_CredentialDetailList credentialList = { 0, nullptr };
   31. int32_t ret = OH_CertManager_GetUkeyCertificate(&keyUri, &ukeyInfo, &credentialList);

   33. /* 调用结束释放内存 */
   34. OH_CertManager_FreeUkeyCertificate(&credentialList);
   35. free(keyUriBuffer);
   36. /* 返回调用结果 */
   37. napi_value retNapi;
   38. napi_create_int32(env, ret, &retNapi);
   39. return retNapi;
   40. }

   42. /* 2. 根据用户选中的keyUri作为resourceId，调用HUKS的NDK接口打开资源 */
   43. OH_Huks_Result InitParamSet(struct OH_Huks_ExternalCryptoParamSet **paramSet,
   44. const struct OH_Huks_ExternalCryptoParam *params, uint32_t paramCount)
   45. {
   46. OH_Huks_Result ret = OH_Huks_InitExternalCryptoParamSet(paramSet);
   47. if (ret.errorCode != OH_HUKS_SUCCESS) {
   48. return ret;
   49. }
   50. ret = OH_Huks_AddExternalCryptoParams(*paramSet, params, paramCount);
   51. if (ret.errorCode != OH_HUKS_SUCCESS) {
   52. OH_Huks_FreeExternalCryptoParamSet(paramSet);
   53. return ret;
   54. }
   55. ret = OH_Huks_BuildExternalCryptoParamSet(paramSet);
   56. if (ret.errorCode != OH_HUKS_SUCCESS) {
   57. OH_Huks_FreeExternalCryptoParamSet(paramSet);
   58. return ret;
   59. }
   60. return ret;
   61. }

   63. static struct OH_Huks_ExternalCryptoParam g_openResourceParamsTest[] = {};

   65. static napi_value OpenResource(napi_env env, napi_callback_info info)
   66. {
   67. size_t argc = 1;
   68. napi_value argv[1] = { nullptr };
   69. napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);
   70. if (argc != 1) {
   71. return nullptr;
   72. }
   73. /* 获取keyUri长度 */
   74. size_t length = 0;
   75. napi_get_value_string_utf8(env, argv[0], nullptr, 0, &length);
   76. /* 获取keyUri值 */
   77. char *keyUriBuffer = static_cast<char*>(malloc(length + 1));
   78. size_t result = 0;
   79. napi_get_value_string_utf8(env, argv[0], keyUriBuffer, length + 1, &result);
   80. OH_Huks_Blob resourceId = {.size = static_cast<uint32_t>(length), .data = (uint8_t*)keyUriBuffer};

   82. struct OH_Huks_ExternalCryptoParamSet *openResourceParamSet = nullptr;
   83. OH_Huks_Result ohResult;
   84. do {
   85. ohResult = InitParamSet(&openResourceParamSet, g_openResourceParamsTest,
   86. sizeof(g_openResourceParamsTest) / sizeof(OH_Huks_ExternalCryptoParam));
   87. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
   88. break;
   89. }
   90. ohResult = OH_Huks_OpenResource(&resourceId, openResourceParamSet);
   91. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
   92. break;
   93. }
   94. } while (0);
   95. free(keyUriBuffer);
   96. OH_Huks_FreeExternalCryptoParamSet(&openResourceParamSet);

   98. OH_Huks_Result res = OH_Huks_OpenResource(&resourceId, openResourceParamSet);
   99. napi_value ret;
   100. napi_create_int32(env, res.errorCode, &ret);
   101. return ret;
   102. }

   104. /* 3. 调用HUKS的NDK接口查询PIN认证状态 */
   105. static struct OH_Huks_ExternalCryptoParam g_getPinStateParamsTest[] = {};

   107. static napi_value GetUkeyPinAuthState(napi_env env, napi_callback_info info)
   108. {
   109. size_t argc = 1;
   110. napi_value argv[1] = { nullptr };
   111. napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);
   112. if (argc != 1) {
   113. return nullptr;
   114. }
   115. /* 获取keyUri长度 */
   116. size_t length = 0;
   117. napi_get_value_string_utf8(env, argv[0], nullptr, 0, &length);
   118. /* 获取keyUri值 */
   119. char *keyUriBuffer = static_cast<char*>(malloc(length + 1));
   120. size_t result = 0;
   121. napi_get_value_string_utf8(env, argv[0], keyUriBuffer, length + 1, &result);
   122. OH_Huks_Blob resourceId = {.size = static_cast<uint32_t>(length), .data = (uint8_t*)keyUriBuffer};

   124. struct OH_Huks_ExternalCryptoParamSet *pinStateParamSet = nullptr;
   125. OH_Huks_ExternalPinAuthState authState = OH_HUKS_EXT_CRYPTO_PIN_NO_AUTH;
   126. OH_Huks_Result ohResult;
   127. do {
   128. ohResult = InitParamSet(&pinStateParamSet, g_getPinStateParamsTest,
   129. sizeof(g_getPinStateParamsTest) / sizeof(OH_Huks_ExternalCryptoParam));
   130. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
   131. break;
   132. }
   133. ohResult = OH_Huks_GetUkeyPinAuthState(&resourceId, pinStateParamSet, &authState);
   134. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
   135. break;
   136. }
   137. } while (0);
   138. free(keyUriBuffer);
   139. OH_Huks_FreeExternalCryptoParamSet(&pinStateParamSet);

   141. napi_value ret;
   142. napi_create_int32(env, ohResult.errorCode, &ret);
   143. return ret;
   144. }

   146. /* 4. 接口定义与注册 */
   147. static napi_value Init(napi_env env, napi_value exports)
   148. {
   149. napi_property_descriptor desc[] = {
   150. { "getUkeyCert", nullptr, GetUkeyCert, nullptr, nullptr, nullptr, napi_default, nullptr },
   151. { "openResource", nullptr, OpenResource, nullptr, nullptr, nullptr, napi_default, nullptr },
   152. { "getUkeyPinAuthState", nullptr, GetUkeyPinAuthState, nullptr, nullptr, nullptr, napi_default, nullptr },
   153. };
   154. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
   155. return exports;
   156. }

   158. static napi_module demoModule = {
   159. .nm_version =1,
   160. .nm_flags = 0,
   161. .nm_filename = nullptr,
   162. .nm_register_func = Init,
   163. .nm_modname = "hello",
   164. .nm_priv = ((void*)0),
   165. .reserved = { 0 },
   166. };
   167. extern "C" __attribute__((constructor)) void RegisterHelloModule(void)
   168. {
   169. napi_module_register(&demoModule);
   170. }
   ```

   对应的d.ts接口声明如下：

   ```
   1. export function getUkeyCert(keyUri: string): number;

   3. export function openResource(keyUri: string): number;

   5. export function getUkeyPinAuthState(keyUri: string): number;
   ```

   调用方式如下：

   ```
   1. import testNapi from "libentry.so";
   2. @Entry
   3. @Component
   4. struct Index {
   5. /* 通过证书弹窗接口获取 */
   6. @State keyUri: string = 'Hello World';
   7. build() {
   8. Row() {
   9. Column() {
   10. Text('Hello World')
   11. .fontSize(50)
   12. .fontWeight(FontWeight.Bold)
   13. .onClick(() => {
   14. testNapi.getUkeyCert(keyUri);
   15. testNapi.openResource(keyUri);
   16. testNapi.getUkeyPinAuthState(keyUri);
   17. })
   18. }
   19. .width('100%')
   20. }
   21. .height('100%')
   22. }
   23. }
   ```
3. 根据认证结果进行处理。

   如果未认证，需让端侧应用拉起PIN认证，此时端侧应用收到认证请求，处理事件，调用证书管理能力拉起PIN认证弹窗[certificateManagerDialog.openUkeyAuthDialog](../harmonyos-references/js-apis-certmanagerdialog.md#certificatemanagerdialogopenukeyauthdialog22)，获得认证结果之后返回给Web组件，接着执行已认证的流程。

   ```
   1. /* 拉起证书管理PIN认证弹窗 */
   2. import { certificateManagerDialog } from '@kit.DeviceCertificateKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   4. import { common } from '@kit.AbilityKit';
   5. import { UIContext } from '@kit.ArkUI';

   7. /* context为应用的上下文信息，调用方自行获取，此处仅为示例 */
   8. let context: common.Context = new UIContext().getHostContext() as common.Context;
   9. /* keyUri为证书凭据的唯一标识符，在第一步中已记录了keyUri，此处仅为示例 */
   10. let keyUri: string = "testKeyAlias";
   11. let ukeyAuthRequest: certificateManagerDialog.UkeyAuthRequest = { keyUri: keyUri };
   12. try {
   13. certificateManagerDialog.openUkeyAuthDialog(context, ukeyAuthRequest)
   14. .then(() => {
   15. console.info(`Succeeded in opening ukey authorization dialog.`);
   16. }).catch((err: BusinessError) => {
   17. console.error(`Failed to open ukey authorization dialog. Code: ${err.code}, message: ${err.message}`);
   18. });
   19. } catch (err) {
   20. let error = err as BusinessError;
   21. console.error(`Failed to open ukey authorization dialog. Code: ${error.code}, message: ${error.message}`);
   22. }
   ```

   如果已认证，Web组件可以直接调用HUKS的三段式接口进行签名。

   ```
   1. /* 调用huks三段式接口获取签名后的数据 */
   2. #include "huks/native_huks_api.h"
   3. #include "huks/native_huks_param.h"
   4. #include "napi/native_api.h"
   5. #include <string.h>

   7. OH_Huks_Result InitParamSet(struct OH_Huks_ParamSet **paramSet,
   8. const struct OH_Huks_Param *params, uint32_t paramCount)
   9. {
   10. OH_Huks_Result ret = OH_Huks_InitParamSet(paramSet);
   11. if (ret.errorCode != OH_HUKS_SUCCESS) {
   12. return ret;
   13. }
   14. ret = OH_Huks_AddParams(*paramSet, params, paramCount);
   15. if (ret.errorCode != OH_HUKS_SUCCESS) {
   16. OH_Huks_FreeParamSet(paramSet);
   17. return ret;
   18. }
   19. ret = OH_Huks_BuildParamSet(paramSet);
   20. if (ret.errorCode != OH_HUKS_SUCCESS) {
   21. OH_Huks_FreeParamSet(paramSet);
   22. return ret;
   23. }
   24. return ret;
   25. }

   27. static struct OH_Huks_Param g_signParamsTest[] = {
   28. {
   29. .tag = OH_HUKS_TAG_ALGORITHM,
   30. .uint32Param = OH_HUKS_ALG_RSA
   31. }, {
   32. .tag = OH_HUKS_TAG_PURPOSE,
   33. .uint32Param = OH_HUKS_KEY_PURPOSE_SIGN
   34. }, {
   35. .tag = OH_HUKS_TAG_KEY_SIZE,
   36. .uint32Param = OH_HUKS_RSA_KEY_SIZE_2048
   37. }, {
   38. .tag = OH_HUKS_TAG_PADDING,
   39. .uint32Param = OH_HUKS_PADDING_PSS
   40. }, {
   41. .tag = OH_HUKS_TAG_DIGEST,
   42. .uint32Param = OH_HUKS_DIGEST_SHA384
   43. }, {
   44. .tag = OH_HUKS_TAG_KEY_CLASS,
   45. .uint32Param = OH_HUKS_KEY_CLASS_EXTENSION
   46. }
   47. };

   49. static const uint32_t RSA_COMMON_SIZE = 1024;
   50. static const char *DATA_TO_SIGN = "testData";
   51. // 此处的keyAlias可以参考第二步的resourceId获取方法，此处仅为示例
   52. static const char *KEY_ALIAS = "testKeyAlias";

   54. static napi_value Sign(napi_env env, napi_callback_info info)
   55. {
   56. // 假设g_keyAlias是获取的resourceId
   57. struct OH_Huks_Blob keyAlias = {
   58. (uint32_t)strlen(KEY_ALIAS),
   59. (uint8_t *)KEY_ALIAS
   60. };
   61. struct OH_Huks_Blob inData = {
   62. (uint32_t)strlen(DATA_TO_SIGN),
   63. (uint8_t *)DATA_TO_SIGN
   64. };
   65. struct OH_Huks_ParamSet *signParamSet = nullptr;
   66. OH_Huks_Result ohResult;
   67. do {
   68. ohResult = InitParamSet(&signParamSet, g_signParamsTest, sizeof(g_signParamsTest) / sizeof(OH_Huks_Param));
   69. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
   70. break;
   71. }
   72. // Init
   73. uint8_t handleS[sizeof(uint64_t)] = {0};
   74. struct OH_Huks_Blob handleSign = { (uint32_t)sizeof(uint64_t), handleS };
   75. ohResult = OH_Huks_InitSession(&keyAlias, signParamSet, &handleSign, nullptr);
   76. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
   77. break;
   78. }
   79. // Finish
   80. uint8_t outDataS[RSA_COMMON_SIZE] = {0};
   81. struct OH_Huks_Blob outDataSign = { RSA_COMMON_SIZE, outDataS };
   82. ohResult = OH_Huks_FinishSession(&handleSign, signParamSet, &inData, &outDataSign);
   83. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
   84. break;
   85. }
   86. } while (0);
   87. OH_Huks_FreeParamSet(&signParamSet);

   89. napi_value ret;
   90. napi_create_int32(env, ohResult.errorCode, &ret);
   91. return ret;
   92. }
   ```
