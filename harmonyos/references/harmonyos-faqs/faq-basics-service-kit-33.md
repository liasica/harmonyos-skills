---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-basics-service-kit-33
title: request.downloadFile如何暂停、恢复下载
breadcrumb: FAQ > 系统开发 > 基础功能 > 基础服务（Basics Service） > request.downloadFile如何暂停、恢复下载
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:39+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:e27d3ddfe84988bca800b4b52b7805b3d1aa0e9477436836fb71eae22b2949e2
---

## 问题现象

request.downloadFile接口下载文件怎么暂停、恢复下载？

## 背景知识

[request](../harmonyos-references/js-apis-request.md)模块给应用提供上传下载文件、后台传输代理的基础能力，其中[request.downloadFile](../harmonyos-references/js-apis-request.md#requestdownloadfile9-1)提供了异步方法下载文件能力。request.downloadFile方法的参数类型[DownloadConfig](../harmonyos-references/js-apis-request.md#downloadconfig)用于设置下载任务的信息配置，包括待下载地址url、下载后缓存的沙盒路径filePath、请求头header等。

## 解决方案

* 可以用request.downloadFile创建的DownloadTask下载任务中[suspend](../harmonyos-references/js-apis-request.md#suspend9-1)、[restore](../harmonyos-references/js-apis-request.md#restore9)接口对下载任务进行暂停和恢复。

  ```screen
  import { BusinessError, request, systemDateTime } from '@kit.BasicServicesKit';
  import { common } from '@kit.AbilityKit';

  interface DownloadResult {
    isSuccess: boolean,
    msg: string
  }
  @Entry
  @Component
  struct downloadFileCase {
    // 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
    context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    // 需要手动将url替换为真实服务器的HTTP协议地址
    downloadUrl: string =
      'http://xxx/xxx.mp4';
    @State filePath: string = '';
    @State downloadTask: request.DownloadTask | undefined = undefined;

    DownloadFile(url: string, savePath: string): Promise<DownloadResult> {
      return new Promise(async () => {
        const fileName = `${systemDateTime.getTime(true)}.mp4`;
        this.filePath = savePath + '/' + fileName;
        console.info('filePath:', JSON.stringify(this.filePath));
        this.downloadTask = await request.downloadFile(this.context, {
          url,
          filePath: this.filePath,
        });
      });
    }
    build() {
      Column({ space: 10 }) {
        Button('download下载').onClick(() => {
          this.DownloadFile(this.downloadUrl, `${this.context.filesDir}/testDir`);
        });
        Button('download暂停').onClick(() => {
          // 暂停下载
          if (!this.downloadTask) return;
          try {
            this.downloadTask.suspend();
            console.info(`Succeeded in pause the download task.`);
          } catch (err) {
            console.error(`Failed to pause the download task. Code: ${err}, message: ${err.message}`);
          }
        });
        Button('download继续').onClick(() => {
          // 继续下载
          if (!this.downloadTask) return;

          this.downloadTask.restore().then((result: boolean) => {
            console.info(`Succeeded in resuming the download task.${result.valueOf()}`);
          }).catch((err: BusinessError) => {
            console.error(`Failed to resume the download task. Code: ${err.code}, message: ${err.message}`);
          });
        });
      }
      .height('100%')
      .width('100%');
    }
  }
  ```

* 若想使用request.agent.create创建下载任务，也可用[pause](../harmonyos-references/js-apis-request.md#pause10)、[resume](../harmonyos-references/js-apis-request.md#resume10)接口来实现下载任务的暂停与恢复，暂停任务后会同步释放HTTP连接。

  ```screen
  import { BusinessError, request } from '@kit.BasicServicesKit';
  import { common } from '@kit.AbilityKit';

  @Entry
  @Component
  struct RequestAgentDemo {
    context = this.getUIContext().getHostContext() as common.UIAbilityContext;

    @State downloadTask: request.agent.Task | null = null;
    @State progressInfo: string = "等待开始...";

    // 配置对象
    config: request.agent.Config = {
      action: request.agent.Action.DOWNLOAD,
      url: 'http://xxx/xxx.mp4',
      mode: request.agent.Mode.BACKGROUND,
      overwrite: true, // 建议设为 true，方便多次测试
      method: "GET",
      saveas: "./" // 下载到应用私有目录
    };

    build() {
      RelativeContainer() {
        Column({ space: 20 }) {
          Text(this.progressInfo)
            .fontSize(16)
            .textAlign(TextAlign.Center)
            .width('90%')

          Row({ space: 10 }) {
            // 1. 开始按钮
            Button('开始')
              .onClick(() => {
                // 防止重复创建
                if (this.downloadTask) return;
                request.agent.create(this.context, this.config)
                  .then((task: request.agent.Task) => {
                    this.downloadTask = task;

                    // 注册监听（为了看效果）
                    task.on('progress', (progress) => {
                      // 进度显示
                      this.progressInfo = `进度: ${progress.processed}/${progress.sizes[0]}`;
                    });
                    task.on('completed', () => {
                      this.progressInfo = "下载完成";
                      this.downloadTask = null; // 下载完重置
                    });
                    task.on('failed', (err) => {
                      this.progressInfo = `失败: ${JSON.stringify(err)}`;
                    });

                    // 启动任务
                    task.start((err: BusinessError) => {
                      if (err) {
                        console.error(`Start failed: ${err.message}`);
                        return;
                      }
                      console.info(`Succeeded in starting task. tid: ${task.tid}`);
                      this.progressInfo = "下载已启动";
                    });
                  })
                  .catch((err: BusinessError) => {
                    console.error(`Create failed: ${err.message}`);
                  });
              })

            // 2. 暂停按钮
            Button('暂停')
              .onClick(() => {
                if (!this.downloadTask) return;

                this.downloadTask.pause((err: BusinessError) => {
                  if (err) {
                    console.error(`Pause failed: ${err.message}`);
                  } else {
                    console.info('Succeeded in pausing task.');
                    this.progressInfo = "已暂停";
                  }
                });
              })

            // 3. 重启（恢复）按钮
            Button('恢复')
              .onClick(() => {
                if (!this.downloadTask) return;
                this.downloadTask.resume((err: BusinessError) => {
                  if (err) {
                    console.error(`Resume failed: ${err.message}`);
                  } else {
                    console.info('Succeeded in resuming task.');
                    this.progressInfo = "已恢复下载";
                  }
                });
              })
          }
          .justifyContent(FlexAlign.Center)
          .width('100%')
        }
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
      }
      .height('100%')
      .width('100%')
    }
  }
  ```

## 常见FAQ

Q：APP在下载文件过程中，用户杀死APP进程，request.downloadFile这个API支不支持下次从已下载的部分文件继续下载？

A：request.downloadFile接口是后台任务，APP退出后，实际还在继续下载，APP再启动后，如果再调用一次request.downloadFile接口，就会新创建一个任务，因为已经有存在下载的文件，所以创建新的任务会因为已存在文件而失败。

Q：如果request.downloadFile不支持断点续传，哪个API支持？

A：如果要实现从已下载的部分文件继续下载，则可以使用request.agent.create创建下载任务使用断点续传，在create任务时记录Task任务id。后续重启应用后，通过request.agent.getTask获取任务，然后使用request.agent.show查询任务状态，如果任务正在进行，重新挂一遍监听回调就行。

Q：使用request.agent.create并发下载大小不一的文件时，大文件任务是否会对系统资源产生明显占用？是否有针对大文件下载的管理或限流方案，以避免小文件下载因资源竞争而被阻塞？

A：可通过[request.agent.Config](../harmonyos-references/js-apis-request.md#requestagentconfig10)中的priority参数设置任务的优先级。前台任务的优先级比后台任务高。任务模式相同的情况下，该配置项的数字越小优先级越高，默认值为0，低优先级任务不会阻塞高优先级任务。

Q：request.agent.Config中的priority参数设置后，可以再次修改吗？

A：config是在任务创建前设置的，任务创建后再修改config中配置，不会影响已创建好的任务。
