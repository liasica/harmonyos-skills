---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-liveview-3
title: 如何监听实况窗计时器倒计时结束事件并关闭实况窗
breadcrumb: FAQ > 应用服务开发 > 实况视图服务（Live View Kit） > 如何监听实况窗计时器倒计时结束事件并关闭实况窗
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:49+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:6257f0b21a9597b9bfd85a2c02dbbf6cac269763fdb3df7f749b36561a2178e6
---

## 问题现象

如何在实况窗计时器倒计时结束时监听到事件，并自动关闭实况窗？

## 解决方案

可以在[startLiveView](../harmonyos-references/liveview-liveviewmanager.md#liveviewmanagerstartliveview)创建实况窗时记录下当前时间，再获取实况窗请求体的倒计时时间，开始计时之后循环计算当前时间减去开始时间是否小于倒计时时间，是则继续循环，否则调用[stopLiveView](../harmonyos-references/liveview-liveviewmanager.md#liveviewmanagerstopliveview)方法结束实况窗。实况窗的构建及开启可参考[创建实况窗](../harmonyos-guides/liveview-create-locally.md#创建实况窗)。完整代码参考如下：

```ts
import { liveViewManager } from '@kit.LiveViewKit';
import { Want, wantAgent } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

const TIME = 10000; // 倒计时实况窗计时器初始值

export class LiveViewController {
  // 获取实况窗请求体的倒计时时间
  public async startLiveView(): Promise<liveViewManager.LiveViewResult> {
    // 校验实况窗开关是否打开
    if (!await LiveViewController.isLiveViewEnabled()) {
      throw new Error('Live view is disabled.');
    }
    // 创建实况窗
    const defaultView = await LiveViewController.buildDefaultView(1);
    return await liveViewManager.startLiveView(defaultView);
  }

  async stopLiveView(): Promise<void> {
    try {
      // 定义要结束的liveView
      const defaultView = await LiveViewController.buildDefaultView(2);
      liveViewManager.stopLiveView(defaultView).then(() => {
        hilog.info(0x0000, 'testTag', 'Succeeded in stopping liveView, result: %{public}s');
      }).catch((err: BusinessError) => {
        hilog.error(0x0000, 'testTag', 'Failed to stop liveView: %{public}d %{public}s', err.code, err.message);
      });
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      hilog.error(0x0000, 'testTag', 'Failed to stop liveView: %{public}d %{public}s', e.code, e.message);
    }
  }

  private static async buildDefaultView(sequence: number): Promise<liveViewManager.LiveView> {
    return {
      id: 123,
      event: 'PICK_UP',
      sequence: sequence,
      isMute: false,
      timer: { time: TIME },
      liveViewData: {
        primary: {
          title: '餐品已备好',
          content: [
            { text: '请前往' },
            { text: '一号窗口', textColor: '#FFFF0000' }
          ],
          keepTime: 1,
          clickAction: await LiveViewController.buildWantAgent(),
          extensionData: {
            text: '待取餐',
            type: liveViewManager.ExtensionType.EXTENSION_TYPE_COMMON_TEXT
          },
          layoutData: {
            layoutType: liveViewManager.LayoutType.LAYOUT_TYPE_PICKUP,
            title: '取餐码',
            content: '72988',
            underlineColor: '#FFFF0000',
            descPic: 'coffee.jpg'
          }
        }
      }
    };
  }

  private static async isLiveViewEnabled(): Promise<boolean> {
    return await liveViewManager.isLiveViewEnabled();
  }

  private static async buildWantAgent(): Promise<Want> {
    const wantAgentInfo: wantAgent.WantAgentInfo = {
      wants: [
        {
          bundleName: 'com.example.liveview', // 应用实际bundleName
          abilityName: 'EntryAbility'
        } as Want
      ],
      actionType: wantAgent.OperationType.START_ABILITIES,
      requestCode: 0,
      actionFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
    };
    const agent = await wantAgent.getWantAgent(wantAgentInfo);
    return agent;
  }
}

@Entry
@Component
struct Index {
  private message: string = '开启实况窗';
  @State starttime: number = 0;
  private LiveViewController: LiveViewController = new LiveViewController();

  // 循环计算当前时间减去开始时间是否小于倒计时时间
  async countDown() {
    while (new Date().getTime() - this.starttime < TIME) { // start为开启实况窗的时间，TIME为实况窗设置的倒计时时间
      await this.sleep(1000);
    }
    this.LiveViewController.stopLiveView();
  }

  // 睡眠
  sleep(ms: number): Promise<void> {
    return new Promise(resolve => setTimeout(resolve, ms));
  }

  build() {
    Column() {
      Text(this.message)
        .fontSize(50)
        .fontWeight(FontWeight.Bold)
        .onClick(() => {
          this.LiveViewController.startLiveView();
          this.starttime = new Date().getTime();
          this.countDown();
        });
    }
    .height('100%')
    .width('100%');
  }
}
```
