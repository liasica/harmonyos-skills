---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-crypto-architecture-52
title: 如何解决对文件进行SM3摘要计算结果错误的问题
breadcrumb: FAQ > 系统开发 > 安全 > 加解密算法（Crypto Architecture） > 如何解决对文件进行SM3摘要计算结果错误的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:35+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:6d53a39e41983c64105634b558ad8aa2eed584a3f6a4e712fd430cd52cc76e77
---

## 问题现象

对目标文件进行SM3摘要计算，计算结果错误。这是什么原因导致，该如何解决？

示例代码：

```typescript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { ReadOptions } from '@kit.CoreFileKit';
import { buffer } from '@kit.ArkTS';
import { fileIo as fs } from '@kit.CoreFileKit';

/**
 * 计算文件SM3
 * @param filePath 文件路径
 * @returns string 摘要数据
 */
function fileSM3(filePath: string): string {
  if (!fs.accessSync(filePath)) {
    // 如果文件不存在，则返回空字符
    return ''
  }
  // 定义摘要类型
  let md = cryptoFramework.createMd('SM3')
  // 打开文件
  let file = fs.openSync(filePath, fs.OpenMode.READ_ONLY)
  let fileBufferSize = 4096
  let readSize = 0
  let fileBuffer = new ArrayBuffer(fileBufferSize)
  let readOptions: ReadOptions = {
    offset: readSize,
    length: fileBufferSize
  }
  let readLength = fs.readSync(file.fd, fileBuffer, readOptions)
  while (readLength > 0) {
    // 更新摘要数据
    md.updateSync({
      data: new Uint8Array(fileBuffer)
    });
    readSize += readLength
    readOptions.offset = readSize;
    readLength = fs.readSync(file.fd, fileBuffer, readOptions);
  }
  // 计算摘要数据
  let mdResult = md.digestSync()
  return buffer.from(mdResult.data).toString('hex')
}
```

待摘要文件名为demoTest.docx，文件内容为demoTest，此为测试文件。

预期SM3摘要数据结果：

```txt
bdf367286a0458f6a6b3698cb2bfa0cf27ed139a6c9ba08addf3c009177e81ce
```

实际SM3摘要数据结果：

```txt
b7e3771fdae3feb2c70d47edd2093cbe533382109ab223d41678d0eb525f731d
```

## 背景知识

消息摘要算法是一种能将任意长度的输入消息，通过特定运算生成固定长度摘要的算法。消息摘要算法也被称为哈希算法或单向散列算法。在摘要算法相同时，生成的摘要值主要有下列特点：

* 当输入消息相同时，生成摘要序列相同。
* 当输入消息的长度不一致时，生成摘要序列长度固定（摘要长度由算法决定）。

[@ohos.file.fs](../harmonyos-references/js-apis-file-fs.md)模块为基础文件操作API，提供基础文件操作能力，包括文件基本管理、文件目录管理、文件信息统计、文件流式读写等常用功能。

* 以同步方法打开文件或目录：[fs.openSync](../harmonyos-references/js-apis-file-fs.md#fileioopensync)。
* 以同步方法从文件读取数据：[fs.readSync](../harmonyos-references/js-apis-file-fs.md#fileioreadsync)。

## 问题定位

1. 文件摘要数据成功计算，结果与预期不一致，表明中间数据有问题，首先检查文件数据是否成功读取完毕。
2. SM3摘要数据为分段导入，检查摘要数据是否全部导入成功。
3. SM3分段导入数据长度为fileBufferSize参数固定设置，检查是否额外导入fileBuffer多余数据。

## 分析结论

SM3分段导入数据fileBuffer长度为fileBufferSize参数固定设置，但因为读取的文件数据长度不是fileBufferSize参数的整数倍，最后一段应该导入的摘要数据长度不等于fileBufferSize参数，所以最后一段摘要数据导入错误，从而导致最终摘要结果与预期不符。

## 修改建议

动态传入每次需要进行摘要的数据长度，长度值readLength为每一段所导入文件的长度数据，这样可以避免传入未被写入fileBuffer中的数据。

对fileBuffer数据进行传入数据readLength长度的截取，最终运行结果符合预期，代码示例如下：

```typescript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { ReadOptions } from '@kit.CoreFileKit';
import { buffer } from '@kit.ArkTS';
import { fileIo as fs } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';

/**
 * 计算文件SM3
 * @param filePath 文件路径
 * @returns string 摘要数据
 */
function fileSM3(filePath: string): string {
  if (!fs.accessSync(filePath)) {
    // 如果文件不存在，则返回空字符
    return '';
  }
  // 定义摘要类型
  let md = cryptoFramework.createMd('SM3');
  // 打开文件
  let file = fs.openSync(filePath, fs.OpenMode.READ_ONLY);
  let fileBufferSize = 4096;
  let readSize = 0;
  let fileBuffer = new ArrayBuffer(fileBufferSize);
  let readOptions: ReadOptions = {
    offset: readSize,
    length: fileBufferSize
  };
  let readLength = fs.readSync(file.fd, fileBuffer, readOptions);
  while (readLength > 0) {
    // 更新摘要数据
    md.updateSync({
      data: new Uint8Array(fileBuffer.slice(0, readLength))
    });
    readSize += readLength;
    readOptions.offset = readSize;
    readLength = fs.readSync(file.fd, fileBuffer, readOptions);
  }
  // 计算摘要数据
  let mdResult = md.digestSync();
  return buffer.from(mdResult.data).toString('hex');
}
```

附加内容：

可以在rawfile同级目录下创建resfile目录，将测试文件放入resfile目录下，通过上下文获取文件目录，示例代码如下：

```typescript
// 获取上下文
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let resourceDir = context.resourceDir;
/*demoTest.docx是resources/resfile中文件的名称
此时resourceDirTest就能拿到resfile文件夹文件的路径
沙箱路径日志为/data/storage/el1/bundle/entry/resources/resfile/demoTest.docx*/
let resourceDirTest = resourceDir + '/demoTest.docx';
console.info(fileSM3(resourceDirTest));
```

完整示例代码如下：

```typescript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { ReadOptions } from '@kit.CoreFileKit';
import { buffer } from '@kit.ArkTS';
import { fileIo as fs } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';

/**
 * 计算文件SM3
 * @param filePath 文件路径
 * @returns string 摘要数据
 */
function fileSM3(filePath: string): string {
  if (!fs.accessSync(filePath)) {
    // 如果文件不存在，则返回空字符
    return '';
  }
  // 定义摘要类型
  let md = cryptoFramework.createMd('SM3');
  // 打开文件
  let file = fs.openSync(filePath, fs.OpenMode.READ_ONLY);
  let fileBufferSize = 4096;
  let readSize = 0;
  let fileBuffer = new ArrayBuffer(fileBufferSize);
  let readOptions: ReadOptions = {
    offset: readSize,
    length: fileBufferSize
  };
  let readLength = fs.readSync(file.fd, fileBuffer, readOptions);
  while (readLength > 0) {
    // 更新摘要数据
    md.updateSync({
      data: new Uint8Array(fileBuffer.slice(0, readLength))
    });
    readSize += readLength;
    readOptions.offset = readSize;
    readLength = fs.readSync(file.fd, fileBuffer, readOptions);
  }
  // 计算摘要数据
  let mdResult = md.digestSync();
  return buffer.from(mdResult.data).toString('hex');
}

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Button('SM3')
        .fontSize($r('app.float.page_text_font_size'))
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          // 获取上下文
          let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
          let resourceDir = context.resourceDir;
          /*demoTest.docx是resources/resfile中文件的名称
          此时resourceDirTest就能拿到resfile文件夹文件的路径
          沙箱路径日志为/data/storage/el1/bundle/entry/resources/resfile/demoTest.docx*/
          let resourceDirTest = resourceDir + '/demoTest.docx';
          console.info(fileSM3(resourceDirTest));
        });
    }
    .height('100%')
    .width('100%');
  }
}
```

## 常见FAQ

Q：cryptoFramework.createMd使用SHA512得到结果与服务端不一致。

A：使用上述代码，SM3改为SHA512，得到的结果与服务端一致。

## 总结

在进行数据处理时，除却注意数据格式的不同，还要注意数据长度是否对结果有影响。
