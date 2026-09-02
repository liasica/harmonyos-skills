---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-39
title: 应用在后台时，一段时间后自动退出
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > 应用在后台时，一段时间后自动退出
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:49+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:f58abb27a3ad259adc20f3500a9aa7e7ee7f576c5cd5c8c993f7c4cf1b112288
---

## 问题现象

退出到后台后，应用自动退出。

## 背景知识

* PROCESS\_KILL是因为各种原因（如应用内存超限、运行锁异常等）导致应用被操作系统强制停止。
* 当前支持的PROCESS\_KILL问题种类可以参考[分析PROCESS KILL问题](../app/agc-help-apms-appterminate-0000002577580566.md)。
* [长时任务(ArkTS)](../harmonyos-guides/continuous-task.md)：应用退至后台后，在后台需要长时间运行用户可感知的任务，如播放音乐、导航等。为防止应用进程被挂起，导致对应功能异常，可以申请长时任务，使应用在后台长时间运行。

## 问题定位

1. 查看faultlogger目录，没有和应用相关的故障日志，应用不是因为崩溃而退出的。
2. 排查应用是否被系统终止，在hilog日志中搜索关键字kill Reason，应用在20:51:29.264被系统终止，终止原因是在后台非法录音。

   ```txt
   04-24 20:51:29.264   998  2232 W C01713/resource_schedule_service/SUSPEND_MANAGER: [(ReportKillAppEvent):277] hisysevent write result=0, send event [FRAMEWORK,PROCESS_KILL], pid=64424, processName=com.hm.example, msg=Kill Reason:ILLEGAL_AUDIO_CAPTURER_BY_SUSPEND, foreground=0
   04-24 20:51:29.264  3674  3674 I A01B05/com.ohos.sceneboard/AOD: AodSettingsModule --> Check isInTimeRange, currentTime: 1745499089264, startTime: 1745449200000, endTime: 1745506800000
   04-24 20:51:29.264   998  2232 I C01713/resource_schedule_service/SUSPEND_MANAGER: [(IsKillAppWhenIllegalUseAudio):248] Application 20020222_com.hm.example_[64424] current has media and not apply background_task or Resource::AUDIO
   ```
3. 搜索关键字TASK\_DETECTION，查看应用正在执行的任务已经切换到后台的时间。应用在20:50:57.360存在player放音任务，在20:50:57.419存在recorder录音任务，在20:51:27.254切换到后台。

   ```txt
   04-24 20:50:57.360   998  1306 I C01724/resource_schedule_service/TASK_DETECTION: [UpdateAudioRecord:89]Get Audio info uid: 20020222, sessionId: 100020, State: 2, type: player, streamType: 1
   04-24 20:50:57.419   998  1307 I C01724/resource_schedule_service/TASK_DETECTION: [UpdateAudioRecord:89]Get Audio info uid: 20020222, sessionId: 100021, State: 2, type: recorder, streamType: 0
   04-24 20:51:27.254   998  2230 I C01724/resource_schedule_service/TASK_DETECTION: [OnAppStateChanged:595]Application State change to background, uid: 20020222, pid: 64424,bundleName: com.hm.example
   // ...
   04-24 20:51:29.309   998  2136 I C01724/resource_schedule_service/TASK_DETECTION: [UpdateAudioRecord:103]Get Audio info uid: 20020222, sessionId: 100020, State: 4, type: player, streamType: 1
   04-24 20:51:29.309   998  2136 I C01724/resource_schedule_service/TASK_DETECTION: [UpdateAudioRecord:103]Get Audio info uid: 20020222, sessionId: 100021, State: 4, type: recorder, streamType: 0
   ```
4. 搜索关键字Freeze pid，查看应用进程被冻结时间。应用进程id是64424，在20:51:29.258被系统冻结。

   ```txt
   04-24 20:51:03.376   998  1173 I C01713/resource_schedule_service/SUSPEND_MANAGER: [(FreezePids):246] Freeze pid: 59581 success.
   04-24 20:51:09.392   998  1173 I C01713/resource_schedule_service/SUSPEND_MANAGER: [(FreezePids):246] Freeze pid: 59581 success.
   04-24 20:51:29.258   998  1173 I C01713/resource_schedule_service/SUSPEND_MANAGER: [(FreezePids):246] Freeze pid: 64424 success.
   04-24 20:51:40.381   998  1173 I C01713/resource_schedule_service/SUSPEND_MANAGER: [(FreezePids):246] Freeze pid: 3847 success.
   04-24 20:51:40.384   998  1173 I C01713/resource_schedule_service/SUSPEND_MANAGER: [(FreezePids):246] Freeze pid: 3653 success.
   ```
5. 搜索关键字CONTINUOUS\_TASK，查看应用是否申请长时任务。从日志可知，应用在20:51:29.267开始申请长时任务，但应用在20:51:29.264已经被系统终止，申请长时任务发生在系统终止之后。

   ```txt
   04-24 20:51:29.264 64424 64424 I C01711/com.hm.example/CONTINUOUS_TASK: [GetModes:433] get bgModes arraylen: 2
   04-24 20:51:29.264 64424 64424 I C01711/com.hm.example/CONTINUOUS_TASK: [GetModes:449] GetBackgroundMode audioRecording.
   04-24 20:51:29.264 64424 64424 I C01711/com.hm.example/CONTINUOUS_TASK: [GetModes:449] GetBackgroundMode audioPlayback.
   04-24 20:51:29.267 64424 65310 I C01711/com.hm.example/CONTINUOUS_TASK: [StartBackgroundRunningExecuteCB:240] RequestStartBackgroundRunning isBatch: 1, bgModeSize: 2
   ```

## 分析结论

切换到后台时，未及时开启长时任务，导致应用因为后台非法录音被系统终止。

## 修改建议

参考[长时任务(ArkTS)](../harmonyos-guides/continuous-task.md)，在开始录音时开启长时任务，在停止录音时停止长时任务。

```ts
import { media } from '@kit.MediaKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';
import { abilityAccessCtrl, WantAgent, wantAgent } from '@kit.AbilityKit';
import { backgroundTaskManager } from '@kit.BackgroundTasksKit';

@Entry
@Component
export struct AudioRecordPage {
  private avRecorder: media.AVRecorder | undefined = undefined;
  private avProfile: media.AVRecorderProfile = {
    audioBitrate: 112000, // 音频比特率。
    audioChannels: 2, // 音频声道数。
    audioCodec: media.CodecMimeType.AUDIO_AAC, // 音频编码格式，当前支持ACC，MP3，G711MU。
    audioSampleRate: 48000, // 音频采样率。
    fileFormat: media.ContainerFormatType.CFT_MPEG_4A, // 封装格式，当前支持MP4，M4A，MP3，WAV，AMR，AAC。
  };
  private avConfig: media.AVRecorderConfig = {
    audioSourceType: media.AudioSourceType.AUDIO_SOURCE_TYPE_MIC, // 音频输入源，这里设置为麦克风。
    profile: this.avProfile,
    url: 'fd://35', // 参考应用文件访问与管理开发示例新建并读写一个文件。
  };
  private fileFd: number = 0;
  // 通过getUIContext().getHostContext()方法，来获取page所在的UIAbility上下文
  private context: Context | undefined = this.getUIContext().getHostContext();
  @State recordState: string = '未开始录制';
  @State longTaskState: string = '未申请';

  startContinuousTask() {
    let wantAgentInfo: wantAgent.WantAgentInfo = {
      // 点击通知后，将要执行的动作列表
      // 添加需要被拉起应用的bundleName和abilityName
      wants: [
        {
          bundleName: 'com.example.commondemofordfx',
          abilityName: 'EntryAbility'
        }
      ],
      // 指定点击通知栏消息后的动作是拉起ability
      actionType: wantAgent.OperationType.START_ABILITY,
      // 使用者自定义的一个私有值
      requestCode: 0,
      // 点击通知后，动作执行属性
      actionFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG],
      // 车钥匙长时任务子类型。只有申请bluetoothInteraction类型的长时任务，车钥匙子类型才能生效。
    };
    try {
      // 通过wantAgent模块下getWantAgent方法获取WantAgent对象
      wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj: WantAgent) => {
        try {
          let list: Array<string> = ['audioRecording'];
          backgroundTaskManager.startBackgroundRunning(this.context, list, wantAgentObj).then(() => {
            console.info('Operation startBackgroundRunning succeeded');
            // 此处执行具体的长时任务逻辑，如录音，录制等。
            this.longTaskState = '已申请';
          }).catch((error: BusinessError) => {
            console.error(`Failed to Operation startBackgroundRunning. code is ${error.code} message is ${error.message}`);
          });
        } catch (error) {
          console.error(`Failed to Operation startBackgroundRunning. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
        }
      });
    } catch (error) {
      console.error(`Failed to Operation getWantAgent. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
    }
  }

  stopContinuousTask() {
    backgroundTaskManager.stopBackgroundRunning(this.context).then(() => {
      console.info(`Succeeded in operationing stopBackgroundRunning.`);
      this.longTaskState = '已取消';
    }).catch((err: BusinessError) => {
      console.error(`Failed to operation stopBackgroundRunning. Code is ${err.code}, message is ${err.message}`);
    });
  }

  // 创建文件以及设置avConfig.url。
  async createAndSetFd(): Promise<void> {
    const context: Context = this.getUIContext().getHostContext()!; // 非空断言，Context类型且非空
    const path: string = context.filesDir + '/example.mp3'; // 文件沙箱路径，文件后缀名应与封装格式对应。
    const audioFile: fs.File | null = null;
    try {
      const audioFile: fs.File = fs.openSync(path, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
      this.avConfig.url = 'fd://' + audioFile.fd; // 更新url。
      this.fileFd = audioFile.fd;
    } catch (error) {
      console.error(`Failed to openSync. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
    } finally {
      if (audioFile !== null) {
        fs.closeSync(audioFile);
      }
    }
  }

  // 注册audioRecorder回调函数。
  setAudioRecorderCallback() {
    if (this.avRecorder !== undefined) {
      // 状态机变化回调函数。
      this.avRecorder.on('stateChange', (state: media.AVRecorderState) => {
        console.info(`Aud ioRecorder current state is ${state.toString()}`);
        this.recordState = state;
      });
      // 错误上报回调函数。
      this.avRecorder.on('error', (err: BusinessError) => {
        console.error(`AudioRecorder failed, code is ${err.code}, message is ${err.message}`);
      });
    }
  }

  // 开始录制对应的流程。
  async startRecordingProcess() {
    if (this.avRecorder !== undefined) {
      await this.avRecorder.release();
      this.avRecorder = undefined;
    }
    // 1.创建录制实例。
    this.avRecorder = await media.createAVRecorder();
    this.setAudioRecorderCallback();
    // 2.获取录制文件fd赋予avConfig里的url；参考FilePicker文档。
    this.createAndSetFd();
    // 3.配置录制参数完成准备工作。
    await this.avRecorder.prepare(this.avConfig);
    // 4.开始录制。
    await this.avRecorder.start();
  }

  // 暂停录制对应的流程。
  async pauseRecordingProcess() {
    if (this.avRecorder !== undefined && this.avRecorder.state === 'started') { // 仅在started状态下调用pause为合理状态切换。
      await this.avRecorder.pause();
    }
  }

  // 恢复录制对应的流程。
  async resumeRecordingProcess() {
    if (this.avRecorder !== undefined && this.avRecorder.state === 'paused') { // 仅在paused状态下调用resume为合理状态切换。
      await this.avRecorder.resume();
    }
  }

  // 停止录制对应的流程。
  async stopRecordingProcess() {
    if (this.avRecorder !== undefined) {
      // 1. 停止录制。
      if (this.avRecorder.state === 'started' ||
        this.avRecorder.state === 'paused') { // 仅在started或者paused状态下调用stop为合理状态切换。
        await this.avRecorder.stop();
      }
      // 2.重置。
      await this.avRecorder.reset();
      // 3.释放录制实例。
      await this.avRecorder.release();
      this.avRecorder = undefined;
      // 4.关闭录制文件fd。
      await fs.close(this.fileFd);
    }
  }

  async checkPermissions(): Promise<void> {
    let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
    atManager.requestPermissionsFromUser(this.context, [
      'ohos.permission.MICROPHONE',
    ], () => {
      console.info('request camera permission');
    });
  }

  aboutToAppear(): void {
    this.checkPermissions();
    if (this.avRecorder !== undefined) {
      if (this.avRecorder.state === 'paused') {
        this.resumeRecordingProcess();
      }
    }
  }

  aboutToDisappear(): void {
    if (this.avRecorder !== undefined) {
      if (this.avRecorder.state === 'started') {
        this.pauseRecordingProcess();
      }
    }
  }

  build() {
    Column({ space: 10 }) {
      Text(`录制状态：${this.recordState}`)
        .fontSize(20)
      Button('开始录音')
        .onClick(() => {
          this.startRecordingProcess();
        })
      Button('暂停录音')
        .onClick(() => {
          this.pauseRecordingProcess();
        })
      Button('恢复录音')
        .onClick(() => {
          this.resumeRecordingProcess();
        })
      Button('停止录音')
        .onClick(() => {
          this.stopRecordingProcess();
        })
      Text(`长时任务状态：${this.longTaskState}`)
        .fontSize(20)
      Button('申请长时任务')
        .onClick(() => {
          // 通过按钮申请长时任务
          this.startContinuousTask();
        })
      Button('取消长时任务')
        .onClick(() => {
          // 通过按钮取消长时任务
          this.stopContinuousTask();
        })
    }
    .width('100%')
    .height('100%')
    .margin({ top: 30 })
  }
}
```
