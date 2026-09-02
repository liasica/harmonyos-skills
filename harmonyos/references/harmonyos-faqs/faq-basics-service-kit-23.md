---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-basics-service-kit-23
title: request.downloadFile下载文件失败
breadcrumb: FAQ > 系统开发 > 基础功能 > 基础服务（Basics Service） > request.downloadFile下载文件失败
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:39+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:be0034306bae09fc2b4545082cee9de4f8a819139d577afb8e237a80a941cff6
---

## 问题现象

* 问题一：报错信息：Failed to request the download. err: {"code":13400001}，提示操作文件异常，问题场景代码如下：

  ```ts
   // 场景一
   let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
   let filesDir = context.filesDir;
   try {
     const filePath = `${filesDir}/xxx/abc.zip`
     await request.downloadFile(context, { url: this.URL, filePath:filePath })
   } catch (error) {
     console.error(`Failed to request the download. Code: ${error.code}, message: ${error.message}`);
   }

   // 场景二
   request.downloadFile(context, {
     url: 'https://www.example.com/xxxx.jpg', 
     filePath: '/data/storage/el2/base/files/test/test.jpg'
   }

   // 场景三
   let url = 'https://www.example.com/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.docx';
   request.downloadFile(context, { url:url}).then((data: request.DownloadTask) => {
     let downloadTask: request.DownloadTask = data;
   }).catch((err: BusinessError) => {
     console.error(`Failed to request the download. Code: ${err.code}, message: ${err.message}`);
   })
  ```
* 问题二：使用request.downloadFile下载时，部分文件正常下载，部分文件下载报错（使用浏览器正常下载），错误信息：bad file path GetFd File exists and other error，error = 8。下载时会进fail回调，问题代码如下：

  ```ts
  request.downloadFile(context, { url: this.url, filePath: tempDir }).then((downloadTask: request.DownloadTask) => {
    downloadTask.on('complete', () => {
      console.info('下载完成');
    });
    downloadTask.on('fail', (err) => {
      console.error(`下载失败:${err}`);
    });
  });
  ```
* 问题三：第一次下载文件成功、失败后，再次下载报[13400002文件路径异常](../harmonyos-references/errorcode-request.md#section13400002-文件路径异常)错误。

## 背景知识

* [request](../harmonyos-references/js-apis-request.md)模块给应用提供上传下载文件、后台代理传输的基础功能，主要适用场景：需后台下载、断点续传、多文件或大文件上传。
* request模块提供了两套上传下载能力：
  1. [request.uploadFile](../harmonyos-references/js-apis-request.md#requestuploadfile9)接口用于上传任务，支持自定义请求头，可以用on('headerReceive')接口接收上传成功或者失败服务端返回的结果。
  2. [request.downloadFile](../harmonyos-references/js-apis-request.md#requestdownloadfile9)接口用于下载任务，支持配置后台下载（后台任务下载成功或者失败界面都会有弹窗提示，前台任务没有任何提示信息），支持暂停恢复下载，用on('complete')成功回调之后可以做一些业务操作，比如将图片保存到相册、进行页面展示等。
  3. [request.agent.create](../harmonyos-references/js-apis-request.md#requestagentcreate10)接口涵盖了uploadFile、downloadFile所有支持的能力，其支持断点续传、重定向（redirect）、代理（proxy）、覆盖已存在的文件（overwrite）等。
* 在普通应用（也称三方应用）视角下，不仅可见的目录与文件数量限制了范围，并且可见的目录与文件路径也与系统进程等其他进程看到的不同。我们将普通应用视角下看到的“[应用沙箱目录](../harmonyos-guides/app-sandbox-directory.md#应用沙箱目录与应用沙箱路径)”下某个文件或某个具体目录的路径，称为“[应用沙箱路径](../harmonyos-guides/app-sandbox-directory.md#应用沙箱目录与应用沙箱路径)”。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/JpQZGIRxT0C89sRsEa8htA/zh-cn_image_0000002628773308.png "点击放大")

## 解决方案

* 问题一：[13400001](../harmonyos-references/errorcode-request.md#section13400001-文件操作异常)操作文件异常。
  + 场景一：filePath参数必须指向已存在的文件夹或具体文件路径，若文件夹不存在，接口不会自动创建。可以通过[fs.mkdir](../harmonyos-references/js-apis-file-fs.md#fileiomkdir)接口在沙箱路径下创建新文件，使用[fs.access](../harmonyos-references/js-apis-file-fs.md#fileioaccess)接口判断文件、目录存在后再执行下载任务。
  + 场景二：request接口中的filePath参数配置只支持沙箱路径，不支持用户uri地址。将用户uri地址修改为通过filesDir、cacheDir获取应用的文件路径即可，下载完成后IDE中查看下载文件位置：

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/8y214lPbTB2tAGYSctIn-A/zh-cn_image_0000002658972625.png "点击放大")
  + 场景三：系统默认以url里最后一个'/'后面的字符串作为文件名，当文件名过长（最大支持255字节）时会导致报错，可通过配置filePath自定义文件名解决。

* 问题二：
  + 可以在下载任务的请求头header中添加User-Agent信息，来模拟浏览器下载行为，完成下载任务。User-Agent介绍及获取方式参考：[User-Agent开发指导示例](../harmonyos-guides/web-default-useragent.md)。
  + error = 8：API version 12及以下版本，系统仅支持串行地尝试连接域名相关IP，不支持单个IP的连接时间控制。若DNS返回的第一个IP被阻塞，可能会由于握手超时导致ERROR\_UNKNOWN错误，建议调用[requestInStream](../harmonyos-references/js-apis-http.md#requestinstream10)方法进行文件下载。
* 问题三：[13400002](../harmonyos-references/errorcode-request.md#section13400002-文件路径异常)文件路径异常。
  + 调用downloadFile接口时，会先根据[DownloadConfig](../harmonyos-references/js-apis-request.md#downloadconfig)中的uri或者filePath创建文件，下载成功或失败均不会自动删除该文件，若要重复下载需要先使用[fs.unlinkSync](../harmonyos-references/js-apis-file-fs.md#fileiounlinksync)删除该文件。
* 文件下载完整示例如下：

  ```ts
  import { request, BusinessError } from '@kit.BasicServicesKit';
  import { common } from '@kit.AbilityKit';
  import fs from '@ohos.file.fs';
  import { promptAction } from '@kit.ArkUI';

  interface DownloadResult {
    isSuccess: boolean,
    msg: string
  }

  @Entry
  @Component
  struct Index {
    context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    downloadUrl: string = ''; // 需要手动将url替换为真实服务器的HTTP协议地址
    @State filePath: string = '';
    @State current: number = 0;
    @State total: number = 0;
    @State downloadTask: request.DownloadTask = {} as request.DownloadTask;
    @State downloadImage: string = '';

    // 创建文件
    createFolder(url: string) {
      let isExist = fs.accessSync(`${this.context.filesDir}/testDir`, fs.AccessModeType.EXIST);
      if (isExist) {
        console.info('文件夹已存在');
      } else {
        fs.mkdir(`${this.context.filesDir}/testDir`).then(() => {
          console.info('mkdir succeed');
        }).catch((err: BusinessError) => {
          console.error('mkdir failed with error message: ' + err.message + ', error code: ' + err.code);
        });
      }
      this.DownloadFile(url, `${this.context.filesDir}/testDir`).then((result) => {
        if (result.isSuccess) {
          promptAction.openToast({ message: '下载成功' });
        } else {
          console.error(`失败: ${result.msg}`);
          promptAction.openToast({ message: '下载失败，请查看日志' });
        }
      });
    }

    DownloadFile(url: string, savePath: string): Promise<DownloadResult> {
      return new Promise(async (resolve, reject) => {
        this.filePath = savePath + '/test.png';
        this.downloadTask = await request.downloadFile(this.context, { url, filePath: this.filePath });
        // 监听下载进度
        this.downloadTask.on('progress', (receivedSize: number, totalSize: number) => {
          this.current = receivedSize;
          this.total = totalSize;
        });

        // 监听下载是否失败
        this.downloadTask.on('fail', (err) => {
          if (err) {
            return reject({ isSuccess: false, msg: '下载失败' });
          }
        });

        // 监听下载是否完成
        this.downloadTask.on('complete', () => {
          this.downloadImage = 'file://' + this.filePath;
          return resolve({ isSuccess: true, msg: 'Download task completed.' });
        });
      });
    }

    build() {
      Column({ space: 16 }) {
        Row({ space: 16 }) {
          Progress({ value: this.current, total: this.total, type: ProgressType.ScaleRing })
            .width(100)
            .height(100)
            .backgroundColor(Color.Black)
            .style({ strokeWidth: 15, scaleCount: 20, scaleWidth: 5 });
          Row() {
            Image(this.downloadImage);
          }.width(100).height(100);
        };

        Column({ space: 16 }) {
          Button('download下载').onClick(() => {
            this.createFolder(this.downloadUrl);
          });
          Button('删除沙箱内的文件').onClick(() => {
            if (this.filePath === `${this.context.filesDir}/testDir/test.png`) {
              fs.unlinkSync(this.filePath);
              promptAction.openToast({ message: '文件已删除' });
            } else {
              promptAction.openToast({ message: '要删除的文件不存在' });
            }
          });
        };
      }
      .height('100%')
      .width('100%');
    }
  }
  ```

## 常见FAQ

Q：下载地址不可用，调用request下载，无状态返回。

A：下载失败都会走到失败的回调中，用downloadFile、request.agent可以分别订阅on('fail')、on('failed')任务失败事件。

Q：使用request.downloadFile下载文件后，再次下载同名无法直接覆盖？

A：downloadFile没有overwrite参数，可更换request.agent接口，支持配置覆盖同名文件，或在文件命名时使用时间戳来规避。

Q：下载bin文件保存为txt出现乱码。

A：使用记事本打开bin文件时，会出现乱码的情况，因为bin文件是一种二进制文件，而记事本是一种文本编辑器，无法正确解析二进制数据，直接下载链接中的文件使用记事本打开也是乱码的。

Q：系统打开VPN导致ohos.request下载接口失败，其它RCP接口请求可以正常使用。

A：上传下载是在独立的SA进程，所以走VPN的应用不能使用ohos.request接口，RCP是在应用进程传输数据。

Q：request.downloadFile调用含有重定向的url文件链接报错：Failed to download the task. Code: 6？

A：request.downloadFile调用含有重定向的url文件链接时，重定向Location头字段里的url不会自动适配百分比编码，建议在服务端返回的响应中，把Location头字段的url改成百分比编码后，调用request.downloadFile即可，也可以调用RCP中[downloadToFile](../harmonyos-references/remote-communication-rcp.md#downloadtofile)方法直接下载文件。

Q：下载文件使用https链接下载失败，改成http可以下载成功。

A：https和http主要区别在于https服务器需要额外进行TLS握手，然后连接的是443端口，由下方日志可以看出是openssl报的，证书校验失败，检查服务端发来的证书有没有问题，是不是通用的：

```screen
03-07 09:22:34.906   3171-3218     C01C50/downloa...equestService  download_server       E     Task 791103119 HttpClientError { ErrorKind: Connect, Cause: Custom { kind: Other, error: SslError { code: SslErrorCode(1), internal: Some(Ssl(ErrorStack([StackError { code: 369098857, file: "", line: 0, func: Some("ossl_store_get0_loader_int"), data: Some("scheme=file") }, StackError { code: 2147483650, file: "", line: 0, func: Some("file_open"), data: Some("calling stat(/system/etc/certs)") }, StackError { code: 369098857, file: "", line: 0, func: Some("ossl_store_get0_loader_int"), data: Some("scheme=file") }, StackError { code: 2147483650, file: "", line: 0, func: Some("file_open"), data: Some("calling stat(/system/etc/certs)") }, StackError { code: 369098857, file: "", line: 0, func: Some("ossl_store_get0_loader_int"), data: Some("scheme=file") }, StackError { code: 2147483650, file: "", line: 0, func: Some("file_open"), data: Some("calling stat(/system/etc/certs)") }, StackError { code: 167772294, file: "", line: 0, func: Some("tls_post_process_server_certificate"), data: None }]))) } } }
```

Q：如何在后台显示request.downloadFile下载文件的进度？

A：可以通过[DownloadConfig](../harmonyos-references/js-apis-request.md#downloadconfig)的background参数控制是否在后台显示文件下载进度。

Q：在PC上进行抓包时，request.downloadFile是否提供添加用户级证书的方法？

A：request.downloadFile当前不支持添加抓包所需的用户级证书。

Q：很多个音频文件（amr后缀）通过request.downloadFile下载时，其中1个音频文件下载后无法播放，播放时错误码5400106。

A：当前服务端返回的文件为压缩格式，客户端需下载后手动改为.zip并解压，再将解压出的文件重命名为.amr才能播放，服务端提供原始的AMR音频文件即可。

Q：request.downloadFile下载文件报错SSL alert number 40，如何解决？

A：定位分析报错SSL alert number 40，此错误是服务端使用了不安全的加密套件，需要更换成安全加密套件，比如GCM。

判断服务端是否使用安全加密套件方式：使用如下命令如果能运行成功，说明服务端是使用了安全加密套件，即可解决该错误：

```screen
openssl s_client -connect pmbank.trcbank.com.cn:8999 -cipher
"DEFAULT:!aNULL:!eNULL:!MD5:!3DES:!DES:!RC4:!IDEA:!SEED:!aDSS:!SRP:!PSK:!SHA1:!CBC"
```

Q：服务端返回http错误码如：404、403时，on('fail')返回的是8，怎么查看具体的错误码？

A：目前没有接口可以直接获取到请求错误码，可以使用[DownloadTask.getTaskInfo](../harmonyos-references/js-apis-request.md#gettaskinfo9)获取下载任务信息，通过下载任务id，在hilog日志中查询下载任务的response信息。

```screen
02-03 19:06:54.622 14358 14398 I C01C50/download_server/RequestService: 551999128 response 404 Not Found
```

Q：压力测试时调用request.downloadFile会出现错误码21900004。

A：[21900004](../harmonyos-references/errorcode-request.md#section21900004-应用任务队列已满)错误指应用任务队列已满，downloadFile是后台任务，单个应用后台任务，运行中的(指的完成、失败、删除之外的状态)任务，最多1000个。

Q：downloadFile是否支持在传输过程中携带Cookie用于身份验证？

A：目前downloadFile暂未提供Cookie携带能力，使用可能导致TCP连接中断，影响文件正常下载。

Q：request.downloadFile资源下载断网情况下不响应downloadTask.on('fail)回调。

A：request.downloadFile默认在网络异常时会进入等待状态；建议切换成request.agent.create，retry自动重试参数设置为false时断网会进入fail回调。
