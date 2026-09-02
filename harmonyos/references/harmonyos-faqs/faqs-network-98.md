---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-98
title: 如何解决给HTTP请求添加本地的.cer证书问题
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > 如何解决给HTTP请求添加本地的.cer证书问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:37+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:e04873e1e7ca427af64ac2fa2a40c4501ca6876057d3b834fe4a2b892ff6dc46
---

## 问题现象

如何实现给HTTP请求添加本地的root.cer证书？

## 背景知识

* .cer文件是一种常用的证书格式，用于在HarmonyOS和其他系统中配置签名信息。这种证书包含公钥和证书指纹（即证书的摘要信息），主要用于保障软件代码的完整性和发布者身份的真实性。
* PEM（Privacy Enhanced Mail）证书是一种用于加密和解密数据的证书格式，广泛应用于HTTPS、SSH等安全协议中。PEM格式的证书包含公钥和签名，用于验证网站或其他实体的身份。这种证书是文本格式，以“-----BEGIN CERTIFICATE-----”开始，并以“-----END CERTIFICATE-----”结束。

  在HarmonyOS开发中，PEM证书也可能用于安全相关的配置，例如在配置HTTP请求时，如果需要进行证书验证，可以通过PEM格式的证书来实现。具体来说，开发者可以将PEM证书通过特定的命令上传到设备，并在代码中使用这些证书来进行加密或验证操作。

## 解决方案

目前可以使用如下方案：

* 步骤一：将.cer文件转换为PEM格式，因为HTTP请求中支持的是PEM格式的证书。开发者可以使用以下命令进行格式转换：

  openssl x509 -inform der -in yourcertificate.cer -out yourcertificate.pem。
* 步骤二：在HTTP中使用：
  + 可以将证书放入根证书同级目录下如“/etc/ssl/certs/cacert1.pem”，将该路径设置到[caPath参数](../harmonyos-references/js-apis-http.md#httprequestoptions)。

    命令如下：

    hdc file send testCert.pem（PC上证书路径）/etc/ssl/certs/testCert.pem(证书默认沙箱路径)。
  + 从代码层面设置写入证书文件，首先将证书放入项目rawfile资源目录下，然后将代码生成写入的filePath参数设置到请求中caPath，关键代码如下：

```screen
import fs from '@ohos.file.fs';
import { http } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct HttpRootCerPage {
  requestHttp(url: string): Promise<string> {
    let context = this.getUIContext()?.getHostContext() as common.Context;
    context.area = 0;
    const keyPem = context.resourceManager.getRawFileContentSync('_.cnfic.com.cn.pem');
    let filesDir: string = context.filesDir;
    let filePath = filesDir + "/testCer2.pem";
    let file = fs.openSync(filePath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
    fs.writeSync(file.fd, keyPem.buffer);
    fs.fsyncSync(file.fd);
    fs.closeSync(file);
    return new Promise(() => {
      let httpRequest = http.createHttp();
      httpRequest.request(url, {
        method: http.RequestMethod.GET,
        caPath: filePath,
        connectTimeout: 60000,
        readTimeout: 60000,
      }, (err: BusinessError, data) => {
        console.info(`1---- url: ${JSON.stringify(url)}`);
        if (!err) {
          // data.result为HTTP响应内容，可根据业务需要进行解析
          console.info(`1---- arrResult: ${JSON.stringify(data.result)}`);
          console.info(`1---- code: ${JSON.stringify(data.responseCode)}`);
          console.info(`1---- type: ${JSON.stringify(data.resultType)}`);
          console.info(`1---- header: ${JSON.stringify(data.header)}`);
          console.info(`1---- cookies: ${JSON.stringify(data.cookies)}`);
          console.info(`1 ---------------------------------------------`);
          httpRequest.destroy();
        } else {
          console.error(`1---- error: ${JSON.stringify(err)}`);
          console.info(`1 ---------------------------------------------`);
          httpRequest.destroy();
        }
      });
    });
  }

  build() {
    Column() {
      Button('testButton')
        .height(50)
        .width(80)
        .onClick(() => {
          this.requestHttp('url');
        })
    }.height('100%')
  }
}
```
