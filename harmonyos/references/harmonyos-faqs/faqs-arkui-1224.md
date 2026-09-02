---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1224
title: 如何实现获取验证码倒计时等待效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现获取验证码倒计时等待效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:22+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:8b1dd0fd0f47c9308d98aff37a8288b2294426eab4a314fae6287cbdc9493491
---

## 问题现象

如何实现点击获取验证码后倒计时等待，并且倒计时结束后可再次点击获取验证码效果。

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/JFqMYRIUQiuMdY1SM9LJrQ/zh-cn_image_0000002658833273.gif "点击放大")

## 背景知识

[setInterval](../harmonyos-references/js-apis-timer.md#setinterval)重复调用一个函数，在每次调用之间具有固定的时间延迟。

## 解决方案

1. 设置按钮展示的动态变量初始值为“获取验证码”，设置初始等待时间为30。
2. 点击按钮，如果按钮值为“获取验证码”或“重获验证码”，按钮文本切换为显示剩余等待时间，并使用setInterval设置等待时间每秒减1，此时按钮不可被点击。
3. 等待时间减少为0后，按钮文本显示为“重获验证码”。
4. 再次点击“重获验证码”后，重置初始等待时间为30，继续按步骤2逻辑实现倒计时。

完整代码如下：

```ts
@Entry
@Component
struct BottomWithBar {
  private maxLength: number = 6;
  private strokeWidth: number = 1;
  private captchaTimerId: number | null = null;
  @State captchaButtonText: string = '获取验证码';
  @State remainingSeconds: number = 30;

  aboutToDisappear() {
    // 清除验证码倒计时定时器
    clearInterval(this.captchaTimerId);
  }

  build() {
    Column() {
      Row() {
        Text('请输入验证码')
          .fontSize(24)
          .fontWeight(FontWeight.Medium)
      }
      .height(32)

      Row() {
        Text('验证码将发送至')
          .fontSize(14)
          .fontColor('#6e6e6e')
          .fontWeight(FontWeight.Regular)
        Text('+86 ***********')
          .fontSize(14)
          .fontColor('#0a59f7')
          .fontWeight(FontWeight.Regular)
      }
      .margin({
        top: 10,
        bottom: 37
      })

      Row() {
        TextInput()
          .backgroundColor(Color.Transparent)
          .width('65%')
          .maxLength(this.maxLength)
          .type(InputType.Number)
          .translate({ x: -12 })
        Text(this.captchaButtonText)
          .fontSize(16)
          .fontWeight(FontWeight.Medium)
          .fontColor((this.captchaButtonText === '获取验证码' || this.captchaButtonText === '重获验证码') ? '#0a59f7' :
            '#6e6e6e')
          .onClick(() => {
            // 判断是否开始倒计时
            if (this.captchaButtonText === '获取验证码' || this.captchaButtonText === '重获验证码') {
              // 设置初始倒计时时间为30秒
              this.remainingSeconds = 30;
              // 更新验证码按钮文本为剩余秒数
              this.captchaButtonText = `${this.remainingSeconds.toString()}s后重新获取`;

              // 清除已存在的定时器
              clearInterval(this.captchaTimerId);

              // 创建新的倒计时定时器
              this.captchaTimerId = setInterval(() => {
                console.info(`定时器执行：${this.captchaButtonText}`);
                // 减少一秒
                this.remainingSeconds--;
                // 更新验证码按钮文本
                this.captchaButtonText = `${this.remainingSeconds.toString()}s后重新获取`;

                // 倒计时结束，恢复初始状态
                if (this.remainingSeconds <= 0) {
                  this.captchaButtonText = '重获验证码';
                  // 清除定时器
                  clearInterval(this.captchaTimerId);
                }
              }, 1000);
            }
          });
      }
      .width('85%')

      Divider()
        .strokeWidth(this.strokeWidth)
        .width('85%')
        .color('#f2f2f2')
        .margin({
          top: 5,
          bottom: 55
        })

      Button('登录/注册')
        .backgroundColor('#0a59f7')
        .fontColor(Color.White)
        .width('85%')
        .height(40)
    }
    .padding({ top: 48 })
    .height('100%')
    .width('100%')
  }
}
```
