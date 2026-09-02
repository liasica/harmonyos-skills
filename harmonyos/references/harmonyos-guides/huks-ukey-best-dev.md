---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-ukey-best-dev
title: UKey流程示例指导
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 外部密钥管理扩展 > UKey流程示例指导
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:33+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:65b9dbd6433ba0af76452bd45f16bfcd2aab6771e6e145c8e29e20b2b1ed6866
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

**注意** 

如果要调用底层Extension的三段式能力，需要传入参数中必须包含[OH\_HUKS\_TAG\_KEY\_CLASS](../harmonyos-references/capi-native-huks-type-h.md#oh_huks_tag)，且值为[OH\_HUKS\_KEY\_CLASS\_EXTENSION](../harmonyos-references/capi-native-huks-type-h.md#oh_huks_keyclasstype)。

## 实践举例

以下是浏览器使用系统能力进行双向SSL认证开发举例。

1. 端侧应用调用证书管理的能力，拉起证书选择弹框[certificateManagerDialog.openAuthorizeDialog](../harmonyos-references/js-apis-certmanagerdialog.md#certificatemanagerdialogopenauthorizedialog22)，等待用户选择证书。

   ```ts
   import { certificateManagerDialog, certificateManager } from '@kit.DeviceCertificateKit';
   import { BusinessError } from '@kit.BasicservicesKit';
   import { common } from '@kit.AbilityKit';
   import { UIContext } from '@kit.ArkUI';

   /* context为应用的上下文信息，调用方自行获取，此处仅为示例 */
   let context: common.Context = new UIContext().getHostContext() as common.Context;
   let certTypes: Array<certificateManagerDialog.CertificateType> = [
     certificateManagerDialog.CertificateType.CREDENTIAL_USER,
     certificateManagerDialog.CertificateType.CREDENTIAL_APP,
     certificateManagerDialog.CertificateType.CREDENTIAL_UKEY
   ];
   let certPurpose: certificateManager.CertificatePurpose = certificateManager.CertificatePurpose.PURPOSE_DEFAULT;
   let authorizeRequest: certificateManagerDialog.AuthorizeRequest = { certTypes: certTypes, certPurpose: certPurpose };
   try {
     certificateManagerDialog.openAuthorizeDialog(context, authorizeRequest).then((certReference: certificateManagerDialog.CertReference) => {
       /* 需要记录选择证书弹窗中获取到的keyUri，方便后续使用 */
       let keyUri = certReference.keyUri;
       console.info('Succeeded in opening authorize dialog.');
     }).catch((err: BusinessError) => {
       console.error(`Failed to open authorize dialog. Code: ${err.code}, message: ${err.message}`);
     });
   } catch (err) {
     let error = err as BusinessError;
     console.error(`Failed to open authorize dialog. Code: ${error.code}, message: ${error.message}`);
   }
   ```
2. Web组件解析证书，调用HUKS打开资源，并查询PIN认证状态。

   首先调用证书管理的NDK接口解析用户选择的证书[OH\_CertManager\_GetUkeyCertificate](../harmonyos-references/capi-cm-native-api-h.md#oh_certmanager_getukeycertificate)，获取对应的证书数据。

   其次，根据用户选中的keyUri作为resourceId调用HUKS的NDK接口打开资源[OH\_Huks\_OpenResource](../harmonyos-references/capi-native-huks-external-crypto-api-h.md#oh_huks_openresource)。

   最后，调用HUKS的NDK接口查询PIN认证状态[OH\_Huks\_GetUkeyPinAuthState](../harmonyos-references/capi-native-huks-external-crypto-api-h.md#oh_huks_getukeypinauthstate)。

   ```c
   #include "huks/native_huks_external_crypto_api.h"
   #include "huks/native_huks_param.h"
   #include <device_certificate/certmanager/cm_native_api.h>
   #include <device_certificate/certmanager/cm_native_type.h>
   #include "napi/native_api.h"
   #include <string.h>

   /* 1. 调用证书管理的NDK接口解析用户选择的证书，获取对应的证书数据 */
   static napi_value GetUkeyCert(napi_env env, napi_callback_info info)
   {
       size_t argc = 1;
       napi_value argv[1] = { nullptr };
       napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);
       if (argc != 1) {
           return nullptr;
       }
       /* 获取keyUri长度 */
       size_t length = 0;
       napi_get_value_string_utf8(env, argv[0], nullptr, 0, &length);
       /* 获取keyUri值 */
       char *keyUriBuffer = static_cast<char*>(malloc(length + 1));
       size_t result = 0;
       napi_get_value_string_utf8(env, argv[0], keyUriBuffer, length + 1, &result);
       OH_CM_Blob keyUri = { static_cast<uint32_t>(length + 1), (uint8_t*)keyUriBuffer };

       /* 定义UkeyInfo入参 */
       OH_CM_UkeyInfo ukeyInfo = { OH_CM_CERT_PURPOSE_SIGN }; /* USB凭据的属性信息，此处省略 */

       /* 获取keyUri对应的UKey证书详情 */
       OH_CM_CredentialDetailList credentialList = { 0, nullptr };
       int32_t ret = OH_CertManager_GetUkeyCertificate(&keyUri, &ukeyInfo, &credentialList);

       /* 调用结束释放内存 */
       OH_CertManager_FreeUkeyCertificate(&credentialList);
       free(keyUriBuffer);
       /* 返回调用结果 */
       napi_value retNapi;
       napi_create_int32(env, ret, &retNapi);
       return retNapi;
   }

   /* 2. 根据用户选中的keyUri作为resourceId，调用HUKS的NDK接口打开资源 */
   OH_Huks_Result InitParamSet(struct OH_Huks_ExternalCryptoParamSet **paramSet,
       const struct OH_Huks_ExternalCryptoParam *params, uint32_t paramCount)
   {
       OH_Huks_Result ret = OH_Huks_InitExternalCryptoParamSet(paramSet);
       if (ret.errorCode != OH_HUKS_SUCCESS) {
           return ret;
       }
       ret = OH_Huks_AddExternalCryptoParams(*paramSet, params, paramCount);
       if (ret.errorCode != OH_HUKS_SUCCESS) {
           OH_Huks_FreeExternalCryptoParamSet(paramSet);
           return ret;
       }
       ret = OH_Huks_BuildExternalCryptoParamSet(paramSet);
       if (ret.errorCode != OH_HUKS_SUCCESS) {
           OH_Huks_FreeExternalCryptoParamSet(paramSet);
           return ret;
       }
       return ret;
   }

   static struct OH_Huks_ExternalCryptoParam g_openResourceParamsTest[] = {};

   static napi_value OpenResource(napi_env env, napi_callback_info info)
   {
       size_t argc = 1;
       napi_value argv[1] = { nullptr };
       napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);
       if (argc != 1) {
           return nullptr;
       }
       /* 获取keyUri长度 */
       size_t length = 0;
       napi_get_value_string_utf8(env, argv[0], nullptr, 0, &length);
       /* 获取keyUri值 */
       char *keyUriBuffer = static_cast<char*>(malloc(length + 1));
       size_t result = 0;
       napi_get_value_string_utf8(env, argv[0], keyUriBuffer, length + 1, &result);
       OH_Huks_Blob resourceId = {.size = static_cast<uint32_t>(length), .data = (uint8_t*)keyUriBuffer};

       struct OH_Huks_ExternalCryptoParamSet *openResourceParamSet = nullptr;
       OH_Huks_Result ohResult;
       do {
           ohResult = InitParamSet(&openResourceParamSet, g_openResourceParamsTest,
               sizeof(g_openResourceParamsTest) / sizeof(OH_Huks_ExternalCryptoParam));
           if (ohResult.errorCode != OH_HUKS_SUCCESS) {
               break;
           }
           ohResult = OH_Huks_OpenResource(&resourceId, openResourceParamSet);
           if (ohResult.errorCode != OH_HUKS_SUCCESS) {
               break;
           }
       } while (0);
       free(keyUriBuffer);
       OH_Huks_FreeExternalCryptoParamSet(&openResourceParamSet);

       OH_Huks_Result res = OH_Huks_OpenResource(&resourceId, openResourceParamSet);
       napi_value ret;
       napi_create_int32(env, res.errorCode, &ret);
       return ret;
   }

   /* 3. 调用HUKS的NDK接口查询PIN认证状态 */
   static struct OH_Huks_ExternalCryptoParam g_getPinStateParamsTest[] = {};

   static napi_value GetUkeyPinAuthState(napi_env env, napi_callback_info info)
   {
       size_t argc = 1;
       napi_value argv[1] = { nullptr };
       napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);
       if (argc != 1) {
           return nullptr;
       }
       /* 获取keyUri长度 */
       size_t length = 0;
       napi_get_value_string_utf8(env, argv[0], nullptr, 0, &length);
       /* 获取keyUri值 */
       char *keyUriBuffer = static_cast<char*>(malloc(length + 1));
       size_t result = 0;
       napi_get_value_string_utf8(env, argv[0], keyUriBuffer, length + 1, &result);
       OH_Huks_Blob resourceId = {.size = static_cast<uint32_t>(length), .data = (uint8_t*)keyUriBuffer};

       struct OH_Huks_ExternalCryptoParamSet *pinStateParamSet = nullptr;
       OH_Huks_ExternalPinAuthState authState = OH_HUKS_EXT_CRYPTO_PIN_NO_AUTH;
       OH_Huks_Result ohResult;
       do {
           ohResult = InitParamSet(&pinStateParamSet, g_getPinStateParamsTest,
               sizeof(g_getPinStateParamsTest) / sizeof(OH_Huks_ExternalCryptoParam));
           if (ohResult.errorCode != OH_HUKS_SUCCESS) {
               break;
           }
           ohResult = OH_Huks_GetUkeyPinAuthState(&resourceId, pinStateParamSet, &authState);
           if (ohResult.errorCode != OH_HUKS_SUCCESS) {
               break;
           }
       } while (0);
       free(keyUriBuffer);
       OH_Huks_FreeExternalCryptoParamSet(&pinStateParamSet);

       napi_value ret;
       napi_create_int32(env, ohResult.errorCode, &ret);
       return ret;
   }

   /* 4. 接口定义与注册 */
   static napi_value Init(napi_env env, napi_value exports)
   {
       napi_property_descriptor desc[] = {
           { "getUkeyCert", nullptr, GetUkeyCert, nullptr, nullptr, nullptr, napi_default, nullptr },
           { "openResource", nullptr, OpenResource, nullptr, nullptr, nullptr, napi_default, nullptr },
           { "getUkeyPinAuthState", nullptr, GetUkeyPinAuthState, nullptr, nullptr, nullptr, napi_default, nullptr },
       };
       napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
       return exports;
   }

   static napi_module demoModule = {
       .nm_version =1,
       .nm_flags = 0,
       .nm_filename = nullptr,
       .nm_register_func = Init,
       .nm_modname = "hello",
       .nm_priv = ((void*)0),
       .reserved = { 0 },
   };
   extern "C" __attribute__((constructor)) void RegisterHelloModule(void)
   {
       napi_module_register(&demoModule);
   }
   ```

   对应的d.ts接口声明如下：

   ```ts
   export function getUkeyCert(keyUri: string): number;

   export function openResource(keyUri: string): number;

   export function getUkeyPinAuthState(keyUri: string): number;
   ```

   调用方式如下：

   ```ts
   import testNapi from "libentry.so";
   @Entry
   @Component
   struct Index {
       /* 通过证书弹窗接口获取 */
       @State keyUri: string = 'Hello World';
       build() {
           Row() {
           Column() {
               Text('Hello World')
               .fontSize(50)
               .fontWeight(FontWeight.Bold)
               .onClick(() => {
                   testNapi.getUkeyCert(keyUri);
                   testNapi.openResource(keyUri);
                   testNapi.getUkeyPinAuthState(keyUri);
               })
           }
           .width('100%')
           }
           .height('100%')
       }
   }
   ```
3. 根据认证结果进行处理。

   如果未认证，需让端侧应用拉起PIN认证，此时端侧应用收到认证请求，处理事件，调用证书管理能力拉起PIN认证弹窗[certificateManagerDialog.openUkeyAuthDialog](../harmonyos-references/js-apis-certmanagerdialog.md#certificatemanagerdialogopenukeyauthdialog22)，获得认证结果之后返回给Web组件，接着执行已认证的流程。

   ```ts
   /* 拉起证书管理PIN认证弹窗 */
   import { certificateManagerDialog } from '@kit.DeviceCertificateKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { common } from '@kit.AbilityKit';
   import { UIContext } from '@kit.ArkUI';

   /* context为应用的上下文信息，调用方自行获取，此处仅为示例 */
   let context: common.Context = new UIContext().getHostContext() as common.Context;
   /* keyUri为证书凭据的唯一标识符，在第一步中已记录了keyUri，此处仅为示例 */
   let keyUri: string = "testKeyAlias";
   let ukeyAuthRequest: certificateManagerDialog.UkeyAuthRequest = { keyUri: keyUri };
   try {
     certificateManagerDialog.openUkeyAuthDialog(context, ukeyAuthRequest)
       .then(() => {
         console.info('Succeeded in opening ukey authorization dialog.');
       }).catch((err: BusinessError) => {
         console.error(`Failed to open ukey authorization dialog. Code: ${err.code}, message: ${err.message}`);
       });
   } catch (err) {
     let error = err as BusinessError;
     console.error(`Failed to open ukey authorization dialog. Code: ${error.code}, message: ${error.message}`);
   }
   ```

   如果已认证，Web组件可以直接调用HUKS的三段式接口进行签名。

   ```c
   /* 调用huks三段式接口获取签名后的数据 */
   #include "huks/native_huks_api.h"
   #include "huks/native_huks_param.h"
   #include "napi/native_api.h"
   #include <string.h>

   OH_Huks_Result InitParamSet(struct OH_Huks_ParamSet **paramSet,
       const struct OH_Huks_Param *params, uint32_t paramCount)
   {
       OH_Huks_Result ret = OH_Huks_InitParamSet(paramSet);
       if (ret.errorCode != OH_HUKS_SUCCESS) {
           return ret;
       }
       ret = OH_Huks_AddParams(*paramSet, params, paramCount);
       if (ret.errorCode != OH_HUKS_SUCCESS) {
           OH_Huks_FreeParamSet(paramSet);
           return ret;
       }
       ret = OH_Huks_BuildParamSet(paramSet);
       if (ret.errorCode != OH_HUKS_SUCCESS) {
           OH_Huks_FreeParamSet(paramSet);
           return ret;
       }
       return ret;
   }

   static struct OH_Huks_Param g_signParamsTest[] = {
       {
           .tag = OH_HUKS_TAG_ALGORITHM,
           .uint32Param = OH_HUKS_ALG_RSA
       }, {
           .tag = OH_HUKS_TAG_PURPOSE,
           .uint32Param = OH_HUKS_KEY_PURPOSE_SIGN
       }, {
           .tag = OH_HUKS_TAG_KEY_SIZE,
           .uint32Param = OH_HUKS_RSA_KEY_SIZE_2048
       }, {
           .tag = OH_HUKS_TAG_PADDING,
           .uint32Param = OH_HUKS_PADDING_PSS
       }, {
           .tag = OH_HUKS_TAG_DIGEST,
           .uint32Param = OH_HUKS_DIGEST_SHA384
       }, {
           .tag = OH_HUKS_TAG_KEY_CLASS,
           .uint32Param = OH_HUKS_KEY_CLASS_EXTENSION
       }
   };

   static const uint32_t RSA_COMMON_SIZE = 1024;
   static const char *DATA_TO_SIGN = "testData";
   // 此处的keyAlias可以参考第二步的resourceId获取方法，此处仅为示例
   static const char *KEY_ALIAS = "testKeyAlias";

   static napi_value Sign(napi_env env, napi_callback_info info)
   {
       // 假设g_keyAlias是获取的resourceId
       struct OH_Huks_Blob keyAlias = {
           (uint32_t)strlen(KEY_ALIAS),
           (uint8_t *)KEY_ALIAS
       };
       struct OH_Huks_Blob inData = {
           (uint32_t)strlen(DATA_TO_SIGN),
           (uint8_t *)DATA_TO_SIGN
       };
       struct OH_Huks_ParamSet *signParamSet = nullptr;
       OH_Huks_Result ohResult;
       do {
           ohResult = InitParamSet(&signParamSet, g_signParamsTest, sizeof(g_signParamsTest) / sizeof(OH_Huks_Param));
           if (ohResult.errorCode != OH_HUKS_SUCCESS) {
               break;
           }
           // Init
           uint8_t handleS[sizeof(uint64_t)] = {0};
           struct OH_Huks_Blob handleSign = { (uint32_t)sizeof(uint64_t), handleS };
           ohResult = OH_Huks_InitSession(&keyAlias, signParamSet, &handleSign, nullptr);
           if (ohResult.errorCode != OH_HUKS_SUCCESS) {
               break;
           }
           // Finish
           uint8_t outDataS[RSA_COMMON_SIZE] = {0};
           struct OH_Huks_Blob outDataSign = { RSA_COMMON_SIZE, outDataS };
           ohResult = OH_Huks_FinishSession(&handleSign, signParamSet, &inData, &outDataSign);
           if (ohResult.errorCode != OH_HUKS_SUCCESS) {
               break;
           }
       } while (0);
       OH_Huks_FreeParamSet(&signParamSet);
       
       napi_value ret;
       napi_create_int32(env, ohResult.errorCode, &ret);
       return ret;
   }
   ```
