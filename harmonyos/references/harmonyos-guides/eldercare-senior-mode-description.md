---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/eldercare-senior-mode-description
title: 应用内关怀模式与系统设置同步
breadcrumb: 指南 > 应用框架 > Accessibility Kit（无障碍服务） > 应用长辈关怀功能体验 > 应用内关怀模式与系统设置同步
category: harmonyos-guides
scraped_at: 2026-09-02T14:49:44+08:00
doc_updated_at: 2026-06-12
content_hash: sha256:34605a37599895274b6761dca1a67eb24b7aeb2cb94a5591cefdb0a77b6d6372
---

## 场景介绍

从API版本26.0.0开始，可通过如下接口设置/获取“设置”中应用管理页面内本应用关怀模式开关状态，以及实现对其开关状态监听。

1. 查询关怀模式状态：应用启动时，可通过getSeniorModeStateForSelf接口查询“设置”中应用管理页面内开关状态。若“设置”中应用管理页面关怀模式已开启，则应用应跟随开启自身关怀模式，若关怀模式未开启，则应用应关闭自身关怀模式。
2. 设置关怀模式状态：应用内开启/关闭关怀模式时，可通过setSeniorModeStateForSelf接口设置，以通知设备“设置”中应用管理页面保持同步。
3. 监听关怀模式状态：应用进程存在时，可通过AccessibilityKit提供的接口onSeniorModeStateChangeForSelf监听设备“设置”中应用管理页面关怀模式开关状态，当监听到变化时，应进行自身关怀模式状态切换。

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| getSeniorModeStateForSelf(): Promise<boolean> | 获取“设置”中应用管理页面关怀模式的开关状态。 |
| setSeniorModeStateForSelf(state: boolean): Promise<void> | 设置设备“设置”中应用管理页面内关怀模式开关状态。 |
| onSeniorModeStateChangeForSelf(callback: Callback<boolean>): void | 注册设备“设置”中应用管理页面内关怀模式开关状态监听。 |
| offSeniorModeStateChangeForSelf(callback?: Callback<boolean>): void | 取消注册设备“设置”中应用管理页面内关怀模式开关状态监听。 |

## 开发实例

1. 导入accessibility模块及相关公共模块。

   ```typescript
   import accessibility from '@ohos.accessibility'
   ```
2. 对设备“设置”中应用管理页面内关怀模式开关状态进行监听。

   在aboutToAppear进行对关怀模式开关状态注册监听，在aboutToDisappear取消对关怀模式开关状态监听。

   ```typescript
   @Entry
   @Component
   struct Index {
     @State state: boolean = false;
     callBack = (data: boolean)=> {
       console.info(`data: ` + data);
       this.state = data;
       // 应用内关怀模式开启/关闭UI刷新
     }

     async aboutToAppear(): Promise<void> {
       console.info('aboutToAppear');
       accessibility.onSeniorModeStateChangeForSelf(this.callBack);
     }

     aboutToDisappear(): void {
       console.info('aboutToDisappear');
       accessibility.offSeniorModeStateChangeForSelf(this.callBack);
     }
   }
   ```
3. 设置/查询设备“设置”中应用管理页面内关怀模式状态。

   ```typescript
    @Entry
    @Component
    struct Index {
      @State state: boolean = false;

      async aboutToAppear(): Promise<void> {
        console.info('aboutToAppear');
        // 组件初始化时，获取长辈模式开关状态
        this.state = await accessibility.getSeniorModeStateForSelf();
      }

      aboutToDisappear(): void {
        console.info('aboutToDisappear');
      }

      build() {
        Column() {
          Row() {
          Text(`${'senior mode: '} ${this.state ? 'open' : 'closed'}`)
            .fontSize(18)
          Toggle({ type: ToggleType.Switch, isOn: this.state })
            .onChange(async (isOn: boolean) => {
              console.info(`Toggle state changed to: ${isOn}`);
              if (isOn !== this.state) {
                this.state = isOn;
                // 设置长辈模式状态
                await accessibility.setSeniorModeStateForSelf(isOn);
              }
            })
         }
        }
        .height('100%')
        .width('100%')
      }
    }
   ```
