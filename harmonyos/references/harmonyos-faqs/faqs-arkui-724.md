---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-724
title: 如何监听手机音量键动作
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何监听手机音量键动作
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:03+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:51d98c9c2ab9ae14a241a70f57a0c4b8959eac8f8351eae41b3addef1c249696
---

## 问题现象

在小说阅读等场景，时常用到手机音量键实现上下页翻动，如何监听手机音量键动作？

## 背景知识

按键事件是指组件与键盘、遥控器等按键设备交互时触发的事件，适用于所有可获焦组件，例如Button。对于默认不可获焦的组件，如Text，Image等，可以将focusable属性设置为true后使用按键事件。按键事件触发的流程和具体时机参考[按键事件数据流](../harmonyos-guides/arkts-interaction-development-guide-keyboard.md#按键事件数据流)。

## 解决方案

参考[KeyCode](../harmonyos-references/js-apis-keycode.md#keycode)枚举表可知，音量键增减的键码值分别为KEYCODE\_VOLUME\_UP以及KEYCODE\_VOLUME\_DOWN。获取需要监听的键码值后，使用[onKeyEvent](../harmonyos-references/ts-universal-events-key.md#onkeyevent15)或[onKeyPreIme](../harmonyos-references/ts-universal-events-key.md#onkeypreime12)触发回调事件，关于音量键实现翻页效果可参考[音量键翻页](../architecture-guides/volume_key_turn_page-0000002293620017.md)。

监听音量键变化的完整代码参考如下：

```screen
@Entry
@Component
struct KeyEventExample {
  build() {
    Column() {
      // 监听音量键的增加或减小
      Button('KeyEvent')
        .defaultFocus(true)
        .onKeyPreIme((event?: KeyEvent) => {
          if (event) {
            console.info('触发onKeyPreIme');
            if (event.keyCode === 16) {
              console.info('UP');
            } else if (event.keyCode === 17) {
              console.info('DOWN');
            }
            return false; // 返回true事件被消费不会执行下面的onKeyEvent，false则会触发onKeyEvent
          }
          return false;
        })
        .onKeyEvent((event) => {
          if (event) {
            console.info('触发onKeyEvent');
            if (event.keyCode === 16) {
              console.info('UP');
            } else if (event.keyCode === 17) {
              console.info('DOWN');
            }
          }
        });
    }.height(300).width('100%').padding(35);
  }
}
```
