---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-file-access
title: 应用文件访问(ArkTS)
breadcrumb: 指南 > 应用框架 > Core File Kit（文件基础服务） > 应用文件 > 应用文件访问与管理 > 应用文件访问(ArkTS)
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:24+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:7a5e561a3190c1a93db94d6f5be5d703dd8b230e8b3598e0d09c8ccda1d7a37d
---

应用需要对应用文件目录下的应用文件进行查看、创建、读写、删除、移动、复制、获取属性等访问操作，下文介绍具体方法。

## 接口说明

开发者通过基础文件操作接口（[ohos.file.fs](../harmonyos-references/js-apis-file-fs.md)）实现应用文件访问能力，主要功能如下表所示。

**表1** 基础文件操作接口功能，其中“√”表示支持，“-”表示不区分同步和异步。

| 接口名 | 功能 | 接口类型 | 支持同步 | 支持异步 |
| --- | --- | --- | --- | --- |
| access | 检查文件是否存在 | 方法 | √ | √ |
| close | 关闭文件 | 方法 | √ | √ |
| copyFile | 复制文件 | 方法 | √ | √ |
| createStream | 基于文件路径打开文件流 | 方法 | √ | √ |
| listFile | 列出文件夹下所有文件名 | 方法 | √ | √ |
| mkdir | 创建目录 | 方法 | √ | √ |
| moveFile | 移动文件 | 方法 | √ | √ |
| open | 打开文件 | 方法 | √ | √ |
| read | 从文件读取数据 | 方法 | √ | √ |
| rename | 重命名文件或文件夹 | 方法 | √ | √ |
| rmdir | 删除整个目录 | 方法 | √ | √ |
| stat | 获取文件详细属性信息 | 方法 | √ | √ |
| unlink | 删除单个文件 | 方法 | √ | √ |
| write | 将数据写入文件 | 方法 | √ | √ |
| Stream.close | 关闭文件流 | 方法 | √ | √ |
| Stream.flush | 刷新文件流 | 方法 | √ | √ |
| Stream.write | 将数据写入流文件 | 方法 | √ | √ |
| Stream.read | 从流文件读取数据 | 方法 | √ | √ |
| File.fd | 获取文件描述符 | 属性 | - | - |
| OpenMode | 设置文件打开标签 | 属性 | - | - |
| Filter | 设置文件过滤配置项 | 类型 | - | - |

**注意** 

使用基础文件操作接口时，耗时较长的操作，例如：read、write等，建议使用异步接口，避免应用崩溃。

## 开发示例

在对应用文件开始访问前，开发者需要[获取应用文件路径](application-context-stage.md#获取应用文件路径)。以从UIAbilityContext获取HAP级别的文件路径为例进行说明，UIAbilityContext的获取方式请参见[获取UIAbility的上下文信息](uiability-usage.md#获取uiability的上下文信息)。

下面介绍几种常用操作示例。

### 新建并读写一个文件

以下示例代码演示了如何新建一个文件并对其读写。

```ts
// pages/xxx.ets
import { fileIo, ReadOptions } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';
import { buffer } from '@kit.ArkTS';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
```

```typescript
function createFile(context: common.UIAbilityContext): void {
  let filesDir = context.filesDir;
  let file: fileIo.File | null = null;
  try {
    // 文件不存在时创建并打开文件，文件存在时打开文件
    file = fileIo.openSync(filesDir + '/test.txt', fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
    // 写入一段内容至文件
    let writeLen = fileIo.writeSync(file.fd, 'Hello world');
    console.info('The length of str is: ' + writeLen);
    // 创建一个大小为1024字节的ArrayBuffer对象，用于存储从文件中读取的数据
    let arrayBuffer = new ArrayBuffer(1024);
    // 设置读取的偏移量和长度，单位为Byte
    let readOptions: ReadOptions = {
      offset: 0,
      length: arrayBuffer.byteLength
    };
    // 读取文件内容到ArrayBuffer对象中，并返回实际读取的字节数
    let readLen = fileIo.readSync(file.fd, arrayBuffer, readOptions);
    // 将ArrayBuffer对象转换为Buffer对象，并转换为字符串输出
    let buf = buffer.from(arrayBuffer, 0, readLen);
    console.info('Succeeded in creating file, the content of file: ' + buf.toString());
  } catch (err) {
    console.error(`Failed to create file. Code: ${err.code}, message: ${err.message}`);
  } finally {
    if (file) {
      try {
        fileIo.closeSync(file);
      } catch (err) {
        console.error(`Failed to close file`);
      }
    }
  }
}
```

### 读取文件内容并写入到另一个文件

以下示例代码演示了如何从一个文件读写内容到另一个文件。

```ts
// pages/xxx.ets
import { fileIo, ReadOptions, WriteOptions } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
```

```typescript
function readWriteFile(context: common.UIAbilityContext): void {
  let srcFile: fileIo.File | null = null;
  let destFile: fileIo.File | null = null;
  try {
    let filesDir = context.filesDir;
    // 以读写的方式打开文件，文件不存在会新建文件
    srcFile = fileIo.openSync(filesDir + '/readFile.txt', fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
    destFile = fileIo.openSync(filesDir + '/writeFile.txt', fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
    // 创建缓冲区
    let bufSize = 4096;
    let buf = new ArrayBuffer(bufSize);
    let readOffset = 0;
    let readLength = 128;
    // 设置读取的偏移量和长度，单位为Byte
    let readOptions: ReadOptions = {
      offset: readOffset,
      length: readLength
    };
    // 分次读取源文件内容并写入至目标文件
    let readLen = fileIo.readSync(srcFile.fd, buf, readOptions);
    while (readLen > 0) {
      readOffset += readLen;
      let writeOptions: WriteOptions = {
        length: readLen
      };
      // 写入目标文件
      fileIo.writeSync(destFile.fd, buf, writeOptions);
      // 更新读取位置
      readOptions.offset = readOffset;
      readLen = fileIo.readSync(srcFile.fd, buf, readOptions);
    }
    console.info(`Succeeded in reading and writing file.`);
  } catch (err) {
    console.error(`Failed to read and write File. Code: ${err.code}, message: ${err.message}`);
  } finally {
    try {
      if (srcFile) {
        fileIo.closeSync(srcFile);
      }
      if (destFile) {
        fileIo.closeSync(destFile);
      }
    } catch (closeErr) {
      console.error(`Failed to close file`);
    }
  }
}
```

**说明** 

使用读写接口时，需注意可选项参数offset的设置。对于已存在且读写过的文件，文件偏移指针默认在上次读写操作的终止位置。

### 以流的形式读写文件

以下示例代码演示了如何使用流接口读取test.txt的文件内容并写入到destFile.txt文件中。

```ts
// pages/xxx.ets
import { fileIo, ReadOptions } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
```

```typescript
async function readWriteFileWithStream(context: common.UIAbilityContext): Promise<void> {
  let filesDir = context.filesDir;
  let inputStream: fileIo.Stream | null = null;
  let outputStream: fileIo.Stream | null = null;
  try {
    // 创建并打开输入文件流
    inputStream = fileIo.createStreamSync(filesDir + '/test.txt', 'r+');
    // 创建并打开输出文件流
    outputStream = fileIo.createStreamSync(filesDir + '/destFile.txt', 'w+');
    let bufSize = 4096;
    let readSize = 0;
    let buf = new ArrayBuffer(bufSize);
    // 设置读取的偏移量和长度，单位为Byte
    let readOptions: ReadOptions = {
      offset: readSize,
      length: bufSize
    };
    // 以流的形式读取源文件内容并写入到目标文件
    let readLen = await inputStream.read(buf, readOptions);
    readSize += readLen;
    while (readLen > 0) {
      const writeBuf = readLen < bufSize ? buf.slice(0, readLen) : buf;
      await outputStream.write(writeBuf);
      readOptions.offset = readSize;
      readLen = await inputStream.read(buf, readOptions);
      readSize += readLen;
    }
    console.info(`Succeeded in reading and writing file with stream.`);
  } catch (err) {
    console.error(`Failed to read and write file with stream. Code: ${err.code}, message: ${err.message}`);
  } finally {
    try {
      if (inputStream) {
        inputStream.closeSync();
      }
      if (outputStream) {
        outputStream.closeSync();
      }
    } catch (closeErr) {
      console.error(`Failed to close stream`);
    }
  }
}
```

**说明** 

使用流接口时，需注意流的及时关闭。同时流的异步接口应严格遵循异步接口使用规范，避免同步、异步接口混用。流接口不支持并发读写。

### 查看文件列表

以下示例代码演示了如何查看文件列表。

```ts
import { fileIo, Filter, ListFileOptions } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
```

```typescript
function getListFile(context: common.UIAbilityContext): void {
  let listFileOption: ListFileOptions = {
    recursion: false,
    listNum: 0,
    filter: {
      suffix: ['.png', '.jpg', '.txt'],
      displayName: ['test*'],
      fileSizeOver: 0,
      lastModifiedAfter: new Date(0).getTime()
    }
  };
  let filesDir = context.filesDir;
  try {
    let files = fileIo.listFileSync(filesDir, listFileOption);
    for (let i = 0; i < files.length; i++) {
      console.info(`Succeeded in listing file, The name of file: ${files[i]}`);
    }
  } catch (err) {
    console.error(`Failed to list file. Code: ${err.code}, message: ${err.message}`);
  }
}
```

### 使用文件流

以下示例代码演示了如何使用文件可读流，文件可写流。

```ts
// pages/xxx.ets
import { fileIo } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
```

```typescript
function copyFileWithReadable(context: common.UIAbilityContext): void {
  try {
    let filesDir = context.filesDir;
    // 创建文件可读流
    const rs = fileIo.createReadStream(`${filesDir}/test.txt`);
    // 创建文件可写流
    const ws = fileIo.createWriteStream(`${filesDir}/destFile.txt`);
    // 暂停模式拷贝文件。在拷贝数据时，将原始数据暂停，然后将数据复制到另一个位置，适用于对数据完整性和一致性要求较高的场景
    rs.on('readable', () => {
      const data = rs.read();
      if (!data) {
        return;
      }
      ws.write(data);
    });

    rs.on('end', () => {
      ws.end();
      console.info(`Succeeded in copying file with read stream.`);
    });

    // 捕获异常
    rs.on('error', () => {
      rs.close();
      ws.close();
    });
  } catch (err) {
    console.error(`Failed to copy file with read stream. Code: ${err.code}, message: ${err.message}`);
  }
}
```

```typescript
function copyFileWithData(context: common.UIAbilityContext): void {
  let filesDir = context.filesDir;

  try {
    // 创建文件可读流
    let rs = fileIo.createReadStream(`${filesDir}/test.txt`);
    // 创建文件可写流
    let ws = fileIo.createWriteStream(`${filesDir}/destFile.txt`);

    rs.push('Hello world');
    // 流动模式拷贝文件
    rs.on('data', (emitData) => {
      const data = emitData?.data;
      if (!data) {
        return;
      }
      ws.write(data as Uint8Array);
    });

    rs.on('end', () => {
      ws.end();
      console.info(`Succeeded in copying file with data.`);
    });

    // 捕获异常
    rs.on('error', () => {
      rs.close();
      ws.close();
    });
  } catch (err) {
    console.error(`Failed to copy file with data. Code: ${err.code}, message: ${err.message}`);
  }
}
```

### 使用文件哈希流

哈希流是一种数据传输和存储技术，可以将任意长度的数据转换为固定长度的哈希值来验证数据的完整性和一致性。以下代码演示了如何使用文件哈希处理接口（[ohos.file.hash](../harmonyos-references/js-apis-file-hash.md)）来处理文件哈希流。

```ts
// pages/xxx.ets
import { fileIo } from '@kit.CoreFileKit';
import { hash } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';

// 获取应用文件路径，请在组件内获取context
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
```

```typescript
function hashFileWithStream(context: common.UIAbilityContext) {
  try {
    let filesDir = context.filesDir;
    const filePath = `${filesDir}/test.txt`;
    // 创建文件可读流
    const rs = fileIo.createReadStream(filePath);
    // 创建哈希流
    const hs = hash.createHash('sha256');
    rs.on('data', (emitData) => {
      const data = emitData?.data;
      hs.update(new Uint8Array(data?.split('').map((x: string) => x.charCodeAt(0))).buffer);
    });
    rs.on('end', async () => {
      const hashResult = hs.digest();
      const fileHash = await hash.hash(filePath, 'sha256');
      console.info(`Succeeded in hashing file with stream, hash result: ${hashResult}, file hash: ${fileHash}`);
    });
  } catch (err) {
    console.error(`Failed to hash file with stream. Code: ${err.code}, message: ${err.message}`);
  }
}
```
