---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-deprecate-api-check
title: "@compatibility/deprecate-api-check"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 兼容性规则@compatibility > @compatibility/deprecate-api-check
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:53+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:3bf71ad5fd70ea6da10ef78daa12ee2f03fbdb1fa1f66fe60f0a23f72eec3377
---

在开发中避免使用废弃的API接口。

## 规则配置

```json5
// code-linter.json5
{
  "rules": {
    "@compatibility/deprecate-api-check": "suggestion"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
import media from '@ohos.multimedia.media';

function nonDeprecatedApi(): void {
  media.createAVPlayer().then((avPlayer) => {
    avPlayer.on('stateChange', () => {});
    avPlayer.play();
  });
}
```

## 反例

```screen
import { media } from '@kit.MediaKit';

function deprecatedApi(): void {
  let audioPlayer: media.AudioPlayer = media.createAudioPlayer ();
  audioPlayer.src = 'https://example.com/audio.mp3';
  audioPlayer.play ();
  audioPlayer.release ();
}
```

## 规则集

```screen
plugin:@compatibility/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
