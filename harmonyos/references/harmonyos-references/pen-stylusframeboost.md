---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pen-stylusframeboost
title: StylusFrameBoost（手写笔跟手性加速功能）
breadcrumb: API参考 > 系统 > 硬件 > Pen Kit（手写笔服务） > ArkTS API > StylusFrameBoost（手写笔跟手性加速功能）
category: harmonyos-references
scraped_at: 2026-09-02T14:52:38+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:4089b8faa0ea5e0a7bb7e41ce0f80079195ee5e233947b546471dbc8baa9ce24
---

本模块提供手写笔跟手性加速能力，通过调用手写笔跟手性加速接口，可以优化手写应用在高帧率状态下的手写笔书写时延。

**起始版本：** 26.0.0

## 导入模块

```typescript
import { StylusFrameBoost } from '@kit.Penkit';
```

## forceRefreshOneFrame

forceRefreshOneFrame(action: number): number

提高手写应用程序在高帧率状态下的手写笔书写时延。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Stylus.Handwrite

**起始版本：** 26.0.0

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| action | number | 是 | 手写笔触控事件。  0：down  1：up  2：move  3：cancel |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回查询结果。  0：手写笔跟手性加速成功。  1：手写笔跟手性加速失败。 |

**示例：**

```typescript
import { LengthMetricsUnit } from '@kit.ArkUI';
import { inputDevice } from '@kit.InputKit';
import { StylusFrameBoost } from '@kit.Penkit';

@Entry
@Component
struct StylusFrameBoostDemo {
  private device: PencilHelper = new PencilHelper()
  private settings: RenderingContextSettings = new RenderingContextSettings(false)
  private ctx: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings, LengthMetricsUnit.PX)
  private stylusFrameBoost: StylusFrameBoost = new StylusFrameBoost();

  build() {
    Column() {
      Canvas(this.ctx)
        .width('100%')
        .height('100%')
        .onReady(() => {
          this.ctx.lineWidth = 20
          this.ctx.beginPath()
          this.ctx.lineCap = 'round'
          this.ctx.strokeStyle = Color.Black;
        })
        .onTouch((event: TouchEvent) => {
          // 判断是否连接手写笔。该接口依赖手写笔服务。
          if (this.device.hasPencil) {
            if (event.sourceTool === SourceTool.Pen || event.sourceTool === SourceTool.MOUSE ||
              event.sourceTool === SourceTool.Finger) {
              this.handleWriteEvent(event)
            }
          }
        })
    }
  }

  aboutToAppear(): void {
    this.device.init();
  }

  handleWriteEvent(event: TouchEvent) {
    if (event.touches.length <= 0) {
      return
    }
    const touch = event.changedTouches[0]
    let x = touch.x
    let y = touch.y
    switch (event.type) {
      case TouchType.Down:
        this.ctx.moveTo(vp2px(x), vp2px(y));
        try {
          this.stylusFrameBoost.forceRefreshOneFrame(event.type);
        } catch (error) {
          console.error('stylusFrameBoost failed: ', error);
        }
        break
      case TouchType.Move:
        this.ctx.lineTo(vp2px(x), vp2px(y));
        try {
          this.stylusFrameBoost.forceRefreshOneFrame(event.type);
        } catch (error) {
          console.error('stylusFrameBoost failed: ', error);
        }
        break
      case TouchType.Up:
      case TouchType.Cancel:
        this.ctx.lineTo(vp2px(x), vp2px(y))
        try {
          this.stylusFrameBoost.forceRefreshOneFrame(event.type);
        } catch (error) {
          console.error('stylusFrameBoost failed: ', error);
        }
        break
    }
    this.ctx.stroke();
  }
}

class PencilHelper {
  private _hasPencil: boolean = false
  private pencilId: number = 0

  public get hasPencil(): boolean {
    return this._hasPencil
  }

  async init() {
    const deviceIds = await inputDevice.getDeviceList()
    inputDevice.on('change', async (device: inputDevice.DeviceListener) => {
      if (device.type === 'add') {
        const isPencil = await this.isPencil(device.deviceId)
        if (isPencil) {
          this._hasPencil = true
          this.pencilId = device.deviceId
        }
      } else if (this.pencilId === device.deviceId) {
        // 删除无法查询信息，只能通过之前的 id 判断。
        this._hasPencil = false
        this.pencilId = 0
      }
    })
    for (const id of deviceIds) {
      const info = await inputDevice.getDeviceInfo(id)
      const isPencil = await this.isPencil(id)
      if (isPencil) {
        this._hasPencil = true
        this.pencilId = id
        break
      }
    }
  }

  async isPencil(deviceId: number) {
    const info = await inputDevice.getDeviceInfo(deviceId)
    return info.name.toLowerCase().indexOf('pencil') >= 0
  }
}
```
