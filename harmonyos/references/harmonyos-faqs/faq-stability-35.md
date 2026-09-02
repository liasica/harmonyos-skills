---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-35
title: 多指操作时应用出现闪退
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > 多指操作时应用出现闪退
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:49+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:6025b7cb165673492a953bd3613fd3a61ea08a000db7079e535dbdd36548abae
---

## 问题现象

在多指操作页面时，应用出现闪退。

## 背景知识

* JsCrash异常根据不同的异常场景，在Reason字段进行了分类，分为Error、TypeError、SyntaxError、ReferenceError、RangeError等错误类型。参考文档[JS Crash（进程崩溃）检测](../harmonyos-guides/jscrash-guidelines.md)。
* TypeError（类型错误）运行时最常见的异常，表示变量或参数不是预期类型。
* [GestureEvent对象说明](../harmonyos-references/ts-gesture-common.md#gestureevent对象说明)：GestureEvent对象中包含fingerList属性，类型为FingerInfo[]，手指索引编号与位置对应，即fingerList[index]的id为index。先按下且未参与当前手势触发的手指在fingerList中对应位置为空。
* [FingerInfo对象说明](../harmonyos-references/ts-gesture-common.md#fingerinfo8对象说明)：FingerInfo对象中包含属性localX，类型为number，表示相对于当前组件元素原始区域左上角的x轴坐标，单位为vp。

## 问题定位

1. 查看faultlogger目录下的故障日志，应用出现了[JS Crash](../best-practices/bpta-quality-overview.md#section19523112309)异常，故障原因是TypeError类型错误，异常信息是Cannot read property localX of undefined，无法从undefined对象中读取localX属性值。

   ```txt
   Reason:TypeError
   Error name:TypeError
   Error message:Cannot read property localX of undefined
   Stacktrace:
   Cannot get SourceMap info, dump raw stack:
       at anonymous (entry|entry|1.0.0|src/main/ets/components/CGBGestureUnlockView.ts:235:1)
   ```
2. 从异常信息可以看出，应用从FingerInfo对象中读取属性localX，没有校验FingerInfo对象是否为undefined。
3. 排查应用是否监听了手势事件，并从GestureEvent对象中获取FingerInfo对象。先按下且未参与当前手势触发的手指在fingerList中对应位置为空，在使用时必须先校验FingerInfo对象是否为空。

## 分析结论

在使用FingerInfo对象前未判断是否为空导致应用使用时闪退。

## 修改建议

在使用前判断FingerInfo对象是否为空。

```typescript
@Entry
@Component
struct PanGesturePage {
  @State offsetX: number = 0;
  @State offsetY: number = 0;
  private panOption: PanGestureOptions = new PanGestureOptions({ direction: PanDirection.Left | PanDirection.Right });

  build() {
    Column() {
      Column() {
        Text('PanGesture offset:\nX: ' + this.offsetX + '\n' + 'Y: ' + this.offsetY)
      }
      .height(200)
      .width(300)
      .padding(20)
      .border({ width: 3 })
      .margin(50)
      .gesture(
        PanGesture(this.panOption)
          .onActionStart((event: GestureEvent) => {
            // 获取fingerInfos信息
            if (event?.fingerList) {
              // 使用前判断FingerInfo对象是否为空
              if (event.fingerList[0] !== undefined) {
                this.offsetX = event.fingerList[0].localX;
                this.offsetY = event.fingerList[0].localY;
              }
            }
          })
      )
    }
  }
}
```

上述为常规修复方案，在API20及以上版本，[GestureEvent](../harmonyos-references/ts-gesture-common.md#gestureevent对象说明)对象新增属性fingerInfos，该属性返回的是当前触摸手势的所有触摸点，不存在空值情况。
