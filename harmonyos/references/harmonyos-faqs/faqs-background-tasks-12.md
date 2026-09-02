---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-background-tasks-12
title: 后台录音类型长时任务的实现指导方案
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 后台任务开发（Background Tasks） > 后台录音类型长时任务的实现指导方案
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:56+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:9437ba2e573769359d626bba0fbcfac011a59ecf4030307343d237a02118f487
---

## 问题现象

如何实现后台录音，结果保存到沙箱。

## 背景知识

* [AUDIO\_RECORDING](../harmonyos-guides/continuous-task.md#使用场景)：应用退至后台后，在后台需要长时间运行用户可感知的任务，如录制。为防止应用进程被挂起，导致对应功能异常，可以申请长时任务，使应用在后台长时间运行。
* [AVRecorder录制音频](../harmonyos-guides/using-avrecorder-for-recording.md)：使用AVRecorder实现音频录制功能，以“开始录制-暂停录制-恢复录制-停止录制”的一次流程为例。

## 解决方案

后台音频录制开发步骤：

1. 需要申请ohos.permission.KEEP\_BACKGROUND\_RUNNING和ohos.permission.MICROPHONE权限，配置方式请参见[声明权限](../harmonyos-guides/declare-permissions.md)。
2. 声明后台模式类型：

   在[module.json5配置文件](../harmonyos-guides/module-configuration-file.md)中abilities下的backgroundModes字段里，为需要使用长时任务的UIAbility声明相应的长时任务类型，配置文件中填写长时任务类型的[配置项](../harmonyos-guides/continuous-task.md#使用场景)。
3. 开发录制能力，包含权限申请，录制音频，以及保存到沙箱，可在列表中查看沙箱中存在的音频文件。在启动录制和结束录制的时候，开启和停止后台长时任务，以保障应用在后台时可以正常录音。

```ts
import { abilityAccessCtrl, common, PermissionRequestResult, Permissions, WantAgent, wantAgent } from '@kit.AbilityKit';
import { fileIo, fileUri, Filter } from '@kit.CoreFileKit';
import { media } from '@kit.MediaKit';
import { backgroundTaskManager } from '@kit.BackgroundTasksKit';

@Entry
@Component
struct Index {
  private context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
  textTimerController: TextTimerController = new TextTimerController();
  private format: string = 'mm:ss.SS';
  private filesDir: string = this.context.filesDir;
  @State recordFlag: boolean = true;
  @State continueFlag: boolean = true;
  @State fileNames: string[] = [];
  private curFile: fileIo.File | undefined = undefined;
  private avRecorder: media.AVRecorder | undefined = undefined;
  private avProfile: media.AVRecorderProfile = {
    audioBitrate: 100000, // 音频比特率
    audioChannels: 2, // 音频声道数
    audioCodec: media.CodecMimeType.AUDIO_AAC, // 音频编码格式，当前只支持aac
    audioSampleRate: 48000, // 音频采样率
    fileFormat: media.ContainerFormatType.CFT_MPEG_4A, // 封装格式，当前只支持m4a
  };
  private avConfig: media.AVRecorderConfig = {
    audioSourceType: media.AudioSourceType.AUDIO_SOURCE_TYPE_MIC, // 音频输入源，这里设置为麦克风
    profile: this.avProfile,
    url: '' // 参考应用文件访问与管理开发示例新建并读写一个文件
  };

  aboutToAppear() {
    let permissions: Array<Permissions> = ['ohos.permission.MICROPHONE'];
    this.reqPermissionsFromUser(permissions);
    this.getFileList();
  }

  build() {
    Column({ space: 10 }) {
      Column() {
        Text('录音').fontSize(24).fontWeight(500).fontColor(Color.Gray)
        TextTimer({ isCountDown: false, count: 30000, controller: this.textTimerController })
          .format(this.format)
          .fontColor(Color.Black)
          .fontSize(50)
          .onTimer((utc: number, elapsedTime: number) => {
            console.info('textTimer notCountDown utc is：' + utc + ', elapsedTime: ' + elapsedTime);
          })

        Row() {
          Image(this.recordFlag ? $r('app.media.ic_record_new') : $r('app.media.ic_recorder_stop'))
            .width(50)
            .height(50)
            .onClick(() => {
              if (this.recordFlag) {
                this.startRecordingProcess();
              } else {
                this.stopRecordingProcess();
              }
            })

          if (!this.recordFlag) {
            Image(this.continueFlag ? $r('app.media.ic_public_pause') : $r('app.media.ic_public_play_blank'))
              .width(50)
              .height(50)
              .onClick(() => {
                if (this.continueFlag) {
                  this.pauseRecordingProcess();
                } else {
                  this.resumeRecordingProcess();
                }
              })
          }
        }
        .width('100%')
        .justifyContent(FlexAlign.SpaceAround)
      }
      .padding(20)
      .borderRadius(16)
      .backgroundColor(Color.White)

      Column({ space: 5 }) {
        Button('文件列表').onClick(() => {
          this.getFileList();
        })

        Scroll() {
          List({ space: 5 }) {
            ForEach(this.fileNames, (item: string) => {
              ListItem() {
                Text(item)
                  .backgroundColor('#f1f3f5')
                  .padding({
                    left: 20,
                    right: 20,
                    top: 8,
                    bottom: 8
                  })
                  .width('100%')
                  .borderRadius(15);
              }
            });
          }
        }
        .scrollBar(BarState.Off)
      }
      .padding(12)
      .borderRadius(16)
      .backgroundColor(Color.White)
      .height('100%')
      .flexShrink(999)
    }
    .width('100%')
    .height('100%')
    .padding(12)
    .backgroundColor('#f1f3f5')
  }

  /* 注册audioRecorder回调函数 */
  setAudioRecorderCallback() {
    if (this.avRecorder != undefined) {
      // 状态机变化回调函数
      this.avRecorder.on('stateChange', (state: media.AVRecorderState) => {
        console.info(`AudioRecorder current state is ${JSON.stringify(state)}`);
      });
      // 错误上报回调函数
      this.avRecorder.on('error', (err: BusinessError) => {
        console.error(`AudioRecorder failed, code is ${err.code}, message is ${err.message}`);
      });
    }
  }

  getFile(): fileIo.File {
    const filePath = fileUri.getUriFromPath(this.filesDir + '/Audio_' + new Date().getTime() + '.mp4');
    let file: fileIo.File = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
    return file;
  }

  /* 开始录制对应的流程 */
  async startRecordingProcess() {
    try {
      if (this.avRecorder == undefined) {
        // 1.创建录制实例
        this.avRecorder = await media.createAVRecorder();
      }

      this.setAudioRecorderCallback();
      // 2.获取录制文件fd赋予avConfig里的url；参考FilePicker文档
      this.curFile = this.getFile();
      this.avConfig.url = 'fd://' + this.curFile.fd;
      // 3.配置录制参数完成准备工作
      await this.avRecorder.prepare(this.avConfig);
      // 4.开始录制
      this.textTimerController.start();
      await this.avRecorder.start();
      this.startContinuousTask();
      this.recordFlag = false;
    } catch (err) {
      console.error(`startRecordingProcess ${JSON.stringify(err)}`);
    }
  }

  /* 暂停录制对应的流程 */
  async pauseRecordingProcess() {
    if (this.avRecorder != undefined && this.avRecorder.state === 'started') { // 仅在started状态下调用pause为合理状态切换
      this.continueFlag = false;
      this.textTimerController.pause();
      await this.avRecorder.pause();
    }
  }

  /* 恢复录制对应的流程 */
  async resumeRecordingProcess() {
    if (this.avRecorder != undefined && this.avRecorder.state === 'paused') { // 仅在paused状态下调用resume为合理状态切换
      this.continueFlag = true;
      this.textTimerController.start();
      await this.avRecorder.resume();
    }
  }

  /* 停止录制对应的流程 */
  async stopRecordingProcess() {
    if (this.avRecorder != undefined) {
      // 1. 停止录制
      if (this.avRecorder.state === 'started' ||
        this.avRecorder.state === 'paused') { // 仅在started或者paused状态下调用stop为合理状态切换
        await this.avRecorder.stop();
      }
      // 2.重置
      this.recordFlag = true;
      await this.avRecorder.reset();
      this.textTimerController.reset();
      // 3.释放录制实例
      await this.avRecorder.release();
      // 4.关闭录制文件fd
      fileIo.closeSync(this.curFile);
      this.getFileList();
    }
    this.stopContinuousTask();
  }

  /* 获取沙箱内容录制的音频列表 */
  getFileList() {
    let option = new ListFileOption();
    option.filter.suffix = ['.mp4'];
    this.fileNames = fileIo.listFileSync(this.filesDir, option);
  }

  reqPermissionsFromUser(permissions: Array<Permissions>): void {
    let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
    // requestPermissionsFromUser会判断权限的授权状态来决定是否唤起弹窗
    atManager.requestPermissionsFromUser(this.context, permissions).then((data: PermissionRequestResult) => {
      console.info(`requestPermissionsFromUser success, result: ${JSON.stringify(data)}`);
    }).catch((err: BusinessError) => {
      console.error(`Failed to request permissions from user. Code is ${err.code}, message is ${err.message}`);
    });
  }

  startContinuousTask() {
    console.info(`start in operationing startBackgroundRunning.`);
    let wantAgentInfo: wantAgent.WantAgentInfo = {
      // 点击通知后，将要执行的动作列表
      // 添加需要被拉起应用的bundleName和abilityName
      wants: [
        {
          bundleName: this.context.abilityInfo.bundleName,
          abilityName: this.context.abilityInfo.moduleName
        }
      ],
      // 指定点击通知栏消息后的动作是拉起ability
      actionType: wantAgent.OperationType.START_ABILITY,
      // 使用者自定义的一个私有值
      requestCode: 0,
      // 点击通知后，动作执行属性
      actionFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
    };

    // 通过wantAgent模块下getWantAgent方法获取WantAgent对象
    wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj: WantAgent) => {
      backgroundTaskManager.startBackgroundRunning(this.context,
        backgroundTaskManager.BackgroundMode.AUDIO_RECORDING, wantAgentObj).then(() => {
        console.info(`Succeeded in operationing startBackgroundRunning.`);
      }).catch((err: BusinessError) => {
        console.error(`Failed to operation startBackgroundRunning. Code is ${err.code}, message is ${err.message}`);
      });
    });
  }

  stopContinuousTask() {
    backgroundTaskManager.stopBackgroundRunning(this.context).then(() => {
      console.info(`Succeeded in operationing stopBackgroundRunning.`);
    }).catch((err: BusinessError) => {
      console.error(`Failed to operation stopBackgroundRunning. Code is ${err.code}, message is ${err.message}`);
    });
  }
}

class ListFileOption {
  public recursion: boolean = false;
  public listNum: number = 0;
  public filter: Filter = {};
}
```
