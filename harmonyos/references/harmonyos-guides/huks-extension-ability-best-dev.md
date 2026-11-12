---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-extension-ability-best-dev
title: 浏览器双向SSL登录
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 应用场景 > 浏览器双向SSL登录
category: harmonyos-guides
scraped_at: 2026-11-12T09:51:41+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:05ab31d77567c28898633912aae89f2b497c45f46b6623285a6edd433019996b
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

如果要调用底层Extension的三段式能力，需要确保传入参数包含[OH\_HUKS\_TAG\_KEY\_CLASS](../harmonyos-references/capi-native-huks-type-h.md#oh_huks_tag)，且值为[OH\_HUKS\_KEY\_CLASS\_EXTENSION](../harmonyos-references/capi-native-huks-type-h.md#oh_huks_keyclasstype)。

## 实践举例

以下是浏览器使用系统能力进行双向SSL认证开发举例。

1. 端侧应用调用证书管理的能力，拉起证书选择弹框[certificateManagerDialog.openAuthorizeDialog](../harmonyos-references/js-apis-certmanagerdialog.md#certificatemanagerdialogopenauthorizedialog22)，等待用户选择证书。

   ```typescript
   import { certificateManagerDialog, certificateManager } from '@kit.DeviceCertificateKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { common } from '@kit.AbilityKit';

   @Entry
   @Component
   struct AuthorizeDialogPage {
     private context: common.Context = getContext(this) as common.Context;

     build() {
       Column() {
         Button($r('app.string.open_authorize_dialog'))
           .onClick(() => {
             this.openAuthorizeDialog();
           })
       }
       .width('100%')
       .height('100%')
     }

     private openAuthorizeDialog(): void {
       let certTypes: certificateManagerDialog.CertificateType[] = [
         certificateManagerDialog.CertificateType.CREDENTIAL_USER,
         certificateManagerDialog.CertificateType.CREDENTIAL_APP,
         certificateManagerDialog.CertificateType.CREDENTIAL_UKEY
       ];
       let certPurpose: certificateManager.CertificatePurpose =
         certificateManager.CertificatePurpose.PURPOSE_DEFAULT;
       let authorizeRequest: certificateManagerDialog.AuthorizeRequest = {
         certTypes: certTypes, certPurpose: certPurpose
       };
       try {
         certificateManagerDialog.openAuthorizeDialog(this.context, authorizeRequest)
           .then((certReference: certificateManagerDialog.CertReference) => {
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
     }
   }
   ```
2. Web组件解析证书，调用HUKS打开资源，并查询PIN认证状态。

   首先调用证书管理的NDK接口解析用户选择的证书[OH\_CertManager\_GetUkeyCertificate](../harmonyos-references/capi-cm-native-api-h.md#oh_certmanager_getukeycertificate)，获取对应的证书数据。

   其次，根据用户选中的keyUri作为resourceId调用HUKS的NDK接口打开资源[OH\_Huks\_OpenResource](../harmonyos-references/capi-native-huks-external-crypto-api-h.md#oh_huks_openresource)。

   最后，调用HUKS的NDK接口查询PIN认证状态[OH\_Huks\_GetUkeyPinAuthState](../harmonyos-references/capi-native-huks-external-crypto-api-h.md#oh_huks_getukeypinauthstate)。

   ```
   /* 1. 调用证书管理接口解析用户选择的证书，获取对应的证书数据 */
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
       if (length == 0 || length >= SIZE_MAX) {
           return nullptr;
       }
       /* 获取keyUri值 */
       char *keyUriBuffer = static_cast<char*>(malloc(length + 1));
       if (keyUriBuffer == nullptr) {
           return nullptr;
       }
       size_t result = 0;
       napi_get_value_string_utf8(env, argv[0], keyUriBuffer, length + 1, &result);
       OH_CM_Blob keyUri = { static_cast<uint32_t>(length), (uint8_t*)keyUriBuffer };

       /* 定义UkeyInfo入参 */
       OH_CM_UkeyInfo ukeyInfo = { OH_CM_CERT_PURPOSE_SIGN };

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

   /* 2. 根据用户选中的keyUri作为resourceId，调用HUKS接口打开资源 */
   static struct OH_Huks_ExternalCryptoParam g_bpOpenResourceParamsTest[] = {};

   static napi_value BpOpenResource(napi_env env, napi_callback_info info)
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
       if (length == 0 || length >= SIZE_MAX) {
           return nullptr;
       }
       /* 获取keyUri值 */
       char *keyUriBuffer = static_cast<char*>(malloc(length + 1));
       if (keyUriBuffer == nullptr) {
           return nullptr;
       }
       size_t result = 0;
       napi_get_value_string_utf8(env, argv[0], keyUriBuffer, length + 1, &result);
       OH_Huks_Blob resourceId = {
           .size = static_cast<uint32_t>(length),
           .data = (uint8_t*)keyUriBuffer
       };

       struct OH_Huks_ExternalCryptoParamSet *openResourceParamSet = nullptr;
       OH_Huks_Result ohResult;
       do {
           ohResult = InitParamSet(&openResourceParamSet, g_bpOpenResourceParamsTest,
               sizeof(g_bpOpenResourceParamsTest) / sizeof(OH_Huks_ExternalCryptoParam));
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

       napi_value ret;
       napi_create_int32(env, ohResult.errorCode, &ret);
       return ret;
   }

   /* 3. 调用HUKS接口查询PIN认证状态 */
   static struct OH_Huks_ExternalCryptoParam g_bpGetPinStateParamsTest[] = {};

   static napi_value BpGetUkeyPinAuthState(napi_env env, napi_callback_info info)
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
       if (length == 0 || length >= SIZE_MAX) {
           return nullptr;
       }
       /* 获取keyUri值 */
       char *keyUriBuffer = static_cast<char*>(malloc(length + 1));
       if (keyUriBuffer == nullptr) {
           return nullptr;
       }
       size_t result = 0;
       napi_get_value_string_utf8(env, argv[0], keyUriBuffer, length + 1, &result);
       OH_Huks_Blob resourceId = {
           .size = static_cast<uint32_t>(length),
           .data = (uint8_t*)keyUriBuffer
       };

       struct OH_Huks_ExternalCryptoParamSet *pinStateParamSet = nullptr;
       OH_Huks_ExternalPinAuthState authState = OH_HUKS_EXT_CRYPTO_PIN_NO_AUTH;
       OH_Huks_Result ohResult;
       do {
           ohResult = InitParamSet(&pinStateParamSet, g_bpGetPinStateParamsTest,
               sizeof(g_bpGetPinStateParamsTest) / sizeof(OH_Huks_ExternalCryptoParam));
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
           { "openResource", nullptr, BpOpenResource, nullptr, nullptr, nullptr, napi_default, nullptr },
           { "getUkeyPinAuthState", nullptr, BpGetUkeyPinAuthState, nullptr, nullptr, nullptr, napi_default, nullptr },
       };
       napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
       return exports;
   }

   static napi_module demoModule = {
       .nm_version = 1,
       .nm_flags = 0,
       .nm_filename = nullptr,
       .nm_register_func = Init,
       .nm_modname = "entry",
       .nm_priv = ((void*)0),
       .reserved = { 0 },
   };
   extern "C" __attribute__((constructor)) void RegisterHelloModule(void)
   {
       napi_module_register(&demoModule);
   }
   ```

   对应的d.ts接口声明如下：

   ```typescript
   export function getUkeyCert(keyUri: string): number;

   export function openResource(keyUri: string): number;

   export function getUkeyPinAuthState(keyUri: string): number;
   ```

   调用方式如下：

   ```typescript
   import testNapi from 'libentry.so';
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
                       testNapi.getUkeyCert(this.keyUri);
                       testNapi.openResource(this.keyUri);
                       testNapi.getUkeyPinAuthState(this.keyUri);
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

   ```typescript
   import { certificateManagerDialog } from '@kit.DeviceCertificateKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { common } from '@kit.AbilityKit';

   @Entry
   @Component
   struct UkeyAuthDialogPage {
     private context: common.Context = getContext(this) as common.Context;
     /* keyUri为证书凭据的唯一标识符，在第一步中已记录了keyUri，此处仅为示例 */
     private keyUri: string = 'testKeyAlias';

     build() {
       Column() {
         Button($r('app.string.open_ukey_auth_dialog'))
           .onClick(() => {
             this.openUkeyAuthDialog();
           })
       }
       .width('100%')
       .height('100%')
     }

     private openUkeyAuthDialog(): void {
       let ukeyAuthRequest: certificateManagerDialog.UkeyAuthRequest = { keyUri: this.keyUri };
       try {
         certificateManagerDialog.openUkeyAuthDialog(this.context, ukeyAuthRequest)
           .then(() => {
             console.info('Succeeded in opening ukey authorization dialog.');
           }).catch((err: BusinessError) => {
             console.error(`Failed to open ukey authorization dialog. Code: ${err.code}, message: ${err.message}`);
           });
       } catch (err) {
         let error = err as BusinessError;
         console.error(`Failed to open ukey authorization dialog. Code: ${error.code}, message: ${error.message}`);
       }
     }
   }
   ```

   如果已认证，Web组件可以直接调用HUKS的三段式接口进行签名。

   ```
   /* 调用huks三段式接口获取签名后的数据 */
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
   static const char *KEY_ALIAS = "testKeyAlias";

   static napi_value Sign(napi_env env, napi_callback_info info)
   {
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
           ohResult = InitHuksParamSet(&signParamSet, g_signParamsTest,
               sizeof(g_signParamsTest) / sizeof(OH_Huks_Param));
           if (ohResult.errorCode != OH_HUKS_SUCCESS) {
               break;
           }
           uint8_t handleS[sizeof(uint64_t)] = {0};
           struct OH_Huks_Blob handleSign = { (uint32_t)sizeof(uint64_t), handleS };
           ohResult = OH_Huks_InitSession(&keyAlias, signParamSet, &handleSign, nullptr);
           if (ohResult.errorCode != OH_HUKS_SUCCESS) {
               break;
           }
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
