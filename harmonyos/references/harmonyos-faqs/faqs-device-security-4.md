---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-device-security-4
title: 使用ArkTS语言完成JWT鉴权令牌
breadcrumb: FAQ > 系统开发 > 安全 > 设备安全服务（Device Security） > 使用ArkTS语言完成JWT鉴权令牌
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:13+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:01ed61a7850e2ef2d73662b57844058dfa22b3c59dbe9e4db3da7f16977f6e60
---

## 问题现象

请问在应用设备状态检测这块功能里，在签名的这一步报错了，生成鉴权令牌中的签名该如何用ArkTS实现？

## 背景知识

[基于服务账号生成鉴权令牌](../harmonyos-guides/devicesecurity-deviceverify-token.md)：使用应用设备状态检测服务时需要配置此章节。

## 解决方案

将完成BASE64编码后的Header字符串与Payload字符串，通过“.”进行连接，并在开发者的应用中，通过服务账号密钥文件中的private\_key（华为不进行存储，请您妥善保管），使用SHA256withRSA/PSS算法对拼接的字符串签名，最后将Header，Payload以及字符串签名通过“.”进行连接，即可得到Token数据。

```ts
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer, util } from '@kit.ArkTS';

let base64 = new util.Base64Helper();

// 生成header
function genHeader(keyId: string): string {
  const jwtHeader: object = new Object({
    'kid': keyId,
    'typ': 'JWT',
    'alg': 'PS256'
  });
  let strArray = new Uint8Array(buffer.from(JSON.stringify(jwtHeader)).buffer);
  return base64.encodeToStringSync(strArray, util.Type.BASIC_URL_SAFE);
}

// 生成payload
function genPayload(subAccount: string): string {
  const now: number = Date.now();
  const jwtPayload: object = new Object({
    'aud': '*****',
    'iss': subAccount,
    'iat': now,
    'exp': now + 3600 * 1000,
  });
  let strArray = new Uint8Array(buffer.from(JSON.stringify(jwtPayload)).buffer);
  return base64.encodeToStringSync(strArray, util.Type.BASIC_URL_SAFE);
}

async function pss(priKey: string, str: string) {
  let asyKeyGenerator = cryptoFramework.createAsyKeyGenerator('RSA2048');
  let keyPair = asyKeyGenerator.convertPemKeySync(null, priKey);

  let signer = cryptoFramework.createSign('RSA2048|PSS|SHA256|MGF1_SHA256');
  await signer.init(keyPair.priKey);
  signer.setSignSpec(cryptoFramework.SignSpecItem.PSS_SALT_LEN_NUM, 32);
  let signData = await signer.sign({ data: new Uint8Array(buffer.from(str).buffer) });
  return signData.data;
}

export async function main() {
  // 服务账号密钥，需要根据教程使用自己的密钥
  const privateJson: object = new Object({
    'project_id': '*****',
    'key_id': '*****',
    'private_key': '*****',
    'sub_account': '*****',
    'auth_uri': '*****',
    'token_uri': '*****',
    'auth_provider_cert_uri': '*****',
    'client_cert_uri': '*****'
  });
  let header = genHeader(privateJson['key_id']);
  let payload = genPayload(privateJson['sub_account']);
  let hap = header + '.' + payload;
  let signature = await pss(privateJson['private_key'], hap);
  let token = hap + '.' + base64.encodeToStringSync(signature, util.Type.BASIC_URL_SAFE);
  console.info(token);
}
@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text('HelloWorld')
        .fontSize($r('app.float.page_text_font_size'))
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          main();
        });
    }
    .height('100%')
    .width('100%');
  }
}
```

**说明** 

鉴权json字段是固定的，无法更改，取用也是需要用json格式。
