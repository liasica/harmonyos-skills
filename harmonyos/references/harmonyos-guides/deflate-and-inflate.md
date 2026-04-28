---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/deflate-and-inflate
title: 压缩与解压
breadcrumb: 指南 > 系统 > 基础功能 > Basic Services Kit（基础服务） > 压缩与解压 > 压缩与解压
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:23+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0345100853fac39866b8012d6806d45835a5385895aa45e95d8f38d6af97916d
---

本文针对常见的几种压缩、解压场景，介绍相关函数的使用方法。

## 接口说明

以下是示例中使用的主要接口，更多接口及使用方式请见@ohos.zlib (Zip模块)(../../reference/apis-basic-services-kit/js-apis-zlib.md)。

| 接口名 | 接口描述 |
| --- | --- |
| compressFile(inFile: string, outFile: string, options: Options): Promise<void> | 压缩文件。 |
| decompressFile(inFile: string, outFile: string, options?: Options): Promise<void> | 解压文件。 |
| compress(dest: ArrayBuffer, source: ArrayBuffer, sourceLen?: number): Promise<ZipOutputInfo> | 将源缓冲区压缩到目标缓冲区。 |
| compressBound(sourceLen: number): Promise<number> | 计算返回压缩大小的上限。 |
| uncompress(dest:ArrayBuffer, source: ArrayBuffer, sourceLen?: number): Promise<ZipOutputInfo> | 将压缩后的数据解压缩为原始的未压缩形式。 |
| deflate(strm: ZStream, flush: CompressFlushMode): Promise<ReturnStatus> | 压缩数据。 |
| inflate(strm: ZStream, flush: CompressFlushMode): Promise<ReturnStatus> | 解压数据。 |

## 开发步骤

### 环境准备

在应用沙箱目录下创建一个测试文件data.txt，并写入测试数据。示例代码如下。

```
1. import { fileIo as fs} from '@kit.CoreFileKit';

3. @Entry
4. @Component
5. struct Index {
6. @State dataSize: number = 0;

8. build() {
9. Row() {
10. Column() {
11. // 在应用沙箱目录下创建文件data.txt，并写入测试数据
12. Button('创建测试文件data.txt').onClick(() => {
13. let path = this.getUIContext()?.getHostContext()?.filesDir;
14. // 创建文件data.txt
15. let inFile = fs.openSync(path + '/data.txt', fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
16. // 写入测试数据
17. for (let index = 0; index < 100; index++) {
18. fs.writeSync(inFile.fd, index + ': hello world, hello world, hello world, hello world, hello world.\n');
19. }
20. // 获取测试数据原始大小，并保存到dataSize中
21. let stat = fs.statSync(inFile.path);
22. this.dataSize = stat.size;
23. console.info('dataSize: ' + this.dataSize);
24. // 关闭文件
25. fs.closeSync(inFile);
26. })
27. }
28. }
29. .height('100%')
30. .width('100%')
31. }
32. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/DeflateAndInflate/entry/src/main/ets/pages/Index.ets#L15-L48)

### Zip文件的压缩与解压

采用接口[zlib.compressFile()](../harmonyos-references/js-apis-zlib.md#zlibcompressfile9-1)将文件data.txt压缩并归档到data.zip中，采用接口[zlib.decompressFile()](../harmonyos-references/js-apis-zlib.md#zlibdecompressfile9-1)将data.zip解压到应用沙箱目录下，示例代码如下。

```
1. import { BusinessError, zlib } from '@kit.BasicServicesKit';

3. @Entry
4. @Component
5. struct Index {
6. build() {
7. Row() {
8. // 示例一：将测试文件data.txt压缩并归档到data.zip中。
9. Button('compressFile').onClick(() => {
10. let path = this.getUIContext()?.getHostContext()?.filesDir;
11. let inFile = path + '/data.txt';
12. let outFile = path + '/data.zip';
13. let options: zlib.Options = {};
14. zlib.compressFile(inFile, outFile, options).then((data: void) => {
15. console.info('compressFile success, data: ' + JSON.stringify(data));
16. }).catch((errData: BusinessError) => {
17. console.error(`compressFile errCode: ${errData.code}, message: ${errData.message}`);
18. })
19. })

21. // 示例二：将data.zip文件解压到应用沙箱目录下。
22. Button('decompressFile').onClick(() => {
23. let path = this.getUIContext()?.getHostContext()?.filesDir;
24. let inFile = path + '/data.zip';
25. let outFile = path;
26. let options: zlib.Options = {};
27. zlib.decompressFile(inFile, outFile, options).then((data: void) => {
28. console.info('decompressFile success, data: ' + JSON.stringify(data));
29. }).catch((errData: BusinessError) => {
30. console.error(`decompressFile errCode: ${errData.code}, message: ${errData.message}`);
31. })
32. })
33. }
34. .height('100%')
35. .width('100%')
36. }
37. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/DeflateAndInflate/entry/src/main/ets/pages1/Index.ets#L16-L54)

### 已知大小缓冲区的压缩与解压

针对一个已知大小的缓冲区中的数据，使用接口[compress()](../harmonyos-references/js-apis-zlib.md#compress12)将其压缩到一个目标缓冲区中，使用接口[compressBound()](../harmonyos-references/js-apis-zlib.md#compressbound12)计算压缩目标缓冲区大小的上限值，使用接口[uncompress()](../harmonyos-references/js-apis-zlib.md#uncompress12)对存储压缩数据的缓冲区进行解压。由于解压时无法获取解压后原始数据的大小，为了确认解压后目标缓冲区的大小，需要在压缩前获取原始数据的大小并保存，示例代码如下。

```
1. import { fileIo as fs} from '@kit.CoreFileKit';
2. import { BusinessError, zlib } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct Index {
7. @State dataSize: number = 0;  // 用于保存原始数据的大小

9. build() {
10. Row() {
11. // 示例一：读取data.txt文件内容并存入一个缓冲区，调用compress接口压缩缓冲区中的数据到目标缓冲区，并将目标缓冲区的内容写入文件data.bin
12. Button('compress buffer').onClick(() => {
13. let path = this.getUIContext()?.getHostContext()?.filesDir;
14. let inFile = fs.openSync(path + '/data.txt', fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
15. let outFile = fs.openSync(path + '/data.bin', fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
16. // 读取data.txt文件的内容，并存入缓冲区inBuf
17. let stat = fs.statSync(inFile.path);
18. let inBuf = new ArrayBuffer(stat.size);
19. let readLen = fs.readSync(inFile.fd, inBuf);
20. console.info(`original size: ${stat.size}, read len: ${readLen}`);
21. // 获取原始数据的大小，并保存
22. this.dataSize = stat.size;
23. // 创建一个压缩对象实例
24. let zip = zlib.createZipSync();
25. // 获取一个目标缓冲区的上限
26. zip.compressBound(stat.size).then((data) => {
27. console.info(`the max dest buf len is ${data}`);
28. // 目标缓冲区outBuf
29. let outBuf = new ArrayBuffer(data);
30. // 将inBuf中的数据压缩到outBuf中
31. zip.compress(outBuf, inBuf, readLen).then((zipOutInfo) => {
32. console.info(`compress success, status ${zipOutInfo.status}, destLen  ${zipOutInfo.destLen}`);
33. // 将outBuf中的数据写入到data.bin文件
34. let writeLen = fs.writeSync(outFile.fd, outBuf, { length: zipOutInfo.destLen });
35. console.info(`write destBuf to data.bin, writeLen ${writeLen}`);
36. // 关闭文件
37. fs.closeSync(inFile.fd);
38. fs.closeSync(outFile.fd);
39. }).catch((errData: BusinessError) => {
40. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
41. })
42. }).catch((errData: BusinessError) => {
43. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
44. })
45. })

47. // 示例二：读取data.bin文件中的压缩数据并存入一个缓冲区，调用uncompress接口将缓冲区中的数据解压到目标缓冲区，并将目标缓冲区的内容写入文件data.txt
48. Button('uncompress buffer').onClick(() => {
49. let path = this.getUIContext()?.getHostContext()?.filesDir;
50. let inFile = fs.openSync(path + '/data.bin', fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
51. let outFile = fs.openSync(path + '/data.txt', fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
52. // 读取data.bin文件中的压缩数据，并存入缓冲区inBuf
53. let stat = fs.statSync(inFile.path);
54. let inBuf = new ArrayBuffer(stat.size);
55. let readLen = fs.readSync(inFile.fd, inBuf);
56. console.info(`compressed data size: ${stat.size}, read len: ${readLen}`);
57. // 创建一个目标缓冲区，此处的dataSize是我们进行数据压缩前保存的数据的原始大小
58. let outBuf = new ArrayBuffer(this.dataSize);
59. console.info(`the dest buf size is ${this.dataSize}`);
60. // 创建一个压缩对象实例
61. let zip = zlib.createZipSync();
62. // 将inBuf中的数据解压缩outBuf中
63. zip.uncompress(outBuf, inBuf, readLen).then((zipOutInfo) => {
64. console.info(`uncompress success, status ${zipOutInfo.status}, destLen  ${zipOutInfo.destLen}`);
65. // 将outBuf中的数据写入到data.txt文件
66. let writeLen = fs.writeSync(outFile.fd, outBuf, { length: zipOutInfo.destLen });
67. console.info(`write destBuf to data.txt, writeLen ${writeLen}`);
68. // 关闭文件
69. fs.closeSync(inFile.fd);
70. fs.closeSync(outFile.fd);
71. }).catch((errData: BusinessError) => {
72. console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
73. })
74. })
75. }
76. .height('100%')
77. .width('100%')
78. }
79. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/DeflateAndInflate/entry/src/main/ets/pages2/Index.ets#L16-L96)

### 未知大小缓冲区的压缩与解压（zlib格式）

针对一个未知大小的缓冲区中的数据，使用接口[deflate()](../harmonyos-references/js-apis-zlib.md#deflate12)将从一个原始输入流中读取的数据进行压缩，使用接口[inflate()](../harmonyos-references/js-apis-zlib.md#inflate12)将从一个压缩输入流中读取的数据进行解压，示例代码如下。

```
1. import { fileIo as fs} from '@kit.CoreFileKit';
2. import { zlib } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct Index {
7. build() {
8. Row() {
9. // 示例一：从文件中不断读取数据进行压缩
10. Button('deflateFile').onClick(() => {
11. let path = this.getUIContext()?.getHostContext()?.filesDir;
12. let inFile = fs.openSync(path + '/data.txt', fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
13. let outFile = fs.openSync(path + '/data.bin', fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
14. deflateFile(inFile, outFile).then(() => {
15. console.info('deflateFile success');
16. fs.closeSync(inFile.fd);
17. fs.closeSync(outFile.fd);
18. })
19. })

21. // 示例二：从文件中不断读取压缩数据进行解压
22. Button('inflateFile').onClick(() => {
23. let path = this.getUIContext()?.getHostContext()?.filesDir;
24. let inFile = fs.openSync(path + '/data.bin', fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
25. let outFile = fs.openSync(path + '/data.txt', fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
26. inflateFile(inFile, outFile).then(() => {
27. console.info('inflateFile success');
28. fs.closeSync(inFile.fd);
29. fs.closeSync(outFile.fd);
30. })
31. })
32. }
33. .height('100%')
34. .width('100%')
35. }
36. }

38. // 从一个文件中，不断的读入数据，进行压缩，并写入到另一个文件中
39. async function deflateFile(src: fs.File, dest: fs.File) {
40. let flush = zlib.CompressFlushMode.NO_FLUSH;
41. let strm: zlib.ZStream = {};  // 初始化一个压缩流
42. const BUFLEN = 4096;
43. let inBuf = new ArrayBuffer(BUFLEN);  // 初始化一个输入缓冲区
44. let outBuf = new ArrayBuffer(BUFLEN); // 初始化一个输出缓冲区
45. // 创建一个压缩对象实例
46. let zip = zlib.createZipSync();
47. // 初始化流的状态
48. let initStatus = zip.deflateInit(strm, zlib.CompressLevel.COMPRESS_LEVEL_BEST_SPEED);
49. console.info('deflateInit ret: ' + (await initStatus).valueOf());
50. do {
51. // 从文件中读取数据到缓冲区
52. let readLen = fs.readSync(src.fd, inBuf);
53. console.info('readSync readLen: ' + readLen);
54. flush = readLen == 0 ? zlib.CompressFlushMode.FINISH : zlib.CompressFlushMode.NO_FLUSH;
55. // 设置输入缓冲区
56. strm.availableIn = readLen;
57. strm.nextIn = inBuf;
58. do {
59. // 设置输出缓冲区
60. strm.availableOut = BUFLEN;
61. strm.nextOut = outBuf;
62. try {
63. // 压缩输入缓冲区中数据到输出缓冲区
64. let deflateStatus = zip.deflate(strm, flush);
65. console.info('deflate ret: ' + (await deflateStatus).valueOf());
66. // 更新流的状态
67. let innerStrm = zip.getZStream();
68. strm.availableIn = (await innerStrm).availableIn;
69. strm.nextIn = (await innerStrm).nextIn;
70. strm.availableOut = (await innerStrm).availableOut;
71. strm.nextOut = (await innerStrm).nextOut;
72. strm.totalIn = (await innerStrm).totalIn;
73. strm.totalOut = (await innerStrm).totalOut;

75. if (strm.availableOut != undefined) {
76. // 将已完成压缩的数据，写入到输出文件中
77. let have = BUFLEN - strm.availableOut;
78. let writeLen = fs.writeSync(dest.fd, outBuf, { length: have });
79. console.info(`writeSync writeLen: ${writeLen}`);
80. }
81. } catch (err) {
82. console.error('deflate err: ' + JSON.stringify(err));
83. }
84. } while (strm.availableOut == 0); // 循环压缩输入缓冲区中剩余的数据，直到全部完成压缩
85. } while (flush != zlib.CompressFlushMode.FINISH); // 循环从文件中读取数据，直到数据全部读取
86. // 释放资源
87. zip.deflateEnd(strm);
88. }

90. // 从一个文件中，不断的读入已压缩的数据，进行解压，并写入到另一个文件中
91. async function inflateFile(src: fs.File, dest: fs.File) {
92. let status: zlib.ReturnStatus = zlib.ReturnStatus.OK;
93. let strm: zlib.ZStream = {};  // 初始化一个压缩流
94. const BUFLEN = 4096;
95. let inBuf = new ArrayBuffer(BUFLEN);  // 初始化一个输入缓冲区
96. let outBuf = new ArrayBuffer(BUFLEN); // 初始化一个输出缓冲区
97. // 创建一个压缩对象实例
98. let zip = zlib.createZipSync();
99. // 初始化流的状态
100. let initStatus = zip.inflateInit(strm);
101. console.info('inflateInit ret: ' + (await initStatus).valueOf());
102. do {
103. // 从文件中读取已压缩的数据到缓冲区
104. let readLen = fs.readSync(src.fd, inBuf);
105. console.info('readSync readLen: ' + readLen);
106. if (readLen == 0) {
107. break;
108. }
109. // 设置输入缓冲区
110. strm.availableIn = readLen;
111. strm.nextIn = inBuf;
112. do {
113. // 设置输出缓冲区
114. strm.availableOut = BUFLEN;
115. strm.nextOut = outBuf;
116. try {
117. // 解压输入缓冲区中数据到输出缓冲区
118. let inflateStatus = zip.inflate(strm, zlib.CompressFlushMode.NO_FLUSH);
119. console.info('inflate ret: ' + (await inflateStatus).valueOf());
120. status = await inflateStatus;
121. // 更新流的状态
122. let innerStrm = zip.getZStream();
123. strm.availableIn = (await innerStrm).availableIn;
124. strm.nextIn = (await innerStrm).nextIn;
125. strm.availableOut = (await innerStrm).availableOut;
126. strm.nextOut = (await innerStrm).nextOut;
127. strm.totalIn = (await innerStrm).totalIn;
128. strm.totalOut = (await innerStrm).totalOut;

130. if (strm.availableOut != undefined) {
131. // 将已完成解压的数据，写入到输出文件中
132. let have = BUFLEN - strm.availableOut;
133. let writeLen = fs.writeSync(dest.fd, outBuf, { length: have });
134. console.info(`writeSync writeLen: ${writeLen}`);
135. }
136. } catch (err) {
137. console.error('inflate err: ' + JSON.stringify(err));
138. }
139. } while (strm.availableOut == 0)  // 循环解压输入缓冲区中剩余的数据，直到全部完成解压
140. } while (status != zlib.ReturnStatus.STREAM_END.valueOf())  // 循环从文件中读取数据，直到数据全部读取
141. // 释放资源
142. zip.inflateEnd(strm);
143. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/DeflateAndInflate/entry/src/main/ets/pages3/Index.ets#L16-L160)

### 未知大小缓冲区的压缩与解压（gzip格式）

采用gzip格式，针对一个未知大小的缓冲区中的数据，使用接口[deflate()](../harmonyos-references/js-apis-zlib.md#deflate12)将从一个原始输入流中读取的数据进行压缩，使用接口[inflate()](../harmonyos-references/js-apis-zlib.md#inflate12)将从一个压缩输入流中读取的数据进行解压，示例代码如下。

```
1. import { fileIo as fs} from '@kit.CoreFileKit';
2. import { zlib } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct Index {
7. build() {
8. Row() {
9. // 示例一：从文件中不断读取数据进行压缩
10. Button('deflateGzipFile').onClick(() => {
11. let path = this.getUIContext()?.getHostContext()?.filesDir;
12. let inFile = fs.openSync(path + '/data.txt', fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
13. let outFile = fs.openSync(path + '/data.gz', fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
14. deflateGzipFile(inFile, outFile).then(() => {
15. console.info('deflateGzipFile success');
16. fs.closeSync(inFile.fd);
17. fs.closeSync(outFile.fd);
18. })
19. })

21. // 示例二：从文件中不断读取压缩数据进行解压
22. Button('inflateGzipFile').onClick(() => {
23. let path = this.getUIContext()?.getHostContext()?.filesDir;
24. let inFile = fs.openSync(path + '/data.gz', fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
25. let outFile = fs.openSync(path + '/data.txt', fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
26. inflateGzipFile(inFile, outFile).then(() => {
27. console.info('inflateGzipFile success');
28. fs.closeSync(inFile.fd);
29. fs.closeSync(outFile.fd);
30. })
31. })
32. }
33. .height('100%')
34. .width('100%')
35. }
36. }

38. // 从一个文件中，不断的读入数据，进行压缩，并写入到另一个文件中
39. async function deflateGzipFile(src: fs.File, dest: fs.File) {
40. let flush = zlib.CompressFlushMode.NO_FLUSH;
41. let strm: zlib.ZStream = {};  // 初始化一个压缩流
42. const BUFLEN = 4096;
43. let inBuf = new ArrayBuffer(BUFLEN);  // 初始化一个输入缓冲区
44. let outBuf = new ArrayBuffer(BUFLEN); // 初始化一个输出缓冲区
45. // 创建一个压缩对象实例
46. let zip = zlib.createZipSync();
47. // 初始化流的状态，windowBits > 15时，启用gzip格式
48. let windowBits = 15 + 16;
49. let initStatus = zip.deflateInit2(strm, zlib.CompressLevel.COMPRESS_LEVEL_BEST_SPEED,
50. zlib.CompressMethod.DEFLATED, windowBits, zlib.MemLevel.MEM_LEVEL_DEFAULT,
51. zlib.CompressStrategy.COMPRESS_STRATEGY_DEFAULT_STRATEGY);
52. console.info('deflateInit2 ret: ' + (await initStatus).valueOf());
53. do {
54. // 从文件中读取数据到缓冲区
55. let readLen = fs.readSync(src.fd, inBuf);
56. console.info('readSync readLen: ' + readLen);
57. flush = readLen == 0 ? zlib.CompressFlushMode.FINISH : zlib.CompressFlushMode.NO_FLUSH;
58. // 设置输入缓冲区
59. strm.availableIn = readLen;
60. strm.nextIn = inBuf;
61. do {
62. // 设置输出缓冲区
63. strm.availableOut = BUFLEN;
64. strm.nextOut = outBuf;
65. try {
66. // 压缩输入缓冲区中数据到输出缓冲区
67. let deflateStatus = zip.deflate(strm, flush);
68. console.info('deflate ret: ' + (await deflateStatus).valueOf());
69. // 更新流的状态
70. let innerStrm = zip.getZStream();
71. strm.availableIn = (await innerStrm).availableIn;
72. strm.nextIn = (await innerStrm).nextIn;
73. strm.availableOut = (await innerStrm).availableOut;
74. strm.nextOut = (await innerStrm).nextOut;
75. strm.totalIn = (await innerStrm).totalIn;
76. strm.totalOut = (await innerStrm).totalOut;

78. if (strm.availableOut != undefined) {
79. // 将已完成压缩的数据，写入到输出文件中
80. let have = BUFLEN - strm.availableOut;
81. let writeLen = fs.writeSync(dest.fd, outBuf, { length: have });
82. console.info(`writeSync writeLen: ${writeLen}`);
83. }
84. } catch (err) {
85. console.error('deflate err: ' + JSON.stringify(err));
86. }
87. } while (strm.availableOut == 0); // 循环压缩输入缓冲区中剩余的数据，直到全部完成压缩
88. } while (flush != zlib.CompressFlushMode.FINISH); // 循环从文件中读取数据，直到数据全部读取
89. // 释放资源
90. zip.deflateEnd(strm);
91. }

93. // 从一个文件中，不断的读入已压缩的数据，进行解压，并写入到另一个文件中
94. async function inflateGzipFile(src: fs.File, dest: fs.File) {
95. let status: zlib.ReturnStatus = zlib.ReturnStatus.OK;
96. let strm: zlib.ZStream = {};  // 初始化一个压缩流
97. const BUFLEN = 4096;
98. let inBuf = new ArrayBuffer(BUFLEN);  // 初始化一个输入缓冲区
99. let outBuf = new ArrayBuffer(BUFLEN); // 初始化一个输出缓冲区
100. // 创建一个压缩对象实例
101. let zip = zlib.createZipSync();
102. // 初始化流的状态，windowBits > 15时，启用gzip格式
103. let windowBits = 15 + 16;
104. let initStatus = zip.inflateInit2(strm, windowBits);
105. console.info('inflateInit2 ret: ' + (await initStatus).valueOf());
106. do {
107. // 从文件中读取已压缩的数据到缓冲区
108. let readLen = fs.readSync(src.fd, inBuf);
109. console.info('readSync readLen: ' + readLen);
110. if (readLen == 0) {
111. break;
112. }
113. // 设置输入缓冲区
114. strm.availableIn = readLen;
115. strm.nextIn = inBuf;
116. do {
117. // 设置输出缓冲区
118. strm.availableOut = BUFLEN;
119. strm.nextOut = outBuf;
120. try {
121. // 解压输入缓冲区中数据到输出缓冲区
122. let inflateStatus = zip.inflate(strm, zlib.CompressFlushMode.NO_FLUSH);
123. console.info('inflate ret: ' + (await inflateStatus).valueOf());
124. status = await inflateStatus;
125. // 更新流的状态
126. let innerStrm = zip.getZStream();
127. strm.availableIn = (await innerStrm).availableIn;
128. strm.nextIn = (await innerStrm).nextIn;
129. strm.availableOut = (await innerStrm).availableOut;
130. strm.nextOut = (await innerStrm).nextOut;
131. strm.totalIn = (await innerStrm).totalIn;
132. strm.totalOut = (await innerStrm).totalOut;

134. if (strm.availableOut != undefined) {
135. // 将已完成解压的数据，写入到输出文件中
136. let have = BUFLEN - strm.availableOut;
137. let writeLen = fs.writeSync(dest.fd, outBuf, { length: have });
138. console.info(`writeSync writeLen: ${writeLen}`);
139. }
140. } catch (err) {
141. console.error('inflate err: ' + JSON.stringify(err));
142. }
143. } while (strm.availableOut == 0)  // 循环解压输入缓冲区中剩余的数据，直到全部完成解压
144. } while (status != zlib.ReturnStatus.STREAM_END.valueOf())  // 循环从文件中读取数据，直到数据全部读取
145. // 释放资源
146. zip.inflateEnd(strm);
147. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/DeflateAndInflate/entry/src/main/ets/pages4/Index.ets#L16-L164)

## 常见问题

1. 17800005 传入的数据错误

   可能原因和处理步骤，请参见[17800005](../harmonyos-references/errorcode-zlib.md#section17800005-传入的数据错误)。
2. 17800007 传入的缓冲区错误

   可能原因和处理步骤，请参见[17800007](../harmonyos-references/errorcode-zlib.md#section17800007-传入的缓冲区错误)。
