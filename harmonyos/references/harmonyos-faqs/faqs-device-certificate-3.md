---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-device-certificate-3
title: 如何解决x509Cert证书获取SN号与预期结果不一致的问题
breadcrumb: FAQ > 系统开发 > 安全 > 证书管理（Device Certificate） > 如何解决x509Cert证书获取SN号与预期结果不一致的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:35+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f0f14296b39d299e0e3428ba5f9218729571ddd5deddd532a55ddb37366fa57d
---

## 问题现象

x509Cert证书获取SN号与预期结果不一致是什么原因？

示例代码：

```ts
import cert from '@ohos.security.cert';
import { BusinessError } from '@ohos.base';

function getCertDetails() {
  // 证书二进制数据，需业务自行赋值，下为示例，代码运行需要自行填充
  let certData = '-----BEGIN CERTIFICATE-----\r\n' +
      'MIIDTjCCAjagAwIBAgIBBDANBgkqhkiG9w0BAQsFADASMRAwDgYDVQQDDAdSb290\n' +
      'IENBMB4XDTI0MDMxOTAyMDQwMVoXDTM0MDMxNzAyMDQwMVowEjEQMA4GA1UEAwwH\n' +
      'ZGV2aWNlMjCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAMIXL3e7UE/c\n' +
      'Z1dPVgRZ5L8gsQ/azuYVBvoFf7o8ksYrL7G1+qZIJjVRqZkuTirLW4GicbkIkPNW\n' +
      'eix5cDhkjkC+q5SBCOrSSTTlvX3xcOY1gMlA5MgeBfGixFusq4d5VPF2KceZ20/a\n' +
      'ygwGD0Uv0X81OERyPom/dYdJUvfaD9ifPFJ1fKIj/cPFG3yJK/ojpEfndZNdESQL\n' +
      'TkoDekilg2UGOLtY6fb9Ns37ncuIj33gCS/R9m1tgtmqCTcgOQ4hwKhjVF3InmPO\n' +
      '2BbWKvD1RUX+rHC2a2HHDQILOOtDTy8dHvE+qZlK0efrpRgoFEERJAGPi1GDGWiA\n' +
      '7UX1c4MCxIECAwEAAaOBrjCBqzAJBgNVHRMEAjAAMB0GA1UdDgQWBBQbkAcMT7ND\n' +
      'fGp3VPFzYHppZ1zxLTAfBgNVHSMEGDAWgBR0W/koCbvDtFGHUQZLM3j6HKsW2DAd\n' +
      'BgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwCwYDVR0PBAQDAgeAMDIGCCsG\n' +
      'AQUFBwEBBCYwJDAiBggrBgEFBQcwAYYWaHR0cHM6Ly8xMjcuMC4wLjE6OTk5OTAN\n' +
      'BgkqhkiG9w0BAQsFAAOCAQEAF1OTzTmbklFOdZCxrF3zg9owUPJR5RB+PbuBlUfI\n' +
      '8tkGXkMltQ8PN1dv6Cq+d8BluiJdWEzqVoJa/e5SHHJyYQSOhlurRG0GBXllVQ1I\n' +
      'n1PFaI40+9X2X6wrEcdC5nbzogR1jSiksCiTcARMddj0Xrp5FMrFaaGY8M/xqzdW\n' +
      'LTDl4nfbuxtA71cIjnE4kOcaemly9/S2wYWdPktsPxQPY1nPUOeJFI7o0sH3rK0c\n' +
      'JSqtgAG8vnjK+jbx9RpkgqCsXgUbIahL573VTgxrNrsRjCuVal7XVxl/xOKXr6Er\n' +
      'Gpc+OCrXbHNZkUQE5fZH3yL2tXd7EASEb6J3aEWHfF8YBA==\n' +
      '-----END CERTIFICATE-----';
  let encodingBlob: cert.EncodingBlob = {
    data: stringToUint8Array(certData),
    // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER
    encodingFormat: cert.EncodingFormat.FORMAT_PEM
  };
  // 创建X509Cert实例
  cert.createX509Cert(encodingBlob, (error, x509Cert) => {
    if (error) {
      hilog.error(0x0000, 'test', `errMsg: ${error.message}`);
    } else {
      hilog.info(0x0000, 'test', 'createX509Cert success');
      try {
        let serialNumber = x509Cert.getCertSerialNumber().toString();
        hilog.info(0x0000, 'test', `sn: ${serialNumber}`)
      } catch (err) {
        let e: BusinessError = err as BusinessError;
        hilog.error(0x0000, 'test', `errMsg: ${e.message}`);
      }
    }
  });
}

// string转Uint8Array
function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}
```

预期结果：

```shell
2911000000000006
```

实际结果：

```shell
2959146430159126534
```

## 背景知识

* 创建X509证书对象：[cert.createX509Cert](../harmonyos-references/js-apis-cert.md#certcreatex509cert)。
* 获取X509证书序列号：[x509Cert.getCertSerialNumber()](../harmonyos-references/js-apis-cert.md#getcertserialnumber10)。

## 问题定位

1. 获取的SN号不符合预期数据，可以先打印证书的所有数据。
2. 可以看到证书信息Certificate:下有个Serial Number参数，此为需要获取的数据。
3. 可以看到数据是Serial Number: 2959146430159126534 (0x2911000000000006)，有2个数据，前面为输出结果数据，后面为预期数据且有0x开头，说明预期数据是16进制的SN号数据。

   ```shell
   Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number: 2959146430159126534 (0x2911000000000006)
   ```

4. 最终可以确认getCertSerialNumber()获取的是前面的10进制数据，而预期获取的是后面的16进制数据。

## 分析结论

getCertSerialNumber()获取的是前面的10进制数据，而预期获取的是后面的16进制数据，想要获取到预期数据需要进行进制转换。

## 修改建议

使用x509Cert.getCertSerialNumber()方法获取SN号时，用toString(16)方法将数据转换为16进制。

示例代码：

```screen
import cert from '@ohos.security.cert';
import { BusinessError } from '@ohos.base';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct X509Cert {
  @State sn: string = '';

  getCertDetails() {
    // 证书二进制数据，需业务自行赋值，下为占位格式示例，代码运行需要自行填充
    let certData = '-----BEGIN CERTIFICATE-----\r\n' +
      'MIIDTjCCAjagAwIBAgIBBDANBgkqhkiG9w0BAQsFADASMRAwDgYDVQQDDAdSb290\n' +
      'IENBMB4XDTI0MDMxOTAyMDQwMVoXDTM0MDMxNzAyMDQwMVowEjEQMA4GA1UEAwwH\n' +
      'ZGV2aWNlMjCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAMIXL3e7UE/c\n' +
      'Z1dPVgRZ5L8gsQ/azuYVBvoFf7o8ksYrL7G1+qZIJjVRqZkuTirLW4GicbkIkPNW\n' +
      'eix5cDhkjkC+q5SBCOrSSTTlvX3xcOY1gMlA5MgeBfGixFusq4d5VPF2KceZ20/a\n' +
      'ygwGD0Uv0X81OERyPom/dYdJUvfaD9ifPFJ1fKIj/cPFG3yJK/ojpEfndZNdESQL\n' +
      'TkoDekilg2UGOLtY6fb9Ns37ncuIj33gCS/R9m1tgtmqCTcgOQ4hwKhjVF3InmPO\n' +
      '2BbWKvD1RUX+rHC2a2HHDQILOOtDTy8dHvE+qZlK0efrpRgoFEERJAGPi1GDGWiA\n' +
      '7UX1c4MCxIECAwEAAaOBrjCBqzAJBgNVHRMEAjAAMB0GA1UdDgQWBBQbkAcMT7ND\n' +
      'fGp3VPFzYHppZ1zxLTAfBgNVHSMEGDAWgBR0W/koCbvDtFGHUQZLM3j6HKsW2DAd\n' +
      'BgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwCwYDVR0PBAQDAgeAMDIGCCsG\n' +
      'AQUFBwEBBCYwJDAiBggrBgEFBQcwAYYWaHR0cHM6Ly8xMjcuMC4wLjE6OTk5OTAN\n' +
      'BgkqhkiG9w0BAQsFAAOCAQEAF1OTzTmbklFOdZCxrF3zg9owUPJR5RB+PbuBlUfI\n' +
      '8tkGXkMltQ8PN1dv6Cq+d8BluiJdWEzqVoJa/e5SHHJyYQSOhlurRG0GBXllVQ1I\n' +
      'n1PFaI40+9X2X6wrEcdC5nbzogR1jSiksCiTcARMddj0Xrp5FMrFaaGY8M/xqzdW\n' +
      'LTDl4nfbuxtA71cIjnE4kOcaemly9/S2wYWdPktsPxQPY1nPUOeJFI7o0sH3rK0c\n' +
      'JSqtgAG8vnjK+jbx9RpkgqCsXgUbIahL573VTgxrNrsRjCuVal7XVxl/xOKXr6Er\n' +
      'Gpc+OCrXbHNZkUQE5fZH3yL2tXd7EASEb6J3aEWHfF8YBA==\n' +
      '-----END CERTIFICATE-----';
    let encodingBlob: cert.EncodingBlob = {
      data: this.stringToUint8Array(certData),
      // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER
      encodingFormat: cert.EncodingFormat.FORMAT_PEM
    };
    // 创建X509Cert实例
    cert.createX509Cert(encodingBlob, (error, x509Cert) => {
      if (error) {
        hilog.error(0x0000, 'test', 'createX509Cert failed, errCode: ' + error.code + ', errMsg: ' + error.message);
      } else {
        hilog.info(0x0000, 'test', 'createX509Cert success');
        hilog.info(0x0000, 'test', x509Cert.toString());
        try {
          let serialNumber = x509Cert.getCertSerialNumber().toString(16);
          this.sn = serialNumber;
          hilog.info(0x0000, 'test', `sn: ${serialNumber}`);
        } catch (err) {
          let e: BusinessError = err as BusinessError;
          hilog.error(0x0000, 'test', 'getCertSerialNumber failed, errCode: ' + e.code + ', errMsg: ' + e.message);
        }
      }
    });
  }

  // string转Uint8Array
  stringToUint8Array(str: string): Uint8Array {
    let arr: Array<number> = [];
    for (let i = 0, j = str.length; i < j; i++) {
      arr.push(str.charCodeAt(i));
    }
    return new Uint8Array(arr);
  }

  build() {
    Column({ space: 20 }) {
      Text('点击获取SN')
        .fontSize(30)
        .onClick(() => {
          this.getCertDetails();
        });
      Text(this.sn)
        .fontSize(16);
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center);
  }
}
```

## 总结

对于获取X509Cert对象的某一条数据，不符合预期结果时，可以将X509Cert对象的所有数据都打印出来，查看数据进行比对分析。
