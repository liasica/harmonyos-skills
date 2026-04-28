---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/remote-communication-filetransferfast
title: 快速实现上传下载
breadcrumb: 指南 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > 使用HTTP协议进行网络通信 > 文件上传下载 > 快速实现上传下载
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:07+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b05b5113317cea53c2be6e11a33a2be68b2c725401ef2c3ae2d41d638cb92f2e
---

Remote Communication Kit 结合 Core File Kit 可以实现基于文件、目录、对象的快速上传和下载功能。 Remote Communication Kit 提供了远程通信的功能，包括远程连接、数据传输等 API 接口。而 Core File Kit 则提供了文件管理的功能，包括文件读取、写入等 API 接口。结合起来使用，可以通过 Remote Communication Kit 实现文件、目录、对象的远程传输，并且由于 Core File Kit 的高效文件处理能力，可以实现快速的上传和下载功能。

## 约束与限制

文件上传下载能力支持Phone、2in1、Tablet、Wearable设备。并且从5.1.1(19)开始，新增支持TV设备。

## 下载功能实现

1. 导入需要的模块，示例中除去发起请求以及响应错误处理，还需用到CoreFileKit中的fileIo，所以需导入以下模块。

   ```
   1. import { rcp } from '@kit.RemoteCommunicationKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   3. import { fileIo } from '@kit.CoreFileKit';
   ```
2. 定义下载路径，并创建相关配置。如还需访问应用文件，可以参考[应用文件](app-file.md)。

   ```
   1. //下载文件保存的文件夹路径，仅为示例，请按需求进行替换。
   2. const DOWNLOAD_TO_PATH = `/data/storage/el2/base/haps/entry/files`;
   3. // 创建了一个安全配置对象，其中remoteValidation设置为'skip'，表示将跳过远程验证。
   4. const securityConfig: rcp.SecurityConfiguration = {
   5. remoteValidation: 'skip'
   6. }

   8. // 创建了一个下载配置对象，其中kind设置为'folder'，表示下载的目标是文件夹，path设置为之前定义的DOWNLOAD_TO_PATH。
   9. let downloadToFile: rcp.DownloadToFile = {
   10. kind: 'folder',
   11. path: DOWNLOAD_TO_PATH
   12. }

   14. // 创建一个HTTP会话，其中请求配置包括传输超时设置和安全配置（配置可自定义）
   15. const session = rcp.createSession({
   16. requestConfiguration: {
   17. transfer: { timeout: { connectMs: 6000, transferMs: 6000, inactivityMs: 6000 } },
   18. security: securityConfig
   19. }
   20. })
   ```
3. 检查目标路径是否存在，如果存在，则先删除该路径，以确保下载的文件不会覆盖已存在的文件；最后发起请求，使用创建的会话执行下载操作，将“https://example.com/test.png”这个URL的内容下载到指定的本地路径。如果下载成功，会输出成功信息；如果失败，会输出错误信息。

   ```
   1. // 检查目标路径是否存在
   2. if (fileIo.accessSync(DOWNLOAD_TO_PATH)) {
   3. fileIo.rmdirSync(DOWNLOAD_TO_PATH);
   4. }
   5. // 发起请求，执行下载操作，这里的"https://example.com/test.png"网址为示例图片网址，模拟下载图片场景
   6. session.downloadToFile('https://example.com/test.png', downloadToFile)
   7. .then((response: rcp.Response) => {
   8. console.info(`Successfully received the response, statusCode: ${JSON.stringify(response.statusCode)}`);
   9. }).catch((err: BusinessError) => {
   10. console.error(`Failed, the error code is ${err.code}, error data is ${err.data}`)
   11. })
   ```

## 上传功能实现

1. 导入需要的模块，示例中除去发起请求以及响应错误处理，还需用到CoreFileKit中的fileIo，需导入以下模块。

   ```
   1. import { rcp } from '@kit.RemoteCommunicationKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   3. import { fileIo } from '@kit.CoreFileKit';
   ```
2. 定义Session配置，定义一个名为SESSION\_CONFIG的对象，用于配置请求会话。配置包括传输超时和安全设置，如远程验证和TLS版本。

   ```
   1. let SESSION_CONFIG: rcp.SessionConfiguration = {
   2. requestConfiguration: {
   3. transfer: {
   4. timeout: {
   5. connectMs: 6000
   6. }
   7. },
   8. security: {
   9. remoteValidation: 'skip',
   10. tlsOptions: {
   11. tlsVersion: 'TlsV1.3'
   12. }
   13. }
   14. }
   15. }
   ```
3. 定义FdReadFile类，用于读取文件描述符（File Descriptor）指向的文件。read方法异步读取指定的ArrayBuffer缓冲区，并返回实际读取的字节数。

   ```
   1. class FdReadFile {
   2. readonly fd: number;

   4. constructor(fd: number) {
   5. this.fd = fd;
   6. }

   8. async read(buffer: ArrayBuffer): Promise<number> {
   9. return fileIo.read(this.fd, buffer);
   10. }
   11. }
   ```
4. 创建会话并打开文件，以只读模式打开一个文件。fileIo.openSync方法返回一个文件描述符，如果打开失败，程序会打印错误信息并返回。

   ```
   1. const session = rcp.createSession(SESSION_CONFIG);
   2. const file = fileIo.openSync('/data/storage/el1/bundle/entry_test/resources/resfile/upload_file.txt',
   3. fileIo.OpenMode.READ_ONLY);
   4. if (!file) {
   5. console.error('fileIo.openSync failed');
   6. return;
   7. }
   ```
5. 读取文件，创建一个FdReadFile实例，并分配一个缓冲区来读取文件。read方法异步执行，等待文件读取完成。

   ```
   1. const fdReadFile = new FdReadFile(file.fd);
   2. const buffer = new ArrayBuffer(1024 * 1024); // 假设文件大小为1MB
   3. await fdReadFile.read(buffer);
   ```
6. 上传文件，使用会话的uploadFromFile方法将文件上传到指定的URL。UploadFromFile构造函数接受一个文件描述符读取文件。上传成功或失败时，会分别打印相应的信息。

   ```
   1. session.uploadFromFile('https://httpbin.org/anything', new rcp.UploadFromFile(fdReadFile))
   2. .then((response: rcp.Response) => {
   3. console.info(`Upload succeeded: ${response}`)
   4. })
   5. .catch((err: BusinessError) => {
   6. console.error(`Upload failed: error code is ${err.code}, error data is ${err.data}`)
   7. });
   ```
7. 关闭文件和会话，释放资源。

   ```
   1. fileIo.closeSync(file.fd);
   2. session.close();
   ```
