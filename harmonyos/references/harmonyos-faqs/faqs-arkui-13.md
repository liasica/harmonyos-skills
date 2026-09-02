---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-13
title: TextInput组件获取焦点的几种场景
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > TextInput组件获取焦点的几种场景
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:58+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:e2669dd3d6e370abea1397a90d9907adde0534d86358bd7e77ed747a6faee071
---

* 场景一：TextInput[主动获焦/失焦](../harmonyos-guides/arkts-common-events-focus-event.md#主动获焦失焦)。

  调用focusControl.requestFocus接口可以主动让焦点转移至参数指定的组件上。可参考如下代码：

  ```typescript
  // xxx.ets
  @Entry
  @Component
  struct TextInputExample {
    build() {
      Row() {
        Column() {
          Button('The second focus acquisition')
            .onClick(() => {
              focusControl.requestFocus('BBB'); // Get focus on the second input box
            })

          TextInput({ placeholder: 'Please enter the content.' })
            .showUnderline(true)
            .width(380)
            .height(60)
            .id('AAA')
          TextInput({ placeholder: 'Please enter the content.' })
            .showUnderline(true)
            .width(380)
            .height(60)
            .id('BBB')
        }
        .width('100%')
      }
      .height('100%')
    }
  }
  ```
* 场景二：页面初次构建完成时，使第二个TextInput获取[默认焦点](../harmonyos-guides/arkts-common-events-focus-event.md#默认焦点)。

  设置defaultFocus属性，defaultFocus可以使绑定的组件成为页面创建后首次获焦的焦点。可参考如下代码：

  ```typescript
  // xxx.ets
  @Entry
  @Component
  struct TextInputExample {
    build() {
      Row() {
        Column() {
          TextInput({ placeholder: 'Please enter the content.' })
            .showUnderline(true)
            .width(380)
            .height(60)

          TextInput({ placeholder: 'Please enter the content.' })
            .showUnderline(true)
            .defaultFocus(true) // When the page is first opened, this TextInput gets focus
            .width(380)
            .height(60)
        }
        .width('100%')
      }
      .height('100%')
    }
  }
  ```
* 场景三：页面初次构建完成时，使TextInput获取焦点且不弹出键盘。

  设置enableKeyboardOnFocus(false)，在页面进入后不弹出键盘。可参考如下代码：

  ```typescript
  // xxx.ets
  @Entry
  @Component
  struct TextInputExample {
    build() {
      Row() {
        Column() {
          TextInput({ placeholder: 'Please enter the content.' })
            .defaultFocus(true) // When the page is first opened, this TextInput gets focus
            .enableKeyboardOnFocus(false) // Is TextInput bound to an input method when focusing through methods other than clicking.
            .placeholderColor(Color.Grey)
            .placeholderFont({ size: 14, weight: 400 })
            .caretColor(Color.Blue)
            .width('95%')
            .height(40)
            .margin(20)
        }
        .width('100%')
      }
      .height('100%')
    }
  }
  ```
* 场景四：页面初次构建完成时，使TextInput不获取焦点且不弹出键盘。

  TextInput默认不获取焦点，不弹出键盘。可参考如下代码：

  ```typescript
  // xxx.ets
  @Entry
  @Component
  struct TextInputExample {
    build() {
      Column() {
        TextInput({ placeholder: 'Please enter the content.' })
      }
      .width('100%')
    }
  }
  ```
