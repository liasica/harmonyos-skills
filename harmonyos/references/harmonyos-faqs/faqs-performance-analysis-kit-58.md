---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-58
title: 使用HiLog打印日志是否有长度限制
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > 使用HiLog打印日志是否有长度限制
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:8462a7f2edb3079b38d2357c8bd20862c85fb085b2a910844b2c6d14a560f216
---

使用HiLog进行日志打印时，最多支持4096字节，超出部分将被截断。

利用HiLog封装日志打印工具类，解决日志信息过长的问题。

示例如下：

封装LogUtil类：

```ts
import { hilog } from '@kit.PerformanceAnalysisKit';

const HILOG_MAX_BYTES = 4096;

// Split the string by byte limit.
function splitByByteLimit(str: string, limit: number): string[] {
  const result: string[] = [];
  let start = 0;
  while (start < str.length) {
    let end = start;
    let byteLen = 0;
    while (end < str.length) {
      const code = str.charCodeAt(end);
      let charBytes: number;
      if (code < 0x80) {
        charBytes = 1;
      } else if (code < 0x800) {
        charBytes = 2;
      } else if (code < 0xD800 || code > 0xDFFF) {
        charBytes = 3;
      } else {
        charBytes = 4;
        end++;
      }
      if (byteLen + charBytes > limit) break;
      byteLen += charBytes;
      end++;
    }
    result.push(str.substring(start, end));
    start = end;
  }
  return result;
}

function printSegments(level: string, logTag: string, content: string): void {
  const segments = splitByByteLimit(content, HILOG_MAX_BYTES);
  for (const seg of segments) {
    switch (level) {
      case 'error':
        hilog.error(0x0000, logTag, '%{public}s', seg);
        break;
      case 'debug':
        hilog.debug(0x0000, logTag, '%{public}s', seg);
        break;
      case 'info':
        hilog.info(0x0000, logTag, '%{public}s', seg);
        break;
    }
  }
}

class LogUtil {
  private static instance: LogUtil;

  private constructor() {
  }

  public static getInstance(): LogUtil {
    if (!LogUtil.instance) {
      LogUtil.instance = new LogUtil();
    }
    return LogUtil.instance;
  }

  public logError(logTag: string, content: string) {
    printSegments('error', logTag, content);
  }

  public logDebug(logTag: string, content: string) {
    printSegments('debug', logTag, content);
  }

  public logInfo(logTag: string, content: string) {
    printSegments('info', logTag, content);
  }
}

export default LogUtil;
```

使用：

```screen
import LogUtil from './LogUtilClass';

@Entry
@Component
struct HiLogIsThereALengthLimit {

  build() {
    Row() {
      Column() {
        Button('hilog util')
          .onClick(() => {
            let str = 'Long log content';
            let utilInfo = LogUtil.getInstance();
            utilInfo.logInfo('testTag', str);
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```
