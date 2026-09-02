---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-ukey-get-error-info-arkts
title: 获取错误信息(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 外部密钥管理扩展 > 通用操作 > 获取错误信息(ArkTS)
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:33+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:54ab38af5513c360821a2c47894a508cce4265bfed7db46aea2b5e04323f0329
---

从API版本26.0.0开始，huksExternalCrypto提供getErrorInfo接口，用于获取最近一次外部密钥操作的详细错误信息。该错误信息由密钥管理扩展（[CryptoExtensionAbility](../harmonyos-references/js-apis-cryptoextensionability.md)）返回，可用于辅助定位问题。

## 开发步骤

1. 调用外部密钥操作接口（如authUkeyPin、getProperty等）。
2. 操作失败后，调用[getErrorInfo](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalcryptogeterrorinfo)获取Extension错误信息。

## 开发案例

### Extension返回错误场景

```ts
import { huksExternalCrypto } from '@kit.UniversalKeystoreKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function testExtensionError(): Promise<void> {
  /* 1.假设已打开的资源如下 */
  const testResourceId = JSON.stringify({
    providerName: "testProviderName",
    bundleName: "com.example.cryptoapplication",
    abilityName: "CryptoExtension",
    index: "testKey"
  });

  /* 2.构造参数 */
  const pin = "123456";
  const params: Array<huksExternalCrypto.HuksExternalCryptoParam> = [
    {
      tag: huksExternalCrypto.HuksExternalCryptoTag.HUKS_EXT_CRYPTO_TAG_UKEY_PIN,
      value: StringToUint8Array(pin)
    }
  ];
  
  /* 3.验证PIN码失败后获取错误信息 */
  try {
    await huksExternalCrypto.authUkeyPin(testResourceId, params);
  } catch (error) {
    const errorInfo = huksExternalCrypto.getErrorInfo();
    if (errorInfo.errno !== 0) {
      console.info(`Extension error code: ${errorInfo.errno}`);
      console.info(`Extension error desc: ${errorInfo.errorDesc}`);
    }
  }
}
```

## 错误信息更新规则

| 场景 | errno | errorDesc |
| --- | --- | --- |
| 密钥管理扩展返回错误信息 | 具体错误码（非0） | 扩展返回的描述（可能为空） |
| 密钥管理扩展未返回错误信息 | 默认值0或保持上次 | 默认值空字符串或保持上次 |

## 注意事项

1. 此接口仅返回密钥管理扩展的详细错误信息，HUKS内部错误通过接口异常抛出。
2. 当密钥管理扩展未返回详细错误信息时（errno为0），errorDesc为空字符串，开发者应通过接口异常的错误码判断错误原因。
3. 建议在操作失败后立即调用getErrorInfo获取详细错误信息。errno非0时，表示扩展返回了错误信息，开发者应优先使用errno定位问题。
4. 错误信息覆盖范围：authUkeyPin、getUkeyPinAuthState、getProperty、setProperty、openResource、closeResource、clearUkeyPinAuthState、getResourceId等接口。
