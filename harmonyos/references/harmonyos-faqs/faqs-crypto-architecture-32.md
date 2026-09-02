---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-crypto-architecture-32
title: 如何校验文件一致性
breadcrumb: FAQ > 系统开发 > 安全 > 加解密算法（Crypto Architecture） > 如何校验文件一致性
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:34+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f09901af976fc9f987bc7fb5b0e3a1247ea616d51ed0eb86866c2f2a5c9efc23
---

## 问题现象

如何通过计算文件的MD5值校验文件的一致性？

## 背景知识

* 文件一致性最基础的要求是两个或多个文件的内容完全一致，即字节级相同。例如，在电子物证检验中，通过计算文件的哈希值（如MD5、SHA-256）验证数据是否相同。ArkTS当中MD5计算可参考[消息摘要计算MD5](../harmonyos-guides/crypto-generate-message-digest-md5.md)。
* [@ohos.request (上传下载)](../harmonyos-references/js-apis-request.md)：request模块给应用提供上传下载文件、后台代理传输的基础功能。
* [应用文件上传下载](../harmonyos-guides/app-file-upload-download.md)：应用可以将应用文件上传到网络服务器，也可以从网络服务器下载网络资源文件到本地应用文件目录。

## 解决方案

通过对比两个文件MD5值是否相同，从而判断文件是否一致，方案如下：

1. 调用[cryptoFramework.createMd](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatemd)，指定摘要算法MD5，生成摘要实例。
2. 传入自定义消息，将一次传入数据量设置为20字节，多次调用[Md.update](../harmonyos-references/js-apis-cryptoframework.md#update-6)，进行摘要更新计算。
3. 调用[Md.digest](../harmonyos-references/js-apis-cryptoframework.md#digest)，获取摘要计算结果。

```ts
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { fileIo as fs } from '@kit.CoreFileKit';
import { buffer } from '@kit.ArkTS';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct VerifyingFile {
  build() {
    RelativeContainer() {
      Text('校验文件一致性')
        .fontSize($r('app.float.page_text_font_size'))
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(async () => {
          // 通过计算文件MD5值判断两个文件是否相同
          // 假设应用沙箱里面的文件目录(context.filesDir)存在两个文本文件test1.txt、test2.txt。
          let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
          let path1 = `${context.filesDir}/test1.txt`;
          let path2 = `${context.filesDir}/test2.txt`;
          let file1MD5 = await this.calFileMd5(path1);
          let file2MD5 = await this.calFileMd5(path2);
          console.info(`${file1MD5 === file2MD5 ? '是同一个文件' : '不是同一个文件'}`);
        })
    }
    .height('100%')
    .width('100%')
  }

  async calFileMd5(fileUrl: string) {
    let calFileMd5: string | undefined;
    try {
      let md = cryptoFramework.createMd('MD5');
      let file = fs.openSync(fileUrl, fs.OpenMode.READ_ONLY);
      let arrayBuffer = new ArrayBuffer(2048);
      let len: number = 0;
      let position: number = 0;
      do {
        len = fs.readSync(file.fd, arrayBuffer, { offset: position });
        if (len > 0) {
          let uint8Array = new Uint8Array(arrayBuffer.slice(0, len));
          let updateMessageBlob: cryptoFramework.DataBlob = { data: uint8Array };
          await md.update(updateMessageBlob);
          position += len;
        }
      } while (len > 0);
      fs.closeSync(file);
      let mdOutput = await md.digest();
      calFileMd5 = buffer.from(mdOutput.data).toString('hex');
    } catch (error) {
      console.error(JSON.stringify(error));
    }
    return calFileMd5;
  }
}
```

## 常见FAQ

Q：除了将文件分段读取从而计算MD5这种方式，还有其他方式可以用于验证文件的一致性吗？

A：ArkTS提供了[文件哈希处理](../harmonyos-references/js-apis-file-hash.md)能力，API更简洁，内存消耗更低。
