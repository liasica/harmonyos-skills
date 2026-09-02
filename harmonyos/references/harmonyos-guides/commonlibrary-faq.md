---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/commonlibrary-faq
title: 基础库常见问题
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS基础类库 > 基础库常见问题
category: harmonyos-guides
scraped_at: 2026-09-02T14:49:45+08:00
doc_updated_at: 2026-06-12
content_hash: sha256:6ea1d9c17672c446e7025e08f45dd6da46dfb3250382d0572cd28adab8d6dad8
---

## 解析大文件xml发生内存溢出（Out of Memory）

由于ArkTS侧提供的XML解析接口暂不支持流式解析模式，建议通过Native工程调用第三方C/C++库来实现。推荐使用**libxml2**库，该库具有成熟稳定、性能优越的特点，能够支持SAX等流式解析方式，有效降低内存占用。

具体实施步骤如下：

1. **创建Native工程**：在HarmonyOS项目中创建C++模块。
2. **集成libxml2**：下载并配置libxml2库源码或预编译库，在CMakeLists.txt中进行引用。
3. **编写解析代码**：使用libxml2提供的API实现流式解析逻辑。
4. **XML对象处理**：当XML文件大小超过100MB时，建议在Native侧处理。

关于如何在ArkTS侧引用编译生成的三方so库，请参考文档：[如何在ArkTS侧引用其他三方so库](../harmonyos-faqs/faqs-ndk-21.md)。

libxml2库支持的回调函数主要如下所示：

| 回调函数指针 | 触发时机 | 用途 |
| --- | --- | --- |
| startDocument | 文档开始时 | 初始化环境，分配资源。 |
| endDocument | 文档结束时 | 释放资源，打印统计信息。 |
| startElement | 读到开始标签（如<tag>） | 获取标签名及其属性。 |
| endElement | 读到结束标签（如</tag>） | 处理标签结束逻辑，如出栈。 |
| characters | 读到标签间的文本内容 | 处理文本数据（注意可能被多次调用）。 |

代码示例：

```c
// 用户自定义数据
ParseContext context;

// 初始化SAX Handler结构体
xmlSAXHandler SAXHandler = { 0 };

// 绑定回调函数，用于在解析过程中处理XML数据
SAXHandler.startDocument = startDocument;
SAXHandler.endDocument = endDocument;
SAXHandler.startElement = startElement;
SAXHandler.endElement = endElement;
SAXHandler.characters = characters;

// 解析文件
// 用户自定义数据指针
int ret = xmlSAXUserParseFile(&SAXHandler, &context, xmlFileName);

if (ret != 0) {
    printf("Failed to parse XML file.\n");
    return 1;
}

// 清理libxml2全局状态
xmlCleanupParser();
```

## 定时器被误删除

由于定时器ID为进程共享，是从0开始的，开发者误操作容易导致定时器被删除。

例如以下场景：

```ts
export class testClass {
    // 初始值设置为0
    private timeoutId: number = 0;
    private intervalId: number = 0;

    // 在某些情况下没有调用setTimeout设置定时器就调用了clearAnimation函数删除了定时器，就会导致timeoutId为0的定时器被删除
    clearAnimation(): void {
        clearInterval(this.intervalId);
        clearTimeout(this.timeoutId);
    }
}
```

可以通过以下方法快速定位：

重写globalThis.clearTimeout函数，实现在调用clearTimeout函数时打印调用栈，快速定位定时器是在哪里被删除的。

调用顺序为先调用clearTimeout.ts文件中的test()函数，再调用TimerTest.ets文件中testClass类的clearAnimation()函数。

示例代码：

```ts
// 自定义TS文件clearTimeout.ts

// test函数需要在程序调用clearTimeout函数之前调用
export function test() {
    // 完全兼容原始 clearTimeout 类型
    const origClear = globalThis.clearTimeout;
    globalThis.clearTimeout = (...args: any[]) => {
        const timeoutId = args[0];

        // 检查所有可能的 timerId = 0 的情况
        if (timeoutId === 0 || timeoutId === "0") {
            console.info("清除 timerId = 0 !", new Error().stack);
            // 触发断点
            debugger;
        }

        // 使用 apply 确保正确传递所有参数
        return origClear.apply(this, args);
    }
}
```

```ts
// 自定义ets文件TimerTest.ets

export class testClass {
    // 初始值设置为0
    private timeoutId: number = 0;
    private intervalId: number = 0;

    // 在某些情况下没有调用setTimeout设置定时器就调用了clearAnimation函数删除了定时器，就会导致timeoutId为0的定时器被删除
    clearAnimation(): void {
        clearInterval(this.intervalId);
        clearTimeout(this.timeoutId);
    }
}
```

```ts
import { test } from './clearTimeout';
import { testClass } from './TimerTest';

@Entry
@Component
struct Index {
    @State message: string = 'Hello World';

    build() {
      Row() {
        Column() {
          Text(this.message)
            .fontSize(50)
            .fontWeight(FontWeight.Bold)
            .onClick(() => {
                test();
                let testCase = new testClass();
                testCase.clearAnimation();
                this.message = 'success';
            })
        }
        .width('100%')
      }
      .height('100%')
    }
}
```

## Base64编码规则

Base64编码使用一组特定的64个字符来表示二进制数据。这64个字符包括大写字母A-Z、小写字母a-z、数字0-9，以及符号"+"和"/"。在某些情况下，还会使用"="作为填充字符。Base64编码将原始数据按每3个字节分组，每组3个字节转换为4个Base64字符。

Base64编码表如下：

| 索引 | 字符 | 索引 | 字符 | 索引 | 字符 | 索引 | 字符 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | 16 | Q | 32 | g | 48 | w |
| 1 | B | 17 | R | 33 | h | 49 | x |
| 2 | C | 18 | S | 34 | i | 50 | y |
| 3 | D | 19 | T | 35 | j | 51 | z |
| 4 | E | 20 | U | 36 | k | 52 | 0 |
| 5 | F | 21 | V | 37 | l | 53 | 1 |
| 6 | G | 22 | W | 38 | m | 54 | 2 |
| 7 | H | 23 | X | 39 | n | 55 | 3 |
| 8 | I | 24 | Y | 40 | o | 56 | 4 |
| 9 | J | 25 | Z | 41 | p | 57 | 5 |
| 10 | K | 26 | a | 42 | q | 58 | 6 |
| 11 | L | 27 | b | 43 | r | 59 | 7 |
| 12 | M | 28 | c | 44 | s | 60 | 8 |
| 13 | N | 29 | d | 45 | t | 61 | 9 |
| 14 | O | 30 | e | 46 | u | 62 | + |
| 15 | P | 31 | f | 47 | v | 63 | / |

由此可见Base64是基于64个可打印字符来表示二进制数据的编解码方式。将二进制数据转为字符串（ASCII码），方便数据传输和加解密保护。

它的编码实现原理为：

将需要编码的字符串转换成二进制序列，然后按每6个二进制位为一组，分成若干组，如果不足6位，则低位补0。每6位组成一个新的字节，高位补00，构成一个新的二进制序列，最后根据Base64索引表中的值找到对应的字符。

例如字符串“ABC”，我们进行Base64编码，最后结果会是QUJD：

| 原始字符 | A | B | C | － |
| --- | --- | --- | --- | --- |
| ASCII编码 | 65 | 66 | 67 | － |
| 二进制位 | 01000001 | 01000010 | 01000011 | － |
| 编码转换 | 010000 | 010100 | 001001 | 000011 |
| base64索引值 | 16 | 20 | 9 | 3 |
| base64字符 | Q | U | J | D |

若原始字符串长度不是3的倍数，编码后末尾用“=”填充，使编码后的Base64字符串最终长度为4的倍数，以满足转换后Base64长度要求。

例如字符串“AB”转换后为“QUI”为了凑齐4字节，需要在末尾补充“=”：

| 原始字符 | A | B | － | － |
| --- | --- | --- | --- | --- |
| ASCII编码 | 65 | 66 | － | － |
| 二进制位 | 01000001 | 01000010 | － | － |
| 编码转换（不足6位补0） | 010000 | 010100 | 001000 | － |
| base64索引值 | 16 | 20 | 8 | － |
| base64字符 | Q | U | I | = |
