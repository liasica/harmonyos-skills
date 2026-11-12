---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-avplayernotrelease
title: AVPlayerNotRelease
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Scanner代码检查规则 > ArkTS代码检查规则 > AVPlayerNotRelease
category: harmonyos-guides
scraped_at: 2026-11-12T09:53:00+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:fc1f8fc30541f77839cad17307614897157fc8bb2670920f2065cd95ce65bb60
---

通过media.createAVPlayer()方法创建的AVPlayer实例，需及时调用release()方法释放实例，避免因多实例导致内存消耗过大，进而引发系统终止应用的风险。

## 规则配置

```screen
// rules.json
{
  "rules": {
    "arkts": {
      "ResourceLeak": [
        {
          "ruleId": "AVPlayerNotRelease",
          "severity": "error",
          "skip": false
        }
      ]
    }
  }
}
```

## 正例

```ts
import UIAbility from '@ohos.app.ability.UIAbility';
import media from '@ohos.multimedia.media';
import { window } from '@kit.ArkUI';

/**
 * 正例：正确释放资源
 */
export default class TestRelease extends UIAbility {
  private avPlayer: media.AVPlayer | null = null;
  async onWindowStageCreate(windowStage: window.WindowStage): Promise<void> {
    this.avPlayer = await media.createAVPlayer();
  }
  async onDestroy(): Promise<void> {
    this.avPlayer?.release();
  }
}
```

## 反例

```ts
import UIAbility from '@ohos.app.ability.UIAbility';
import media from '@ohos.multimedia.media';
import { window } from '@kit.ArkUI';

/**
 * 反例：未释放资源
 */
export class TestNotRelease extends UIAbility {
  private avPlayer: media.AVPlayer | null = null;
  async onWindowStageCreate(windowStage: window.WindowStage): Promise<void> {
    this.avPlayer = await media.createAVPlayer(); // leak
  }
}
```

Code Scanner代码检查规则的配置指导请参考[1.6.3 代码检查工具（codescanner）](ide-command-line-codescanner.md)
