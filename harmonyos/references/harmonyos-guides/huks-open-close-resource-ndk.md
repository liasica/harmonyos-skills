---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-open-close-resource-ndk
title: 打开资源/关闭资源(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 外部密钥管理扩展 > 资源管理 > 打开资源/关闭资源(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:32+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:866638ffbd6d9f302422a046d43ea13053a7ec61ef6a713b9ef0f6153aa24396
---

## 打开资源

从API 22开始，huksExternalCrypto提供打开/关闭资源功能接口。应用在密钥操作之前（密钥操作、通用操作、PIN码认证等），需要先调用[OH\_Huks\_OpenResource](../harmonyos-references/capi-native-huks-external-crypto-api-h.md#oh_huks_openresource)打开资源。打开资源需要获取resourceId，resourceId通过调用证书管理系统能力提供的[证书选择接口](../harmonyos-references/js-apis-certmanagerdialog.md#certificatemanagerdialogopenauthorizedialog22)获取。

### 在CMake脚本中链接相关动态库

```
1. target_link_libraries(entry PUBLIC libhuks_ndk.z.so libhuks_external_crypto.z.so)
```

### 开发步骤

1. 通过证书管理系统能力提供的[证书选择接口](../harmonyos-references/js-apis-certmanagerdialog.md#certificatemanagerdialogopenauthorizedialog22)获取[keyUri](../harmonyos-references/js-apis-certmanagerdialog.md#certreference22)，并将其作为resourceId。
2. 初始化参数集：通过[OH\_Huks\_InitExternalCryptoParamSet](../harmonyos-references/capi-native-huks-external-crypto-api-h.md#oh_huks_initexternalcryptoparamset)、[OH\_Huks\_AddExternalCryptoParams](../harmonyos-references/capi-native-huks-external-crypto-api-h.md#oh_huks_addexternalcryptoparams)、[OH\_Huks\_BuildExternalCryptoParamSet](../harmonyos-references/capi-native-huks-external-crypto-api-h.md#oh_huks_buildexternalcryptoparamset)构造参数集paramSet。
3. 调用[OH\_Huks\_OpenResource](../harmonyos-references/capi-native-huks-external-crypto-api-h.md#oh_huks_openresource)打开资源。

### 开发案例

```
1. #include "huks/native_huks_external_crypto_api.h"
2. #include "huks/native_huks_param.h"
3. #include "napi/native_api.h"
4. #include <string.h>

6. OH_Huks_Result InitParamSet(
7. struct OH_Huks_ExternalCryptoParamSet **paramSet,
8. const struct OH_Huks_ExternalCryptoParam *params,
9. uint32_t paramCount)
10. {
11. OH_Huks_Result ret = OH_Huks_InitExternalCryptoParamSet(paramSet);
12. if (ret.errorCode != OH_HUKS_SUCCESS) {
13. return ret;
14. }
15. ret = OH_Huks_AddExternalCryptoParams(*paramSet, params, paramCount);
16. if (ret.errorCode != OH_HUKS_SUCCESS) {
17. OH_Huks_FreeExternalCryptoParamSet(paramSet);
18. return ret;
19. }
20. ret = OH_Huks_BuildExternalCryptoParamSet(paramSet);
21. if (ret.errorCode != OH_HUKS_SUCCESS) {
22. OH_Huks_FreeExternalCryptoParamSet(paramSet);
23. return ret;
24. }
25. return ret;
26. }

28. static const char *g_resourceId = "{\"providerName\":\"testProviderName\",\"abilityName\":\"CryptoExtension\",\"bundleName\":\"com.example.cryptoapplication\",\"index\":{\"key\":\"testKey\"}}";

30. static struct OH_Huks_ExternalCryptoParam g_openResourceParamsTest[] = {};

32. static napi_value OpenResource(napi_env env, napi_callback_info info)
33. {
34. struct OH_Huks_Blob resourceId = {
35. (uint32_t)strlen(g_resourceId),
36. (uint8_t *)g_resourceId
37. };
38. struct OH_Huks_ExternalCryptoParamSet *openResourceParamSet = nullptr;
39. OH_Huks_Result ohResult;
40. do {
41. ohResult = InitParamSet(&openResourceParamSet, g_openResourceParamsTest,
42. sizeof(g_openResourceParamsTest) / sizeof(OH_Huks_ExternalCryptoParam));
43. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
44. break;
45. }
46. ohResult = OH_Huks_OpenResource(&resourceId, openResourceParamSet);
47. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
48. break;
49. }
50. } while (0);
51. OH_Huks_FreeExternalCryptoParamSet(&openResourceParamSet);

53. napi_value ret;
54. napi_create_int32(env, ohResult.errorCode, &ret);
55. return ret;
56. }
```

## 关闭资源

生态应用调用证书HAP界面，展示证书列表，用户选择证书，生态应用拿到对应的resourceId，关闭资源依赖于对应的resourceId。具体的场景介绍及规格，请参考[资源管理介绍及规格](huks-resource-management-overview.md)。

### 在CMake脚本中链接相关动态库

```
1. target_link_libraries(entry PUBLIC libhuks_ndk.z.so libhuks_external_crypto.z.so)
```

### 开发步骤

1. 通过证书管理系统能力提供的[证书选择接口](../harmonyos-references/js-apis-certmanagerdialog.md#certificatemanagerdialogopenauthorizedialog22)获取resourceId。
2. 初始化参数集：通过[OH\_Huks\_InitExternalCryptoParamSet](../harmonyos-references/capi-native-huks-external-crypto-api-h.md#oh_huks_initexternalcryptoparamset)、[OH\_Huks\_AddExternalCryptoParams](../harmonyos-references/capi-native-huks-external-crypto-api-h.md#oh_huks_addexternalcryptoparams)、[OH\_Huks\_BuildExternalCryptoParamSet](../harmonyos-references/capi-native-huks-external-crypto-api-h.md#oh_huks_buildexternalcryptoparamset)构造参数集paramSet。
3. 调用[OH\_Huks\_CloseResource](../harmonyos-references/capi-native-huks-external-crypto-api-h.md#oh_huks_closeresource)关闭资源。该接口会回调[onClearUkeyPinAuthState](../harmonyos-references/js-apis-cryptoextensionability.md#cryptoextensionabilityonclearukeypinauthstate)清理该资源关联的PIN认证状态，以及会回调[onFinishSession](../harmonyos-references/js-apis-cryptoextensionability.md#cryptoextensionabilityonfinishsession)清理该资源关联的会话handle。

### 开发案例

```
1. #include "huks/native_huks_external_crypto_api.h"
2. #include "huks/native_huks_param.h"
3. #include "huks/native_huks_type.h"
4. #include "huks/native_huks_api.h"
5. #include "napi/native_api.h"
6. #include <string.h>

8. OH_Huks_Result InitParamSet(
9. struct OH_Huks_ExternalCryptoParamSet **paramSet,
10. const struct OH_Huks_ExternalCryptoParam *params,
11. uint32_t paramCount)
12. {
13. OH_Huks_Result ret = OH_Huks_InitExternalCryptoParamSet(paramSet);
14. if (ret.errorCode != OH_HUKS_SUCCESS) {
15. return ret;
16. }
17. ret = OH_Huks_AddExternalCryptoParams(*paramSet, params, paramCount);
18. if (ret.errorCode != OH_HUKS_SUCCESS) {
19. OH_Huks_FreeExternalCryptoParamSet(paramSet);
20. return ret;
21. }
22. ret = OH_Huks_BuildExternalCryptoParamSet(paramSet);
23. if (ret.errorCode != OH_HUKS_SUCCESS) {
24. OH_Huks_FreeExternalCryptoParamSet(paramSet);
25. return ret;
26. }
27. return ret;
28. }

30. static const char *g_resourceId = "{\"providerName\":\"testProviderName\",\"abilityName\":\"CryptoExtension\",\"bundleName\":\"com.example.cryptoapplication\",\"userid\":100,\"index\":{\"key\":\"testKey\"}}";

32. static struct OH_Huks_ExternalCryptoParam g_closeResourceParamsTest[] = {};

34. static napi_value CloseResource(napi_env env, napi_callback_info info)
35. {
36. struct OH_Huks_Blob resourceId = {
37. (uint32_t)strlen(g_resourceId),
38. (uint8_t *)g_resourceId
39. };
40. struct OH_Huks_ExternalCryptoParamSet *closeResourceParamSet = nullptr;
41. OH_Huks_Result ohResult;
42. do {
43. ohResult = InitParamSet(&closeResourceParamSet, g_closeResourceParamsTest,
44. sizeof(g_closeResourceParamsTest) / sizeof(OH_Huks_ExternalCryptoParam));
45. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
46. break;
47. }
48. ohResult = OH_Huks_CloseResource(&resourceId, closeResourceParamSet);
49. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
50. break;
51. }
52. } while (0);
53. OH_Huks_FreeExternalCryptoParamSet(&closeResourceParamSet);

55. napi_value ret;
56. napi_create_int32(env, ohResult.errorCode, &ret);
57. return ret;
58. }
```
