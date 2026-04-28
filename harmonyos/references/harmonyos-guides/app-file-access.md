---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-file-access
title: 应用文件访问(ArkTS)
breadcrumb: 指南 > 应用框架 > Core File Kit（文件基础服务） > 应用文件 > 应用文件访问与管理 > 应用文件访问(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:12+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:7c2cc9d61a11ee47f0f32de62253209a8f22e58fd007270a6bb5d552b12421e0
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

注意

使用基础文件操作接口时，耗时较长的操作，例如：read、write等，建议使用异步接口，避免应用崩溃。

## 开发示例

在对应用文件开始访问前，开发者需要[获取应用文件路径](application-context-stage.md#获取应用文件路径)。以从UIAbilityContext获取HAP级别的文件路径为例进行说明，UIAbilityContext的获取方式请参见[获取UIAbility的上下文信息](uiability-usage.md#获取uiability的上下文信息)。

下面介绍几种常用操作示例。

### 新建并读写一个文件

以下示例代码演示了如何新建一个文件并对其读写。

```
1. // pages/xxx.ets
2. import { fileIo, ReadOptions } from '@kit.CoreFileKit';
3. import { common } from '@kit.AbilityKit';
4. import { buffer } from '@kit.ArkTS';

6. // 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
7. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
```

```
1. function createFile(context: common.UIAbilityContext): void {
2. let filesDir = context.filesDir;
3. let file: fileIo.File | null = null;
4. try {
5. // 文件不存在时创建并打开文件，文件存在时打开文件
6. file = fileIo.openSync(filesDir + '/test.txt', fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
7. // 写入一段内容至文件
8. let writeLen = fileIo.writeSync(file.fd, 'Hello world');
9. console.info('The length of str is: ' + writeLen);
10. // 创建一个大小为1024字节的ArrayBuffer对象，用于存储从文件中读取的数据
11. let arrayBuffer = new ArrayBuffer(1024);
12. // 设置读取的偏移量和长度，单位为Byte
13. let readOptions: ReadOptions = {
14. offset: 0,
15. length: arrayBuffer.byteLength
16. };
17. // 读取文件内容到ArrayBuffer对象中，并返回实际读取的字节数
18. let readLen = fileIo.readSync(file.fd, arrayBuffer, readOptions);
19. // 将ArrayBuffer对象转换为Buffer对象，并转换为字符串输出
20. let buf = buffer.from(arrayBuffer, 0, readLen);
21. console.info('Succeeded in creating file, the content of file: ' + buf.toString());
22. } catch (err) {
23. console.error(`Failed to create file. Code: ${err.code}, message: ${err.message}`);
24. } finally {
25. if (file) {
26. try {
27. fileIo.closeSync(file);
28. } catch (err) {
29. console.error(`Failed to close file`);
30. }
31. }
32. }
33. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/CoreFile/FileApiFileSample/entry/src/main/ets/pages/Index.ets#L21-L44)

### 读取文件内容并写入到另一个文件

以下示例代码演示了如何从一个文件读写内容到另一个文件。

```
1. // pages/xxx.ets
2. import { fileIo, ReadOptions, WriteOptions } from '@kit.CoreFileKit';
3. import { common } from '@kit.AbilityKit';

5. // 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
6. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
```

```
1. function readWriteFile(context: common.UIAbilityContext): void {
2. let srcFile: fileIo.File | null = null;
3. let destFile: fileIo.File | null = null;
4. try {
5. let filesDir = context.filesDir;
6. // 以读写的方式打开文件，文件不存在会新建文件
7. srcFile = fileIo.openSync(filesDir + '/readFile.txt', fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
8. destFile = fileIo.openSync(filesDir + '/writeFile.txt', fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
9. // 创建缓冲区
10. let bufSize = 4096;
11. let buf = new ArrayBuffer(bufSize);
12. let readOffset = 0;
13. let readLength = 128;
14. // 设置读取的偏移量和长度，单位为Byte
15. let readOptions: ReadOptions = {
16. offset: readOffset,
17. length: readLength
18. };
19. // 分次读取源文件内容并写入至目标文件
20. let readLen = fileIo.readSync(srcFile.fd, buf, readOptions);
21. while (readLen > 0) {
22. readOffset += readLen;
23. let writeOptions: WriteOptions = {
24. length: readLen
25. };
26. // 写入目标文件
27. fileIo.writeSync(destFile.fd, buf, writeOptions);
28. // 更新读取位置
29. readOptions.offset = readOffset;
30. readLen = fileIo.readSync(srcFile.fd, buf, readOptions);
31. }
32. console.info(`Succeeded in reading and writing file.`);
33. } catch (err) {
34. console.error(`Failed to read and write File. Code: ${err.code}, message: ${err.message}`);
35. } finally {
36. try {
37. if (srcFile) {
38. fileIo.closeSync(srcFile);
39. }
40. if (destFile) {
41. fileIo.closeSync(destFile);
42. }
43. } catch (closeErr) {
44. console.error(`Failed to close file`);
45. }
46. }
47. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/CoreFile/FileApiFileSample/entry/src/main/ets/pages/Index.ets#L46-L74)

说明

使用读写接口时，需注意可选项参数offset的设置。对于已存在且读写过的文件，文件偏移指针默认在上次读写操作的终止位置。

### 以流的形式读写文件

以下示例代码演示了如何使用流接口读取test.txt的文件内容并写入到destFile.txt文件中。

```
1. // pages/xxx.ets
2. import { fileIo, ReadOptions } from '@kit.CoreFileKit';
3. import { common } from '@kit.AbilityKit';

5. // 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
6. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
```

```
1. async function readWriteFileWithStream(context: common.UIAbilityContext): Promise<void> {
2. let filesDir = context.filesDir;
3. let inputStream: fileIo.Stream | null = null;
4. let outputStream: fileIo.Stream | null = null;
5. try {
6. // 创建并打开输入文件流
7. inputStream = fileIo.createStreamSync(filesDir + '/test.txt', 'r+');
8. // 创建并打开输出文件流
9. outputStream = fileIo.createStreamSync(filesDir + '/destFile.txt', 'w+');
10. let bufSize = 4096;
11. let readSize = 0;
12. let buf = new ArrayBuffer(bufSize);
13. // 设置读取的偏移量和长度，单位为Byte
14. let readOptions: ReadOptions = {
15. offset: readSize,
16. length: bufSize
17. };
18. // 以流的形式读取源文件内容并写入到目标文件
19. let readLen = await inputStream.read(buf, readOptions);
20. readSize += readLen;
21. while (readLen > 0) {
22. const writeBuf = readLen < bufSize ? buf.slice(0, readLen) : buf;
23. await outputStream.write(writeBuf);
24. readOptions.offset = readSize;
25. readLen = await inputStream.read(buf, readOptions);
26. readSize += readLen;
27. }
28. console.info(`Succeeded in reading and writing file with stream.`);
29. } catch (err) {
30. console.error(`Failed to read and write file with stream. Code: ${err.code}, message: ${err.message}`);
31. } finally {
32. try {
33. if (inputStream) {
34. inputStream.closeSync();
35. }
36. if (outputStream) {
37. outputStream.closeSync();
38. }
39. } catch (closeErr) {
40. console.error(`Failed to close stream`);
41. }
42. }
43. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/CoreFile/FileApiFileSample/entry/src/main/ets/pages/Index.ets#L76-L105)

说明

使用流接口时，需注意流的及时关闭。同时流的异步接口应严格遵循异步接口使用规范，避免同步、异步接口混用。流接口不支持并发读写。

### 查看文件列表

以下示例代码演示了如何查看文件列表。

```
1. import { fileIo, Filter, ListFileOptions } from '@kit.CoreFileKit';
2. import { common } from '@kit.AbilityKit';

4. // 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
5. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
```

```
1. function getListFile(context: common.UIAbilityContext): void {
2. let listFileOption: ListFileOptions = {
3. recursion: false,
4. listNum: 0,
5. filter: {
6. suffix: ['.png', '.jpg', '.txt'],
7. displayName: ['test*'],
8. fileSizeOver: 0,
9. lastModifiedAfter: new Date(0).getTime()
10. }
11. };
12. let filesDir = context.filesDir;
13. try {
14. let files = fileIo.listFileSync(filesDir, listFileOption);
15. for (let i = 0; i < files.length; i++) {
16. console.info(`Succeeded in listing file, The name of file: ${files[i]}`);
17. }
18. } catch (err) {
19. console.error(`Failed to list file. Code: ${err.code}, message: ${err.message}`);
20. }
21. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/CoreFile/FileApiFileSample/entry/src/main/ets/pages/Index.ets#L108-L126)

### 使用文件流

以下示例代码演示了如何使用文件可读流，文件可写流。

```
1. // pages/xxx.ets
2. import { fileIo } from '@kit.CoreFileKit';
3. import { common } from '@kit.AbilityKit';

5. // 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
6. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
```

```
1. function copyFileWithReadable(context: common.UIAbilityContext): void {
2. try {
3. let filesDir = context.filesDir;
4. // 创建文件可读流
5. const rs = fileIo.createReadStream(`${filesDir}/test.txt`);
6. // 创建文件可写流
7. const ws = fileIo.createWriteStream(`${filesDir}/destFile.txt`);
8. // 暂停模式拷贝文件。在拷贝数据时，将原始数据暂停，然后将数据复制到另一个位置，适用于对数据完整性和一致性要求较高的场景
9. rs.on('readable', () => {
10. const data = rs.read();
11. if (!data) {
12. return;
13. }
14. ws.write(data);
15. });

17. rs.on('end', () => {
18. ws.end();
19. console.info(`Succeeded in copying file with read stream.`);
20. });

22. // 捕获异常
23. rs.on('error', () => {
24. rs.close();
25. ws.close();
26. });
27. } catch (err) {
28. console.error(`Failed to copy file with read stream. Code: ${err.code}, message: ${err.message}`);
29. }
30. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/CoreFile/FileApiFileSample/entry/src/main/ets/pages/Index.ets#L128-L144)

```
1. function copyFileWithData(context: common.UIAbilityContext): void {
2. let filesDir = context.filesDir;

4. try {
5. // 创建文件可读流
6. let rs = fileIo.createReadStream(`${filesDir}/test.txt`);
7. // 创建文件可写流
8. let ws = fileIo.createWriteStream(`${filesDir}/destFile.txt`);

10. rs.push('Hello world');
11. // 流动模式拷贝文件
12. rs.on('data', (emitData) => {
13. const data = emitData?.data;
14. if (!data) {
15. return;
16. }
17. ws.write(data as Uint8Array);
18. });

20. rs.on('end', () => {
21. ws.end();
22. console.info(`Succeeded in copying file with data.`);
23. });

25. // 捕获异常
26. rs.on('error', () => {
27. rs.close();
28. ws.close();
29. });
30. } catch (err) {
31. console.error(`Failed to copy file with data. Code: ${err.code}, message: ${err.message}`);
32. }
33. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/CoreFile/FileApiFileSample/entry/src/main/ets/pages/Index.ets#L146-L162)

### 使用文件哈希流

哈希流是一种数据传输和存储技术，可以将任意长度的数据转换为固定长度的哈希值来验证数据的完整性和一致性。以下代码演示了如何使用文件哈希处理接口（[ohos.file.hash](../harmonyos-references/js-apis-file-hash.md)）来处理文件哈希流。

```
1. // pages/xxx.ets
2. import { fileIo } from '@kit.CoreFileKit';
3. import { hash } from '@kit.CoreFileKit';
4. import { common } from '@kit.AbilityKit';

6. // 获取应用文件路径，请在组件内获取context
7. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
```

```
1. function hashFileWithStream(context: common.UIAbilityContext) {
2. try {
3. let filesDir = context.filesDir;
4. const filePath = `${filesDir}/test.txt`;
5. // 创建文件可读流
6. const rs = fileIo.createReadStream(filePath);
7. // 创建哈希流
8. const hs = hash.createHash('sha256');
9. rs.on('data', (emitData) => {
10. const data = emitData?.data;
11. hs.update(new Uint8Array(data?.split('').map((x: string) => x.charCodeAt(0))).buffer);
12. });
13. rs.on('end', async () => {
14. const hashResult = hs.digest();
15. const fileHash = await hash.hash(filePath, 'sha256');
16. console.info(`Succeeded in hashing file with stream, hash result: ${hashResult}, file hash: ${fileHash}`);
17. });
18. } catch (err) {
19. console.error(`Failed to hash file with stream. Code: ${err.code}, message: ${err.message}`);
20. }
21. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/CoreFile/FileApiFileSample/entry/src/main/ets/pages/Index.ets#L164-L182)
