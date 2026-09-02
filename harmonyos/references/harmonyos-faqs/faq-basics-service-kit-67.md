---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-basics-service-kit-67
title: 如何使用request.agent实现文件断点续传
breadcrumb: FAQ > 系统开发 > 基础功能 > 基础服务（Basics Service） > 如何使用request.agent实现文件断点续传
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:40+08:00
doc_updated_at: 2026-07-09
content_hash: sha256:7af81ff5263197d2557f1686729eb7df53d1d063bcfd264ff02e754ec6711626
---

## 问题现象

使用request.agent下载文件过程中因为网络问题或者手动停止后，使用request.agent.Task.resume()无法继续下载，使用request.agent.Task.start()会重新开始下载，不能从中断的进度继续下载。

## 背景知识

* [request.agent.Config](../harmonyos-references/js-apis-request.md#requestagentconfig10)：设置下载配置信息，参数begins设置下载时请求读取服务器开始下载文件时的起点位置。
* [request.agent.show](../harmonyos-references/js-apis-request.md#requestagentshow10)：可以根据任务id查询任务的详细信息。查询到中断的任务信息。
* [request.agent.getTask](../harmonyos-references/js-apis-request.md#requestagentgettask11)：根据任务id查询任务，获取任务配置信息。
* 下载需要使用到网络能力，需要申请[ohos.permission.INTERNET](../harmonyos-guides/permissions-for-all.md#ohospermissioninternet)权限。

## 解决方案

1. 任务中断后使用request.agent.show()接口查询传输中断的任务信息，记录文件的断点进度和文件路径。

   从中断的任务Task中获取配置信息，用于创建一个新的下载任务，下载断点后的文件：修改文件下载时的起点位置为断点进度位置，修改存储路径。

   ```ts
   Continue() {
     request.agent.show(this.downloadTask!.tid, (err: BusinessError, taskInfo: request.agent.TaskInfo) => {
       if (err) {
         console.error(`Failed to show a upload task, Code: ${err.code}, message: ${err.message}`);
         return;
       }
       this.oldFileLen = taskInfo.progress.processed;
       let config = this.downloadTask!.config;
       this.oldFilePath = config.saveas!;
       config.begins = taskInfo.progress.processed;
       config.saveas = `${config.saveas}.1`;
       request.agent.create(this.context, config)
         .then((task: request.agent.Task) => {
           this.downloadTask = task;
           this.InitEvent(task);
           task.start((err: BusinessError) => {
             if (err) {
               console.error(`Start failed: ${err.message}`);
               return;
             }
             console.info(`Succeeded in starting task. tid: ${task.tid}`);
             this.progressInfo = '下载已启动';
           });
         })
         .catch((err: BusinessError) => {
           console.error(`Create failed: ${err.message}`);
         });
     });
   }
   ```
2. 在新的下载任务完成后，将断点前的文件和断点后的临时文件拼接，获取拼接后最终文件的哈希值，检测文件完整性。

   ```ts
   setFile(length: number) {
     let oldFile: fs.File | undefined = undefined;
     let newFile: fs.File | undefined = undefined;
     try {
       oldFile = fs.openSync(this.oldFilePath, fs.OpenMode.CREATE | fs.OpenMode.READ_WRITE);
       newFile = fs.openSync(this.downloadTask?.config.saveas, fs.OpenMode.CREATE | fs.OpenMode.READ_WRITE);
       let bufsize = 4096;
       let buf = new ArrayBuffer(bufsize);
       let len = 0;
       let fileOffset = 0;
       len = fs.readSync(newFile.fd, buf, { offset: fileOffset, length: bufsize });
       while (len) {
         fs.writeSync(oldFile.fd, buf, { offset: this.oldFileLen + fileOffset, length: len });
         fileOffset += len;
         if ((length - fileOffset) < bufsize) {
           bufsize = length - fileOffset;
         }
         len = fs.readSync(newFile.fd, buf, { offset: fileOffset, length: bufsize });
       }
       hash.hash(this.oldFilePath, 'sha256').then((str: string) => {
         this.promptAction.showToast({
           message: `下载完成,文件哈希值${str}`
         });
         console.info('calculate file hash succeed:' + str);
       }).catch((err: BusinessError) => {
         console.error(`calculate file hash failed with error message: ${err.message}, error code: ${err.code}`);
       });
     } catch (error) {
       console.error(`getRawFdSync failed, error code: ${error.code}, message: ${error.message}.`);
     } finally {
       if (newFile) {
         fs.close(newFile.fd);
       }
       if (oldFile) {
         fs.close(oldFile.fd);
       }
     }
   }
   ```

完整示例参考如下：

```ts
import { BusinessError, request } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import { fileIo as fs, hash } from '@kit.CoreFileKit';
import { PromptAction } from '@kit.ArkUI';

@Entry
@Component
struct RequestAgentDemo {
  context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  @State taskIds: string[] = [];
  promptAction: PromptAction = this.getUIContext().getPromptAction();

  aboutToAppear(): void {
    let filter: request.agent.Filter = {
      action: request.agent.Action.DOWNLOAD
    };
    request.agent.search(filter).then((data: Array<string>) => {
      this.addTaskId(data);
    }).catch((err: BusinessError) => {
      console.error(`Failed to search a upload task, Code: ${err.code}, message: ${err.message}`);
    });
  }

  addTaskId(data: Array<string>) {
    for (let i = 0; i < data.length; i++) {
      this.taskIds.push(data[i]);
    }
  }

  build() {
    Column({ space: 20 }) {
      Row({ space: 10 }) {
        Button('创建任务')
          .onClick(() => {
            let fileName = `XXX`; //需要替换为开发者需要的资源名称
            // 配置对象
            let config: request.agent.Config = {
              action: request.agent.Action.DOWNLOAD,
              url: 'https://XXX', //需要替换为开发者需要的资源链接
              mode: request.agent.Mode.FOREGROUND,
              overwrite: true,
              method: 'POST',
              title: fileName,
              begins: 0,
              saveas: `XXXXXXXX`//需要替换为开发者需要的资源保存路径
            };
            request.agent.create(this.context, config)
              .then((task: request.agent.Task) => {
                this.taskIds.push(task.tid);
                task.start((err: BusinessError) => {
                  if (err) {
                    console.error(`Start failed: ${err.message}`);
                    return;
                  }
                  console.info(`Succeeded in starting task. tid: ${task.tid}`);
                });
              })
              .catch((err: BusinessError) => {
                console.error(`Create failed: ${err.message}`);
              });
          });
      }
      .justifyContent(FlexAlign.Center)
      .width('100%');

      List({ space: 10 }) {
        ForEach(this.taskIds, (item: string) => {
          ObjectBuild({ taskId: item });
        }, (item: string) => item);
      }
      .alignListItem(ListItemAlign.Center)
      .width('98%');
    }
    .alignRules({
      center: { anchor: '__container__', align: VerticalAlign.Top },
      middle: { anchor: '__container__', align: HorizontalAlign.Center }
    })
    .height('100%')
    .width('100%');
  }
}

@Component
struct ObjectBuild {
  context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  promptAction: PromptAction = this.getUIContext().getPromptAction();
  taskId: string = '';
  @State downloadTask: request.agent.Task | null = null;
  oldFileLen: number = 0;
  oldFilePath: string = '';
  @State downloadState: request.agent.State = 0;
  @State progress: number = 0;
  @State progressInfo: string = '';
  @State downloadName: string = '';

  aboutToAppear(): void {
    request.agent.show(this.taskId, (err: BusinessError, taskInfo: request.agent.TaskInfo) => {
      if (err) {
        console.error(`Failed to show a upload task, Code: ${err.code}, message: ${err.message}`);
        return;
      }
      this.downloadName = taskInfo.title;
      this.progress =
        (taskInfo.progress.processed + this.oldFileLen) / (taskInfo.progress.sizes[0] + this.oldFileLen) * 100;
      this.downloadState = taskInfo.progress.state;
    });
    request.agent.getTask(this.context, this.taskId)
      .then((task: request.agent.Task) => {
        this.downloadTask = task;
        this.oldFileLen = task.config.begins!;
        // 注册监听
        this.InitEvent(task);
      })
      .catch((err: BusinessError) => {
        console.error(`Create failed: ${err.message}`);
      });
  }

  build() {
    Row() {
      Column() {
        Row() {
          Text(this.downloadName)
            .fontSize(16)
            .textAlign(TextAlign.Center);
          Text(this.progressInfo)
            .fontSize(16)
            .textAlign(TextAlign.Center);
        }
        .alignItems(VerticalAlign.Center)
        .justifyContent(FlexAlign.SpaceBetween)
        .width('100%');

        Progress({ value: this.progress, total: 100, type: ProgressType.Linear })
          .style({ strokeWidth: 10, enableSmoothEffect: true })
          .margin({ top: 3 });

        Row() {
          Button('断点续传')
            .onClick(() => {
              request.agent.show(this.taskId, (err: BusinessError, taskInfo: request.agent.TaskInfo) => {
                if (err) {
                  console.error(`Resume failed: ${err.message}`);
                }
                this.downloadState = taskInfo.progress.state;
                if (this.downloadState === request.agent.State.STOPPED ||
                  this.downloadState === request.agent.State.FAILED) {
                  this.Continue();
                }
              });

            });
          Button('暂停下载')
            .onClick(() => {
              if (!this.downloadTask) {
                return;
              }
              this.downloadTask.pause((err: BusinessError) => {
                if (err) {
                  this.promptAction.showToast({
                    message: `Resume failed: ${err.message}`
                  });
                  console.error(`Resume failed: ${err.message}`);
                } else {
                  console.info('Succeeded in resuming task.');
                  this.progressInfo = '暂停下载';
                }
              });
            });
          Button('恢复下载')
            .onClick(() => {
              if (!this.downloadTask) {
                return;
              }
              this.downloadTask.resume((err: BusinessError) => {
                if (err) {
                  console.error(`Resume failed: ${err.message}`);
                  this.promptAction.showToast({
                    message: `Resume failed: ${err.message}`
                  });
                } else {
                  console.info('Succeeded in resuming task.');
                  this.progressInfo = '下载中';
                }
              });
            })
            .background();
        }
        .margin({ top: 3 })
        .width('100%')
        .alignItems(VerticalAlign.Center)
        .justifyContent(FlexAlign.SpaceBetween);
      }.width('90%')
      .justifyContent(FlexAlign.Start)
      .alignItems(HorizontalAlign.Center);
    };
  }
  Continue() {
    request.agent.show(this.downloadTask!.tid, (err: BusinessError, taskInfo: request.agent.TaskInfo) => {
      if (err) {
        console.error(`Failed to show a upload task, Code: ${err.code}, message: ${err.message}`);
        return;
      }
      this.oldFileLen = taskInfo.progress.processed;
      let config = this.downloadTask!.config;
      this.oldFilePath = config.saveas!;
      config.begins = taskInfo.progress.processed;
      config.saveas = `${config.saveas}.1`;
      request.agent.create(this.context, config)
        .then((task: request.agent.Task) => {
          this.downloadTask = task;
          this.InitEvent(task);
          task.start((err: BusinessError) => {
            if (err) {
              console.error(`Start failed: ${err.message}`);
              return;
            }
            console.info(`Succeeded in starting task. tid: ${task.tid}`);
            this.progressInfo = '下载已启动';
          });
        })
        .catch((err: BusinessError) => {
          console.error(`Create failed: ${err.message}`);
        });
    });
  }

  setFile(length: number) {
    let oldFile: fs.File | undefined = undefined;
    let newFile: fs.File | undefined = undefined;
    try {
      oldFile = fs.openSync(this.oldFilePath, fs.OpenMode.CREATE | fs.OpenMode.READ_WRITE);
      newFile = fs.openSync(this.downloadTask?.config.saveas, fs.OpenMode.CREATE | fs.OpenMode.READ_WRITE);
      let bufsize = 4096;
      let buf = new ArrayBuffer(bufsize);
      let len = 0;
      let fileOffset = 0;
      len = fs.readSync(newFile.fd, buf, { offset: fileOffset, length: bufsize });
      while (len) {
        fs.writeSync(oldFile.fd, buf, { offset: this.oldFileLen + fileOffset, length: len });
        fileOffset += len;
        if ((length - fileOffset) < bufsize) {
          bufsize = length - fileOffset;
        }
        len = fs.readSync(newFile.fd, buf, { offset: fileOffset, length: bufsize });
      }
      hash.hash(this.oldFilePath, 'sha256').then((str: string) => {
        this.promptAction.showToast({
          message: `下载完成,文件哈希值${str}`
        });
        console.info('calculate file hash succeed:' + str);
      }).catch((err: BusinessError) => {
        console.error(`calculate file hash failed with error message: ${err.message}, error code: ${err.code}`);
      });
    } catch (error) {
      console.error(`getRawFdSync failed, error code: ${error.code}, message: ${error.message}.`);
    } finally {
      if (newFile) {
        fs.close(newFile.fd);
      }
      if (oldFile) {
        fs.close(oldFile.fd);
      }
    }
  }
  InitEvent(task: request.agent.Task) {
    task.on('progress', (progress) => {
      this.progress = (progress.processed + this.oldFileLen) / (progress.sizes[0] + this.oldFileLen) * 100;
      this.downloadState = progress.state;
      if (progress.state === request.agent.State.RUNNING) {
        this.progressInfo = '下载中';
      } else if (progress.state === request.agent.State.PAUSED) {
        this.progressInfo = '暂停下载';
      }
      console.info(`Succeeded get progress：${progress}`);
    });
    task.on('completed', (progress) => {
      this.progressInfo = '下载完成';
      this.progress = (progress.processed + this.oldFileLen) / (progress.sizes[0] + this.oldFileLen) * 100;
      this.downloadState = progress.state;
      if (this.oldFileLen > 0) {
        this.setFile(progress.processed);
      } else {
        hash.hash(this.downloadTask?.config.saveas, 'sha256').then((str: string) => {
          this.promptAction.showToast({
            message: `下载完成,文件哈希值${str}`
          });
          console.info('calculate file hash succeed:' + str);
        }).catch((err: BusinessError) => {
          console.error(`calculate file hash failed with error message: ${err.message}, error code: ${err.code}`);
        });
      }
      this.downloadTask = null; // 下载完重置
    });
    task.on('failed', (err) => {
      this.progressInfo = '下载失败';
      this.promptAction.showToast({
        message: `下载失败: ${JSON.stringify(err)}`
      });
    });
    task.on('pause', (progress) => {
      this.progressInfo = '暂停下载';
      this.downloadState = progress.state;
    });
  }
}
```
