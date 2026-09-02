---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-device-security-5
title: 系统安全性检测
breadcrumb: FAQ > 系统开发 > 安全 > 设备安全服务（Device Security） > 系统安全性检测
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:35+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:d32b15e5a27897c420d08795df60883b197a0847a72d45972c8881265f2597e1
---

## 问题现象

当前使用系统安全性检测的日志结果并不符合接口文档预期，另外，是否可以在客户端解析JWS？

## 背景知识

[系统完整性检测](../harmonyos-guides/devicesecurity-sysintegrity-check.md)：应用通过调用Device Security Kit的checkSysIntegrity接口获取系统完整性检测结果，用于判断设备环境是否安全，比如是否被越狱、被模拟等。

## 问题定位

根据系统完整性检测[开发步骤](../harmonyos-guides/devicesecurity-sysintegrity-check.md#开发步骤)打印result，日志格式如下：\*\*\*\*\*\*.\*\*\*\*\*\*\*\*\*，复现问题。对日志内容进行Base64解码，结果为Header的一部分。

## 分析结论

由于日志打印长度有限，result内容被日志截断，所以日志里面的result确实不符合预期，但是可以直接对result进行解析，符合官网结果预期。

## 修改建议

直接对返回结果进行解析，分段打印，可以避免日志内容被截断。以下为客户端直接解析JWS的核心判断逻辑，可根据需求添加相应的业务代码：

```ts
import { safetyDetect } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@ohos.base';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { JSON, util } from '@kit.ArkTS';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

let base64 = new util.Base64Helper();
const TAG = 'SafetyDetectJsTest';

class Payload {
  hapCertificateSha256: string = '';
  hapBundleName: string = '';
  appId: string = '';
  basicIntegrity: boolean = false;
  nonce: boolean = false;
  timestamp: number = 0;
  detail: Array<string> = [];
}

function checkSysIntegrityPromise(): Promise<String> {
  return new Promise(async (resolve, reject) => {
    let strLen: number = 16;
    let srcStr: string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhijklmnopqrstuvwxyz0123456789';
    let randomStr: string = '';
    let rand = cryptoFramework.createRandom();
    for (let i = 0; i < strLen; i++) {
      let randData = rand.generateRandomSync(1);
      randomStr += srcStr.charAt(Math.floor(randData.data[0] * srcStr.length / 255));
    }
    let sysIntegrityRequest: safetyDetect.SysIntegrityRequest = {
      nonce: randomStr
    };
    try {
      hilog.info(0x0000, TAG, 'CheckSysIntegrity begin.');
      let sysIntegrityResponse: safetyDetect.SysIntegrityResponse =
        await safetyDetect.checkSysIntegrity(sysIntegrityRequest);
      let result: string = sysIntegrityResponse.result;
      resolve(result);
      hilog.info(0x0000, TAG, 'Succeeded in checkSysIntegrity: %{public}s', result);
    } catch (err) {
      hilog.error(0x0000, TAG, 'CheckSysIntegrity failed: %{public}d %{public}s', err.code, err.message);
      reject(err);
    }
  });
}

async function analysis(): Promise<boolean> {
  // 请求系统完整性检测，并处理结果
  let ret = false;
  await checkSysIntegrityPromise().then((result) => {
    let resultArray: string[] = result.split('.');

    // 解析JWS，获取header、payload、signature。
    let headerUint = base64.decodeSync(resultArray[0], util.Type.BASIC_URL_SAFE);
    let decoder = util.TextDecoder.create('utf-8');
    let headerStr = decoder.decodeToString(headerUint);
    hilog.info(0x0000, TAG, 'analysis Succeeded in Header: %{public}s', headerStr);

    let payloadUint = base64.decodeSync(resultArray[1], util.Type.BASIC_URL_SAFE);
    let payloadStr = decoder.decodeToString(payloadUint);
    hilog.info(0x0000, TAG, 'analysis Succeeded in Payload: %{public}s', payloadStr);
    let payload: Payload = JSON.parse(payloadStr) as Payload;
    ret = payload.basicIntegrity;

    let signatureUint = base64.decodeSync(resultArray[2], util.Type.BASIC_URL_SAFE);
    let signatureStr = decoder.decodeToString(signatureUint);
    hilog.info(0x0000, TAG, 'analysis Succeeded in Signature: %{public}s', signatureStr);

  }).catch((err: BusinessError) => {
    ret = false;
    hilog.error(0x0000, TAG, 'analysis failed: %{public}d %{public}s', err.code, err.message);
  });
  return ret;
}

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Button('检测系统完整性')
        .onClick(async () => {
          let ret = await analysis();
          hilog.info(0x0000, TAG, 'Succeeded in Signature: %{public}s', ret);
        });
    }
    .height('100%')
    .width('100%');
  }
}
```

其中result为eyAgICAiYW\*\*.\*\*.\*Jxse，split分离三段数据后可解析出Header（头部），Payload（负载），Signature（签名）。

## 总结

发现日志过长时可考虑日志不全的情况。
