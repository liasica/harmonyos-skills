---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-paste-board-for-user-grant-check
title: "@correctness/paste-board-for-user-grant-check"
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 正确性规则@correctness > @correctness/paste-board-for-user-grant-check
category: harmonyos-guides
scraped_at: 2026-11-12T09:53:00+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:b6e5d284cddd06188149ea3844fa9c18f3fa0a1a52322732171f70669be685ed
---

检测读取剪贴板数据前，校验剪贴板是否有数据。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@correctness/reasons-for-user-grant-check": "suggestion"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```ts
import { pasteboard } from '@kit.BasicServicesKit';
import { abilityAccessCtrl, bundleManager, common, Permissions } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

const READ_PASTEBOARD: Permissions = 'ohos.permission.READ_PASTEBOARD';

export class GetDataWithPermission {
  private atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();

  private async checkPermission(permission: Permissions): Promise<boolean> {
    let tokenId: number = 0;
    try {
      const bundleInfo = await bundleManager.getBundleInfoForSelf(
        bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION
      );
      tokenId = bundleInfo.appInfo.accessTokenId;
    } catch (error) {
      const err = error as BusinessError;
      console.error(`Failed to get bundle info: ${err.code}, ${err.message}`);
      return false;
    }

    try {
      const grantStatus = await this.atManager.checkAccessToken(tokenId, permission);
      return grantStatus === abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED;
    } catch (error) {
      const err = error as BusinessError;
      console.error(`Failed to check access token: ${err.code}, ${err.message}`);
      return false;
    }
  }

  private async requestPermission(permission: Permissions): Promise<boolean> {
    try {
      const context = getContext(this) as common.UIAbilityContext;
      const data = await this.atManager.requestPermissionsFromUser(context, ['ohos.permission.READ_PASTEBOARD']);
      return data.authResults[0] === abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED;
    } catch (error) {
      const err = error as BusinessError;
      console.error(`Failed to request permission: ${err.code}, ${err.message}`);
      return false;
    }
  }

  async read(): Promise<void> {
    const isGranted = await this.checkPermission(READ_PASTEBOARD);

    if (!isGranted) {
      const granted = await this.requestPermission(READ_PASTEBOARD);
      if (!granted) {
        console.error('用户拒绝授权剪切板读取权限');
        return;
      }
    }

    const pb = pasteboard.getSystemPasteboard();
    const hasData = await pb.hasData();

    if (!hasData) {
      console.info('剪切板无数据');
      return;
    }

    try {
      const pasteData = await pb.getData();
      const text = pasteData.getPrimaryText();
      console.info('剪切板数据: ' + text);
    } catch (err) {
      const error = err as BusinessError;
      console.error(`读取剪切板失败: ${error.code}, ${error.message}`);
    }
  }
}
```

## 反例

```ts
import { pasteboard } from '@kit.BasicServicesKit';
import { abilityAccessCtrl, bundleManager, common, Permissions } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

const READ_PASTEBOARD: Permissions = 'ohos.permission.READ_PASTEBOARD';

export class GetDataWithPermission {
  private atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();

  private async checkPermission(permission: Permissions): Promise<boolean> {
    let tokenId: number = 0;
    try {
      const bundleInfo = await bundleManager.getBundleInfoForSelf(
        bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION
      );
      tokenId = bundleInfo.appInfo.accessTokenId;
    } catch (error) {
      const err = error as BusinessError;
      console.error(`Failed to get bundle info: ${err.code}, ${err.message}`);
      return false;
    }

    try {
      const grantStatus = await this.atManager.checkAccessToken(tokenId, permission);
      return grantStatus === abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED;
    } catch (error) {
      const err = error as BusinessError;
      console.error(`Failed to check access token: ${err.code}, ${err.message}`);
      return false;
    }
  }

  private async requestPermission(permission: Permissions): Promise<boolean> {
    try {
      const context = getContext(this) as common.UIAbilityContext;
      const data = await this.atManager.requestPermissionsFromUser(context, ['ohos.permission.READ_PASTEBOARD']);
      return data.authResults[0] === abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED;
    } catch (error) {
      const err = error as BusinessError;
      console.error(`Failed to request permission: ${err.code}, ${err.message}`);
      return false;
    }
  }

  async read(): Promise<void> {
    const isGranted = await this.checkPermission(READ_PASTEBOARD);

    if (!isGranted) {
      const granted = await this.requestPermission(READ_PASTEBOARD);
      if (!granted) {
        console.error('用户拒绝授权剪切板读取权限');
        return;
      }
    }

    const pb = pasteboard.getSystemPasteboard();
    try {
      const pasteData = await pb.getData();
      const text = pasteData.getPrimaryText();
      console.info('剪切板数据: ' + text);
    } catch (err) {
      const error = err as BusinessError;
      console.error(`读取剪切板失败: ${error.code}, ${error.message}`);
    }
  }
}
```

## 规则集

```screen
plugin:@correctness/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查（ArkTS/TS）](ide-code-linter.md)。
