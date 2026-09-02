---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-access-control-10
title: 在系统设置修改了应用权限，应用能否监听到权限变化
breadcrumb: FAQ > 系统开发 > 安全 > 程序访问控制 > 在系统设置修改了应用权限，应用能否监听到权限变化
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:34+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:899145e5e8778dc6ea23a92a45f4057fc2f88fa368ed5055cf66ebbfe7813f51
---

使用[on](../harmonyos-references/js-apis-abilityaccessctrl.md#on18)可以监听应用权限变化，示例代码中监听的是ohos.permission.APPROXIMATELY\_LOCATION权限变化，需要在module.json5进行相应的权限声明，参考代码如下：

```typescript
import { abilityAccessCtrl, Permissions } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  aboutToAppear(): void {
    let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
    let permissionList: Array<Permissions> = ['ohos.permission.APPROXIMATELY_LOCATION'];
    try {
      atManager.on('selfPermissionStateChange', permissionList, (data: abilityAccessCtrl.PermissionStateChangeInfo) => {
        console.info('receive permission state change, data:' + JSON.stringify(data));
      });
    } catch (err) {
      console.error(`catch err->${JSON.stringify(err)}`);
    }
  }

  build() {
    // ...
  }
}
```
