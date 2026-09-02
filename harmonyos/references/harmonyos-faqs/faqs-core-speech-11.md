---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-core-speech-11
title: 语音识别1002200010报错
breadcrumb: FAQ > AI功能开发 > 机器学习 > 基础语音（Core Speech） > 语音识别1002200010报错
category: harmonyos-faqs
scraped_at: 2026-09-02T14:55:00+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:710c9052fff148ea37a7250afcf6b0bae1882f026b0888c66e49e53326c06ba2
---

## 问题现象

语音识别报错，errorCode: 1002200010 errorMessage: Write audio failed because the start listening is failed。

```screen
let ss: fileIo.Stream = fileIo.createStreamSync(cachePath, 'r+'); // 创建文件流
try {
  const bufferSize: number = 1280; // 每次读取的Buffer大小（单位：字节）
  const buf: ArrayBuffer = new ArrayBuffer(bufferSize);
  while (true) {
    let readResult: number = await ss.read(buf); // 异步读取Buffer
    if (readResult <= 0) {
      break;
    } // 文件读取结束
    let validData = new Uint8Array(buf.slice(0, readResult));
    this.asrEngine.writeAudio(this.sessionId, validData);
    await this.countDownLatch(1);
  }
} catch (err) {
  logger.error(TAG, `Failed to read from file. Code: ${err.code}, message: ${err.message}.`);
} finally {
  ss.close(); // 确保流被关闭
}
```

## 背景知识

[语音识别](../harmonyos-guides/speechrecognizer-guide.md)：将一段中文音频信息（中文、中文语境下的英文；短语音模式不超过60s，长语音模式不超过8h）转换为文本，音频信息可以为PCM音频文件或者实时语音。

支持的语种类型：中文普通话。

支持的模型类型：离线。

语音时长：短语音模式不超过60s，长语音模式不超过8h。

## 问题定位

1. 通过调试定位到报错的接口为：writeAudio(sessionId: string, audio: Uint8Array): void。
2. writeAudio的入参audio当前仅支持音频数据长度为640字节或1280字节。建议每次发送音频调用间隔为20ms（传输音频长度为640字节）或40ms（传输音频长度为1280字节），具体可以参考官方文档的[参数说明](../harmonyos-references/hms-ai-speechrecognizer.md#writeaudio)。通过打印每条数据长度，发现报错的数据长度不是640的整数倍。日志如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/srqq8620TTSKuUXzywmJog/zh-cn_image_0000002628394836.png "点击放大")

## 分析结论

调用writeAudio接口的入参audio分段后的最后一段长度不满足640字节或1280字节导致触发onError()回调，但功能实现并无影响，仅最后一段的音频报错被截断。

## 修改建议

目前有两种修复方式：

1. audio分段后的最后一段的音频最多80ms，如果80ms并不影响最终结果，可以忽略此报错。
2. 如果希望保留audio分段后的最后一段的运行结果，可以通过将音频补齐到640字节或者1280字节。例如'问题现象'中所展示的代码片段中设置了1280字节，就需要将音频补齐到1280字节。

补齐后日志如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/pUD_--TOQaKYUVdOWublSA/zh-cn_image_0000002628554732.png "点击放大")
