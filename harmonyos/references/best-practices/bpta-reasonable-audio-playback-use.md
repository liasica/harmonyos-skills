---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-reasonable-audio-playback-use
title: 后台音频播放合理使用
breadcrumb: 最佳实践 > 功耗 > 应用功耗优化 > 后台任务低功耗 > 后台软件资源合理使用 > 后台音频播放合理使用
category: best-practices
scraped_at: 2026-04-28T08:22:46+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:887ca390efb39a33c3d2cd5622fbcb1464b70b78fb1b04e8642804e5918d6ce6
---

申请音频播放长时任务的应用退到后台后，禁止不写入数据或写入静音数据等恶意行为。

## 约束

系统检测到应用后台行为时，将挂起或清理应用。

## 示例

```
1. import { fileIo as fs } from '@kit.CoreFileKit';
2. // ...

4. const uiContext: UIContext | undefined = AppStorage.get('uiContext');
5. let context = uiContext!.getHostContext()!;

7. async function read() {
8. const bufferSize: number = await audioRenderer.getBufferSize();
9. let path = context.filesDir; // Path of the file

11. const filePath = path + '/voice_call_data.wav'; // Prohibit the file from being played silently
12. try {
13. let file: fs.File = fs.openSync(filePath, fs.OpenMode.READ_ONLY); // Open the file
14. let buf = new ArrayBuffer(bufferSize);
15. let readSize: number = await fs.read(file.fd, buf); // Read the file content
16. } catch (error) {
17. let err = error as BusinessError;
18. hilog.warn(0x000, 'testTag', `openSync or read failed, code=${err.code}, message=${err.message}`);
19. }
20. }
```

[Audio.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/BptaUseSoftware/entry/src/main/ets/pages/Audio.ets#L21-L71)

有关AudioRenderer开发相关接口的使用，详情可以参考[使用AudioRenderer开发音频播放功能](../harmonyos-guides/using-audiorenderer-for-playback.md)。
