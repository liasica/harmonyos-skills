---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-avsession-23
title: 音视频后台播放和长时任务的使用流程以及注意事项
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音视频播控（AVSession） > 音视频后台播放和长时任务的使用流程以及注意事项
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:45+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:2556933cd98a5c7ac0128d30c798352522f2bf669cbee589513861c7dbe99f18
---

## 问题现象

音视频后台播放场景开发流程、注意事项及特殊场景问题，涉及接入AVSession和长时任务的使用。

## 背景知识

[AVSession Kit](../harmonyos-guides/avsession-overview.md)：是系统提供的音视频管控服务，用于统一管理系统中所有音视频行为。通常，音视频后台播放需要接入AVSession。应用接入播控中心通常还可以用于开发分布式媒体会话投播、设备切换功能。

[长时任务](../harmonyos-guides/continuous-task.md)：支持在应用退至后台后，应用进程不被挂起，仍可以长时间播放音视频。

## 解决方案

应用如果要实现后台播放或锁屏播放，需要同时满足：根据应用类型正确创建并接入AVSession；按需申请相应的长时任务避免应用进入挂起状态。其中，AVSession主要是提供后台播放控制，允许用户在后台控制音视频的播放、暂停、资源切换、进度控制、输出设备切换等播放控制功能；在后台播放音频使进程保活主要依赖对应的长时任务。

使用流程：

1. 正确创建并接入AVSession。

   通常，音视频后台播放场景的实现依赖于播控中心，建议开发者参考[播控中心接入流程](../harmonyos-guides/avsession-access-scene.md#接入流程)正确完成播控中心的接入。

   注意，应用需创建对应类型的AVSession。

   * 媒体类应用应创建'audio'或'video'类型的AVSession；
     + 应用需正确通过setAVMetadata[设置元数据](../harmonyos-guides/avsession-access-scene.md#设置元数据信息)；至少完成一条[控制命令注册](../harmonyos-guides/avsession-access-scene.md#控制命令的处理)；否则播控中心界面不显示。
     + 由于媒体类应用后台播放时需要依赖播控中心的界面对音视频后台播放进行播控操作，应用需注册相应的控制命令，应用播放状态（播放进度、状态、倍速等）也需及时通过setAVPlaybackState[更新播放相关的状态](../harmonyos-guides/avsession-access-scene.md#设置播放状态)。本地媒体播放场景下控制命令需要激活AVSession后才可以生效。
     + 应用切换资源时，应重新设置正确的元数据，并注意[更新播放相关的状态。](../harmonyos-guides/avsession-access-scene.md#设置播放状态)
     + 建议应用尽可能将播控中心的生命周期和对应长时任务的生命周期一致，特殊情况仍需按实际业务特殊处理。
   * 通话类应用应创建'video\_call'或'voice\_call'类型的AVSession。

   参考示例：

   1. 正确初始化AVSession，同步开启长时任务。

      ```ts
      async initAvsession() {
        this.session = await AVSessionManager.createAVSession(this.context, 'SESSION_NAME', this.type);
        this.startContinuousTask(this.uiAbilityContext);
        this.setAVMetadata();
        this.registerSessionListener();
        this.session.activate();
      }
      ```

      ```ts
      private registerSessionListener() {
        this.session!.on('play', () => {
          console.info(`on play , do pause task`);
          this.controller.start();
        });
        this.session!.on('pause', () => {
          this.controller.pause();
        });
        this.session!.on('stop', () => {
          this.controller.stop();
        });
      }
      ```

      ```ts
      private setAVMetadata() {
        let metadata: AVSessionManager.AVMetadata = {
          assetId: '0',
          title: 'TITLE',
          mediaImage: 'IMAGE',
          duration: 91000,
        };
        this.session!.setAVMetadata(metadata).then(() => {
          console.info(`SetAVMetadata successfully`);
        }).catch((err: BusinessError) => {
          console.error(`Failed to set AVMetadata. Code: ${err.code}, message: ${err.message}`);
        });
      }
      ```
   2. 设置播放状态。

      ```ts
      private setAVPlaybackState(currentState: AVSessionManager.AVPlaybackState) {
        this.session!.setAVPlaybackState(currentState, (err) => {
          if (err) {
            console.error(`Failed to set AVPlaybackState. Code: ${err.code}, message: ${err.message}`);
          } else {
            console.info(`SetAVPlaybackState successfully`);
          }
        });
      }
      ```
   3. 销毁AVSession，同步取消长时任务。

      ```ts
      async destroySession() {
        this.unRegisterSessionListener();
        this.stopContinuousTask(this.uiAbilityContext);
        this.session?.destroy();
      }
      ```

      ```ts
      private unRegisterSessionListener() {
        this.session!.off('play');
        this.session!.off('pause');
        this.session!.off('stop');
      }
      ```
2. 按需接入长时任务。
   1. 在module.json5文件中添加后台运行权限[ohos.permission.KEEP\_BACKGROUND\_RUNNING。](../harmonyos-guides/permissions-for-all.md#ohospermissionkeep_background_running)

      ```json
      "requestPermissions": [
        {
          "name": "ohos.permission.KEEP_BACKGROUND_RUNNING",
          "reason": "$string:reason_background",
          "usedScene": {
            "abilities": [
              "EntryAbility"
            ],
            "when": "always"
          }
        }
      ],
      ```
   2. 创建、取消对应类型的长时任务。
      * 长时任务相关的模块为@ohos.resourceschedule.backgroundTaskManager和@ohos.app.ability.wantAgent，其余模块按实际需要导入。
      * 音视频播放，录制，音视频通话时退后台。在上述三种场景下，选择MODE\_AV\_PLAYBACK\_AND\_RECORD类型长时任务或对应类型的长时任务均可。例如在音视频播放场景下，选择AUDIO\_PLAYBACK或者MODE\_AV\_PLAYBACK\_AND\_RECORD任意一个即可。
      * 按需创建对应类型的长时任务并在对应的UIAbility标签下添加后台模式如'audioPlayback'或'avPlaybackAndRecord'。

      参考示例：
      * 开启长时任务。

        ```ts
        startContinuousTask(context?: common.UIAbilityContext) {
          let wantAgentInfo: wantAgent.WantAgentInfo = {
            wants: [
              {
                bundleName: context?.abilityInfo.bundleName,
                abilityName: context?.abilityInfo.name
              }
            ],
            actionType: wantAgent.OperationType.START_ABILITY,
            requestCode: 0,
            actionFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG],
          };
          try {
            wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj: WantAgent) => {
              try {
                let list: Array<string> = ['audioPlayback'];
                backgroundTaskManager.startBackgroundRunning(this.context, list, wantAgentObj)
                  .then(() => {
                    console.info('Operation startBackgroundRunning succeeded');
                  })
                  .catch((error: BusinessError) => {
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
        ```
      * 取消长时任务。

        ```ts
        stopContinuousTask(context?: common.UIAbilityContext) {
          backgroundTaskManager.stopBackgroundRunning(context).then(() => {
            console.info(`AVPlayerDemo Succeeded in operationing stopBackgroundRunning.`);
          }).catch((err: BusinessError) => {
            console.error(`AVPlayerDemo Failed to operation stopBackgroundRunning. Code is ${err.code}, message is ${err.message}`);
          });
        }
        ```
   3. 设计合理的长时任务生命周期。
      * 应用音视频播放在设计后台播放场景时，关键是接入长时任务进行后台保活，防止应用进程被系统挂起。同时也需接入播控中心提供音频后台约束能力，允许通过控制中心的播控面板控制三方应用的播放功能。
      * 应用要按需设计长时任务接入，在音视频播放场景下，可以将长时任务和播控中心的生命周期一致。
      * 若音频在后台播放时被焦点打断，系统会自行检测和停止长时任务，音频重启播放时，需要再次申请长时任务。
      * 应用不可滥用长时任务，需妥善设计业务逻辑。例如在前台音视频已停止播放时，应及时取消相应的长时任务和AVSession。更多长时任务的约束与限制请参考：[长时任务约束与限制。](../harmonyos-guides/continuous-task.md#约束与限制)

      音视频后台播放参考示例如下：

      ```ts
      import { avSession as AVSessionManager } from '@kit.AVSessionKit';
      import { BusinessError } from '@kit.BasicServicesKit';
      import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
      import { wantAgent, WantAgent, common } from '@kit.AbilityKit';

      @Entry
      @Component
      struct Index {
        @State elapsedTime: number = 0;
        public updateTime: number = 0;
        @State currentState: AVSessionManager.AVPlaybackState = {
          state: AVSessionManager.PlaybackState.PLAYBACK_STATE_INITIAL, // 播放状态。
          position: {
            elapsedTime: 0, // 已经播放的位置，以ms为单位。
            updateTime: new Date().getTime(), // 应用更新当前位置时的时间戳，以ms为单位。
          },
        };
        public context: Context = this.getUIContext().getHostContext() as Context;
        public uiAbilityContext: common.UIAbilityContext | undefined = AppStorage.get('mUIAbilityContext');
        public type: AVSessionManager.AVSessionType = 'audio';
        public session: AVSessionManager.AVSession | undefined = undefined;
        public controller: VideoController = new VideoController();

        aboutToAppear(): void {
          this.initAvsession();
        }

        aboutToDisappear(): void {
          this.destroySession();
        }

        async initAvsession() {
          this.session = await AVSessionManager.createAVSession(this.context, 'SESSION_NAME', this.type);
          this.startContinuousTask(this.uiAbilityContext);
          this.setAVMetadata();
          this.registerSessionListener();
          this.session.activate();
        }

        async destroySession() {
          this.unRegisterSessionListener();
          this.stopContinuousTask(this.uiAbilityContext);
          this.session?.destroy();
        }

        private registerSessionListener() {
          this.session!.on('play', () => {
            console.info(`on play , do pause task`);
            this.controller.start();
          });
          this.session!.on('pause', () => {
            this.controller.pause();
          });
          this.session!.on('stop', () => {
            this.controller.stop();
          });
        }

        private unRegisterSessionListener() {
          this.session!.off('play');
          this.session!.off('pause');
          this.session!.off('stop');
        }

        private setAVPlaybackState(currentState: AVSessionManager.AVPlaybackState) {
          this.session!.setAVPlaybackState(currentState, (err) => {
            if (err) {
              console.error(`Failed to set AVPlaybackState. Code: ${err.code}, message: ${err.message}`);
            } else {
              console.info(`SetAVPlaybackState successfully`);
            }
          });
        }

        private setAVMetadata() {
          let metadata: AVSessionManager.AVMetadata = {
            assetId: '0',
            title: 'TITLE',
            mediaImage: 'IMAGE',
            duration: 91000,
          };
          this.session!.setAVMetadata(metadata).then(() => {
            console.info(`SetAVMetadata successfully`);
          }).catch((err: BusinessError) => {
            console.error(`Failed to set AVMetadata. Code: ${err.code}, message: ${err.message}`);
          });
        }

        startContinuousTask(context?: common.UIAbilityContext) {
          let wantAgentInfo: wantAgent.WantAgentInfo = {
            wants: [
              {
                bundleName: context?.abilityInfo.bundleName,
                abilityName: context?.abilityInfo.name
              }
            ],
            actionType: wantAgent.OperationType.START_ABILITY,
            requestCode: 0,
            actionFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG],
          };
          try {
            wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj: WantAgent) => {
              try {
                let list: Array<string> = ['audioPlayback'];
                backgroundTaskManager.startBackgroundRunning(this.context, list, wantAgentObj)
                  .then(() => {
                    console.info('Operation startBackgroundRunning succeeded');
                  })
                  .catch((error: BusinessError) => {
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

        stopContinuousTask(context?: common.UIAbilityContext) {
          backgroundTaskManager.stopBackgroundRunning(context).then(() => {
            console.info(`AVPlayerDemo Succeeded in operationing stopBackgroundRunning.`);
          }).catch((err: BusinessError) => {
            console.error(`AVPlayerDemo Failed to operation stopBackgroundRunning. Code is ${err.code}, message is ${err.message}`);
          });
        }

        build() {
          Column() {
            Video({
              src: $rawfile('free.mp4'),
              controller: this.controller,
            })
              .width('100%')
              .height(300)
              .onStart(() => {
                console.info('onStart');
                this.currentState.state = AVSessionManager.PlaybackState.PLAYBACK_STATE_PLAY;
                this.updateTime = new Date().getTime();
                this.currentState.position = { elapsedTime: this.elapsedTime, updateTime: this.updateTime };
                this.setAVPlaybackState(this.currentState);
                this.startContinuousTask(this.uiAbilityContext);
              })
              .onPause(() => {
                console.info('onPause');
                this.currentState.state = AVSessionManager.PlaybackState.PLAYBACK_STATE_PAUSE;
                this.updateTime = new Date().getTime();
                this.currentState.position = { elapsedTime: this.elapsedTime, updateTime: this.updateTime };
                this.setAVPlaybackState(this.currentState);
              })
              .onStop(() => {
                console.info('onStop');
                this.currentState.state = AVSessionManager.PlaybackState.PLAYBACK_STATE_STOP;
                this.updateTime = new Date().getTime();
                this.currentState.position = { elapsedTime: this.elapsedTime, updateTime: this.updateTime };
                this.setAVPlaybackState(this.currentState);
                this.stopContinuousTask(this.uiAbilityContext);
              })
              .onSeeked((playbackInfo: PlaybackInfo) => {
                console.info('onSeeked');
                this.elapsedTime = playbackInfo.time * 1000;
                this.updateTime = new Date().getTime();
                this.currentState.position = { elapsedTime: this.elapsedTime, updateTime: this.updateTime };
                this.setAVPlaybackState(this.currentState);
              })
              .onUpdate((playbackInfo: PlaybackInfo) => {
                console.info('onUpdate');
                this.elapsedTime = playbackInfo.time * 1000;
                this.currentState.position = { elapsedTime: this.elapsedTime, updateTime: this.updateTime };
              })

            Text(`应用当前播放进度：${this.elapsedTime}ms`)
            Text(`应用当前播放状态：${this.currentState.state}`)
          }
          .width('100%')
          .height('100%')
        }
      }
      ```

## 常见FAQ

Q：应用后台切换音视频资源，是否需要取消和重新申请长时任务？

A：应用后台切换音频一般在数秒内完成，故不需要取消、重新申请后台长时任务和AVSession，直接在播放器内切换资源，并重新设置新的AVSession元数据信息并注意同步正确的播控状态即可。

但是由于系统对长时任务有管控，不允许创建长时任务但是未实际进行相应的长时任务业务，否则会取消相应的长时任务。故应用切歌需要尽量在1分钟内重新起播，不能一直处于暂停或停止状态。

Q：应用接入长时任务以及AVSession，切到后台无法播放音乐。

A：应用需检查业务逻辑查看长时任务是否被取消，导致应用切后台后无法播放音乐，可以在音乐播放时申请长时任务，达到默认支持后台播放的效果，在播放器释放时取消长时任务。

应用后台播放时若进行资源切换等操作，不需要重新申请长时任务，直接进行资源切换即可。

Q：长时任务是否有数量限制？

A：参考[长时任务约束与限制](../harmonyos-guides/continuous-task.md#约束与限制)。

从API version 21开始，支持一个UIAbility同一时刻申请多个长时任务，最多可申请10个，具体实现可参考[startBackgroundRunning()](../harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmanagerstartbackgroundrunning21)。

对于API version 20及之前版本，一个UIAbility（FA模型则为ServiceAbility）同一时刻仅支持申请一个长时任务，即在一个长时任务结束后才能继续申请。如果一个应用同时需要申请多个长时任务，需要创建多个UIAbility。

如果一个应用创建了多个UIAbility，一个UIAbility申请长时任务后，整个应用下的所有进程均不会被挂起。

Q：音视频后台播放时，如何在后台显示播控中心组件？

A：媒体类应用需要正确接入播控中心，并保证创建'video'或'audio'类型的AVSession；正确设置元数据；至少创建一条播控中心控制命令，播控中心组件才可以正确显示。

播控中心是一种系统设计的[实况窗](../design-guides/system-features-live-view-0000001955186861.md)，播控中心样式参考[播控中心](../design-guides/broadcasting-control-0000001957017133.md)。

其中，通知中心的播控页面需要相应的流起播时由播控中心发送相应通知得到，删除播控通知将收到播控中心的pause控制命令。

Q：后台播放是发长时任务的通知还是发播控中心的通知，删除相应的通知后会怎样？

A：从API version 20开始，申请AUDIO\_PLAYBACK类型长时任务但不接入AVSession，申请长时任务成功后会在通知栏显示通知（延迟发送）；接入AVSession后，后台任务模块不会发送通知栏通知，在应用音频流起播时由AVSession发送通知。

若删除AVSession的通知，应用会收到AVSession的pause控制命令，后台任务模块的通知将显示，若删除后台任务的通知，后台任务将停止。

对于API version 19及之前的版本，后台任务模块不会在通知栏显示通知，若接入AVSession，在应用音频流起播时，AVSession会发送通知。

Q：特殊场景不接入AVSession如何使用长时任务开发后台播放？

A：通常，应用后台播放需要同时接入AVSession和启动相应的长时任务。但在某些特殊场景下，如在后台进行导出媒体文件，使用三方投播组件在后台进行投播，应用不接入AVSession，此时可以创建MODE\_SPECIAL\_SCENARIO\_PROCESSING类型的长时任务进行后台播放支持。

Q：接入AVSession和长时任务进行音视频后台播放开发时，AVSession的[activate()](../harmonyos-references/arkts-apis-avsession-avsession.md#activate10)和[deactivate()](../harmonyos-references/arkts-apis-avsession-avsession.md#deactivate10)是否会影响音视频后台播放？

A：不会，AVSession的激活和去激活只影响本地媒体播放时播控中心控制命令是否有效。AVSession去激活后，在本地媒体播放场景下，AVSession的控制命令将无法传至应用。音视频后台播放的后台保活主要依赖长时任务，要保障应用执行相应的业务，否则系统会对应用进行管控，即应用退至后台会被挂起。
