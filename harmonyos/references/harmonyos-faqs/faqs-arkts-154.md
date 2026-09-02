---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-154
title: 验证码后台计时不准确
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 验证码后台计时不准确
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:53+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a54e44ac83008341973ba2cabe265813688e9a7fe69d4dec0e3cfad9dd9ad651
---

## 问题现象

验证码后台计时不准确。比如当前计时剩余时间30s，退到后台20s再切换前台，预期剩余10s，实际显示25s。

## 背景知识

* [setInterval](../harmonyos-references/js-apis-timer.md#setinterval)：重复调用一个函数，在每次调用之间具有固定的时间延迟。
* [TextTimer](../harmonyos-references/ts-basic-components-texttimer.md)：通过文本显示计时信息并控制其计时器状态的组件。

## 问题定位

排查代码是否通过setInterval实现倒计时功能，类似如下代码。

```typescript
@Entry
@Component
struct Index {
  private maxLength: number = 6;
  private strokeWidth: number = 1;
  private captchaTimerId: number | null = null
  @State captchaButtonText: string = '获取验证码';
  @State remainingSeconds: number = 30

  build() {
    Column() {
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
              this.captchaButtonText = this.remainingSeconds.toString() + 's后重新获取';

              // 清除已存在的定时器
              clearInterval(this.captchaTimerId);

              // 创建新的倒计时定时器
              this.captchaTimerId = setInterval(() => {
                console.info(`定时器执行：${ this.captchaButtonText}`);
                // 减少一秒
                this.remainingSeconds--;
                // 更新验证码按钮文本
                this.captchaButtonText = this.remainingSeconds.toString() + 's后重新获取';

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

    }
    .padding({ top: 48 })
    .height('100%')
    .width('100%')
  }
}
```

## 分析结论

当应用退到后台时，系统会冻结应用的主线程和相关任务。setInterval依赖于主线程的事件循环机制，当应用进入后台后，主线程被冻结，setInterval的回调函数也就无法被触发。

## 修改建议

使用[TextTimer](../harmonyos-references/ts-basic-components-texttimer.md)进行计时，[TextTimer](../harmonyos-references/ts-basic-components-texttimer.md)是ArkUI（方舟UI框架）提供的组件，可以实现后台继续计时的效果。计时器时间最长不超过86400000毫秒（24小时）。

```typescript
@Entry
@Component
struct VerificationCodeTimerPage {
  @State captchaButtonText: string = '获取验证码';
  textTimerController: TextTimerController = new TextTimerController();
  private format: string = 'ss';
  private maxLength: number = 6;
  private strokeWidth: number = 1;

  build() {
    Column() {
      Row() {
        Text('请输入验证码')
          .fontSize(24)
          .fontWeight(FontWeight.Medium);
      }
      .height(32);

      Row() {
        Text('验证码将发送至')
          .fontSize(14)
          .fontColor('#6e6e6e')
          .fontWeight(FontWeight.Regular);
        Text('+86 182******02')
          .fontSize(14)
          .fontColor('#0a59f7')
          .fontWeight(FontWeight.Regular);
      }
      .margin({
        top: 10,
        bottom: 37
      });

      Row() {
        TextInput()
          .backgroundColor(Color.Transparent)
          .width('65%')
          .maxLength(this.maxLength)
          .type(InputType.Number)
          .translate({ x: -12 });
        Row() {

          TextTimer({ isCountDown: true, count: 30000, controller: this.textTimerController })
            .format(this.format)
            .fontColor(Color.Black)
            .fontSize(16)
            .visibility((this.captchaButtonText === '获取验证码' || this.captchaButtonText === '重获验证码') ?
              Visibility.Hidden :
              Visibility.Visible)
            .onTimer((utc: number, elapsedTime: number) => {
              if (elapsedTime >= 30) {
                this.captchaButtonText = '重获验证码';
                this.textTimerController.reset();
              }

            });

          Text(this.captchaButtonText)
            .fontSize(16)
            .fontWeight(FontWeight.Medium)
            .fontColor((this.captchaButtonText === '获取验证码' || this.captchaButtonText === '重获验证码') ?
              '#0a59f7' :
              '#6e6e6e')
            .onClick(() => {
              // 判断是否开始倒计时
              if (this.captchaButtonText === '获取验证码' || this.captchaButtonText === '重获验证码') {
                // 更新验证码按钮文本为剩余秒数
                this.captchaButtonText = 's后重新获取';
                this.textTimerController.start();
              }
            });
        };

      }
      .width('85%');

      Divider()
        .strokeWidth(this.strokeWidth)
        .width('85%')
        .color('#f2f2f2')
        .margin({
          top: 5,
          bottom: 55
        });

      Button('登录/注册')
        .backgroundColor('#0a59f7')
        .fontColor(Color.White)
        .width('85%')
        .height(40);
    }
    .padding({ top: 48 })
    .height('100%')
    .width('100%');
  }
}
```
