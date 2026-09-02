---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-49
title: 如何解决日志内容过大时控制台打印被截断的问题
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > 如何解决日志内容过大时控制台打印被截断的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:50+08:00
doc_updated_at: 2026-08-05
content_hash: sha256:e3f197f0be1cdfb01daaf486fd81f26255bc1c7ff82f00060f45132383a6d6fc
---

## 问题现象

控制台日志输出内容被截断，后半部分无法打印。以下文日志为例（单个文本16个字符，一共拼接500次，累计8000字符），使用hilog进行打印时截断（只打印到第233次）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/sLLx-V09TameY75qUmFwsQ/zh-cn_image_0000002689423443.png "点击放大")

## 背景知识

日志打印最多打印4096字节，超出限制文本将被截断，详见[约束与限制](../harmonyos-guides/hilog-guidelines-arkts.md#约束与限制)。

## 解决方案

利用hilog封装log工具类检查日志长度，超出特定长度（比如：1024字节）就分段打印。

示例代码参考如下：

```ts
import hilog from '@ohos.hilog';
import { util } from '@kit.ArkTS';

class LogUtil {
  private static instance: LogUtil;
  private static DOMAIN: number = 0x0000;

  private constructor() {
    // 私有构造函数，防止外部实例化
  }

  public static getInstance(): LogUtil {
    if (!LogUtil.instance) {
      LogUtil.instance = new LogUtil();
    }
    return LogUtil.instance;
  }

  // error、debug参照info即可
  public info(logTag: string, content: string) {
    const maxSize = 1024;
    let textEncoder = new util.TextEncoder('utf-8');
    let result = textEncoder.encodeInto(content);
    if (result.byteLength <= maxSize) {
      // 长度小于等于限制直接打印
    } else {
      while (result.byteLength > maxSize) {
        // 循环分段打印
        let logContent = content.substring(0, maxSize);
        content = content.replace(logContent, '');
        result = textEncoder.encodeInto(content);
        hilog.info(LogUtil.DOMAIN, logTag, '%{public}s', logContent);
        // 打印剩余日志
      }
    }
    hilog.info(LogUtil.DOMAIN, logTag, '%{public}s', content);
  }
}

export default LogUtil;

@Entry
@Component
struct LongLogPrint {
  private oneContent: string = 'LongLogPrint';
  private logContent: string = '';

  aboutToAppear(): void {
    for (let i = 0; i < 500; i++) {
      this.logContent += this.oneContent + '[' + i + '],';
    }
  }

  build() {
    Row() {
      Column() {
        Button('Log Test')
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            LogUtil.getInstance().info('Long Log', this.logContent);
          });
      }
      .width('100%');
    }
    .height('100%');
  }
}
```

修改后日志能打印完整：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/NMwXfVnWSDGy6KBfVdBzFg/zh-cn_image_0000002659467164.png "点击放大")
