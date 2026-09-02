---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-907
title: 多指touch中move事件下发时机问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 多指touch中move事件下发时机问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:04+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:74aee43015ad1e002e3d3881cf9b286eb2f057fa4cf713b416bfa693b4e03cec
---

## 问题现象

在多指touch事件上，当第二个手指触发的时候，回调的touch事件会短暂丢失第二根手指的move信息。

问题代码示例参考如下：

```screen
@Entry
@Component
struct TouchExample {
  @State text: string = ''
  @State eventType: string = ''

  build() {
    Column() {
      Button('Touch').height(50).width(200).margin(20)
        .onTouch((event?: TouchEvent) => {
          if (event) {
            let info = JSON.stringify(event.touches)
            console.info(`${event.touches.length}`, info)
            if (event.type === TouchType.Down) {
              this.eventType = 'Down'
            }
            if (event.type === TouchType.Up) {
              this.eventType = 'Up'
            }
            if (event.type === TouchType.Move) {
              this.eventType = 'Move'
            }
            this.text = 'TouchType:' + this.eventType + '\nDistance between touch point and touch element:\nx: '
              + event.touches[0].x + '\n' + 'y: ' + event.touches[0].y + '\nComponent globalPos:('
              + event.target.area.globalPosition.x + ',' + event.target.area.globalPosition.y + ')\nwidth:'
              + event.target.area.width + '\nheight:' + event.target.area.height + '\ntouches' +
            JSON.stringify(event.touches)
          }
        })
      Text(this.text)
    }.width('100%').padding(30)
  }
}
```

## 解决方案

手指信息未丢失，原因在于move和down事件的下发周期问题，down事件的信息是立即下发，move事件的信息是由vsync按帧刷新下发，两帧中间存在多个move报点，不是每个报点都会下发，是等vsync来了，下发最新的那个报点。
